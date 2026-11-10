#!/usr/bin/env python3
"""Export SUMMARY-ordered GitBook Markdown to a self-contained offline book/EPUB3.

Contract: html/index.html is the interactive single-page book; book-export.html
contains exactly the same main.book-content, without navigation/scripts, and with
details expanded. Every source page is section.book-chapter with an H1 whose ID
is its stable pagekey. All other IDs are scoped to that pagekey.

The normal build is gated by work/CHAPTER_LAYOUT_READY. Use --self-test for an
isolated parser/link/EPUB regression test without publishing current docs.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import tempfile
import zipfile
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
import yaml

ROOT = Path(__file__).resolve().parents[1]
VERSION = "9.2.13"
TITLE = f"Proxmox VE {VERSION} 简体中文文档"
EPUB_NAME = f"Proxmox-VE-{VERSION}-zh-CN.epub"
HINT = re.compile(r'^\s*\{%\s*hint\s+style=[\"\']([\w-]+)[\"\']\s*%\}\s*$')
END_HINT = re.compile(r'^\s*\{%\s*endhint\s*%\}\s*$')


def hint_block(state, start_line: int, end_line: int, silent: bool) -> bool:
    """A native block rule retains Markdown's list indentation context."""
    if state.sCount[start_line] - state.blkIndent >= 4:
        return False
    line = state.src[state.bMarks[start_line] + state.tShift[start_line]:state.eMarks[start_line]]
    match = HINT.match(line)
    if not match:
        return False
    if silent:
        return True
    close = start_line + 1
    nesting = 1
    fence = None
    while close < end_line:
        candidate = state.src[state.bMarks[close] + state.tShift[close]:state.eMarks[close]]
        marker = re.match(r"^(`{3,}|~{3,})", candidate)
        if marker:
            if fence is None:
                fence = marker[1]
            elif marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
        elif fence is None:
            if HINT.match(candidate):
                nesting += 1
            elif END_HINT.match(candidate):
                nesting -= 1
                if nesting == 0:
                    break
        close += 1
    if close == end_line:
        raise ValueError(f"Unclosed GitBook hint at line {start_line + 1}")
    parent_type, line_max = state.parentType, state.lineMax
    state.parentType = "hint"
    state.lineMax = close
    opening = state.push("hint_open", "aside", 1)
    opening.block = True
    opening.map = [start_line, close + 1]
    opening.attrs = {"class": "hint hint-" + match[1], "role": "note"}
    state.md.block.tokenize(state, start_line + 1, close)
    closing = state.push("hint_close", "aside", -1)
    closing.block = True
    state.parentType, state.lineMax = parent_type, line_max
    state.line = close + 1
    return True


MD = MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])
MD.block.ruler.before("fence", "gitbook_hint", hint_block, {"alt": ["paragraph", "reference", "blockquote", "list"]})


def slug(text: str) -> str:
    return re.sub(r"[^\w\-]+", "-", text.lower(), flags=re.UNICODE).strip("_-") or "section"


def strip_frontmatter(text: str) -> str:
    """Remove only an initial, closed YAML metadata mapping; never execute tags.

    A later horizontal rule, an unclosed header, scalar YAML, and invalid/unsafe
    YAML remain ordinary document text. The size bound also prevents scanning a
    whole large API page when an opening horizontal rule is ordinary Markdown.
    """
    opening = re.match(r"\A\ufeff?---[ \t]*\r?\n", text)
    if not opening:
        return text
    closing = re.search(r"^(?:---|\.\.\.)[ \t]*\r?$", text[opening.end():opening.end() + 65536], re.MULTILINE)
    if not closing:
        return text
    start = opening.end()
    try:
        metadata = yaml.safe_load(text[start:start + closing.start()])
    except yaml.YAMLError:
        return text
    if not isinstance(metadata, dict) or not all(isinstance(key, str) for key in metadata):
        return text
    body_start = start + closing.end()
    if text[body_start:body_start + 1] == "\n":
        body_start += 1
    return text[body_start:]


def render_markdown(text: str) -> str:
    return MD.render(strip_frontmatter(text))


