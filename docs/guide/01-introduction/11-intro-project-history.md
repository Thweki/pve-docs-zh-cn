# 1.11. 项目历史 <a href="#intro_project_history" id="intro_project_history"></a>

该项目于 2007 年启动，随后于 2008 年发布了第一个稳定版本。当时，它使用 OpenVZ 实现容器，使用 KVM 实现虚拟机。集群功能有限，用户界面也很简单（由服务器生成的网页）。

该项目使用[Corosync](https://corosync.github.io/corosync/)集群堆栈快速开发了新功能，而 Proxmox 集群文件系统（pmxcfs）的引入是向前迈出的一大步，因为它向用户完全隐藏了集群的复杂性。管理一个包含 16 个节点的集群与管理单个节点一样简单。

REST API 的引入及其使用 JSON Schema 编写的完整声明式规范，使其他人能够将 Proxmox VE 集成到自己的基础设施中，也让提供附加服务变得容易。

REST API 还使使用 JavaScript 编写的现代客户端单页应用程序取代原有用户界面成为可能。旧的基于 Java 的 VNC 控制台代码被[noVNC](https://novnc.com/info.html)取代，因此只需 Web 浏览器即可管理虚拟机。

对各种存储类型的支持是另一项重大成就。值得一提的是，Proxmox VE 于 2014 年成为第一个默认附带[ZFS on Linux](https://zfsonlinux.org/)的发行版。另一个里程碑是能够在虚拟化管理程序节点上运行和管理[Ceph](https://ceph.com/)存储。这种部署方式极具成本效益。

项目启动时，Proxmox 是首批为 KVM 提供商业支持的公司之一。KVM 项目本身不断发展，现已成为广泛使用的虚拟化管理程序。每个版本都会带来新功能。由 Proxmox 开发的 KVM 在线备份功能使在任何存储类型上创建快照备份成为可能。

4.0 版本最显著的变化是从 OpenVZ 转向[LXC](https://linuxcontainers.org/)。容器现已深度集成，可以使用与虚拟机相同的存储和网络功能。与此同时，还引入了易于使用的[高可用性（HA）管理器](../15-ha-manager/README.md)，简化了高可用性部署的配置和管理。

在 Proxmox VE 5 的开发过程中，引入了异步[存储复制](../09-pvesr/README.md)以及使用 ACME/Let’s Encrypt 的自动化[证书管理](../03-system-administration/12-sysadmin-certificate-management.md)等诸多功能。

[软件定义网络（SDN）](../12-pvesdn/README.md)堆栈是与社区合作开发的。它在 6.2 版本中作为实验性功能集成到 Web 界面中，简化了复杂网络配置的管理。自 8.1 版本起，SDN 集成已获得全面支持，并默认安装。

2020 年，一个使用 Rust 编程语言编写的新项目[Proxmox Backup Server](https://www.proxmox.com/en/products/proxmox-backup-server/overview)发布。Proxmox Backup Server 与 Proxmox VE 深度集成，通过实现增量备份、去重等功能，显著增强了备份能力。

另一个新工具[Proxmox Offline Mirror](https://pom.proxmox.com)于 2022 年发布，使无法连接公共互联网的系统也能使用订阅。

2023 年，Web 界面引入了备受期待的深色主题。同年晚些时候，8.0 版集成了对 Ceph 企业仓库的访问。任何 Proxmox VE 订阅均包含对最稳定 Ceph 仓库的访问权限。

8.2 版引入了适用于官方 [ISO 安装程序](../02-installation/03-installation-installer.md) 的自动化无人值守安装，显著简化了 Proxmox VE 的大规模部署。

[导入向导](../10-virtual-machines/07-qm-import-virtual-machines.md)同样在 8.2 版中引入，用户可以通过它轻松高效地将客户机直接从 VMware ESXi 等其他虚拟机监控程序迁移过来 [\[1\]](#note-52264c29-1)。此外，现在还可以在 Web 界面中直接从基于文件的存储导入开放虚拟化格式（OVF/OVA）归档文件。

## 注释

### 注释 1 <a href="#note-52264c29-1" id="note-52264c29-1"></a>

迁移到 Proxmox VE [https://pve.proxmox.com/wiki/Migrate\_to\_Proxmox\_VE](https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
