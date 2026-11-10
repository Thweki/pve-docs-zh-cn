# 11.1. 技术概述 <a href="#technology_overview" id="technology_overview"></a>

- LXC（[https://linuxcontainers.org/](https://linuxcontainers.org/)）
- 集成到 Proxmox VE 图形化 Web 用户界面（GUI）中
- 易于使用的命令行工具 `pct`
- 通过 Proxmox VE REST API 访问
- *lxcfs* 用于提供容器化的 /proc 文件系统
- 控制组（*cgroups*），用于资源隔离和限制
- *AppArmor* 和 *seccomp*，用于提高安全性
- 现代 Linux 内核
- 基于镜像的部署（[模板](02-pct-supported-distributions.md)）
- 使用 Proxmox VE [存储库](../07-storage/README.md)
- 从宿主机配置容器（网络、DNS、存储等）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
