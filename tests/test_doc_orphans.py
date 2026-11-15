"""Offline navigation reachability fixtures; no rebuild or release outputs."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import report_doc_orphans


class OrphanReportTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.docs = self.base / "docs"
        self.write("SUMMARY.md", "- [Home](README.md)\n")
        self.write("README.md", "# 首页\n")

    def write(self, relative, text):
        path = self.docs / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def report(self):
        return report_doc_orphans.build_report(self.docs)

    def cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(Path(report_doc_orphans.__file__).resolve()),
             "--docs", str(self.docs), *arguments],
            cwd=self.base, capture_output=True, text=True, timeout=30,
        )

    def test_complete_navigation(self):
        self.write("SUMMARY.md", "[Home](README.md#top)\n[Again](./README.md)\n")
        self.assertEqual(self.report(), {
            "schema_version": 1,
            "summary": "SUMMARY.md",
            "counts": {"pages": 1, "listed": 1, "indirect": 0, "unreachable": 0},
            "indirect_pages": [],
            "unreachable_pages": [],
        })

    def test_indirect_pages_include_shortest_path_and_incoming_sources(self):
        self.write("README.md", "# 首页\n[long](a.md) [short](b.md)\n")
        self.write("a.md", "# A\n[hop](c.md)\n")
        self.write("b.md", "# B\n[target](target.md) [again](target.md#part)\n")
        self.write("c.md", "# C\n[target](target.md)\n")
        self.write("target.md", "# **目标** `API`\n")
        report = self.report()
        target = report["indirect_pages"][-1]
        self.assertEqual(target, {
            "path": "target.md", "title": "目标 API",
            "via": ["SUMMARY.md", "README.md", "b.md", "target.md"],
            "referenced_by": ["b.md", "c.md"],
        })
        self.assertEqual(report["counts"], {
            "pages": 5, "listed": 1, "indirect": 4, "unreachable": 0,
        })

    def test_isolated_cycles_and_self_links_are_unreachable(self):
        self.write("a.md", "# A\n[B](b.md) [self](a.md)\n")
        self.write("b.md", "# B\n[A](a.md)\n")
        self.write("alone.md", "# Alone\n[self](#alone)\n")
        self.assertEqual(self.report()["unreachable_pages"], [
            {"path": "a.md", "title": "A", "referenced_by": ["b.md"]},
            {"path": "alone.md", "title": "Alone", "referenced_by": []},
            {"path": "b.md", "title": "B", "referenced_by": ["a.md"]},
        ])

    def test_reference_and_html_links_and_encoded_relative_paths(self):
        self.write("SUMMARY.md", '- [chapter][ch]\n\n[ch]: <guide/start.md> "Title"\n')
        self.write("guide/start.md", '# Start\n<a href="../%E4%B8%AD%E6%96%87%20page.md?view=1#part">中</a>\n')
        self.write("中文 page.md", '# 中文\n[home](README.md)\n')
        report = self.report()
        self.assertEqual(report["counts"], {
            "pages": 3, "listed": 1, "indirect": 2, "unreachable": 0,
        })
        self.assertEqual(report["indirect_pages"][0]["via"],
                         ["SUMMARY.md", "guide/start.md", "中文 page.md", "README.md"])

    def test_prose_examples_comments_images_metadata_and_external_links_are_not_edges(self):
        self.write("SUMMARY.md", '''---
description: '[metadata](hidden.md)'
---
[Home](README.md)
hidden.md
`[inline](hidden.md)`
```
[fenced](hidden.md)
```
<!-- <a href="hidden.md">comment</a> -->
<pre><a href="hidden.md">example</a></pre>

![image](hidden.md)
[remote](https://example.test/hidden.md)
[protocol relative](//example.test/hidden.md)
[mail](mailto:hidden.md)
''')
        self.write("hidden.md", "# Hidden\n")
        self.assertEqual(self.report()["unreachable_pages"], [
            {"path": "hidden.md", "title": "Hidden", "referenced_by": []},
        ])

    def test_gitbook_hints_are_parsed_like_the_exporter(self):
        self.write("README.md", '''# Home
{% hint style="info" %}
[Useful](hint.md)
{% endhint %}
''')
        self.write("hint.md", "# Hint\n")
        self.assertEqual(self.report()["indirect_pages"][0]["path"], "hint.md")

    def test_only_existing_local_markdown_pages_can_be_edges(self):
        self.write("README.md", '''# Home
[missing](missing.md) [outside](../outside.md) [root](/hidden.md)
[encoded escape](%2E%2E/outside.md) [asset](asset.svg)
[self](?view=1#part) [summary](SUMMARY.md)
''')
        (self.base / "outside.md").write_text("# Outside", encoding="utf-8")
        self.write("asset.svg", '<a href="hidden.md">not Markdown</a>')
        self.write("hidden.md", "# Hidden\n")
        self.assertEqual(self.report()["counts"], {
            "pages": 2, "listed": 1, "indirect": 0, "unreachable": 1,
        })

    def test_empty_navigation_and_nested_summary_are_reported(self):
        self.write("SUMMARY.md", "# No links\n")
        self.write("guide/SUMMARY.md", "No heading\n")
        report = self.report()
        self.assertEqual(report["counts"]["unreachable"], 2)
        self.assertEqual(report["unreachable_pages"][1], {
            "path": "guide/SUMMARY.md", "title": "guide/SUMMARY.md", "referenced_by": [],
        })

    def test_missing_summary_and_invalid_markdown_fail_without_partial_json(self):
        (self.docs / "SUMMARY.md").unlink()
        result = self.cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("SUMMARY.md", result.stderr)
        self.write("SUMMARY.md", '[Home](README.md)\n')
        self.write("README.md", '{% hint style="info" %}\nUnclosed\n')
        result = self.cli()
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("README.md", result.stderr)

    def test_symlink_files_and_directories_are_rejected(self):
        for name, directory in (("alias.md", False), ("alias", True)):
            with self.subTest(name=name):
                alias = self.docs / name
                alias.symlink_to(self.docs if directory else self.docs / "README.md",
                                 target_is_directory=directory)
                try:
                    with self.assertRaisesRegex(ValueError, "[Ss]ymlink"):
                        self.report()
                finally:
                    alias.unlink()

    def test_cli_is_deterministic_read_only_and_check_is_opt_in(self):
        self.write("loose.md", "# 未收录\n")
        before = {p.relative_to(self.base): p.read_bytes()
                  for p in self.base.rglob("*") if p.is_file()}
        first, second, check = self.cli(), self.cli(), self.cli("--check")
        self.assertEqual((first.returncode, second.returncode, check.returncode), (0, 0, 1))
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stdout, check.stdout)
        self.assertEqual(json.loads(first.stdout), self.report())
        self.assertNotIn(str(self.base), first.stdout)
        self.assertIn("未收录", first.stdout)
        self.assertEqual(before, {p.relative_to(self.base): p.read_bytes()
                                 for p in self.base.rglob("*") if p.is_file()})
        self.write("SUMMARY.md", "[Home](README.md) [Loose](loose.md)\n")
        self.assertEqual(self.cli("--check").returncode, 0)

    def test_check_also_flags_indirect_pages_omitted_from_exports(self):
        self.write("README.md", "# Home\n[Indirect](indirect.md)\n")
        self.write("indirect.md", "# Indirect\n")
        result = self.cli("--check")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["counts"]["unreachable"], 0)


if __name__ == "__main__":
    unittest.main()
