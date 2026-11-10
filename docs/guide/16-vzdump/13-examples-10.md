# 16.13. 示例 <a href="#examples_10" id="examples_10"></a>

仅转储客户机 777：不创建快照，只将客户机的私有区域和配置文件归档到默认转储目录（通常为 `/var/lib/vz/dump/`）。

```text
# vzdump 777
```

使用 rsync 和挂起/恢复创建快照（停机时间最短）。

```text
# vzdump 777 --mode suspend
```

备份所有客户机系统，并向 root 和 admin 发送通知邮件。由于设置了 `mailto`，且 `notification-mode` 默认设置为 `auto`，通知邮件通过系统的 `sendmail` 命令发送，而不是通过通知系统发送。

```text
# vzdump --all --mode suspend --mailto root --mailto admin
```

使用快照模式（无需停机）和非默认的转储目录。

```text
# vzdump 777 --dumpdir /mnt/backup --mode snapshot
```

备份多个客户机（选择性备份）

```text
# vzdump 101 102 103 --mailto root
```

备份除 101 和 102 以外的所有客户机

```text
# vzdump --mode suspend --exclude 101,102
```

将容器恢复为新的 CT 600

```text
# pct restore 600 /mnt/backup/vzdump-lxc-777.tar
```

将 QemuServer 虚拟机恢复为 VM 601

```text
# qmrestore /mnt/backup/vzdump-qemu-888.vma 601
```

使用管道将现有容器 101 克隆为具有 4GB 根文件系统的新容器 300

```text
# vzdump 101 --stdout | pct restore --rootfs 4 300 -
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
