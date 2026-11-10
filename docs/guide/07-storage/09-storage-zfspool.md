# 7.9. Local ZFS Pool Backend <a href="#storage_zfspool" id="storage_zfspool"></a>

Storage pool type: `zfspool`

This backend allows you to access local ZFS pools (or ZFS file systems inside such pools).

## 7.9.1. Configuration <a href="#_configuration_6" id="_configuration_6"></a>

The backend supports the common storage properties `content`, `nodes`, `disable`, and the following ZFS specific properties:

**pool**

Select the ZFS pool/filesystem. All allocations are done within that pool.

**blocksize**

Set ZFS blocksize parameter.

**sparse**

Use ZFS thin-provisioning. A sparse volume is a volume whose reservation is not equal to the volume size.

**mountpoint**

The mount point of the ZFS pool/filesystem. Changing this does not affect the `mountpoint` property of the dataset seen by `zfs`. Defaults to `/<pool>`.

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
zfspool: vmdata
        pool tank/vmdata
        content rootdir,images
        sparse
```

## 7.9.2. File naming conventions <a href="#_file_naming_conventions_2" id="_file_naming_conventions_2"></a>

The backend uses the following naming scheme for VM images:

```text
vm-<VMID>-<NAME>      // normal VM images
base-<VMID>-<NAME>    // template VM image (read-only)
subvol-<VMID>-<NAME>  // subvolumes (ZFS filesystem for containers)
```

**`<VMID>`**

This specifies the owner VM.

**`<NAME>`**

This can be an arbitrary name (`ascii`) without white space. The backend uses `disk[N]` as default, where `[N]` is replaced by an integer to make the name unique.

## 7.9.3. Storage Features <a href="#_storage_features_5" id="_storage_features_5"></a>

ZFS is probably the most advanced storage type regarding snapshot and cloning. The backend uses ZFS datasets for both VM images (format `raw`) and container data (format `subvol`). ZFS properties are inherited from the parent dataset, so you can simply set defaults on the parent dataset.

<table>
<caption>Table 8. Storage features for backend <code>zfs</code></caption>





<thead>
<tr>
<th>Content types</th>
<th>Image formats</th>
<th>Shared</th>
<th>Snapshots</th>
<th>Clones</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images rootdir</p></td>
<td><p>raw subvol</p></td>
<td><p>no</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
</tbody>
</table>

## 7.9.4. Encryption <a href="#_encryption" id="_encryption"></a>

ZFS supports encryption of dataset hierarchies. Each encrypted dataset, is either an `encryption_root`, storing the properties for encryption itself or descendant of its `encryption_root` \- see the `zfs-load-key(8)` manpage for details.

Sending and receiving encrypted datasets is subject to constraints as some encryption parameters (initialization vectors for the symmetric ciphers) need to be either transferred with the data, breaking inheriting the encryption properties on the receiving side, or need to be recreated on target, requiring the data to be sent unencrypted \- see the `zfs-recv(8)` manpage for details.

For migration and storage replication of encrypted datasets in Proxmox VE, the data is sent without the encryption properties, and the state of encryption is determined by the target.

If you want to send and receive encrypted ZFS datasets, you need to ensure that all involved storages on all nodes are encrypted.

## 7.9.5. Examples <a href="#_examples_5" id="_examples_5"></a>

It is recommended to create an extra ZFS file system to store your VM images:

```text
# zfs create tank/vmdata
```

To enable compression on that newly allocated file system:

```text
# zfs set compression=on tank/vmdata
```

You can get a list of available ZFS filesystems with:

```text
# pvesm scan zfs
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
