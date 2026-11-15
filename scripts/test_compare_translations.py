"""Offline fixtures for the public translation-map comparison CLI."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from compare_translations import compare


SCRIPT = Path(__file__).with_name('compare_translations.py')
A, B, C, D = (f'u{n:020x}' for n in range(4))


def unit(key, text='Source text', fragments=None):
    return {'id': key, 'text': text, 'fragments': fragments or []}


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.before = self.root / 'before'
        self.after = self.root / 'after'
        self.units = {A: unit(A), B: unit(B, 'Use ⟦0⟧', ['--help'])}
        self.translations = {A: '原文', B: '使用 ⟦0⟧'}
        for root in (self.before, self.after):
            self.write(root, self.units, self.translations)

    def write(self, root, units, translations):
        directory = root / 'translations'
        directory.mkdir(parents=True, exist_ok=True)
        for name, data in (('units.json', units), ('zh-CN.json', translations)):
            (directory / name).write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')

    def cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(SCRIPT),
                               str(self.before), str(self.after), *args],
                              capture_output=True, text=True, encoding='utf-8', check=False)

    def test_equal_maps_ignore_serialization_and_key_order(self):
        reordered = {key: dict(reversed(list(value.items())))
                     for key, value in reversed(list(self.units.items()))}
        self.write(self.after, reordered, dict(reversed(list(self.translations.items()))))
        path = self.after / 'translations/units.json'
        path.write_text(json.dumps(reordered, indent=4), encoding='utf-8')
        result = self.cli('--check')
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertFalse(report['has_changes'])
        for field in ('sources', 'translations'):
            self.assertEqual(report[field], {'added': [], 'removed': [], 'changed': [],
                                             'unchanged_count': 2})

    def test_source_additions_removals_and_translation_edits_are_independent(self):
        self.write(self.after, {B: self.units[B], D: unit(D), C: unit(C)},
                   {B: '采用 ⟦0⟧', C: '新增'})
        report = compare(self.before, self.after)
        self.assertTrue(report['has_changes'])
        self.assertEqual(report['sources'], {'added': [C, D], 'removed': [A],
                                             'changed': [], 'unchanged_count': 1})
        self.assertEqual(report['translations'], {'added': [C], 'removed': [A],
                                                  'changed': [B], 'unchanged_count': 0})
        self.assertEqual(report['coverage']['after']['missing'], [D])

    def test_source_text_fragments_and_translation_can_change_at_same_id(self):
        changed = copy.deepcopy(self.units)
        changed[A]['text'] = 'New source text'
        changed[B]['fragments'] = ['--version']
        self.write(self.after, changed, {A: '新原文', B: self.translations[B]})
        report = compare(self.before, self.after)
        self.assertEqual(report['sources']['changed'], [A, B])
        self.assertEqual(report['translations']['changed'], [A])

    def test_translation_whitespace_change_is_visible(self):
        self.write(self.after, self.units, {**self.translations, A: '原文 '})
        report = compare(self.before, self.after)
        self.assertEqual(report['translations']['changed'], [A])
        self.assertEqual(report['sources']['changed'], [])

    def test_partial_maps_report_blank_missing_and_orphaned(self):
        self.write(self.after, {**self.units, C: unit(C)}, {A: ' \n\t', D: '旧译文'})
        report = compare(self.before, self.after)
        self.assertEqual(report['coverage']['after'], {
            'unit_count': 3, 'translation_count': 2, 'missing': [A, B, C], 'orphaned': [D]})
        self.assertEqual(report['coverage']['before'], {
            'unit_count': 2, 'translation_count': 2, 'missing': [], 'orphaned': []})

    def test_empty_maps_and_identical_incomplete_maps(self):
        for units in ({}, self.units):
            with self.subTest(units=len(units)):
                for root in (self.before, self.after):
                    self.write(root, units, {})
                report = compare(self.before, self.after)
                self.assertFalse(report['has_changes'])
                self.assertEqual(report['coverage']['after']['missing'], sorted(units))

    def test_cli_is_deterministic_read_only_and_ignores_work(self):
        work = self.after / 'work'
        work.mkdir()
        (work / 'units.json').write_text('invalid ignored local data', encoding='utf-8')
        original = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        first, second = self.cli(), self.cli()
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        self.assertNotIn(str(self.root), first.stdout)
        self.assertNotIn('原文', first.stdout)
        self.assertNotIn('--help', first.stdout)
        self.assertEqual(original, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_cli_differences_exit_zero_by_default_and_one_with_check(self):
        self.write(self.after, self.units, {**self.translations, A: '修改'})
        normal, checked = self.cli(), self.cli('--check')
        self.assertEqual(normal.returncode, 0, normal.stderr)
        self.assertEqual(checked.returncode, 1, checked.stderr)
        self.assertEqual(normal.stdout, checked.stdout)
        self.assertTrue(json.loads(checked.stdout)['has_changes'])

    def test_cli_invalid_input_exits_two_without_partial_report_or_content(self):
        path = self.after / 'translations/zh-CN.json'
        path.write_text('{"private fixture sentinel": invalid}', encoding='utf-8')
        result = self.cli('--check')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, '')
        self.assertIn('after:', result.stderr)
        self.assertNotIn('private fixture sentinel', result.stderr)
        self.assertNotIn(str(self.root), result.stderr)

    def test_missing_and_non_utf8_inputs(self):
        path = self.before / 'translations/units.json'
        path.unlink()
        with self.assertRaisesRegex(ValueError, 'before: cannot read units.json'):
            compare(self.before, self.after)
        path.write_bytes(b'\xff')
        with self.assertRaisesRegex(ValueError, 'before: cannot read units.json'):
            compare(self.before, self.after)

    def test_duplicate_keys_rejected_including_nested_records(self):
        for name, content in (
                ('zh-CN.json', f'{{"{A}": "one", "{A}": "two"}}'),
                ('units.json', f'{{"{A}": {{"id": "{A}", "text": "one",'
                               ' "text": "two", "fragments": []}}')):
            with self.subTest(name=name):
                self.write(self.after, self.units, self.translations)
                (self.after / 'translations' / name).write_text(content, encoding='utf-8')
                with self.assertRaisesRegex(ValueError, 'unambiguous UTF-8 JSON'):
                    compare(self.before, self.after)

    def test_invalid_map_shapes_and_records(self):
        for units, translations in (
                ([], {}), ({}, []), ({'bad-id': unit(A)}, {}),
                ({A: unit(B)}, {}), ({A: {'id': A, 'text': 'missing fragments'}}, {}),
                ({A: unit(A, text=123)}, {}), ({A: unit(A, fragments=[42])}, {}),
                ({A: []}, {}), (self.units, {A: None}), (self.units, {A: 123}),
                (self.units, {'bad-id': 'text'})):
            with self.subTest(units=units, translations=translations):
                self.write(self.after, units, translations)
                with self.assertRaises(ValueError):
                    compare(self.before, self.after)


if __name__ == '__main__':
    unittest.main()
