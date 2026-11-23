"""Check offline note generation against isolated copies of release metadata."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts import generate_release_notes as notes


class ReleaseNotesTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in ("README.md", "NOTICE.md"):
            (self.root / name).write_bytes((notes.ROOT / name).read_bytes())
        self.changes = self.root / "changes.md"
        self.changes.write_text("- 更新翻译。\n- 改进 PDF 排版。\n", encoding="utf-8")

    def run_cli(self, *arguments):
        return subprocess.run(
            [sys.executable, str(notes.ROOT / "scripts/generate_release_notes.py"),
             str(self.changes), *arguments],
            cwd=self.root, capture_output=True, text=True, encoding="utf-8")

    def test_complete_notes_preserve_summary_and_readme_content(self):
        summary = "- 更新 **翻译**。\n\n  保留 Markdown 排版。"
        result = notes.generate_notes(self.root, summary)
        self.assertTrue(result.startswith("# Proxmox VE v9.2.13-zh.2 中文文档\n"))
        self.assertIn("## 本次更新\n\n" + summary, result)
        self.assertIn("| EPUB | 完整电子书", result)
        self.assertIn("| SHA256 校验文件 |", result)
        self.assertIn("**680 个 API 操作**", result)
        self.assertIn("未经 Proxmox 官方审核", result)
        self.assertIn("https://thweki.gitbook.io/pve-docs-zh-cn/", result)
        for name in ("NOTICE.md", "LICENSE"):
            self.assertIn(f"{notes.REPOSITORY}/blob/v9.2.13-zh.2/{name}", result)
        self.assertNotIn("## 元数据校验", result)
        self.assertNotIn("## 生成发行说明", result)
        self.assertTrue(result.endswith("\n"))

    def test_versions_and_scope_follow_checkout_updates(self):
        for name in ("README.md", "NOTICE.md"):
            path = self.root / name
            text = path.read_text(encoding="utf-8")
            path.write_text(text.replace("9.2.13-zh.2", "10.0.1-zh.4")
                            .replace("9.2.13", "10.0.1")
                            .replace("680 个 API", "700 个 API"), encoding="utf-8")
        result = notes.generate_notes(self.root, "- 新版。")
        self.assertIn("# Proxmox VE v10.0.1-zh.4 中文文档", result)
        self.assertIn("对应上游文档版本 **10.0.1**", result)
        self.assertIn("/blob/v10.0.1-zh.4/NOTICE.md", result)
        self.assertIn("**700 个 API 操作**", result)
        self.assertNotIn("9.2.13", result)

    def test_empty_summaries_are_rejected(self):
        for summary in ("", " \n\t"):
            with self.subTest(summary=summary):
                with self.assertRaisesRegex(ValueError, "summary must not be empty"):
                    notes.generate_notes(self.root, summary)

    def test_required_sections_must_be_unique_and_nonempty(self):
        for title in ("下载版本", "内容范围"):
            for text in ("# Other\n", f"## {title}\n \n## Other\nText",
                         f"## {title}\nOne\n## {title}\nTwo"):
                with self.subTest(title=title, text=text):
                    with self.assertRaisesRegex(ValueError, "expected one nonempty"):
                        notes.readme_section(text, title)

    def test_sections_keep_nested_headings_and_stop_at_next_peer(self):
        self.assertEqual(notes.readme_section(
            "## 内容范围\n\n正文\n### 子节\n细节\n## Other\nExcluded", "内容范围"),
            "## 内容范围\n\n正文\n### 子节\n细节")

    def test_cli_from_another_directory_is_read_only_and_needs_no_assets(self):
        before = {path.name: path.read_bytes() for path in self.root.iterdir()}
        result = self.run_cli("--root", str(self.root))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, notes.generate_notes(
            self.root, self.changes.read_text(encoding="utf-8")))
        self.assertEqual(before, {path.name: path.read_bytes() for path in self.root.iterdir()})

    def test_default_root_is_script_checkout_not_current_directory(self):
        (self.root / "README.md").unlink()
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("## 本次更新", result.stdout)

    def test_cli_errors_have_no_partial_notes_or_traceback(self):
        notice = self.root / "NOTICE.md"
        readme = self.root / "README.md"
        originals = {path: path.read_bytes() for path in (notice, readme, self.changes)}
        cases = [
            (notice, originals[notice].replace(b"9.2.13-zh.2", b"9.2.13-zh.3"), "disagree"),
            (readme, originals[readme].replace("## 内容范围".encode(), b"## Other"), "section"),
            (self.changes, b" \n", "empty"),
            (self.changes, b"\xff", "decode"),
            (self.changes, None, "No such file"),
            (notice, None, "No such file"),
        ]
        for path, data, message in cases:
            with self.subTest(path=path.name, message=message):
                for original_path, original in originals.items():
                    original_path.write_bytes(original)
                if data is None:
                    path.unlink()
                else:
                    path.write_bytes(data)
                result = self.run_cli("--root", str(self.root))
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertIn("Release notes generation failed:", result.stderr)
                self.assertIn(message, result.stderr)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
