#!/usr/bin/env python3
"""Print release notes from checkout metadata and a maintainer's UTF-8 changelog."""

import argparse
from pathlib import Path
import re
import sys

if __package__:
    from .validate_metadata import ROOT, one_version, require, validate_versions
else:
    from validate_metadata import ROOT, one_version, require, validate_versions


REPOSITORY = "https://github.com/Thweki/pve-docs-zh-cn"


def readme_section(text, title):
    """Read one nonempty level-two section in this repository's README format."""
    sections = re.split(r"^##[ \t]+(.+?)[ \t]*$", text, flags=re.MULTILINE)
    bodies = [sections[index + 1].strip()
              for index in range(1, len(sections), 2) if sections[index] == title]
    require(len(bodies) == 1 and bool(bodies[0]),
            f"README.md: expected one nonempty '## {title}' section")
    return f"## {title}\n\n{bodies[0]}"


def generate_notes(root, changes):
    """Return Markdown without reading release assets or writing any files."""
    require(bool(changes.strip()), "change summary must not be empty")
    documents = {name: (Path(root) / name).read_text(encoding="utf-8")
                 for name in ("README.md", "NOTICE.md")}
    validate_versions(documents)
    readme = documents["README.md"]
    release = one_version(re.sub(r"[*`]", "", readme),
                          r"当前发行标签为\s*v?(\d+\.\d+\.\d+-zh\.\d+)(?![\w.-])",
                          "README.md: release")
    tag = "v" + release
    return "\n\n".join([
        f"# Proxmox VE {tag} 中文文档",
        "## 本次更新\n\n" + changes.strip(),
        readme_section(readme, "下载版本"),
        readme_section(readme, "内容范围"),
        "## 来源与许可证\n\n"
        "完整可编辑源码与构建说明见 [源码仓库](https://github.com/Thweki/pve-docs-zh-cn)。\n\n"
        f"本发行的 [来源、版权与许可证声明]({REPOSITORY}/blob/{tag}/NOTICE.md) "
        f"及 [文档许可证全文]({REPOSITORY}/blob/{tag}/LICENSE)。",
    ]) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("changes", type=Path, help="UTF-8 Markdown describing this release's changes")
    parser.add_argument("--root", type=Path, default=ROOT, help="checkout containing README.md and NOTICE.md")
    args = parser.parse_args(argv)
    try:
        notes = generate_notes(args.root, args.changes.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"Release notes generation failed: {error}", file=sys.stderr)
        return 1
    print(notes, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
