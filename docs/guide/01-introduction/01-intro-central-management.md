# 1.1. 集中管理 <a href="#intro_central_management" id="intro_central_management"></a>

虽然许多人从单个节点开始，但 Proxmox VE 可以横向扩展到由大量节点组成的集群。集群栈已完全集成，并随默认安装一起提供。

**独特的多主节点设计**

Proxmox VE 集群中的每个节点都可以执行所有管理任务。不存在单点故障的中央管理服务器——任何节点都可以管理整个集群。即使个别节点暂时不可用，这种多主节点架构也能使集群保持可管理状态。

**Proxmox 集群文件系统（pmxcfs）**

Proxmox VE 使用 Proxmox 集群文件系统（pmxcfs），这是一种用于存储配置文件的数据库驱动文件系统。它可以存储数千台虚拟机的配置。Corosync 将这些文件实时复制到所有集群节点。该文件系统将所有数据存储在磁盘上的持久化数据库中，同时在 RAM 中保留一份副本，最大存储容量为 128 MiB——对于数千台 VM 而言绰绰有余。

Proxmox VE 是唯一使用这种集群文件系统的虚拟化平台。

**基于 Web 的管理界面**

Proxmox VE 简单易用。其内置的基于 Web 的界面构建于 ExtJS JavaScript 框架之上，可清晰概览所有 KVM 客户机和 Linux 容器，并提供对所有集群资源的完全控制。您可以通过 GUI 管理 VM、容器、存储和网络，包括查看每个节点的历史记录和 syslog、运行备份或恢复任务、在线迁移以及 HA 触发的活动。无需安装单独的管理工具或额外的管理节点。

**命令行**

对于偏爱 Unix shell 或 Windows PowerShell 便捷体验的高级用户，Proxmox VE 提供了命令行界面，用于管理虚拟环境的所有组件。此命令行界面具有智能 Tab 补全功能，并以 man 手册页的形式提供完整文档。

**REST API**

Proxmox VE 使用 RESTful API，并以 JSON 作为主要数据格式。整个 API 均使用 JSON Schema 进行形式化定义，使自定义托管环境等第三方管理工具能够快速、轻松地完成集成。

**基于角色的管理**

通过基于角色的用户和权限管理，您可以为所有对象（如虚拟机、存储和节点）定义精细的访问权限。每项权限都按照访问控制列表模型，指定特定路径上的一个主体（用户或组）和一个角色（权限集合）。

**认证域**

Proxmox VE 支持多种认证来源，包括 Microsoft Active Directory、LDAP、Linux PAM 标准认证以及内置的 Proxmox VE 认证服务器。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
