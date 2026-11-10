# 4.4. Content Panels <a href="#_content_panels" id="_content_panels"></a>

When you select an item from the resource tree, the corresponding object displays configuration and status information in the content panel. The following sections provide a brief overview of this functionality. Please refer to the corresponding chapters in the reference documentation to get more detailed information.

## 4.4.1. Datacenter <a href="#_datacenter" id="_datacenter"></a>

[![screenshot/gui-datacenter-search.png](../../assets/screenshot-gui-datacenter-search-png-0d4035c472d2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-search.png)

On the datacenter level, you can access cluster-wide settings and information.

- **Search:** perform a cluster-wide search for nodes, VMs, containers, storage devices, and pools.
- **Summary:** gives a brief overview of the cluster’s health and resource usage.
- **Cluster:** provides the functionality and information necessary to create or join a cluster.
- **Options:** view and manage cluster-wide default settings.
- **Storage:** provides an interface for managing cluster storage.
- **Backup:** schedule backup jobs. This operates cluster wide, so it doesn’t matter where the VMs/containers are on your cluster when scheduling.
- **Replication:** view and manage replication jobs.
- **Permissions:** manage user, group, and API token permissions, and LDAP, MS-AD and Two-Factor authentication.
- **HA:** manage Proxmox VE High Availability.
- **ACME:** set up ACME (Let’s Encrypt) certificates for server nodes.
- **Firewall:** configure and make templates for the Proxmox Firewall cluster wide.
- **Metric Server:** define external metric servers for Proxmox VE.
- **Notifications:** configurate notification behavior and targets for Proxmox VE.
- **Support:** display information about your support subscription.

## 4.4.2. Nodes <a href="#_nodes" id="_nodes"></a>

[![screenshot/gui-node-summary.png](../../assets/screenshot-gui-node-summary-png-fa9649a32134.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-summary.png)

Nodes in your cluster can be managed individually at this level.

The top header has useful buttons such as *Reboot*, *Shutdown*, *Shell*, *Bulk Actions* and *Help*. *Shell* has the options *noVNC*, *SPICE* and *xterm.js*. *Bulk Actions* has the options *Bulk Start*, *Bulk Shutdown* and *Bulk Migrate*.

- **Search:** search a node for VMs, containers, storage devices, and pools.
- **Summary:** display a brief overview of the node’s resource usage.
- **Notes:** write custom comments in [Markdown syntax](../28-markdown-primer/01-markdown-basics.md#markdown_basics).
- **Shell:** access to a shell interface for the node.
- **System:** configure network, DNS and time settings, and access the syslog.
- **Updates:** upgrade the system and see the available new packages.
- **Firewall:** manage the Proxmox Firewall for a specific node.
- **Disks:** get an overview of the attached disks, and manage how they are used.
- **Ceph:** is only used if you have installed a Ceph server on your host. In this case, you can manage your Ceph cluster and see the status of it here.
- **Replication:** view and manage replication jobs.
- **Task History:** see a list of past tasks.
- **Subscription:** upload a subscription key, and generate a system report for use in support cases.

## 4.4.3. Guests <a href="#_guests" id="_guests"></a>

[![screenshot/gui-qemu-summary.png](../../assets/screenshot-gui-qemu-summary-png-58b9f19bf02c.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-summary.png)

There are two different kinds of guests and both can be converted to a template. One of them is a Kernel-based Virtual Machine (KVM) and the other is a Linux Container (LXC). Navigation for these are mostly the same; only some options are different.

To access the various guest management interfaces, select a VM or container from the menu on the left.

The header contains commands for items such as power management, migration, console access and type, cloning, HA, and help. Some of these buttons contain drop-down menus, for example, *Shutdown* also contains other power options, and *Console* contains the different console types: *SPICE*, *noVNC* and *xterm.js*.

The panel on the right contains an interface for whatever item is selected from the menu on the left.

The available interfaces are as follows.

- **Summary:** provides a brief overview of the VM’s activity and a `Notes` field for [Markdown syntax](../28-markdown-primer/01-markdown-basics.md#markdown_basics) comments.
- **Console:** access to an interactive console for the VM/container.
- **(KVM)Hardware:** define the hardware available to the KVM VM.
- **(LXC)Resources:** define the system resources available to the LXC.
- **(LXC)Network:** configure a container’s network settings.
- **(LXC)DNS:** configure a container’s DNS settings.
- **Options:** manage guest options.
- **Task History:** view all previous tasks related to the selected guest.
- **(KVM) Monitor:** an interactive communication interface to the KVM process.
- **Backup:** create and restore system backups.
- **Replication:** view and manage the replication jobs for the selected guest.
- **Snapshots:** create and restore VM snapshots.
- **Firewall:** configure the firewall on the VM level.
- **Permissions:** manage permissions for the selected guest.

## 4.4.4. Storage <a href="#_storage" id="_storage"></a>

[![screenshot/gui-storage-summary-local.png](../../assets/screenshot-gui-storage-summary-local-png-bed0feb5e875.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-storage-summary-local.png)

As with the guest interface, the interface for storage consists of a menu on the left for certain storage elements and an interface on the right to manage these elements.

In this view we have a two partition split-view. On the left side we have the storage options and on the right side the content of the selected option will be shown.

- **Summary:** shows important information about the storage, such as the type, usage, and content which it stores.
- **Content:** a menu item for each content type which the storage stores, for example, Backups, ISO Images, CT Templates.
- **Permissions:** manage permissions for the storage.

## 4.4.5. Pools <a href="#_pools" id="_pools"></a>

[![screenshot/gui-pool-summary-development.png](../../assets/screenshot-gui-pool-summary-development-png-00f1481ce5db.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-pool-summary-development.png)

Again, the pools view comprises two partitions: a menu on the left, and the corresponding interfaces for each menu item on the right.

- **Summary:** shows a description of the pool.
- **Members:** display and manage pool members (guests and storage).
- **Permissions:** manage the permissions for the pool.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
