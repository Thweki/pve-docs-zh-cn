# PDF export regressions

Run from the repository root with Python 3.12+:

```sh
python3 -m unittest discover -s tests -v
```

The fixtures are synthetic; they do not require rebuilding the book or editing
translation sources. All test inputs, styles and fonts are local. Tests use
temporary directories and do not modify the fixtures or release reports.

- `test_doc_index.py` needs the Markdown tooling in `requirements.txt`. It
  covers SUMMARY order/depth, Chinese and formatted titles, synthetic H1s,
  duplicate headings, encoded links matching exported chapter IDs, title
  filtering, deterministic read-only CLI output, and invalid/missing navigation.
  It needs neither Pandoc nor a built book.
- `test_doc_crossrefs.py` uses the same Markdown dependencies. Its 12 tests
  cover broken and ambiguous targets, distinct export candidate IDs, repeated
  aliases on one heading, explicit IDs and title collisions, named bookmarks,
  encoded Chinese paths/fragments, synthetic headings, reference/HTML/table/hint
  links, ignored code/assets/external links, escaping symlinks, deterministic
  read-only JSON, and CLI exit codes. Run it alone with
  `python3 -m unittest discover -s tests -p test_doc_crossrefs.py -v`.
  The report uses the exporter's first-match aliases without changing exported
  links; ambiguity is additional diagnostic information, not a new build gate.
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

## Worktree validation

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

## API fragment parse cache

`python3 -m unittest discover -s tests -p test_render_parse_cache.py -v`
requires BeautifulSoup and markdownify from `requirements.txt`. The four tests
cover reuse across schema fields/calls, unchanged nested data, translation and
fragment edits, and eviction at the 1,024-entry limit. The parse-count test fails
against the original implementation (four parses instead of one).

On the frozen API schema, a cold cache reduced HTML parses from 7,308 to 2,784
(4,524 hits), with identical complete schema output. An isolated full render
also matched all 72 Markdown files, the render report, and the anchor map byte
for byte against the original implementation. No release files were rewritten.
Local unittest discovery reported 21 tests OK and two PDF class skips because
pypdf is unavailable; WeasyPrint is also absent. Full verification and HTML/EPUB
export were not run because markdown-it-py, PyYAML and Pandoc are unavailable.
Python compilation, offline JavaScript syntax and `git diff --check` passed.

## Cross-reference report validation

The cross-reference worktree passed all 60 runnable tests, including 12 new
cross-reference tests. PDF font and rendering test classes were skipped because
`pypdf` is unavailable; WeasyPrint and Pandoc are also absent, so full PDF/EPUB
exports were not run. The system Python lacks Markdown dependencies and a pip
install attempt failed due to unavailable network/DNS. Tests instead used
existing local packages without changing repository requirements:

```sh
PYTHONPATH=/tmp/pve-docs-venv/lib/python3.13/site-packages \
  /tmp/pve-crossrefs-venv/bin/python -B -m unittest discover -s tests -v
```

The report checked 1,118 links across all 71 current book pages with zero issues.
An in-memory comparison against the parent revision confirmed identical heading
IDs, alias selections, rewritten links and chapter HTML for all 71 pages.
Python syntax, offline JavaScript syntax and `git diff --check` also passed.
