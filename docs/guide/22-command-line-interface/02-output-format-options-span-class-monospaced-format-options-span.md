# 22.2. Output format options `[FORMAT_OPTIONS]` <a href="#_output_format_options_span_class_monospaced_format_options_span" id="_output_format_options_span_class_monospaced_format_options_span"></a>

It is possible to specify the output format using the `--output-format` parameter. The default format *text* uses ASCII-art to draw nice borders around tables. It additionally transforms some values into human-readable text, for example:

- Unix epoch is displayed as ISO 8601 date string.
- Durations are displayed as week/day/hour/minute/second count, i.e `1d 5h`.
- Byte sizes value include units (`B`, `KiB`, `MiB`, `GiB`, `TiB`, `PiB`).
- Fractions are display as percentage, i.e. 1.0 is displayed as 100%.

You can also completely suppress output using option `--quiet`.

**`--human-readable` `<boolean>` (*default \=* `1`)**

Call output rendering functions to produce human readable text.

**`--noborder` `<boolean>` (*default \=* `0`)**

Do not draw borders (for *text* format).

**`--noheader` `<boolean>` (*default \=* `0`)**

Do not show column headers (for *text* format).

**`--output-format` `<json | json-pretty | text | yaml>` (*default \=* `text`)**

Output format.

**`--quiet` `<boolean>`**

Suppress printing results.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
