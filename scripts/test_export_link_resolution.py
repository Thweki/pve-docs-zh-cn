"""Run with: python3 -m unittest discover -s scripts -p 'test_*.py' -v."""
from collections import Counter
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from bs4 import BeautifulSoup

import export_web_epub as export


class LinkResolutionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.docs = Path(self.temporary.name) / "docs"
        self.docs.mkdir()

    def page(self, name, markup, key="page"):
        path = self.docs / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("", encoding="utf-8")
        return export.Page(path, name, 0, key,
                           BeautifulSoup(markup, "html.parser"),
                           aliases={"": key, "one": key + "--one", "two": key + "--two"})

    def test_repeated_targets_resolve_once_despite_different_fragments_and_encoding(self):
        markup = ('<a href="target%20page.md#one">One</a>'
                  '<a href="target page.md#two">Two</a>'
                  '<a href="#one">Here</a>'
                  '<img src="image.svg"><video poster="image.svg"></video>') * 100
        source = self.page("source.md", markup, "source")
        target = self.page("target page.md", "", "target")
        asset = self.docs / "image.svg"
        asset.write_text("<svg/>", encoding="utf-8")
        counts = Counter()
        resolve = Path.resolve

        def counted(path, *args, **kwargs):
            counts[path] += 1
            return resolve(path, *args, **kwargs)

        with patch.object(Path, "resolve", counted):
            self.assertEqual(export.rewrite_links([source, target], self.docs), [])

        # One inventory resolution plus one link-target resolution per page.
        self.assertEqual(counts[target.path], 2)
        self.assertEqual(counts[source.path], 2)
        self.assertEqual(counts[asset], 1)
        self.assertEqual(counts[self.docs], 1)
        self.assertEqual([a["href"] for a in source.soup.select("a")],
                         ["#target--one", "#target--two", "#source--one"] * 100)
        self.assertTrue(all(img["loading"] == "lazy" and img["decoding"] == "async"
                            for img in source.soup.select("img")))

    def test_relative_targets_are_scoped_to_each_source_directory(self):
        left = self.page("left/index.md", '<a href="target.md#one">Left</a>')
        right = self.page("right/index.md", '<a href="target.md#one">Right</a>')
        left_target = self.page("left/target.md", "", "left")
        right_target = self.page("right/target.md", "", "right")
        self.assertEqual(export.rewrite_links([left, right, left_target, right_target], self.docs), [])
        self.assertEqual(left.soup.a["href"], "#left--one")
        self.assertEqual(right.soup.a["href"], "#right--one")

    def test_symlink_target_is_resolved_again_on_the_next_call(self):
        markup = '<a href="alias.md#one">Target</a>'
        source = self.page("index.md", markup)
        first = self.page("first.md", "", "first")
        second = self.page("second.md", "", "second")
        alias = self.docs / "alias.md"
        alias.symlink_to(first.path.name)
        self.assertEqual(export.rewrite_links([source, first, second], self.docs), [])
        self.assertEqual(source.soup.a["href"], "#first--one")
        alias.unlink()
        alias.symlink_to(second.path.name)
        source.soup = BeautifulSoup(markup, "html.parser")
        self.assertEqual(export.rewrite_links([source, first, second], self.docs), [])
        self.assertEqual(source.soup.a["href"], "#second--one")

    def test_missing_anchors_pages_and_escaping_assets_still_fail(self):
        outside = self.docs.parent / "outside.svg"
        outside.write_text("<svg/>", encoding="utf-8")
        (self.docs / "escape.svg").symlink_to(outside)
        source = self.page("index.md", '<a href="#missing">Missing anchor</a>'
                           '<a href="absent.md">Missing page</a>'
                           '<img src="absent.svg"><img src="escape.svg">')
        self.assertEqual(export.rewrite_links([source], self.docs), [
            "Unknown anchor: #missing in index.md",
            "Page missing from SUMMARY: absent.md in index.md",
            "Missing local asset: absent.svg in index.md",
            "Missing local asset: escape.svg in index.md",
        ])

    def test_external_links_and_embedded_data_keep_existing_behavior(self):
        source = self.page("index.md", '<a href="https://example.invalid/a.md#one">External</a>'
                           '<img src="data:image/svg+xml,%3Csvg/%3E">'
                           '<img src="https://example.invalid/image.svg">'
                           '<pre>code</pre>')
        self.assertEqual(export.rewrite_links([source], self.docs), [
            "Remote embedded asset in index.md: https://example.invalid/image.svg",
        ])
        self.assertEqual(source.soup.a["href"], "https://example.invalid/a.md#one")
        self.assertEqual(source.soup.img["src"], "data:image/svg+xml,%3Csvg/%3E")
        self.assertEqual(source.soup.pre["tabindex"], "0")


if __name__ == "__main__":
    unittest.main()
