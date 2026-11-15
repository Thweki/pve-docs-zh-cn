"""Validate HTML and its transitive CSS resources without fetching any URLs."""
from __future__ import annotations

from collections import Counter
import base64
from pathlib import Path
import re
from urllib.parse import unquote, unquote_to_bytes, urlsplit

from bs4 import BeautifulSoup


# Tokenize strings/comments before identifiers so apparent URLs inside either
# cannot become dependencies. CSS escapes apply to both identifiers and URLs.
_ESCAPE = r"\\(?:[0-9a-fA-F]{1,6}(?:\r\n|[ \t\r\n\f])?|[^\r\n\f0-9a-fA-F])"
_IDENT = rf"(?:[_a-zA-Z-]|[^\x00-\x7f]|{_ESCAPE})(?:[\w-]|[^\x00-\x7f]|{_ESCAPE})*"
_TOKEN = re.compile(
    rf'''(?P<comment>/\*.*?(?:\*/|\Z))|(?P<space>\s+)|'''
    rf'''(?P<string>"(?:\\(?:\r\n|[\s\S])|[^"\\\r\n])*"|'(?:\\(?:\r\n|[\s\S])|[^'\\\r\n])*')|'''
    rf"(?P<ident>{_IDENT})|(?P<other>.)", re.DOTALL,
)


def css_unescape(value: str) -> str:
    def replace(match: re.Match) -> str:
        escaped = match[0][1:]
        if escaped in ("\n", "\r", "\r\n", "\f"):
            return ""
        digits = re.match(r"[0-9a-fA-F]{1,6}", escaped)
        if digits:
            code = int(digits[0], 16)
            return chr(code) if 0 < code <= 0x10ffff and not 0xd800 <= code <= 0xdfff else "\ufffd"
        return escaped
    return re.sub(r"\\(?:\r\n|[0-9a-fA-F]{1,6}(?:\r\n|[ \t\r\n\f])?|[\s\S])", replace, value)


def css_references(css: str):
    """Yield (URL, is_import) for url(), image-set() and CSS @import.

    This is a dependency scanner, not a CSS validity checker. It deliberately
    checks all media/supports branches, even those inactive on this machine.
    """
    tokens = [(match.lastgroup, match[0]) for match in _TOKEN.finditer(css)
              if match.lastgroup not in {"comment", "space"}]
    i = 0
    importing = False
    functions = []
    while i < len(tokens):
        kind, value = tokens[i]
        if value == "@" and i + 1 < len(tokens) and tokens[i + 1][0] == "ident":
            importing = css_unescape(tokens[i + 1][1]).lower() == "import"
            i += 2
            continue
        if importing and kind == "string":
            yield css_unescape(value[1:-1]), True
        elif kind == "string" and functions and functions[-1] in {"image-set", "-webkit-image-set"}:
            yield css_unescape(value[1:-1]), False
        elif kind == "ident" and css_unescape(value).lower() == "url" and i + 1 < len(tokens) and tokens[i + 1][1] == "(":
            end = i + 2
            while end < len(tokens) and tokens[end][1] != ")":
                end += 1
            values = tokens[i + 2:end]
            if end == len(tokens) or not values:
                raise ValueError("Malformed CSS url() dependency")
            if len(values) == 1 and values[0][0] == "string":
                raw = values[0][1][1:-1]
            else:
                if any(k == "string" or v in {'"', "'", "("} for k, v in values):
                    raise ValueError("Malformed CSS url() dependency")
                raw = "".join(v for _, v in values)
            yield css_unescape(raw), importing
            i = end
        elif value == "(":
            previous = tokens[i - 1] if i else (None, "")
            functions.append(css_unescape(previous[1]).lower() if previous[0] == "ident" else "")
        elif value == ")" and functions:
            functions.pop()
        importing = False
        i += 1


def srcset_urls(value: str):
    """Read image candidates, retaining commas within data URLs."""
    while value:
        value = value.lstrip(" \t\r\n\f,")
        if not value:
            return
        match = re.match(r"[^ \t\r\n\f]+", value)
        raw = match[0]
        yield raw.rstrip(",")
        value = value[len(raw):]
        if raw.endswith(","):
            continue
        # Descriptors end at a comma outside parentheses (HTML srcset grammar).
        depth = 0
        for i, char in enumerate(value):
            if char == "(":
                depth += 1
            elif char == ")":
                depth = max(0, depth - 1)
            elif char == "," and depth == 0:
                value = value[i + 1:]
                break
        else:
            return


