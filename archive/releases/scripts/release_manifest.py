#!/usr/bin/env python3
"""Create or verify a complete local release archive inventory, offline."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import sys


MANIFEST = "RELEASE-MANIFEST.json"
CHUNK_SIZE = 1024 * 1024


def validate_tag(tag):
    if not isinstance(tag, str) or not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+-zh\.[0-9]+", tag):
        raise ValueError("release_tag must have the form v9.2.13-zh.2")


def validate_path(path):
    if (not isinstance(path, str) or not path or
            any(part in ("", ".", "..") for part in path.split("/")) or
            any(char in path for char in "\\:") or
            any(ord(char) < 32 or ord(char) == 127 for char in path) or
            path == MANIFEST):
        raise ValueError(f"invalid relative file path: {path!r}")


def inventory(directory):
    """Hash all regular files recursively, excluding only the root manifest."""
    files = []

    def visit(folder):
        for path in folder.iterdir():
            relative = path.relative_to(directory).as_posix()
            if relative == MANIFEST:
                continue
            validate_path(relative)
            mode = path.lstat().st_mode
            if stat.S_ISDIR(mode):
                visit(path)
            elif stat.S_ISREG(mode):
                digest = hashlib.sha256()
                size = 0
                with path.open("rb") as source:
                    for chunk in iter(lambda: source.read(CHUNK_SIZE), b""):
                        size += len(chunk)
                        digest.update(chunk)
                files.append({"path": relative, "bytes": size, "sha256": digest.hexdigest()})
            else:
                raise ValueError(f"not a regular file or directory (links unsupported): {relative!r}")

    visit(directory)
    return sorted(files, key=lambda entry: entry["path"])


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def require_fields(value, fields):
    if not isinstance(value, dict) or set(value) != set(fields):
        raise ValueError(f"expected object with fields: {', '.join(fields)}")


def load_manifest(path, tag):
    if not stat.S_ISREG(path.lstat().st_mode):
        raise ValueError("manifest must be a regular file, not a link")
    manifest = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    require_fields(manifest, ("schema_version", "release_tag", "files"))
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1:
        raise ValueError("unsupported schema_version; expected 1")
    validate_tag(manifest["release_tag"])
    if manifest["release_tag"] != tag:
        raise ValueError(f"release_tag must equal {tag!r}")
    if not isinstance(manifest["files"], list) or not manifest["files"]:
        raise ValueError("files must be a nonempty list")
    names = set()
    for entry in manifest["files"]:
        require_fields(entry, ("path", "bytes", "sha256"))
        name = entry["path"]
        validate_path(name)
        if name in names:
            raise ValueError(f"duplicate file path: {name!r}")
        names.add(name)
        if type(entry["bytes"]) is not int or entry["bytes"] < 0:
            raise ValueError(f"bytes must be a nonnegative integer: {name!r}")
        if not isinstance(entry["sha256"], str) or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            raise ValueError(f"sha256 must be 64 lowercase hex characters: {name!r}")
    return manifest


def create_manifest(directory, tag):
    validate_tag(tag)
    target = directory / MANIFEST
    if target.exists() or target.is_symlink():
        raise ValueError(f"refusing to overwrite {MANIFEST}; move the old manifest before creating a new one")
    files = inventory(directory)
    if not files:
        raise ValueError("release directory contains no files")
    manifest = {"schema_version": 1, "release_tag": tag, "files": files}
    # No timestamps or absolute paths: identical inputs produce identical bytes.
    content = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    with target.open("x", encoding="utf-8", newline="\n") as output:
        try:
            output.write(content)
            output.flush()
        except (OSError, UnicodeError):
            target.unlink()
            raise
    return len(files)


def verify_manifest(directory, tag):
    validate_tag(tag)
    manifest = load_manifest(directory / MANIFEST, tag)
    # Never open paths supplied by JSON; compare against the actual directory walk.
    expected = {entry["path"]: entry for entry in manifest["files"]}
    actual = {entry["path"]: entry for entry in inventory(directory)}
    problems = []
    for name in sorted(expected.keys() - actual.keys()):
        problems.append(f"missing file: {name!r}")
    for name in sorted(actual.keys() - expected.keys()):
        problems.append(f"unexpected file: {name!r}")
    for name in sorted(expected.keys() & actual.keys()):
        if actual[name]["bytes"] != expected[name]["bytes"]:
            problems.append(f"byte count mismatch: {name!r}")
        if actual[name]["sha256"] != expected[name]["sha256"]:
            problems.append(f"SHA256 mismatch: {name!r}")
    if problems:
        raise ValueError("\n".join(problems))
    return len(expected)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("create", "verify"))
    parser.add_argument("directory", type=Path, help="local release directory to archive")
    parser.add_argument("--tag", required=True, help="intended release tag, e.g. v9.2.13-zh.2")
    args = parser.parse_args(argv)
    try:
        action = create_manifest if args.command == "create" else verify_manifest
        count = action(args.directory, args.tag)
    except (OSError, ValueError) as error:
        print(f"Release manifest failed: {error}", file=sys.stderr)
        return 1
    verb = "created" if args.command == "create" else "verified"
    print(f"Release manifest {verb}: {args.tag}, {count} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
