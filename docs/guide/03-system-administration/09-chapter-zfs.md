# 3.9. Linux 上的 ZFS <a href="#chapter_zfs" id="chapter_zfs"></a>

ZFS 是由 Sun Microsystems 设计的文件系统与逻辑卷管理器的结合体。从 Proxmox VE 3.4 开始，引入了 ZFS 文件系统的原生 Linux 内核移植版本，可作为可选文件系统，也可作为根文件系统的额外选择。无需手动编译 ZFS 模块——所有软件包均已包含。

使用 ZFS，可以在低成本硬件上获得最全面的企业级功能，也可以通过 SSD 缓存甚至纯 SSD 配置来构建高性能系统。ZFS 能以适中的 CPU 和内存负载以及简便的管理，取代价格高昂的硬件 RAID 卡。

**ZFS 的一般优势**

- 通过 Proxmox VE GUI 和 CLI 轻松配置和管理。
- 可靠
- 防止数据损坏
- 文件系统级数据压缩
- 快照
- 写时复制克隆
- 多种 RAID 级别：RAID0、RAID1、RAID10、RAIDZ-1、RAIDZ-2、RAIDZ-3、dRAID、dRAID2、dRAID3
- 可使用 SSD 作为缓存
- 自我修复
- 持续进行完整性检查
- 专为大容量存储而设计
- 通过网络进行异步复制
- 开源
- 加密
- …

## 3.9.1. 硬件 <a href="#hardware_2" id="hardware_2"></a>

ZFS 对内存依赖很大，因此至少需要 8GB 才能开始使用。实践中，应在硬件/预算允许的范围内尽可能多配置内存。为防止数据损坏，我们建议使用高品质的 ECC RAM。

如果使用专用的缓存和/或日志磁盘，则应使用企业级 SSD。这可以显著提高整体性能。

{% hint style="warning" %}
不要在具有自身缓存管理功能的硬件 RAID 控制器之上使用 ZFS。ZFS 需要直接与磁盘通信。使用 HBA 适配器或类似刷写为“IT”模式的 LSI 控制器更合适。
{% endhint %}

如果您尝试在 VM 内安装 Proxmox VE（嵌套虚拟化），请勿为该 VM 的磁盘使用 `virtio`，因为 ZFS 不支持它们。请改用 IDE 或 SCSI（也适用于 `virtio` SCSI 控制器类型）。

## 3.9.2. 安装为根文件系统 <a href="#installation_as_root_file_system" id="installation_as_root_file_system"></a>

使用 Proxmox VE 安装程序进行安装时，可以选择 ZFS 作为根文件系统。您需要在安装时选择 RAID 类型：

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
<tr>
<td>RAIDZ-1 <br/></td>
<td>
<p>RAID-5 的变体，采用单奇偶校验。至少需要 3 块磁盘。</p>
</td>
</tr>
<tr>
<td>RAIDZ-2 <br/></td>
<td>
<p>RAID-5 的变体，采用双奇偶校验。至少需要 4 块磁盘。</p>
</td>
</tr>
<tr>
<td>RAIDZ-3 <br/></td>
<td>
<p>RAID-5 的变体，采用三奇偶校验。至少需要 5 块磁盘。</p>
</td>
</tr>
</table>

安装程序会自动对磁盘进行分区，创建名为 `rpool` 的 ZFS 池，并将根文件系统安装在 ZFS 子卷 `rpool/ROOT/pve-1` 上。

安装程序还会创建一个名为 `rpool/data` 的子卷，用于存储 VM 镜像。为了能在 Proxmox VE 工具中使用该子卷，安装程序会在 `/etc/pve/storage.cfg` 中创建以下配置条目：

```text
zfspool: local-zfs
        pool rpool/data
        sparse
        content images,rootdir
```

安装后，您可以使用 `zpool` 命令查看 ZFS 池状态：

```text
# zpool status
  pool: rpool
 state: ONLINE
  scan: none requested
config:

        NAME        STATE     READ WRITE CKSUM
        rpool       ONLINE       0     0     0
          mirror-0  ONLINE       0     0     0
            sda2    ONLINE       0     0     0
            sdb2    ONLINE       0     0     0
          mirror-1  ONLINE       0     0     0
            sdc     ONLINE       0     0     0
            sdd     ONLINE       0     0     0

errors: No known data errors
```

`zfs` 命令用于配置和管理 ZFS 文件系统。以下命令列出安装后的所有文件系统：

