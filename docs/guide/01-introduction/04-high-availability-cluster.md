# 1.4. 高可用性集群 <a href="#_high_availability_cluster" id="_high_availability_cluster"></a>

多节点 Proxmox VE HA 集群可实现虚拟机和容器的高可用性。集成的[高可用性（HA）管理器](../15-ha-manager/README.md#chapter_ha_manager)通过基于看门狗的隔离自动检测节点故障，并在健康节点上重新启动受影响的服务。无需 Pacemaker 等外部工具——HA 堆栈随 Proxmox VE 提供，并且完全通过 Web 界面或命令行进行配置。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
