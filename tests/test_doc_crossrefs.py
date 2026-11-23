"""Read-only cross-reference diagnostics using the real export anchor rules."""
import importlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


class DocumentationCrossrefTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for name in ("bs4", "markdown_it", "yaml"):
            try:
                importlib.import_module(name)
            except ImportError as error:
                raise unittest.SkipTest(f"{name} unavailable: {error}") from error
        cls.reporter = importlib.import_module("report_doc_crossrefs")
        cls.exporter = importlib.import_module("export_web_epub")

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.docs = Path(temporary.name) / "docs"
        self.docs.mkdir()
        self.write("SUMMARY.md", "- [首页](README.md)\n- [API 导航](<章节/API 中文.md>)\n")
        self.write("README.md", "# 首页\n")
        self.write("章节/API 中文.md",
                   '## GET `/nodes` <a id="api/nodes?x#y"></a>\n\n'
                   '## Backup {#backup}\n\n'
                   '## 重复\n\n## 重复\n')

    def write(self, path, text):
        target = self.docs / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def report(self):
        return self.reporter.build_report(self.docs)

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts/report_doc_crossrefs.py"),
             "--docs", "docs", *args], cwd=self.docs.parent,
            capture_output=True, text=True, encoding="utf-8", timeout=30)

    def test_resolves_heading_aliases_encoded_paths_queries_and_page_tops(self):
        self.write("README.md", '# 首页\n\n'
                   '[top](#) [self](#首页) [query](?view=full#首页)\n\n'
                   '[page](<章节/API 中文.md>)\n\n'
                   '[API](章节/API%20中文.md?view=full#api%2Fnodes%3Fx%23y)\n\n'
                   '[slug](章节/API%20中文.md#get-nodes)\n\n'
                   '[explicit](章节/API%20中文.md#backup)\n\n'
                   '[synthetic](章节/API%20中文.md#api-导航)\n')
        report = self.report()
        self.assertEqual(report["links_checked"], 8)
        self.assertEqual(report["links_resolved"], 8)
        self.assertEqual(report["issues"], [])
        pages = self.exporter.summary_pages(self.docs)
        for page in pages:
            self.exporter.namespace(page)
        self.assertEqual(self.exporter.rewrite_links(pages, self.docs), [])

    def test_reports_broken_targets_in_document_order(self):
        self.write("README.md", '# 首页\n\n'
                   '[anchor](#gone) [file](missing.md#gone)\n\n'
                   '[unpublished](draft.md#exists) [escape](../outside.md)\n')
        self.write("draft.md", '# Draft <a id="exists"></a>\n[ignored](missing.md)\n')
        report = self.report()
        self.assertEqual(report["page_count"], 2)
        self.assertEqual(report["links_checked"], 4)
        self.assertEqual(report["links_resolved"], 0)
        self.assertEqual([i["reason"] for i in report["issues"]],
                         ["missing_fragment", "missing_page", "page_not_in_book", "outside_docs"])
        self.assertEqual([i["link_index"] for i in report["issues"]], [1, 2, 3, 4])
        self.assertTrue(all(i["source"] == "README.md" for i in report["issues"]))
        self.assertEqual(report["issues"][0]["target"], "README.md")
        self.assertEqual(report["issues"][0]["text"], "anchor")
        self.assertIsNone(report["issues"][-1]["target"])

    def test_repeated_titles_are_ambiguous_with_real_export_candidates(self):
        self.write("README.md", '# 首页\n\n[重复章节](章节/API%20中文.md#重复)\n')
        report = self.report()
        self.assertEqual(report["issues_by_reason"], {"ambiguous_fragment": 1})
        issue = report["issues"][0]
        self.assertEqual(issue["fragment"], "重复")
        candidates = issue["candidates"]
        self.assertEqual([c["title"] for c in candidates], ["重复", "重复"])
        self.assertEqual(len({c["href"] for c in candidates}), 2)
        pages = self.exporter.summary_pages(self.docs)
        for page in pages:
            self.exporter.namespace(page)
        self.assertEqual(self.exporter.rewrite_links(pages, self.docs), [])
        ids = [unquote(c["href"].split("#", 1)[1]) for c in candidates]
        # The exporter still chooses the first alias, and both candidates
        # identify distinct headings in its actual output.
        self.assertEqual(pages[0].soup.select_one("a[href]")["href"], "#" + ids[0])
        chapter = self.exporter.BeautifulSoup(self.exporter.chapter_html(pages[1]), "html.parser")
        for ident in ids:
            self.assertEqual(len(chapter.find_all(id=ident)), 1)

    def test_explicit_alias_and_slug_collisions_include_nonheading_bookmarks(self):
        self.write("README.md", '# 首页\n\n'
                   '## One <a id="shared"></a> <a name="shared"></a>\n\n'
                   '## Shared\n\n<div id="shared">Bookmark</div>\n\n'
                   '[collision](#shared)\n')
        issue = self.report()["issues"][0]
        self.assertEqual(issue["reason"], "ambiguous_fragment")
        self.assertEqual([c["title"] for c in issue["candidates"]], ["One", "Shared", None])

    def test_duplicate_explicit_ids_on_different_headings_are_ambiguous(self):
        self.write("README.md", '# 首页\n\n'
                   '## One <a id="same"></a>\n\n'
                   '## Two <a id="same"></a>\n\n[duplicate](#same)\n')
        issue = self.report()["issues"][0]
        self.assertEqual(issue["reason"], "ambiguous_fragment")
        self.assertEqual([c["title"] for c in issue["candidates"]], ["One", "Two"])

    def test_same_heading_alias_repetition_is_not_ambiguous(self):
        self.write("README.md", '# 首页\n\n'
                   '## Shared <a id="shared"></a> <a name="shared"></a> {#shared}\n\n'
                   '[valid](#shared)\n')
        self.assertEqual(self.report()["issues"], [])
        self.assertEqual(self.report()["links_resolved"], 1)

    def test_reference_links_html_tables_hints_and_relative_parent_links(self):
        self.write("章节/API 中文.md", '# API\n\n'
                   '[parent][home]\n\n[home]: ../README.md#首页\n\n'
                   '| Link |\n| --- |\n| [broken](#table) |\n\n'
                   '{% hint style="info" %}\n[broken](#hint)\n{% endhint %}\n\n'
                   '<div><a href="#html">HTML</a></div>\n')
        report = self.report()
        self.assertEqual((report["links_checked"], report["links_resolved"]), (4, 1))
        self.assertEqual([i["fragment"] for i in report["issues"]], ["table", "hint", "html"])
        self.assertTrue(all(i["source"] == "章节/API 中文.md" for i in report["issues"]))

    def test_ignores_external_assets_code_metadata_and_empty_heading_selflinks(self):
        self.write("README.md", '---\ntitle: "[metadata](missing.md)"\n---\n'
                   '# 首页 <a href="#missing" id="top"></a>\n\n'
                   '[external](https://example.org/a.md#missing) [cdn](//example.org/a.md)\n\n'
                   '[mail](mailto:a@example.org) [asset](missing.svg#shape)\n\n'
                   '![image](missing.md)\n\n`[inline](missing.md)`\n\n'
                   '```markdown\n[code](missing.md)\n<a href="#missing">Fake</a>\n```\n\n'
                   '    [indented](missing.md)\n\n<!-- <a href="#missing">Comment</a> -->\n')
        self.assertEqual(self.report()["links_checked"], 0)
        self.assertEqual(self.report()["issues"], [])

    def test_escaping_symlink_is_reported_without_reading_target(self):
        outside = self.docs.parent / "outside.md"
        outside.write_bytes(b"\xff")
        (self.docs / "escape.md").symlink_to(outside)
        self.write("README.md", '# 首页\n\n[escape](escape.md#anchor)\n')
        issue = self.report()["issues"][0]
        self.assertEqual(issue["reason"], "outside_docs")
        self.assertIsNone(issue["target"])

    def test_cli_is_deterministic_read_only_and_check_is_opt_in(self):
        self.write("README.md", '# 首页\n\n[broken](#丢失)\n')
        before = {p.relative_to(self.docs): p.read_bytes() for p in self.docs.rglob("*") if p.is_file()}
        first, second, check = self.run_cli(), self.run_cli(), self.run_cli("--check")
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stderr, "")
        self.assertEqual(first.stdout, second.stdout)
        self.assertEqual(first.stdout, check.stdout)
        self.assertEqual(check.returncode, 1, check.stderr)
        self.assertEqual(json.loads(first.stdout), self.report())
        self.assertIn("丢失", first.stdout)
        self.assertNotIn(str(self.docs), first.stdout)
        self.assertEqual(before, {p.relative_to(self.docs): p.read_bytes() for p in self.docs.rglob("*") if p.is_file()})
        self.assertEqual(list(self.docs.parent.iterdir()), [self.docs])

    def test_check_succeeds_without_issues(self):
        result = self.run_cli("--check")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["issue_count"], 0)

    def test_invalid_input_fails_without_partial_json(self):
        for summary in ('- [missing](missing.md)', '- [escape](../outside.md)', '# Empty'):
            with self.subTest(summary=summary):
                self.write("SUMMARY.md", summary)
                result = self.run_cli()
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("Traceback", result.stderr)
        (self.docs / "SUMMARY.md").unlink()
        self.assertEqual(self.run_cli().returncode, 2)


if __name__ == "__main__":
    unittest.main()
