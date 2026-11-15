"""Small, offline regression cases; run with unittest discovery (see README)."""
from __future__ import annotations

import copy
import hashlib
import importlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

from scripts import export_pdf

FIXTURES = Path(__file__).parent / 'fixtures/pdf'


def dependency(name):
    try:
        return importlib.import_module(name)
    except (ImportError, OSError) as error:
        message = f'{name} unavailable: {error}'
        if os.environ.get('PVE_PDF_REQUIRE_DEPS') == '1':
            raise AssertionError(message) from error
        raise unittest.SkipTest(message) from error


class PreprocessingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = dependency('lxml.html')

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)

    def test_tables_details_and_chapter_targets(self):
        source = FIXTURES / 'tables.html'
        original = source.read_bytes()
        prepared, report = export_pdf.prepare_html(source, 'Fixture title', self.work)
        tree = self.html.document_fromstring(prepared)
        self.assertEqual(report['tables_as_paginated_records'], 2)
        self.assertEqual(report['two_column_api_parameter_tables'], 1)
        self.assertEqual(tree.xpath('//*[@id="parameters"]')[0].tag, 'table')
        self.assertIn('pdf-api-parameters', tree.xpath('//*[@id="parameters"]')[0].get('class'))
        record = tree.xpath('//*[@id="long-code"]')[0]
        self.assertEqual(record.tag, 'div')
        self.assertEqual(record.get('class'), 'pdf-record-table')
        self.assertEqual(record.tail.strip(), '表格后的直接文本不能丢失。')
        self.assertEqual(record.xpath('./caption/text()'), ['多行代码表'])
        self.assertEqual(record.xpath('.//pre/code/text()'),
                         self.html.fromstring(original).xpath('//*[@id="long-code"]//pre/code/text()'))
        for marker in ('完整字段', '页脚字段必须保留', '配置'):
            self.assertIn(marker, export_pdf.text_content(record))
        self.assertEqual(tree.xpath('//*[@id="nested"]')[0].tag, 'div')
        self.assertEqual(tree.xpath('//*[@id="inner"]')[0].tag, 'table')
        self.assertFalse(tree.xpath('//details|//summary|//script|//style'))
        self.assertEqual(tree.xpath('//*[@class="pdf-details-title"]/text()'), ['展开说明'])
        self.assertIn('折叠内容必须保留', export_pdf.text_content(tree))
        self.assertEqual([item['id'] for item in report['chapter_targets']],
                         ['fixture-tables', 'pdf-chapter-2'])
        self.assertEqual(tree.xpath('//*[@class="pdf-toc"]//a/@href'),
                         ['#fixture-tables', '#pdf-chapter-2'])
        self.assertEqual(report['source_sha256'], hashlib.sha256(original).hexdigest())
        self.assertEqual(source.read_bytes(), original)

    def test_conversion_thresholds(self):
        for content, expected in [('x' * 900, 0), ('x' * 901, 1),
                                  ('<pre>' + '\n'.join(['x'] * 14) + '</pre>', 0),
                                  ('<pre>' + '\n'.join(['x'] * 15) + '</pre>', 1)]:
            with self.subTest(length=len(content), converted=expected):
                source = self.work / 'boundary.html'
                source.write_text('<main class="book-content"><section class="book-chapter">'
                                  '<h1>边界</h1><table id="boundary"><tr><td>' + content +
                                  '</td></tr></table></section></main>', encoding='utf-8')
                prepared, report = export_pdf.prepare_html(source, 'Boundary', self.work)
                self.assertEqual(report['tables_as_paginated_records'], expected)
                node = self.html.fromstring(prepared).xpath('//*[@id="boundary"]')[0]
                self.assertEqual(node.tag, 'div' if expected else 'table')

    def test_invalid_book_structure(self):
        for markup, message in [('<main/>', 'book-content'),
                                ('<main class="book-content"/>', 'book-chapter'),
                                ('<main class="book-content"><section class="book-chapter"/></main>',
                                 'without H1')]:
            with self.subTest(message=message):
                source = self.work / 'invalid.html'
                source.write_text(markup, encoding='utf-8')
                with self.assertRaisesRegex(ValueError, message):
                    export_pdf.prepare_html(source, 'Invalid', self.work)


class SectionTextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = dependency('lxml.html')

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        prepared, self.report = export_pdf.prepare_html(FIXTURES / 'render.html', 'Smoke', self.work)
        chapters = self.html.fromstring(prepared).xpath('//section[@class="book-chapter"]')
        self.texts = [export_pdf.text_content(chapter) for chapter in chapters]
        self.pages = ['Cover', 'Contents ' + self.texts[1], *self.texts]
        self.report['chapter_pages'] = {'render-tables': 3, 'render-short': 4}

    def check(self, pages):
        export_pdf.check_section_text(self.work / 'prepared.html', pages, self.report)

    def test_whitespace_and_page_furniture_are_allowed(self):
        self.check(['Header\n' + re.sub(r'\s+', '\n ', text) + '\nFooter' for text in self.pages])
        self.assertEqual(len(self.report['section_text_checks']), 2)
        self.assertTrue(all(item['text_preserved_in_order'] for item in self.report['section_text_checks']))

    def test_chapter_spanning_pages_is_checked_in_full(self):
        split = self.pages[2].index('row30')
        pages = [*self.pages[:2], self.pages[2][:split] + '\nPage footer',
                 'Repeated header\n' + self.pages[2][split:], self.pages[3]]
        self.report['chapter_pages']['render-short'] = 5
        self.check(pages)
        self.assertEqual(self.report['section_text_checks'][0]['last_page'], 4)
        pages[3] = pages[3].replace('CODE-END', '')
        with self.assertRaisesRegex(AssertionError, 'render-tables.*lost or reordered text'):
            self.check(pages)

    def test_small_section_loss_cannot_hide_in_total_or_toc(self):
        pages = self.pages.copy()
        pages[-1] = '短节'
        # This loss passes the previous global 95% length check, even before TOC text.
        self.assertGreater(len(''.join(pages[2:])), len(''.join(self.texts)) * .95)
        with self.assertRaisesRegex(AssertionError, 'render-short.*lost or reordered text'):
            self.check(pages)

    def test_missing_table_body_middle_or_tail_is_rejected(self):
        for marker in ('TABLE-CELL', 'row30', 'CODE-END', 'OMEGA-TAIL'):
            with self.subTest(marker=marker):
                pages = self.pages.copy()
                pages[2] = pages[2].replace(marker, '')
                with self.assertRaisesRegex(AssertionError, 'render-tables.*lost or reordered text'):
                    self.check(pages)

    def test_reordered_body_is_rejected(self):
        pages = self.pages.copy()
        pages[2] = pages[2].replace('row30\nrow31', 'row31\nrow30')
        with self.assertRaisesRegex(AssertionError, 'lost or reordered text'):
            self.check(pages)

    def test_missing_or_reordered_chapter_pages_are_rejected(self):
        for starts in ({'render-tables': 3}, {'render-tables': 4, 'render-short': 3},
                       {'render-tables': 3, 'render-short': 5}):
            with self.subTest(starts=starts):
                self.report['chapter_pages'] = starts
                with self.assertRaisesRegex(AssertionError, 'chapter pages'):
                    self.check(self.pages)


class FontEmbeddingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dependency('pypdf')

    def test_unembedded_simple_and_descendant_fonts_are_rejected(self):
        from pypdf import PdfWriter
        from pypdf.generic import ArrayObject, DictionaryObject, NameObject

        for composite in (False, True):
            with self.subTest(composite=composite), tempfile.TemporaryDirectory() as directory:
                work = Path(directory)
                writer = PdfWriter()
                page = writer.add_blank_page(100, 100)
                font = DictionaryObject({NameObject('/Type'): NameObject('/Font'),
                                         NameObject('/Subtype'): NameObject('/Type1'),
                                         NameObject('/BaseFont'): NameObject('/NotoSansCJKsc')})
                if composite:
                    font = DictionaryObject({NameObject('/Subtype'): NameObject('/Type0'),
                                             NameObject('/BaseFont'): NameObject('/NotoSansCJKsc'),
                                             NameObject('/DescendantFonts'): ArrayObject([font])})
                page[NameObject('/Resources')] = DictionaryObject({
                    NameObject('/Font'): DictionaryObject({NameObject('/F1'): font})})
                pdf = work / 'unembedded.pdf'
                writer.write(pdf)
                with self.assertRaisesRegex(AssertionError, 'unembedded fonts'):
                    export_pdf.qa_pdf(pdf, work, {'source_characters_without_whitespace': 0})

    def test_no_fonts_is_not_a_successful_embedding_check(self):
        from pypdf import PdfWriter

        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)
            writer = PdfWriter()
            writer.add_blank_page(100, 100)
            pdf = work / 'no-fonts.pdf'
            writer.write(pdf)
            with self.assertRaisesRegex(AssertionError, 'no embedded fonts'):
                export_pdf.qa_pdf(pdf, work, {'source_characters_without_whitespace': 0})


class RenderingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dependency('lxml.html')
        dependency('pypdf')
        dependency('weasyprint')
        for tool in ('pdftoppm', 'pdfinfo', 'pdffonts'):
            try:
                export_pdf.tool_path(tool)
            except RuntimeError as error:
                if os.environ.get('PVE_PDF_REQUIRE_DEPS') == '1':
                    raise AssertionError(str(error)) from error
                raise unittest.SkipTest(str(error)) from error
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.work = Path(cls.temp.name)
        cls.pdf = cls.work / 'smoke.pdf'
        result = subprocess.run(
            [sys.executable, str(export_pdf.ROOT / 'scripts/export_pdf.py'),
             '--input', str(FIXTURES / 'render.html'), '--output', str(cls.pdf),
             '--work-dir', str(cls.work), '--title', 'PDF 回归测试', '--qa'],
            capture_output=True, text=True, timeout=120, cwd=export_pdf.ROOT)
        if result.returncode:
            raise AssertionError(f'PDF smoke failed:\n{result.stdout}\n{result.stderr}')
        cls.report = json.loads((cls.work / 'qa-report.json').read_text(encoding='utf-8'))

    def test_rendered_fixture(self):
        report = self.report
        self.assertEqual(report['tables_as_paginated_records'], 1)
        self.assertEqual(report['two_column_api_parameter_tables'], 1)
        self.assertEqual(report['printable_area_text_overflow_count'], 0)
        self.assertGreaterEqual(report['pages'], 5)  # cover, TOC, paginated record, short chapter
        self.assertLessEqual(report['pages'], 8)
        self.assertEqual(report['unembedded_fonts'], [])
        for family in ('Noto-Sans-CJK-SC', 'Noto-Sans-CJK-SC-Bold', 'Noto-Sans-Mono-CJK-SC'):
            self.assertTrue(any(name.endswith('+' + family) for name in report['embedded_fonts']), family)
        self.assertEqual(len(report['section_text_checks']), 2)
        self.assertTrue(all(item['text_preserved_in_order'] for item in report['section_text_checks']))
        self.assertGreaterEqual(report['outline_entries_top_level'], 2)
        self.assertTrue(list(self.work.glob('qa-*.png')))
        self.assertTrue((self.work / 'pdffonts.txt').is_file())

    def test_removing_embedded_font_from_real_pdf_fails_qa(self):
        from pypdf import PdfReader, PdfWriter

        writer = PdfWriter()
        writer.clone_document_from_reader(PdfReader(self.pdf))
        removed = 0
        for page in writer.pages:
            for ref in page['/Resources']['/Font'].values():
                font = ref.get_object()
                if '/DescendantFonts' in font:
                    font = font['/DescendantFonts'][0].get_object()
                descriptor = font.get('/FontDescriptor')
                if descriptor:
                    descriptor = descriptor.get_object()
                    for key in ('/FontFile', '/FontFile2', '/FontFile3'):
                        if key in descriptor:
                            del descriptor[key]
                            removed += 1
        self.assertGreater(removed, 0)
        broken = self.work / 'stripped.pdf'
        writer.write(broken)
        with self.assertRaisesRegex(AssertionError, 'unembedded fonts'):
            export_pdf.qa_pdf(broken, self.work, copy.deepcopy(self.report))


if __name__ == '__main__':
    unittest.main()
