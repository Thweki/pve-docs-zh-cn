# pvesubscription(1)

## 名称 <a href="#_name" id="_name"></a>

pvesubscription \- Proxmox VE Subscription Manager

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pvesubscription"></a>



**pvesubscription** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvesubscription_delete"></a>



**pvesubscription delete**

Delete subscription key of this node.

<a id="cli_pvesubscription_get"></a>



**pvesubscription get**

Read subscription info.

<a id="cli_pvesubscription_help"></a>



**pvesubscription help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvesubscription_set"></a>



**pvesubscription set** `<key>`

Set subscription key.

**`<key>`: `\s*pve([1248])([cbsp])-(arm-)?[0-9a-f]{10}\s*`**

Proxmox VE subscription key

<a id="cli_pvesubscription_set-offline-key"></a>



**pvesubscription set-offline-key** `<data>`

Internal use only! To set an offline key, use the package proxmox-offline-mirror-helper instead.

**`<data>`: `<string>`**

A signed subscription info blob

<a id="cli_pvesubscription_update"></a>



**pvesubscription update** `[OPTIONS]`

Update subscription info.

**`--force` `<boolean>`（*默认 \=* `0`）**

Always connect to server, even if local cache is still valid.

## 描述 <a href="#_description" id="_description"></a>

This tool is used to handle Proxmox VE subscriptions.

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvesubscription.1.html) · 版本 9.2.13 · 非官方中文翻译。
