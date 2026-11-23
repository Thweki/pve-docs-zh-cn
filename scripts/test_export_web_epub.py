"""HTML export regressions: python3 -m unittest discover -s scripts -p 'test_*.py'."""
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import export_web_epub as exporter
from package_html import PACKAGE, package_html


def inventory(directory: Path) -> dict[str, bytes]:
    return {path.relative_to(directory).as_posix(): path.read_bytes()
            for path in directory.rglob("*") if path.is_file()}


class HtmlExportTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.docs = self.root / "docs"
        self.docs.mkdir()
        (self.docs / "SUMMARY.md").write_text('- [Chapter](README.md)\n')
        self.page = self.docs / "README.md"
        self.page.write_text('# Chapter\n\n![Current](assets/current.svg)\n'
                             '![Removed](assets/removed.svg)\n[Download](removed.txt)\n')
        (self.docs / "assets").mkdir()
        for name in ("current.svg", "removed.svg"):
            (self.docs / "assets" / name).write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
        (self.docs / "removed.txt").write_text('download')
        assets = self.root / "export-assets"
        assets.mkdir()
        (assets / "screen.css").write_text('body { color: black; }')
        (assets / "offline.js").write_text('/* offline */')
        self.fonts = assets / "fonts"
        self.fonts.mkdir()
        for name in ("current.ttf", "removed.otf", "OFL.txt", "OFL-removed.txt"):
            (self.fonts / name).write_text(name)
        (self.root / "LICENSE").write_text('license')
        (self.root / "LICENSES").mkdir()
        (self.root / "LICENSES/removed.txt").write_text('old license')
        self.output = self.root / "reused"
        root_patch = patch.object(exporter, "ROOT", self.root)
        root_patch.start()
        self.addCleanup(root_patch.stop)

    def build(self, output=None, require_fonts=True):
        return exporter.build(self.docs, output or self.output,
                              with_epub=False, require_fonts=require_fonts)

    def assert_matches_clean_zip(self, removed, require_fonts=True):
        self.build(require_fonts=require_fonts)
        clean = self.root / "clean"
        self.build(clean, require_fonts=require_fonts)
        self.assertEqual(inventory(clean), inventory(self.output))
        archives = []
        for output in (clean, self.output):
            archive_path = self.root / (output.name + '.zip')
            package_html(output / "html", archive_path)
            with zipfile.ZipFile(archive_path) as archive:
                members = {name.removeprefix(PACKAGE + '/'): archive.read(name)
                           for name in archive.namelist() if not name.endswith('/')}
            self.assertEqual(members, inventory(clean / "html"))
            self.assertTrue(removed.isdisjoint(members))
            archives.append(archive_path.read_bytes())
        self.assertEqual(*archives)

    def test_reused_output_drops_removed_resources(self):
        self.build()
        (self.output / "html/stale.txt").write_text('unmanaged old resource')
        (self.output / "html/epub.css").write_text('obsolete stylesheet')
        (self.docs / "assets/removed.svg").unlink()
        (self.docs / "assets/current.svg").write_text('<svg><!-- updated --></svg>')
        (self.docs / "removed.txt").unlink()
        (self.fonts / "removed.otf").unlink()
        (self.fonts / "OFL-removed.txt").unlink()
        (self.root / "LICENSES/removed.txt").unlink()
        self.page.write_text('# Chapter\n\n![Current](assets/current.svg)\n')
        self.assert_matches_clean_zip({"assets/removed.svg", "removed.txt", "fonts/removed.otf",
                                       "fonts/OFL-removed.txt", "LICENSES/removed.txt",
                                       "stale.txt", "epub.css"})

    def test_reused_output_drops_absent_asset_and_font_directories(self):
        self.build()
        shutil.rmtree(self.docs / "assets")
        shutil.rmtree(self.fonts)
        shutil.rmtree(self.root / "LICENSES")
        (self.docs / "removed.txt").unlink()
        self.page.write_text('# Chapter\n')
        self.assert_matches_clean_zip({"assets/current.svg", "assets/removed.svg",
                                       "fonts/current.ttf", "fonts/removed.otf"}, require_fonts=False)
        for name in ("assets", "fonts", "LICENSES"):
            self.assertFalse((self.output / "html" / name).exists())

    def test_failed_validation_preserves_previous_export(self):
        self.build()
        (self.output / "unrelated.txt").write_text('keep')
        before = inventory(self.output)
        self.page.write_text('# Changed chapter\n')
        audit = exporter.audit_html

        def fail_export_audit(text, base):
            self.assertTrue(base.is_relative_to(self.output))
            self.assertNotEqual(base, self.output)
            if base.name == "export":
                raise ValueError('injected export validation failure')
            return audit(text, base)

        with patch.object(exporter, "audit_html", side_effect=fail_export_audit):
            with self.assertRaisesRegex(ValueError, 'injected export validation failure'):
                self.build()
        self.assertEqual(before, inventory(self.output))
        self.assertFalse(list(self.output.glob('.web-epub-*')))

    def test_failed_html_replacement_restores_previous_export(self):
        self.build()
        before = inventory(self.output)
        self.page.write_text('# Changed chapter\n')
        replace = Path.replace

        def fail_staged_html(path, target):
            if path.name == "html" and path.parent != self.output:
                raise OSError('injected replacement failure')
            return replace(path, target)

        with patch.object(Path, "replace", fail_staged_html):
            with self.assertRaisesRegex(OSError, 'injected replacement failure'):
                self.build()
        self.assertEqual(before, inventory(self.output))
        self.assertFalse(list(self.output.glob('.web-epub-*')))


if __name__ == '__main__':
    unittest.main()
