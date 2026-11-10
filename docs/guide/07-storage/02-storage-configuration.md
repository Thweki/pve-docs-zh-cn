# 7.2. Storage Configuration <a href="#_storage_configuration" id="_storage_configuration"></a>

All Proxmox VE related storage configuration is stored within a single text file at `/etc/pve/storage.cfg`. As this file is within `/etc/pve/`, it gets automatically distributed to all cluster nodes. So all nodes share the same storage configuration.

Sharing storage configuration makes perfect sense for shared storage, because the same “shared” storage is accessible from all nodes. But it is also useful for local storage types. In this case such local storage is available on all nodes, but it is physically different and can have totally different content.

## 7.2.1. Storage Pools <a href="#_storage_pools" id="_storage_pools"></a>

Each storage pool has a `<type>`, and is uniquely identified by its `<STORAGE_ID>`. A pool configuration looks like this:

```text
<type>: <STORAGE_ID>
        <property> <value>
        <property> <value>
        <property>
        ...
```

The `<type>: <STORAGE_ID>` line starts the pool definition, which is then followed by a list of properties. Most properties require a value. Some have reasonable defaults, in which case you can omit the value.

To be more specific, take a look at the default storage configuration after installation. It contains one special local storage pool named `local`, which refers to the directory `/var/lib/vz` and is always available. The Proxmox VE installer creates additional storage entries depending on the storage type chosen at installation time.

**Default storage configuration (`/etc/pve/storage.cfg`)**

```text
dir: local
        path /var/lib/vz
        content iso,vztmpl,backup

# default image store on LVM based installation
lvmthin: local-lvm
        thinpool data
        vgname pve
        content rootdir,images

# default image store on ZFS based installation
zfspool: local-zfs
        pool rpool/data
        sparse
        content images,rootdir
```

{% hint style="danger" %}
It is problematic to have multiple storage configurations pointing to the exact same underlying storage. Such an *aliased* storage configuration can lead to two different volume IDs (*volid*) pointing to the exact same disk image. Proxmox VE expects that the images' volume IDs point to, are unique. Choosing different content types for *aliased* storage configurations can be fine, but is not recommended.
{% endhint %}

## 7.2.2. Common Storage Properties <a href="#_common_storage_properties" id="_common_storage_properties"></a>

A few storage properties are common among different storage types.

**nodes**

List of cluster node names where this storage is usable/accessible. One can use this property to restrict storage access to a limited set of nodes.

**content**

A storage can support several content types, for example virtual disk images, cdrom iso images, container templates or container root directories. Not all storage types support all content types. One can set this property to select what this storage is used for.

**images**

QEMU/KVM VM images.

**rootdir**

Allow to store container data.

**vztmpl**

Container templates.

**backup**

Backup files (`vzdump`).

**iso**

ISO images

**snippets**

Snippet files, for example guest hook scripts

**import**

OVAs and VM disk images that can be imported from this storage

**shared**

Indicate that this is a single storage with the same contents on all nodes (or all listed in the *nodes* option). It will not make the contents of a local storage automatically accessible to other nodes, it just marks an already shared storage as such!

**disable**

You can use this flag to disable the storage completely.

**prune-backups**

Retention options for backups. For details, see [Backup Retention](../16-vzdump/06-vzdump-retention.md#vzdump_retention).

**format**

Default image format (`raw|qcow2|vmdk`)

**preallocation**

Preallocation mode (`off|metadata|falloc|full`) for `raw` and `qcow2` images on file-based storages. The default is `metadata`, which is treated like `off` for `raw` images. When using network storages in combination with large `qcow2` images, using `off` can help to avoid timeouts.

{% hint style="warning" %}
It is not advisable to use the same storage pool on different Proxmox VE clusters. Some storage operation need exclusive access to the storage, so proper locking is required. While this is implemented within a cluster, it does not work between different clusters.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
