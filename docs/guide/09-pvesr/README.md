# 9\. Storage Replication <a href="#chapter_pvesr" id="chapter_pvesr"></a>

The `pvesr` command-line tool manages the Proxmox VE storage replication framework. Storage replication brings redundancy for guests using local storage and reduces migration time.

It replicates guest volumes to another node so that all data is available without using shared storage. Replication uses snapshots to minimize traffic sent over the network. Therefore, new data is sent only incrementally after the initial full sync. In the case of a node failure, your guest data is still available on the replicated node.

The replication is done automatically in configurable intervals. The minimum replication interval is one minute, and the maximal interval once a week. The format used to specify those intervals is a subset of `systemd` calendar events, see [Schedule Format](02-pvesr-schedule-time-format.md#pvesr_schedule_time_format) section:

It is possible to replicate a guest to multiple target nodes, but not twice to the same target node.

Each replications bandwidth can be limited, to avoid overloading a storage or server.

Only changes since the last replication (so-called `deltas`) need to be transferred if the guest is migrated to a node to which it already is replicated. This reduces the time needed significantly. The replication direction automatically switches if you migrate a guest to the replication target node.

For example: VM100 is currently on `nodeA` and gets replicated to `nodeB`. You migrate it to `nodeB`, so now it gets automatically replicated back from `nodeB` to `nodeA`.

If you migrate to a node where the guest is not replicated, the whole disk data must send over. After the migration, the replication job continues to replicate this guest to the configured nodes.

{% hint style="warning" %}
High-Availability is allowed in combination with storage replication, but there may be some data loss between the last synced time and the time a node failed.
{% endhint %}

## 本章内容

- [9.1. Supported Storage Types](01-supported-storage-types.md)
- [9.2. Schedule Format](02-pvesr-schedule-time-format.md)
- [9.3. Error Handling](03-error-handling.md)
- [9.4. Managing Jobs](04-managing-jobs.md)
- [9.5. Network](05-network.md)
- [9.6. Command-line Interface Examples](06-command-line-interface-examples.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
