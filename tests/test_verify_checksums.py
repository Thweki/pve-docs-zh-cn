"""Verify downloaded release files using temporary, entirely offline fixtures."""

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts import verify_checksums as verifier


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/verify_checksums.py"


class ChecksumTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.sums = self.root / "SHA256SUMS"

    def entry(self, name, data=b"release content", marker=" "):
        (self.root / name).write_bytes(data)
        return f"{hashlib.sha256(data).hexdigest()} {marker}{name}\n"

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(self.sums), *args],
            cwd=self.root.parent, capture_output=True, text=True)

    def test_cli_checks_text_and_binary_entries_relative_to_manifest(self):
        self.sums.write_text(
            self.entry("中文 manual.pdf") + self.entry("source.zip", b"\x00\xff", "*"),
            encoding="utf-8")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "中文 manual.pdf: OK\nsource.zip: OK\n")
        self.assertEqual(result.stderr, "")

    def test_explicit_directory_and_large_binary_file(self):
        self.sums.write_text(self.entry("source.zip", bytes(range(256)) * 10000),
                             encoding="utf-8")
        downloads = self.root / "downloads"
        downloads.mkdir()
        (self.root / "source.zip").rename(downloads / "source.zip")
        result = self.run_cli("--directory", str(downloads))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "source.zip: OK\n")

    def test_corrupt_missing_and_good_files_are_all_reported(self):
        self.sums.write_text(self.entry("bad.pdf") + self.entry("missing.epub") +
                             self.entry("good.zip"), encoding="utf-8")
        (self.root / "bad.pdf").write_bytes(b"Release content")  # Same size, wrong hash.
        (self.root / "missing.epub").unlink()
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("bad.pdf: FAILED", result.stdout)
        self.assertIn("expected " + hashlib.sha256(b"release content").hexdigest(), result.stdout)
        self.assertIn("got " + hashlib.sha256(b"Release content").hexdigest(), result.stdout)
        self.assertIn("missing.epub: MISSING", result.stdout)
        self.assertIn("good.zip: OK", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_uppercase_hash_crlf_blank_lines_and_empty_file(self):
        line = self.entry("empty.pdf", b"")
        digest, name = line.split("  ")
        self.sums.write_bytes(("\r\n" + digest.upper() + "  " + name.rstrip("\n") +
                              "\r\n\r\n").encode())
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_manifest_is_rejected_before_checking_any_files(self):
        valid = self.entry("manual.pdf")
        invalid = ["", "\n", "abc  manual.pdf\n", "g" * 64 + "  manual.pdf\n",
                   "a" * 64 + " manual.pdf\n", "a" * 64 + "  \n",
                   valid + valid, valid + "malformed\n"]
        for content in invalid:
            with self.subTest(content=content):
                self.sums.write_text(content, encoding="utf-8")
                result = self.run_cli()
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertIn("Checksum verification failed", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_paths_and_control_characters_are_rejected(self):
        for name in ("../outside", "/tmp/outside", "dir/file", "dir\\file", "C:outside",
                     ".", "..", "bad\x00name", "bad\tname", "bad\x1bname", "bad\x7fname"):
            with self.subTest(name=name):
                with self.assertRaisesRegex(ValueError, "filename"):
                    verifier.parse_checksums("a" * 64 + "  " + name + "\n")

    def test_symlink_and_directory_are_not_hashed(self):
        self.sums.write_text(self.entry("linked.pdf") + self.entry("directory.zip"),
                             encoding="utf-8")
        (self.root / "linked.pdf").unlink()
        (self.root / "linked.pdf").symlink_to(self.sums)
        (self.root / "directory.zip").unlink()
        (self.root / "directory.zip").mkdir()
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("linked.pdf: ERROR", result.stdout)
        self.assertIn("directory.zip: ERROR", result.stdout)

    def test_read_error_is_reported(self):
        line = self.entry("manual.pdf")
        entries = verifier.parse_checksums(line)
        with patch.object(Path, "open", side_effect=PermissionError("denied")):
            reports = list(verifier.verify_checksums(entries, self.root))
        self.assertEqual(len(reports), 1)
        self.assertFalse(reports[0][0])
        self.assertIn("manual.pdf: ERROR", reports[0][1])

    def test_missing_or_non_utf8_manifest_fails_cleanly(self):
        for data in (None, b"\xff"):
            with self.subTest(data=data):
                if data is not None:
                    self.sums.write_bytes(data)
                result = self.run_cli()
                self.assertEqual(result.returncode, 1)
                self.assertIn("Checksum verification failed", result.stderr)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
