# Release attachment checks in the source repository

This is the first, additive consolidation step. It makes the existing offline
attachment checks available from `Thweki/pve-docs-zh-cn`; it does not publish a
release, move assets or tags, archive the old repository, redirect download
links, or change GitBook configuration.

## Check attachment metadata

Save a single GitHub release API response obtained through an already authorized
read, then check its intended tag and five required uploaded, nonempty assets:

```sh
python3 -B scripts/check_release_assets.py /path/to/release.json --tag v9.2.13-zh.2
```

The input must be one release object, not a list of releases. The checker expects
EPUB, PDF, HTML ZIP, source ZIP and `SHA256SUMS` names for the upstream version in
the tag, and checks the full tag including the Chinese revision. It allows extra
attachments. It does not download assets, verify their contents, or publish.

## Check downloaded bytes

Download a trusted `SHA256SUMS` and its listed attachments to a local directory:

```sh
python3 -B scripts/verify_checksums.py /path/to/downloads/SHA256SUMS
python3 -B scripts/verify_checksums.py /path/to/SHA256SUMS --directory /path/to/downloads
```

This checks each listed regular file in bounded chunks and reports all failures.
It does not authenticate the checksum list, require a complete release, create
a local manifest, or upload anything. Use the metadata and byte checks together;
neither is a publication or reproducibility gate by itself.

## Tests and packaging

Both helpers and their tests use only Python's standard library. Existing source
CI already discovers `tests/`, including these two new test files:

```sh
python3 -B -m unittest discover -s tests -p 'test_check_release_assets.py' -v
python3 -B -m unittest discover -s tests -p 'test_verify_checksums.py' -v
```

The existing source-package selection includes `scripts/` and `tests/`, so these
files need no packaging-rule change. A full source-package build still needs the
repository's declared inputs, translations, fonts, license files and existing
release checks. These helpers do not replace those checks.

## Origin and unchanged notices

The following files are copied byte-for-byte from
[`Thweki/pve-docs-zh-cn-releases` at `d780a83912763ea0807fb667a1b72939cd44d03b`](https://github.com/Thweki/pve-docs-zh-cn-releases/tree/d780a83912763ea0807fb667a1b72939cd44d03b):

- `scripts/check_release_assets.py` (Git blob `c554d01d96add9524e64043b29f324dde482c5bf`)
- `scripts/verify_checksums.py` (Git blob `6cd63cab5995a3c81c1be0be780bcb896a689a85`)
- `tests/test_check_release_assets.py` (Git blob `8db7ae81877fd90a0734a0a960a173f3254438f3`)
- `tests/test_verify_checksums.py` (Git blob `f1a0741149c8d1eff3813d9accf860e2dfbbed47`)

Their existing docstrings and file contents are retained. The source and donor
repositories share the same `NOTICE.md` at this baseline. It states that the
project's Python build programs are Copyright (C) 2026 project contributors,
AGPL-3.0-or-later. See [the unchanged notice](../NOTICE.md) and
[the existing AGPL text](../LICENSES/AGPL-3.0.txt). This migration does not
substitute licenses or change upstream/document/font notices.

## Deferred publication gates

- Preserve all existing releases, assets, old download links and historic tags.
- Do not rewrite the historic `v9.2.13-zh.2` tag.
- Resolve the known incomplete/malformed root GFDL text through a separate,
  reviewed correction. This helper migration does not repair or alter `LICENSE`.
- Build and verify the first release in the source repository, including actual
  attachment contents and license/package checks, before switching download
  documentation or GitBook references.
- Archive the old release repository only after the verified replacement and
  preservation checks. No archival or automatic publishing is implemented here.
