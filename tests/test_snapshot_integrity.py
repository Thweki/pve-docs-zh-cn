"""Malformed snapshot regressions; run python3 -m unittest discover -s tests -v.

Build tiny tar fixtures independently of create_snapshot(), so the writer cannot
hide a reader regression. All archives and restore destinations are temporary.
"""
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import package_source


class SnapshotIntegrityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="pve-snapshot-integrity-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.payload = [(directory + "/fixture.txt", b"public fixture\n")
                        for directory in package_source.INPUT_DIRS]
        self.records = [{"path": name, "bytes": len(data),
                         "sha256": hashlib.sha256(data).hexdigest()}
                        for name, data in self.payload]

    def member(self, name, data=b"", **attributes):
        info = tarfile.TarInfo(name)
        info.size = len(data)
        for key, value in attributes.items():
            setattr(info, key, value)
        return info, data

    def write_snapshot(self, members=None, records=None, manifest=True):
        if members is None:
            members = [self.member(name, data) for name, data in self.payload]
        else:
            members = list(members)
        if manifest:
            data = json.dumps({"files": self.records if records is None else records}).encode()
            members.append(self.member(package_source.SNAPSHOT_MANIFEST, data))
        path = self.root / package_source.SNAPSHOT
        path.parent.mkdir(parents=True, exist_ok=True)
        with tarfile.open(path, "w:gz", format=tarfile.PAX_FORMAT) as archive:
            for info, data in members:
                archive.addfile(info, io.BytesIO(data))

    def test_valid_fixture_round_trips_exact_bytes(self):
        self.write_snapshot()
        report, entries = package_source.audit_snapshot(self.root)
        self.assertEqual(entries, self.payload)
        self.assertEqual(report["files"], self.records)
        self.assertEqual(report["input_counts"], dict.fromkeys(package_source.INPUT_DIRS, 1))
        self.assertEqual(report["uncompressed_bytes"], sum(len(data) for _, data in self.payload))
        destination = self.root / "restored"
        package_source.restore_snapshot(destination, entries)
        self.assertEqual(sorted(p.relative_to(destination).as_posix()
                                for p in destination.rglob("*") if p.is_file()),
                         sorted(name for name, _ in self.payload))
        for name, data in self.payload:
            self.assertEqual((destination / name).read_bytes(), data)

    def test_duplicate_members_are_rejected_even_with_identical_bytes(self):
        for name in (self.payload[0][0], package_source.SNAPSHOT_MANIFEST):
            with self.subTest(name=name):
                members = [self.member(n, data) for n, data in self.payload]
                data = (json.dumps({"files": self.records}).encode()
                        if name == package_source.SNAPSHOT_MANIFEST else self.payload[0][1])
                members.append(self.member(name, data))
                self.write_snapshot(members)
                with self.assertRaisesRegex(ValueError, "Duplicate snapshot entry"):
                    package_source.audit_snapshot(self.root)

    def test_manifest_is_required(self):
        self.write_snapshot(manifest=False)
        with self.assertRaisesRegex(ValueError, "Snapshot manifest is absent"):
            package_source.audit_snapshot(self.root)

    def test_manifest_inventory_must_match_exactly(self):
        extra = dict(self.records[0], path="source/html/extra.txt")
        for records in (self.records[:-1], self.records + [extra],
                        self.records + [self.records[0]]):
            with self.subTest(records=records):
                self.write_snapshot(records=records)
                with self.assertRaisesRegex(ValueError, "Snapshot manifest coverage mismatch"):
                    package_source.audit_snapshot(self.root)

    def test_manifest_hash_and_size_are_independently_checked(self):
        for field, value in (("sha256", "0" * 64), ("bytes", self.records[0]["bytes"] + 1)):
            with self.subTest(field=field):
                records = [dict(record) for record in self.records]
                records[0][field] = value
                self.write_snapshot(records=records)
                with self.assertRaisesRegex(ValueError, "Snapshot hash mismatch"):
                    package_source.audit_snapshot(self.root)

    def test_changed_payload_with_unchanged_size_is_rejected(self):
        members = [self.member(name, data) for name, data in self.payload]
        name, data = self.payload[0]
        members[0] = self.member(name, b"X" * len(data))
        self.write_snapshot(members)
        with self.assertRaisesRegex(ValueError, "Snapshot hash mismatch"):
            package_source.audit_snapshot(self.root)

    def test_special_members_are_rejected(self):
        for kind in (tarfile.SYMTYPE, tarfile.LNKTYPE, tarfile.DIRTYPE,
                     tarfile.FIFOTYPE, tarfile.CHRTYPE, tarfile.BLKTYPE):
            with self.subTest(kind=kind):
                member = self.member(self.payload[0][0], type=kind,
                                     linkname="source/html/target.txt")
                self.write_snapshot([member])
                with self.assertRaisesRegex(ValueError, "Non-regular snapshot entry"):
                    package_source.audit_snapshot(self.root)

    def test_owner_metadata_is_rejected(self):
        for field, value in (("uid", 1000), ("gid", 1000),
                             ("uname", "fixture-user"), ("gname", "fixture-group")):
            with self.subTest(field=field):
                self.write_snapshot([self.member(*self.payload[0], **{field: value})])
                with self.assertRaisesRegex(ValueError, "local owner metadata"):
                    package_source.audit_snapshot(self.root)

    def test_tar_paths_cannot_escape_or_alias_approved_inputs(self):
        for name in ("../outside", "/source/html/file", "source/html/../file",
                     "source/html//file", "source/html/./file", "source/html/C:drive",
                     "source/html\\file"):
            with self.subTest(name=name):
                self.write_snapshot([self.member(name, b"fixture")])
                with self.assertRaisesRegex(ValueError, "Unsafe archive path"):
                    package_source.audit_snapshot(self.root)

    def test_safe_but_unapproved_paths_are_rejected(self):
        for name in ("docs/page.md", "work/cache.json", "source/html-backup/file"):
            with self.subTest(name=name):
                self.write_snapshot([self.member(name, b"fixture")])
                with self.assertRaisesRegex(ValueError, "Unapproved snapshot input"):
                    package_source.audit_snapshot(self.root)

    def test_late_restore_conflict_does_not_write_earlier_entries(self):
        self.write_snapshot()
        _, entries = package_source.audit_snapshot(self.root)
        destination = self.root / "restored"
        conflict = destination / entries[-1][0]
        conflict.parent.mkdir(parents=True)
        conflict.write_bytes(b"local edit")
        with self.assertRaisesRegex(ValueError, "Refusing to replace changed input"):
            package_source.restore_snapshot(destination, entries)
        self.assertEqual(conflict.read_bytes(), b"local edit")
        for name, _ in entries[:-1]:
            self.assertFalse((destination / name).exists())

    def test_dangling_restore_symlink_is_rejected_before_any_write(self):
        self.write_snapshot()
        _, entries = package_source.audit_snapshot(self.root)
        destination = self.root / "restored"
        link = destination / entries[-1][0]
        link.parent.mkdir(parents=True)
        outside = self.root / "outside.txt"
        link.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Restore destination contains symlink"):
            package_source.restore_snapshot(destination, entries)
        self.assertTrue(link.is_symlink())
        self.assertFalse(outside.exists())
        for name, _ in entries[:-1]:
            self.assertFalse((destination / name).exists())

    def test_source_selection_includes_regression_tests(self):
        test_file = Path(__file__).resolve()
        self.assertIn(test_file, package_source.select_sources(test_file.parents[1]))


if __name__ == "__main__":
    unittest.main()
