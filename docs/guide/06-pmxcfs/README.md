# 6\. Proxmox Cluster File System (pmxcfs) <a href="#chapter_pmxcfs" id="chapter_pmxcfs"></a>

Proxmox 集群文件系统（“pmxcfs”）是一种数据库驱动的文件系统，用于存储配置文件，并通过 `corosync` 实时复制到所有集群节点。我们使用它来存储所有与 Proxmox VE 相关的配置文件。

尽管文件系统将所有数据存储在磁盘上的持久化数据库中，但 RAM 中也保留了一份数据副本。这限制了其最大容量，目前为 128 MiB。但这仍足以存储数千台虚拟机的配置。

该系统具有以下优点：

- 将所有配置实时无缝复制到所有节点
- 提供强一致性检查，避免 VM ID 重复
- 节点失去仲裁时为只读状态
- 自动将 corosync 集群配置更新到所有节点
- 包含分布式锁机制

## 本章内容

- [6.1. POSIX Compatibility](01-posix-compatibility.md)
- [6.2. File Access Rights](02-file-access-rights.md)
- [6.3. Technology](03-technology.md)
- [6.4. File System Layout](04-file-system-layout.md)
- [6.5. Recovery](05-recovery.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
