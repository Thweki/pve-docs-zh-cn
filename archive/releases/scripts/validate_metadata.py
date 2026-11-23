#!/usr/bin/env python3
"""Validate this release-metadata checkout without downloads or dependencies."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path("export-assets/fonts")
MANIFEST = FONT_DIR / "FONT-SOURCES.json"
CJK_REPOSITORY = "https://github.com/notofonts/noto-cjk"
UPSTREAM_FILES = {
    "NotoSansCJKsc-Regular.otf": ("notofonts/noto-cjk", "Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Regular.otf"),
    "NotoSansCJKsc-Bold.otf": ("notofonts/noto-cjk", "Sans/OTF/SimplifiedChinese/NotoSansCJKsc-Bold.otf"),
    "NotoSansMonoCJKsc-Regular.otf": ("notofonts/noto-cjk", "Sans/Mono/NotoSansMonoCJKsc-Regular.otf"),
    "OFL.txt": ("notofonts/noto-cjk", "Sans/LICENSE"),
    "NotoEmoji-wght.ttf": ("google/fonts", "ofl/notoemoji/NotoEmoji[wght].ttf"),
    "OFL-NotoEmoji.txt": ("google/fonts", "ofl/notoemoji/OFL.txt"),
}
LOCAL_LICENSES = ("OFL.txt", "OFL-NotoEmoji.txt")


class ValidationError(ValueError):
    """Invalid release metadata, reported without a traceback by the CLI."""


def require(condition, message):
    if not condition:
        raise ValidationError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"{MANIFEST}: duplicate JSON key {key!r}")
        result[key] = value
    return result


def require_fields(value, fields, label):
    require(isinstance(value, dict), f"{label}: expected an object")
    require(set(value) == set(fields), f"{label}: expected fields {', '.join(sorted(fields))}")


def validate_manifest(root):
    manifest = json.loads((root / MANIFEST).read_text(encoding="utf-8"),
                          object_pairs_hook=unique_object)
    require_fields(manifest, ("repository", "commit", "license", "files"), str(MANIFEST))
    require(manifest["repository"] == CJK_REPOSITORY, f"{MANIFEST}: unexpected CJK repository")
    require(isinstance(manifest["commit"], str) and
            re.fullmatch(r"[0-9a-f]{40}", manifest["commit"]),
            f"{MANIFEST}: commit must be 40 lowercase hexadecimal characters")
    require(manifest["license"] == "SIL Open Font License 1.1", f"{MANIFEST}: unexpected license")
    require_fields(manifest["files"], UPSTREAM_FILES, f"{MANIFEST}: files")
    emoji_commits = set()
    for name, (repository, upstream_path) in UPSTREAM_FILES.items():
        entry = manifest["files"][name]
        label = f"{MANIFEST}: {name}"
        require_fields(entry, ("url", "bytes", "sha256"), label)
        require(type(entry["bytes"]) is int and entry["bytes"] > 0,
                f"{label}: bytes must be a positive integer")
        require(isinstance(entry["sha256"], str) and
                re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]),
                f"{label}: sha256 must be 64 lowercase hexadecimal characters")
        require(isinstance(entry["url"], str), f"{label}: url must be a string")
        # Match the entire URL: no credentials, query string, fragment or floating ref.
        match = re.fullmatch(
            r"https://raw\.githubusercontent\.com/" + re.escape(repository) +
            r"/([0-9a-f]{40})/" + re.escape(upstream_path), unquote(entry["url"]))
        require(match is not None, f"{label}: expected HTTPS URL pinned to a full upstream commit")
        commit = match.group(1)
        if repository == "notofonts/noto-cjk":
            require(commit == manifest["commit"], f"{label}: URL commit differs from CJK commit")
        else:
            emoji_commits.add(commit)
    require(len(emoji_commits) == 1, f"{MANIFEST}: Emoji font and license commits differ")

    for name in LOCAL_LICENSES:
        data = (root / FONT_DIR / name).read_bytes()
        entry = manifest["files"][name]
        require(len(data) == entry["bytes"], f"{FONT_DIR / name}: byte count mismatch")
        require(hashlib.sha256(data).hexdigest() == entry["sha256"],
                f"{FONT_DIR / name}: SHA256 mismatch")


def one_version(text, pattern, label):
    versions = set(re.findall(pattern, text))
    require(len(versions) == 1, f"{label}: missing or conflicting version declarations")
    return versions.pop()


def validate_versions(documents):
    # Ignore Markdown emphasis/code delimiters, while keeping the declarations explicit.
    texts = {name: text.replace("*", "").replace("`", "") for name, text in documents.items()}
    releases = []
    upstreams = []
    for name, text in texts.items():
        prefix = "当前发行标签为" if name == "README.md" else "发布版本为"
        release = one_version(text, prefix + r"\s*v?(\d+\.\d+\.\d+-zh\.\d+)(?![\w.-])",
                              f"{name}: release")
        upstream = one_version(text, r"Proxmox VE\s+(\d+\.\d+\.\d+)(?![\w.-])",
                               f"{name}: upstream")
        if name == "README.md":
            declared = one_version(text, r"对应上游文档版本\s+(\d+\.\d+\.\d+)(?![\w.-])",
                                   f"{name}: download upstream")
            require(declared == upstream, f"{name}: upstream declarations disagree")
        require(release.split("-zh.")[0] == upstream, f"{name}: release and upstream disagree")
        releases.append(release)
        upstreams.append(upstream)
    require(len(set(releases)) == 1, "README.md and NOTICE.md: release versions disagree")
    require(len(set(upstreams)) == 1, "README.md and NOTICE.md: upstream versions disagree")


def validate_links(root, documents):
    # These documents use inline Markdown links. Code spans describe source-archive
    # paths and are not local links. Anchors are excluded from filesystem checks.
    link_pattern = r"!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))(?:\s+[\"'][^\n]*?[\"'])?\s*\)"
    for name, text in documents.items():
        text = re.sub(r"`[^`\n]*`", "", text)
        for match in re.finditer(link_pattern, text):
            target = match.group(1) or match.group(2)
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            destination = (root / Path(name).parent / unquote(url.path)).resolve()
            require(destination.is_relative_to(root), f"{name}: local link escapes checkout: {target}")
            require(destination.exists(), f"{name}: missing local link target: {target}")


def validate(root):
    root = Path(root).resolve()
    validate_manifest(root)
    documents = {name: (root / name).read_text(encoding="utf-8")
                 for name in ("README.md", "NOTICE.md")}
    validate_versions(documents)
    validate_links(root, documents)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="checkout to validate")
    args = parser.parse_args()
    try:
        validate(args.root)
    except (ValidationError, OSError, UnicodeError, ValueError) as error:
        print(f"Metadata validation failed: {error}", file=sys.stderr)
        return 1
    print("Metadata valid: manifest, two local OFL files, versions and local links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