```text
# zfs list
NAME               USED  AVAIL  REFER  MOUNTPOINT
rpool             4.94G  7.68T    96K  /rpool
rpool/ROOT         702M  7.68T    96K  /rpool/ROOT
rpool/ROOT/pve-1   702M  7.68T   702M  /
rpool/data          96K  7.68T    96K  /rpool/data
rpool/swap        4.25G  7.69T    64K  -
```

## 3.9.3. ZFS RAID 级别注意事项 <a href="#sysadmin_zfs_raid_considerations" id="sysadmin_zfs_raid_considerations"></a>

选择 ZFS 池的布局时，需要考虑几个因素。ZFS 池的基本构建块是虚拟设备，即 `vdev`。池中的所有 vdev 都会被均等使用，数据在它们之间进行条带化（RAID0）。有关 vdev 的更多详细信息，请查看 `zpoolconcepts(7)` 手册页。

### 性能 <a href="#sysadmin_zfs_raid_performance" id="sysadmin_zfs_raid_performance"></a>

每种 `vdev` 类型都有不同的性能表现。需要关注的两个参数是 IOPS（每秒输入/输出操作次数）以及数据写入或读取的带宽。

写入数据时，就这两个参数而言，*mirror* vdev（RAID1）的表现大致与单块磁盘相同。读取数据时，性能会随镜像中的磁盘数量线性提升。

一种常见情况是使用 4 块磁盘。将其配置为 2 个镜像 vdev（RAID10）时，在 IOPS 和带宽方面，该池的写入特性将相当于两块独立磁盘。对于读取操作，其表现则相当于 4 块独立磁盘。

任何冗余级别的 *RAIDZ* 在 IOPS 方面都大致相当于单块磁盘，但具有较高的带宽。带宽大小取决于 RAIDZ vdev 的规模和冗余级别。

*dRAID* 池的性能应与同等的 *RAIDZ* 池相当。

对于运行中的 VM，在大多数情况下，IOPS 是更重要的指标。

### 大小、空间使用情况和冗余 <a href="#sysadmin_zfs_raid_size_space_usage_redundancy" id="sysadmin_zfs_raid_size_space_usage_redundancy"></a>

由 *mirror* vdev 组成的池虽然具有最佳性能特性，但可用空间仅为所有磁盘容量的 50%。如果一个镜像 vdev 包含超过 2 块磁盘，例如三向镜像，可用空间还会更少。每个镜像至少需要一块健康磁盘，池才能保持正常运行。

由 N 块磁盘组成的 *RAIDZ* 类型 vdev，其可用空间大致为 N-P，其中 P 为 RAIDZ 级别。RAIDZ 级别表示在不丢失数据的情况下，允许发生故障的任意磁盘数量。一个特例是使用 4 块磁盘的 RAIDZ2 池。在这种情况下，由于可用空间相同，通常最好使用 2 个镜像 vdev，以获得更好的性能。

使用任何 RAIDZ 级别时，另一个重要因素是用作 VM 磁盘的 ZVOL 数据集的行为。对于每个数据块，池都需要奇偶校验数据，其大小至少为池的 `ashift` 值所定义的最小块大小。当 ashift 为 12 时，池的块大小为 4k。ZVOL 的默认块大小为 8k。因此，在 RAIDZ2 中，每写入一个 8k 数据块，都会额外写入两个 4k 奇偶校验块，即 8k \+ 4k \+ 4k \= 16k。当然，这是一种简化说明，实际情况会略有不同，因为此示例未计入元数据、压缩等因素。

检查 ZVOL 的以下属性时，可以观察到这种行为：

- `volsize`
- `refreservation`（如果池未采用精简置备）
- `used`（如果池采用精简置备且不存在快照）

```text
# zfs get volsize,refreservation,used <pool>/vm-<vmid>-disk-X
```

`volsize` 是呈现给 VM 的磁盘大小，而 `refreservation` 显示池中的预留空间，其中包括奇偶校验数据预计所需的空间。如果池采用精简置备，`refreservation` 将设置为 0。观察这种行为的另一种方法是比较 VM 内已使用的磁盘空间与 `used` 属性。请注意，快照会使该值失真。

有几种方法可以减少由此增加的空间占用：

- 增大 `volblocksize`，以提高数据与奇偶校验数据的比例
- 使用 *mirror* vdev 替代 *RAIDZ*
- 使用 `ashift=9`（块大小为 512 bytes）

