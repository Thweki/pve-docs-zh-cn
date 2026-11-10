# 22.2. 输出格式选项 `[FORMAT_OPTIONS]` <a href="#output_format_options_span_class_monospaced_format_options_span" id="output_format_options_span_class_monospaced_format_options_span"></a>

可以使用 `--output-format` 参数指定输出格式。默认格式 *text* 使用 ASCII 字符画为表格绘制美观的边框。此外，还会将某些值转换为易于阅读的文本，例如：

- Unix 纪元时间显示为 ISO 8601 日期字符串。
- 时长显示为周/天/小时/分钟/秒的数量，即 `1d 5h`。
- 字节大小值包含单位（`B`、`KiB`、`MiB`、`GiB`、`TiB`、`PiB`）。
- 小数显示为百分比，即 1.0 显示为 100%。

还可以使用选项 `--quiet` 完全禁止输出。

**`--human-readable` `<boolean>`（*默认值 \=* `1`）**

调用输出渲染函数，生成易于阅读的文本。

**`--noborder` `<boolean>`（*默认值 \=* `0`）**

不绘制边框（适用于 *text* 格式）。

**`--noheader` `<boolean>`（*默认值 \=* `0`）**

不显示列标题（适用于 *text* 格式）。

**`--output-format` `<json | json-pretty | text | yaml>`（*默认值 \=* `text`）**

输出格式。

**`--quiet` `<boolean>`**

禁止打印结果。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
