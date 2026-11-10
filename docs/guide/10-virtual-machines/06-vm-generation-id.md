# 10.6. VM Generation ID <a href="#_vm_generation_id" id="_vm_generation_id"></a>

Proxmox VE supports Virtual Machine Generation ID (*vmgenid*)   
[Official *vmgenid* Specification [https://docs.microsoft.com/en-us/windows/desktop/hyperv_v2/virtual-machine-generation-identifier](https://docs.microsoft.com/en-us/windows/desktop/hyperv_v2/virtual-machine-generation-identifier)]  
 for virtual machines. This can be used by the guest operating system to detect any event resulting in a time shift event, for example, restoring a backup or a snapshot rollback.

When creating new VMs, a *vmgenid* will be automatically generated and saved in its configuration file.

To create and add a *vmgenid* to an already existing VM one can pass the special value ‘1’ to let Proxmox VE autogenerate one or manually set the *UUID*   
[Online GUID generator [http://guid.one/](http://guid.one/)]  
 by using it as value, for example:

```text
# qm set VMID -vmgenid 1
# qm set VMID -vmgenid 00000000-0000-0000-0000-000000000000
```

{% hint style="info" %}
The initial addition of a *vmgenid* device to an existing VM, may result in the same effects as a change on snapshot rollback, backup restore, etc., has as the VM can interpret this as generation change.
{% endhint %}

In the rare case the *vmgenid* mechanism is not wanted one can pass ‘0’ for its value on VM creation, or retroactively delete the property in the configuration with:

```text
# qm set VMID -delete vmgenid
```

The most prominent use case for *vmgenid* are newer Microsoft Windows operating systems, which use it to avoid problems in time sensitive or replicate services (such as databases or domain controller   
[[https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture)]  
) on snapshot rollback, backup restore or a whole VM clone operation.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