def audit_html(text: str, base: Path) -> dict:
    """Check anchors and embedded resources, confined to the packaged tree."""
    base = base.resolve()
    soup = BeautifulSoup(text, "html.parser")
    ids = Counter(tag["id"] for tag in soup.select("[id]"))
    errors = [f"Duplicate ID {key}" for key, count in ids.items() if count != 1]
    links = 0
    for link in soup.select("a[href]"):
        href = link["href"]
        parsed = urlsplit(href)
        if href.startswith("#"):
            links += 1
            if unquote(parsed.fragment) not in ids:
                errors.append(f"Broken single-page anchor {href}")
        elif not parsed.scheme and not parsed.netloc and unquote(parsed.path).endswith(".md"):
            errors.append(f"Unrewritten Markdown link {href}")

    visited: set[Path] = set()

    def stylesheet(css: str, directory: Path | None) -> None:
        try:
            for raw, imported in css_references(css):
                dependency(raw, directory, imported)
        except ValueError as error:
            errors.append(str(error))

    def dependency(raw: str, directory: Path | None, is_css: bool = False) -> None:
        raw = raw.strip()
        parsed = urlsplit(raw)
        if parsed.scheme.lower() == "data":
            if is_css:
                try:
                    header, payload = raw.split(",", 1)
                    data = unquote_to_bytes(payload)
                    if header.lower().endswith(";base64"):
                        data = base64.b64decode(data, validate=True)
                    stylesheet(data.decode("utf-8-sig"), None)
                except (ValueError, UnicodeError) as error:
                    errors.append(f"Invalid embedded stylesheet: {error}")
            return
        if parsed.scheme or parsed.netloc or raw.startswith(("//", "\\")):
            errors.append(f"Remote dependency {raw}")
            return
        # Fragment-only references (e.g. SVG filters) use the current document.
        if raw.startswith("#"):
            return
        if directory is None:
            errors.append(f"Relative dependency in embedded data stylesheet {raw}")
            return
        path = (directory / unquote(parsed.path)).resolve()
        if not path.is_relative_to(base):
            errors.append(f"Dependency outside packaged directory {raw}")
        elif not path.is_file():
            errors.append(f"Missing packaged dependency {raw}")
        elif is_css and path not in visited:
            visited.add(path)  # Mark before recursion: circular imports are legal.
            stylesheet(path.read_text(encoding="utf-8-sig"), path.parent)

    # Navigation anchors remain external-capable; these attributes embed data.
    for tag in soup.select("[src], [poster], object[data], link[href], image, use, [srcset], [imagesrcset]"):
        for attr in ("src", "poster", "data" if tag.name == "object" else ""):
            if attr and tag.has_attr(attr):
                dependency(tag[attr], base)
        for attr in ("srcset", "imagesrcset"):
            for raw in srcset_urls(tag.get(attr, "")):
                dependency(raw, base)
        if tag.name == "link":
            rel = {value.lower() for value in tag.get("rel", [])}
            if rel & {"stylesheet", "icon", "apple-touch-icon", "mask-icon", "preload", "modulepreload", "manifest", "prefetch"}:
                dependency(tag["href"], base, "stylesheet" in rel or tag.get("as") == "style")
        elif tag.name in {"image", "use"}:
            for attr in ("href", "xlink:href"):
                if tag.has_attr(attr):
                    dependency(tag[attr], base)
    for tag in soup.select("style, [style]"):
        if tag.name == "style":
            stylesheet(tag.get_text(), base)
        if tag.has_attr("style"):
            stylesheet(tag["style"], base)
    if soup.select_one("base[href]"):
        errors.append("HTML base URLs are not supported in offline exports")
    if errors:
        raise ValueError("\n".join(errors[:40]))
    return {"chapters": len(soup.select("section.book-chapter")), "headings": len(soup.select("h1,h2,h3,h4,h5,h6")),
            "ids": len(ids), "internal_links": links, "images": len(soup.select("img")),
            "tables": len(soup.select("table")), "code_blocks": len(soup.select("pre")), "hints": len(soup.select(".hint"))}
