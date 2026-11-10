# 7.11. LVM thin 后端 <a href="#storage_lvmthin" id="storage_lvmthin"></a>

存储池类型：`lvmthin`

LVM 通常在创建卷时分配块。而 LVM thin 池则在写入块时才分配块。这种行为称为精简置备，因为卷可以远大于实际可用的物理空间。

可以使用常规的 LVM 命令行工具管理和创建 LVM thin 池（详情请参阅 `man lvmthin`）。假设已经有一个名为 `pve` 的 LVM 卷组，以下命令将创建一个名为 `data` 的新 LVM thin 池（大小为 100G）：

```text
lvcreate -L 100G -n data pve
lvconvert --type thin-pool pve/data
```

## 7.11.1. 配置 <a href="#_configuration_7" id="_configuration_7"></a>

LVM thin 后端支持通用存储属性 `content`、`nodes`、`disable`，以及以下 LVM 特定属性：

**`vgname`**

LVM 卷组名称。必须指向一个现有的卷组。

**`thinpool`**

LVM thin 池的名称。

**配置示例（`/etc/pve/storage.cfg`）**

```text
lvmthin: local-lvm
        thinpool data
        vgname pve
        content rootdir,images
```

## 7.11.2. 文件命名约定 <a href="#_file_naming_conventions_4" id="_file_naming_conventions_4"></a>

该后端基本上使用与 ZFS 池后端相同的命名约定。

```text
vm-<VMID>-<NAME>      // normal VM images
```

## 7.11.3. 存储功能 <a href="#_storage_features_7" id="_storage_features_7"></a>

LVM thin 是块存储，但能高效地全面支持快照和克隆。新卷会自动用零初始化。

必须指出，LVM thin 池不能跨多个节点共享，因此只能将其用作本地存储。

<table>
<caption>表 10. 后端 <code>lvmthin</code> 的存储功能</caption>





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
<td><p>raw</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
</tbody>
</table>

## 7.11.4. 示例 <a href="#_examples_7" id="_examples_7"></a>

可以使用以下命令获取卷组 `pve` 上可用的 LVM thin 池列表：

```text
# pvesm scan lvmthin pve
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
