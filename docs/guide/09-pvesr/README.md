# 9\. Storage Replication <a href="#chapter_pvesr" id="chapter_pvesr"></a>

`pvesr` 命令行工具用于管理 Proxmox VE 存储复制框架。存储复制为使用本地存储的客户机提供冗余，并缩短迁移时间。

它会将客户机卷复制到另一个节点，因此无需使用共享存储即可使所有数据可用。复制使用快照来最大限度地减少通过网络发送的流量。因此，在初始完全同步之后，仅增量发送新数据。如果节点发生故障，客户机数据仍可在副本所在节点上使用。

复制会按可配置的时间间隔自动进行。最短复制间隔为一分钟，最长间隔为每周一次。用于指定这些间隔的格式是 `systemd` 日历事件的子集，请参阅 [计划格式](02-pvesr-schedule-time-format.md) 一节：

可以将一台客户机复制到多个目标节点，但不能向同一目标节点复制两次。

可以限制每次复制的带宽，以避免存储或服务器过载。

如果客户机迁移到的节点已经是其复制目标，则只需传输自上次复制以来的更改（所谓的 `deltas`）。这可显著缩短所需时间。如果将客户机迁移到复制目标节点，复制方向会自动切换。

例如：VM100 当前位于 `nodeA`，并复制到 `nodeB`。您将其迁移到 `nodeB`，因此现在它会自动从 `nodeB` 复制回 `nodeA`。

如果迁移到的节点不是客户机的复制目标，则必须传输整个磁盘数据。迁移后，复制作业会继续将此客户机复制到配置的节点。

{% hint style="warning" %}
高可用性可以与存储复制结合使用，但在上次同步时间与节点故障时间之间可能会丢失一些数据。
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
