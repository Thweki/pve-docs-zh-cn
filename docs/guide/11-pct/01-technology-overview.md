# 11.1. Technology Overview <a href="#_technology_overview" id="_technology_overview"></a>

- LXC（[https://linuxcontainers.org/](https://linuxcontainers.org/)）
- 集成到 Proxmox VE 图形化 Web 用户界面（GUI）中
- Easy to use command-line tool `pct`
- 通过 Proxmox VE REST API 访问
- *lxcfs* to provide containerized /proc file system
- 控制组（*cgroups*），用于资源隔离和限制
- *AppArmor* and *seccomp* to improve security
- 现代 Linux 内核
- Image based deployment ([templates](02-pct-supported-distributions.md))
- Uses Proxmox VE [storage library](../07-storage/README.md)
- 从宿主机配置容器（网络、DNS、存储等）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
