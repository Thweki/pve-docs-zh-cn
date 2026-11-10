# 7.5. 目录后端 <a href="#storage_directory" id="storage_directory"></a>

存储池类型：`dir`

Proxmox VE 可以使用本地目录或本地挂载的共享目录进行存储。目录是一种文件级存储，因此你可以存储任何内容类型，例如虚拟磁盘镜像、容器、模板、ISO 镜像或备份文件。

{% hint style="info" %}
你可以通过标准 Linux `/etc/fstab` 挂载其他存储，然后为该挂载点定义一个目录存储。通过这种方式，可以使用 Linux 支持的任何文件系统。
{% endhint %}

此后端仅假定底层目录兼容 POSIX，别无其他要求。这意味着你无法在存储级别创建快照。但使用 `qcow2` 文件格式的 VM 镜像有一种变通方法，因为该格式内部支持快照。

{% hint style="success" %}
某些存储类型不支持 `O_DIRECT`，因此无法在此类存储上使用缓存模式 `none`。只需改用缓存模式 `writeback` 即可。
{% endhint %}

我们使用预定义的目录布局，将不同的内容类型存储到不同的子目录中。所有文件级存储后端都使用此布局。

<table>
<caption>表 3. 目录布局</caption>


<thead>
<tr>
<th>内容类型</th>
<th>子目录</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>VM 镜像</p></td>
<td><p><code>images/&lt;VMID&gt;/</code></p></td>
</tr>
<tr>
<td><p>ISO 镜像</p></td>
<td><p><code>template/iso/</code></p></td>
</tr>
<tr>
<td><p>容器模板</p></td>
<td><p><code>template/cache/</code></p></td>
</tr>
<tr>
<td><p>备份文件</p></td>
<td><p><code>dump/</code></p></td>
</tr>
<tr>
<td><p>片段</p></td>
<td><p><code>snippets/</code></p></td>
</tr>
<tr>
<td><p>导入</p></td>
<td><p><code>import/</code></p></td>
</tr>
</tbody>
</table>

## 7.5.1. 配置 <a href="#configuration_2" id="configuration_2"></a>

此后端支持所有通用存储属性，并增加了两个附加属性。`path` 属性用于指定目录。该目录必须是绝对文件系统路径。

可选的 `content-dirs` 属性允许更改默认布局。它由逗号分隔的标识符列表组成，格式如下：

```text
vtype=path
```

其中，`vtype` 是该存储允许的一种内容类型，`path` 是相对于该存储挂载点的路径。

**配置示例（`/etc/pve/storage.cfg`）**

```text
dir: backup
        path /mnt/backup
        content backup
        prune-backups keep-last=7
        max-protected-backups 3
        content-dirs backup=custom/backup/dir
```

上述配置定义了一个名为 `backup` 的存储池。该池可用于为每个 VM 存储最多 7 个常规备份（`keep-last=7`）和 3 个受保护备份。备份文件的实际路径为 `/mnt/backup/custom/backup/dir/...`。

## 7.5.2. 文件命名约定 <a href="#file_naming_conventions" id="file_naming_conventions"></a>

此后端为 VM 镜像使用明确定义的命名方案：

```text
vm-<VMID>-<NAME>.<FORMAT>
```

**`<VMID>`**

指定所有者 VM。

**`<NAME>`**

这可以是不含空白字符的任意名称（`ascii`）。后端默认使用 `disk-[N]`，其中 `[N]` 会被替换为一个整数，以使名称唯一。

**`<FORMAT>`**

指定镜像格式（`raw|qcow2|vmdk`）。

创建 VM 模板时，所有 VM 镜像都会被重命名，以表明它们现在是只读的，并且可以用作克隆的基础镜像：

```text
base-<VMID>-<NAME>.<FORMAT>
```

{% hint style="info" %}
此类基础镜像用于生成克隆镜像。因此，必须确保这些文件为只读且永远不会被修改。后端会将访问模式更改为 `0444`，并在存储支持的情况下设置不可变标志（`chattr +i`）。
{% endhint %}

## 7.5.3. 存储功能 <a href="#storage_features" id="storage_features"></a>

如上所述，大多数文件系统本身并不支持快照。为解决此问题，此后端能够使用 `qcow2` 的内部快照功能。

克隆也是如此。后端使用 `qcow2` 的基础镜像功能来创建克隆。

<table>
<caption>表 4. 后端 <code>dir</code> 的存储功能</caption>





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
<td><p>images rootdir vztmpl iso backup snippets</p></td>
<td><p>raw qcow2 vmdk subvol</p></td>
<td><p>否</p></td>
<td><p>qcow2</p></td>
<td><p>qcow2</p></td>
</tr>
</tbody>
</table>

## 7.5.4. 示例 <a href="#examples_2" id="examples_2"></a>

请使用以下命令在存储 `local` 上分配一个 4GB 镜像：

```text
# pvesm alloc local 100 vm-100-disk10.raw 4G
Formatting '/var/lib/vz/images/100/vm-100-disk10.raw', fmt=raw size=4294967296
successfully created 'local:100/vm-100-disk10.raw'
```

{% hint style="info" %}
镜像名称必须符合上述命名约定。
{% endhint %}

实际的文件系统路径可通过以下命令查看：

```text
# pvesm path local:100/vm-100-disk10.raw
/var/lib/vz/images/100/vm-100-disk10.raw
```

可以通过以下命令删除镜像：

```text
# pvesm free local:100/vm-100-disk10.raw
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
