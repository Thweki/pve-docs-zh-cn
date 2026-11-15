# Offline resource audit tests

Run from the repository root (Python 3.12+):

```sh
python3 -B -m unittest discover -s tests -v
```

The resource fixtures need BeautifulSoup from `requirements.txt`; font-manifest
tests use the standard library. Export integration tests also need markdown-it-py
and PyYAML from `requirements.txt`. They report explicit skips if these are
unavailable. Tests use temporary directories and never fetch fixture URLs.

Coverage includes local versus external Markdown links, percent-encoded paths
and anchors, embedded HTML resources, image candidates, inline CSS, recursive
imports (including cycles), CSS escapes, comments/strings, data URLs, missing
fonts, remote resources, package-directory confinement, and font/license hash
and size validation. Integration fixtures check both HTML outputs and confirm
that exports use the shared font validator. Source archives retain this suite.

For the existing parser/EPUB integration test, install `requirements.txt` and a
compatible Pandoc, then run:

```sh
python3 -B scripts/export_web_epub.py --self-test
```

Validation on 2026-11-15 used Python 3.13.5 and BeautifulSoup 4.15.0:

- Unit suite: 23 passed, 4 exporter integration tests skipped.
- Original `audit_html()` independently failed the new external-Markdown,
  missing-CSS-resource, and remote-CSS-resource fixtures, confirming regression
  coverage.
- Bundled screen CSS and its four font dependencies passed the new audit.
- Existing snapshot audit passed (267 files); license/font validation passed
  (six manifest entries); public translation-map validation passed (11,508 IDs).
- HTML ZIP smoke check, source-archive test inclusion, Python syntax checks,
  JavaScript syntax check, and `git diff --check` passed.
- Full exporter/self-test and rebuild/verify checks could not run: markdown-it-py
  and PyYAML were absent. Pandoc was also unavailable. PDF generation was skipped
  (WeasyPrint and pypdf absent). Package installation failed because DNS/network
  access was unavailable; no dependency versions were changed.