@dataclass
class Page:
    path: Path
    title: str
    depth: int
    key: str
    soup: BeautifulSoup
    aliases: dict[str, str] = field(default_factory=dict)
    headings: list[dict] = field(default_factory=list)


def summary_pages(docs: Path) -> list[Page]:
    summary = BeautifulSoup(MD.render(strip_frontmatter((docs / "SUMMARY.md").read_text())), "html.parser")
    result: list[Page] = []
    seen: set[Path] = set()
    for link in summary.select("a[href]"):
        parsed = urlsplit(link["href"])
        if parsed.scheme or parsed.netloc:
            continue
        path = (docs / unquote(parsed.path)).resolve()
        if path in seen:
            continue
        if not path.is_relative_to(docs.resolve()) or not path.is_file() or path.suffix != ".md":
            raise ValueError(f"Invalid SUMMARY page: {link['href']}")
        seen.add(path)
        rel = path.relative_to(docs.resolve()).as_posix()
        key = "page-" + slug(str(Path(rel).with_suffix(""))) + "-" + hashlib.sha256(rel.encode()).hexdigest()[:8]
        depth = max(0, sum(p.name == "ul" for p in link.parents) - 1)
        rendered = BeautifulSoup(render_markdown(path.read_text(encoding="utf-8")), "html.parser")
        result.append(Page(path, link.get_text(" ", strip=True), depth, key, rendered))
    if not result:
        raise ValueError("SUMMARY contains no pages")
    return result


def namespace(page: Page) -> None:
    soup = page.soup
    headings = soup.find_all(re.compile(r"^h[1-6]$"))
    if not headings or headings[0].name != "h1":
        heading = soup.new_tag("h1")
        heading.string = page.title
        soup.insert(0, heading)
        headings.insert(0, heading)
    used: set[str] = set()

    def unique(original: str) -> str:
        base = page.key + "--" + original
        target = base
        count = 1
        while target in used:
            count += 1
            target = f"{base}-{count}"
        used.add(target)
        return target

    for i, heading in enumerate(headings):
        anchors = heading.select("[id], a[name]")
        originals = ([heading["id"]] if heading.get("id") else []) + [a.get("id") or a["name"] for a in anchors]
        # Some renderers use {#id}, while this project normally uses inline <a>.
        trailing = re.search(r"\s*\{#([^}]+)\}\s*$", heading.get_text())
        if trailing:
            originals.append(trailing[1])
            for text in list(heading.find_all(string=True)):
                if trailing[0] in str(text):
                    text.replace_with(str(text).replace(trailing[0], ""))
        title = heading.get_text(" ", strip=True)
        target = page.key if i == 0 else unique(originals[0] if originals else slug(title))
        used.add(target)
        heading["id"] = target
        for old in originals + [slug(title)]:
            page.aliases.setdefault(old, target)
        for anchor in anchors:
            anchor.attrs.pop("id", None)
            anchor.attrs.pop("name", None)
            if not anchor.get_text(strip=True):
                anchor.decompose()
        page.headings.append({"id": target, "title": title, "level": int(heading.name[1])})
    for element in soup.select("[id], a[name]"):
        if element.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            continue
        old = element.get("id") or element.get("name")
        target = unique(old)
        page.aliases.setdefault(old, target)
        element["id"] = target
        element.attrs.pop("name", None)
    # A page top alias is useful for README links and links to the original H1.
    page.aliases[""] = page.key


