# 1.7. 超融合基础设施 <a href="#chapter_hyper_converged_infrastructure" id="chapter_hyper_converged_infrastructure"></a>

Proxmox VE 是一个紧密集成计算、存储和网络资源的虚拟化平台，可管理高可用性集群、备份/恢复以及灾难恢复。所有组件均由软件定义，并且彼此兼容。

因此，可以通过集中式 Web 管理界面像管理单个系统一样管理这些组件。这些功能使 Proxmox VE 成为部署和管理开源[超融合基础设施](https://en.wikipedia.org/wiki/Hyper-converged_infrastructure)的理想选择。

## 1.7.1. 使用 Proxmox VE 构建超融合基础设施（HCI）的优势 <a href="#_benefits_of_a_hyper_converged_infrastructure_hci_with_proxmox_ve" id="_benefits_of_a_hyper_converged_infrastructure_hci_with_proxmox_ve"></a>

超融合基础设施（HCI）特别适用于基础设施需求高但管理预算有限的部署、远程和分支机构环境等分布式部署，以及虚拟私有云和公有云。

HCI 具有以下优势：

- 可扩展性：无缝扩展计算、网络和存储设备（即快速且彼此独立地扩展服务器和存储）。
- 低成本：Proxmox VE 是开源软件，集成了您所需的所有组件，如计算、存储、网络、备份和管理中心。它可以取代昂贵的计算/存储基础设施。
- 数据保护与效率：集成了备份和灾难恢复等服务。
- 简单性：配置简便，管理集中。
- 开源：无供应商锁定。

## 1.7.2. 超融合基础设施：存储 <a href="#_hyper_converged_infrastructure_storage" id="_hyper_converged_infrastructure_storage"></a>

Proxmox VE 紧密集成了部署超融合存储基础设施的支持。例如，您可以仅通过 Web 界面部署和管理以下两种存储技术：

- **Ceph**：一种自愈、自管理的共享存储系统，可靠且高度可扩展。了解[如何在 Proxmox VE 节点上管理 Ceph 服务](../08-pveceph/README.md)
- **ZFS**：集文件系统与逻辑卷管理器于一体，可全面防止数据损坏，支持多种 RAID 模式以及快速、低成本的快照等功能。了解[如何在 Proxmox VE 节点上发挥 ZFS 的强大功能](../03-system-administration/09-chapter-zfs.md)。

除上述技术外，Proxmox VE 还支持集成多种其他存储技术。您可以在[“存储管理器”一章](../07-storage/README.md)中了解这些技术。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
