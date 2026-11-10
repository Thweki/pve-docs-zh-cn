# 5.1. 要求 <a href="#pvecm_cluster_requirements" id="pvecm_cluster_requirements"></a>

- 所有节点必须能够通过 UDP 端口 5405-5412 相互连接，corosync 才能正常工作。
- 日期和时间必须保持同步。
- 节点之间需要通过 TCP 端口 22 建立 SSH 隧道。
- 如果您对高可用性感兴趣，则至少需要三个节点才能实现可靠的仲裁。所有节点应使用相同的版本。

  {% hint style="info" %}
  对于较小的双节点集群，可以使用 [QDevice](11-corosync-external-vote-support.md) 提供第三票。
  {% endhint %}
- 我们建议为集群流量使用专用的物理 NIC。

  {% hint style="info" %}
  Proxmox VE 集群通信使用 Corosync 协议。它需要稳定的低延迟，但不需要很大的带宽。在大多数情况下，专用的 1 Gbit NIC 就足够了。这有助于避免其他服务耗尽所有可用带宽的情况，而这又会增加 Corosync 数据包的延迟。
  {% endhint %}
- 为集群流量添加额外链路可在专用网络发生故障时提供冗余。

  {% hint style="info" %}
  Corosync 最多支持 8 条链路。
  {% endhint %}

  {% hint style="info" %}
  为确保可靠的 Corosync 冗余，必须在不同的物理网络上至少再配置一条链路。这样，当专用网络发生故障时，Corosync 仍能保持集群通信。
  {% endhint %}

  {% hint style="info" %}
  由 bond 支持的单一链路在某些故障场景下可能会出现问题，请参见[通过 Bond 使用 Corosync](08-pvecm-cluster-network.md#pvecm_corosync_over_bonds)。
  {% endhint %}
- 添加节点时需要集群节点的 root 密码。
- 仅当节点使用同一供应商的 CPU 时，才支持虚拟机在线迁移。在其他情况下也可能可行，但无法保证。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
