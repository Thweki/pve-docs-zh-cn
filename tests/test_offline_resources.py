"""Offline resource fixtures. Run: python3 -m unittest discover -s tests -v."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from offline_resources import audit_html
from package_source import validate_fonts, validate_licenses_and_fonts

try:
    import export_web_epub as exporter
except ModuleNotFoundError as error:
    if error.name not in {"markdown_it", "yaml"}:
        raise
    exporter = None
    EXPORT_SKIP = f"Exporter requires requirements.txt dependencies (missing {error.name})"
else:
    EXPORT_SKIP = ""


class ResourceFixtures(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name) / "html"
        self.base.mkdir()

    def write(self, name, text="fixture"):
        path = self.base / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def css(self, text):
        self.write("screen.css", text)
        return '<link rel="stylesheet" href="screen.css">'

    def test_external_markdown_links_and_navigation_remain_usable(self):
        for url in ("https://example.invalid/README.md", "http://example.invalid/a.md?q=1#x",
                    "//example.invalid/README.md", "HTTPS://example.invalid/a.md",
                    "mailto:reader@example.invalid", "https://example.invalid/README%2Emd"):
            with self.subTest(url=url):
                audit_html(f'<a href="{url}">Source</a>', self.base)
        audit_html('<link rel="canonical" href="https://example.invalid/">', self.base)

    def test_unrewritten_local_markdown_links_fail(self):
        self.write("README.md")
        for url in ("README.md", "./README.md?raw=1#heading", "README%2emd", "nested/../README.md"):
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, "Unrewritten Markdown link"):
                audit_html(f'<a href="{url}">Local</a>', self.base)

    def test_anchors_are_still_audited(self):
        result = audit_html('<h1 id="中文">Title</h1><a href="#%E4%B8%AD%E6%96%87">Jump</a>', self.base)
        self.assertEqual(result["internal_links"], 1)
        for text, message in (('<a href="#missing">Jump</a>', "Broken single-page anchor"),
                              ('<p id="same"></p><p id="same"></p>', "Duplicate ID")):
            with self.subTest(text=text), self.assertRaisesRegex(ValueError, message):
                audit_html(text, self.base)

    def test_nested_imports_resolve_from_each_stylesheet_and_allow_cycles(self):
        self.write("fonts/font file.otf")
        self.write("images/icon.svg")
        self.write("css/nested/theme", '@import url("../../screen.css"); '
                   '@font-face { src: url("../../fonts/font%20file.otf?v=1#face") } '
                   '@media print { p { background: URL(../../images/icon.svg) } }')
        text = self.css('@import "css/nested/theme" screen; '
                        'p { mask: url(#filter); background: url(data:image/png;base64,eA==) }')
        audit_html(text, self.base)

    def test_missing_css_resources_and_imports_fail(self):
        for css in ('@font-face {src: url(fonts/missing.otf)}',
                    'p{background:URL("missing image.png?rev=1#x")}',
                    '@import "missing.css";', "@import 'missing.css' print;",
                    '@import url(missing.css) layer(theme);',
                    r'p{background:u\72l(missing\20 image.png)}',
                    'p{background:image-set(url(missing.png) 1x)}',
                    'p{background:image-set("missing.png" 1x)}'):
            with self.subTest(css=css), self.assertRaisesRegex(ValueError, "Missing packaged dependency"):
                audit_html(self.css(css), self.base)

    def test_remote_css_urls_fail_in_all_supported_forms(self):
        for css in ('@import "https://example.invalid/theme.css";',
                    "@import '//example.invalid/theme.css';",
                    '@import url(https://example.invalid/theme.css);',
                    '@font-face {src: url("https://example.invalid/font.otf")}',
                    'p{background:url(//example.invalid/image.png)}',
                    r'p{background:u\72l(\68 ttps\3a //example.invalid/image.png)}',
                    'p{background:image-set("https://example.invalid/image.png" 1x)}',
                    'p{background:url(file:///tmp/font.otf)}'):
            with self.subTest(css=css), self.assertRaisesRegex(ValueError, "Remote dependency"):
                audit_html(self.css(css), self.base)

    def test_transitive_remote_and_missing_import_resources_fail(self):
        for url, message in (("../fonts/missing.otf", "Missing packaged dependency"),
                             ("https://example.invalid/font.otf", "Remote dependency")):
            self.write("css/theme.css", f'@font-face{{src:url("{url}")}}')
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, message):
                audit_html(self.css('@import url("css/theme.css");'), self.base)

    def test_comments_and_ordinary_strings_are_not_dependencies(self):
        audit_html(self.css('/* @import "missing.css"; url(https://example.invalid/x) */ '
                            'p::after{content:"url(missing.png)"}'), self.base)

    def test_image_set_local_and_data_candidates(self):
        self.write("image.png")
        audit_html(self.css('p{background:image-set("image.png" type("image/png") 1x, '
                            'url("data:image/png;base64,eA==") 2x)}'), self.base)

    def test_css_quoted_parentheses_and_escapes(self):
        self.write("font (regular).otf")
        self.write("font)regular.otf")
        audit_html(self.css('@font-face{src:url("font (regular).otf")} '
                            r'@font-face{src:url(font\)regular.otf)}'), self.base)

    def test_inline_css_is_audited(self):
        self.write("image.png")
        audit_html('<style>p{background:url(image.png)}</style>'
                   '<p style="mask:url(#filter)">Text</p>', self.base)
        for text in ('<style>@import "missing.css";</style>',
                     '<p style="background:url(https://example.invalid/image.png)">Text</p>'):
            with self.subTest(text=text), self.assertRaises(ValueError):
                audit_html(text, self.base)

    def test_embedded_data_stylesheets_are_audited(self):
        audit_html(self.css('@import "data:text/css,p%7Bcolor:red%7D";'), self.base)
        for css in ('@import "data:text/css,@import%20%27https://example.invalid/x.css%27;";',
                    '@import "data:text/css,p%7Bbackground:url(missing.png)%7D";'):
            with self.subTest(css=css), self.assertRaises(ValueError):
                audit_html(self.css(css), self.base)

    def test_html_embedded_dependencies_fail_when_missing_or_remote(self):
        templates = ('<img src="{}">', '<script src="{}"></script>',
                     '<link rel="stylesheet" href="{}">', '<video poster="{}"></video>',
                     '<audio src="{}"></audio>', '<source src="{}">',
                     '<object data="{}"></object>', '<embed src="{}">',
                     '<svg><image href="{}"/></svg>', '<svg><use xlink:href="{}"/></svg>',
                     '<link rel="preload" as="font" href="{}">')
        for template in templates:
            for url, message in (("missing.bin", "Missing packaged dependency"),
                                 ("//example.invalid/asset", "Remote dependency")):
                with self.subTest(template=template, url=url), self.assertRaisesRegex(ValueError, message):
                    audit_html(template.format(url), self.base)
        self.write("image.png")
        audit_html('<img src="image.png?rev=1#view"><script src="data:text/javascript,void(0)"></script>', self.base)

    def test_srcset_candidates_are_audited_without_splitting_data_urls(self):
        self.write("image.png")
        audit_html('<img srcset="data:image/png;base64,eA== 1x, image.png 2x">', self.base)
        for attr in ("srcset", "imagesrcset"):
            for url in ("missing.png", "https://example.invalid/image.png"):
                with self.subTest(attr=attr, url=url), self.assertRaises(ValueError):
                    audit_html(f'<img {attr}="image.png 1x, {url} 2x">', self.base)

    def test_dependencies_cannot_escape_the_packaged_tree(self):
        outside = self.base.parent / "outside.otf"
        outside.write_text("outside")
        (self.base / "alias.otf").symlink_to(outside)
        for url in ("../outside.otf", "%2e%2e/outside.otf", str(outside), "alias.otf"):
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, "outside packaged directory"):
                audit_html(self.css(f'@font-face{{src:url("{url}")}}'), self.base)

    def test_malformed_url_and_html_base_fail_closed(self):
        for css in ('p{background:url("unterminated)}', 'p{background:url(missing.png}'):
            with self.subTest(css=css), self.assertRaisesRegex(ValueError, "Malformed CSS"):
                audit_html(self.css(css), self.base)
        with self.assertRaisesRegex(ValueError, "base URLs"):
            audit_html('<base href="https://example.invalid/">', self.base)


def font_fixture(root):
    fonts = root / "export-assets/fonts"
    fonts.mkdir(parents=True)
    files = {}
    for name in ("regular.otf", "bold.otf", "mono.otf", "emoji.ttf", "OFL.txt", "OFL-Emoji.txt"):
        data = ("fixture: " + name).encode()
        (fonts / name).write_bytes(data)
        files[name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
    (fonts / "FONT-SOURCES.json").write_text(json.dumps({"license": "SIL OFL 1.1", "files": files}))
    return fonts


class FontManifestTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.fonts = font_fixture(self.root)

    def test_complete_manifest_passes(self):
        result = validate_fonts(self.root)
        self.assertEqual(result["files_verified"], 6)
        self.assertIn("emoji.ttf", result["verified_entries"])

    def test_missing_font_or_license_fails(self):
        for name in ("bold.otf", "OFL-Emoji.txt"):
            path = self.fonts / name
            original = path.read_bytes()
            path.unlink()
            with self.subTest(name=name), self.assertRaises(FileNotFoundError):
                validate_fonts(self.root)
            path.write_bytes(original)

    def test_hash_and_size_mismatches_fail(self):
        path = self.fonts / "regular.otf"
        original = path.read_bytes()
        for changed in (b"x" * len(original), original + b"extra"):
            path.write_bytes(changed)
            with self.subTest(size=len(changed)), self.assertRaisesRegex(ValueError, "hash mismatch"):
                validate_fonts(self.root)

    def test_manifest_size_is_checked_independently_of_hash(self):
        path = self.fonts / "FONT-SOURCES.json"
        manifest = json.loads(path.read_text())
        manifest["files"]["regular.otf"]["bytes"] += 1
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            validate_fonts(self.root)

    def test_missing_manifest_fails(self):
        (self.fonts / "FONT-SOURCES.json").unlink()
        with self.assertRaises(FileNotFoundError):
            validate_fonts(self.root)

    def test_unsafe_manifest_path_fails(self):
        path = self.fonts / "FONT-SOURCES.json"
        manifest = json.loads(path.read_text())
        manifest["files"]["../outside.otf"] = manifest["files"].pop("regular.otf")
        path.write_text(json.dumps(manifest))
        with self.assertRaises(ValueError):
            validate_fonts(self.root)

    def test_source_packaging_uses_the_shared_validator(self):
        with patch("package_source.validate_fonts", return_value={"shared": True}) as validator:
            report = validate_licenses_and_fonts(ROOT)
        validator.assert_called_once_with(ROOT)
        self.assertEqual(report["fonts"], {"shared": True})


@unittest.skipIf(exporter is None, EXPORT_SKIP)
class ExportIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.fonts = font_fixture(self.root)
        assets = self.root / "export-assets"
        (assets / "screen.css").write_text('@font-face{src:url("fonts/bold.otf")}')
        (assets / "offline.js").write_text("// fixture")
        self.docs = self.root / "docs"
        self.docs.mkdir()
        (self.docs / "SUMMARY.md").write_text('- [Home](README.md)\n- [Other](other.md)\n')
        (self.docs / "README.md").write_text('# Home\n\n[Other](other.md#target)\n'
                                            '[External](https://example.invalid/README.md)\n'
                                            '[Protocol relative](//example.invalid/README.md)\n')
        (self.docs / "other.md").write_text('# Other\n\n## Target <a id="target"></a>\n')
        self.output = self.root / "out"

    def build(self):
        with patch.object(exporter, "ROOT", self.root):
            return exporter.build(self.docs, self.output, with_epub=False)

    def test_build_rewrites_local_links_and_preserves_external_links_in_both_outputs(self):
        report = self.build()
        self.assertEqual(report["html"]["chapters"], 2)
        for path in (self.output / "html/index.html", self.output / "book-export.html"):
            soup = exporter.BeautifulSoup(path.read_text(), "html.parser")
            links = {a.get_text(): a["href"] for a in soup.select("a[href]")}
            self.assertTrue(links["Other"].startswith("#page-other-"))
            self.assertEqual(links["External"], "https://example.invalid/README.md")
            self.assertEqual(links["Protocol relative"], "//example.invalid/README.md")

    def test_export_rejects_incomplete_or_corrupt_font_manifest_before_output(self):
        for name in ("bold.otf", "OFL-Emoji.txt"):
            path = self.fonts / name
            original = path.read_bytes()
            for changed in (None, b"x" * len(original)):
                if changed is None:
                    path.unlink()
                else:
                    path.write_bytes(changed)
                with self.subTest(name=name, changed=changed), self.assertRaises((ValueError, FileNotFoundError)):
                    self.build()
                self.assertFalse(self.output.exists())
                path.write_bytes(original)

    def test_build_rejects_missing_css_font_and_remote_import(self):
        for css in ('@font-face{src:url(fonts/unlisted.otf)}', '@import "//example.invalid/theme.css";'):
            (self.root / "export-assets/screen.css").write_text(css)
            with self.subTest(css=css), self.assertRaises(ValueError):
                self.build()

    def test_rewrite_rejects_missing_summary_page_and_unknown_local_anchor(self):
        for url, message in (("unlisted.md", "Page missing from SUMMARY"),
                             ("other.md#missing", "Unknown anchor")):
            (self.docs / "README.md").write_text(f'# Home\n\n[Broken]({url})\n')
            with self.subTest(url=url), self.assertRaisesRegex(ValueError, message):
                self.build()


if __name__ == "__main__":
    unittest.main()