def rewrite_links(pages: list[Page], docs: Path) -> list[str]:
    by_path = {page.path.resolve(): page for page in pages}
    errors: list[str] = []
    for page in pages:
        for element in page.soup.select("[href], [src], [poster]"):
            for attribute in ("href", "src", "poster"):
                if attribute not in element.attrs:
                    continue
                raw = element[attribute]
                parsed = urlsplit(raw)
                if parsed.scheme or parsed.netloc:
                    if attribute in {"src", "poster"} and not raw.startswith("data:"):
                        errors.append(f"Remote embedded asset in {page.path.name}: {raw}")
                    continue
                target = (page.path.parent / unquote(parsed.path)).resolve() if parsed.path else page.path.resolve()
                fragment = unquote(parsed.fragment)
                if attribute == "href" and (target in by_path or target.suffix == ".md"):
                    other = by_path.get(target)
                    if other is None:
                        errors.append(f"Page missing from SUMMARY: {raw} in {page.path.name}")
                    else:
                        anchor = other.aliases.get(fragment)
                        if anchor is None:
                            errors.append(f"Unknown anchor: {raw} in {page.path.name}")
                        else:
                            element[attribute] = "#" + anchor
                elif parsed.path:
                    if not target.is_relative_to(docs.resolve()) or not target.is_file():
                        errors.append(f"Missing local asset: {raw} in {page.path.name}")
                    else:
                        relative = target.relative_to(docs.resolve()).as_posix()
                        element[attribute] = quote(relative, safe="/._-") + (("#" + parsed.fragment) if parsed.fragment else "")
        for image in page.soup.find_all("img"):
            image["loading"] = "lazy"
            image["decoding"] = "async"
        for pre in page.soup.find_all("pre"):
            pre["tabindex"] = "0"
    return errors


def chapter_html(page: Page) -> str:
    nav = '<nav class="chapter-nav" aria-label="章内导航"><details><summary>本页目录</summary><ul>'
    for heading in page.headings[1:]:
        nav += f'<li class="level-{heading["level"]}"><a href="#{heading["id"]}">{html.escape(heading["title"])}</a></li>'
    nav += "</ul></details></nav>"
    first = page.soup.find("h1")
    first.insert_after(BeautifulSoup(nav, "html.parser"))
    return f'<section class="book-chapter" data-pagekey="{page.key}" data-source="{html.escape(page.path.name)}">{page.soup}</section>'


def document(content: str, css: str, extra: str = "", scripts: bool = False) -> str:
    return ('<!DOCTYPE html>\n<html lang="zh-CN"><head><meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="description" content="Proxmox VE {VERSION} 全量简体中文离线文档">'
            f'<title>{TITLE}</title><link rel="stylesheet" href="{css}"></head><body>'
            + extra + f'<main class="book-content" id="book-content">{content}</main>'
            + ('<script src="offline.js" defer></script>' if scripts else '') + '</body></html>\n')


def audit_html(text: str, base: Path) -> dict:
    soup = BeautifulSoup(text, "html.parser")
    ids = Counter(tag["id"] for tag in soup.select("[id]"))
    errors = [f"Duplicate ID {key}" for key, count in ids.items() if count != 1]
    links = 0
    for link in soup.select("a[href]"):
        href = link["href"]
        if href.startswith("#"):
            links += 1
            if unquote(href[1:]) not in ids:
                errors.append(f"Broken single-page anchor {href}")
        elif urlsplit(href).path.endswith(".md"):
            errors.append(f"Unrewritten Markdown link {href}")
    for tag in soup.select("img[src], link[href], script[src]"):
        raw = tag.get("src") or tag.get("href")
        if urlsplit(raw).scheme or raw.startswith("//"):
            if not raw.startswith("data:"):
                errors.append(f"Remote dependency {raw}")
        elif not (base / unquote(urlsplit(raw).path)).is_file():
            errors.append(f"Missing packaged dependency {raw}")
    if errors:
        raise ValueError("\n".join(errors[:40]))
    return {"chapters": len(soup.select("section.book-chapter")), "headings": len(soup.select("h1,h2,h3,h4,h5,h6")),
            "ids": len(ids), "internal_links": links, "images": len(soup.select("img")),
            "tables": len(soup.select("table")), "code_blocks": len(soup.select("pre")), "hints": len(soup.select(".hint"))}


