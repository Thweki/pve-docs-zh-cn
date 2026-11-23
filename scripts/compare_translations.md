# Compare translation maps

Before rebuilding an updated source tree, review which public source units and
translations changed. This offline command uses only Python's standard library:

```sh
python3 -B scripts/compare_translations.py /path/to/previous-source /path/to/candidate-source
python3 -B scripts/compare_translations.py /path/to/previous-source . --check > /tmp/translation-diff.json
```

Both directories must contain `translations/units.json` and
`translations/zh-CN.json`; extracted source releases work without Git history.
The command reads only those four files, ignores local `work/` overrides, and
writes a deterministic JSON report to stdout. No translation text, protected
fragments, or absolute input paths are included in the report.

`sources` and `translations` each contain sorted `added`, `removed`, and `changed`
ID lists plus an `unchanged_count`. Source comparison includes the entire unit
record, including protected fragments. Translation comparison uses exact string
equality, including whitespace. JSON object ordering and serialization whitespace
do not count as changes. Source IDs are content-derived, so an upstream edit
normally appears as a removed ID and an added ID; no fuzzy pairing is attempted.
An ID present in both maps can appear in both `changed` lists.

`coverage.before` and `coverage.after` list `missing` translations (absent or blank)
and `orphaned` translations (IDs without source units), with total record counts.
Partial and empty maps are supported. This is a comparison report, not a
translation-quality or placeholder validator; continue to run `verify.py` for
release validation. Identical incomplete maps have `has_changes: false`.

Exit status is 0 for a successful report, 1 for differences with `--check`, and 2
for invalid inputs or arguments. Errors go to stderr without echoing input data.
Missing files, duplicate JSON keys, malformed records, and nonstandard unit IDs
are rejected before a report is printed. No build/export tools or services run.

Run the fixture tests with:

```sh
python3 -B -m unittest discover -s scripts -p 'test_compare_translations.py' -v
```

The tool, these instructions, and its tests are included by the existing source
package selection of `scripts/`.
