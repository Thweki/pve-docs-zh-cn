"""Temporary-fixture tests for the read-only Markdown size report."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import report_doc_sizes as sizes


class DocSizeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.docs = self.root / "docs"
        self.docs.mkdir()

    def write(self, name, content):
        path = self.docs / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(Path(sizes.__file__)),
             "--docs", str(self.docs), *args],
            cwd=self.root, capture_output=True, text=True, timeout=10,
        )

    def baseline(self):
        path = self.root / "baseline.json"
        path.write_text(json.dumps(sizes.build_report(self.docs)), encoding="utf-8")
        return path

    def test_counts_utf8_bytes_and_only_markdown(self):
        self.write("guide/README.md", "中文\n".encode())
        self.write("SUMMARY.md", b"summary")
        self.write("assets/image.png", b"ignored")
        self.write("api/empty.md", b"")
        report = sizes.build_report(self.docs)
        self.assertEqual(report["schema_version"], 1)
        self.assertEqual(report["total_bytes"], 14)
        self.assertEqual(report["page_count"], 3)
        self.assertEqual(report["pages"], [
            {"path": "SUMMARY.md", "bytes": 7},
            {"path": "api/empty.md", "bytes": 0},
            {"path": "guide/README.md", "bytes": 7},
        ])
        self.assertNotIn("comparison", report)

    def test_comparison_accounts_for_added_removed_changed_and_unchanged(self):
        self.write("grow.md", b"a")
        self.write("shrink.md", b"1234")
        self.write("removed.md", b"12")
        self.write("same.md", b"x")
        baseline = sizes.build_report(self.docs)
        self.write("grow.md", b"1234")
        self.write("shrink.md", b"1")
        (self.docs / "removed.md").unlink()
        self.write("new.md", b"12345")
        self.write("same.md", b"y")
        report = sizes.build_report(self.docs, baseline)
        comparison = report["comparison"]
        self.assertEqual(comparison["total_delta_bytes"], 3)
        self.assertEqual(comparison["changes"], [
            {"path": "new.md", "status": "added", "before_bytes": 0, "bytes": 5, "delta_bytes": 5},
            {"path": "grow.md", "status": "changed", "before_bytes": 1, "bytes": 4, "delta_bytes": 3},
            {"path": "removed.md", "status": "removed", "before_bytes": 2, "bytes": 0, "delta_bytes": -2},
            {"path": "shrink.md", "status": "changed", "before_bytes": 4, "bytes": 1, "delta_bytes": -3},
        ])

    def test_zero_byte_addition_and_removal_are_visible(self):
        self.write("old.md", b"")
        baseline = sizes.build_report(self.docs)
        (self.docs / "old.md").unlink()
        self.write("new.md", b"")
        changes = sizes.build_report(self.docs, baseline)["comparison"]["changes"]
        self.assertEqual([(c["path"], c["status"]) for c in changes],
                         [("new.md", "added"), ("old.md", "removed")])

    def test_cli_budget_is_per_page_and_inclusive(self):
        self.write("grow.md", b"1")
        self.write("shrink.md", b"123456789")
        baseline = self.baseline()
        self.write("grow.md", b"1234")
        self.write("shrink.md", b"")
        for limit, code, exceeded in [(3, 0, []), (2, 1, ["grow.md"])]:
            with self.subTest(limit=limit):
                result = self.cli("--baseline", str(baseline), "--max-growth-bytes", str(limit), "--format", "json")
                self.assertEqual(result.returncode, code, result.stderr)
                self.assertEqual(json.loads(result.stdout)["budget"]["exceeded"], exceeded)
        self.assertEqual(self.cli("--baseline", str(baseline)).returncode, 0)

    def test_new_page_is_budgeted_from_zero(self):
        self.write("old.md", b"a")
        baseline = self.baseline()
        self.write("new.md", b"x")
        result = self.cli("--baseline", str(baseline), "--max-growth-bytes", "0")
        self.assertEqual(result.returncode, 1)
        self.assertIn("new.md", result.stdout)
        self.assertIn("Growth budget exceeded", result.stdout)

    def test_json_is_repeatable_and_command_does_not_write(self):
        self.write("b.md", b"123")
        self.write("a.md", b"123")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        first = self.cli("--format", "json")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, self.cli("--format", "json").stdout)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_report_can_be_reused_as_a_baseline(self):
        self.write("a.md", b"a")
        original = sizes.build_report(self.docs)
        self.write("a.md", b"aa")
        compared = sizes.build_report(self.docs, original)
        again = sizes.build_report(self.docs, compared)
        self.assertEqual(again["comparison"]["changes"], [])
        self.assertEqual(again["comparison"]["total_delta_bytes"], 0)

    def test_markdown_ranks_largest_pages_and_escapes_paths(self):
        self.write("small.md", b"a")
        self.write("<large>|`.md", b"1234")
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("&lt;large&gt;&#124;&#96;.md", result.stdout)
        self.assertLess(result.stdout.index("&lt;large&gt;"), result.stdout.index("small.md"))

    def test_missing_empty_or_non_directory_docs_fail(self):
        for path in [self.docs, self.root / "missing", self.write("file.txt", b"x")]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                sizes.build_report(path)

    def test_symlink_page_directory_and_root_are_rejected(self):
        self.write("a.md", b"a")
        for name, target in [("linked.md", self.docs / "a.md"), ("linked-dir", self.docs)]:
            link = self.docs / name
            link.symlink_to(target)
            with self.subTest(name=name), self.assertRaises(ValueError):
                sizes.build_report(self.docs)
            link.unlink()
        link = self.root / "linked-root"
        link.symlink_to(self.docs)
        with self.assertRaises(ValueError):
            sizes.build_report(link)

    def test_invalid_baselines_fail_without_echoing_contents(self):
        self.write("a.md", b"a")
        for value in [[], {}, {"schema_version": 2, "pages": []},
                      {"schema_version": 1, "pages": [{"path": "a.md", "bytes": -1}]},
                      {"schema_version": 1, "pages": [{"path": "a.md", "bytes": True}]},
                      {"schema_version": 1, "pages": [{"path": "../a.md", "bytes": 1}]},
                      {"schema_version": 1, "pages": [{"path": "a.md", "bytes": 1}] * 2}]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                sizes.build_report(self.docs, value)
        path = self.root / "bad.json"
        path.write_text("PRIVATE_TEST_CONTENT", encoding="utf-8")
        result = self.cli("--baseline", str(path))
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("PRIVATE_TEST_CONTENT", result.stdout + result.stderr)
        self.assertNotIn("Traceback", result.stderr)

    def test_invalid_budget_arguments_fail(self):
        self.write("a.md", b"a")
        baseline = self.baseline()
        for args in [("--max-growth-bytes", "0"),
                     ("--baseline", str(baseline), "--max-growth-bytes", "-1")]:
            with self.subTest(args=args):
                self.assertEqual(self.cli(*args).returncode, 2)


if __name__ == "__main__":
    unittest.main()
