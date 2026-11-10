# 23.6. **pmxcfs** - Proxmox Cluster File System <a href="#_strong_pmxcfs_strong_proxmox_cluster_file_system" id="_strong_pmxcfs_strong_proxmox_cluster_file_system"></a>

**pmxcfs** `[OPTIONS]`

帮助选项：

**`-h`, `--help`**

显示帮助选项

应用程序选项：

**`-d`, `--debug`**

Turn on debug messages

**`-f`, `--foreground`**

Do not daemonize server

**`-l`, `--local`**

Force local mode (ignore corosync.conf, force quorum)

This service is usually started and managed using systemd toolset. The service is called *pve-cluster*.

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