def audit_source_content(pages: list[Page], docs: Path) -> dict:
    """Independent plain CommonMark baseline catches parser-context regressions."""
    baseline_md = MarkdownIt("commonmark", {"html": True}).enable(["table", "strikethrough"])
    stats = {"pages": len(pages), "code_blocks": 0, "images": 0, "tables": 0}
    errors = []
    for page in pages:
        baseline = BeautifulSoup(baseline_md.render(strip_frontmatter(page.path.read_text())), "html.parser")
        for text in list(baseline.find_all(string=True)):
            if any(parent.name in {"code", "pre"} for parent in text.parents):
                continue
            text.replace_with(re.sub(r'\{%\s*(?:hint\s+style=[\"\'][\w-]+[\"\']|endhint)\s*%\}', '', str(text)))
        expected = re.sub(r"\s+", "", baseline.get_text())
        actual = re.sub(r"\s+", "", page.soup.get_text())
        if expected != actual:
            offset = next((i for i, (left, right) in enumerate(zip(expected, actual)) if left != right), min(len(expected), len(actual)))
            errors.append(f"{page.path}: text differs at {offset}: {expected[max(0,offset-20):offset+60]!r} != {actual[max(0,offset-20):offset+60]!r}")
        if [pre.get_text() for pre in baseline.select("pre")] != [pre.get_text() for pre in page.soup.select("pre")]:
            errors.append(f"{page.path}: code blocks changed")
        for name, selector in (("code_blocks", "pre"), ("images", "img"), ("tables", "table")):
            count = len(baseline.select(selector))
            stats[name] += count
            if count != len(page.soup.select(selector)):
                errors.append(f"{page.path}: {name} count changed")
    listed = {page.path.resolve() for page in pages}
    unlisted = [str(path.relative_to(docs)) for path in docs.rglob("*.md") if path.name != "SUMMARY.md" and path.resolve() not in listed]
    if unlisted:
        errors.append(f"Content pages absent from SUMMARY: {unlisted}")
    if errors:
        raise ValueError("Source content audit failed:\n" + "\n".join(errors[:20]))
    return {"all_content_pages_included": True, "full_text_matches_markdown": True, "code_blocks_exact": True, **stats}


def find_pandoc() -> str:
    found = shutil.which("pandoc")
    if found:
        return found
    fallback = ROOT.home() / ".cache/codex-runtimes/codex-primary-runtime/dependencies/bin/fallback/pandoc"
    if fallback.is_file():
        return str(fallback)
    raise RuntimeError("pandoc is required (brew install pandoc)")


def audit_epub(path: Path, pagekeys: list[str], source_text: str) -> dict:
    with zipfile.ZipFile(path) as archive:
        members = set(archive.namelist())
        if archive.read("mimetype") != b"application/epub+zip":
            raise ValueError("Invalid EPUB mimetype")
        documents = {}
        ids = {}
        for name in members:
            if name.endswith((".xhtml", ".html")):
                root = ET.fromstring(archive.read(name))
                documents[name] = root
                values = [node.attrib["id"] for node in root.iter() if "id" in node.attrib]
                if len(values) != len(set(values)):
                    raise ValueError(f"Duplicate EPUB IDs in {name}")
                ids[name] = set(values)
        broken = []
        for name, root in documents.items():
            for element in root.iter():
                for attr in ("href", "src"):
                    ref = element.get(attr)
                    if not ref:
                        continue
                    parsed = urlsplit(ref)
                    if parsed.scheme or parsed.netloc or ref.startswith("data:"):
                        continue
                    target = os.path.normpath(str(Path(name).parent / unquote(parsed.path))) if parsed.path else name
                    if target not in members or (parsed.fragment and target in ids and unquote(parsed.fragment) not in ids[target]):
                        broken.append(f"{name}: {ref}")
        if broken:
            raise ValueError("Broken EPUB links: " + "; ".join(broken[:20]))
        chapter_documents = []
        for key in pagekeys:
            found = [name for name, values in ids.items() if key in values]
            if len(found) != 1:
                raise ValueError(f"EPUB chapter anchor mismatch: {key}: {found}")
            chapter_documents.extend(found)
        if len(set(chapter_documents)) != len(pagekeys):
            raise ValueError("EPUB chapters were not split on source-page boundaries")
        source_normalized = re.sub(r"\s+", "", source_text)
        epub_text = "".join("".join(documents[name].find("{http://www.w3.org/1999/xhtml}body").itertext()) for name in chapter_documents)
        epub_normalized = re.sub(r"\s+", "", epub_text)
        if source_normalized != epub_normalized:
            offset = next((i for i, (left, right) in enumerate(zip(source_normalized, epub_normalized)) if left != right), min(len(source_normalized), len(epub_normalized)))
            raise ValueError(f"EPUB text differs from full export at character {offset}: source={source_normalized[max(0, offset-40):offset+100]!r}; EPUB={epub_normalized[max(0, offset-40):offset+100]!r}")
        for name in members:
            if name.endswith(".css"):
                css = archive.read(name).decode("utf-8")
                for ref in re.findall(r'url\([\"\']?([^\)\"\']+)', css):
                    target = os.path.normpath(str(Path(name).parent / ref))
                    if not urlsplit(ref).scheme and target not in members:
                        raise ValueError(f"Missing EPUB stylesheet resource: {target}")
        return {"documents": len(documents), "book_chapters": len(pagekeys), "images": sum('/media/' in name for name in members),
                "fonts": sum(name.endswith((".otf", ".ttf", ".woff2")) for name in members), "internal_links_valid": True,
                "full_text_matches_html": True, "text_characters_without_whitespace": len(epub_normalized)}


