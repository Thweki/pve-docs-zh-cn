"""Offline regressions for cached API translation fragment parsing."""
import importlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))


class FragmentCacheTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for name in ('bs4', 'markdownify'):
            try:
                importlib.import_module(name)
            except ImportError as error:
                raise unittest.SkipTest(f'{name} unavailable: {error}') from error
        cls.render = importlib.import_module('render')

    def setUp(self):
        self.units = {
            'one': {'text': 'Use ⟦0⟧ now.', 'fragments': ['<code>qm</code>']},
            'two': {'text': 'Other text', 'fragments': []},
        }
        self.translations = {'one': '使用 ⟦0⟧ & 检查。'}
        for name, value in (('UNITS', self.units), ('TRANSLATIONS', self.translations)):
            patcher = patch.object(self.render, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)
        # Also permit the unoptimized implementation for the equivalence tests.
        if hasattr(self.render, '_fragment_text'):
            self.render._fragment_text.cache_clear()
            self.addCleanup(self.render._fragment_text.cache_clear)

    def test_repeated_fragments_parse_once_across_schema_calls(self):
        schema = [{'_description_i18n': 'one'},
                  {'nested': {'_title_i18n': 'one', '_verbose_description_i18n': 'one'}}]
        with patch.object(self.render, 'BeautifulSoup', wraps=self.render.BeautifulSoup) as parser:
            first = self.render.schema_translated(schema)
            second = self.render.schema_translated({'_description_i18n': 'one'})
        self.assertEqual(parser.call_count, 1)
        text = '使用 qm & 检查。'
        self.assertEqual(first, [{'description': text},
                                {'nested': {'title': text, 'verbose_description': text}}])
        self.assertEqual(second, {'description': text})

    def test_schema_structure_fallback_and_independent_results(self):
        schema = {'properties': [{'type': 'string', 'default': 3, 'optional': False,
                                  '_description_i18n': 'one'},
                                 {'_title_i18n': 'two', 'enum': ['a', 'b'], 'extra': None}],
                  'description': 'Unmarked text', '_unknown_i18n': 'ignored'}
        expected = {'properties': [{'type': 'string', 'default': 3, 'optional': False,
                                    'description': '使用 qm & 检查。'},
                                   {'title': 'Other text', 'enum': ['a', 'b'], 'extra': None}],
                    'description': 'Unmarked text'}
        first = self.render.schema_translated(schema)
        self.assertEqual(first, expected)
        first['properties'][0]['description'] = 'changed'
        first['properties'][1]['enum'].append('c')
        self.assertEqual(self.render.schema_translated(schema), expected)
        self.assertEqual(schema['properties'][0]['_description_i18n'], 'one')
        self.assertEqual(schema['properties'][1]['enum'], ['a', 'b'])

    def test_translation_and_fragment_edits_are_visible(self):
        schema = {'_description_i18n': 'one'}
        self.render.schema_translated(schema)
        self.translations['one'] = '运行 ⟦0⟧。'
        self.assertEqual(self.render.schema_translated(schema)['description'], '运行 qm。')
        self.units['one']['fragments'][0] = '<code>pct</code>'
        self.assertEqual(self.render.schema_translated(schema)['description'], '运行 pct。')
        del self.translations['one']
        self.assertEqual(self.render.schema_translated(schema)['description'], 'Use pct now.')

    def test_cache_is_bounded_and_eviction_reparses(self):
        cache = self.render._fragment_text
        limit = cache.cache_info().maxsize
        self.assertEqual(limit, 1024)
        cache('<b>oldest</b>')
        for index in range(limit):
            cache(f'<b>{index}</b>')
        self.assertEqual(cache.cache_info().currsize, limit)
        misses = cache.cache_info().misses
        self.assertEqual(cache('<b>oldest</b>'), 'oldest')
        self.assertEqual(cache.cache_info().misses, misses + 1)


if __name__ == '__main__':
    unittest.main()
