# pvesh(1)

## 名称 <a href="#_name" id="_name"></a>

pvesh \- Shell interface for the Proxmox VE API

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pvesh"></a>



**pvesh** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvesh_create"></a>



**pvesh create** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API POST on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_delete"></a>



**pvesh delete** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API DELETE on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_get"></a>



**pvesh get** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API GET on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_help"></a>



**pvesh help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvesh_ls"></a>



**pvesh ls** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

List child objects on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_set"></a>



**pvesh set** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API PUT on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_usage"></a>



**pvesh usage** `<api_path>` `[OPTIONS]`

print API usage information for \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--command` `<create | delete | get | set>`**

API command.

**`--returns` `<boolean>`**

Including schema for returned data.

**`--verbose` `<boolean>`**

详细输出格式。

## 描述 <a href="#_description" id="_description"></a>

The Proxmox VE management tool (`pvesh`) allows to directly invoke API function, without using the REST/HTTPS server.

{% hint style="info" %}
Only *root* is allowed to do that.
{% endhint %}

## FORMAT\_OPTIONS <a href="#_format_options" id="_format_options"></a>

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

## EXAMPLES <a href="#_examples" id="_examples"></a>

Get the list of nodes in my cluster

```text
# pvesh get /nodes
```

Get a list of available options for the datacenter

```text
# pvesh usage cluster/options -v
```

Set the HTMl5 NoVNC console as the default console for the datacenter

```text
# pvesh set cluster/options -console html5
```

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvesh.1.html) · 版本 9.2.13 · 非官方中文翻译。
