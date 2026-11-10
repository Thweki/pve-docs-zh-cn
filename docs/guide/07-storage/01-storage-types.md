# 7.1. 存储类型 <a href="#_storage_types" id="_storage_types"></a>

基本上有两类不同的存储类型：

**文件级存储**

文件级存储技术允许访问功能完整的（POSIX）文件系统。它们通常比任何块级存储（见下文）都更灵活，并允许您存储任何类型的内容。ZFS 可能是最先进的系统，它完全支持快照和克隆。

**块级存储**

允许存储大型 *raw* 镜像。通常无法在这类存储类型上存储其他文件（ISO、备份等）。大多数现代块级存储实现都支持快照和克隆。Ceph RADOS 是一个分布式系统，可将存储数据复制到不同的节点，并可作为 RBD（RADOS 块设备）进行访问。

<table>
<caption>表 2. 可用的存储类型</caption>






<thead>
<tr>
<th>描述</th>
<th>插件类型</th>
<th>级别</th>
<th>共享</th>
<th>快照</th>
<th>稳定</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>ZFS（本地）</p></td>
<td><p>zfspool</p></td>
<td><p>两者<sup>1</sup></p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>目录</p></td>
<td><p>dir</p></td>
<td><p>文件</p></td>
<td><p>否</p></td>
<td><p>是<sup>2</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>BTRFS</p></td>
<td><p>btrfs</p></td>
<td><p>文件</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>技术预览<sup>5</sup></p></td>
</tr>
<tr>
<td><p>NFS</p></td>
<td><p>nfs</p></td>
<td><p>文件</p></td>
<td><p>是</p></td>
<td><p>是<sup>2</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>CIFS</p></td>
<td><p>cifs</p></td>
<td><p>文件</p></td>
<td><p>是</p></td>
<td><p>是<sup>2</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>Proxmox Backup</p></td>
<td><p>pbs</p></td>
<td><p>两者</p></td>
<td><p>是</p></td>
<td><p>n/a</p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>CephFS</p></td>
<td><p>cephfs</p></td>
<td><p>文件</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>LVM</p></td>
<td><p>lvm</p></td>
<td><p>块</p></td>
<td><p>否<sup>3</sup></p></td>
<td><p>是<sup>4</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>LVM-thin</p></td>
<td><p>lvmthin</p></td>
<td><p>块</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>iSCSI/kernel</p></td>
<td><p>iscsi</p></td>
<td><p>块</p></td>
<td><p>是<sup>3</sup></p></td>
<td><p>是<sup>4</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>iSCSI/libiscsi</p></td>
<td><p>iscsidirect</p></td>
<td><p>块</p></td>
<td><p>是<sup>3</sup></p></td>
<td><p>是<sup>4</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>FC/SAS</p></td>
<td><p>native<sup>6</sup></p></td>
<td><p>块</p></td>
<td><p>是<sup>3</sup></p></td>
<td><p>是<sup>4</sup></p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>Ceph/RBD</p></td>
<td><p>rbd</p></td>
<td><p>块</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
<tr>
<td><p>基于 iSCSI 的 ZFS</p></td>
<td><p>zfs</p></td>
<td><p>块</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
</tbody>
</table>

1：VM 的磁盘镜像存储在 ZFS 卷（zvol）数据集中，这些数据集提供块设备功能。

2：在基于文件的存储上，可以使用 *qcow2* 格式创建快照，既可以使用内部快照功能，也可以使用卷链快照4。创建和删除内部 *qcow2* 快照会阻塞正在运行的 VM，而且效率不高。在 NFS 等网络存储上，性能尤其差。在某些配置中，对于大型磁盘（大小为数百 GiB 或 TiB 级），这些操作可能需要几分钟，在极端情况下甚至需要数小时。如果您的配置受到影响，请在 VM 关机时创建和删除快照，并做好任务耗时较长的准备。

3：在集群中使用 iSCSI、FibreChannel（FC）或 SAS 块存储作为共享存储时，LVM 用于将 LUN 划分为虚拟磁盘。[多路径指南](https://pve.proxmox.com/wiki/Multipath)介绍了如何在集群中进行配置，包括多路径配置，在这些场景中通常需要多路径。

4：自 Proxmox VE 9 起，VM 已支持卷链快照。这些快照使用单独的卷来存储快照数据，并将这些卷分层。有关更多详细信息，请参阅 `snapshot-as-volume-chain` 的描述，该描述位于 [LVM 配置](10-storage-lvm.md#pvesm_lvm_config) 一节中。

5 技术预览，提供尽力而为的支持。

6 Fibre Channel（FC）和 SAS 块存储由宿主机直接处理，无需专用存储插件。

## 7.1.1. 精简置备 <a href="#_thin_provisioning" id="_thin_provisioning"></a>

许多存储以及 QEMU 镜像格式 `qcow2` 都支持 *精简置备*。启用精简置备后，只有客户机系统实际使用的块才会写入存储。

例如，假设您创建了一台配备 32GB 硬盘的 VM，安装客户机操作系统后，该 VM 的根文件系统中包含 3 GB 数据。在这种情况下，即使客户机 VM 看到的是 32GB 硬盘，也只有 3GB 会写入存储。通过这种方式，精简置备允许您创建大于当前可用存储块的磁盘镜像。您可以为 VM 创建大型磁盘镜像，并在需要时向存储添加更多磁盘，而无需调整 VM 文件系统的大小。

所有具有“快照”功能的存储类型也都支持精简置备。

{% hint style="danger" %}
如果存储空间用尽，使用该存储上卷的所有客户机都会收到 IO 错误。这可能导致文件系统不一致，并可能损坏您的数据。因此，建议避免对存储资源进行过度置备，或者仔细监测可用空间，以避免出现此类情况。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
