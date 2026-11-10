# qmrestore(1)

## NAME <a href="#_name" id="_name"></a>

qmrestore \- Restore QemuServer `vzdump` Backups

## SYNOPSIS <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_qmrestore_help"></a>



**qmrestore** `help`

<a id="cli_qmrestore"></a>



**qmrestore** `<archive> <vmid>` `[OPTIONS]`

Restore QemuServer vzdump backups.

**`<archive>`: `<string>`**

The backup file. You can pass *\-* to read from standard input.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--bwlimit` `<number> (0 - N)`**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--force` `<boolean>`**

Allow to overwrite existing VM.

**`--ha-managed` `<boolean>` (*default \=* `0`)**

Add the VM as a HA resource after it was restored.

**`--live-restore` `<boolean>`**

Start the VM immediately from the backup and restore in background. PBS only.

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--start` `<boolean>` (*default \=* `0`)**

Start VM after it was restored successfully.

**`--storage` `<storage ID>`**

Default storage.

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

## DESCRIPTION <a href="#_description" id="_description"></a>

Restore the QemuServer vzdump backup `archive` to virtual machine `vmid`. Volumes are allocated on the original storage if there is no `storage` specified.

## Copyright and Disclaimer <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/qmrestore.1.html) · 版本 9.2.13 · 非官方中文翻译。
