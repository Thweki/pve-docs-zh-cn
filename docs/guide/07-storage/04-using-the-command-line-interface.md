# 7.4. 使用命令行界面 <a href="#_using_the_command_line_interface" id="_using_the_command_line_interface"></a>

建议你熟悉存储池和卷标识符背后的概念，但在实际使用中，并不强制你在命令行上执行任何此类底层操作。通常，卷的分配和删除由 VM 和容器管理工具完成。

尽管如此，仍有一个名为 `pvesm` 的命令行工具（“Proxmox VE Storage Manager”），它能够执行常见的存储管理任务。

## 7.4.1. 示例 <a href="#_examples" id="_examples"></a>

添加存储池

```text
pvesm add <TYPE> <STORAGE_ID> <OPTIONS>
pvesm add dir <STORAGE_ID> --path <PATH>
pvesm add nfs <STORAGE_ID> --path <PATH> --server <SERVER> --export <EXPORT>
pvesm add lvm <STORAGE_ID> --vgname <VGNAME>
pvesm add iscsi <STORAGE_ID> --portal <HOST[:PORT]> --target <TARGET>
```

禁用存储池

```text
pvesm set <STORAGE_ID> --disable 1
```

启用存储池

```text
pvesm set <STORAGE_ID> --disable 0
```

更改/设置存储选项

```text
pvesm set <STORAGE_ID> <OPTIONS>
pvesm set <STORAGE_ID> --shared 1
pvesm set local --format qcow2
pvesm set <STORAGE_ID> --content iso
```

删除存储池。此操作不会删除任何数据，也不会断开连接或卸载任何内容。它仅删除存储配置。

```text
pvesm remove <STORAGE_ID>
```

分配卷

```text
pvesm alloc <STORAGE_ID> <VMID> <name> <size> [--format <raw|qcow2>]
```

在本地存储中分配一个 4G 的卷。如果将空字符串作为 `<name>` 传入，则会自动生成名称。

```text
pvesm alloc local <VMID> '' 4G
```

释放卷

```text
pvesm free <VOLUME_ID>
```

{% hint style="warning" %}
此操作确实会销毁所有卷数据。
{% endhint %}

列出存储状态

```text
pvesm status
```

列出存储内容

```text
pvesm list <STORAGE_ID> [--vmid <VMID>]
```

列出按 VMID 分配的卷

```text
pvesm list <STORAGE_ID> --vmid <VMID>
```

列出 ISO 镜像

```text
pvesm list <STORAGE_ID> --content iso
```

列出容器模板

```text
pvesm list <STORAGE_ID> --content vztmpl
```

显示卷的文件系统路径

```text
pvesm path <VOLUME_ID>
```

将卷 `local:103/vm-103-disk-0.qcow2` 导出到文件 `target`。这主要在内部与 `pvesm import` 一起使用。流格式 qcow2\+size 与 qcow2 格式不同。因此，导出的文件不能直接附加到 VM。其他格式也是如此。

```text
pvesm export local:103/vm-103-disk-0.qcow2 qcow2+size target --with-snapshots 1
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
