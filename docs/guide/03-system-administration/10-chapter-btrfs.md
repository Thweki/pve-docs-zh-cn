# 3.10. BTRFS <a href="#chapter_btrfs" id="chapter_btrfs"></a>

{% hint style="warning" %}
BTRFS 集成目前在 Proxmox VE 中属于**技术预览**。
{% endhint %}

BTRFS 是一种现代的写时复制文件系统，由 Linux 内核原生支持，实现了快照、内置 RAID 以及通过数据和元数据校验和进行自我修复等功能。从 Proxmox VE 7.0 开始，BTRFS 被引入为根文件系统的可选项。

**BTRFS 的一般优势**

- 主系统设置与基于传统 ext4 的设置几乎相同
- 快照
- 文件系统级数据压缩
- 写时复制克隆
- RAID0、RAID1 和 RAID10
- 防止数据损坏
- 自我修复
- 由 Linux 内核原生支持

**注意事项**

- RAID 级别 5/6 仍处于实验阶段且存在危险，请参阅[BTRFS 状态](https://btrfs.readthedocs.io/en/latest/Status.html)

## 3.10.1. 安装为根文件系统 <a href="#_installation_as_root_file_system_2" id="_installation_as_root_file_system_2"></a>

使用 Proxmox VE 安装程序安装时，可以为根文件系统选择 BTRFS。需要在安装时选择 RAID 类型：

<table>
<tr>
<td>RAID0 <br/></td>
<td>
<p>也称为“条带化”。这种卷的容量是所有磁盘容量之和。但 RAID0 不提供任何冗余，因此单块磁盘发生故障就会导致整个卷不可用。</p>
</td>
</tr>
<tr>
<td>RAID1 <br/></td>
<td>
<p>也称为“镜像”。相同的数据会写入所有磁盘。这种模式至少需要 2 块大小相同的磁盘。最终容量相当于单块磁盘的容量。</p>
</td>
</tr>
<tr>
<td>RAID10 <br/></td>
<td>
<p>RAID0 和 RAID1 的组合。至少需要 4 块磁盘。</p>
</td>
</tr>
</table>

安装程序会自动对磁盘进行分区，并在 `/var/lib/pve/local-btrfs` 处创建一个额外的子卷。为了与 Proxmox VE 工具配合使用，安装程序会在 `/etc/pve/storage.cfg` 中创建以下配置条目：

```text
dir: local
        path /var/lib/vz
        content iso,vztmpl,backup
        disable

btrfs: local-btrfs
        path /var/lib/pve/local-btrfs
        content iso,vztmpl,backup,images,rootdir
```

这会显式禁用默认的 `local` 存储，转而使用位于额外子卷上的 BTRFS 专用存储条目。

`btrfs` 命令用于配置和管理 BTRFS 文件系统。安装后，以下命令会列出所有额外的子卷：

```text
# btrfs subvolume list /
ID 256 gen 6 top level 5 path var/lib/pve/local-btrfs
```

## 3.10.2. BTRFS 管理 <a href="#_btrfs_administration" id="_btrfs_administration"></a>

本节提供一些常见任务的用法示例。

### 创建 BTRFS 文件系统 <a href="#_creating_a_btrfs_file_system" id="_creating_a_btrfs_file_system"></a>

创建 BTRFS 文件系统时使用 `mkfs.btrfs`。`-d` 和 `-m` 参数分别用于设置元数据和数据的配置模式。使用可选的 `-L` 参数可以设置标签。

通常支持以下模式：`single`、`raid0`、`raid1`、`raid10`。

在单个磁盘 `/dev/sdb` 上创建标签为 `My-Storage` 的 BTRFS 文件系统：

```text
 # mkfs.btrfs -m single -d single -L My-Storage /dev/sdb
```

或者在两个分区 `/dev/sdb1` 和 `/dev/sdc1` 上创建 RAID1：

```text
 # mkfs.btrfs -m raid1 -d raid1 -L My-Storage /dev/sdb1 /dev/sdc1
```

### 挂载 BTRFS 文件系统 <a href="#_mounting_a_btrfs_file_system" id="_mounting_a_btrfs_file_system"></a>

随后可以手动挂载新文件系统，例如：

```text
 # mkdir /my-storage
 # mount /dev/sdb /my-storage
```

与其他挂载点一样，也可以将 BTRFS 添加到 `/etc/fstab` 中，使其在启动时自动挂载。建议避免使用块设备路径，而应使用 `UUID` 值，该值由 `mkfs.btrfs` 命令输出，尤其是在 BTRFS 配置包含多块磁盘时。

例如：

**文件 `/etc/fstab`**

```text
# ... other mount points left out for brevity

# using the UUID from the mkfs.btrfs output is highly recommended
UUID=e2c0c3ff-2114-4f54-b767-3a203e49f6f3 /my-storage btrfs defaults 0 0
```

{% hint style="success" %}
如果不再知道 UUID，可以使用 `blkid` 工具列出块设备的所有属性。
{% endhint %}

之后，可以执行以下命令触发首次挂载：

```text
mount /my-storage
```

下次重新启动后，系统将在启动时自动完成此操作。

### 将 BTRFS 文件系统添加到 Proxmox VE <a href="#_adding_a_btrfs_file_system_to_proxmox_ve" id="_adding_a_btrfs_file_system_to_proxmox_ve"></a>

可以通过 Web 界面或使用 CLI 将现有 BTRFS 文件系统添加到 Proxmox VE，例如：

```text
pvesm add btrfs my-storage --path /my-storage
```

### 创建子卷 <a href="#_creating_a_subvolume" id="_creating_a_subvolume"></a>

创建子卷会将其链接到 BTRFS 文件系统中的一个路径，并在该路径中显示为普通目录。

```text
# btrfs subvolume create /some/path
```

之后，`/some/path` 的行为将与普通目录一样。

### 删除子卷 <a href="#_deleting_a_subvolume" id="_deleting_a_subvolume"></a>

与通过 `rmdir` 删除的目录不同，子卷无需为空即可通过 `btrfs` 命令删除。

```text
# btrfs subvolume delete /some/path
```

### 创建子卷的快照 <a href="#_creating_a_snapshot_of_a_subvolume" id="_creating_a_snapshot_of_a_subvolume"></a>

BTRFS 实际上并不区分快照和普通子卷，因此创建快照也可以看作创建子卷的任意副本。按照惯例，Proxmox VE 在创建客户机磁盘或子卷的快照时会使用只读标志，但之后也可以更改此标志。

```text
# btrfs subvolume snapshot -r /some/path /a/new/path
```

This will create a read-only "clone" of the subvolume on `/some/path` at `/a/new/path`. Any future modifications to `/some/path` cause the modified data to be copied before modification.

如果省略只读（`-r`）选项，两个子卷都将可写。

### 启用压缩 <a href="#_enabling_compression" id="_enabling_compression"></a>

默认情况下，BTRFS 不压缩数据。要启用压缩，可以添加 `compress` 挂载选项。请注意，已经写入的数据不会在事后被压缩。

默认情况下，rootfs 将在 `/etc/fstab` 中列出，如下所示：

```text
UUID=<uuid of your root file system> / btrfs defaults 0 1
```

只需将 `compress=zstd`、`compress=lzo` 或 `compress=zlib` 附加到上面的 `defaults` 中，如下所示：

```text
UUID=<uuid of your root file system> / btrfs defaults,compress=zstd 0 1
```

此更改将在重新启动后生效。

### 检查空间使用情况 <a href="#_checking_space_usage" id="_checking_space_usage"></a>

对于某些 BTRFS 配置，经典的 `df` 工具可能会输出令人困惑的值。要获得更准确的估计，请使用 `btrfs filesystem usage /PATH` 命令，例如：

```text
# btrfs fi usage /my-storage
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
