# 5\. 集群管理器 <a href="#chapter_pvecm" id="chapter_pvecm"></a>

Proxmox VE 集群管理器 `pvecm` 是一个用于创建物理服务器组的工具。这样的组称为**集群**。我们使用 [Corosync Cluster Engine](http://www.corosync.org) 实现可靠的组通信。集群中的节点数量没有明确限制。在实践中，实际可支持的节点数量可能受宿主机和网络性能限制。目前（2021 年），已有报告称，使用高端企业级硬件的集群在生产环境中运行了超过 50 个节点。

`pvecm` 可用于创建新集群、将节点加入集群、离开集群、获取状态信息以及执行各种其他集群相关任务。**P**rox**m**o**x** **C**luster **F**ile **S**ystem（“pmxcfs”）用于以透明方式将集群配置分发到所有集群节点。

将节点组成集群具有以下优点：

- 集中式、基于 Web 的管理
- 多主集群：每个节点都可以执行所有管理任务
- 使用 `pmxcfs`（一种数据库驱动的文件系统）存储配置文件，并通过 `corosync` 在所有节点上实时复制
- 在物理宿主机之间轻松迁移虚拟机和容器
- 快速部署
- 集群范围的服务，如防火墙和 HA

## 本章内容

- [5.1. 要求](01-pvecm-cluster-requirements.md)
- [5.2. 准备节点](02-preparing-nodes.md)
- [5.3. 创建集群](03-pvecm-create-cluster.md)
- [5.4. 向集群添加节点](04-pvecm-join-node-to-cluster.md)
- [5.5. 移除集群节点](05-pvecm-remove-node.md)
- [5.6. 在不重新安装的情况下分离节点](06-pvecm-separate-node-without-reinstall.md)
- [5.7. 仲裁](07-quorum.md)
- [5.8. 集群网络](08-pvecm-cluster-network.md)
- [5.9. Corosync 冗余](09-pvecm-redundancy.md)
- [5.10. SSH 在 Proxmox VE 集群中的作用](10-role-of-ssh-in-proxmox-ve-clusters.md)
- [5.11. Corosync 外部投票支持](11-corosync-external-vote-support.md)
- [5.12. Corosync 配置](12-corosync-configuration.md)
- [5.13. 集群冷启动](13-cluster-cold-start.md)
- [5.14. 客户机 VMID 自动选择](14-pvecm-next-id-range.md)
- [5.15. 客户机迁移](15-guest-migration.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
