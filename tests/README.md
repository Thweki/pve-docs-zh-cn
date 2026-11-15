# Tests

Run from the repository root (Python 3.12+):

```sh
python3 -B -m unittest discover -s tests -v
```

## Offline resource audit tests

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

## PDF export regressions

The fixtures are synthetic; they do not require rebuilding the book or editing
translation sources. All test inputs, styles and fonts are local. Tests use
temporary directories and do not modify the fixtures or release reports.

- Preprocessing and section-text tests need `lxml`. They cover normal API tables,
  the 900/901-character and 14/15-line conversion boundaries, nested tables,
  captions, mixed header/data cells, footer rows, text after tables, details and
  chapter anchors.
- Font rejection tests need `pypdf`, but no renderer or native dependencies.
  They construct small PDFs with unembedded simple/descendant fonts and no fonts.
- Rendering tests need `requirements-export.txt`, Pango and Poppler (`pdftoppm`,
  `pdfinfo`, `pdffonts`). On Ubuntu install `libpango-1.0-0`,
  `libpangoft2-1.0-0` and `poppler-utils`. They run the actual exporter with `--qa`,
  exercise a record spanning pages, require embedded regular/bold/monospace Noto
  fonts, then remove font streams from that PDF and require QA to fail.

`--qa` now checks every chapter's complete prepared text as an ordered subsequence
of text extracted from that chapter's page range. Whitespace differences, repeated
table headers and page furniture are allowed. A dropped short chapter, missing
table/code content or reordered text cannot pass just because the total extracted
length remains above 95%. The report records `section_text_checks` for each chapter.
This is a text-integrity check; printable-area checks and rendered page review
remain necessary for layout QA.

Missing Python/native dependencies are reported as explicit unittest skips locally.
Set `PVE_PDF_REQUIRE_DEPS=1` to turn missing dependencies into failures, as CI does.
Once dependencies are present, rendering/export errors always fail; they are never
treated as skips. The fixture render has a 120-second timeout and must produce
5–8 pages. CI bounds the test command to 180 seconds and the entire job to 10 minutes.
It runs on relevant pull requests or manually, without a full source/book rebuild.

### Worktree validation

The available bundled Python 3.12 (lxml 6.1.1, pypdf 6.21.4) passed all 11
preprocessing, section-text and offline font tests. The rendering class (two tests)
was skipped because WeasyPrint is not installed; installing either the pinned
70.0 version or an unpinned version returned no available distribution in this
environment. Poppler is available. Full rendering, font embedding in a newly
rendered PDF and visual QA therefore remain unverified here. The CI strict-mode
check was separately verified to fail on the missing renderer. CI installs the
repository's pinned export requirements, including pypdf 6.10.0.
Automated workflow YAML parsing could not run locally because neither PyYAML nor
the Node `yaml` package is installed; the workflow was inspected manually.

## Merge validation (2026-11-15)

The combined suite ran on Python 3.13.5 with
`python3 -B -m unittest discover -s tests -v`: unittest reported 44 tests,
`OK (skipped=6)`. Four exporter integration tests were skipped because
markdown-it-py is unavailable; PyYAML is also absent. The PDF font and rendering
classes were skipped because pypdf is unavailable; WeasyPrint is also absent.
The parser/EPUB self-test and full exports were not run because these Python
dependencies and Pandoc are unavailable. Poppler is installed.
Python syntax checks passed for all 13 files in `scripts/` and `tests/`;
`node --check export-assets/offline.js` and `git diff --check` also passed.
