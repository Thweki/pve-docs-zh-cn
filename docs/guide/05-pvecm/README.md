# 5. Cluster Manager <a href="#chapter_pvecm" id="chapter_pvecm"></a>

The Proxmox VE cluster manager `pvecm` is a tool to create a group of physical servers. Such a group is called a **cluster**. We use the [Corosync Cluster Engine](http://www.corosync.org) for reliable group communication. There’s no explicit limit for the number of nodes in a cluster. In practice, the actual possible node count may be limited by the host and network performance. Currently (2021), there are reports of clusters (using high-end enterprise hardware) with over 50 nodes in production.

`pvecm` can be used to create a new cluster, join nodes to a cluster, leave the cluster, get status information, and do various other cluster-related tasks. The **P**rox**m**o**x** **C**luster **F**ile **S**ystem (“pmxcfs”) is used to transparently distribute the cluster configuration to all cluster nodes.

Grouping nodes into a cluster has the following advantages:

- Centralized, web-based management
- Multi-master clusters: each node can do all management tasks
- Use of `pmxcfs`, a database-driven file system, for storing configuration files, replicated in real-time on all nodes using `corosync`
- Easy migration of virtual machines and containers between physical hosts
- Fast deployment
- Cluster-wide services like firewall and HA

## 本章内容

- [5.1. Requirements](01-pvecm-cluster-requirements.md)
- [5.2. Preparing Nodes](02-preparing-nodes.md)
- [5.3. Create a Cluster](03-pvecm-create-cluster.md)
- [5.4. Adding Nodes to the Cluster](04-pvecm-join-node-to-cluster.md)
- [5.5. Remove a Cluster Node](05-pvecm-remove-node.md)
- [5.6. Separate a Node Without Reinstalling](06-pvecm-separate-node-without-reinstall.md)
- [5.7. Quorum](07-quorum.md)
- [5.8. Cluster Network](08-pvecm-cluster-network.md)
- [5.9. Corosync Redundancy](09-pvecm-redundancy.md)
- [5.10. Role of SSH in Proxmox VE Clusters](10-role-of-ssh-in-proxmox-ve-clusters.md)
- [5.11. Corosync External Vote Support](11-corosync-external-vote-support.md)
- [5.12. Corosync Configuration](12-corosync-configuration.md)
- [5.13. Cluster Cold Start](13-cluster-cold-start.md)
- [5.14. Guest VMID Auto-Selection](14-pvecm-next-id-range.md)
- [5.15. Guest Migration](15-guest-migration.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