`volblocksize` 属性只能在创建 ZVOL 时设置。其默认值可在存储配置中更改。执行此操作时，需要相应调整客户机；并且根据使用场景，写放大问题可能只是从 ZFS 层转移到了客户机。

创建池时使用 `ashift=9` 可能会导致性能不佳，具体取决于底层磁盘，而且此设置以后无法更改。

镜像 vdev（RAID1、RAID10）对 VM 工作负载具有良好的表现。除非您的环境有特定需求和特性，且 RAIDZ 的性能特性可以接受，否则应使用镜像 vdev。

## 3.9.4. ZFS dRAID <a href="#zfs_draid" id="zfs_draid"></a>

在 ZFS dRAID（去集群化 RAID）中，热备盘也参与 RAID。其备用容量会被预留，并在某块磁盘发生故障时用于重建。根据配置的不同，与 RAIDZ 相比，在磁盘发生故障时这可提供更快的重建速度。更多信息请参阅 OpenZFS 官方文档。[\[1\]](#note-769d32f3-1)

{% hint style="info" %}
dRAID 适用于包含超过 10-15 块磁盘的 dRAID。在大多数使用场景中，磁盘数量较少时，RAIDZ 设置应该更合适。
{% endhint %}

{% hint style="info" %}
GUI 要求比最低磁盘数多一块磁盘（即 dRAID1 需要 3 块）。它预期还会添加一块备用磁盘。
{% endhint %}

- `dRAID1` 或 `dRAID`：至少需要 2 块磁盘，在数据丢失前允许 1 块磁盘发生故障
- `dRAID2`：至少需要 3 块磁盘，在数据丢失前允许 2 块磁盘发生故障
- `dRAID3`：至少需要 4 块磁盘，在数据丢失前允许 3 块磁盘发生故障

更多信息请参阅手册页：

```text
# man zpoolconcepts
```

### 备用磁盘和数据 <a href="#spares_and_data" id="spares_and_data"></a>

`spares` 的数量告知系统应准备多少块磁盘以应对磁盘故障。默认值为 0 `spares`。没有备用磁盘，重建就不会获得任何速度优势。

`data` 定义冗余组中的设备数量。默认值为 8。但如果 `disks - parity - spares` 等于某个小于 8 的值，则使用较小的数值。一般来说，`data` 设备数量越少，IOPS 越高、压缩率越好、重同步速度越快，但定义较少的数据设备会减少池的可用存储容量。

## 3.9.5. 引导加载程序 <a href="#bootloader_2" id="bootloader_2"></a>

Proxmox VE 使用 [`proxmox-boot-tool`](13-sysboot.md#sysboot_proxmox_boot_tool) 管理引导加载程序配置。有关详细信息，请参阅 [Proxmox VE 宿主机引导加载程序](13-sysboot.md) 一章。

## 3.9.6. ZFS 管理 <a href="#zfs_administration" id="zfs_administration"></a>

本节提供一些常见任务的使用示例。ZFS 本身功能非常强大，并提供了许多选项。管理 ZFS 的主要命令是 `zfs` 和 `zpool`。这两个命令都配有详尽的手册页，可以使用以下命令阅读：

```text
# man zpool
# man zfs
```

### 创建新的 zpool <a href="#sysadmin_zfs_create_new_zpool" id="sysadmin_zfs_create_new_zpool"></a>

要创建新池，至少需要一块磁盘。`ashift` 的扇区大小（2 的 `ashift` 次幂）应与底层磁盘的扇区大小相同或更大。

```text
# zpool create -f -o ashift=12 <pool> <device>
```

{% hint style="success" %}
池名称必须遵循以下规则：

- 以字母（a-z 或 A-Z）开头
- 只能包含字母数字、`-`、`_`、`.`、`:` 或 \` \`（空格）字符
- **不得**以 `mirror`、`raidz`、`draid` 或 `spare` 之一开头
- 不得为 `log`
{% endhint %}

要启用压缩（请参阅 [ZFS 中的压缩](#zfs_compression) 一节）：

```text
# zfs set compression=lz4 <pool>
```

### 使用 RAID-0 创建新池 <a href="#sysadmin_zfs_create_new_zpool_raid0" id="sysadmin_zfs_create_new_zpool_raid0"></a>

最少 1 块磁盘

```text
# zpool create -f -o ashift=12 <pool> <device1> <device2>
```

### 使用 RAID-1 创建新池 <a href="#sysadmin_zfs_create_new_zpool_raid1" id="sysadmin_zfs_create_new_zpool_raid1"></a>

最少 2 块磁盘

```text
# zpool create -f -o ashift=12 <pool> mirror <device1> <device2>
```

### 使用 RAID-10 创建新池 <a href="#sysadmin_zfs_create_new_zpool_raid10" id="sysadmin_zfs_create_new_zpool_raid10"></a>

最少 4 块磁盘

```text
# zpool create -f -o ashift=12 <pool> mirror <device1> <device2> mirror <device3> <device4>
```

### 使用 RAIDZ-1 创建新池 <a href="#sysadmin_zfs_create_new_zpool_raidz1" id="sysadmin_zfs_create_new_zpool_raidz1"></a>

最少 3 块磁盘

```text
# zpool create -f -o ashift=12 <pool> raidz1 <device1> <device2> <device3>
```

### 使用 RAIDZ-2 创建新池 <a href="#create_a_new_pool_with_raidz_2" id="create_a_new_pool_with_raidz_2"></a>

最少 4 块磁盘

```text
# zpool create -f -o ashift=12 <pool> raidz2 <device1> <device2> <device3> <device4>
```

请阅读 [ZFS RAID 级别注意事项](#sysadmin_zfs_raid_considerations) 一节，以便在设置池之前对 IOPS 和带宽预期进行粗略估算，尤其是在希望使用 RAID-Z 模式时。

### 扩展 RAIDZ-N <a href="#sysadmin_zfs_extend_raidz" id="sysadmin_zfs_extend_raidz"></a>

{% hint style="info" %}
此功能仅适用于 Proxmox VE 9（ZFS 2.3.3）及更高版本。
{% endhint %}

假设你有一个现有的 `<pool>`，其中包含一个 RAIDZ-N `<raidzN-M>` vdev，则可以使用以下语法添加新的物理磁盘 `<device>`：

```text
zpool attach <pool> <raidzN-M> <device>
```

你可以通过运行 `zpool status <pool>` 验证总体是否成功，并通过运行 `zpool list <pool> -v` 获取所有已连接磁盘的详细输出。要检查池的新容量，请运行 `zfs list <pool>`。

### 创建带有缓存（L2ARC）的新池 <a href="#sysadmin_zfs_create_new_zpool_with_cache" id="sysadmin_zfs_create_new_zpool_with_cache"></a>

可以使用专用设备或分区作为二级缓存来提高性能。此类缓存设备尤其有助于读取大多为静态的数据时的随机读取工作负载。由于它充当实际存储与内存中的 ARC 之间的附加缓存层，因此在因内存限制而必须缩减 ARC 时，它也能提供帮助。

**创建带有磁盘缓存的 ZFS 池**

```text
# zpool create -f -o ashift=12 <pool> <device> cache <cache-device>
```

这里只使用了一个 `<device>` 和一个 `<cache-device>`，但可以使用更多设备，如 [创建 RAID 池](#sysadmin_zfs_create_new_zpool_raid0) 中所示。

请注意，缓存设备没有镜像或 RAID 模式，它们都只是简单累加。

如果任何缓存设备在读取时产生错误，ZFS 会透明地将该请求转到底层存储层。

### 创建带有日志（ZIL）的新池 <a href="#sysadmin_zfs_create_new_zpool_with_log" id="sysadmin_zfs_create_new_zpool_with_log"></a>

可以使用专用驱动器或分区作为 ZFS 意图日志（ZIL），它主要用于提供安全的同步事务，因此常用于数据库或其他更频繁发出 `fsync` 操作的程序等性能关键路径。

池默认用作 ZIL 位置。将 ZIL I/O 负载转移到独立设备有助于降低事务延迟，同时减轻主池负担，从而提高整体性能。

对于直接或通过分区用作日志设备的磁盘，建议：

- 使用具有断电保护功能的快速 SSD，因为这类设备的提交延迟要低得多。
- 为分区（或整个设备）至少分配几 GB，但使用超过已安装内存一半的容量不会带来任何实际优势。

**创建带有独立日志设备的 ZFS 池**

```text
# zpool create -f -o ashift=12 <pool> <device> log <log-device>
```

在上面的示例中，使用了一个 `<device>` 和一个 `<log-device>`，但你也可以将其与其他 RAID 变体结合使用，如 [创建 RAID 池](#sysadmin_zfs_create_new_zpool_raid0) 一节所述。

你还可以将日志设备镜像到多个设备，这主要用于确保单个日志设备发生故障时性能不会立即下降。

如果所有日志设备都发生故障，则会再次使用 ZFS 主池本身，直到更换日志设备。

### 向现有池添加缓存和日志 <a href="#sysadmin_zfs_add_cache_and_log_dev" id="sysadmin_zfs_add_cache_and_log_dev"></a>

如果你的池没有缓存和日志，仍然可以随时添加两者，或只添加其中之一。

例如，假设你有一块不错的、具有断电保护功能的企业级 SSD，希望用它来提高池的整体性能。

由于日志设备的最大大小应约为已安装物理内存大小的一半，这意味着 ZIL 很可能只占用 SSD 中相对较小的一部分，剩余空间可以用作缓存。

首先，你必须使用 `parted` 或 `gdisk` 在 SSD 上创建两个 GPT 分区。

然后即可将它们添加到池中：

**将独立日志设备和二级缓存都添加到现有池**

```text
# zpool add -f <pool> log <device-part1> cache <device-part2>
```

只需将 `<pool>`、`<device-part1>` 和 `<device-part2>` 替换为池名称以及两个指向分区的 `/dev/disk/by-id/` 路径。

你也可以分别添加 ZIL 和缓存。

**向现有 ZFS 池添加日志设备**

```text
# zpool add <pool> log <log-device>
```

### 更换故障设备 <a href="#sysadmin_zfs_change_failed_dev" id="sysadmin_zfs_change_failed_dev"></a>

```text
# zpool replace -f <pool> <old-device> <new-device>
```

**更换故障的可引导设备**

根据 Proxmox VE 的安装方式，它可能使用 `systemd-boot`，或通过 `proxmox-boot-tool` [\[2\]](#note-769d32f3-2) 使用 GRUB，也可能直接使用 GRUB 作为引导加载程序（请参阅 [宿主机引导加载程序](13-sysboot.md)）。你可以通过运行以下命令进行检查：

```text
# proxmox-boot-tool status
```

复制分区表、重新生成 GUID 和替换 ZFS 分区的最初步骤相同。要使系统能够从新磁盘引导，需要根据所使用的引导加载程序执行不同的步骤。

```text
# sgdisk <healthy bootable device> -R <new device>
# sgdisk -G <new device>
# zpool replace -f <pool> <old zfs partition> <new zfs partition>
```

{% hint style="info" %}
使用 `zpool status -v` 命令监视新磁盘的重同步进程进度。
{% endhint %}

**使用 `proxmox-boot-tool`：**

```text
# proxmox-boot-tool format <new disk's ESP>
# proxmox-boot-tool init <new disk's ESP> [grub]
```

{% hint style="info" %}
`ESP` 表示 EFI 系统分区。自 5.4 版起，使用 Proxmox VE 安装程序时，该分区会在可引导磁盘上设置为第 2 号分区。有关详细信息，请参阅 [设置用作同步 ESP 的新分区](13-sysboot.md#sysboot_proxmox_boot_setup)。
{% endhint %}

{% hint style="info" %}
务必将 *grub* 作为模式传递给 `proxmox-boot-tool init`，如果 `proxmox-boot-tool status` 表明当前磁盘使用 GRUB，尤其是在启用了安全启动时！
{% endhint %}

**直接使用 GRUB：**

```text
# grub-install <new disk>
```

{% hint style="info" %}
只有使用 Proxmox VE 6.3 或更早版本安装且尚未手动迁移为使用 `proxmox-boot-tool` 的系统才直接使用 GRUB。
{% endhint %}

## 3.9.7. 配置电子邮件通知 <a href="#configure_e_mail_notification" id="configure_e_mail_notification"></a>

ZFS 附带一个事件守护进程 `ZED`，用于监视 ZFS 内核模块生成的事件。该守护进程还可以针对池错误等 ZFS 事件发送电子邮件。较新的 ZFS 软件包将该守护进程放在独立的 `zfs-zed` 软件包中，在 Proxmox VE 中默认应已安装该软件包。

可以使用你喜欢的编辑器通过文件 `/etc/zfs/zed.d/zed.rc` 配置该守护进程。电子邮件通知所需的设置为 `ZED_EMAIL_ADDR`，其默认值为 `root`。

```text
ZED_EMAIL_ADDR="root"
```

请注意，Proxmox VE 会将发送到 `root` 的邮件转发到为 root 用户配置的电子邮件地址。

## 3.9.8. 限制 ZFS 内存使用量 <a href="#sysadmin_zfs_limit_memory_usage" id="sysadmin_zfs_limit_memory_usage"></a>

默认情况下，ZFS 使用宿主机内存的 *10 %*，上限为 `16 GiB`，用于自适应替换缓存（**A**daptive **R**eplacement **C**ache，ARC）。安装期间会将此值写入 `/etc/modprobe.d/zfs.conf`。有关 ZFS 内核模块参数的更多信息，请参阅手册 `man 4 zfs`。

在 Proxmox VE 8.1 之前，安装期间不会设置 ARC 使用上限，而是采用 ZFS 的默认值：从 ZFS 2.3.0 开始为 62.5%，更早版本为 50%。对于早于 Proxmox VE 8.1 的现有安装，必须手动执行下述步骤才能降低使用上限。

为 ARC 分配足够的内存对于 I/O 性能至关重要，因此请谨慎缩减。一般经验法则是至少分配 `2 GiB Base + 1
GiB/TiB-Storage`。例如，如果池有 `8 TiB` 的可用存储空间，则应为 ARC 使用 `10 GiB` 的内存。

ZFS 还会强制执行最小值 `64 MiB`。

通过直接写入 `zfs_arc_max` 模块参数，可以更改本次启动的 ARC 使用上限（重启后此更改会再次重置）：

```text
 echo "$[10 * 1024*1024*1024]" >/sys/module/zfs/parameters/zfs_arc_max
```

要**永久更改** ARC 限制，请将以下行添加到 `/etc/modprobe.d/zfs.conf`（如果已存在，则进行修改）：

```text
options zfs zfs_arc_max=8589934592
```

此示例设置将使用量限制为 8 GiB（*8 \* 230*）。

{% hint style="warning" %}
如果所需的 `zfs_arc_max` 值小于或等于 `zfs_arc_min`（默认为系统内存的 1/32），则会忽略 `zfs_arc_max`，除非同时将 `zfs_arc_min` 设为不超过 `zfs_arc_max - 1`。
{% endhint %}

```text
echo "$[8 * 1024*1024*1024 - 1]" >/sys/module/zfs/parameters/zfs_arc_min
echo "$[8 * 1024*1024*1024]" >/sys/module/zfs/parameters/zfs_arc_max
```

此示例设置将总内存超过 256 GiB 的系统上的使用量（临时）限制为 8 GiB（*8 \* 230*）；在这类系统上，仅设置 `zfs_arc_max` 不会生效。

{% hint style="warning" %}
如果根文件系统是 ZFS，则每次此值更改后都必须更新 initramfs：

```text
# update-initramfs -u -k all
```

你**必须重启**才能激活这些更改。
{% endhint %}

## 3.9.9. ZFS 上的 SWAP <a href="#zfs_swap" id="zfs_swap"></a>

在 zvol 上创建的交换空间可能会引发一些问题，例如阻塞服务器或产生较高的 I/O 负载，这些问题通常在开始向外部存储进行备份时出现。

我们强烈建议使用足够的内存，以便通常不会遇到内存不足的情况。如果需要或想要添加交换空间，最好在物理磁盘上创建一个分区并将其用作交换设备。可以在安装程序的高级选项中为此留出一些空闲空间。此外，还可以降低“swappiness”值。对于服务器，10 是一个合适的值：

```text
# sysctl -w vm.swappiness=10
```

要使 swappiness 设置持久生效，请使用所选编辑器创建新文件 `/etc/sysctl.d/99-swappiness.conf`，并添加以下行：

```text
vm.swappiness = 10
```

<table>
<caption>表 1. Linux 内核 <code>swappiness</code> 参数值</caption>


<thead>
<tr>
<th>值</th>
<th>策略</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>vm.swappiness = 0</p></td>
<td><p>内核仅会为避免<em>内存不足</em>情况而进行交换</p></td>
</tr>
<tr>
<td><p>vm.swappiness = 1</p></td>
<td><p>在不完全禁用交换的情况下，将交换量降至最低。</p></td>
</tr>
<tr>
<td><p>vm.swappiness = 10</p></td>
<td><p>当系统具有足够内存时，有时会建议使用此值来提高性能。</p></td>
</tr>
<tr>
<td><p>vm.swappiness = 60</p></td>
<td><p>默认值。</p></td>
</tr>
<tr>
<td><p>vm.swappiness = 100</p></td>
<td><p>内核会积极地进行交换。</p></td>
</tr>
</tbody>
</table>

## 3.9.10. 加密的 ZFS 数据集 <a href="#zfs_encryption" id="zfs_encryption"></a>

{% hint style="warning" %}
Proxmox VE 中的原生 ZFS 加密是实验性功能。已知的限制和问题包括加密数据集的复制 [\[3\]](#note-769d32f3-3)，以及使用快照或 ZVOL 时的校验和错误。[\[4\]](#note-769d32f3-4)
{% endhint %}

ZFS on Linux 0.8.0 版本引入了对数据集原生加密的支持。从早期 ZFS on Linux 版本升级后，可以为每个池启用加密功能：

```text
# zpool get feature@encryption tank
NAME  PROPERTY            VALUE            SOURCE
tank  feature@encryption  disabled         local

# zpool set feature@encryption=enabled

# zpool get feature@encryption tank
NAME  PROPERTY            VALUE            SOURCE
tank  feature@encryption  enabled         local
```

{% hint style="warning" %}
目前不支持使用 GRUB 从包含加密数据集的池启动，并且对启动时自动解锁加密数据集的支持也很有限。不支持加密的旧版 ZFS 将无法解密存储的数据。
{% endhint %}

{% hint style="info" %}
建议在启动后手动解锁存储数据集，或者编写自定义单元，将启动时解锁所需的密钥材料传递给 `zfs load-key`。
{% endhint %}

{% hint style="warning" %}
在为生产数据启用加密之前，请建立并测试备份流程。如果相关的密钥材料/密码短语/密钥文件丢失，将无法再访问加密数据。
{% endhint %}

创建数据集/zvol 时需要设置加密，默认情况下，子数据集将继承加密设置。例如，要创建加密数据集 `tank/encrypted_data` 并在 Proxmox VE 中将其配置为存储，请运行以下命令：

```text
# zfs create -o encryption=on -o keyformat=passphrase tank/encrypted_data
Enter passphrase:
Re-enter passphrase:

# pvesm add zfspool encrypted_zfs -pool tank/encrypted_data
```

在此存储上创建的所有客户机卷/磁盘都将使用父数据集的共享密钥材料进行加密。

要实际使用该存储，需要加载相关的密钥材料并挂载数据集。可以通过以下命令一步完成：

```text
# zfs mount -l tank/encrypted_data
Enter passphrase for 'tank/encrypted_data':
```

也可以在创建时设置 `keylocation` 和 `keyformat` 属性，或对现有数据集使用 `zfs change-key` 设置这些属性，从而使用（随机）密钥文件，而不是提示输入密码短语：

```text
# dd if=/dev/urandom of=/path/to/keyfile bs=32 count=1

# zfs change-key -o keyformat=raw -o keylocation=file:///path/to/keyfile tank/encrypted_data
```

{% hint style="warning" %}
使用密钥文件时，需要特别注意保护密钥文件，防止未经授权的访问或意外丢失。没有密钥文件，就无法访问明文数据！
{% endhint %}

在加密数据集下创建的客户机卷，其 `encryptionroot` 属性也会相应设置。每个 encryptionroot 只需加载一次密钥材料，其下的所有加密数据集便都可以使用。

有关更多详情和高级用法，请参阅 `encryptionroot`、`encryption`、`keylocation`、`keyformat` 和 `keystatus` 属性，`zfs load-key`、`zfs unload-key` 和 `zfs
change-key` 命令，以及 `Encryption` 一节（位于 `man zfs` 中）。

## 3.9.11. ZFS 中的压缩 <a href="#zfs_compression" id="zfs_compression"></a>

在数据集上启用压缩后，ZFS 会尝试在写入前压缩所有**新**数据块，并在读取时将其解压缩。已有数据不会被追溯压缩。

可以使用以下命令启用压缩：

```text
# zfs set compression=<algorithm> <dataset>
```

我们建议使用 `lz4` 算法，因为它带来的 CPU 开销非常小。还可以使用 `lzjb` 和 `gzip-N` 等其他算法，其中 `N` 是从 `1`（最快）到 `9`（最佳压缩比）的整数。根据算法和数据的可压缩程度，启用压缩甚至可以提高 I/O 性能。

可以随时使用以下命令禁用压缩：

```text
# zfs set compression=off <dataset>
```

同样，此更改只会影响新数据块。

## 3.9.12. ZFS 特殊设备 <a href="#sysadmin_zfs_special_device" id="sysadmin_zfs_special_device"></a>

自 0.8.0 版起，ZFS 支持`special`设备。池中的`special`设备用于存储元数据、去重表，以及可选的小文件块。

对于由低速机械硬盘组成且元数据变更频繁的池，`special`设备可以提高其速度。例如，涉及创建、更新或删除大量文件的工作负载将受益于`special`设备。还可以将 ZFS 数据集配置为把整个小文件存储在`special`设备上，从而进一步提高性能。`special`设备应使用高速 SSD。

{% hint style="warning" %}
`special`设备的冗余级别应与池一致，因为`special`设备是整个池的单点故障。
{% endhint %}

{% hint style="warning" %}
向池添加`special`设备的操作无法撤销！
{% endhint %}

**创建带有`special`设备和 RAID-1 的池：**

```text
# zpool create -f -o ashift=12 <pool> mirror <device1> <device2> special mirror <device3> <device4>
```

**向具有 RAID-1 的现有池添加`special`设备：**

```text
# zpool add <pool> special mirror <device1> <device2>
```

ZFS 数据集公开 `special_small_blocks=<size>` 属性。`size` 可以设为 `0`，以禁止将小文件块存储在`special`设备上；也可以设为 `512B` 到 `1M` 范围内 2 的幂。设置该属性后，小于 `size` 的新文件块将分配到`special`设备上。

{% hint style="warning" %}
如果 `special_small_blocks` 的值大于或等于数据集的 `recordsize`（默认值为 `128K`），则**所有**数据都将写入`special`设备，因此请务必小心！
{% endhint %}

在池上设置 `special_small_blocks` 属性将更改所有子 ZFS 数据集的该属性默认值（例如，池中的所有容器都将启用小文件块存储）。

**在整个池中为所有小于 4K 块的文件启用小文件块存储：**

```text
# zfs set special_small_blocks=4K <pool>
```

**为单个数据集启用小文件块存储：**

```text
# zfs set special_small_blocks=4K <pool>/<filesystem>
```

**为单个数据集禁用小型文件块存储：**

```text
# zfs set special_small_blocks=0 <pool>/<filesystem>
```

## 3.9.13. ZFS 池功能 <a href="#sysadmin_zfs_features" id="sysadmin_zfs_features"></a>

ZFS 磁盘格式的更改仅在主版本变更时进行，并通过**功能**来指定。所有功能以及总体机制均在 `zpool-features(5)` 手册页中有详细说明。

由于启用新功能可能导致旧版 ZFS 无法导入池，因此需要管理员主动在池上运行 `zpool upgrade` 来完成此操作（请参阅 `zpool-upgrade(8)` 手册页）。

除非需要使用其中某项新功能，否则启用它们没有任何好处。

事实上，启用新功能有一些缺点：

- 对于根文件系统位于 ZFS 上且仍使用 GRUB 启动的系统，如果 rpool 上激活了新功能，由于 GRUB 中的 ZFS 实现不兼容，系统将无法启动。
- 使用仍附带旧 ZFS 模块的旧内核启动时，系统将无法导入任何已升级的池。
- 同样，也无法通过启动旧版 Proxmox VE ISO 来修复无法启动的系统。

{% hint style="warning" %}
如果系统仍使用 GRUB 启动，请**不要**升级 rpool，否则系统将无法启动。这包括 Proxmox VE 5.4 之前安装的系统，以及使用传统 BIOS 启动的系统（请参阅[如何确定引导加载程序](13-sysboot.md#sysboot_determine_bootloader_used)）。
{% endhint %}

**为 ZFS 池启用新功能：**

```text
# zpool upgrade <pool>
```

## 注释

### 注释 1 <a href="#note-769d32f3-1" id="note-769d32f3-1"></a>

OpenZFS dRAID [https://openzfs.github.io/openzfs-docs/Basic%20Concepts/dRAID%20Howto.html](https://openzfs.github.io/openzfs-docs/Basic%20Concepts/dRAID%20Howto.html)

### 注释 2 <a href="#note-769d32f3-2" id="note-769d32f3-2"></a>

使用 Proxmox VE 6.4 或更高版本安装的系统，以及使用 Proxmox VE 5.4 或更高版本安装的 EFI 系统

### 注释 3 <a href="#note-769d32f3-3" id="note-769d32f3-3"></a>

[https://bugzilla.proxmox.com/show\_bug.cgi?id\=2350](https://bugzilla.proxmox.com/show_bug.cgi?id=2350)

### 注释 4 <a href="#note-769d32f3-4" id="note-769d32f3-4"></a>

[https://github.com/openzfs/zfs/issues/11688](https://github.com/openzfs/zfs/issues/11688)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
