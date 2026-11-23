"""Source packaging regressions; run with python3 -m unittest discover -s tests -v.

Tiny deterministic render/verify scripts exercise the real isolated subprocess,
snapshot, translation validation, source selection, and ZIP paths without export
dependencies or the production documentation corpus.
"""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile


PROJECT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_source', PROJECT / 'scripts/package_source.py')
package_source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_source)
EVIDENCE = 'reports/source-rebuild-evidence.json'
GENERATED = 'docs/generated.md'
RENDER = '''
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
assert not list((root / 'work').iterdir()), 'inherited work cache'
assert not (root / 'docs/generated.md').exists(), 'inherited generated page'
(root / 'docs/generated.md').write_bytes((root / 'source/prepared/input.txt').read_bytes())
'''
VERIFY = '''
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
assert (root / 'docs/generated.md').read_bytes() == (root / 'source/prepared/input.txt').read_bytes()
(root / 'reports/verification.json').write_text(json.dumps({'passed': True, 'mode': 'release'}))
'''


class SourcePackageTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='test-source-package-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in ('README.md', 'NOTICE.md', 'LICENSE', 'requirements.txt',
                     'requirements-export.txt', 'Brewfile', 'export-assets/fonts/OFL.txt'):
            self.put(name, 'Public fixture\n')
        self.put('export-assets/fonts/FONT-SOURCES.json',
                 json.dumps({'files': {}, 'license': 'Fixture license'}))
        for name in ('AGPL-3.0.txt', 'GPL-2.0.txt', 'GPL-3.0.txt'):
            self.put('LICENSES/' + name, (PROJECT / 'LICENSES' / name).read_bytes())
        for name in ('translate.py', 'package_source.py'):
            source = Path(package_source.__file__) if name == 'package_source.py' else PROJECT / 'scripts' / name
            self.put('scripts/' + name, source.read_bytes())
        self.put('scripts/render.py', RENDER)
        self.put('scripts/verify.py', VERIFY)
        self.put('translations/units.json', json.dumps({str(i): {'text': 'fixture'} for i in range(11508)}))
        self.put('translations/zh-CN.json', json.dumps({str(i): 'fixture' for i in range(11508)}))
        for directory in package_source.INPUT_DIRS:
            self.put(directory + '/input.txt', b'clean generated page\n')
        for name in ('glossary.md', 'copyright.md', 'license-original.md'):
            self.put('docs/' + name, 'Manual fixture page\n')
        self.put(GENERATED, b'clean generated page\n')
        package_source.create_snapshot(self.root)
        self.snapshot, _ = package_source.audit_snapshot(self.root)

    def put(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data.encode() if isinstance(data, str) else data)

    def read_json(self, name):
        return json.loads((self.root / name).read_text())

    def legacy_evidence(self):
        evidence = {
            'status': 'passed',
            'inputs_sha256': {'scripts/render.py': package_source.sha256((self.root / 'scripts/render.py').read_bytes())},
            'main_docs_byte_identical': True,
        }
        self.put(package_source.AUDIT, json.dumps({'status': 'passed', 'cold_rebuild': evidence}))
        return evidence

    def cli(self, mode):
        with patch.object(sys, 'argv', ['package_source.py', '--root', str(self.root), mode]):
            with contextlib.redirect_stdout(io.StringIO()):
                package_source.main()

    def package(self):
        return package_source.package(self.root, 'builds/test-source.zip', self.snapshot)

    def assert_no_zip(self):
        self.assertFalse((self.root / 'builds/test-source.zip').exists())

    def test_changed_generated_docs_cannot_inherit_legacy_success(self):
        self.legacy_evidence()
        self.put(GENERATED, b'changed without rebuilding\n')
        with self.assertRaisesRegex(ValueError, 'Markdown mismatch.*docs/generated.md'):
            self.package()
        self.assert_no_zip()
        self.assertEqual(self.read_json(package_source.AUDIT)['offline_rebuild']['status'], 'failed')

    def test_snapshot_audit_cannot_wipe_rebuild_guard(self):
        evidence = self.legacy_evidence()
        self.cli('--audit-snapshot')
        # Previously the audit erased cold_rebuild, disabling input checks.
        # This renderer change now changes the cold output and must be rejected.
        self.put('scripts/render.py', RENDER + "\n(root / 'docs/generated.md').write_text('changed renderer output')\n")
        with self.assertRaises(ValueError):
            self.package()
        self.assert_no_zip()
        self.assertEqual(self.read_json(EVIDENCE), evidence)

    def test_clean_rebuild_package_binds_exact_archive_inventory(self):
        # Local work overrides must not leak into the isolated build.
        self.put('work/units.json', '{invalid local cache')
        self.put('work/translations.jsonl', 'invalid local translations')
        result = self.package()
        self.assertEqual(result['offline_rebuild']['status'], 'passed')
        evidence = self.read_json(EVIDENCE)
        self.assertEqual(evidence['status'], 'passed')
        self.assertEqual(evidence['markdown_files_compared'], 4)
        self.assertEqual(evidence['outputs_sha256'][GENERATED], package_source.sha256((self.root / GENERATED).read_bytes()))
        with zipfile.ZipFile(self.root / result['package']['path']) as archive:
            prefix = 'Proxmox-VE-' + package_source.VERSION + '-zh-CN-source/'
            manifest = json.loads(archive.read(prefix + 'SOURCE-PACKAGE-MANIFEST.json'))
            archived_evidence = archive.read(prefix + EVIDENCE)
            self.assertEqual(json.loads(archived_evidence), evidence)
            self.assertEqual(manifest['offline_rebuild']['evidence_sha256'], package_source.sha256(archived_evidence))
            records = {record['path']: record for record in manifest['files']}
            self.assertEqual(set(records), set(evidence['package_files_sha256']) | {EVIDENCE})
            for name, digest in evidence['package_files_sha256'].items():
                data = archive.read(prefix + name)
                self.assertEqual(package_source.sha256(data), digest, name)
                self.assertEqual(records[name]['sha256'], digest, name)
            self.assertFalse(any('/work/' in name for name in archive.namelist()))
        # Transient operations must leave independently saved evidence intact.
        saved = (self.root / EVIDENCE).read_bytes()
        for mode in ('--restore-snapshot', '--audit-snapshot', '--snapshot-only'):
            with self.subTest(mode=mode):
                self.cli(mode)
                self.assertEqual((self.root / EVIDENCE).read_bytes(), saved)
                self.assertEqual(self.read_json(package_source.AUDIT)['offline_rebuild']['status'], 'not-verified')
        # A package from the unpacked tree must establish its own evidence.
        unpacked = self.root / 'unpacked'
        with zipfile.ZipFile(self.root / result['package']['path']) as archive:
            archive.extractall(unpacked)
        rebuilt_root = unpacked / prefix
        snapshot, _ = package_source.audit_snapshot(rebuilt_root)
        self.assertEqual(package_source.package(rebuilt_root, 'builds/repacked.zip', snapshot)['offline_rebuild']['status'], 'passed')

    def test_changed_generated_inventory_is_rejected(self):
        self.package()
        (self.root / 'builds/test-source.zip').unlink()
        saved = (self.root / EVIDENCE).read_bytes()
        for change in ('added', 'removed', 'edited'):
            with self.subTest(change=change):
                self.put(GENERATED, b'clean generated page\n')
                if change == 'added':
                    self.put('docs/unexpected.md', 'Unexpected page\n')
                elif change == 'removed':
                    (self.root / GENERATED).unlink()
                else:
                    self.put(GENERATED, 'Stale output\n')
                with self.assertRaisesRegex(ValueError, 'Markdown mismatch'):
                    self.package()
                self.assert_no_zip()
                self.assertEqual((self.root / EVIDENCE).read_bytes(), saved)
                (self.root / 'docs/unexpected.md').unlink(missing_ok=True)

    def test_failed_rebuild_keeps_historical_evidence_and_rejects_package(self):
        self.package()
        saved = (self.root / EVIDENCE).read_bytes()
        (self.root / 'builds/test-source.zip').unlink()
        self.put('scripts/verify.py', 'raise SystemExit(1)\n')
        with self.assertRaisesRegex(ValueError, 'failed in verify.py'):
            self.package()
        self.assertEqual((self.root / EVIDENCE).read_bytes(), saved)
        self.assertEqual(self.read_json(package_source.AUDIT)['offline_rebuild']['status'], 'failed')
        self.assert_no_zip()

    def test_fresh_tree_has_no_implicit_reproducibility_claim(self):
        self.cli('--audit-snapshot')
        self.assertFalse((self.root / EVIDENCE).exists())
        self.assertEqual(self.read_json(package_source.AUDIT)['offline_rebuild']['status'], 'not-verified')
        self.put('scripts/render.py', 'raise SystemExit(1)\n')
        with self.assertRaisesRegex(ValueError, 'failed in render.py'):
            self.package()
        self.assert_no_zip()

    def test_offline_rebuild_blocks_network_and_subprocesses(self):
        for operation in ("import socket; socket.socket()", "import subprocess; subprocess.run(['true'])"):
            with self.subTest(operation=operation):
                self.put('scripts/render.py', operation)
                with self.assertRaisesRegex(ValueError, 'failed in render.py'):
                    self.package()
                self.assert_no_zip()

    def test_stale_verification_report_cannot_substitute_for_new_verification(self):
        self.put('reports/verification.json', json.dumps({'passed': True, 'mode': 'release'}))
        self.put('scripts/verify.py', '# Does not produce a verification report\n')
        with self.assertRaises(OSError):
            self.package()
        self.assertEqual(self.read_json(package_source.AUDIT)['offline_rebuild']['status'], 'failed')
        self.assert_no_zip()

    def test_rebuild_timeout_rejects_package(self):
        with patch.object(package_source.subprocess, 'run', side_effect=subprocess.TimeoutExpired('render.py', 300)):
            with self.assertRaises(subprocess.TimeoutExpired):
                self.package()
        self.assertEqual(self.read_json(package_source.AUDIT)['offline_rebuild']['status'], 'failed')
        self.assert_no_zip()


if __name__ == '__main__':
    unittest.main()
