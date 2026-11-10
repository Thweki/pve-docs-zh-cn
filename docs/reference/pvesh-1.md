# pvesh(1)

## 名称 <a href="#name" id="name"></a>

pvesh \- Proxmox VE API 的 Shell 接口

## 概要 <a href="#synopsis" id="synopsis"></a>

### <strong>pvesh</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesh" id="cli_pvesh"></a>

### <strong>pvesh create</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_create" id="cli_pvesh_create"></a>

对 \<api\_path\> 调用 API POST。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh delete</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_delete" id="cli_pvesh_delete"></a>

对 \<api\_path\> 调用 API DELETE。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh get</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_get" id="cli_pvesh_get"></a>

对 \<api\_path\> 调用 API GET。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh help</strong> `[OPTIONS]` <a href="#cli_pvesh_help" id="cli_pvesh_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvesh ls</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_ls" id="cli_pvesh_ls"></a>

列出 \<api\_path\> 下的子对象。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh set</strong> `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_set" id="cli_pvesh_set"></a>

对 \<api\_path\> 调用 API PUT。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

### <strong>pvesh usage</strong> `<api_path>` `[OPTIONS]` <a href="#cli_pvesh_usage" id="cli_pvesh_usage"></a>

打印 \<api\_path\> 的 API 使用信息。

**`<api_path>`: `<string>`**

API 路径。

**`--command` `<create | delete | get | set>`**

API 命令。

**`--returns` `<boolean>`**

包含返回数据的模式定义。

**`--verbose` `<boolean>`**

详细输出格式。

## 描述 <a href="#description" id="description"></a>

Proxmox VE 管理工具（`pvesh`）允许直接调用 API 函数，无需使用 REST/HTTPS 服务器。

{% hint style="info" %}
只有 <em>root</em> 可以这样做。
{% endhint %}

## FORMAT\_OPTIONS <a href="#format_options" id="format_options"></a>

可以使用 `--output-format` 参数指定输出格式。默认格式 <em>text</em> 使用 ASCII 字符画为表格绘制美观的边框。此外，还会将某些值转换为易于阅读的文本，例如：

- Unix 纪元时间显示为 ISO 8601 日期字符串。
- 时长显示为周/天/小时/分钟/秒的数量，即 `1d 5h`。
- 字节大小值包含单位（`B`、`KiB`、`MiB`、`GiB`、`TiB`、`PiB`）。
- 小数显示为百分比，即 1.0 显示为 100%。

还可以使用选项 `--quiet` 完全禁止输出。

**`--human-readable` `<boolean>`（<em>默认值 \=</em> `1`）**

调用输出渲染函数，生成易于阅读的文本。

**`--noborder` `<boolean>`（<em>默认值 \=</em> `0`）**

不绘制边框（适用于 <em>text</em> 格式）。

**`--noheader` `<boolean>`（<em>默认值 \=</em> `0`）**

不显示列标题（适用于 <em>text</em> 格式）。

**`--output-format` `<json | json-pretty | text | yaml>`（<em>默认值 \=</em> `text`）**

输出格式。

**`--quiet` `<boolean>`**

禁止打印结果。

## 示例 <a href="#examples" id="examples"></a>

获取我的集群中的节点列表

```text
# pvesh get /nodes
```

获取数据中心的可用选项列表

```text
# pvesh usage cluster/options -v
```

将 HTMl5 NoVNC 控制台设置为数据中心的默认控制台

```text
# pvesh set cluster/options -console html5
```

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvesh.1.html) · 版本 9.2.13 · 非官方中文翻译。
