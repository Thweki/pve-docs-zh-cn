"""Dependency-free, offline regressions for source and HTML archive tooling."""
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import package_html
import package_source


class SourcePackageTests(unittest.TestCase):
    def test_safe_archive_names(self):
        for name in ("source/html/index.html", "docs/中文 文档.md", "LICENSE"):
            with self.subTest(name=name):
                self.assertEqual(package_source.safe_name(name), name)

    def test_unsafe_archive_names_fail(self):
        for name in ("", "/absolute", "../outside", "docs/../outside", "./docs",
                     "docs//page", "docs/", "C:/absolute", "docs\\page"):
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, "Unsafe archive path"):
                    package_source.safe_name(name)

    def test_checked_in_snapshot_passes_offline_audit(self):
        # Read-only verification of every archived file's size/hash, inventory,
        # path, owner metadata and type. No restoration or live upstream fetch.
        report, entries = package_source.audit_snapshot(package_source.ROOT)
        self.assertTrue(report["manifest_verified"])
        self.assertGreater(report["file_count"], 0)
        self.assertEqual(report["file_count"], len(entries))
        self.assertTrue(all(report["input_counts"].values()))
        self.assertEqual(report["unsafe_paths"], 0)
        self.assertEqual(report["symlinks"], 0)
        self.assertEqual(report["secret_pattern_findings"], [])

    def test_restore_preserves_existing_inputs_and_rejects_changes(self):
        with tempfile.TemporaryDirectory(prefix="pve-restore-test-") as temporary:
            root = Path(temporary)
            entries = [("source/html/page.html", b"original")]
            package_source.restore_snapshot(root, entries)
            package_source.restore_snapshot(root, entries)
            target = root / entries[0][0]
            self.assertEqual(target.read_bytes(), b"original")
            target.write_bytes(b"local edit")
            with self.assertRaisesRegex(ValueError, "Refusing to replace changed input"):
                package_source.restore_snapshot(root, entries)
            self.assertEqual(target.read_bytes(), b"local edit")

    def test_restore_rejects_symlink_parent(self):
        with tempfile.TemporaryDirectory(prefix="pve-restore-test-") as temporary:
            root = Path(temporary)
            outside = root / "outside"
            outside.mkdir()
            (root / "source").symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, "Restore destination contains symlink"):
                package_source.restore_snapshot(root, [("source/page.html", b"original")])
            self.assertEqual(list(outside.iterdir()), [])


class HtmlPackageTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="pve-package-test-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.source = self.base / "html"
        (self.source / "assets").mkdir(parents=True)
        (self.source / "index.html").write_text("<!doctype html><p>Offline</p>", encoding="utf-8")
        (self.source / "assets/data.bin").write_bytes(bytes(range(256)))

    def test_archive_preserves_bytes_and_is_reproducible(self):
        first, second = self.base / "first.zip", self.base / "second.zip"
        report = package_html.package_html(self.source, first, package_html.sha256(self.source / "index.html"))
        package_html.package_html(self.source, second)
        self.assertEqual(first.read_bytes(), second.read_bytes())
        self.assertEqual(report["files"], 2)
        with zipfile.ZipFile(first) as archive:
            self.assertIsNone(archive.testzip())
            for relative in ("index.html", "assets/data.bin"):
                self.assertEqual(archive.read(f"{package_html.PACKAGE}/{relative}"), (self.source / relative).read_bytes())

    def test_rejects_digest_mismatch_and_output_inside_source(self):
        with self.assertRaisesRegex(ValueError, "Unexpected index.html SHA256"):
            package_html.package_html(self.source, self.base / "bad.zip", "0" * 64)
        with self.assertRaisesRegex(ValueError, "Output ZIP must be outside"):
            package_html.package_html(self.source, self.source / "bad.zip")
        self.assertFalse(any(self.base.rglob("*.zip")))

    def test_rejects_symlink_resource(self):
        (self.source / "linked.html").symlink_to(self.source / "index.html")
        with self.assertRaisesRegex(ValueError, "Symlink is not permitted"):
            package_html.package_html(self.source, self.base / "bad.zip")
        self.assertFalse(any(self.base.rglob("*.zip")))


if __name__ == "__main__":
    unittest.main()
