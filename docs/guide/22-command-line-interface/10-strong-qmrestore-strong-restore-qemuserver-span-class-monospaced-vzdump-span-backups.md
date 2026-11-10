# 22.10. **qmrestore** \- 恢复 QemuServer `vzdump` 备份 <a href="#strong_qmrestore_strong_restore_qemuserver_span_class_monospaced_vzdump_span_backups" id="strong_qmrestore_strong_restore_qemuserver_span_class_monospaced_vzdump_span_backups"></a>

## **qmrestore** `help` <a href="#cli_qmrestore_help" id="cli_qmrestore_help"></a>

## **qmrestore** `<archive> <vmid>` `[OPTIONS]` <a href="#cli_qmrestore" id="cli_qmrestore"></a>

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

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
