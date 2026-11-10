# 3.11. Proxmox Node Management <a href="#proxmox_node_management" id="proxmox_node_management"></a>

The Proxmox VE node management tool (`pvenode`) allows you to control node specific settings and resources.

Currently `pvenode` allows you to set a node’s description, run various bulk operations on the node’s guests, view the node’s task history, and manage the node’s SSL certificates, which are used for the API and the web GUI through `pveproxy`.

## 3.11.1. Wake-on-LAN <a href="#_wake_on_lan" id="_wake_on_lan"></a>

Wake-on-LAN (WoL) allows you to switch on a sleeping computer in the network, by sending a magic packet. At least one NIC must support this feature, and the respective option needs to be enabled in the computer’s firmware (BIOS/UEFI) configuration. The option name can vary from *Enable Wake-on-Lan* to *Power On By PCIE Device*; check your motherboard’s vendor manual, if you’re unsure. `ethtool` can be used to check the WoL configuration of `<interface>` by running:

```text
ethtool <interface> | grep Wake-on
```

`pvenode` allows you to wake sleeping members of a cluster via WoL, using the command:

```text
pvenode wakeonlan <node>
```

This broadcasts the WoL magic packet on UDP port 9, containing the MAC address of `<node>` obtained from the `wakeonlan` property. The node-specific `wakeonlan` property can be set using the following command:

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX
```

The interface via which to send the WoL packet is determined from the default route. It can be overwritten by setting the `bind-interface` via the following command:

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX,bind-interface=<iface-name>
```

The broadcast address (default `255.255.255.255`) used when sending the WoL packet can further be changed by setting the `broadcast-address` explicitly using the following command:

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX,broadcast-address=<broadcast-address>
```

## 3.11.2. Task History <a href="#_task_history" id="_task_history"></a>

When troubleshooting server issues, for example, failed backup jobs, it can often be helpful to have a log of the previously run tasks. With Proxmox VE, you can access the nodes’s task history through the `pvenode task` command.

You can get a filtered list of a node’s finished tasks with the `list` subcommand. For example, to get a list of tasks related to VM *100* that ended with an error, the command would be:

```text
pvenode task list --errors --vmid 100
```

The log of a task can then be printed using its UPID:

```text
pvenode task log UPID:pve1:00010D94:001CA6EA:6124E1B9:vzdump:100:root@pam:
```

## 3.11.3. Bulk Guest Power Management <a href="#_bulk_guest_power_management" id="_bulk_guest_power_management"></a>

In case you have many VMs/containers, starting and stopping guests can be carried out in bulk operations with the `startall` and `stopall` subcommands of `pvenode`. By default, `pvenode startall` will only start VMs/containers which have been set to automatically start on boot (see [Automatic Start and Shutdown of Virtual Machines](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_startup_and_shutdown)), however, you can override this behavior with the `--force` flag. Both commands also have a `--vms` option, which limits the stopped/started guests to the specified VMIDs.

For example, to start VMs *100*, *101*, and *102*, regardless of whether they have `onboot` set, you can use:

```text
pvenode startall --vms 100,101,102 --force
```

To stop these guests (and any other guests that may be running), use the command:

```text
pvenode stopall
```

{% hint style="info" %}
The stopall command first attempts to perform a clean shutdown and then waits until either all guests have successfully shut down or an overridable timeout (3 minutes by default) has expired. Once that happens and the force-stop parameter is not explicitly set to 0 (false), all virtual guests that are still running are hard stopped.
{% endhint %}

## 3.11.4. First Guest Boot Delay <a href="#first_guest_boot_delay" id="first_guest_boot_delay"></a>

In case your VMs/containers rely on slow-to-start external resources, for example an NFS server, you can also set a per-node delay between the time Proxmox VE boots and the time the first VM/container that is configured to autostart boots (see [Automatic Start and Shutdown of Virtual Machines](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_startup_and_shutdown)).

You can achieve this by setting the following (where `10` represents the delay in seconds):

```text
pvenode config set --startall-onboot-delay 10
```

## 3.11.5. Bulk Guest Migration <a href="#_bulk_guest_migration" id="_bulk_guest_migration"></a>

In case an upgrade situation requires you to migrate all of your guests from one node to another, `pvenode` also offers the `migrateall` subcommand for bulk migration. By default, this command will migrate every guest on the system to the target node. It can however be set to only migrate a set of guests.

For example, to migrate VMs *100*, *101*, and *102*, to the node *pve2*, with live-migration for local disks enabled, you can run:

```text
pvenode migrateall pve2 --vms 100,101,102 --with-local-disks
```

## 3.11.6. RAM Usage Target for Ballooning <a href="#ballooning-target" id="ballooning-target"></a>

The target percentage for [automatic memory allocation](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_ballooning) defaults to 80%. You can customize this target per node by setting the `ballooning-target` property. For example, to target 90% host memory usage instead:

```text
pvenode config set --ballooning-target 90
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
