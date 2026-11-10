# 5.2. Preparing Nodes <a href="#_preparing_nodes" id="_preparing_nodes"></a>

First, install Proxmox VE on all nodes. Make sure that each node is installed with the final hostname and IP configuration. Changing the hostname and IP is not possible after cluster creation.

While it’s common to reference all node names and their IPs in `/etc/hosts` (or make their names resolvable through other means), this is not necessary for a cluster to work. It may be useful however, as you can then connect from one node to another via SSH, using the easier to remember node name (see also [Link Address Types](08-pvecm-cluster-network.md#pvecm_corosync_addresses)). Note that we always recommend referencing nodes by their IP addresses in the cluster configuration.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
