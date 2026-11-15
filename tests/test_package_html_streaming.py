"""Offline regressions for bounded-memory HTML archive packaging."""
from pathlib import Path
import stat
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import package_html


CHUNK_SIZE = 1024 * 1024


class HtmlStreamingTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="pve-html-streaming-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.source = self.base / "html"
        self.source.mkdir()
        (self.source / "index.html").write_bytes(b"<p>Offline book</p>")
        (self.source / "empty.bin").touch()
        self.asset = self.source / "download.bin"
        # Multiple full chunks and a partial final chunk, including binary data.
        self.asset.write_bytes(bytes(range(256)) * (2 * CHUNK_SIZE // 256) + b"end")
        self.output = self.base / "book.zip"

    def test_source_reads_are_bounded(self):
        original_open = Path.open
        reads = []
        streams = []
        test = self

        class BoundedReader:
            def __init__(self, stream):
                self.stream = stream

            def __enter__(self):
                return self

            def __exit__(self, *args):
                self.stream.close()

            def read(self, size=-1):
                test.assertGreater(size, 0, "source read must have a bound")
                test.assertLessEqual(size, CHUNK_SIZE)
                reads.append(size)
                return self.stream.read(size)

        def guarded_open(path, mode="r", *args, **kwargs):
            stream = original_open(path, mode, *args, **kwargs)
            if mode == "rb":
                streams.append(stream)
                return BoundedReader(stream)
            return stream

        with patch.object(Path, "open", guarded_open):
            package_html.package_html(self.source, self.output)
        self.assertTrue(reads)
        self.assertTrue(all(stream.closed for stream in streams))

    def test_archive_validation_reads_are_bounded(self):
        original_read = zipfile.ZipExtFile.read
        reads = []

        def bounded_read(stream, size=-1):
            self.assertGreater(size, 0, "archive read must have a bound")
            self.assertLessEqual(size, CHUNK_SIZE)
            reads.append(size)
            return original_read(stream, size)

        with patch.object(zipfile.ZipExtFile, "read", bounded_read):
            package_html.package_html(self.source, self.output)
        self.assertTrue(reads)

    def test_archive_bytes_match_previous_format(self):
        expected = self.base / "expected.zip"
        # Reference the original whole-buffer writer to check level-9
        # compression, fixed metadata, empty files and exact archive bytes.
        with zipfile.ZipFile(expected, "w", compression=zipfile.ZIP_DEFLATED,
                             compresslevel=9) as archive:
            top = zipfile.ZipInfo(package_html.PACKAGE + "/", (2026, 1, 1, 0, 0, 0))
            top.create_system = 3
            top.external_attr = (stat.S_IFDIR | 0o755) << 16
            archive.writestr(top, b"")
            for path in sorted(self.source.iterdir()):
                info = zipfile.ZipInfo(package_html.PACKAGE + "/" + path.name,
                                       (2026, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes(), compresslevel=9)
        report = package_html.package_html(self.source, self.output)
        self.assertEqual(expected.read_bytes(), self.output.read_bytes())
        self.assertEqual(report["files"], 3)
        self.assertEqual(report["sha256"], package_html.sha256(expected))
        self.assertTrue(report["all_files_match_source_bytes"])

    def test_large_member_selects_zip64_before_writing(self):
        # Exercise the multi-gigabyte path without a multi-gigabyte fixture.
        with patch.object(zipfile, "ZIP64_LIMIT", CHUNK_SIZE):
            package_html.package_html(self.source, self.output)
        with zipfile.ZipFile(self.output) as archive:
            name = package_html.PACKAGE + "/download.bin"
            self.assertEqual(archive.read(name), self.asset.read_bytes())
            self.assertEqual(archive.getinfo(name).extract_version, 45)

    def test_read_failure_closes_member_and_preserves_previous_archive(self):
        self.output.write_bytes(b"previous release")
        before = set(self.base.iterdir())
        streams = []

        def failed_read(stream, size=-1):
            streams.append(stream)
            raise OSError("injected read failure")

        with patch.object(zipfile.ZipFile, "testzip", return_value=None), \
                patch.object(zipfile.ZipExtFile, "read", failed_read):
            with self.assertRaisesRegex(OSError, "injected read failure"):
                package_html.package_html(self.source, self.output)
        self.assertTrue(streams)
        self.assertTrue(all(stream.closed for stream in streams))
        self.assertEqual(self.output.read_bytes(), b"previous release")
        self.assertEqual(set(self.base.iterdir()), before)

    def test_streamed_checksum_still_rejects_changed_archive_bytes(self):
        original_read = zipfile.ZipExtFile.read
        self.output.write_bytes(b"previous release")

        def altered_read(stream, size=-1):
            data = original_read(stream, size)
            return b"!" + data[1:] if data else data

        with patch.object(zipfile.ZipFile, "testzip", return_value=None), \
                patch.object(zipfile.ZipExtFile, "read", altered_read):
            with self.assertRaisesRegex(ValueError, "Archived file inventory or bytes differ"):
                package_html.package_html(self.source, self.output)
        self.assertEqual(self.output.read_bytes(), b"previous release")


if __name__ == "__main__":
    unittest.main()
