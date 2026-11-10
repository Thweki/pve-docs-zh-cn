# 10.3. Migration <a href="#qm_migration" id="qm_migration"></a>

[![screenshot/gui-qemu-migrate.png](../../assets/screenshot-gui-qemu-migrate-png-75844014c4d2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-migrate.png)

If you have a cluster, you can migrate your VM to another host with

```text
# qm migrate <vmid> <target>
```

There are generally two mechanisms for this

- Online Migration (aka Live Migration)
- Offline Migration

## 10.3.1. Online Migration <a href="#_online_migration" id="_online_migration"></a>

If your VM is running and no locally bound resources are configured (such as devices that are passed through), you can initiate a live migration with the `--online` flag in the `qm migration` command evocation. The web interface defaults to live migration when the VM is running.

{% hint style="info" %}
Live migration is only possible between hosts of the same CPU architecture. A running guest’s CPU state cannot be transferred between an x86 and an arm64 host.
{% endhint %}

### How it works <a href="#_how_it_works" id="_how_it_works"></a>

Online migration first starts a new QEMU process on the target host with the *incoming* flag, which performs only basic initialization with the guest vCPUs still paused and then waits for the guest memory and device state data streams of the source Virtual Machine. All other resources, such as disks, are either shared or got already sent before runtime state migration of the VMs begins; so only the memory content and device state remain to be transferred.

Once this connection is established, the source begins asynchronously sending the memory content to the target. If the guest memory on the source changes, those sections are marked dirty and another pass is made to send the guest memory data. This loop is repeated until the data difference between running source VM and incoming target VM is small enough to be sent in a few milliseconds, because then the source VM can be paused completely, without a user or program noticing the pause, so that the remaining data can be sent to the target, and then unpause the targets VM’s CPU to make it the new running VM in well under a second.

### Requirements <a href="#_requirements" id="_requirements"></a>

For Live Migration to work, there are some things required:

- The VM has no local resources that cannot be migrated. For example, PCI or USB devices that are passed through currently block live-migration. Local Disks, on the other hand, can be migrated by sending them to the target just fine.
- The hosts are located in the same Proxmox VE cluster.
- The hosts have a working (and reliable) network connection between them.
- The target host must have the same, or higher versions of the Proxmox VE packages. Although it can sometimes work the other way around, this cannot be guaranteed.
- The hosts have CPUs from the same vendor with similar capabilities. Different vendor **might** work depending on the actual models and VMs CPU type configured, but it cannot be guaranteed \- so please test before deploying such a setup in production.

### Conntrack State Migration <a href="#_conntrack_state_migration" id="_conntrack_state_migration"></a>

{% hint style="info" %}
Conntrack state migration is considered best-effort only and might not work, as it heavily depends on the network setup. For example, setups using [source address masquerading (SNAT)](../03-system-administration/04-sysadmin-network-configuration.md#sysadmin_network_masquerading) on the host will most likely **not** work.
{% endhint %}

Conntrack is a Linux kernel mechanism to enable a stateful firewall by tracking individual connection. When live migrating running VMs, active in- and/or outbound connections **might** get interrupted as soon as the VM starts running on the target host, as the new host node does not have the same conntrack entries and thus the firewall can drop packets.

Conntrack state migration copies all conntrack entries on the host for the live-migrated VM to the target node and afterwards flushes the migrated entries from the conntrack table on the source node.

## 10.3.2. Offline Migration <a href="#_offline_migration" id="_offline_migration"></a>

If you have local resources, you can still migrate your VMs offline as long as all disk are on storage defined on both hosts. Migration then copies the disks to the target host over the network, as with online migration. Note that any hardware passthrough configuration may need to be adapted to the device location on the target host.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
