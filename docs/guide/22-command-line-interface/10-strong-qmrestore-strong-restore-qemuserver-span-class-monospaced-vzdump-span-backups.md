# 22.10. **qmrestore** \- Restore QemuServer `vzdump` Backups <a href="#_strong_qmrestore_strong_restore_qemuserver_span_class_monospaced_vzdump_span_backups" id="_strong_qmrestore_strong_restore_qemuserver_span_class_monospaced_vzdump_span_backups"></a>

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

**`--ha-managed` `<boolean>`（*默认 \=* `0`）**

Add the VM as a HA resource after it was restored.

**`--live-restore` `<boolean>`**

Start the VM immediately from the backup and restore in background. PBS only.

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--start` `<boolean>`（*默认 \=* `0`）**

Start VM after it was restored successfully.

**`--storage` `<storage ID>`**

Default storage.

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
