#!/usr/bin/env python3
"""Report page reachability from SUMMARY without rebuilding or changing docs."""
from __future__ import annotations

import argparse
from collections import deque
import json
import os
from pathlib import Path
import posixpath
import stat
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

from export_web_epub import ROOT, render_markdown

SUMMARY = "SUMMARY.md"


def markdown_files(docs: Path) -> dict[str, Path]:
    """Inventory the tree without following symlinks or silently skipping errors."""
    def walk_error(error):
        raise error

    files = {}
    for parent, directories, names in os.walk(docs, followlinks=False, onerror=walk_error):
        for name in directories + names:
            path = Path(parent) / name
            relative = path.relative_to(docs).as_posix()
            if path.is_symlink() and (name in directories or path.suffix == ".md"):
                raise ValueError(f"Symlink documentation path: {relative}")
            if name in names and path.suffix == ".md":
                if not stat.S_ISREG(path.stat().st_mode):
                    raise ValueError(f"Non-regular Markdown file: {relative}")
                files[relative] = path
    if SUMMARY not in files:
        raise ValueError("Documentation root must contain SUMMARY.md")
    return dict(sorted(files.items()))


def local_page(source: str, href: str, files: dict[str, Path]) -> str | None:
    """Resolve only relative links to inventoried pages; never open link targets.

    This is a page graph, not an anchor/link validator. Query strings and
    fragments do not change the page reached. Directory shorthand, absolute
    paths, missing pages, assets and external URLs do not create graph edges.
    """
    try:
        parsed = urlsplit(href)
    except ValueError:
        return None
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if path.startswith("/") or "\\" in path:
        return None
    target = posixpath.normpath(posixpath.join(posixpath.dirname(source), path)) if path else source
    if target in files and target not in {source, SUMMARY}:
        return target
    return None


def build_report(docs: Path) -> dict:
    files = markdown_files(docs)
    outgoing = {name: set() for name in files}
    incoming = {name: set() for name in files}
    titles = {}
    for name, path in files.items():
        try:
            soup = BeautifulSoup(render_markdown(path.read_text(encoding="utf-8")), "html.parser")
        except (OSError, ValueError) as error:
            raise ValueError(f"Cannot parse {name}: {error}") from error
        heading = soup.find("h1")
        titles[name] = heading.get_text(" ", strip=True) if heading else name
        for link in soup.select("a[href]"):
            if link.find_parent(["pre", "code", "script", "style", "template"]):
                continue
            target = local_page(name, link["href"], files)
            if target is not None:
                outgoing[name].add(target)
                incoming[target].add(name)

    # A breadth-first walk finds the shortest route from navigation, without
    # mistaking backlinks within an isolated cycle for a route into that cycle.
    predecessor = {SUMMARY: None}
    pending = deque([SUMMARY])
    while pending:
        source = pending.popleft()
        for target in sorted(outgoing[source]):
            if target not in predecessor:
                predecessor[target] = source
                pending.append(target)

    indirect, unreachable = [], []
    for name in files:
        if name == SUMMARY or name in outgoing[SUMMARY]:
            continue
        entry = {"path": name, "title": titles[name], "referenced_by": sorted(incoming[name])}
        if name in predecessor:
            route = []
            step = name
            while step is not None:
                route.append(step)
                step = predecessor[step]
            entry["via"] = list(reversed(route))
            indirect.append(entry)
        else:
            unreachable.append(entry)
    return {
        "schema_version": 1,
        "summary": SUMMARY,
        "counts": {
            "pages": len(files) - 1,
            "listed": len(outgoing[SUMMARY]),
            "indirect": len(indirect),
            "unreachable": len(unreachable),
        },
        "indirect_pages": indirect,
        "unreachable_pages": unreachable,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", type=Path, default=ROOT / "docs", help="documentation root (default: repository docs)")
    parser.add_argument("--check", action="store_true", help="exit 1 if any page is absent from SUMMARY; still print the report")
    args = parser.parse_args()
    try:
        report = build_report(args.docs)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return int(args.check and bool(report["indirect_pages"] or report["unreachable_pages"]))


if __name__ == "__main__":
    raise SystemExit(main())
