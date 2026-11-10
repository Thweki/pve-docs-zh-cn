# 5.6. 在不重新安装的情况下分离节点 <a href="#pvecm_separate_node_without_reinstall" id="pvecm_separate_node_without_reinstall"></a>

{% hint style="danger" %}
这**不是**推荐的方法，请谨慎操作。如果不确定，请使用前一种方法。
{% endhint %}

您也可以在不从头重新安装的情况下，将节点从集群中分离出来。但是，从集群中移除节点后，它仍然可以访问任何共享存储。必须在开始从集群中移除节点之前解决此问题。Proxmox VE 集群不能与另一个集群共享完全相同的存储，因为存储锁定无法跨集群边界工作。此外，这还可能导致 VMID 冲突。

建议创建一个新存储，只有要分离的节点才有权访问该存储。例如，这可以是您的 NFS 上的新导出，也可以是新的 Ceph 池。重要的是，完全相同的存储不能被多个集群访问。设置此存储后，将该节点上的所有数据和 VM 都移动到此存储中。然后，您就可以将节点从集群中分离出来了。

{% hint style="info" %}
如果配置中包含 QDevice，则需要先按照常见问题中[此处](11-corosync-external-vote-support.md#_adding_deleting_nodes_after_qdevice_setup)的说明将其移除，然后再移除集群节点。
{% endhint %}

{% hint style="warning" %}
确保所有共享资源都已彻底分离！否则将遇到冲突和问题。
{% endhint %}

首先，停止节点上的 corosync 和 pve-cluster 服务：

```text
systemctl stop pve-cluster
systemctl stop corosync
```

再次以本地模式启动集群文件系统：

```text
pmxcfs -l
```

删除 corosync 配置文件：

```text
rm /etc/pve/corosync.conf
rm -r /etc/corosync/*
```

现在可以再次将文件系统作为普通服务启动：

```text
killall pmxcfs
systemctl start pve-cluster
```

该节点现已与集群分离。您可以在集群的任一剩余节点上使用以下命令将其删除：

```text
pvecm delnode oldnode
```

如果命令因剩余节点失去仲裁而失败，可以将预期票数设置为 1 作为变通方法：

```text
pvecm expected 1
```

然后重复执行 *pvecm delnode* 命令。

现在切换回已分离的节点，并删除其上所有剩余的集群文件。这样可以确保该节点能够再次加入另一个集群而不会出现问题。

```text
rm /var/lib/corosync/*
```

由于其他节点的配置文件仍位于集群文件系统中，您可能也希望清理这些文件。在绝对确定节点名称正确无误后，只需从 */etc/pve/nodes/NODENAME* 中递归删除整个目录即可。

{% hint style="danger" %}
该节点的 SSH 密钥仍将保留在 *authorized\_key* 文件中。这意味着各节点仍可以使用公钥身份验证相互连接。您应通过从 */etc/pve/priv/authorized\_keys* 文件中删除相应密钥来解决此问题。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
