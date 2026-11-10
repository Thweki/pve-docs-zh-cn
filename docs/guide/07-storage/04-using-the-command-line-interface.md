# 7.4. Using the Command-line Interface <a href="#_using_the_command_line_interface" id="_using_the_command_line_interface"></a>

It is recommended to familiarize yourself with the concept behind storage pools and volume identifiers, but in real life, you are not forced to do any of those low level operations on the command line. Normally, allocation and removal of volumes is done by the VM and Container management tools.

Nevertheless, there is a command-line tool called `pvesm` (“Proxmox VE Storage Manager”), which is able to perform common storage management tasks.

## 7.4.1. Examples <a href="#_examples" id="_examples"></a>

Add storage pools

```text
pvesm add <TYPE> <STORAGE_ID> <OPTIONS>
pvesm add dir <STORAGE_ID> --path <PATH>
pvesm add nfs <STORAGE_ID> --path <PATH> --server <SERVER> --export <EXPORT>
pvesm add lvm <STORAGE_ID> --vgname <VGNAME>
pvesm add iscsi <STORAGE_ID> --portal <HOST[:PORT]> --target <TARGET>
```

Disable storage pools

```text
pvesm set <STORAGE_ID> --disable 1
```

Enable storage pools

```text
pvesm set <STORAGE_ID> --disable 0
```

Change/set storage options

```text
pvesm set <STORAGE_ID> <OPTIONS>
pvesm set <STORAGE_ID> --shared 1
pvesm set local --format qcow2
pvesm set <STORAGE_ID> --content iso
```

Remove storage pools. This does not delete any data, and does not disconnect or unmount anything. It just removes the storage configuration.

```text
pvesm remove <STORAGE_ID>
```

Allocate volumes

```text
pvesm alloc <STORAGE_ID> <VMID> <name> <size> [--format <raw|qcow2>]
```

Allocate a 4G volume in local storage. The name is auto-generated if you pass an empty string as `<name>`

```text
pvesm alloc local <VMID> '' 4G
```

Free volumes

```text
pvesm free <VOLUME_ID>
```

{% hint style="warning" %}
This really destroys all volume data.
{% endhint %}

List storage status

```text
pvesm status
```

List storage contents

```text
pvesm list <STORAGE_ID> [--vmid <VMID>]
```

List volumes allocated by VMID

```text
pvesm list <STORAGE_ID> --vmid <VMID>
```

List iso images

```text
pvesm list <STORAGE_ID> --content iso
```

List container templates

```text
pvesm list <STORAGE_ID> --content vztmpl
```

Show file system path for a volume

```text
pvesm path <VOLUME_ID>
```

Exporting the volume `local:103/vm-103-disk-0.qcow2` to the file `target`. This is mostly used internally with `pvesm import`. The stream format qcow2\+size is different to the qcow2 format. Consequently, the exported file cannot simply be attached to a VM. This also holds for the other formats.

```text
pvesm export local:103/vm-103-disk-0.qcow2 qcow2+size target --with-snapshots 1
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
