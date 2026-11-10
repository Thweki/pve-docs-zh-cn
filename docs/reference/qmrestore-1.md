# qmrestore(1)

## 名称 <a href="#name" id="name"></a>

qmrestore \- 恢复 QemuServer `vzdump` 备份

## 概要 <a href="#synopsis" id="synopsis"></a>

### **qmrestore** `help` <a href="#cli_qmrestore_help" id="cli_qmrestore_help"></a>

### **qmrestore** `<archive> <vmid>` `[OPTIONS]` <a href="#cli_qmrestore" id="cli_qmrestore"></a>

恢复 QemuServer vzdump 备份。

**`<archive>`: `<string>`**

备份文件。可以传入 *\-* 以从标准输入读取。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--bwlimit` `<number> (0 - N)`**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--force` `<boolean>`**

允许覆盖现有虚拟机。

**`--ha-managed` `<boolean>`（*默认 \=* `0`）**

恢复虚拟机后，将其添加为 HA 资源。

**`--live-restore` `<boolean>`**

立即从备份启动虚拟机，并在后台恢复。仅适用于 PBS。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--start` `<boolean>`（*默认 \=* `0`）**

成功恢复后启动虚拟机。

**`--storage` `<storage ID>`**

默认存储。

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

## 描述 <a href="#description" id="description"></a>

将 QemuServer vzdump 备份 `archive` 恢复到虚拟机 `vmid`。如果未指定 `storage`，则在原始存储上分配卷。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/qmrestore.1.html) · 版本 9.2.13 · 非官方中文翻译。
