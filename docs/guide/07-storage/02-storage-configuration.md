# 7.2. 存储配置 <a href="#storage_configuration" id="storage_configuration"></a>

所有与 Proxmox VE 相关的存储配置都存储在 `/etc/pve/storage.cfg` 处的单个文本文件中。由于该文件位于 `/etc/pve/` 中，因此会自动分发到所有集群节点。所以，所有节点共享相同的存储配置。

共享存储配置对于共享存储非常有意义，因为所有节点都可以访问同一个“共享”存储。但它对本地存储类型也很有用。在这种情况下，此类本地存储在所有节点上都可用，但它们在物理上并不相同，并且可以包含完全不同的内容。

## 7.2.1. 存储池 <a href="#storage_pools" id="storage_pools"></a>

每个存储池都有一个 `<type>`，并通过其 `<STORAGE_ID>` 进行唯一标识。池配置如下所示：

```text
<type>: <STORAGE_ID>
        <property> <value>
        <property> <value>
        <property>
        ...
```

`<type>: <STORAGE_ID>` 行开始池定义，后面是属性列表。大多数属性都需要一个值。某些属性有合理的默认值，在这种情况下可以省略该值。

具体来说，请查看安装后的默认存储配置。其中包含一个名为 `local` 的特殊本地存储池，该池指向目录 `/var/lib/vz`，并且始终可用。Proxmox VE 安装程序会根据安装时选择的存储类型创建其他存储条目。

**默认存储配置（`/etc/pve/storage.cfg`）**

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
让多个存储配置指向完全相同的底层存储会产生问题。此类*别名*存储配置可能导致两个不同的卷 ID（*volid*）指向完全相同的磁盘镜像。Proxmox VE 要求镜像的卷 ID 所指向的位置是唯一的。为*别名*存储配置选择不同的内容类型或许可行，但不建议这样做。
{% endhint %}

## 7.2.2. 通用存储属性 <a href="#common_storage_properties" id="common_storage_properties"></a>

一些存储属性为不同存储类型所共有。

**nodes**

可使用或访问此存储的集群节点名称列表。可以使用此属性将存储访问权限限制在一组特定的节点内。

**content**

一个存储可以支持多种内容类型，例如虚拟磁盘镜像、CD-ROM ISO 镜像、容器模板或容器根目录。并非所有存储类型都支持所有内容类型。可以设置此属性来选择此存储的用途。

**images**

QEMU/KVM VM 镜像。

**rootdir**

允许存储容器数据。

**vztmpl**

容器模板。

**backup**

备份文件（`vzdump`）。

**iso**

ISO 镜像

**snippets**

片段文件，例如客户机钩子脚本

**import**

可从此存储导入的 OVA 和 VM 磁盘镜像

**shared**

表明这是一个在所有节点（或 *nodes* 选项中列出的所有节点）上具有相同内容的单一存储。它不会使本地存储的内容自动可供其他节点访问，只是将已共享的存储标记为共享存储！

**disable**

可以使用此标志完全禁用该存储。

**prune-backups**

备份的保留选项。有关详细信息，请参阅[备份保留](../16-vzdump/06-vzdump-retention.md)。

**format**

默认镜像格式（`raw|qcow2|vmdk`）

**preallocation**

预分配模式（`off|metadata|falloc|full`），用于基于文件的存储上的 `raw` 和 `qcow2` 镜像。默认为 `metadata`，其处理方式与 `off` 相同（针对 `raw` 镜像）。将网络存储与大型 `qcow2` 镜像结合使用时，使用 `off` 有助于避免超时。

{% hint style="warning" %}
不建议在不同的 Proxmox VE 集群上使用同一个存储池。某些存储操作需要独占访问存储，因此需要正确的锁定机制。虽然集群内部实现了这种锁定，但它在不同集群之间不起作用。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
