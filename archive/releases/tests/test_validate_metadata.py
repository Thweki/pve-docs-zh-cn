"""Exercise real metadata copies; never edit the working checkout."""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts import validate_metadata as validator


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in ("README.md", "NOTICE.md", "LICENSE", "LICENSES", "export-assets"):
            source = validator.ROOT / name
            if source.is_dir():
                shutil.copytree(source, self.root / name)
            else:
                shutil.copyfile(source, self.root / name)
        self.manifest_path = self.root / validator.MANIFEST
        self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def write_manifest(self, manifest):
        self.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def test_checkout_passes_without_release_font_binaries(self):
        for name in validator.UPSTREAM_FILES:
            if name not in validator.LOCAL_LICENSES:
                self.assertFalse((self.root / validator.FONT_DIR / name).exists())
        validator.validate(self.root)

    def test_malformed_and_duplicate_json(self):
        for content in ('{', '{"commit": 1, "commit": 2}',
                        '{"files": {"OFL.txt": {}, "OFL.txt": {}}}'):
            with self.subTest(content=content):
                self.manifest_path.write_text(content, encoding="utf-8")
                with self.assertRaises((validator.ValidationError, json.JSONDecodeError)):
                    validator.validate(self.root)

    def test_manifest_schema_rejects_invalid_values(self):
        cases = [
            ((), [], "expected an object"),
            (("extra",), True, "expected fields"),
            (("repository",), "https://github.com/other/fonts", "repository"),
            (("commit",), "main", "commit"),
            (("commit",), 123, "commit"),
            (("license",), "unknown", "license"),
            (("files",), [], "expected an object"),
            (("files", "extra.ttf"), {}, "expected fields"),
            (("files", "OFL.txt"), None, "expected an object"),
            (("files", "OFL.txt", "extra"), True, "expected fields"),
            (("files", "OFL.txt", "bytes"), 0, "positive integer"),
            (("files", "OFL.txt", "bytes"), -1, "positive integer"),
            (("files", "OFL.txt", "bytes"), True, "positive integer"),
            (("files", "OFL.txt", "bytes"), 1.5, "positive integer"),
            (("files", "OFL.txt", "sha256"), "a" * 63, "sha256"),
            (("files", "OFL.txt", "sha256"), "G" * 64, "sha256"),
            (("files", "OFL.txt", "sha256"), None, "sha256"),
            (("files", "OFL.txt", "url"), None, "url must be a string"),
        ]
        for keys, value, message in cases:
            with self.subTest(keys=keys, value=value):
                manifest = copy.deepcopy(self.manifest)
                if keys:
                    parent = manifest
                    for key in keys[:-1]:
                        parent = parent[key]
                    parent[keys[-1]] = value
                else:
                    manifest = value
                self.write_manifest(manifest)
                with self.assertRaisesRegex(validator.ValidationError, message):
                    validator.validate(self.root)

    def test_missing_required_fields_and_entries(self):
        for keys in (("commit",), ("files", "OFL.txt"), ("files", "NotoEmoji-wght.ttf"),
                     ("files", "OFL.txt", "sha256")):
            with self.subTest(keys=keys):
                manifest = copy.deepcopy(self.manifest)
                parent = manifest
                for key in keys[:-1]:
                    parent = parent[key]
                del parent[keys[-1]]
                self.write_manifest(manifest)
                with self.assertRaisesRegex(validator.ValidationError, "expected fields"):
                    validator.validate(self.root)

    def test_unpinned_or_incorrect_upstreams(self):
        original = self.manifest["files"]["OFL.txt"]["url"]
        commit = self.manifest["commit"]
        urls = [original.replace("https:", "http:"),
                original.replace(commit, "main"),
                original.replace("notofonts/noto-cjk", "google/fonts"),
                original.replace("Sans/LICENSE", "wrong.txt"),
                original + "?download=1", original + "#fragment",
                original.replace(commit, "a" * 40)]
        for url in urls:
            with self.subTest(url=url):
                manifest = copy.deepcopy(self.manifest)
                manifest["files"]["OFL.txt"]["url"] = url
                self.write_manifest(manifest)
                with self.assertRaisesRegex(validator.ValidationError, "URL|commit"):
                    validator.validate(self.root)

    def test_emoji_license_and_font_must_share_separate_commit(self):
        manifest = copy.deepcopy(self.manifest)
        entry = manifest["files"]["OFL-NotoEmoji.txt"]
        entry["url"] = entry["url"].replace(entry["url"].split("/")[5], "b" * 40)
        self.write_manifest(manifest)
        with self.assertRaisesRegex(validator.ValidationError, "Emoji.*commits differ"):
            validator.validate(self.root)

    def test_each_local_license_size_digest_and_presence(self):
        for name in validator.LOCAL_LICENSES:
            path = self.root / validator.FONT_DIR / name
            original = path.read_bytes()
            for data, message in ((original + b"\n", "byte count"),
                                  (b"X" + original[1:], "SHA256")):
                with self.subTest(name=name, message=message):
                    path.write_bytes(data)
                    with self.assertRaisesRegex(validator.ValidationError, message):
                        validator.validate(self.root)
            path.unlink()
            with self.subTest(name=name, message="missing"):
                with self.assertRaises(FileNotFoundError):
                    validator.validate(self.root)
            path.write_bytes(original)

    def test_missing_conflicting_or_mismatched_versions(self):
        readme = (self.root / "README.md").read_text(encoding="utf-8")
        notice = (self.root / "NOTICE.md").read_text(encoding="utf-8")
        cases = [
            ("README.md", readme.replace("当前发行标签为", "标签")),
            ("NOTICE.md", notice.replace("发布版本为", "版本")),
            ("README.md", readme.replace("对应上游文档版本", "上游")),
            ("README.md", readme + "\n当前发行标签为 v9.2.13-zh.3\n"),
            ("NOTICE.md", notice.replace("9.2.13-zh.2", "9.2.13-zh.3")),
            ("NOTICE.md", notice.replace("9.2.13-zh.2", "9.2.14-zh.2")),
            ("NOTICE.md", notice.replace("9.2.13", "9.2.14")),
            ("README.md", readme.replace("**9.2.13**", "**9.2.14**")),
            ("NOTICE.md", notice.replace("Proxmox VE **9.2.13**", "Proxmox VE")),
        ]
        for name, content in cases:
            with self.subTest(name=name, content=content[:40]):
                (self.root / "README.md").write_text(readme, encoding="utf-8")
                (self.root / "NOTICE.md").write_text(notice, encoding="utf-8")
                (self.root / name).write_text(content, encoding="utf-8")
                with self.assertRaisesRegex(validator.ValidationError, "version|disagree"):
                    validator.validate(self.root)

    def test_version_delimiters_preserve_plain_text_equivalence(self):
        documents = {
            "README.md": "当前发行标签为 v9.2.13-zh.2；对应上游文档版本 9.2.13；Proxmox VE 9.2.13。",
            "NOTICE.md": "发布版本为 9.2.13-zh.2；Proxmox VE 9.2.13。",
        }
        for delimiter in ("", "*", "**", "`", "**`", "`***`"):
            with self.subTest(delimiter=delimiter):
                # Include delimiters within declarations as well as around them.
                decorated = {name: delimiter + delimiter.join(text) + delimiter
                             for name, text in documents.items()}
                validator.validate_versions(decorated)

    def test_version_delimiter_removal_preserves_conflicts_and_boundaries(self):
        documents = {name: (self.root / name).read_text(encoding="utf-8")
                     for name in ("README.md", "NOTICE.md")}
        for suffix in ("", "_", ".", "-extra", "中"):
            with self.subTest(suffix=suffix):
                changed = dict(documents)
                version = "9.2.13-zh.2" + suffix if suffix else "9.2.13-zh.3"
                changed["NOTICE.md"] = changed["NOTICE.md"].replace(
                    "9.2.13-zh.2", "**`" + version + "`**")
                with self.assertRaisesRegex(validator.ValidationError, "version"):
                    validator.validate_versions(changed)

    def test_links_allow_directories_encoding_titles_and_fragments(self):
        (self.root / "with space.txt").touch()
        with (self.root / "README.md").open("a", encoding="utf-8") as output:
            output.write('\n[file](with%20space.txt#part) [title](<with space.txt> "title")\n'
                         '[dir](LICENSES/) [anchor](#下载版本)\n'
                         '[external](https://example.invalid/missing)\n'
                         '[mail](mailto:example@example.invalid)\n'
                         '`[source archive example](source/missing)`\n')
        validator.validate(self.root)

    def test_broken_file_and_directory_links(self):
        for name in ("LICENSE", "LICENSES"):
            path = self.root / name
            backup = self.root / (name + ".saved")
            path.rename(backup)
            with self.subTest(name=name):
                with self.assertRaisesRegex(validator.ValidationError, "missing local link"):
                    validator.validate(self.root)
            backup.rename(path)

    def test_link_outside_checkout_is_rejected(self):
        with (self.root / "README.md").open("a", encoding="utf-8") as output:
            output.write("\n[escape](../outside)\n")
        with self.assertRaisesRegex(validator.ValidationError, "escapes checkout"):
            validator.validate(self.root)

    def test_cli_success_and_failure(self):
        command = [sys.executable, str(validator.ROOT / "scripts/validate_metadata.py"),
                   "--root", str(self.root)]
        result = subprocess.run(command, capture_output=True, text=True, cwd=self.root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Metadata valid", result.stdout)
        self.manifest_path.write_text("{", encoding="utf-8")
        result = subprocess.run(command, capture_output=True, text=True, cwd=self.root)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Metadata validation failed", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
