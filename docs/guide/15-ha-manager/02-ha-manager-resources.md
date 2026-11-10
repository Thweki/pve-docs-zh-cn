# 15.2. 资源 <a href="#ha_manager_resources" id="ha_manager_resources"></a>

HA 管理器的主要管理单元称为 HA 资源（或“HA 服务”）。目前，HA 资源可以是虚拟机（VM）或 Linux 容器（CT）。

每个 HA 资源都由服务 ID（`sid`）唯一标识，服务 ID 由资源类型和特定于类型的 ID 组成，对于 VM 和容器，该 ID 为 VMID。例如，对于 VMID 为`100`的 VM，其服务 ID 为`vm:100`。

HA 资源只能在其所有依赖项均可用的节点上运行。默认情况下，HA 管理器将每个集群节点都视为合格节点。要保持此默认行为，VM 或容器应：

- 使用与所有集群节点兼容的选项
- 仅使用所有集群节点均可访问的共享存储
- 仅使用所有集群节点上都存在的网络接口
- 仅使用所有集群节点上都存在的设备直通

如果这些依赖中有任何一项仅在部分节点上可用，请通过严格的 [节点亲和性规则](06-configuration-15.md#ha_manager_node_affinity_rules) 将 HA 资源限制在该节点子集内。HA 管理器随后会将放置、恢复和迁移限制在规则的节点内。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
