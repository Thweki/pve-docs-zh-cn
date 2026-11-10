# 3.8. Logical Volume Manager (LVM) <a href="#chapter_lvm" id="chapter_lvm"></a>

Most people install Proxmox VE directly on a local disk. The Proxmox VE installation CD offers several options for local disk management, and the current default setup uses LVM. The installer lets you select a single disk for such setup, and uses that disk as physical volume for the **V**olume **G**roup (VG) `pve`. The following output is from a test installation using a small 8GB disk:

```text
# pvs
  PV         VG   Fmt  Attr PSize PFree
  /dev/sda3  pve  lvm2 a--  7.87g 876.00m

# vgs
  VG   #PV #LV #SN Attr   VSize VFree
  pve    1   3   0 wz--n- 7.87g 876.00m
```

The installer allocates three **L**ogical **V**olumes (LV) inside this VG:

```text
# lvs
  LV   VG   Attr       LSize   Pool Origin Data%  Meta%
  data pve  twi-a-tz--   4.38g             0.00   0.63
  root pve  -wi-ao----   1.75g
  swap pve  -wi-ao---- 896.00m
```

**root**

Formatted as `ext4`, and contains the operating system.

**swap**

Swap partition

**data**

This volume uses LVM-thin, and is used to store VM images. LVM-thin is preferable for this task, because it offers efficient support for snapshots and clones.

For Proxmox VE versions up to 4.1, the installer creates a standard logical volume called “data”, which is mounted at `/var/lib/vz`.

Starting from version 4.2, the logical volume “data” is a LVM-thin pool, used to store block based guest images, and `/var/lib/vz` is simply a directory on the root file system.

## 3.8.1. Hardware <a href="#_hardware" id="_hardware"></a>

We highly recommend to use a hardware RAID controller (with BBU) for such setups. This increases performance, provides redundancy, and make disk replacements easier (hot-pluggable).

LVM itself does not need any special hardware, and memory requirements are very low.

## 3.8.2. Bootloader <a href="#_bootloader" id="_bootloader"></a>

We install two boot loaders by default. The first partition contains the standard GRUB boot loader. The second partition is an **E**FI **S**ystem **P**artition (ESP), which makes it possible to boot on EFI systems and to apply [persistent firmware updates](03-chapter-firmware-updates.md#sysadmin_firmware_persistent) from the user space.

## 3.8.3. Creating a Volume Group <a href="#_creating_a_volume_group" id="_creating_a_volume_group"></a>

Let’s assume we have an empty disk `/dev/sdb`, onto which we want to create a volume group named “vmdata”.

{% hint style="danger" %}
Please note that the following commands will destroy all existing data on `/dev/sdb`.
{% endhint %}

First create a partition.

```text
# sgdisk -N 1 /dev/sdb
```

Create a **P**hysical **V**olume (PV) without confirmation and 250K metadatasize.

```text
# pvcreate --metadatasize 250k -y -ff /dev/sdb1
```

Create a volume group named “vmdata” on `/dev/sdb1`

```text
# vgcreate vmdata /dev/sdb1
```

## 3.8.4. Creating an extra LV for `/var/lib/vz` <a href="#_creating_an_extra_lv_for_span_class_monospaced_var_lib_vz_span" id="_creating_an_extra_lv_for_span_class_monospaced_var_lib_vz_span"></a>

This can be easily done by creating a new thin LV.

```text
# lvcreate -n <Name> -V <Size[M,G,T]> <VG>/<LVThin_pool>
```

A real world example:

```text
# lvcreate -n vz -V 10G pve/data
```

Now a filesystem must be created on the LV.

```text
# mkfs.ext4 /dev/pve/vz
```

At last this has to be mounted.

{% hint style="warning" %}
be sure that `/var/lib/vz` is empty. On a default installation it’s not.
{% endhint %}

To make it always accessible add the following line in `/etc/fstab`.

```text
# echo '/dev/pve/vz /var/lib/vz ext4 defaults 0 2' >> /etc/fstab
```

## 3.8.5. Resizing the thin pool <a href="#_resizing_the_thin_pool" id="_resizing_the_thin_pool"></a>

Resize the LV and the metadata pool with the following command:

```text
# lvresize --size +<size[\M,G,T]> --poolmetadatasize +<size[\M,G]> <VG>/<LVThin_pool>
```

{% hint style="info" %}
When extending the data pool, the metadata pool must also be extended.
{% endhint %}

## 3.8.6. Create a LVM-thin pool <a href="#_create_a_lvm_thin_pool" id="_create_a_lvm_thin_pool"></a>

A thin pool has to be created on top of a volume group. How to create a volume group see Section LVM.

```text
# lvcreate -L 80G -T -n vmstore vmdata
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
