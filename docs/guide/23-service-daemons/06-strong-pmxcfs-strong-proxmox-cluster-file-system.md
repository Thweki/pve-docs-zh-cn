# 23.6. **pmxcfs** \- Proxmox 集群文件系统 <a href="#strong_pmxcfs_strong_proxmox_cluster_file_system" id="strong_pmxcfs_strong_proxmox_cluster_file_system"></a>

**pmxcfs** `[OPTIONS]`

帮助选项：

**`-h`, `--help`**

显示帮助选项

应用程序选项：

**`-d`, `--debug`**

启用调试消息

**`-f`, `--foreground`**

不要将服务器守护进程化

**`-l`, `--local`**

强制使用本地模式（忽略 corosync.conf，强制仲裁）

通常使用 systemd 工具集启动和管理此服务。该服务称为 *pve-cluster*。

```text
systemctl start pve-cluster
```

```text
systemctl stop pve-cluster
```

```text
systemctl status pve-cluster
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
