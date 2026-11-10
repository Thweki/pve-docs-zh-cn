# 6.5. Recovery <a href="#_recovery" id="_recovery"></a>

如果您的 Proxmox VE 宿主机出现严重问题，例如硬件故障，复制 pmxcfs 数据库文件 `/var/lib/pve-cluster/config.db` 并将其移动到新的 Proxmox VE 宿主机可能会有所帮助。在新宿主机上（未运行任何内容），您需要停止 `pve-cluster` 服务并替换 `config.db` 文件（所需权限为 `0600`）。随后，根据丢失的 Proxmox VE 宿主机调整 `/etc/hostname` 和 `/etc/hosts`，然后重新启动并检查（也不要忘记您的 VM/CT 数据）。

## 6.5.1. Remove Cluster Configuration <a href="#_remove_cluster_configuration" id="_remove_cluster_configuration"></a>

建议的方法是在将节点从集群中移除后重新安装该节点。这可确保所有集群/SSH 密钥以及任何共享配置数据均被销毁。

In some cases, you might prefer to put a node back to local mode without reinstalling, which is described in [Separate A Node Without Reinstalling](../05-pvecm/06-pvecm-separate-node-without-reinstall.md#pvecm_separate_node_without_reinstall)

## 6.5.2. Recovering/Moving Guests from Failed Nodes <a href="#_recovering_moving_guests_from_failed_nodes" id="_recovering_moving_guests_from_failed_nodes"></a>

对于 `nodes/<NAME>/qemu-server/`（VM）和 `nodes/<NAME>/lxc/`（容器）中的客户机配置文件，Proxmox VE 将包含这些文件的节点 `<NAME>` 视为相应客户机的所有者。这一概念使得我们可以使用本地锁，而不是开销较大的集群范围锁，以防止并发更改客户机配置。

因此，如果客户机的所属节点发生故障（例如由于断电、隔离事件等），则无法进行常规迁移（即使所有磁盘都位于共享存储上），因为无法获得（离线）所属节点上的这种本地锁。对于由 HA 管理的客户机，这不是问题，因为 Proxmox VE 的高可用性栈包含必要的（集群范围）锁和看门狗功能，可确保客户机从被隔离的节点正确、自动地恢复。

如果非 HA 管理的客户机只有共享磁盘（并且没有其他仅在故障节点上可用的本地资源），则只需将客户机配置文件从 `/etc/pve/` 中故障节点的目录移动到在线节点的目录，即可手动恢复（这会更改客户机的逻辑所有者或位置）。

例如，在集群的任何成员节点上以 root 身份运行以下命令，即可将 ID 为 `100` 的 VM 从离线的 `node1` 恢复到另一个节点 `node2`：

```text
mv /etc/pve/nodes/node1/qemu-server/100.conf /etc/pve/nodes/node2/qemu-server/
```

{% hint style="warning" %}
在以这种方式手动恢复客户机之前，请务必确保故障源节点确实已关机/隔离。否则，`mv` 命令会违反 Proxmox VE 的锁定原则，可能产生意想不到的后果。
{% endhint %}

{% hint style="warning" %}
具有本地磁盘（或其他仅在离线节点上可用的本地资源）的客户机无法通过这种方式恢复。请等待故障节点重新加入集群，或从备份中恢复此类客户机。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
