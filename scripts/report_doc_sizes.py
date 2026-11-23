#!/usr/bin/env python3
"""Report Markdown byte sizes and optional per-page growth against a JSON baseline.

Read-only, offline, and standard-library only. This measures source Markdown,
not rendered HTML size, browser performance, or documentation completeness.
"""
from __future__ import annotations

import argparse
import html
import json
import os
from pathlib import Path, PurePosixPath
import stat

ROOT = Path(__file__).resolve().parents[1]


def page_sizes(docs: Path) -> dict[str, int]:
    if docs.is_symlink() or not docs.is_dir():
        raise ValueError("Docs must be an existing directory, not a symlink")
    pages = {}

    def walk_error(error):
        raise error

    for parent, directories, files in os.walk(docs, onerror=walk_error, followlinks=False):
        for name in directories:
            if (Path(parent) / name).is_symlink():
                raise ValueError("Symlink directories are not supported in docs")
        for name in files:
            if not name.endswith(".md"):
                continue
            path = Path(parent) / name
            info = path.lstat()
            if not stat.S_ISREG(info.st_mode):
                raise ValueError("Markdown pages must be regular files, not symlinks")
            pages[path.relative_to(docs).as_posix()] = info.st_size
    if not pages:
        raise ValueError("No Markdown pages found in docs")
    return dict(sorted(pages.items()))


def baseline_sizes(report: object) -> dict[str, int]:
    """Validate the versioned page inventory; recompute totals from that inventory."""
    if (not isinstance(report, dict) or type(report.get("schema_version")) is not int
            or report["schema_version"] != 1 or not isinstance(report.get("pages"), list)):
        raise ValueError("Baseline must be a schema_version 1 size report with pages")
    pages = {}
    for page in report["pages"]:
        if not isinstance(page, dict):
            raise ValueError("Invalid baseline page record")
        path, size = page.get("path"), page.get("bytes")
        if (not isinstance(path, str) or not path.endswith(".md")
                or PurePosixPath(path).is_absolute() or "\\" in path or ":" in path
                or any(part in {"", ".", ".."} for part in path.split("/"))
                or path in pages or type(size) is not int or size < 0):
            raise ValueError("Baseline pages require unique relative Markdown paths and nonnegative integer bytes")
        pages[path] = size
    return pages


def build_report(docs: Path, baseline: object = None) -> dict:
    pages = page_sizes(docs)
    report = {
        "schema_version": 1,
        "page_count": len(pages),
        "total_bytes": sum(pages.values()),
        "pages": [{"path": path, "bytes": size} for path, size in pages.items()],
    }
    if baseline is not None:
        before = baseline_sizes(baseline)
        changes = []
        for path in pages.keys() | before.keys():
            if path in pages and path in before and pages[path] == before[path]:
                continue
            changes.append({
                "path": path,
                "status": "added" if path not in before else "removed" if path not in pages else "changed",
                "before_bytes": before.get(path, 0),
                "bytes": pages.get(path, 0),
                "delta_bytes": pages.get(path, 0) - before.get(path, 0),
            })
        report["comparison"] = {
            "total_delta_bytes": sum(pages.values()) - sum(before.values()),
            "changes": sorted(changes, key=lambda page: (-page["delta_bytes"], page["path"])),
        }
    return report


def markdown_report(report: dict) -> str:
    def escape(path):
        return (html.escape(path).replace("|", "&#124;").replace("`", "&#96;")
                .replace("\n", "&#10;").replace("\r", "&#13;"))

    lines = ["# Documentation size report", "",
             f"{report['page_count']} Markdown pages; {report['total_bytes']:,} bytes.", "",
             "Largest pages (up to 10; paths relative to docs):", "",
             "| Page | Bytes |", "| --- | ---: |"]
    for page in sorted(report["pages"], key=lambda page: (-page["bytes"], page["path"]))[:10]:
        lines.append(f"| {escape(page['path'])} | {page['bytes']:,} |")
    if "comparison" in report:
        comparison = report["comparison"]
        lines += ["", f"Total change: {comparison['total_delta_bytes']:+,} bytes.", "",
                  "| Page | Status | Before | Now | Delta |", "| --- | --- | ---: | ---: | ---: |"]
        for page in comparison["changes"]:
            lines.append(f"| {escape(page['path'])} | {page['status']} | {page['before_bytes']:,} | "
                         f"{page['bytes']:,} | {page['delta_bytes']:+,} |")
        if not comparison["changes"]:
            lines += ["", "No page size changes."]
    if "budget" in report:
        budget = report["budget"]
        lines += ["", f"Per-page growth budget: {budget['max_growth_bytes']:,} bytes."]
        if budget["exceeded"]:
            lines += ["", "Growth budget exceeded:"]
            lines += [f"- {escape(path)}" for path in budget["exceeded"]]
        else:
            lines += ["", "Growth budget passed."]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs", type=Path, default=ROOT / "docs", help="Markdown tree to measure")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--baseline", type=Path, help="JSON output from an earlier run")
    parser.add_argument("--max-growth-bytes", type=int,
                        help="Fail if any page grows by more than this many bytes; requires --baseline")
    args = parser.parse_args()
    if args.max_growth_bytes is not None and (args.baseline is None or args.max_growth_bytes < 0):
        parser.error("--max-growth-bytes requires --baseline and a nonnegative integer")
    try:
        baseline = None
        if args.baseline is not None:
            baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
            baseline_sizes(baseline)
        report = build_report(args.docs, baseline)
    except (OSError, ValueError) as error:
        # Never echo file contents, including malformed JSON or undecodable bytes.
        if isinstance(error, (json.JSONDecodeError, UnicodeError)):
            parser.error("Baseline must contain valid UTF-8 JSON")
        parser.error(str(error))
    exceeded = []
    if args.max_growth_bytes is not None:
        exceeded = [page["path"] for page in report["comparison"]["changes"]
                    if page["delta_bytes"] > args.max_growth_bytes]
        report["budget"] = {"max_growth_bytes": args.max_growth_bytes, "exceeded": exceeded}
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(markdown_report(report), end="")
    return 1 if exceeded else 0


if __name__ == "__main__":
    raise SystemExit(main())
