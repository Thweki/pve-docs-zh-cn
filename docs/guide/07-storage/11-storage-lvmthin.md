# 7.11. LVM thin Backend <a href="#storage_lvmthin" id="storage_lvmthin"></a>

Storage pool type: `lvmthin`

LVM normally allocates blocks when you create a volume. LVM thin pools instead allocates blocks when they are written. This behaviour is called thin-provisioning, because volumes can be much larger than physically available space.

You can use the normal LVM command-line tools to manage and create LVM thin pools (see `man lvmthin` for details). Assuming you already have a LVM volume group called `pve`, the following commands create a new LVM thin pool (size 100G) called `data`:

```text
lvcreate -L 100G -n data pve
lvconvert --type thin-pool pve/data
```

## 7.11.1. Configuration <a href="#_configuration_7" id="_configuration_7"></a>

The LVM thin backend supports the common storage properties `content`, `nodes`, `disable`, and the following LVM specific properties:

**`vgname`**

LVM volume group name. This must point to an existing volume group.

**`thinpool`**

The name of the LVM thin pool.

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
lvmthin: local-lvm
        thinpool data
        vgname pve
        content rootdir,images
```

## 7.11.2. File naming conventions <a href="#_file_naming_conventions_4" id="_file_naming_conventions_4"></a>

The backend use basically the same naming conventions as the ZFS pool backend.

```text
vm-<VMID>-<NAME>      // normal VM images
```

## 7.11.3. Storage Features <a href="#_storage_features_7" id="_storage_features_7"></a>

LVM thin is a block storage, but fully supports snapshots and clones efficiently. New volumes are automatically initialized with zero.

It must be mentioned that LVM thin pools cannot be shared across multiple nodes, so you can only use them as local storage.

<table>
<caption>Table 10. Storage features for backend <code>lvmthin</code></caption>





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
<td><p>raw</p></td>
<td><p>no</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
</tbody>
</table>

## 7.11.4. Examples <a href="#_examples_7" id="_examples_7"></a>

You can get a list of available LVM thin pools on the volume group `pve` with:

```text
# pvesm scan lvmthin pve
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
