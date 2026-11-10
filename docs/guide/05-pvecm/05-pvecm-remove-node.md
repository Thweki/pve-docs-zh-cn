# 5.5. Remove a Cluster Node <a href="#pvecm_remove_node" id="pvecm_remove_node"></a>

{% hint style="danger" %}
Read the procedure carefully before proceeding, as it may not be what you want or need.
{% endhint %}

The following steps explain how to remove a node from a cluster that was also part of a [Ceph](../08-pveceph/README.md#chapter_pveceph) cluster. If Ceph was not installed on your node, you can simply ignore the steps that mention it.

{% hint style="info" %}
If your configuration contains a QDevice, you will need to remove it before removing the cluster node, as outlined in the FAQ [here](11-corosync-external-vote-support.md#_adding_deleting_nodes_after_qdevice_setup).
{% endhint %}

## 5.5.1. Prerequisites <a href="#_prerequisites" id="_prerequisites"></a>

- Move all virtual machines and containers away from the node.
- Back up all local data on the node to be deleted.
- Make sure the node to be deleted is not part of any replication job anymore.

  {% hint style="danger" %}
  If you fail to remove replication jobs from a node before removing the node itself, the replication job will become irremovable. Note that replication automatically switches direction when a replicated VM is migrated. Therefore, migrating a replicated VM from a node that is going to be deleted will set up replication jobs to that node automatically.
  {% endhint %}
- Ensure that the remaining Ceph cluster has sufficient storage space and that the OSDs are running (i.e. `up` and `in`). The destruction of any OSD, especially the last one on a node, will trigger a data rebalance in Ceph.

  {% hint style="info" %}
  Make sure that there are still enough nodes with OSDs available to satisfy the `size/min_size` parameters configured for the Ceph pools. If there are fewer than `size` (default: 3) nodes available, data redundancy will be degraded. If there are fewer than `min_size` (default: 2) nodes available, the I/O of the pools will be blocked until there are enough replicas available. Affected guests may crash if their I/O is blocked.
  {% endhint %}
- Ensure that sufficient [monitors](../08-pveceph/05-pve-ceph-monitors.md#pve_ceph_monitors), [managers](../08-pveceph/06-pve-ceph-manager.md#pve_ceph_manager) and, if using CephFS, [metadata servers](../08-pveceph/13-pveceph-fs.md#pveceph_fs_mds) remain available in the Ceph cluster.

## 5.5.2. Remove the Cluster Node <a href="#_remove_the_cluster_node" id="_remove_the_cluster_node"></a>

Before a node can be removed from a cluster, you must ensure that it is no longer part of a Ceph cluster and that no Ceph resources or services are residing on it.

In the following example, the cluster node `node4` will be removed from both the Ceph-, and Proxmox VE corosync-cluster.

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

1. Start by removing the node from the Ceph cluster, this consists of multiple steps:

   1. Start by [destroying](../08-pveceph/07-pve-ceph-osds.md#pve_ceph_osd_destroy) the remaining Ceph OSDs on the node to be deleted, one after another.
   2. Wait until the [CEPH status](../08-pveceph/15-pve-ceph-mon-and-ts.md#pve_ceph_mon_and_ts) reaches `HEALTH_OK` again.
   3. If any exists, destroy the remaining [Ceph metadata servers](../08-pveceph/13-pveceph-fs.md#pveceph_fs_mds) via the web interface at *Ceph → CephFS* or by running:

      ```text
      node4# pveceph mds destroy node4
      ```
   4. [Destroy the remaining Ceph monitor.](../08-pveceph/05-pve-ceph-monitors.md#pveceph_destroy_mon)
   5. [Destroy the remaining Ceph manager.](../08-pveceph/06-pve-ceph-manager.md#pveceph_destroy_mgr)
   6. Finally, remove the now empty Ceph bucket (Proxmox VE node to be removed) from the CRUSH hierarchy.

      ```text
      node4# ceph osd crush remove node4
      ```
2. Now, power off `node4` and ensure that it will not power on again in this network with its current configuration.

   {% hint style="warning" %}
   As mentioned above, it is critical to power off the node **before** removal, and make sure that it will **not** power on again (in the existing cluster network) with its current configuration. If you power on the node as it is, the cluster could end up broken, and it could be difficult to restore it to a functioning state.
   {% endhint %}
3. Log into one of the remaining cluster nodes and remove the node `node4` from the cluster.

   ```text
   node1# pvecm delnode node4
   ```

   {% hint style="info" %}
   It is possible that you will receive an error message stating `could not kill node (error = cs_err_not_exist)`. This does not signify an actual failure in the deletion of the node, but rather a failure in Corosync trying to kill an offline node. Thus, it can be safely ignored.
   {% endhint %}
4. Verify the node was successfully removed from the cluster

   ```text
   node1# pvecm nodes

   Membership information
   ~~~~~~~~~~~~~~~~~~~~~~
       Nodeid      Votes Name
            1          1 node1 (local)
            2          1 node2
            3          1 node3
   ```

## 5.5.3. Cleanup Steps After Node Removal <a href="#_cleanup_steps_after_node_removal" id="_cleanup_steps_after_node_removal"></a>

- The configuration files of the removed node will still reside in */etc/pve/nodes/node4* in the cluster filesystem. Recover any configuration you still need and remove the directory afterwards.
- The SSH fingerprint of the removed node will still reside in the *known_hosts* file on the other nodes. If you receive an SSH error after rejoining a node with the same IP or hostname, run `pvecm
    updatecerts` once on the re-added node to update its fingerprint cluster wide.
- Existing [high availability rules](../15-ha-manager/06-configuration-15.md#ha_manager_rules) will still reference the deleted node, therefore remove the node from any existing rules.
- The public key of the removed node will still be listed in */etc/pve/priv/authorized_keys* and should be deleted if it is no longer needed.

**Rejoin the same node again:**

If you want the same server to join the same cluster again, you have to:

- Reinstall Proxmox VE on the server,
- then [rejoin the node to the cluster](04-pvecm-join-node-to-cluster.md#pvecm_join_node_to_cluster)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
