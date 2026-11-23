import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from scripts.check_release_assets import check_release_assets


ROOT = Path(__file__).resolve().parents[1]
TAG = "v9.2.13-zh.2"
NAMES = [
    "Proxmox-VE-9.2.13-zh-CN.epub",
    "Proxmox-VE-9.2.13-zh-CN.pdf",
    "Proxmox-VE-9.2.13-zh-CN-html.zip",
    "Proxmox-VE-9.2.13-zh-CN-source.zip",
    "SHA256SUMS",
]


def release_fixture():
    return {"tag_name": TAG, "assets": [
        {"name": name, "state": "uploaded", "size": 123} for name in NAMES
    ]}


class ReleaseInventoryTests(unittest.TestCase):
    def test_complete_release_and_draft(self):
        for draft in (False, True):
            with self.subTest(draft=draft):
                release = release_fixture()
                release["draft"] = draft
                self.assertEqual(check_release_assets(release, TAG), NAMES)

    def test_each_required_asset_must_be_present(self):
        for index, name in enumerate(NAMES):
            with self.subTest(name=name):
                release = release_fixture()
                release["assets"].pop(index)
                with self.assertRaisesRegex(ValueError, "missing asset") as error:
                    check_release_assets(release, TAG)
                self.assertIn(name, str(error.exception))

    def test_reports_all_missing_assets(self):
        with self.assertRaises(ValueError) as error:
            check_release_assets({"tag_name": TAG, "assets": []}, TAG)
        for name in NAMES:
            self.assertIn(name, str(error.exception))

    def test_old_version_assets_do_not_satisfy_new_tag(self):
        release = release_fixture()
        release["tag_name"] = "v9.2.14-zh.1"
        with self.assertRaisesRegex(ValueError, "Proxmox-VE-9.2.14-zh-CN"):
            check_release_assets(release, "v9.2.14-zh.1")

    def test_future_release_uses_tag_version_for_names(self):
        release = release_fixture()
        release["tag_name"] = "v10.0.1-zh.12"
        for asset in release["assets"]:
            asset["name"] = asset["name"].replace("9.2.13", "10.0.1")
        expected = [name.replace("9.2.13", "10.0.1") for name in NAMES]
        self.assertEqual(check_release_assets(release, "v10.0.1-zh.12"), expected)

    def test_different_translation_revision_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "tag_name"):
            check_release_assets(release_fixture(), "v9.2.13-zh.3")

    def test_invalid_tag(self):
        for tag in ("latest", "9.2.13-zh.2", "v9.2.13-zh.2\n"):
            with self.subTest(tag=tag), self.assertRaisesRegex(ValueError, "expected tag"):
                check_release_assets(release_fixture(), tag)

    def test_missing_or_incomplete_upload_state(self):
        for state in (None, "starter", "uploading", "", True):
            with self.subTest(state=state):
                release = release_fixture()
                release["assets"][0]["state"] = state
                with self.assertRaisesRegex(ValueError, "not uploaded"):
                    check_release_assets(release, TAG)

    def test_missing_empty_or_invalid_size(self):
        for size in (None, 0, -1, True, "123", 1.5):
            with self.subTest(size=size):
                release = release_fixture()
                release["assets"][-1]["size"] = size
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    check_release_assets(release, TAG)

    def test_duplicate_names_rejected(self):
        release = release_fixture()
        release["assets"].append(dict(release["assets"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate asset"):
            check_release_assets(release, TAG)

    def test_extra_assets_allowed(self):
        release = release_fixture()
        release["assets"].append({"name": "SHA256SUMS.asc", "state": "uploaded", "size": 30})
        self.assertEqual(check_release_assets(release, TAG), NAMES)

    def test_malformed_response(self):
        for release in (None, [], {}, {"tag_name": TAG},
                        {"tag_name": TAG, "assets": {}},
                        {"tag_name": TAG, "assets": [None]},
                        {"tag_name": TAG, "assets": [{"name": 123}]}):
            with self.subTest(release=release), self.assertRaises(ValueError):
                check_release_assets(release, TAG)

    def test_cli_from_another_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            snapshot = Path(directory) / "release.json"
            for content, code, message in (
                (json.dumps(release_fixture()), 0, "5 required assets"),
                (json.dumps({"tag_name": TAG, "assets": []}), 1, "missing asset"),
                ("invalid json", 1, "Release inventory check failed"),
                (None, 1, "Release inventory check failed"),
            ):
                with self.subTest(content=content):
                    if content is None:
                        snapshot.unlink()
                    else:
                        snapshot.write_text(content, encoding="utf-8")
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "scripts/check_release_assets.py"),
                         str(snapshot), "--tag", TAG],
                        cwd=directory, capture_output=True, text=True,
                    )
                    self.assertEqual(result.returncode, code, result.stderr)
                    self.assertIn(message, result.stdout if code == 0 else result.stderr)
                    self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
