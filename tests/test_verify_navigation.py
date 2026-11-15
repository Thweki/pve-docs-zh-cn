"""Exercise SUMMARY reachability through the real verifier and its exit status."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import verify


class SummaryNavigationTests(unittest.TestCase):
    def verify_book(self, summary, pages):
        with tempfile.TemporaryDirectory(prefix="pve-navigation-test-") as temporary:
            root = Path(temporary)
            docs = root / "docs"
            for directory in (docs, root / "source/api", root / "reports", root / "work"):
                directory.mkdir(parents=True)
            (root / "source/assets-manifest.json").write_text("[]", encoding="utf-8")
            (root / "source/api/schema.json").write_text("{}", encoding="utf-8")
            (docs / "SUMMARY.md").write_text(summary, encoding="utf-8")
            for name in pages:
                path = docs / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('# Page <a id="top"></a>\n', encoding="utf-8")
            status = 0
            with patch.multiple(verify, ROOT=root, DOCS=docs, UNITS={}, TRANSLATIONS={}), \
                    patch.object(sys, "argv", ["verify.py"]), \
                    contextlib.redirect_stdout(io.StringIO()):
                try:
                    verify.main()
                except SystemExit as error:
                    status = error.code
            report = json.loads((root / "reports/verification.json").read_text())
            self.assertEqual(report["passed"], status == 0)
            return status, report["errors"]

    def test_nested_readme_does_not_cover_root_readme(self):
        status, errors = self.verify_book("- [Guide](guide/README.md)\n",
                                          ["README.md", "guide/README.md"])
        self.assertEqual(status, 1)
        self.assertEqual(errors, ["not in SUMMARY: README.md"])

    def test_mentions_without_local_links_do_not_cover_pages(self):
        for summary in (
            "The missing page is chapter.md.\n",
            "`[Chapter](chapter.md)`\n",
            "```markdown\n[Chapter](chapter.md)\n```\n",
            "<!-- [Chapter](chapter.md) -->\n",
            "- [chapter.md](README.md)\n",
            "- [External](https://example.invalid/chapter.md)\n",
            "- [External](//example.invalid/chapter.md)\n",
            "[unused]: chapter.md\n",
        ):
            with self.subTest(summary=summary):
                status, errors = self.verify_book("- [Home](README.md)\n" + summary,
                                                  ["README.md", "chapter.md"])
                self.assertEqual(status, 1)
                self.assertEqual(errors, ["not in SUMMARY: chapter.md"])

    def test_local_markdown_reference_and_html_links_cover_pages(self):
        for summary in (
            '- [Chapter](chapter.md "Chapter title")\n',
            "- [Chapter][chapter]\n\n[chapter]: chapter.md\n",
            '<a href="chapter.md">Chapter</a>\n',
        ):
            with self.subTest(summary=summary):
                self.assertEqual(self.verify_book(summary, ["chapter.md"]), (0, []))

    def test_encoded_and_normalized_paths_cover_pages(self):
        for target in ("%63hapter.md", "./chapter.md", "nested/../chapter.md"):
            with self.subTest(target=target):
                self.assertEqual(self.verify_book(f"- [Chapter]({target})\n", ["chapter.md"]),
                                 (0, []))
        self.assertEqual(self.verify_book("- [Page](%E7%AB%A0%20%E8%8A%82.md)\n", ["章 节.md"]),
                         (0, []))

    def test_query_and_fragment_do_not_change_target_page(self):
        self.assertEqual(self.verify_book("- [Chapter](chapter.md?view=book#top)\n", ["chapter.md"]),
                         (0, []))

    def test_broken_summary_links_still_fail(self):
        for target, message in (("missing.md", "broken file link"),
                                ("chapter.md#missing", "broken anchor")):
            with self.subTest(target=target):
                status, errors = self.verify_book(f"- [Chapter](chapter.md)\n- [Broken]({target})\n",
                                                  ["chapter.md"])
                self.assertEqual(status, 1)
                self.assertEqual(len(errors), 1)
                self.assertIn(message, errors[0])


if __name__ == "__main__":
    unittest.main()
