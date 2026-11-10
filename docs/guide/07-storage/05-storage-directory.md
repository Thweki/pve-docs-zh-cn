# 7.5. Directory Backend <a href="#storage_directory" id="storage_directory"></a>

Storage pool type: `dir`

Proxmox VE can use local directories or locally mounted shares for storage. A directory is a file level storage, so you can store any content type like virtual disk images, containers, templates, ISO images or backup files.

{% hint style="info" %}
You can mount additional storages via standard linux `/etc/fstab`, and then define a directory storage for that mount point. This way you can use any file system supported by Linux.
{% endhint %}

This backend assumes that the underlying directory is POSIX compatible, but nothing else. This implies that you cannot create snapshots at the storage level. But there exists a workaround for VM images using the `qcow2` file format, because that format supports snapshots internally.

{% hint style="success" %}
Some storage types do not support `O_DIRECT`, so you can’t use cache mode `none` with such storages. Simply use cache mode `writeback` instead.
{% endhint %}

We use a predefined directory layout to store different content types into different sub-directories. This layout is used by all file level storage backends.

<table>
<caption>Table 3. Directory layout</caption>


<thead>
<tr>
<th>Content type</th>
<th>Subdir</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>VM images</p></td>
<td><p><code>images/&lt;VMID&gt;/</code></p></td>
</tr>
<tr>
<td><p>ISO images</p></td>
<td><p><code>template/iso/</code></p></td>
</tr>
<tr>
<td><p>Container templates</p></td>
<td><p><code>template/cache/</code></p></td>
</tr>
<tr>
<td><p>Backup files</p></td>
<td><p><code>dump/</code></p></td>
</tr>
<tr>
<td><p>Snippets</p></td>
<td><p><code>snippets/</code></p></td>
</tr>
<tr>
<td><p>Import</p></td>
<td><p><code>import/</code></p></td>
</tr>
</tbody>
</table>

## 7.5.1. Configuration <a href="#_configuration_2" id="_configuration_2"></a>

This backend supports all common storage properties, and adds two additional properties. The `path` property is used to specify the directory. This needs to be an absolute file system path.

The optional `content-dirs` property allows for the default layout to be changed. It consists of a comma-separated list of identifiers in the following format:

```text
vtype=path
```

Where `vtype` is one of the allowed content types for the storage, and `path` is a path relative to the mountpoint of the storage.

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
dir: backup
        path /mnt/backup
        content backup
        prune-backups keep-last=7
        max-protected-backups 3
        content-dirs backup=custom/backup/dir
```

The above configuration defines a storage pool called `backup`. That pool can be used to store up to 7 regular backups (`keep-last=7`) and 3 protected backups per VM. The real path for the backup files is `/mnt/backup/custom/backup/dir/...`.

## 7.5.2. File naming conventions <a href="#_file_naming_conventions" id="_file_naming_conventions"></a>

This backend uses a well defined naming scheme for VM images:

```text
vm-<VMID>-<NAME>.<FORMAT>
```

**`<VMID>`**

This specifies the owner VM.

**`<NAME>`**

This can be an arbitrary name (`ascii`) without white space. The backend uses `disk-[N]` as default, where `[N]` is replaced by an integer to make the name unique.

**`<FORMAT>`**

Specifies the image format (`raw|qcow2|vmdk`).

When you create a VM template, all VM images are renamed to indicate that they are now read-only, and can be used as a base image for clones:

```text
base-<VMID>-<NAME>.<FORMAT>
```

{% hint style="info" %}
Such base images are used to generate cloned images. So it is important that those files are read-only, and never get modified. The backend changes the access mode to `0444`, and sets the immutable flag (`chattr +i`) if the storage supports that.
{% endhint %}

## 7.5.3. Storage Features <a href="#_storage_features" id="_storage_features"></a>

As mentioned above, most file systems do not support snapshots out of the box. To workaround that problem, this backend is able to use `qcow2` internal snapshot capabilities.

Same applies to clones. The backend uses the `qcow2` base image feature to create clones.

<table>
<caption>Table 4. Storage features for backend <code>dir</code></caption>





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
<td><p>images rootdir vztmpl iso backup snippets</p></td>
<td><p>raw qcow2 vmdk subvol</p></td>
<td><p>no</p></td>
<td><p>qcow2</p></td>
<td><p>qcow2</p></td>
</tr>
</tbody>
</table>

## 7.5.4. Examples <a href="#_examples_2" id="_examples_2"></a>

Please use the following command to allocate a 4GB image on storage `local`:

```text
# pvesm alloc local 100 vm-100-disk10.raw 4G
Formatting '/var/lib/vz/images/100/vm-100-disk10.raw', fmt=raw size=4294967296
successfully created 'local:100/vm-100-disk10.raw'
```

{% hint style="info" %}
The image name must conform to above naming conventions.
{% endhint %}

The real file system path is shown with:

```text
# pvesm path local:100/vm-100-disk10.raw
/var/lib/vz/images/100/vm-100-disk10.raw
```

And you can remove the image with:

```text
# pvesm free local:100/vm-100-disk10.raw
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
