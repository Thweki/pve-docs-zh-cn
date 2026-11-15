"""Offline source ZIP consumer tests; all archives live in temporary directories."""
import copy
import hashlib
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import warnings
import zipfile

import package_source
import verify_source_package as verifier


class SourcePackageVerificationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.path = self.root / "source.zip"
        self.prefix = "Proxmox-VE-9.2.13-zh-CN-source/"
        self.files = {"docs/中文.md": "测试\n".encode(), "scripts/build.py": b"raise RuntimeError()\n"}
        self.manifest = {"format": 1, "files": [
            {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            for name, data in self.files.items()
        ]}

    def write_archive(self, files=None, manifest=..., extra=(), mode=stat.S_IFREG | 0o644):
        files = self.files if files is None else files
        manifest = self.manifest if manifest is ... else manifest
        entries = [(self.prefix + name, data) for name, data in files.items()]
        entries += [(self.prefix + verifier.MANIFEST, json.dumps(manifest).encode())]
        entries += list(extra)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)  # Deliberate duplicate members.
            with zipfile.ZipFile(self.path, "w") as archive:
                for name, data in entries:
                    info = zipfile.ZipInfo(name)
                    info.create_system = 3
                    info.external_attr = mode << 16
                    archive.writestr(info, data)

    def test_valid_archive_is_read_only_and_does_not_execute_packaged_code(self):
        self.write_archive()
        before = self.path.read_bytes()
        with mock.patch.object(zipfile.ZipFile, "extract", side_effect=AssertionError), \
                mock.patch.object(zipfile.ZipFile, "extractall", side_effect=AssertionError):
            result = verifier.verify_package(self.path)
        self.assertEqual(result, {"status": "passed", "files_verified": 2,
                                  "bytes_verified": sum(map(len, self.files.values()))})
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(list(self.root.iterdir()), [self.path])

    def test_accepts_actual_source_packager_output(self):
        source = self.root / "example.txt"
        source.write_bytes(b"example")
        # Exercise the real ZIP writer without requiring the production maps/fonts.
        with mock.patch.object(package_source, "validate_translations", return_value={}), \
                mock.patch.object(package_source, "validate_licenses_and_fonts", return_value={}), \
                mock.patch.object(package_source, "select_sources", return_value=[source]):
            result = package_source.package(self.root, None, {})
        verified = verifier.verify_package(self.root / result["package"]["path"])
        self.assertEqual(verified["files_verified"], 1)
        self.assertEqual(verified["bytes_verified"], 7)

    def test_changed_bytes_with_valid_zip_crc_fail_manifest_checksum(self):
        changed = dict(self.files)
        changed["scripts/build.py"] = b"x" * len(changed["scripts/build.py"])
        self.write_archive(files=changed)
        with zipfile.ZipFile(self.path) as archive:
            self.assertIsNone(archive.testzip())
        with self.assertRaisesRegex(ValueError, "checksum"):
            verifier.verify_package(self.path)

    def test_changed_size_fails(self):
        self.write_archive(files={**self.files, "scripts/build.py": b"short"})
        with self.assertRaisesRegex(ValueError, "size"):
            verifier.verify_package(self.path)

    def test_missing_and_extra_files_fail(self):
        for files in ({"docs/中文.md": self.files["docs/中文.md"]}, {**self.files, "extra": b""}):
            with self.subTest(files=list(files)):
                self.write_archive(files=files)
                with self.assertRaisesRegex(ValueError, "inventory"):
                    verifier.verify_package(self.path)

    def test_duplicate_zip_members_fail(self):
        for name in ("docs/中文.md", verifier.MANIFEST):
            with self.subTest(name=name):
                self.write_archive(extra=[(self.prefix + name, b"duplicate")])
                with self.assertRaisesRegex(ValueError, "Duplicate ZIP"):
                    verifier.verify_package(self.path)

    def test_duplicate_manifest_paths_fail(self):
        self.manifest["files"].append(self.manifest["files"][0])
        self.write_archive()
        with self.assertRaisesRegex(ValueError, "Duplicate source package manifest"):
            verifier.verify_package(self.path)

    def test_unsafe_zip_paths_fail(self):
        for name in ("/absolute", "../escape", self.prefix + "../escape",
                     self.prefix + "a\\b", self.prefix + "a//b", "C:/file"):
            with self.subTest(name=name):
                self.write_archive(extra=[(name, b"unsafe")])
                with self.assertRaisesRegex(ValueError, "Unsafe archive path"):
                    verifier.verify_package(self.path)

    def test_unsafe_manifest_paths_fail(self):
        for name in ("../escape", "/absolute", "a\\b", "./file"):
            with self.subTest(name=name):
                manifest = copy.deepcopy(self.manifest)
                manifest["files"][0]["path"] = name
                self.write_archive(manifest=manifest)
                with self.assertRaisesRegex(ValueError, "Unsafe archive path"):
                    verifier.verify_package(self.path)

    def test_symlinks_and_special_members_fail(self):
        for mode in (stat.S_IFLNK, stat.S_IFIFO, stat.S_IFDIR):
            with self.subTest(mode=mode):
                self.write_archive(mode=mode | 0o644)
                with self.assertRaisesRegex(ValueError, "non-regular"):
                    verifier.verify_package(self.path)

    def test_missing_manifest_and_multiple_roots_fail(self):
        with zipfile.ZipFile(self.path, "w") as archive:
            info = zipfile.ZipInfo(self.prefix + "file")
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, b"data")
        with self.assertRaisesRegex(ValueError, "manifest is absent"):
            verifier.verify_package(self.path)
        self.write_archive(extra=[("other/file", b"data")])
        with self.assertRaisesRegex(ValueError, "one top-level directory"):
            verifier.verify_package(self.path)

    def test_invalid_manifest_shapes_fail(self):
        for manifest in ([], None, {"format": 2, "files": []}, {"format": True, "files": []},
                         {"format": 1}, {"format": 1, "files": {}}, {"format": 1, "files": [None]}):
            with self.subTest(manifest=manifest):
                self.write_archive(manifest=manifest)
                with self.assertRaises(ValueError):
                    verifier.verify_package(self.path)

    def test_invalid_manifest_record_fields_fail(self):
        for key, value in (("path", 1), ("bytes", -1), ("bytes", True),
                           ("bytes", "7"), ("sha256", "bad"), ("sha256", None)):
            with self.subTest(key=key, value=value):
                manifest = copy.deepcopy(self.manifest)
                manifest["files"][0][key] = value
                self.write_archive(manifest=manifest)
                with self.assertRaisesRegex(ValueError, "Invalid source package manifest record"):
                    verifier.verify_package(self.path)

    def test_corrupt_zip_crc_fails(self):
        self.write_archive()
        data = self.path.read_bytes()
        payload = self.files["scripts/build.py"]
        self.path.write_bytes(data.replace(payload, b"x" * len(payload), 1))
        with self.assertRaises(zipfile.BadZipFile):
            verifier.verify_package(self.path)

    def test_cli_exit_status_and_no_output_files(self):
        self.write_archive()
        command = [sys.executable, "-B", str(Path(verifier.__file__).resolve()), str(self.path)]
        passed = subprocess.run(command, cwd=self.root, capture_output=True, text=True)
        self.assertEqual(passed.returncode, 0, passed.stderr)
        self.assertEqual(json.loads(passed.stdout)["files_verified"], 2)
        self.path.write_bytes(b"not a zip")
        failed = subprocess.run(command, cwd=self.root, capture_output=True, text=True)
        self.assertEqual(failed.returncode, 1)
        self.assertEqual(failed.stdout, "")
        self.assertIn("Source package verification failed", failed.stderr)
        self.assertNotIn("Traceback", failed.stderr)
        self.assertEqual(list(self.root.iterdir()), [self.path])

    def test_verifier_and_tests_are_selected_for_source_packages(self):
        names = {path.name for path in package_source.files_in(package_source.ROOT, "scripts")}
        self.assertTrue({"verify_source_package.py", Path(__file__).name, "README.md"} <= names)


if __name__ == "__main__":
    unittest.main()
