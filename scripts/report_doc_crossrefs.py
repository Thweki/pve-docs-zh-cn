#!/usr/bin/env python3
"""Report broken or ambiguous in-book links using offline export anchor rules.

Read only SUMMARY-listed pages; emit deterministic JSON to stdout. External
links, assets and code examples are outside this report's scope. No snapshot,
book build or network access is required. --check exits 1 if issues are found.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

from export_web_epub import ROOT, namespace, summary_pages


def build_report(docs: Path) -> dict:
    docs = docs.resolve()
    pages = summary_pages(docs)
    by_path = {page.path: page for page in pages}
    for page in pages:
        namespace(page)
    issues = []
    checked = 0
    for page in pages:
        # namespace removes empty heading bookmarks, just as the exporter
        # does. Inspect surviving reader-facing links, not those self-links.
        for ordinal, link in enumerate(page.soup.select("a[href]"), 1):
            raw = link["href"]
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc:
                continue
            target = (page.path.parent / unquote(parsed.path)).resolve() if parsed.path else page.path
            if target not in by_path and target.suffix != ".md":
                continue
            checked += 1
            fragment = unquote(parsed.fragment)
            candidates = []
            reason = None
            if not target.is_relative_to(docs):
                reason = "outside_docs"
            elif not target.is_file():
                reason = "missing_page"
            elif target not in by_path:
                reason = "page_not_in_book"
            else:
                other = by_path[target]
                targets = other.alias_targets.get(fragment, [])
                if not targets:
                    reason = "missing_fragment"
                elif len(targets) > 1:
                    reason = "ambiguous_fragment"
                    headings = {heading["id"]: heading for heading in other.headings}
                    candidates = [
                        {"href": "index.html#" + quote(ident, safe=""),
                         "title": headings[ident]["title"] if ident in headings else None}
                        for ident in targets
                    ]
            if reason:
                issues.append({
                    "source": page.path.relative_to(docs).as_posix(),
                    "link_index": ordinal,
                    "text": link.get_text(" ", strip=True),
                    "href": raw,
                    "target": target.relative_to(docs).as_posix() if target.is_relative_to(docs) else None,
                    "fragment": fragment,
                    "reason": reason,
                    "candidates": candidates,
                })
    counts = Counter(issue["reason"] for issue in issues)
    return {"schema_version": 1, "page_count": len(pages),
            "links_checked": checked, "links_resolved": checked - len(issues),
            "issue_count": len(issues), "issues_by_reason": dict(sorted(counts.items())),
            "issues": issues}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", type=Path, default=ROOT / "docs",
                        help="Markdown directory containing SUMMARY.md (default: repository docs)")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 when broken or ambiguous links are reported")
    args = parser.parse_args()
    try:
        report = build_report(args.docs)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.check and report["issue_count"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
