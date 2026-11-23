# Tooling CI

`workflows/tooling.yml` runs on every push and pull request with only
`contents: read`. It uses Ubuntu 24.04, Python 3.12, Node.js 24, and the pinned
dependencies in `requirements.txt`. The tests use Python's built-in `unittest`;
`requirements-export.txt` and native rendering libraries are unnecessary.

Run the same checks locally from the repository root:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m compileall -q scripts tests
.venv/bin/python -m unittest discover -s tests -v
if [ -f export-assets/offline.js ]; then
  node --check export-assets/offline.js
fi
```

The offline audit reads the checked-in `source/upstream-snapshot.tar.gz` and
verifies its complete manifest, file sizes and hashes, allowed paths, file
types, and owner metadata. It takes about two seconds locally. Small tests also
cover safe archive names, snapshot restoration without overwriting local edits
or following symlinks, and reproducible HTML ZIP packaging with byte preservation
and rejection of symlinks and unsafe output locations. Fixtures and build outputs
stay in temporary directories; the tests do not modify `docs/`, translations, or
committed reports, or access the network.

The existing `scripts/export_web_epub.py --self-test` also builds an EPUB and
requires Pandoc options such as `--split-level` and `--syntax-highlighting`.
No compatible Pandoc installation was available to validate locally, so this
first workflow uses the offline snapshot audit instead of adding an unverified
Pandoc download or version pin. Full-book HTML/EPUB exports and the 1,921-page
PDF build remain manual release checks. CI does not run `prepare.py`,
`translate.py`, fetch upstream inputs, deploy, or publish anything.
