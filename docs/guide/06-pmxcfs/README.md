# 6. Proxmox Cluster File System (pmxcfs) <a href="#chapter_pmxcfs" id="chapter_pmxcfs"></a>

The Proxmox Cluster file system (“pmxcfs”) is a database-driven file system for storing configuration files, replicated in real time to all cluster nodes using `corosync`. We use this to store all Proxmox VE related configuration files.

Although the file system stores all data inside a persistent database on disk, a copy of the data resides in RAM. This imposes restrictions on the maximum size, which is currently 128 MiB. This is still enough to store the configuration of several thousand virtual machines.

This system provides the following advantages:

- Seamless replication of all configuration to all nodes in real time
- Provides strong consistency checks to avoid duplicate VM IDs
- Read-only when a node loses quorum
- Automatic updates of the corosync cluster configuration to all nodes
- Includes a distributed locking mechanism

## 本章内容

- [6.1. POSIX Compatibility](01-posix-compatibility.md)
- [6.2. File Access Rights](02-file-access-rights.md)
- [6.3. Technology](03-technology.md)
- [6.4. File System Layout](04-file-system-layout.md)
- [6.5. Recovery](05-recovery.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