def attach_epub_licenses(path: Path, fonts: Path) -> None:
    """Retain redistribution licenses beside the fonts in Pandoc's EPUB package."""
    additions = {}
    for name in sorted({"FONT-SOURCES.json", *(path.name for path in fonts.glob("OFL*.txt"))}):
        if (fonts / name).is_file():
            additions["EPUB/fonts/" + name] = (fonts / name).read_bytes()
    if (ROOT / "LICENSE").is_file():
        additions["EPUB/LICENSE-original.txt"] = (ROOT / "LICENSE").read_bytes()
    if (ROOT / "NOTICE.md").is_file():
        additions["EPUB/NOTICE.md"] = (ROOT / "NOTICE.md").read_bytes()
    for license_file in sorted((ROOT / "LICENSES").glob("*.txt")):
        additions["EPUB/LICENSES/" + license_file.name] = license_file.read_bytes()
    if not additions:
        return
    temporary = path.with_suffix(".tmp.epub")
    with zipfile.ZipFile(path) as source, zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as destination:
        opf = next(name for name in source.namelist() if name.endswith(".opf"))
        root = ET.fromstring(source.read(opf))
        ns = "http://www.idpf.org/2007/opf"
        manifest = root.find(f"{{{ns}}}manifest")
        for i, name in enumerate(additions):
            ET.SubElement(manifest, f"{{{ns}}}item", {"id": f"export-license-{i}", "href": os.path.relpath(name, str(Path(opf).parent)),
                          "media-type": "application/json" if name.endswith(".json") else "text/plain"})
        for info in source.infolist():
            value = ET.tostring(root, encoding="utf-8", xml_declaration=True) if info.filename == opf else source.read(info.filename)
            destination.writestr(info, value)
        for name, value in additions.items():
            destination.writestr(name, value)
    temporary.replace(path)


