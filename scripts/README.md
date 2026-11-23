# Source ZIP verification

Before extracting a downloaded source package, check its embedded file inventory,
sizes, SHA-256 hashes, ZIP CRCs, paths, and regular-file types:

```sh
python3 -B scripts/verify_source_package.py path/to/Proxmox-VE-9.2.13-zh-CN-source.zip
```

This offline command needs only Python's standard library and the checked-out
scripts. It reads the archive without extracting files, running packaged code,
or writing reports. Success prints a JSON summary and exits zero; an invalid
archive exits nonzero. It accepts the source ZIP format from `package_source.py`,
which stores files under one directory without explicit directory entries.

The embedded manifest checks internal integrity, not publisher authenticity or
rebuild reproducibility. It does not recursively audit the bundled upstream TAR.

Run its temporary-fixture tests without export dependencies:

```sh
python3 -B -m unittest discover -s scripts -p 'test_verify_source_package.py' -v
```

The verifier and its tests are included by the existing source package selection
of `scripts/`.
