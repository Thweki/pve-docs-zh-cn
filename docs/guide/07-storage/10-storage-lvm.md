# 7.10. LVM Backend <a href="#storage_lvm" id="storage_lvm"></a>

Storage pool type: `lvm`

LVM is a lightweight software layer that sits on top of hard disks and partitions. It can be used to divide available disk space into smaller logical volumes.

Another use case is placing LVM on top of a large iSCSI LUN (Logical Unit Number) or a SAN (Storage Area Network) connected via Fibre Channel. This allows you to easily manage the space on the iSCSI LUN, which would otherwise be impossible because the iSCSI specification does not define a management interface for space allocation.

## 7.10.1. Configuration <a href="#pvesm_lvm_config" id="pvesm_lvm_config"></a>

The LVM backend supports the common storage properties `content`, `nodes`, `disable`, and the following LVM specific properties:

**`vgname`**

LVM volume group name. This must point to an existing volume group.

**`base`**

Base volume. This volume is automatically activated before accessing the storage. This is mostly useful when the LVM volume group resides on a remote iSCSI server.

**`saferemove`**

Called "Wipe Removed Volumes" in the web UI. Zero-out data when removing LVs. When removing a volume, this makes sure that all data gets erased and cannot be accessed by other LVs created later (which happen to be assigned the same physical extents). This is a costly operation, but may be required as a security measure in certain environments.

Storage devices that support the "write zeroes" operation will use `blkdiscard` to zero blocks. Otherwise, a fallback to `cstream` is performed.

**`saferemove-stepsize`**

Wipe step size in MiB (`blkdiscard -p` parameter value), capped to the maximum step size supported by the underlying storage. Up to 32 MiB (maximum) by default.

**`saferemove_throughput`**

Wipe throughput (`cstream -t` parameter value), up to 10 MiB/s by default.

**`snapshot-as-volume-chain`**

Set this flag to enable snapshot support for virtual machines on LVM with a volume backing chain. With this setting, taking a snapshot persists the current state under the snapshot’s name and starts a new volume backed by the snapshot.

A volume based on a snapshot references its parent snapshot volume as its backing volume and records only the differences to that backing volume. Snapshot volumes are currently thick-provisioned LVM logical volumes.

This design avoids issues with native LVM snapshots, such as significant input/output (I/O) penalties and unexpected, dangerous behavior when running out of pre-allocated space.

Snapshots as volume chains provide vendor-agnostic support for snapshots on any storage system that supports block storage. This includes iSCSI and Fibre Channel-attached SANs.

Note that, although this feature relies on qcow2, it only uses qcow2’s ability to layer multiple volumes in a backing chain, not qcow2’s snapshot functionality. The snapshot functionality is managed by the PVE storage system.

Enabling or disabling this flag only affects newly created virtual disk volumes.

For efficient support of `snapshot-as-volume-chain`, the backing storage must support thin-provisioning and discard. Each snapshot will appear to use the full volume size on the PVE side, but the actual space usage on the underlying storage will be smaller if those requirements are met.

{% hint style="warning" %}
Snapshots as volume chains are currently a **technology preview** in Proxmox VE.
{% endhint %}

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
lvm: myspace
        vgname myspace
        content rootdir,images
```

## 7.10.2. File naming conventions <a href="#_file_naming_conventions_3" id="_file_naming_conventions_3"></a>

The backend use basically the same naming conventions as the ZFS pool backend.

```text
vm-<VMID>-<NAME>      // normal VM images
```

## 7.10.3. Storage Features <a href="#_storage_features_6" id="_storage_features_6"></a>

LVM is a typical block storage system. Unfortunately, regular LVM snapshots are inefficient because they interfere with all write operations within the entire volume group while the snapshot is active, which causes significant I/O degradation. This is why LVM does not support linked clones, and why Proxmox VE added support for snapshots as volume chains. This feature manages the snapshot volume through the storage plugin and uses qcow2 to layer separate volumes as a backing chain. This creates a single disk state that is exposed to the guest.

A benefit of LVM is that it can be used with shared storage. For example, an iSCSI LUN. The backend implements proper cluster-wide locking if the storage is marked as shared in the configuration.

{% hint style="success" %}
You can use the LVM-thin backend for non-shared local storage. It supports snapshots and linked clones.
{% endhint %}

<table>
<caption>Table 9. Storage features for backend <code>lvm</code></caption>






<thead>
<tr>
<th>Content types</th>
<th>Image formats</th>
<th>Shared</th>
<th>Snapshots</th>
<th>Full Clones</th>
<th>Linked Clones</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images rootdir</p></td>
<td><p>raw, qcow2<sup>1</sup></p></td>
<td><p>possible</p></td>
<td><p>yes<sup>1</sup></p></td>
<td><p>yes</p></td>
<td><p>no</p></td>
</tr>
</tbody>
</table>

1: Since Proxmox VE 9, snapshots as a volume chain have been available for VMs, for details see the [LVM configuration](#pvesm_lvm_config) section.

## 7.10.4. Examples <a href="#_examples_6" id="_examples_6"></a>

You can get a list of available LVM volume groups with:

```text
# pvesm scan lvm
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
