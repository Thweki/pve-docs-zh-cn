import copy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

from scripts import release_manifest as manifest


ROOT = Path(__file__).resolve().parents[1]
TAG = "v9.2.13-zh.2"


class ReleaseManifestTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.release = self.root / "release"
        self.release.mkdir()
        self.data = {
            "Proxmox-VE-9.2.13-zh-CN.pdf": b"pdf fixture",
            "SHA256SUMS": b"published checksum fixture\n",
            ".archive-note": b"",
            "extras/中文 说明.txt": "归档说明\n".encode(),
            # Only the root manifest is excluded, not files with the same basename.
            "extras/RELEASE-MANIFEST.json": b"{}",
        }
        for name, content in self.data.items():
            path = self.release / name
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(content)
        self.path = self.release / manifest.MANIFEST

    def create(self):
        manifest.create_manifest(self.release, TAG)
        return json.loads(self.path.read_text(encoding="utf-8"))

    def write(self, document):
        self.path.write_text(json.dumps(document), encoding="utf-8")

    def cli(self, *args):
        return subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts/release_manifest.py"), *args],
            cwd=self.root, capture_output=True, text=True,
        )

    def test_complete_inventory_and_round_trip(self):
        document = self.create()
        self.assertEqual(document, {
            "schema_version": 1, "release_tag": TAG,
            "files": [{"path": name, "bytes": len(self.data[name]),
                       "sha256": hashlib.sha256(self.data[name]).hexdigest()}
                      for name in sorted(self.data)],
        })
        self.assertEqual(manifest.verify_manifest(self.release, TAG), len(self.data))

    def test_reproducible_and_relocatable(self):
        self.create()
        original = self.path.read_bytes()
        relocated = self.root / "relocated"
        shutil.copytree(self.release, relocated)
        self.assertEqual(manifest.verify_manifest(relocated, TAG), len(self.data))
        (relocated / manifest.MANIFEST).unlink()
        for path in relocated.rglob("*"):
            os.utime(path, (123456789, 123456789))
        manifest.create_manifest(relocated, TAG)
        self.assertEqual((relocated / manifest.MANIFEST).read_bytes(), original)

    def test_missing_extra_and_changed_files_reported_together(self):
        self.create()
        (self.release / "SHA256SUMS").unlink()
        (self.release / "extra.asc").write_bytes(b"signature")
        (self.release / ".archive-note").write_bytes(b"longer")
        with self.assertRaises(ValueError) as error:
            manifest.verify_manifest(self.release, TAG)
        for message in ("missing file: 'SHA256SUMS'", "unexpected file: 'extra.asc'",
                        "byte count mismatch: '.archive-note'", "SHA256 mismatch: '.archive-note'"):
            self.assertIn(message, str(error.exception))

    def test_same_size_corruption_and_renames_detected(self):
        self.create()
        (self.release / "Proxmox-VE-9.2.13-zh-CN.pdf").write_bytes(b"PDF fixture")
        (self.release / "SHA256SUMS").rename(self.release / "renamed")
        with self.assertRaises(ValueError) as error:
            manifest.verify_manifest(self.release, TAG)
        self.assertIn("SHA256 mismatch", str(error.exception))
        self.assertNotIn("byte count mismatch", str(error.exception))
        self.assertIn("missing file", str(error.exception))
        self.assertIn("unexpected file", str(error.exception))

    def test_hashes_files_in_bounded_chunks(self):
        content = b"0123456789" * 101
        (self.release / "large.zip").write_bytes(content)
        original_open = Path.open
        reads = []

        def tracked_open(path, *args, **kwargs):
            source = original_open(path, *args, **kwargs)
            if args == ("rb",):
                original_read = source.read

                def read(size=-1):
                    self.assertEqual(size, 32)
                    reads.append(size)
                    return original_read(size)

                source.read = read
            return source

        with mock.patch.object(manifest, "CHUNK_SIZE", 32), mock.patch.object(Path, "open", tracked_open):
            document = self.create()
        entry = next(entry for entry in document["files"] if entry["path"] == "large.zip")
        self.assertEqual(entry["sha256"], hashlib.sha256(content).hexdigest())
        self.assertEqual(entry["bytes"], len(content))
        self.assertGreater(len(reads), len(content) // 32)

    def test_refuses_overwrite_even_if_old_manifest_is_invalid(self):
        for content in (b"old archive baseline", b""):
            with self.subTest(content=content):
                self.path.write_bytes(content)
                with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
                    manifest.create_manifest(self.release, TAG)
                self.assertEqual(self.path.read_bytes(), content)

    def test_empty_directory_and_invalid_tag_leave_no_manifest(self):
        empty = self.root / "empty"
        empty.mkdir()
        with self.assertRaisesRegex(ValueError, "no files"):
            manifest.create_manifest(empty, TAG)
        self.assertFalse((empty / manifest.MANIFEST).exists())
        for tag in ("latest", "v9.2.13-zh.2\n", None):
            with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, "release_tag"):
                manifest.create_manifest(self.release, tag)
        self.assertFalse(self.path.exists())

    def test_translation_revision_must_match(self):
        self.create()
        with self.assertRaisesRegex(ValueError, "release_tag must equal"):
            manifest.verify_manifest(self.release, "v9.2.13-zh.3")

    def test_manifest_schema_validation(self):
        original = self.create()
        cases = [([], "expected object"), ({}, "expected object")]
        for field, value, message in (
            ("schema_version", 2, "schema_version"),
            ("schema_version", True, "schema_version"),
            ("release_tag", 123, "release_tag"),
            ("files", [], "nonempty list"),
            ("files", {}, "nonempty list"),
            ("extra", 1, "expected object"),
        ):
            document = copy.deepcopy(original)
            document[field] = value
            cases.append((document, message))
        for field, value, message in (
            ("bytes", True, "nonnegative integer"),
            ("bytes", -1, "nonnegative integer"),
            ("bytes", 1.5, "nonnegative integer"),
            ("bytes", "0", "nonnegative integer"),
            ("sha256", "a" * 63, "lowercase hex"),
            ("sha256", "G" * 64, "lowercase hex"),
            ("sha256", None, "lowercase hex"),
            ("extra", 1, "expected object"),
        ):
            document = copy.deepcopy(original)
            document["files"][0][field] = value
            cases.append((document, message))
        document = copy.deepcopy(original)
        document["files"].append(document["files"][0])
        cases.append((document, "duplicate file path"))
        document = copy.deepcopy(original)
        document["files"][0] = None
        cases.append((document, "expected object"))
        for document, message in cases:
            with self.subTest(document=document):
                self.write(document)
                with self.assertRaisesRegex(ValueError, message):
                    manifest.verify_manifest(self.release, TAG)

    def test_unsafe_paths_rejected_before_scanning_files(self):
        document = self.create()
        for name in ("../outside", "/absolute", "./file", "x/../y", "x//y", "x/",
                     "C:/file", "x\\file", "line\nbreak", "", None, manifest.MANIFEST):
            with self.subTest(name=name):
                document["files"][0]["path"] = name
                self.write(document)
                with mock.patch.object(manifest, "inventory") as scan:
                    with self.assertRaisesRegex(ValueError, "relative file path"):
                        manifest.verify_manifest(self.release, TAG)
                    scan.assert_not_called()

    def test_symlinks_rejected_for_files_directories_and_manifest(self):
        self.create()
        link = self.release / "link"
        for target in (self.release / "SHA256SUMS", self.release / "extras", self.root / "missing"):
            with self.subTest(target=target):
                link.symlink_to(target)
                with self.assertRaisesRegex(ValueError, "links unsupported"):
                    manifest.verify_manifest(self.release, TAG)
                link.unlink()
        self.path.unlink()
        self.path.symlink_to(self.root / "missing")
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            manifest.create_manifest(self.release, TAG)
        with self.assertRaisesRegex(ValueError, "manifest must be a regular file"):
            manifest.verify_manifest(self.release, TAG)

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX FIFO support")
    def test_special_files_rejected_without_opening(self):
        os.mkfifo(self.release / "pipe")
        with self.assertRaisesRegex(ValueError, "not a regular file"):
            manifest.create_manifest(self.release, TAG)
        self.assertFalse(self.path.exists())

    def test_scan_errors_are_not_silently_ignored(self):
        with mock.patch.object(Path, "iterdir", side_effect=PermissionError("unreadable directory")):
            with self.assertRaisesRegex(PermissionError, "unreadable directory"):
                manifest.create_manifest(self.release, TAG)
        self.assertFalse(self.path.exists())

    def test_cli_round_trip_and_failures_from_another_directory(self):
        for command in ("create", "verify"):
            result = self.cli(command, "release", "--tag", TAG)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("5 files", result.stdout)
        (self.release / "SHA256SUMS").unlink()
        result = self.cli("verify", "release", "--tag", TAG)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing file", result.stderr)
        for content in (b"{", b'{"files": [], "files": []}', b"\xff", None):
            with self.subTest(content=content):
                if content is None:
                    self.path.unlink()
                else:
                    self.path.write_bytes(content)
                result = self.cli("verify", "release", "--tag", TAG)
                self.assertEqual(result.returncode, 1)
                self.assertIn("Release manifest failed", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
        result = self.cli("create", "missing", "--tag", TAG)
        self.assertEqual(result.returncode, 1)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(self.cli("verify", "release").returncode, 2)


if __name__ == "__main__":
    unittest.main()
