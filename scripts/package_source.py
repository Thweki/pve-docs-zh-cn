#!/usr/bin/env python3
"""Package the public, reproducible Chinese documentation sources.

Run --snapshot-only while the public upstream inputs are available. The default
mode selects the current source tree at run time and requires the complete
translations/units.json and translations/zh-CN.json maps. It never includes Git
history, local translation-service state, work/, builds/, or QA images.

After unpacking the source ZIP, --restore-snapshot restores the public upstream
inputs needed by scripts/render.py. Only Python's standard library is required
for snapshot creation, restoration, validation, and ZIP packaging.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '9.2.13'
RELEASE = VERSION + '-zh.2'
EPOCH = 1794268800  # 2026-11-10 00:00:00 UTC; reproducible archive metadata.
SNAPSHOT = 'source/upstream-snapshot.tar.gz'
AUDIT = 'reports/source-package-audit.json'
SNAPSHOT_MANIFEST = 'SOURCE-SNAPSHOT-MANIFEST.json'
INPUT_DIRS = ('source/html', 'source/api', 'source/prepared', 'source/raw-assets')
SOURCE_DIRS = ('docs', 'scripts', 'export-assets', 'fonts', 'LICENSES', '.github')
REPORTS = ('images.json', 'verification.json', 'render.json',
           'translation-progress.json', 'independent-review.json',
           'export-verification.json')
IGNORED_NAMES = {'.DS_Store', '__pycache__', '.git', '.venv', 'node_modules'}
SECRET_PATTERNS = {
    'private-key': rb'-----BEGIN (?:RSA |EC |DSA |OPENSSH |PGP )?PRIVATE KEY(?: BLOCK)?-----',
    'github-token': rb'\b(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{30,})\b',
    'provider-token': rb'\bsk-(?:proj-|ant-api\d+-)?[A-Za-z0-9_-]{20,}\b',
    'aws-key': rb'\b(?:AKIA|ASIA)[A-Z0-9]{16}\b',
    'google-api-key': rb'\bAIza[0-9A-Za-z_-]{30,}\b',
    'jwt': rb'\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}',
    'oauth-local-callback': rb'(?:localhost|127\.0\.0\.1)[^\s<>\"]*[?&](?:code|access_token|refresh_token|id_token)=[A-Za-z0-9_%.-]{12,}',
}


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_name(name: str) -> str:
    """Reject traversal, platform-specific paths, and ambiguous archive names."""
    path = PurePosixPath(name)
    if (not name or path.is_absolute() or '\\' in name or
            any(p in ('', '.', '..') or ':' in p for p in name.split('/'))):
        raise ValueError('Unsafe archive path: ' + repr(name))
    return name


def files_in(root: Path, relative: str) -> list[Path]:
    directory = root / relative
    if directory.is_symlink():
        raise ValueError('Symlink source directory: ' + relative)
    if not directory.is_dir():
        return []
    result: list[Path] = []
    for parent, dirs, files in os.walk(directory, followlinks=False):
        parent_path = Path(parent)
        for name in dirs:
            if (parent_path / name).is_symlink():
                raise ValueError('Symlink source directory: ' + str((parent_path / name).relative_to(root)))
        dirs[:] = sorted(n for n in dirs if n not in IGNORED_NAMES)
        for name in sorted(files):
            if name in IGNORED_NAMES or name.endswith(('.pyc', '.pyo', '.swp', '~')):
                continue
            path = parent_path / name
            if path.is_symlink() or not stat.S_ISREG(path.lstat().st_mode):
                raise ValueError('Non-regular source file: ' + str(path.relative_to(root)))
            safe_name(path.relative_to(root).as_posix())
            result.append(path)
    return result


def scan(data: bytes, path: str) -> list[dict]:
    """Report categories and locations only; never emit candidate secret values."""
    findings = []
    for category, pattern in SECRET_PATTERNS.items():
        for match in re.finditer(pattern, data):
            findings.append({'path': path, 'category': category,
                             'line': data.count(b'\n', 0, match.start()) + 1})
    # Public Linux home-directory examples in upstream manuals are intentional.
    for match in re.finditer(rb'/Users/[A-Za-z0-9_.-]+/', data):
        findings.append({'path': path, 'category': 'local-macos-path',
                         'line': data.count(b'\n', 0, match.start()) + 1})
    return findings


def write_report(root: Path, report: dict) -> None:
    path = root / AUDIT
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json_bytes(report))


def create_snapshot(root: Path) -> None:
    files = []
    for directory in INPUT_DIRS:
        group = files_in(root, directory)
        if not group:
            raise ValueError('Missing public upstream input directory: ' + directory)
        files.extend(group)
    payload = []
    findings = []
    for path in sorted(files):
        name = path.relative_to(root).as_posix()
        data = path.read_bytes()
        findings.extend(scan(data, name))
        payload.append((name, data))
    if findings:
        write_report(root, {'status': 'rejected', 'snapshot_findings': findings})
        raise ValueError('Snapshot audit rejected input; see ' + AUDIT)
    manifest = {
        'format': 1, 'version': VERSION,
        'source_url': 'https://pve.proxmox.com/pve-docs/',
        'contents': 'Public original inputs and reproducible preparation cache only; no work or service logs.',
        'files': [{'path': n, 'bytes': len(b), 'sha256': sha256(b)} for n, b in payload],
    }
    target = root / SNAPSHOT
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('wb') as raw, gzip.GzipFile(filename='', mode='wb', fileobj=raw, mtime=EPOCH) as zipped:
        with tarfile.open(fileobj=zipped, mode='w', format=tarfile.PAX_FORMAT) as archive:
            for name, data in payload + [(SNAPSHOT_MANIFEST, json_bytes(manifest))]:
                member = tarfile.TarInfo(safe_name(name))
                member.size = len(data)
                member.mtime = EPOCH
                member.uid = member.gid = 0
                member.uname = member.gname = ''
                member.mode = 0o644
                archive.addfile(member, io.BytesIO(data))


def audit_snapshot(root: Path) -> tuple[dict, list[tuple[str, bytes]]]:
    path = root / SNAPSHOT
    entries: list[tuple[str, bytes]] = []
    seen = set()
    manifest = None
    findings = []
    with tarfile.open(path, 'r:gz') as archive:
        for member in archive:
            name = safe_name(member.name)
            if name in seen:
                raise ValueError('Duplicate snapshot entry: ' + name)
            seen.add(name)
            if not member.isfile() or member.issym() or member.islnk():
                raise ValueError('Non-regular snapshot entry: ' + name)
            if member.uid or member.gid or member.uname or member.gname:
                raise ValueError('Snapshot contains local owner metadata: ' + name)
            if name != SNAPSHOT_MANIFEST and not any(name.startswith(d + '/') for d in INPUT_DIRS):
                raise ValueError('Unapproved snapshot input: ' + name)
            data = archive.extractfile(member).read()
            findings.extend(scan(data, name))
            if name == SNAPSHOT_MANIFEST:
                manifest = json.loads(data)
            else:
                entries.append((name, data))
    if manifest is None:
        raise ValueError('Snapshot manifest is absent')
    declared = manifest.get('files', [])
    expected = {record['path']: record for record in declared}
    if len(expected) != len(declared) or expected.keys() != {n for n, _ in entries}:
        raise ValueError('Snapshot manifest coverage mismatch')
    for name, data in entries:
        if expected[name]['sha256'] != sha256(data) or expected[name]['bytes'] != len(data):
            raise ValueError('Snapshot hash mismatch: ' + name)
    if findings:
        raise ValueError('Snapshot contains audit findings: ' + json.dumps(findings))
    return {
        'path': SNAPSHOT, 'bytes': path.stat().st_size,
        'sha256': sha256(path.read_bytes()), 'file_count': len(entries),
        'input_counts': {d: sum(n.startswith(d + '/') for n, _ in entries) for d in INPUT_DIRS},
        'uncompressed_bytes': sum(len(b) for _, b in entries),
        'manifest_verified': True, 'unsafe_paths': 0, 'symlinks': 0,
        'owner_metadata': 0, 'secret_pattern_findings': findings,
        'files': declared,
    }, entries


def restore_snapshot(root: Path, entries: list[tuple[str, bytes]]) -> None:
    """Extract vetted regular files without trusting tarfile extraction rules."""
    for name, data in entries:
        target = root / name
        for part in (target, *target.parents):
            if part == root.parent:
                break
            if part.is_symlink():
                raise ValueError('Restore destination contains symlink: ' + name)
        if target.exists() and target.read_bytes() != data:
            raise ValueError('Refusing to replace changed input: ' + name)
    for name, data in entries:
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            target.write_bytes(data)


def validate_translations(root: Path) -> dict:
    units = json.loads((root / 'translations/units.json').read_text())
    translated = json.loads((root / 'translations/zh-CN.json').read_text())
    if not isinstance(units, dict) or not isinstance(translated, dict):
        raise ValueError('Translation maps must be JSON objects')
    if len(units) != 11508 or units.keys() != translated.keys():
        raise ValueError('Expected exactly 11508 matching source and translation IDs')
    spec = importlib.util.spec_from_file_location('source_package_translate', root / 'scripts/translate.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    errors = [{'id': k, 'error': error} for k, unit in units.items()
              if (error := module.validate(unit['text'], translated[k]))]
    if errors:
        raise ValueError('Invalid public translation maps: ' + json.dumps(errors[:20]))
    return {'source_units': len(units), 'translations': len(translated), 'validation_errors': 0}


def select_sources(root: Path) -> list[Path]:
    selected = []
    for path in sorted(root.iterdir()):
        if path.is_file() and (path.name in ('LICENSE', 'Brewfile', '.gitignore', '.gitbook.yaml') or
                               (not path.name.startswith('.') and path.suffix in ('.md', '.txt', '.yaml', '.yml', '.toml'))):
            selected.append(path)
    for directory in SOURCE_DIRS:
        selected.extend(files_in(root, directory))
    for name in ('units.json', 'zh-CN.json'):
        selected.append(root / 'translations' / name)
    for path in sorted((root / 'source').glob('*.json')):
        if path.name != 'publication.json':  # Account-specific editor IDs are not build inputs.
            selected.append(path)
    selected.append(root / SNAPSHOT)
    for name in REPORTS:
        if (root / 'reports' / name).is_file():
            selected.append(root / 'reports' / name)
    result = sorted(set(selected))
    for path in result:
        safe_name(path.relative_to(root).as_posix())
        if path.is_symlink() or not path.is_file():
            raise ValueError('Missing or non-regular public source: ' + str(path.relative_to(root)))
    for required in ('README.md', 'NOTICE.md', 'LICENSE', 'LICENSES/AGPL-3.0.txt',
                     'LICENSES/GPL-2.0.txt', 'LICENSES/GPL-3.0.txt',
                     'requirements.txt', 'requirements-export.txt', 'Brewfile',
                     'scripts/render.py', 'scripts/package_source.py',
                     'export-assets/fonts/OFL.txt', 'export-assets/fonts/FONT-SOURCES.json'):
        if root / required not in result:
            raise ValueError('Required public source absent: ' + required)
    return result


def validate_licenses_and_fonts(root: Path) -> dict:
    license_path = root / 'LICENSES/AGPL-3.0.txt'
    license_data = license_path.read_bytes()
    if (len(license_data) < 30000 or b'GNU AFFERO GENERAL PUBLIC LICENSE' not in license_data or
            b'END OF TERMS AND CONDITIONS' not in license_data):
        raise ValueError('The complete official AGPL text is required')
    gpl = []
    for version, url, minimum in (
        ('2.0', 'https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt', 17000),
        ('3.0', 'https://www.gnu.org/licenses/gpl-3.0.txt', 34000),
    ):
        name = f'LICENSES/GPL-{version}.txt'
        data = (root / name).read_bytes()
        if len(data) < minimum or b'GNU GENERAL PUBLIC LICENSE' not in data or b'END OF TERMS AND CONDITIONS' not in data:
            raise ValueError('The complete official GPL text is required: ' + name)
        gpl.append({'path': name, 'source_url': url, 'bytes': len(data), 'sha256': sha256(data)})
    fonts = root / 'export-assets/fonts'
    font_manifest = json.loads((fonts / 'FONT-SOURCES.json').read_text())
    for name, record in font_manifest['files'].items():
        safe_name(name)
        data = (fonts / name).read_bytes()
        if sha256(data) != record['sha256'] or len(data) != record['bytes']:
            raise ValueError('Bundled font/license hash mismatch: ' + name)
    return {
        'agpl': {'path': 'LICENSES/AGPL-3.0.txt',
                 'source_url': 'https://www.gnu.org/licenses/agpl-3.0.txt',
                 'bytes': len(license_data), 'sha256': sha256(license_data)},
        'gpl': gpl,
        'fonts': {'files_verified': len(font_manifest['files']),
                  'manifest': 'export-assets/fonts/FONT-SOURCES.json',
                  'license': font_manifest['license'],
                  'verified_entries': sorted(font_manifest['files'])},
    }


def package(root: Path, output: str | None, snapshot: dict) -> dict:
    translations = validate_translations(root)
    files = select_sources(root)
    licenses = validate_licenses_and_fonts(root)
    previous = json.loads((root / AUDIT).read_text()) if (root / AUDIT).exists() else {}
    cold_rebuild = previous.get('cold_rebuild')
    if cold_rebuild:
        changed = [name for name, digest in cold_rebuild.get('inputs_sha256', {}).items()
                   if not (root / name).is_file() or sha256((root / name).read_bytes()) != digest]
        if cold_rebuild.get('status') != 'passed' or changed:
            raise ValueError('Refresh the offline cold rebuild audit before packaging; changed inputs: ' + ', '.join(changed))
    contents = []
    findings = []
    for path in files:
        name = path.relative_to(root).as_posix()
        data = path.read_bytes()
        # The compressed public snapshot is audited separately, including its contents.
        if name != SNAPSHOT:
            findings.extend(scan(data, name))
        contents.append((name, data))
    if findings:
        write_report(root, {'status': 'rejected', 'snapshot': snapshot, 'package_findings': findings})
        raise ValueError('Public source audit rejected input; see ' + AUDIT)
    manifest = {
        'format': 1, 'upstream_version': VERSION, 'release': RELEASE,
        'translations': translations,
        'licenses': licenses,
        'offline_rebuild': ({k: v for k, v in cold_rebuild.items()
                             if k not in ('steps', 'verification')} if cold_rebuild else None),
        'snapshot': {k: v for k, v in snapshot.items() if k != 'files'},
        'excluded': ['.git/', '.venv/', 'work/', 'builds/', 'tmp/', 'preview/',
                     'source/publication.json', 'OAuth/usage/session logs', 'QA PDF/PNG files'],
        'files': [{'path': n, 'bytes': len(b), 'sha256': sha256(b)} for n, b in contents],
    }
    name = safe_name(output or f'builds/Proxmox-VE-{VERSION}-zh-CN-source.zip')
    if not name.startswith('builds/') or not name.endswith('.zip'):
        raise ValueError('The source ZIP output must be a relative .zip path under builds/')
    target = root / name
    if target in files:
        raise ValueError('Output cannot replace a source file')
    target.parent.mkdir(parents=True, exist_ok=True)
    prefix = f'Proxmox-VE-{VERSION}-zh-CN-source/'
    with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for filename, data in contents + [('SOURCE-PACKAGE-MANIFEST.json', json_bytes(manifest))]:
            item = zipfile.ZipInfo(prefix + safe_name(filename), date_time=(2026, 11, 10, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.create_system = 3
            item.external_attr = ((stat.S_IFREG | (0o755 if filename.startswith('scripts/') and filename.endswith('.py') else 0o644)) << 16)
            archive.writestr(item, data, compresslevel=9)
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ValueError('Source ZIP CRC verification failed')
        for member in archive.infolist():
            safe_name(member.filename)
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError('Source ZIP contains a symlink')
    result = {
        'status': 'passed', 'snapshot': snapshot, 'translations': translations, 'licenses': licenses,
        'package': {'path': name, 'bytes': target.stat().st_size,
                    'sha256': sha256(target.read_bytes()), 'file_count': len(contents) + 1,
                    'crc_verified': True, 'manifest_path': prefix + 'SOURCE-PACKAGE-MANIFEST.json'},
        'package_findings': findings,
    }
    if cold_rebuild:
        result['cold_rebuild'] = cold_rebuild
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Project root; defaults to the script parent directory')
    parser.add_argument('--output', help='Relative ZIP output path within the project')
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument('--snapshot-only', action='store_true', help='Create and audit the public upstream snapshot')
    modes.add_argument('--audit-snapshot', action='store_true', help='Audit the existing snapshot without making the final ZIP')
    modes.add_argument('--restore-snapshot', action='store_true', help='Safely restore public upstream inputs for rebuilding')
    args = parser.parse_args()
    root = args.root.resolve()
    if args.snapshot_only:
        create_snapshot(root)
    snapshot, entries = audit_snapshot(root)
    if args.restore_snapshot:
        restore_snapshot(root, entries)
        report = {'status': 'restored', 'snapshot': snapshot}
    elif args.snapshot_only or args.audit_snapshot:
        report = {'status': 'snapshot-ready', 'snapshot': snapshot,
                  'source_zip': 'not built; final source selection happens at package run time'}
    else:
        report = package(root, args.output, snapshot)
    write_report(root, report)
    print(json.dumps({k: v for k, v in report.items() if k != 'snapshot'}, ensure_ascii=False))
    print(json.dumps({k: v for k, v in snapshot.items() if k != 'files'}, ensure_ascii=False))


if __name__ == '__main__':
    main()
