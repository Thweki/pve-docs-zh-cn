# 16.1. Backup Modes <a href="#_backup_modes" id="_backup_modes"></a>

There are several ways to provide consistency (option `mode`), depending on the guest type.

**Backup modes for VMs:**

**`stop` mode**

This mode provides the highest consistency of the backup, at the cost of a short downtime in the VM operation. It works by executing an orderly shutdown of the VM, and then runs a background QEMU process to backup the VM data. After the backup is started, the VM goes to full operation mode if it was previously running. Consistency is guaranteed by using the live backup feature.

**`suspend` mode**

This mode is provided for compatibility reason, and suspends the VM before calling the `snapshot` mode. Since suspending the VM results in a longer downtime and does not necessarily improve the data consistency, the use of the `snapshot` mode is recommended instead.

**`snapshot` mode**

This mode provides the lowest operation downtime, at the cost of a small inconsistency risk. It works by performing a Proxmox VE live backup, in which data blocks are copied while the VM is running. If the guest agent is enabled (`agent: 1`) and running, it calls `guest-fsfreeze-freeze` and `guest-fsfreeze-thaw` to improve consistency.

{% hint style="info" %}
On Windows guests it is necessary to configure the guest agent if another backup software is used within the guest. See [Freeze \& Thaw](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_qga_fsfreeze) in the guest agent section for more details.
{% endhint %}

A technical overview of the Proxmox VE live backup for QemuServer can be found online [here](https://git.proxmox.com/?p=pve-qemu.git;a=blob_plain;f=backup.txt).

{% hint style="info" %}
Proxmox VE live backup provides snapshot-like semantics on any storage type. It does not require that the underlying storage supports snapshots. Also please note that since the backups are done via a background QEMU process, a stopped VM will appear as running for a short amount of time while the VM disks are being read by QEMU. However the VM itself is not booted, only its disk(s) are read.
{% endhint %}

**Backup modes for Containers:**

**`stop` mode**

Stop the container for the duration of the backup. This potentially results in a very long downtime.

**`suspend` mode**

This mode uses rsync to copy the container data to a temporary location (see option `--tmpdir`). Then the container is suspended and a second rsync copies changed files. After that, the container is started (resumed) again. This results in minimal downtime, but needs additional space to hold the container copy.

When the container is on a local file system and the target storage of the backup is an NFS/CIFS server, you should set `--tmpdir` to reside on a local file system too, as this will result in a many fold performance improvement. Use of a local `tmpdir` is also required if you want to backup a local container using ACLs in suspend mode if the backup storage is an NFS server.

**`snapshot` mode**

This mode uses the snapshotting facilities of the underlying storage. First, the container will be suspended to ensure data consistency. A temporary snapshot of the container’s volumes will be made and the snapshot content will be archived in a tar file. Finally, the temporary snapshot is deleted again.

{% hint style="info" %}
`snapshot` mode requires that all backed up volumes are on a storage that supports snapshots. Using the `backup=no` mount point option individual volumes can be excluded from the backup (and thus this requirement).
{% endhint %}

{% hint style="info" %}
By default additional mount points besides the Root Disk mount point are not included in backups. For volume mount points you can set the **Backup** option to include the mount point in the backup. Device and bind mounts are never backed up as their content is managed outside the Proxmox VE storage library.
{% endhint %}

## 16.1.1. VM Backup Fleecing <a href="#_vm_backup_fleecing" id="_vm_backup_fleecing"></a>

When a backup for a VM is started, QEMU will install a "copy-before-write" filter in its block layer. This filter ensures that upon new guest writes, old data still needed for the backup is sent to the backup target first. The guest write blocks until this operation is finished so guest IO to not-yet-backed-up sectors will be limited by the speed of the backup target.

With backup fleecing, such old data is cached in a fleecing image rather than sent directly to the backup target. This can help guest IO performance and even prevent hangs in certain scenarios, at the cost of requiring more storage space.

To manually start a backup of VM `123` with fleecing images created on the storage `local-lvm`, run

```text
vzdump 123 --fleecing enabled=1,storage=local-lvm
```

As always, you can set the option for specific backup jobs, or as a node-wide fallback via the [configuration options](10-vzdump-configuration.md). In the UI, fleecing can be configured in the *Advanced* tab when editing a backup job.

The fleecing storage should be a fast local storage, with thin provisioning and discard support. Examples are LVM-thin, RBD, ZFS with `sparse 1` in the storage configuration, many file-based storages. Ideally, the fleecing storage is a dedicated storage, so it running full will not affect other guests and just fail the backup. Parts of the fleecing image that have been backed up will be discarded to try and keep the space usage low.

For file-based storages that do not support discard (for example, NFS before version 4.2), you should set `preallocation off` in the storage configuration. In combination with `qcow2` (used automatically as the format for the fleecing image when the storage supports it), this has the advantage that already allocated parts of the image can be re-used later, which can still help save quite a bit of space.

{% hint style="warning" %}
On a storage that’s not thinly provisioned, for example, LVM or ZFS without the `sparse` option, the full size of the original disk needs to be reserved for the fleecing image up-front. On a thinly provisioned storage, the fleecing image can grow to the same size as the original image only if the guest re-writes a whole disk while the backup is busy with another disk.
{% endhint %}

## 16.1.2. CT Change Detection Mode <a href="#_ct_change_detection_mode" id="_ct_change_detection_mode"></a>

Setting the change detection mode defines the encoding format for the pxar archives and how changed, and unchanged files are handled for container backups with Proxmox Backup Server as the target.

The change detection mode option can be configured for individual backup jobs in the *Advanced* tab while editing a job. Further, this option can be set as node-wide fallback via the [configuration options](10-vzdump-configuration.md).

There are 3 change detection modes available:

<table>


<thead>
<tr>
<th>Mode</th>
<th>描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Default</p></td>
<td><p>Read and encode all files into a single archive, using the pxar format version 1.</p></td>
</tr>
<tr>
<td><p>Data</p></td>
<td><p>Read and encode all files, but split data and metadata into separate streams, using the pxar format version 2.</p></td>
</tr>
<tr>
<td><p>Metadata</p></td>
<td><p>Split streams and use archive format version 2 like <code>Data</code>, but use the metadata archive of the previous snapshot (if one exists) to detect unchanged files, and reuse their data chunks without reading file contents from disk, whenever possible.</p></td>
</tr>
</tbody>
</table>

To perform a backup using the change detecation mode `metadata` you can run

```text
vzdump 123 --storage pbs-storage --pbs-change-detection-mode metadata
```

{% hint style="info" %}
Backups of VMs or to storage backends other than Proxmox Backup Server are not affected by this setting.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
