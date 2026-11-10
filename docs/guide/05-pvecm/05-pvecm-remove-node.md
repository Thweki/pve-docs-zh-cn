# 5.5. 移除集群节点 <a href="#pvecm_remove_node" id="pvecm_remove_node"></a>

{% hint style="danger" %}
在继续操作之前，请仔细阅读该过程，因为它可能不符合您的意图或需求。
{% endhint %}

以下步骤介绍如何从一个同时也是 [Ceph](../08-pveceph/README.md) 集群成员的集群中移除节点。如果节点上未安装 Ceph，则可以直接忽略其中提及 Ceph 的步骤。

{% hint style="info" %}
如果配置中包含 QDevice，则需要先按照常见问题中[此处](11-corosync-external-vote-support.md#adding_deleting_nodes_after_qdevice_setup)的说明将其移除，然后再移除集群节点。
{% endhint %}

## 5.5.1. 前提条件 <a href="#prerequisites" id="prerequisites"></a>

- 将所有虚拟机和容器迁离该节点。
- 备份待删除节点上的所有本地数据。
- 确保待删除的节点不再属于任何复制任务。

  {% hint style="danger" %}
  如果在移除节点本身之前，未能从该节点移除复制任务，复制任务将变得无法移除。请注意，当已配置复制的 VM 迁移时，复制会自动切换方向。因此，将已配置复制的 VM 从待删除的节点迁出，会自动建立指向该节点的复制任务。
  {% endhint %}
- 确保剩余的 Ceph 集群具有足够的存储空间，并且 OSD 正在运行（即 `up` 和 `in`）。销毁任何 OSD，尤其是节点上的最后一个 OSD，都会触发 Ceph 数据重新平衡。

  {% hint style="info" %}
  确保仍有足够数量带有 OSD 的节点可用，以满足为 Ceph 池配置的 `size/min_size` 参数。如果可用节点少于 `size`（默认值：3）个，数据冗余程度将会降低。如果可用节点少于 `min_size`（默认值：2）个，池的 I/O 将被阻塞，直到有足够的副本可用。如果受影响的客户机的 I/O 被阻塞，它们可能会崩溃。
  {% endhint %}
- 确保 Ceph 集群中仍有足够的[监视器](../08-pveceph/05-pve-ceph-monitors.md)、[管理器](../08-pveceph/06-pve-ceph-manager.md)可用，并且在使用 CephFS 时，仍有足够的[元数据服务器](../08-pveceph/13-pveceph-fs.md#pveceph_fs_mds)可用。

## 5.5.2. 移除集群节点 <a href="#remove_the_cluster_node" id="remove_the_cluster_node"></a>

在从集群中移除节点之前，必须确保该节点不再是 Ceph 集群的一部分，并且其上不再驻留任何 Ceph 资源或服务。

在以下示例中，将从 Ceph 集群和 Proxmox VE corosync 集群中同时移除集群节点 `node4`。

```text
node4# pvecm nodes

Membership information
~~~~~~~~~~~~~~~~~~~~~~
    Nodeid      Votes Name
         1          1 node1
         2          1 node2
         3          1 node3
         4          1 node4 (local)
```

1. 首先从 Ceph 集群中移除该节点，这包括多个步骤：

   1. 首先，逐一[销毁](../08-pveceph/07-pve-ceph-osds.md#pve_ceph_osd_destroy)待删除节点上剩余的 Ceph OSD。
   2. 等待 [CEPH 状态](../08-pveceph/15-pve-ceph-mon-and-ts.md)再次恢复到 `HEALTH_OK`。
   3. 如果存在剩余的 [Ceph 元数据服务器](../08-pveceph/13-pveceph-fs.md#pveceph_fs_mds)，请通过 *Ceph → CephFS* 处的 Web 界面将其销毁，或者运行：

      ```text
      node4# pveceph mds destroy node4
      ```
   4. [销毁剩余的 Ceph 监视器。](../08-pveceph/05-pve-ceph-monitors.md#pveceph_destroy_mon)
   5. [销毁剩余的 Ceph 管理器。](../08-pveceph/06-pve-ceph-manager.md#pveceph_destroy_mgr)
   6. 最后，从 CRUSH 层次结构中移除现在已清空的 Ceph 桶（待移除的 Proxmox VE 节点）。

      ```text
      node4# ceph osd crush remove node4
      ```
2. 现在，关闭 `node4` 的电源，并确保它不会以当前配置在此网络中再次开机。

   {% hint style="warning" %}
   如上所述，在移除**之前**将节点关机至关重要，并且必须确保它**不会**以当前配置（在现有集群网络中）再次开机。如果按原样将节点开机，集群可能会损坏，并且可能难以恢复到正常运行的状态。
   {% endhint %}
3. 登录剩余的任一集群节点，然后从集群中移除节点 `node4`。

   ```text
   node1# pvecm delnode node4
   ```

   {% hint style="info" %}
   您可能会收到一条错误消息，内容为 `could not kill node (error = cs_err_not_exist)`。这并不表示节点删除实际失败，而是表示 Corosync 尝试终止离线节点时失败。因此，可以安全地忽略该消息。
   {% endhint %}
4. 验证节点已成功从集群中移除

   ```text
   node1# pvecm nodes

   Membership information
   ~~~~~~~~~~~~~~~~~~~~~~
       Nodeid      Votes Name
            1          1 node1 (local)
            2          1 node2
            3          1 node3
   ```

## 5.5.3. 节点移除后的清理步骤 <a href="#cleanup_steps_after_node_removal" id="cleanup_steps_after_node_removal"></a>

- 被移除节点的配置文件仍位于集群文件系统中的 */etc/pve/nodes/node4* 下。恢复您仍需要的所有配置，然后删除该目录。
- 被移除节点的 SSH 指纹仍将位于其他节点上的 *known\_hosts* 文件中。如果使用相同 IP 或主机名重新加入节点后收到 SSH 错误，请在重新添加的节点上运行一次 `pvecm
    updatecerts`，以在整个集群范围内更新其指纹。
- 现有的[高可用性规则](../15-ha-manager/06-configuration-15.md#ha_manager_rules)仍将引用已删除的节点，因此请从所有现有规则中移除该节点。
- 被移除节点的公钥仍会列在 */etc/pve/priv/authorized\_keys* 中，如果不再需要，应将其删除。

**重新加入同一节点：**

如果希望同一台服务器再次加入同一集群，必须：

- 在服务器上重新安装 Proxmox VE，
- 然后[将该节点重新加入集群](04-pvecm-join-node-to-cluster.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
