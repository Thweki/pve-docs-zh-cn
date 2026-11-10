# 3.8. 逻辑卷管理器（LVM） <a href="#chapter_lvm" id="chapter_lvm"></a>

大多数人会直接将 Proxmox VE 安装在本地磁盘上。Proxmox VE 安装光盘提供了多种本地磁盘管理选项，当前的默认设置使用 LVM。安装程序允许您为此类设置选择单块磁盘，并将该磁盘用作**卷****组**（VG）`pve`的物理卷。以下输出来自使用一块小型 8GB 磁盘的测试安装：

```text
# pvs
  PV         VG   Fmt  Attr PSize PFree
  /dev/sda3  pve  lvm2 a--  7.87g 876.00m

# vgs
  VG   #PV #LV #SN Attr   VSize VFree
  pve    1   3   0 wz--n- 7.87g 876.00m
```

安装程序会在此 VG 中分配三个**逻**辑**卷**（LV）：

```text
# lvs
  LV   VG   Attr       LSize   Pool Origin Data%  Meta%
  data pve  twi-a-tz--   4.38g             0.00   0.63
  root pve  -wi-ao----   1.75g
  swap pve  -wi-ao---- 896.00m
```

**root**

格式化为 `ext4`，并包含操作系统。

**swap**

交换分区

**data**

此卷使用 LVM-thin，用于存储 VM 镜像。LVM-thin 更适合此用途，因为它能够高效地支持快照和克隆。

对于 4.1 及更早版本的 Proxmox VE，安装程序会创建一个名为“data”的标准逻辑卷，并将其挂载到 `/var/lib/vz`。

从 4.2 版开始，逻辑卷“data”是一个 LVM-thin 池，用于存储基于块的客户机镜像，而 `/var/lib/vz` 只是根文件系统上的一个目录。

## 3.8.1. 硬件 <a href="#_hardware" id="_hardware"></a>

对于此类设置，我们强烈建议使用硬件 RAID 控制器（带 BBU）。这可以提高性能、提供冗余，并使磁盘更换更加容易（支持热插拔）。

LVM 本身不需要任何特殊硬件，内存要求也非常低。

## 3.8.2. 引导加载程序 <a href="#_bootloader" id="_bootloader"></a>

默认情况下，我们会安装两个引导加载程序。第一个分区包含标准的 GRUB 引导加载程序。第二个分区是**E**FI **系**统**分**区（ESP），它使系统能够在 EFI 系统上引导，并从用户空间应用[持久性固件更新](03-chapter-firmware-updates.md#sysadmin_firmware_persistent)。

## 3.8.3. 创建卷组 <a href="#_creating_a_volume_group" id="_creating_a_volume_group"></a>

假设我们有一块空磁盘 `/dev/sdb`，并希望在其上创建一个名为“vmdata”的卷组。

{% hint style="danger" %}
请注意，以下命令将销毁 `/dev/sdb` 上的所有现有数据。
{% endhint %}

首先创建一个分区。

```text
# sgdisk -N 1 /dev/sdb
```

创建一个**物**理**卷**（PV），无需确认，并将 metadatasize 设置为 250K。

```text
# pvcreate --metadatasize 250k -y -ff /dev/sdb1
```

在 `/dev/sdb1` 上创建一个名为“vmdata”的卷组

```text
# vgcreate vmdata /dev/sdb1
```

## 3.8.4. 为 `/var/lib/vz` 创建额外的 LV <a href="#_creating_an_extra_lv_for_span_class_monospaced_var_lib_vz_span" id="_creating_an_extra_lv_for_span_class_monospaced_var_lib_vz_span"></a>

只需创建一个新的精简 LV 即可轻松完成。

```text
# lvcreate -n <Name> -V <Size[M,G,T]> <VG>/<LVThin_pool>
```

一个实际示例：

```text
# lvcreate -n vz -V 10G pve/data
```

现在必须在 LV 上创建文件系统。

```text
# mkfs.ext4 /dev/pve/vz
```

最后必须将其挂载。

{% hint style="warning" %}
请确保 `/var/lib/vz` 为空。在默认安装中，它并非为空。
{% endhint %}

要使其始终可访问，请在 `/etc/fstab` 中添加以下行。

```text
# echo '/dev/pve/vz /var/lib/vz ext4 defaults 0 2' >> /etc/fstab
```

## 3.8.5. 调整精简池的大小 <a href="#_resizing_the_thin_pool" id="_resizing_the_thin_pool"></a>

使用以下命令调整 LV 和元数据池的大小：

```text
# lvresize --size +<size[\M,G,T]> --poolmetadatasize +<size[\M,G]> <VG>/<LVThin_pool>
```

{% hint style="info" %}
扩展数据池时，也必须扩展元数据池。
{% endhint %}

## 3.8.6. 创建 LVM-thin 池 <a href="#_create_a_lvm_thin_pool" id="_create_a_lvm_thin_pool"></a>

精简池必须创建在卷组之上。有关如何创建卷组，请参阅“LVM”一节。

```text
# lvcreate -L 80G -T -n vmstore vmdata
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
