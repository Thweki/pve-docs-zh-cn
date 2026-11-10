# 7.10. LVM 后端 <a href="#storage_lvm" id="storage_lvm"></a>

存储池类型：`lvm`

LVM 是位于硬盘和分区之上的轻量级软件层。它可用于将可用磁盘空间划分为更小的逻辑卷。

另一种用例是在大型 iSCSI LUN（逻辑单元号）或通过光纤通道连接的 SAN（存储区域网络）之上部署 LVM。这样，您就可以轻松管理 iSCSI LUN 上的空间；否则这将无法实现，因为 iSCSI 规范未定义用于空间分配的管理接口。

## 7.10.1. 配置 <a href="#pvesm_lvm_config" id="pvesm_lvm_config"></a>

LVM 后端支持通用存储属性 `content`、`nodes`、`disable`，以及以下 LVM 特定属性：

**`vgname`**

LVM 卷组名称。必须指向一个现有的卷组。

**`base`**

基础卷。在访问存储之前，会自动激活此卷。当 LVM 卷组位于远程 iSCSI 服务器上时，这尤其有用。

**`saferemove`**

在 Web 界面中称为“擦除已删除的卷”（Wipe Removed Volumes）。删除 LV 时将数据清零。删除卷时，这可确保所有数据都被擦除，之后创建的其他 LV（恰好分配到相同物理区域）无法访问这些数据。这是一项开销很大的操作，但在某些环境中，可能需要将其作为一项安全措施。

支持“写零”操作的存储设备将使用 `blkdiscard` 将块清零。否则，将改用 `cstream`。

**`saferemove-stepsize`**

擦除步长，单位为 MiB（`blkdiscard -p` 参数值），上限为底层存储支持的最大步长。默认最高为 32 MiB（最大值）。

**`saferemove_throughput`**

擦除吞吐量（`cstream -t` 参数值），默认最高为 10 MiB/s。

**`snapshot-as-volume-chain`**

设置此标志可为使用卷后备链的 LVM 上的虚拟机启用快照支持。启用此设置后，拍摄快照会以快照名称保存当前状态，并启动一个以该快照为后备的新卷。

基于快照的卷将其父快照卷引用为后备卷，并且仅记录与该后备卷的差异。目前，快照卷是厚置备的 LVM 逻辑卷。

这种设计避免了原生 LVM 快照的问题，例如显著的输入/输出（I/O）性能损失，以及预分配空间耗尽时出现的意外危险行为。

卷链快照为任何支持块存储的存储系统提供与厂商无关的快照支持。这包括 iSCSI 和通过光纤通道连接的 SAN。

请注意，尽管此功能依赖 qcow2，但它仅使用 qcow2 在后备链中对多个卷进行分层的能力，而不使用 qcow2 的快照功能。快照功能由 PVE 存储系统管理。

启用或禁用此标志仅影响新创建的虚拟磁盘卷。

为了高效支持 `snapshot-as-volume-chain`，后备存储必须支持精简置备和 discard。在 PVE 端，每个快照都会显示为占用完整的卷大小，但如果满足这些要求，其在底层存储上的实际空间占用会更小。

{% hint style="warning" %}
卷链快照目前在 Proxmox VE 中属于**技术预览**。
{% endhint %}

**配置示例（`/etc/pve/storage.cfg`）**

```text
lvm: myspace
        vgname myspace
        content rootdir,images
```

## 7.10.2. 文件命名约定 <a href="#_file_naming_conventions_3" id="_file_naming_conventions_3"></a>

该后端基本上使用与 ZFS 池后端相同的命名约定。

```text
vm-<VMID>-<NAME>      // normal VM images
```

## 7.10.3. 存储功能 <a href="#_storage_features_6" id="_storage_features_6"></a>

LVM 是典型的块存储系统。遗憾的是，常规 LVM 快照效率低下，因为在快照处于活动状态时，它们会干扰整个卷组内的所有写操作，导致 I/O 性能显著下降。这就是 LVM 不支持链接克隆的原因，也是 Proxmox VE 增加卷链快照支持的原因。此功能通过存储插件管理快照卷，并使用 qcow2 将各个独立卷分层组成后备链。这会创建向客户机公开的单一磁盘状态。

LVM 的一个优点是可以与共享存储配合使用，例如 iSCSI LUN。如果在配置中将存储标记为共享，后端会实现适当的集群范围锁定。

{% hint style="success" %}
对于非共享的本地存储，可以使用 LVM-thin 后端。它支持快照和链接克隆。
{% endhint %}

<table>
<caption>表 9. 后端 <code>lvm</code> 的存储功能</caption>






<thead>
<tr>
<th>内容类型</th>
<th>镜像格式</th>
<th>共享</th>
<th>快照</th>
<th>完整克隆</th>
<th>链接克隆</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images rootdir</p></td>
<td><p>raw, qcow2<sup>1</sup></p></td>
<td><p>可行</p></td>
<td><p>是<sup>1</sup></p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
</tbody>
</table>

1：自 Proxmox VE 9 起，VM 已支持卷链快照，详情请参阅“[LVM 配置](#pvesm_lvm_config)”一节。

## 7.10.4. 示例 <a href="#_examples_6" id="_examples_6"></a>

可以使用以下命令获取可用 LVM 卷组的列表：

```text
# pvesm scan lvm
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
