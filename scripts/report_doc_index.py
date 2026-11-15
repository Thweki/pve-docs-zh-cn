#!/usr/bin/env python3
"""Print a SUMMARY-ordered JSON heading index without building the offline book.

Paths are relative to --docs; hrefs are relative to the offline HTML directory.
Only SUMMARY-listed pages are included. --query filters heading titles by a
case-insensitive substring, retaining their original order and export anchors.
This is a navigation catalog, not a link or publication-integrity audit.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from urllib.parse import quote

from export_web_epub import ROOT, namespace, summary_pages


def build_index(docs: Path, query: str = "") -> dict:
    docs = docs.resolve()
    pages = []
    needle = query.casefold()
    for page in summary_pages(docs):
        # Assign every anchor before filtering so duplicate titles keep exactly
        # the same suffixes as a full HTML export.
        namespace(page)
        headings = [
            {"title": heading["title"], "level": heading["level"],
             "href": "index.html#" + quote(heading["id"], safe="")}
            for heading in page.headings
            if needle in heading["title"].casefold()
        ]
        if headings:
            pages.append({
                "path": page.path.relative_to(docs).as_posix(),
                "title": page.title,
                "depth": page.depth,
                "href": "index.html#" + quote(page.key, safe=""),
                "headings": headings,
            })
    return {"schema_version": 1, "page_count": len(pages),
            "heading_count": sum(len(page["headings"]) for page in pages),
            "pages": pages}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", type=Path, default=ROOT / "docs",
                        help="Markdown directory containing SUMMARY.md (default: repository docs)")
    parser.add_argument("--query", default="",
                        help="case-insensitive substring of a heading title")
    args = parser.parse_args()
    try:
        report = build_index(args.docs, args.query)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
