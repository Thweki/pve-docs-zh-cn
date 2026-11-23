"""Offline regressions for safe HTML ZIP staging and publication."""
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import package_html
import package_source


class HtmlStagingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="pve-html-staging-test-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.source = self.base / "html"
        self.source.mkdir()
        (self.source / "index.html").write_bytes(b"<p>Offline book</p>")
        self.output = self.base / "book.zip"
        self.sibling = self.base / "book.tmp.zip"

    def test_existing_temporary_name_is_preserved(self):
        self.sibling.write_bytes(b"unrelated archive")

        package_html.package_html(self.source, self.output)

        self.assertTrue(self.sibling.is_file())
        self.assertEqual(self.sibling.read_bytes(), b"unrelated archive")
        self.assertTrue(zipfile.is_zipfile(self.output))

    def test_temporary_name_symlink_is_not_followed_or_removed(self):
        victim = self.base / "unrelated.txt"
        victim.write_bytes(b"keep these bytes")
        self.sibling.symlink_to(victim)

        package_html.package_html(self.source, self.output)

        self.assertEqual(victim.read_bytes(), b"keep these bytes")
        self.assertTrue(self.sibling.is_symlink())
        self.assertEqual(self.sibling.readlink(), victim)
        self.assertFalse(self.output.is_symlink())
        self.assertTrue(zipfile.is_zipfile(self.output))

    def test_crc_failure_preserves_previous_archive_and_sibling(self):
        self.output.write_bytes(b"previous release")
        self.sibling.write_bytes(b"unrelated archive")
        before = set(self.base.iterdir())

        with patch.object(zipfile.ZipFile, "testzip", return_value="corrupt-member"):
            with self.assertRaisesRegex(ValueError, "ZIP CRC validation failed"):
                package_html.package_html(self.source, self.output)

        self.assertEqual(self.output.read_bytes(), b"previous release")
        self.assertTrue(self.sibling.is_file())
        self.assertEqual(self.sibling.read_bytes(), b"unrelated archive")
        self.assertEqual(set(self.base.iterdir()), before)

    def test_write_failure_cleans_staging_and_preserves_previous_archive(self):
        self.output.write_bytes(b"previous release")
        before = set(self.base.iterdir())

        with patch.object(zipfile.ZipFile, "writestr", side_effect=OSError("disk full")):
            with self.assertRaisesRegex(OSError, "disk full"):
                package_html.package_html(self.source, self.output)

        self.assertEqual(self.output.read_bytes(), b"previous release")
        self.assertEqual(set(self.base.iterdir()), before)

    def test_replace_failure_cleans_staging_and_preserves_previous_archive(self):
        self.output.write_bytes(b"previous release")
        before = set(self.base.iterdir())

        with patch.object(Path, "replace", side_effect=OSError("cannot replace")):
            with self.assertRaisesRegex(OSError, "cannot replace"):
                package_html.package_html(self.source, self.output)

        self.assertEqual(self.output.read_bytes(), b"previous release")
        self.assertEqual(set(self.base.iterdir()), before)

    def test_success_is_reproducible_and_leaves_no_staging_files(self):
        (self.source / "asset.bin").write_bytes(bytes(range(256)))
        self.output.write_bytes(b"previous release")
        report = package_html.package_html(self.source, self.output)
        first = self.output.read_bytes()
        package_html.package_html(self.source, self.output)

        self.assertEqual(first, self.output.read_bytes())
        self.assertEqual(report["sha256"], package_html.sha256(self.output))
        with zipfile.ZipFile(self.output) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), {
                package_html.PACKAGE + "/",
                package_html.PACKAGE + "/index.html",
                package_html.PACKAGE + "/asset.bin",
            })
            for source in self.source.iterdir():
                self.assertEqual(archive.read(package_html.PACKAGE + "/" + source.name),
                                 source.read_bytes())
        self.assertEqual(set(self.base.iterdir()), {
            self.source, self.output, self.output.with_suffix(".report.json"),
        })

    def test_source_package_retains_regression_tests(self):
        selected = package_source.select_sources(package_source.ROOT)
        self.assertTrue(Path(__file__).resolve() in selected,
                        "Source packages must include the HTML packaging regressions")


if __name__ == "__main__":
    unittest.main()
