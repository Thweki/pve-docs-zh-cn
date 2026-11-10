#!/usr/bin/env python3
"""Package an existing offline HTML export without rebuilding it.

Example:
  .venv/bin/python scripts/package_html.py --expected-index-sha256 HASH

The ZIP contains one top-level directory and preserves all exported resources.
Symlinks and unsafe archive paths are rejected. Every stored file is checked
against its source bytes, and the ZIP's CRCs are tested before publication.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import stat
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = "Proxmox-VE-9.2.13-zh-CN-html"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_html(source: Path, output: Path, expected_index: str | None = None) -> dict:
    if source.is_symlink() or not source.is_dir():
        raise ValueError("HTML source must be a real directory, not a symlink")
    source = source.resolve()
    paths = sorted(source.rglob("*"))
    for path in paths:
        if path.is_symlink():
            raise ValueError(f"Symlink is not permitted in HTML package: {path}")
        if not path.is_file() and not path.is_dir():
            raise ValueError(f"Non-regular resource in HTML package: {path}")
    files = [path for path in paths if path.is_file()]
    index = source / "index.html"
    index_sha = sha256(index)
    if expected_index and index_sha != expected_index.lower():
        raise ValueError(f"Unexpected index.html SHA256: {index_sha}")
    if output.resolve().is_relative_to(source):
        raise ValueError("Output ZIP must be outside the HTML resource directory")
    source_hashes = {path.relative_to(source).as_posix(): sha256(path) for path in files}
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".tmp.zip")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            # Fixed timestamps and permissions make identical exports reproducible.
            top = zipfile.ZipInfo(PACKAGE + "/", date_time=(2026, 1, 1, 0, 0, 0))
            top.create_system = 3
            top.external_attr = (stat.S_IFDIR | 0o755) << 16
            archive.writestr(top, b"")
            for path in files:
                relative = path.relative_to(source).as_posix()
                archive_path = PurePosixPath(PACKAGE) / relative
                if archive_path.is_absolute() or ".." in archive_path.parts or "\\" in relative:
                    raise ValueError(f"Unsafe archive path: {archive_path}")
                info = zipfile.ZipInfo(str(archive_path), date_time=(2026, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = (stat.S_IFREG | 0o644) << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, path.read_bytes(), compresslevel=9)
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise ValueError("ZIP CRC validation failed")
            archived = {}
            for info in archive.infolist():
                path = PurePosixPath(info.filename)
                if path.is_absolute() or ".." in path.parts or "\\" in info.filename or path.parts[0] != PACKAGE:
                    raise ValueError(f"Unsafe ZIP member: {info.filename}")
                if stat.S_ISLNK(info.external_attr >> 16):
                    raise ValueError(f"Symlink ZIP member: {info.filename}")
                if not info.is_dir():
                    relative = path.relative_to(PACKAGE).as_posix()
                    if relative in archived:
                        raise ValueError(f"Duplicate ZIP member: {info.filename}")
                    archived[relative] = hashlib.sha256(archive.read(info)).hexdigest()
            if archived != source_hashes:
                raise ValueError("Archived file inventory or bytes differ from HTML export")
        # Catch source changes made concurrently while the ZIP was being written.
        if any(sha256(source / relative) != digest for relative, digest in source_hashes.items()):
            raise ValueError("HTML resources changed during packaging")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    report = {"archive": str(output.resolve()), "top_level_directory": PACKAGE, "files": len(files),
              "bytes": output.stat().st_size, "sha256": sha256(output), "index_sha256": index_sha,
              "safe_relative_paths": True, "no_symlinks": True, "crc_valid": True,
              "all_files_match_source_bytes": True, "fixed_zip_timestamps": True}
    output.with_suffix(".report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ROOT / "builds/html")
    parser.add_argument("--output", type=Path, default=ROOT / "builds" / (PACKAGE + ".zip"))
    parser.add_argument("--expected-index-sha256")
    args = parser.parse_args()
    print(json.dumps(package_html(args.source, args.output, args.expected_index_sha256), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
