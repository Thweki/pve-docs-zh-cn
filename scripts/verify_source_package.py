#!/usr/bin/env python3
"""Verify a source ZIP's embedded inventory and checksums without extracting it.

Usage: python3 -B scripts/verify_source_package.py path/to/source.zip
Requires only the standard library. This checks integrity against the embedded
manifest; it does not authenticate the publisher or establish reproducibility.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile
import zlib

from package_source import safe_name

MANIFEST = "SOURCE-PACKAGE-MANIFEST.json"


def verify_package(path: Path) -> dict:
    """Check the format emitted by package_source.py, reading payloads in chunks."""
    with zipfile.ZipFile(path) as archive:
        members = {}
        roots = set()
        for member in archive.infolist():
            # ZipInfo truncates names at NUL; reject that ambiguity as well.
            if member.orig_filename != member.filename:
                raise ValueError("Ambiguous ZIP member name")
            name = safe_name(member.filename)
            root, separator, _ = name.partition("/")
            if not separator:
                raise ValueError("Source ZIP must have one top-level directory")
            roots.add(root)
            if name in members:
                raise ValueError("Duplicate ZIP member")
            if not stat.S_ISREG(member.external_attr >> 16):
                raise ValueError("Source ZIP contains a non-regular member")
            members[name] = member
        if len(roots) != 1:
            raise ValueError("Source ZIP must have one top-level directory")
        prefix = roots.pop() + "/"
        manifest_name = prefix + MANIFEST
        if manifest_name not in members:
            raise ValueError("Source package manifest is absent")
        manifest = json.loads(archive.read(members.pop(manifest_name)))
        if (not isinstance(manifest, dict) or type(manifest.get("format")) is not int
                or manifest["format"] != 1 or not isinstance(manifest.get("files"), list)):
            raise ValueError("Unsupported source package manifest")
        declared = {}
        for record in manifest["files"]:
            if (not isinstance(record, dict) or not isinstance(record.get("path"), str)
                    or type(record.get("bytes")) is not int or record["bytes"] < 0
                    or not isinstance(record.get("sha256"), str)
                    or not re.fullmatch(r"[0-9a-f]{64}", record["sha256"])):
                raise ValueError("Invalid source package manifest record")
            name = prefix + safe_name(record["path"])
            if name in declared:
                raise ValueError("Duplicate source package manifest path")
            declared[name] = record
        if declared.keys() != members.keys():
            raise ValueError("Source package inventory differs from manifest")
        total = 0
        for name, member in members.items():
            record = declared[name]
            if member.file_size != record["bytes"]:
                raise ValueError("Source package file size differs from manifest")
            digest = hashlib.sha256()
            size = 0
            with archive.open(member) as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
                    size += len(chunk)
            # Reading to EOF also checks the ZIP member's CRC.
            if size != record["bytes"] or digest.hexdigest() != record["sha256"]:
                raise ValueError("Source package file checksum differs from manifest")
            total += size
    return {"status": "passed", "files_verified": len(members), "bytes_verified": total}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="Source ZIP produced by package_source.py")
    args = parser.parse_args()
    try:
        result = verify_package(args.archive)
    except (OSError, ValueError, zipfile.BadZipFile, zlib.error, RuntimeError) as error:
        parser.exit(1, f"Source package verification failed: {error}\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
