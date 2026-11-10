# 5.1. Requirements <a href="#pvecm_cluster_requirements" id="pvecm_cluster_requirements"></a>

- All nodes must be able to connect to each other via UDP ports 5405-5412 for corosync to work.
- Date and time must be synchronized.
- An SSH tunnel on TCP port 22 between nodes is required.
- If you are interested in High Availability, you need to have at least three nodes for reliable quorum. All nodes should have the same version.

  {% hint style="info" %}
  For smaller 2-node clusters, the [QDevice](11-corosync-external-vote-support.md#_corosync_external_vote_support) can be used to provide a 3rd vote.
  {% endhint %}
- We recommend a dedicated physical NIC for the cluster traffic.

  {% hint style="info" %}
  The Proxmox VE cluster communication uses the Corosync protocol. It needs consistent low latency but not a lot of bandwidth. A dedicated 1 Gbit NIC is enough in most situations. It helps to avoid situations where other services can use up all the available bandwidth. Which in turn would increase the latency for the Corosync packets.
  {% endhint %}
- Additional links for cluster traffic offers redundancy in case the dedicated network is down.

  {% hint style="info" %}
  Corosync supports up to 8 links.
  {% endhint %}

  {% hint style="info" %}
  To ensure reliable Corosync redundancy, it is essential to have at least another link on a different physical network. This enables Corosync to keep the cluster communication alive should the dedicated network be down.
  {% endhint %}

  {% hint style="info" %}
  A single link backed by a bond can be problematic in certain failure scenarios, see [Corosync Over Bonds](08-pvecm-cluster-network.md#pvecm_corosync_over_bonds).
  {% endhint %}
- The root password of a cluster node is required for adding nodes.
- Online migration of virtual machines is only supported when nodes have CPUs from the same vendor. It might work otherwise, but this is never guaranteed.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
