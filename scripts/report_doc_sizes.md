# Documentation size regression report

Large API groups and whole-chapter pages can grow unnoticed during regeneration.
`report_doc_sizes.py` ranks the largest Markdown pages and compares page sizes
against a saved baseline, without rendering, restoring snapshots, or reading
translation-service state. It needs only Python's standard library.

Run from the repository root:

```sh
python3 -B scripts/report_doc_sizes.py
python3 -B scripts/report_doc_sizes.py --format json > /tmp/docs-before.json
# After regenerating docs, or use --docs /path/to/another/docs tree:
python3 -B scripts/report_doc_sizes.py --baseline /tmp/docs-before.json
```

The default Markdown report lists the ten largest pages and every added,
removed, or resized page, ordered by decreasing byte growth. JSON output includes
the complete inventory with stable relative paths and no timestamps or absolute
paths. Either a first-run or comparison JSON report can serve as a baseline;
comparison totals are recomputed from its `pages` inventory.

For an optional CI gate, choose a per-page growth allowance in bytes:

```sh
python3 -B scripts/report_doc_sizes.py \
  --baseline /tmp/docs-before.json --max-growth-bytes 65536
```

Exit status is **0** for a successful report within the budget (or no budget),
**1** if any page grows by more than the allowance, and **2** for invalid inputs
or arguments. A new page starts from zero; shrinkage elsewhere cannot offset
an oversized addition or increase. Equality passes. The full report is still
printed on budget failure. The allowance must be nonnegative and requires a
baseline. Baselines should come from a trusted build of the same docs tree;
there is no automatic Git or network access.

Sizes are raw UTF-8 file bytes, including frontmatter and `SUMMARY.md`, and
exclude non-Markdown assets. This is a size signal, not a rendered HTML size,
browser-performance benchmark, content diff, or completeness check. Same-size
edits are invisible; renames appear as removal plus addition. A missing/empty
Markdown tree, symlinked directory, or non-regular Markdown file is rejected.
The command writes only to stdout; save reports outside the measured docs tree.

Run the isolated fixture tests:

```sh
python3 -B -m unittest discover -s scripts -p 'test_report_doc_sizes.py' -v
```

The report, documentation, and tests reside in `scripts/`, so the existing
source packager includes them without changes to its inventory rules.
