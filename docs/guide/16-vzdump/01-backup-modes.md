# 16.1. 备份模式 <a href="#backup_modes" id="backup_modes"></a>

根据客户机类型，有多种方式提供一致性（选项 `mode`）。

**虚拟机的备份模式：**

**`stop` 模式**

此模式以虚拟机短暂停机为代价，提供最高的备份一致性。其工作方式是先有序关闭虚拟机，然后运行后台 QEMU 进程备份虚拟机数据。备份开始后，如果虚拟机此前正在运行，将恢复全面运行模式。一致性通过在线备份功能保证。

**`suspend` 模式**

此模式出于兼容性原因提供，在调用 `snapshot` 模式之前暂停虚拟机。由于暂停虚拟机会造成更长的停机时间，并且不一定提高数据一致性，建议改用 `snapshot` 模式。

**`snapshot` 模式**

此模式以少量不一致风险为代价，提供最短的运行停机时间。其工作方式是执行 Proxmox VE 在线备份，在虚拟机运行时复制数据块。如果启用客户机代理（`agent: 1`）且其正在运行，会调用 `guest-fsfreeze-freeze` 和 `guest-fsfreeze-thaw` 以提高一致性。

{% hint style="info" %}
在 Windows 客户机上，如果客户机内部还使用其他备份软件，则必须配置客户机代理。更多详情请参阅客户机代理章节中的 [冻结与解冻](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_qga_fsfreeze)。
{% endhint %}

有关用于 QemuServer 的 Proxmox VE 在线备份的技术概述，可在线查阅 [此处](https://git.proxmox.com/?p=pve-qemu.git;a=blob_plain;f=backup.txt)。

{% hint style="info" %}
Proxmox VE 在线备份在任意存储类型上提供类似快照的语义，不要求底层存储支持快照。另请注意，由于备份通过后台 QEMU 进程完成，因此当 QEMU 读取虚拟机磁盘时，已停止的虚拟机会短暂显示为正在运行。不过，虚拟机本身并未启动，只是读取其磁盘。
{% endhint %}

**容器的备份模式：**

**`stop` 模式**

在整个备份期间停止容器。这可能导致非常长的停机时间。

**`suspend` 模式**

此模式使用 rsync 将容器数据复制到临时位置（参见选项 `--tmpdir`）。然后暂停容器，再执行一次 rsync 复制已更改的文件。之后，再次启动（恢复）容器。这可使停机时间最短，但需要额外空间来保存容器副本。

当容器位于本地文件系统，而备份目标存储是 NFS/CIFS 服务器时，还应将 `--tmpdir` 设为位于本地文件系统，这会使性能提高数倍。如果备份存储为 NFS 服务器，并且要在 suspend 模式下备份使用 ACL 的本地容器，也必须使用本地 `tmpdir`。

**`snapshot` 模式**

此模式使用底层存储的快照功能。首先暂停容器，以确保数据一致性。随后为容器卷创建临时快照，并将快照内容归档到 tar 文件中。最后再次删除临时快照。

{% hint style="info" %}
`snapshot` 模式要求所有备份的卷都位于支持快照的存储上。使用 `backup=no` 挂载点选项，可以将单独的卷排除在备份之外（因而也不受此要求限制）。
{% endhint %}

{% hint style="info" %}
默认情况下，除根磁盘挂载点外，其他挂载点不包含在备份中。对于卷挂载点，可以设置 **备份** 选项，将挂载点包含在备份中。设备挂载和绑定挂载从不备份，因为其内容由 Proxmox VE 存储库之外管理。
{% endhint %}

## 16.1.1. 虚拟机备份 Fleecing <a href="#vm_backup_fleecing" id="vm_backup_fleecing"></a>

启动虚拟机备份时，QEMU 会在其块层安装“写前复制”过滤器。此过滤器确保当客户机发生新写入时，会先将备份仍需要的旧数据发送到备份目标。客户机写入会阻塞到此操作完成，因此客户机对尚未备份扇区的 IO 会受备份目标速度限制。

使用备份 fleecing 时，这些旧数据会缓存在 fleecing 镜像中，而非直接发送到备份目标。这有助于提高客户机 IO 性能，甚至可在某些场景中避免挂起，代价是需要更多存储空间。

要手动启动虚拟机 `123` 的备份，并在存储 `local-lvm` 上创建 fleecing 镜像，请运行

```text
vzdump 123 --fleecing enabled=1,storage=local-lvm
```

与往常一样，可以为特定备份作业设置此选项，或通过 [配置选项](10-vzdump-configuration.md) 将其设置为节点范围的后备值。在 UI 中，编辑备份作业时，可在 *高级* 选项卡配置 fleecing。

fleecing 存储应是快速本地存储，支持精简置备和 discard。例如 LVM-thin、RBD、在存储配置中设置了 `sparse 1` 的 ZFS，以及许多基于文件的存储。理想情况下，fleecing 存储应为专用存储，这样即使空间耗尽，也不会影响其他客户机，只会使备份失败。fleecing 镜像中已完成备份的部分会被丢弃，以尽量保持较低的空间用量。

对于不支持 discard 的基于文件的存储（例如 4.2 之前版本的 NFS），应在存储配置中设置 `preallocation off`。与 `qcow2`（存储支持时，自动用作 fleecing 镜像格式）结合使用时，其优点是镜像中已分配的部分以后可以复用，仍可节省相当多的空间。

{% hint style="warning" %}
在未使用精简置备的存储上，例如 LVM 或没有 `sparse` 选项的 ZFS，需要提前为 fleecing 镜像预留原始磁盘的全部大小。在精简置备存储上，只有当备份正在处理另一块磁盘、而客户机重写了整块磁盘时，fleecing 镜像才可能增长到与原始镜像相同的大小。
{% endhint %}

## 16.1.2. 容器变更检测模式 <a href="#ct_change_detection_mode" id="ct_change_detection_mode"></a>

设置变更检测模式会定义 pxar 归档的编码格式，以及以 Proxmox Backup Server 为目标备份容器时，如何处理已更改和未更改的文件。

编辑作业时，可在 *高级* 选项卡为单个备份作业配置变更检测模式选项。此外，还可通过 [配置选项](10-vzdump-configuration.md) 将此选项设为节点范围的后备值。

有 3 种可用的变更检测模式：

<table>


<thead>
<tr>
<th>模式</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Default</p></td>
<td><p>读取所有文件并编码到单个归档中，使用 pxar 格式版本 1。</p></td>
</tr>
<tr>
<td><p>Data</p></td>
<td><p>读取并编码所有文件，但将数据和元数据拆分为独立流，使用 pxar 格式版本 2。</p></td>
</tr>
<tr>
<td><p>Metadata</p></td>
<td><p>像 <code>Data</code> 一样拆分流并使用归档格式版本 2，但使用上一个快照的元数据归档（如果存在）检测未更改的文件，并尽可能复用其数据块，而无需从磁盘读取文件内容。</p></td>
</tr>
</tbody>
</table>

要使用变更检测模式 `metadata` 执行备份，可以运行

```text
vzdump 123 --storage pbs-storage --pbs-change-detection-mode metadata
```

{% hint style="info" %}
虚拟机备份或备份到 Proxmox Backup Server 以外的存储后端不受此设置影响。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
