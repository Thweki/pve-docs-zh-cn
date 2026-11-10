# 7.9. 本地 ZFS 池后端 <a href="#storage_zfspool" id="storage_zfspool"></a>

存储池类型：`zfspool`

该后端允许您访问本地 ZFS 池（或此类池中的 ZFS 文件系统）。

## 7.9.1. 配置 <a href="#_configuration_6" id="_configuration_6"></a>

该后端支持通用存储属性 `content`、`nodes`、`disable`，以及以下 ZFS 特有属性：

**pool**

选择 ZFS 池/文件系统。所有分配都在该池内完成。

**blocksize**

设置 ZFS 的 blocksize 参数。

**sparse**

使用 ZFS 精简置备。稀疏卷是指预留空间不等于卷大小的卷。

**挂载点**

The mount point of the ZFS pool/filesystem. Changing this does not affect the `mountpoint` property of the dataset seen by `zfs`. Defaults to `/<pool>`.

**配置示例（`/etc/pve/storage.cfg`）**

```text
zfspool: vmdata
        pool tank/vmdata
        content rootdir,images
        sparse
```

## 7.9.2. 文件命名约定 <a href="#_file_naming_conventions_2" id="_file_naming_conventions_2"></a>

后端对 VM 镜像使用以下命名方案：

```text
vm-<VMID>-<NAME>      // normal VM images
base-<VMID>-<NAME>    // template VM image (read-only)
subvol-<VMID>-<NAME>  // subvolumes (ZFS filesystem for containers)
```

**`<VMID>`**

指定所有者 VM。

**`<NAME>`**

这可以是不含空白的任意名称（`ascii`）。后端默认使用 `disk[N]`，其中 `[N]` 会替换为一个整数，以确保名称唯一。

## 7.9.3. 存储功能 <a href="#_storage_features_5" id="_storage_features_5"></a>

就快照和克隆而言，ZFS 可能是最先进的存储类型。后端同时将 ZFS 数据集用于 VM 镜像（格式为 `raw`）和容器数据（格式为 `subvol`）。ZFS 属性会从父数据集继承，因此您可以直接在父数据集上设置默认值。

<table>
<caption>表 8. 后端 <code>zfs</code> 的存储功能</caption>





<thead>
<tr>
<th>内容类型</th>
<th>镜像格式</th>
<th>共享</th>
<th>快照</th>
<th>克隆</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images rootdir</p></td>
<td><p>raw subvol</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
</tbody>
</table>

## 7.9.4. 加密 <a href="#_encryption" id="_encryption"></a>

ZFS 支持对数据集层级结构进行加密。每个加密数据集要么是 `encryption_root`，自身存储加密属性，要么是其 `encryption_root` 的后代——详情请参阅 `zfs-load-key(8)` 手册页。

发送和接收加密数据集受到一些限制，因为某些加密参数（对称密码的初始化向量）要么需要随数据一起传输，这会破坏接收端对加密属性的继承；要么需要在目标端重新创建，这就要求以未加密形式发送数据——详情请参阅 `zfs-recv(8)` 手册页。

在 Proxmox VE 中迁移和存储复制加密数据集时，发送的数据不包含加密属性，加密状态由目标端决定。

如果要发送和接收加密的 ZFS 数据集，需要确保所有节点上所有涉及的存储均已加密。

## 7.9.5. 示例 <a href="#_examples_5" id="_examples_5"></a>

建议额外创建一个 ZFS 文件系统来存储 VM 镜像：

```text
# zfs create tank/vmdata
```

要在新分配的文件系统上启用压缩：

```text
# zfs set compression=on tank/vmdata
```

可以使用以下命令获取可用 ZFS 文件系统的列表：

```text
# pvesm scan zfs
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