def build(docs: Path, output: Path, with_epub: bool = True, require_fonts: bool = True) -> dict:
    docs = docs.resolve()
    output.mkdir(parents=True, exist_ok=True)
    web = output / "html"
    web.mkdir(exist_ok=True)
    pages = summary_pages(docs)
    for page in pages:
        namespace(page)
    errors = rewrite_links(pages, docs)
    if errors:
        raise ValueError("\n".join(errors[:50]))
    source_audit = audit_source_content(pages, docs)
    assets = ROOT / "export-assets"
    for item in ("screen.css", "offline.js"):
        shutil.copy2(assets / item, web / item)
    (web / "epub.css").unlink(missing_ok=True)
    if (docs / "assets").is_dir():
        shutil.copytree(docs / "assets", web / "assets", dirs_exist_ok=True)
        source_assets = [path for path in (docs / "assets").rglob("*") if path.is_file()]
        for path in source_assets:
            target = web / path.relative_to(docs)
            if hashlib.sha256(path.read_bytes()).digest() != hashlib.sha256(target.read_bytes()).digest():
                raise ValueError(f"Asset changed during export: {path}")
        source_audit["asset_files_copied_byte_for_byte"] = len(source_assets)
    # Other source-local downloads are retained too, if future docs use any.
    for page in pages:
        for tag in page.soup.select("[href], [src]"):
            raw = tag.get("src") or tag.get("href") or ""
            parsed = urlsplit(raw)
            if not parsed.scheme and parsed.path and not raw.startswith("#"):
                source = docs / unquote(parsed.path)
                if source.is_file() and not source.is_relative_to(docs / "assets"):
                    destination = web / source.relative_to(docs)
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, destination)
    fonts = assets / "fonts"
    font_files = sorted(fonts.glob("*.otf")) + sorted(fonts.glob("*.ttf"))
    if require_fonts and (not font_files or not (fonts / "OFL.txt").is_file()):
        raise ValueError("CJK fonts and export-assets/fonts/OFL.txt must be ready before export")
    if fonts.is_dir():
        shutil.copytree(fonts, web / "fonts", dirs_exist_ok=True)
    if (ROOT / "LICENSE").is_file():
        shutil.copy2(ROOT / "LICENSE", web / "LICENSE.txt")
    if (ROOT / "NOTICE.md").is_file():
        shutil.copy2(ROOT / "NOTICE.md", web / "NOTICE.md")
    if (ROOT / "LICENSES").is_dir():
        shutil.copytree(ROOT / "LICENSES", web / "LICENSES", dirs_exist_ok=True)
    content = "\n".join(chapter_html(page) for page in pages)
    toc = '<aside class="book-sidebar"><a class="book-brand" href="#' + pages[0].key + '">Proxmox VE <span>9.2.13 · 简体中文</span></a><label class="toc-search">筛选目录<input id="toc-filter" type="search" placeholder="章节名称" autocomplete="off"></label><nav aria-label="全书目录"><ol>'
    for page in pages:
        toc += f'<li data-depth="{page.depth}"><a href="#{page.key}">{html.escape(page.title)}</a></li>'
    toc += '</ol></nav><p class="offline-label">离线全书 · GNU FDL 1.3<br><a href="LICENSE.txt">原始许可证</a></p></aside>'
    controls = '<a class="skip-link" href="#book-content">跳到正文</a><button class="nav-toggle" type="button" aria-label="展开或收起目录" aria-expanded="false">目录</button>'
    index = document(content, "screen.css", controls + toc, True)
    (web / "index.html").write_text(index, encoding="utf-8")
    export_soup = BeautifulSoup(document(content, "html/screen.css"), "html.parser")
    for nav in export_soup.select(".chapter-nav"):
        nav.decompose()
    for details in export_soup.find_all("details"):
        details.name = "div"
        details["class"] = list(details.get("class", [])) + ["expanded-details"]
    for summary in export_soup.find_all("summary"):
        summary.name = "p"
        summary["class"] = ["details-title"]
    for image in export_soup.find_all("img"):
        image.attrs.pop("loading", None)
        image.attrs.pop("decoding", None)
    for tag in export_soup.select("[href], [src], [poster]"):
        for attr in ("href", "src", "poster"):
            raw = tag.get(attr)
            if raw and not raw.startswith("#") and not urlsplit(raw).scheme and not raw.startswith("html/"):
                tag[attr] = "html/" + raw
    exported = str(export_soup)
    (output / "book-export.html").write_text(exported, encoding="utf-8")
    report = {"version": VERSION, "source_summary": str(docs / "SUMMARY.md"), "source_content": source_audit, "html": audit_html(index, web),
              "export_html": audit_html(exported, output), "pages": [{"source": str(page.path.relative_to(docs)), "pagekey": page.key} for page in pages]}
    if with_epub:
        # Pandoc treats a surrounding <main> as one Div, preventing chapter
        # splitting. Derive its input from the shared full export and unwrap
        # structural containers only; all content and IDs remain intact.
        epub_soup = copy.deepcopy(export_soup)
        for wrapper in epub_soup.select("main.book-content, section.book-chapter"):
            wrapper.unwrap()
        for stylesheet in epub_soup.select('link[rel="stylesheet"]'):
            stylesheet.decompose()
        epub_input = output / "epub-input.html"
        epub_input.write_text(str(epub_soup), encoding="utf-8")
        command = [find_pandoc(), str(epub_input), "--from=html", "--to=epub3", "--standalone", "--toc", "--toc-depth=3", "--split-level=1", "--epub-title-page=false", "--syntax-highlighting=none",
                   "--metadata", f"title={TITLE}", "--metadata", "lang=zh-CN", "--metadata", "creator=Proxmox Server Solutions GmbH；非官方简体中文译本", "--metadata", "rights=GNU Free Documentation License 1.3 or later",
                   "--css", str(assets / "epub.css"), "--resource-path", str(output), "--output", str(output / EPUB_NAME)]
        for font in font_files:
            command.extend(["--epub-embed-font", str(font)])
        result = subprocess.run(command, capture_output=True, text=True, cwd=output)
        if result.returncode:
            raise RuntimeError("Pandoc EPUB export failed: " + result.stderr[-6000:])
        if result.stderr:
            (output / "epub-pandoc.log").write_text(result.stderr, encoding="utf-8")
        attach_epub_licenses(output / EPUB_NAME, fonts)
        report["epub"] = audit_epub(output / EPUB_NAME, [page.key for page in pages], export_soup.select_one("main.book-content").get_text())
    (output / "web-epub-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def self_test() -> None:
    example_body = '# 节点 API\n\n## 标题 <a id="name"></a>\n\n完整正文。\n'
    header = '---\nlayout:\n  outline:\n    visible: false\n---\n\n'
    assert render_markdown(header + example_body) == render_markdown(example_body)
    for ordinary in ('---\n普通正文\n---\n', '---\nlayout: unclosed\n',
                     '# 正文\n\n---\nlayout: not-at-start\n---\n',
                     '---\nvalue: !!python/object/apply:os.system ["false"]\n---\n'):
        assert strip_frontmatter(ordinary) == ordinary
    (ROOT / "builds").mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="export-test-", dir=ROOT / "builds") as temporary:
        base = Path(temporary)
        docs = base / "docs"
        docs.mkdir()
        (docs / "assets").mkdir()
        (docs / "assets/tiny.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" width="30" height="20"><rect width="30" height="20" fill="red"/></svg>')
        (docs / "SUMMARY.md").write_text('- [首页](README.md)\n- [命令](command.md)\n')
        (docs / "README.md").write_text('# 首页 <a id="top"></a>\n\n## 名称 <a id="name"></a>\n\n[跨页](command.md#name) ![图](assets/tiny.svg)\n\n{% hint style="danger" %}\n不可删除。\n{% endhint %}\n\n<table><tr><th>字段</th></tr><tr><td>值</td></tr></table>\n\n```text\n{% hint style="info" %}\n```\n')
        (docs / "command.md").write_text('# 命令\n\n## 名称 <a id="name"></a>\n\n[返回](README.md#name) [自身](#name)\n\n<details>\n<summary>参数</summary>\n\n完整内容\n\n</details>\n\n12. 列表\n\n    ```text\n    apt update\n    ```\n\n    {% hint style="warning" %}\n    必须先检查[返回](README.md#name)，并运行 `apt update`。\n    {% endhint %}\n13. 后续列表项\n')
        result = build(docs, base / "out", require_fonts=False)
        assert result["html"]["chapters"] == 2
        assert result["html"]["hints"] == 2
        assert result["html"]["tables"] == 1
        exported = (base / "out/book-export.html").read_text()
        assert "<details" not in exported and "完整内容" in exported
        assert 'src="html/assets/tiny.svg"' in exported
        assert '必须先检查<a href="#page-readme-' in exported
        assert result["html"]["code_blocks"] == 2
        print(json.dumps({"self_test": "passed", "epub": result["epub"]}, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-root", type=Path, default=ROOT / "docs")
    parser.add_argument("--output-root", type=Path, default=ROOT / "builds")
    parser.add_argument("--html-only", action="store_true", help="Write HTML first; leave EPUB for a subsequent run")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not (ROOT / "work/CHAPTER_LAYOUT_READY").is_file():
        parser.error("Waiting for work/CHAPTER_LAYOUT_READY; chapter layout must be final before exporting")
    result = build(args.docs_root, args.output_root.resolve(), not args.html_only)
    print(json.dumps({key: value for key, value in result.items() if key != "pages"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
