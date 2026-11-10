# 7.3. Volumes <a href="#_volumes" id="_volumes"></a>

We use a special notation to address storage data. When you allocate data from a storage pool, it returns such a volume identifier. A volume is identified by the `<STORAGE_ID>`, followed by a storage type dependent volume name, separated by colon. A valid `<VOLUME_ID>` looks like:

```text
local:230/example-image.raw
```

```text
local:iso/debian-501-amd64-netinst.iso
```

```text
local:vztmpl/debian-5.0-joomla_1.5.9-1_i386.tar.gz
```

```text
iscsi-storage:0.0.2.scsi-14f504e46494c4500494b5042546d2d646744372d31616d61
```

To get the file system path for a `<VOLUME_ID>` use:

```text
pvesm path <VOLUME_ID>
```

## 7.3.1. Volume Ownership <a href="#_volume_ownership" id="_volume_ownership"></a>

There exists an ownership relation for `image` type volumes. Each such volume is owned by a VM or Container. For example volume `local:230/example-image.raw` is owned by VM 230\. Most storage backends encodes this ownership information into the volume name.

When you remove a VM or Container, the system also removes all associated volumes which are owned by that VM or Container.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
