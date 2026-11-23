#!/usr/bin/env python3
"""Check the upload inventory in a saved GitHub release API response, offline."""

import argparse
import json
from pathlib import Path
import re
import sys


def check_release_assets(release, tag):
    """Return expected asset names or raise ValueError for an incomplete release."""
    match = re.fullmatch(r"v([0-9]+\.[0-9]+\.[0-9]+)-zh\.[0-9]+", tag)
    if not match:
        raise ValueError("expected tag must have the form v9.2.13-zh.2")
    if not isinstance(release, dict) or release.get("tag_name") != tag:
        raise ValueError(f"release tag_name must equal {tag!r}")
    assets = release.get("assets")
    if not isinstance(assets, list):
        raise ValueError("release assets must be a list")

    by_name = {}
    for asset in assets:
        if not isinstance(asset, dict) or not isinstance(asset.get("name"), str):
            raise ValueError("each asset must be an object with a string name")
        name = asset["name"]
        if name in by_name:
            raise ValueError(f"duplicate asset: {name!r}")
        by_name[name] = asset

    prefix = f"Proxmox-VE-{match.group(1)}-zh-CN"
    expected = [prefix + suffix for suffix in (".epub", ".pdf", "-html.zip", "-source.zip")]
    expected.append("SHA256SUMS")
    problems = []
    for name in expected:
        asset = by_name.get(name)
        if asset is None:
            problems.append(f"missing asset: {name}")
            continue
        if asset.get("state") != "uploaded":
            problems.append(f"asset is not uploaded: {name}")
        size = asset.get("size")
        if type(size) is not int or size <= 0:
            problems.append(f"asset size must be a positive integer: {name}")
    if problems:
        raise ValueError("; ".join(problems))
    return expected


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("release_json", type=Path, help="saved GitHub release API JSON object")
    parser.add_argument("--tag", required=True, help="intended release tag, e.g. v9.2.13-zh.2")
    args = parser.parse_args(argv)
    try:
        release = json.loads(args.release_json.read_text(encoding="utf-8"))
        names = check_release_assets(release, args.tag)
    except (OSError, ValueError) as error:
        print(f"Release inventory check failed: {error}", file=sys.stderr)
        return 1
    print(f"Release inventory OK: {args.tag}, {len(names)} required assets uploaded and nonempty.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
