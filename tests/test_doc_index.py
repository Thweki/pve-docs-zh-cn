"""Offline heading lookup without a book build or renderer dependencies."""
import hashlib
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


class DocumentationIndexTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        for name in ("bs4", "markdown_it", "yaml"):
            try:
                importlib.import_module(name)
            except ImportError as error:
                raise unittest.SkipTest(f"{name} unavailable: {error}") from error
        cls.index = importlib.import_module("report_doc_index")

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.docs = Path(temporary.name) / "docs"
        self.docs.mkdir()
        (self.docs / "SUMMARY.md").write_text(
            '- [导航首页](README.md)\n'
            '  - [API 导航](<中文 API.md>)\n'
            '- [重复引用](README.md#top)\n'
            '- [外部页面](https://example.org/)\n', encoding="utf-8")
        (self.docs / "README.md").write_text(
            '---\ntitle: 隐藏元数据\n---\n'
            '# 首页\n\n## **备份** `VM` <a id="backup"></a>\n\n'
            '## 重复\n\n## 重复\n\n'
            '```md\n# 假标题\n```\n', encoding="utf-8")
        (self.docs / "中文 API.md").write_text(
            '## GET /nodes <a id="api/nodes?x#y"></a>\n\n'
            '## POST /nodes {#create}\n', encoding="utf-8")
        (self.docs / "orphan.md").write_text('# 未收录\n', encoding="utf-8")

    def test_order_titles_depth_and_counts(self):
        report = self.index.build_index(self.docs)
        self.assertEqual(report["schema_version"], 1)
        self.assertEqual(report["page_count"], 2)
        self.assertEqual(report["heading_count"], 7)
        pages = report["pages"]
        self.assertEqual([p["path"] for p in pages], ["README.md", "中文 API.md"])
        self.assertEqual([p["title"] for p in pages], ["导航首页", "API 导航"])
        self.assertEqual([p["depth"] for p in pages], [0, 1])
        self.assertEqual([h["title"] for h in pages[0]["headings"]],
                         ["首页", "备份 VM", "重复", "重复"])
        self.assertEqual([h["level"] for h in pages[1]["headings"]], [1, 2, 2])
        self.assertEqual(pages[1]["headings"][0]["title"], "API 导航")

    def test_links_use_export_ids_and_encode_fragments(self):
        pages = self.index.build_index(self.docs)["pages"]
        key = "page-readme-" + hashlib.sha256(b"README.md").hexdigest()[:8]
        self.assertEqual(pages[0]["href"], "index.html#" + key)
        self.assertEqual(pages[0]["headings"][1]["href"], "index.html#" + key + "--backup")
        self.assertTrue(pages[1]["headings"][1]["href"].endswith("--api%2Fnodes%3Fx%23y"))
        self.assertTrue(pages[1]["headings"][2]["href"].endswith("--create"))

        # Compare every reported target with the actual chapter HTML, including
        # repeated headings and the synthetic H1 for a page starting at H2.
        import export_web_epub as exporter
        for indexed, page in zip(pages, exporter.summary_pages(self.docs)):
            exporter.namespace(page)
            chapter = exporter.BeautifulSoup(exporter.chapter_html(page), "html.parser")
            targets = [unquote(h["href"].split("#", 1)[1]) for h in indexed["headings"]]
            self.assertEqual(len(targets), len(set(targets)))
            for target in targets:
                self.assertEqual(len(chapter.find_all(id=target)), 1)

    def test_query_is_case_insensitive_and_counts_only_matching_headings(self):
        report = self.index.build_index(self.docs, query="get /NODES")
        self.assertEqual((report["page_count"], report["heading_count"]), (1, 1))
        self.assertEqual(report["pages"][0]["path"], "中文 API.md")
        self.assertEqual(report["pages"][0]["headings"][0]["title"], "GET /nodes")
        self.assertEqual(self.index.build_index(self.docs, query="备份")["heading_count"], 1)
        self.assertEqual(self.index.build_index(self.docs, query="not present")["pages"], [])

    def test_filter_preserves_duplicate_heading_targets(self):
        full = self.index.build_index(self.docs)["pages"][0]["headings"][2:]
        filtered = self.index.build_index(self.docs, query="重复")["pages"][0]["headings"]
        self.assertEqual(filtered, full)
        self.assertTrue(unquote(filtered[1]["href"]).endswith("--重复-2"))

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts/report_doc_index.py"),
             "--docs", "docs", *args], cwd=self.docs.parent,
            capture_output=True, text=True, encoding="utf-8", timeout=30)

    def test_cli_is_deterministic_and_does_not_change_inputs(self):
        before = {p.relative_to(self.docs): p.read_bytes() for p in self.docs.rglob("*") if p.is_file()}
        first, second = self.run_cli(), self.run_cli()
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stderr, "")
        self.assertEqual(first.stdout, second.stdout)
        self.assertIn("备份", first.stdout)
        self.assertNotIn(str(self.docs), first.stdout)
        self.assertEqual(json.loads(first.stdout), self.index.build_index(self.docs))
        self.assertEqual(before, {p.relative_to(self.docs): p.read_bytes() for p in self.docs.rglob("*") if p.is_file()})
        self.assertEqual(list(self.docs.parent.iterdir()), [self.docs])

    def test_cli_no_matches_is_success(self):
        result = self.run_cli("--query", "no match")
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual((report["page_count"], report["heading_count"]), (0, 0))

    def test_invalid_summary_fails_without_partial_json(self):
        for summary in ('- [missing](missing.md)', '- [escape](../outside.md)', '# Empty'):
            with self.subTest(summary=summary):
                (self.docs / "SUMMARY.md").write_text(summary, encoding="utf-8")
                result = self.run_cli()
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("error:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_missing_summary_fails_cleanly(self):
        (self.docs / "SUMMARY.md").unlink()
        result = self.run_cli()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("SUMMARY.md", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
