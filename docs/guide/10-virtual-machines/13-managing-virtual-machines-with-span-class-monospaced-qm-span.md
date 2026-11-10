# 10.13. Managing Virtual Machines with `qm` <a href="#_managing_virtual_machines_with_span_class_monospaced_qm_span" id="_managing_virtual_machines_with_span_class_monospaced_qm_span"></a>

qm is the tool to manage QEMU/KVM virtual machines on Proxmox VE. You can create and destroy virtual machines, and control execution (start/stop/suspend/resume). Besides that, you can use qm to set parameters in the associated config file. It is also possible to create and delete virtual disks.

## 10.13.1. CLI Usage Examples <a href="#_cli_usage_examples" id="_cli_usage_examples"></a>

Using an iso file uploaded on the *local* storage, create a VM with a 4 GB IDE disk on the *local-lvm* storage

```text
# qm create 300 -ide0 local-lvm:4 -net0 e1000 -cdrom local:iso/proxmox-mailgateway_2.1.iso
```

Start the new VM

```text
# qm start 300
```

Send a shutdown request, then wait until the VM is stopped.

```text
# qm shutdown 300 && qm wait 300
```

Same as above, but only wait for 40 seconds.

```text
# qm shutdown 300 && qm wait 300 -timeout 40
```

If the VM does not shut down, force-stop it and overrule any running shutdown tasks. As stopping VMs may incur data loss, use it with caution.

```text
# qm stop 300 -overrule-shutdown 1
```

Destroying a VM always removes it from Access Control Lists and it always removes the firewall configuration of the VM. You have to activate *--purge*, if you want to additionally remove the VM from replication jobs, backup jobs and HA resource configurations.

{% hint style="info" %}
启用 purge 还会从所有引用该 HA 资源的亲和性规则中移除该资源，并移除仅剩这一个资源的规则。
{% endhint %}

```text
# qm destroy 300 --purge
```

Move a disk image to a different storage.

```text
# qm move-disk 300 scsi0 other-storage
```

Reassign a disk image to a different VM. This will remove the disk `scsi1` from the source VM and attaches it as `scsi3` to the target VM. In the background the disk image is being renamed so that the name matches the new owner.

```text
# qm move-disk 300 scsi1 --target-vmid 400 --target-disk scsi3
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
