# 7.1. Storage Types <a href="#_storage_types" id="_storage_types"></a>

There are basically two different classes of storage types:

**File level storage**

File level based storage technologies allow access to a fully featured (POSIX) file system. They are in general more flexible than any Block level storage (see below), and allow you to store content of any type. ZFS is probably the most advanced system, and it has full support for snapshots and clones.

**Block level storage**

Allows to store large *raw* images. It is usually not possible to store other files (ISO, backups, ..) on such storage types. Most modern block level storage implementations support snapshots and clones. Ceph RADOS is a distributed systems, replicating storage data to different nodes that can be accessed as RBD (RADOS Block Device).

<table>
<caption>Table 2. Available storage types</caption>






<thead>
<tr>
<th>Description</th>
<th>Plugin type</th>
<th>Level</th>
<th>Shared</th>
<th>Snapshots</th>
<th>Stable</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>ZFS (local)</p></td>
<td><p>zfspool</p></td>
<td><p>both<sup>1</sup></p></td>
<td><p>no</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>Directory</p></td>
<td><p>dir</p></td>
<td><p>file</p></td>
<td><p>no</p></td>
<td><p>yes<sup>2</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>BTRFS</p></td>
<td><p>btrfs</p></td>
<td><p>file</p></td>
<td><p>no</p></td>
<td><p>yes</p></td>
<td><p>TP<sup>5</sup></p></td>
</tr>
<tr>
<td><p>NFS</p></td>
<td><p>nfs</p></td>
<td><p>file</p></td>
<td><p>yes</p></td>
<td><p>yes<sup>2</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>CIFS</p></td>
<td><p>cifs</p></td>
<td><p>file</p></td>
<td><p>yes</p></td>
<td><p>yes<sup>2</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>Proxmox Backup</p></td>
<td><p>pbs</p></td>
<td><p>both</p></td>
<td><p>yes</p></td>
<td><p>n/a</p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>CephFS</p></td>
<td><p>cephfs</p></td>
<td><p>file</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>LVM</p></td>
<td><p>lvm</p></td>
<td><p>block</p></td>
<td><p>no<sup>3</sup></p></td>
<td><p>yes<sup>4</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>LVM-thin</p></td>
<td><p>lvmthin</p></td>
<td><p>block</p></td>
<td><p>no</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>iSCSI/kernel</p></td>
<td><p>iscsi</p></td>
<td><p>block</p></td>
<td><p>yes<sup>3</sup></p></td>
<td><p>yes<sup>4</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>iSCSI/libiscsi</p></td>
<td><p>iscsidirect</p></td>
<td><p>block</p></td>
<td><p>yes<sup>3</sup></p></td>
<td><p>yes<sup>4</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>FC/SAS</p></td>
<td><p>native<sup>6</sup></p></td>
<td><p>block</p></td>
<td><p>yes<sup>3</sup></p></td>
<td><p>yes<sup>4</sup></p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>Ceph/RBD</p></td>
<td><p>rbd</p></td>
<td><p>block</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
<tr>
<td><p>ZFS over iSCSI</p></td>
<td><p>zfs</p></td>
<td><p>block</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
</tbody>
</table>

1: Disk images for VMs are stored in ZFS volume (zvol) datasets, which provide block device functionality.

2: On file based storages, snapshots are possible with the *qcow2* format, either using the internal snapshot function, or snapshots as volume chains4. Creating and deleting internal *qcow2* snapshots will block a running VM and is not an efficient operation. The performance is particularly bad with network storages like NFS. On some setups and for large disks (multiple hundred GiB or TiB sized), these operations may take several minutes, or in extreme cases, even hours. If your setup is affected, create and remove snapshots while the VM is shut down, expecting a long task duration.

3: With iSCSI, FibreChannel (FC), or SAS block storage as shared storage in a cluster, LVM is used to split the LUN into virtual disks. The [Multipath Guide](https://pve.proxmox.com/wiki/Multipath) explains how to configure it in a cluster, including multipathing which is usually a requirement in these scenarios.

4: Since Proxmox VE 9, snapshots as a volume chain have been available for VMs. These snapshots use separate volumes for the snapshot data and layer them. For more details, see the description for `snapshot-as-volume-chain` in the [LVM configuration](10-storage-lvm.md#pvesm_lvm_config) section.

5 Technology preview with best-effort support.

6 Fibre Channel (FC) and SAS block storage is handled directly by the host without a dedicated storage plugin.

## 7.1.1. Thin Provisioning <a href="#_thin_provisioning" id="_thin_provisioning"></a>

A number of storages, and the QEMU image format `qcow2`, support *thin provisioning*. With thin provisioning activated, only the blocks that the guest system actually use will be written to the storage.

Say for instance you create a VM with a 32GB hard disk, and after installing the guest system OS, the root file system of the VM contains 3 GB of data. In that case only 3GB are written to the storage, even if the guest VM sees a 32GB hard drive. In this way thin provisioning allows you to create disk images which are larger than the currently available storage blocks. You can create large disk images for your VMs, and when the need arises, add more disks to your storage without resizing the VMs' file systems.

All storage types which have the “Snapshots” feature also support thin provisioning.

{% hint style="danger" %}
If a storage runs full, all guests using volumes on that storage receive IO errors. This can cause file system inconsistencies and may corrupt your data. So it is advisable to avoid over-provisioning of your storage resources, or carefully observe free space to avoid such conditions.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
