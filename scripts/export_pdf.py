#!/usr/bin/env python3
"""Create the complete Chinese manual PDF from builds/book-export.html.

Dependencies: Python 3.12+, weasyprint==70.0, lxml, pypdf, Pillow, fonttools;
Pango 1.44+; Poppler's pdftoppm, pdfinfo and pdffonts for QA. On macOS install
Pango via Homebrew. No Apple fonts are bundled. The three bundled Noto font
files and their OFL license live in export-assets/fonts/.

Example:
  python scripts/export_pdf.py --qa

PDF creation intentionally remains an explicit command, after the book export
is ready. It never modifies the source HTML or Markdown. Oversized table rows
are presented as labelled, freely paginated records instead of being clipped.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time
from xml.sax.saxutils import escape as xml_escape
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = Path.home() / '.cache/codex-runtimes/codex-primary-runtime/dependencies'


def native_environment() -> None:
    """Make locally installed Pango visible to cffi on Homebrew macOS."""
    if sys.platform == 'darwin' and not os.environ.get('PVE_PDF_NATIVE_READY'):
        paths = [str(p) for p in (Path('/opt/homebrew/lib'), Path('/usr/local/lib')) if p.is_dir()]
        old = os.environ.get('DYLD_FALLBACK_LIBRARY_PATH')
        if old:
            paths.append(old)
        if paths:
            env = dict(os.environ, DYLD_FALLBACK_LIBRARY_PATH=':'.join(paths), PVE_PDF_NATIVE_READY='1')
            os.execve(sys.executable, [sys.executable, *sys.argv], env)


def approved_font_environment(work: Path) -> None:
    """Exclude proprietary system fallback fonts, including SVG/emoji fonts."""
    directory = xml_escape(str((ROOT / 'export-assets/fonts').resolve()))
    cache = xml_escape(str((work / 'font-cache').resolve()))
    aliases = {'sans-serif': 'Noto Sans CJK SC', 'serif': 'Noto Sans CJK SC',
               'monospace': 'Noto Sans Mono CJK SC', 'Helvetica': 'Noto Sans CJK SC',
               'Arial': 'Noto Sans CJK SC', 'Courier': 'Noto Sans Mono CJK SC',
               'emoji': 'Noto Emoji', 'Apple Color Emoji': 'Noto Emoji'}
    config = ['<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">',
              f'<fontconfig><dir>{directory}</dir><cachedir>{cache}</cachedir>']
    for family, substitute in aliases.items():
        config.append(f'<alias><family>{family}</family><prefer><family>{substitute}</family></prefer></alias>')
    config.append('</fontconfig>')
    path = work / 'fontconfig.xml'
    path.write_text(''.join(config), encoding='utf-8')
    os.environ['FONTCONFIG_FILE'] = str(path)


def tool_path(name: str) -> str:
    candidates = [
        RUNTIME / 'bin/override' / name,
        RUNTIME / 'bin/fallback' / name,
        RUNTIME / 'native/poppler/poppler/bin' / name,
        RUNTIME / 'native/poppler/bin' / name,
    ]
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    found = shutil.which(name)
    if found:
        return found
    raise RuntimeError(f'Required QA tool not found: {name}')


def text_content(node) -> str:
    return ''.join(node.itertext())


def prepare_html(source: Path, title: str, work: Path) -> tuple[str, dict]:
    from lxml import etree, html

    tree = html.document_fromstring(source.read_text(encoding='utf-8'))
    for node in tree.xpath('//script|//style|//link[@rel="stylesheet"]'):
        node.getparent().remove(node)
    for details in tree.xpath('//details'):
        details.tag = 'div'
        details.set('class', (details.get('class', '') + ' pdf-details').strip())
        for summary in details.xpath('./summary'):
            summary.tag = 'p'
            summary.set('class', 'pdf-details-title')
    mains = tree.xpath('//main[contains(concat(" ",normalize-space(@class)," ")," book-content ")]')
    if not mains:
        raise ValueError('Source must contain <main class="book-content">')
    main = mains[0]
    chapters = main.xpath('./section[contains(concat(" ",normalize-space(@class)," ")," book-chapter ")]')
    if not chapters:
        raise ValueError('Source must contain section.book-chapter elements')
    before_text = re.sub(r'\s+', '', text_content(main))
    images = []
    for image in main.xpath('.//img[@src]'):
        src = image.get('src')
        parsed = urlsplit(src)
        if parsed.scheme == 'data':
            continue
        if parsed.scheme not in ('', 'file') or parsed.netloc:
            raise ValueError(f'Non-local image in offline export: {src}')
        local = Path(unquote(parsed.path))
        if not local.is_absolute():
            local = source.parent / local
        if not local.is_file():
            raise FileNotFoundError(f'Book image not found: {local}')
        images.append(str(local.resolve()))
        image.set('src', local.resolve().as_uri())

    # WeasyPrint cannot split an arbitrarily tall table row. Keep normal
    # tables intact, and turn only tables containing oversized rows into
    # labelled records. Their original cells and markup remain unabridged.
    converted = 0
    parameter_tables = 0
    for table in reversed(list(main.xpath('.//table'))):
        if table.getparent() is None:
            continue
        rows = table.xpath('./thead/tr|./tbody/tr|./tfoot/tr|./tr')
        top_headers = table.xpath('./thead/tr[1]/th')
        if [text_content(cell).strip() for cell in top_headers] == ['参数', '定义与说明']:
            table.set('class', (table.get('class', '') + ' pdf-api-parameters').strip())
            parameter_tables += 1
        data_rows = [r for r in rows if r.xpath('./td')]
        if not data_rows:
            continue
        oversized = any(
            max((len(text_content(c)) for c in row.xpath('./td|./th')), default=0) > 900
            or any(len(text_content(p).splitlines()) > 14 for p in row.xpath('.//pre'))
            or bool(row.xpath('.//table'))
            for row in data_rows
        )
        if not oversized:
            continue
        header_rows = [r for r in rows if r.xpath('./th') and not r.xpath('./td')]
        headers = header_rows[-1].xpath('./th') if header_rows else []
        wrapper = html.Element('div', {'class': 'pdf-record-table'})
        if table.get('id'):
            wrapper.set('id', table.get('id'))
        for caption in table.xpath('./caption'):
            wrapper.append(copy.deepcopy(caption))
        # Preserve all header cells once, even when a colspan prevents a
        # one-to-one match with the data cells.
        if header_rows:
            header_block = etree.SubElement(wrapper, 'div', {'class': 'pdf-record-label'})
            for row in header_rows:
                for cell in row.xpath('./th'):
                    span = copy.deepcopy(cell)
                    span.tag = 'span'
                    span.tail = '  '
                    header_block.append(span)
        for row in data_rows:
            record = etree.SubElement(wrapper, 'div', {'class': 'pdf-record'})
            for index, cell in enumerate(row.xpath('./td|./th')):
                field = etree.SubElement(record, 'div', {'class': 'pdf-record-field'})
                if index < len(headers):
                    label = etree.SubElement(field, 'div', {'class': 'pdf-record-label'})
                    label.text = text_content(headers[index]).strip()
                value = copy.deepcopy(cell)
                value.tag = 'div'
                value.set('class', 'pdf-record-value')
                field.append(value)
        table.getparent().replace(table, wrapper)
        converted += 1
    # Every original non-whitespace character must still occur, in order.
    # Added record labels can occur between source characters.
    after_text = re.sub(r'\s+', '', text_content(main))
    iterator = iter(after_text)
    if not all(any(c == original for c in iterator) for original in before_text):
        raise AssertionError('PDF table preprocessing lost or reordered source text')

    head = tree.find('head')
    if head is None:
        head = html.Element('head')
        tree.insert(0, head)
    for old in head.xpath('./title'):
        head.remove(old)
    etree.SubElement(head, 'title').text = title
    etree.SubElement(head, 'meta', {'name': 'author', 'content': 'Proxmox Server Solutions GmbH; unofficial Chinese translation'})
    tree.set('lang', 'zh-CN')
    body = tree.find('body')
    cover = html.Element('section', {'class': 'pdf-cover'})
    etree.SubElement(cover, 'p', {'class': 'pdf-eyebrow'}).text = 'PROXMOX VIRTUAL ENVIRONMENT'
    etree.SubElement(cover, 'h1').text = title
    etree.SubElement(cover, 'p', {'class': 'pdf-subtitle'}).text = '管理手册 · 命令参考 · API 参考'
    etree.SubElement(cover, 'p', {'class': 'pdf-edition'}).text = 'Proxmox VE 9.2.13 | 非官方简体中文译本'
    etree.SubElement(cover, 'p', {'class': 'pdf-note'}).text = '原始文档版权及许可声明见正文。命令、配置项、路径与 API 字段保留原文。'
    toc = html.Element('section', {'class': 'pdf-toc'})
    etree.SubElement(toc, 'h1').text = '目录'
    entries = etree.SubElement(toc, 'ol')
    chapter_targets = []
    for index, chapter in enumerate(chapters, 1):
        headings = chapter.xpath('./h1')
        if not headings:
            headings = chapter.xpath('.//h1')
        if not headings:
            raise ValueError(f'Chapter without H1: {chapter.get("data-source")}')
        heading = headings[0]
        ident = heading.get('id') or f'pdf-chapter-{index}'
        heading.set('id', ident)
        link = etree.SubElement(etree.SubElement(entries, 'li'), 'a', {'href': '#' + ident})
        link.text = text_content(heading).strip()
        chapter_targets.append({'id': ident, 'source': chapter.get('data-source', ''), 'title': link.text})
    body.insert(0, toc)
    body.insert(0, cover)
    output = html.tostring(tree, encoding='unicode', method='html', doctype='<!doctype html>')
    work.mkdir(parents=True, exist_ok=True)
    (work / 'prepared.html').write_text(output, encoding='utf-8')
    report = {
        'source': str(source), 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'source_characters_without_whitespace': len(before_text),
        'chapters': len(chapters), 'images': len(images),
        'unique_images': len(set(images)), 'tables_as_paginated_records': converted,
        'two_column_api_parameter_tables': parameter_tables,
        'source_text_preserved_in_order': True,
        'chapter_targets': chapter_targets,
    }
    return output, report


def sample_pages(reader, report: dict) -> dict[str, int]:
    chosen = {'cover': 1, 'contents': 2, 'ending': len(reader.pages)}
    chosen.update(report.get('layout_representative_pages', {}))
    patterns = {
        'image': r'安装向导|安装介质|Web.*界面|GUI',
        'table': r'存储类型|CPU.*标志|可用的.*类型',
        'code_notice': r'警告|注意.*命令|安全.*启动',
        'api_schema': r'返回.*模式|schema|additionalProperties|请求参数',
    }
    for index, page in enumerate(reader.pages, 1):
        content = page.extract_text() or ''
        for label, pattern in patterns.items():
            if label not in chosen and re.search(pattern, content, re.I):
                chosen[label] = index
        if all(k in chosen for k in patterns):
            break
    chosen['middle'] = max(1, len(reader.pages) // 2)
    return chosen


def qa_pdf(pdf: Path, work: Path, report: dict) -> None:
    from pypdf import PdfReader

    reader = PdfReader(pdf)
    report['pages'] = len(reader.pages)
    if not reader.pages:
        raise AssertionError('PDF is empty')
    all_text = []
    embedded_fonts = set()
    missing_fonts = set()
    image_objects = 0
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ''
        all_text.append(text)
        resources = page.get('/Resources', {})
        resources = resources.get_object() if hasattr(resources, 'get_object') else resources
        fonts = resources.get('/Font', {})
        fonts = fonts.get_object() if hasattr(fonts, 'get_object') else fonts
        for ref in fonts.values():
            font = ref.get_object()
            name = str(font.get('/BaseFont', 'unknown'))
            if '/DescendantFonts' in font:
                font = font['/DescendantFonts'][0].get_object()
            descriptor = font.get('/FontDescriptor')
            descriptor = descriptor.get_object() if descriptor else {}
            if any(k in descriptor for k in ('/FontFile', '/FontFile2', '/FontFile3')):
                embedded_fonts.add(name)
            else:
                missing_fonts.add(name)
        objects = resources.get('/XObject', {})
        objects = objects.get_object() if hasattr(objects, 'get_object') else objects
        image_objects += sum(obj.get_object().get('/Subtype') == '/Image' for obj in objects.values())
    combined = '\n'.join(all_text)
    (work / 'extracted-text.txt').write_text(combined, encoding='utf-8')
    report.update({
        'extracted_characters': len(combined),
        'embedded_fonts': sorted(embedded_fonts), 'unembedded_fonts': sorted(missing_fonts),
        'page_image_objects': image_objects, 'outline_entries_top_level': len(reader.outline),
        'pdf_bytes': pdf.stat().st_size,
        'extracted_characters_without_whitespace': len(re.sub(r'\s+', '', combined)),
    })
    if missing_fonts:
        raise AssertionError(f'PDF contains unembedded fonts: {missing_fonts}')
    if any('Noto' not in name for name in embedded_fonts):
        raise AssertionError(f'PDF contains a non-approved fallback font: {embedded_fonts}')
    if '\ufffd' in combined:
        raise AssertionError('PDF text contains Unicode replacement characters')
    if not re.search('[\u4e00-\u9fff]', combined):
        raise AssertionError('No Chinese text could be extracted from PDF')
    if report['extracted_characters_without_whitespace'] < report['source_characters_without_whitespace'] * .95:
        raise AssertionError('Extracted PDF text is substantially shorter than the complete source')
    samples = sample_pages(reader, report)
    report['representative_pages'] = samples
    for label, page in samples.items():
        prefix = work / f'qa-{label}-{page:04d}'
        subprocess.run([tool_path('pdftoppm'), '-f', str(page), '-l', str(page), '-singlefile',
                        '-scale-to', '1700', '-png', str(pdf), str(prefix)], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for name in ('pdfinfo', 'pdffonts'):
        result = subprocess.run([tool_path(name), str(pdf)], check=True, capture_output=True, text=True)
        (work / f'{name}.txt').write_text(result.stdout, encoding='utf-8')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=ROOT / 'builds/book-export.html')
    parser.add_argument('--output', type=Path, default=ROOT / 'output/pdf/Proxmox-VE-9.2.13-zh-CN.pdf')
    parser.add_argument('--work-dir', type=Path, default=ROOT / 'tmp/pdfs/full')
    parser.add_argument('--title', default='Proxmox VE 9.2.13 简体中文文档')
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--qa', action='store_true')
    args = parser.parse_args()
    source, output, work = args.input.resolve(), args.output.resolve(), args.work_dir.resolve()
    work.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    html, report = prepare_html(source, args.title, work)
    if not args.prepare_only:
        approved_font_environment(work)
        native_environment()
        from weasyprint import CSS, HTML
        from weasyprint.text.fonts import FontConfiguration
        from weasyprint.urls import URLFetcher

        offline_fetcher = URLFetcher(allowed_protocols={'file', 'data'}, fail_on_errors=True)

        handler = logging.FileHandler(work / 'weasyprint.log', encoding='utf-8', mode='w')
        logger = logging.getLogger('weasyprint')
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        fonts = FontConfiguration()
        stylesheet = CSS(filename=str(ROOT / 'export-assets/print.css'),
                         font_config=fonts, url_fetcher=offline_fetcher)
        print(f'Layout: {report["chapters"]} chapters, {report["images"]} images, '
              f'{report["tables_as_paginated_records"]} oversized tables converted', flush=True)
        document = HTML(string=html, base_url=str(source.parent) + '/',
                        url_fetcher=offline_fetcher).render(stylesheets=[stylesheet], font_config=fonts)
        report['rendered_pages'] = len(document.pages)
        overflow = []
        samples = {}
        chapter_pages = {}
        chapter_ids = {item['id']: item for item in report['chapter_targets']}
        for index, page in enumerate(document.pages, 1):
            for ident in page.anchors:
                if ident in chapter_ids:
                    chapter_pages[ident] = index
                    source_name = chapter_ids[ident]['source']
                    if (source_name.startswith('api/') or ident.startswith('page-api-group-')) and index > 2:
                        samples.setdefault('api_schema', min(index + 1, len(document.pages)))
                    elif index > 5:
                        samples.setdefault('chapter_transition', index)
                        samples.setdefault('chapter_transition_before', index - 1)
            body_boxes = [box for child in page._page_box.children if type(child).__name__ != 'MarginBox'
                          for box in child.descendants()]
            for box in body_boxes:
                tag = getattr(box, 'element_tag', '')
                if tag == 'img' and getattr(box, 'height', 0) > 60:
                    samples.setdefault('image', index)
                if type(box).__name__ == 'TableBox' and len(getattr(box, 'children', ())) > 0:
                    samples.setdefault('table', index)
                if tag == 'pre':
                    samples.setdefault('code_notice', index)
                if type(box).__name__ == 'TextBox' and getattr(box, 'text', '').strip():
                    if (box.position_x < page._page_box.margin_left - 2
                            or box.position_x + box.width > page.width - page._page_box.margin_right + 2
                            or box.position_y < page._page_box.margin_top - 2
                            or box.position_y + box.height > page.height - page._page_box.margin_bottom + 2):
                        overflow.append({'page': index, 'text': box.text[:120],
                                         'x': round(box.position_x, 2), 'y': round(box.position_y, 2),
                                         'width': round(box.width, 2), 'height': round(box.height, 2)})
        report['printable_area_text_overflows'] = overflow[:100]
        report['printable_area_text_overflow_count'] = len(overflow)
        report['layout_representative_pages'] = samples
        report['chapter_pages'] = chapter_pages
        if set(chapter_ids) != set(chapter_pages):
            raise AssertionError(f'Chapters missing from rendered PDF: {set(chapter_ids) - set(chapter_pages)}')
        if overflow:
            (work / 'qa-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
            raise AssertionError(f'{len(overflow)} text boxes extend beyond the printable area')
        output.parent.mkdir(parents=True, exist_ok=True)
        document.write_pdf(str(output), pdf_tags=True)
        print(f'Written: {len(document.pages)} pages, {output.stat().st_size:,} bytes', flush=True)
        del document
        if args.qa:
            qa_pdf(output, work, report)
    report['elapsed_seconds'] = round(time.monotonic() - started, 2)
    (work / 'qa-report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    main()
