#!/usr/bin/env python3
"""Verify local release downloads against a saved SHA256SUMS file, offline."""

import argparse
import hashlib
from pathlib import Path
import re
import sys


def parse_checksums(text):
    """Parse sha256sum text/binary records for flat release attachment names."""
    entries = {}
    for number, line in enumerate(text.split("\n"), 1):
        line = line.removesuffix("\r")
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9a-fA-F]{64}) [ *](.+)", line)
        if match is None:
            raise ValueError(f"line {number}: expected SHA256, two separators and filename")
        digest, name = match.groups()
        if (name in (".", "..") or any(char in name for char in "/\\:") or
                any(ord(char) < 32 or ord(char) == 127 for char in name)):
            raise ValueError(f"line {number}: filename must be a plain attachment name")
        if name in entries:
            raise ValueError(f"line {number}: duplicate filename {name!r}")
        entries[name] = digest.lower()
    if not entries:
        raise ValueError("no checksum entries")
    return entries


def verify_checksums(entries, directory):
    """Yield (success, report) for every entry, reading files in bounded chunks."""
    for name, expected in entries.items():
        path = directory / name
        try:
            if path.is_symlink():
                raise ValueError("symbolic links are not supported")
            if not path.exists():
                yield False, f"{name}: MISSING"
                continue
            if not path.is_file():
                raise ValueError("not a regular file")
            digest = hashlib.sha256()
            with path.open("rb") as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    digest.update(chunk)
            actual = digest.hexdigest()
            if actual == expected:
                yield True, f"{name}: OK"
            else:
                yield False, f"{name}: FAILED (expected {expected}, got {actual})"
        except (OSError, ValueError) as error:
            yield False, f"{name}: ERROR ({error})"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checksums", type=Path, help="saved SHA256SUMS file")
    parser.add_argument("--directory", type=Path,
                        help="download directory (default: SHA256SUMS parent directory)")
    args = parser.parse_args(argv)
    try:
        entries = parse_checksums(args.checksums.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"Checksum verification failed: {error}", file=sys.stderr)
        return 1
    success = True
    for valid, report in verify_checksums(entries, args.directory or args.checksums.parent):
        print(report)
        success = success and valid
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
