"""Exercise the read-only release tree with entirely local fixtures."""

import hashlib
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts import release_tree


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/release_tree.py"


class ReleaseTreeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "release"
        self.root.mkdir()

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(SCRIPT), str(self.root), *args],
            cwd=self.root.parent, capture_output=True, text=True, timeout=10)

    def test_sorted_nested_tree_sizes_and_totals(self):
        (self.root / "中文 manual.pdf").write_bytes(b"pdf")
        (self.root / "html").mkdir()
        (self.root / "html/index.html").write_bytes(b"hello")
        (self.root / "html/empty").mkdir()
        (self.root / ".hidden").write_bytes(b"")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, (
            f"{str(self.root)!r}/\n"
            "|-- '.hidden' [0 bytes]\n"
            "|-- 'html'/\n"
            "|   |-- 'empty'/\n"
            "|   `-- 'index.html' [5 bytes]\n"
            "`-- '中文 manual.pdf' [3 bytes]\n"
            "\n3 files, 2 directories, 0 symlinks, 0 special entries; 8 bytes\n"))

    def test_empty_directory(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("0 files, 0 directories", result.stdout)
        self.assertTrue(result.stdout.endswith("; 0 bytes\n"))

    def test_optional_hashes_and_read_only_behavior(self):
        contents = {"source.zip": bytes(range(256)) * 10000, "empty.pdf": b""}
        for name, data in contents.items():
            (self.root / name).write_bytes(data)
        before = {p.name: (p.read_bytes(), p.stat().st_mtime_ns)
                  for p in self.root.iterdir()}
        result = self.run_cli("--sha256")
        self.assertEqual(result.returncode, 0, result.stderr)
        for data in contents.values():
            self.assertIn("sha256=" + hashlib.sha256(data).hexdigest(), result.stdout)
        after = {p.name: (p.read_bytes(), p.stat().st_mtime_ns)
                 for p in self.root.iterdir()}
        self.assertEqual(before, after)

    def test_default_mode_does_not_open_file_contents(self):
        (self.root / "manual.pdf").write_bytes(b"pdf")
        output = io.StringIO()
        with patch.object(Path, "open", side_effect=AssertionError("file opened")):
            self.assertTrue(release_tree.print_tree(self.root, stream=output))
        self.assertNotIn("sha256=", output.getvalue())

    def test_symlinks_are_listed_without_following_them(self):
        (self.root.parent / "outside").write_bytes(b"private outside data")
        for name, target in (("file", self.root.parent / "outside"),
                             ("loop", self.root), ("broken", self.root / "missing")):
            (self.root / name).symlink_to(target)
        result = self.run_cli("--sha256")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("[symlink, not followed]"), 3)
        self.assertIn("0 files, 0 directories, 3 symlinks", result.stdout)
        self.assertNotIn("sha256=", result.stdout)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX named pipes")
    def test_special_files_are_not_opened(self):
        os.mkfifo(self.root / "pipe")
        result = self.run_cli("--sha256")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("'pipe' [special, not read]", result.stdout)
        self.assertIn("1 special entries; 0 bytes", result.stdout)

    def test_names_cannot_inject_terminal_lines_or_controls(self):
        (self.root / "bad\n\t\x1b[31m\u202ename").write_bytes(b"x")
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(r"bad\n\t\x1b[31m\u202ename", result.stdout)
        self.assertEqual(len(result.stdout.splitlines()), 4)

    def test_invalid_roots_fail_cleanly(self):
        file = self.root / "file"
        file.write_bytes(b"x")
        link = self.root / "link"
        link.symlink_to(self.root)
        for root in (self.root / "missing", file, link):
            with self.subTest(root=root):
                result = subprocess.run([sys.executable, "-B", str(SCRIPT), str(root)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertIn("Tree inspection failed:", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_hash_read_error_reports_partial_tree_and_continues(self):
        (self.root / "a.pdf").write_bytes(b"a")
        (self.root / "z").mkdir()
        output = io.StringIO()
        with patch.object(Path, "open", side_effect=PermissionError("denied")):
            self.assertFalse(release_tree.print_tree(self.root, hashes=True, stream=output))
        self.assertIn("'a.pdf' [1 bytes] [ERROR:", output.getvalue())
        self.assertIn("`-- 'z'/", output.getvalue())
        self.assertIn("incomplete: 1 errors", output.getvalue())

    def test_unreadable_directory_reports_partial_tree(self):
        output = io.StringIO()
        with patch.object(Path, "iterdir", side_effect=PermissionError("denied")):
            self.assertFalse(release_tree.print_tree(self.root, stream=output))
        self.assertIn("[ERROR:", output.getvalue())
        self.assertIn("incomplete: 1 errors", output.getvalue())

    def test_disappearing_entry_does_not_hide_other_entries(self):
        (self.root / "a").write_bytes(b"a")
        (self.root / "z").write_bytes(b"z")
        original = Path.lstat

        def lstat(path):
            if path.name == "a":
                raise FileNotFoundError("disappeared")
            return original(path)

        output = io.StringIO()
        with patch.object(Path, "lstat", lstat):
            self.assertFalse(release_tree.print_tree(self.root, stream=output))
        self.assertIn("'a' [ERROR:", output.getvalue())
        self.assertIn("'z' [1 bytes]", output.getvalue())
        self.assertIn("incomplete: 1 errors", output.getvalue())

    def test_unknown_option_is_usage_error(self):
        result = self.run_cli("--unknown")
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
