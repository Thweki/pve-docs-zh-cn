# 16.13. Examples <a href="#_examples_10" id="_examples_10"></a>

Simply dump guest 777 \- no snapshot, just archive the guest private area and configuration files to the default dump directory (usually `/var/lib/vz/dump/`).

```text
# vzdump 777
```

Use rsync and suspend/resume to create a snapshot (minimal downtime).

```text
# vzdump 777 --mode suspend
```

Backup all guest systems and send notification mails to root and admin. Due to `mailto` being set and `notification-mode` being set to `auto` by default, the notification mails are sent via the system’s `sendmail` command instead of the notification system.

```text
# vzdump --all --mode suspend --mailto root --mailto admin
```

Use snapshot mode (no downtime) and non-default dump directory.

```text
# vzdump 777 --dumpdir /mnt/backup --mode snapshot
```

Backup more than one guest (selectively)

```text
# vzdump 101 102 103 --mailto root
```

Backup all guests excluding 101 and 102

```text
# vzdump --mode suspend --exclude 101,102
```

Restore a container to a new CT 600

```text
# pct restore 600 /mnt/backup/vzdump-lxc-777.tar
```

Restore a QemuServer VM to VM 601

```text
# qmrestore /mnt/backup/vzdump-qemu-888.vma 601
```

Clone an existing container 101 to a new container 300 with a 4GB root file system, using pipes

```text
# vzdump 101 --stdout | pct restore --rootfs 4 300 -
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
