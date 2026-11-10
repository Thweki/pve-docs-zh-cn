# 7.3. 卷 <a href="#volumes" id="volumes"></a>

我们使用一种特殊表示法来定位存储数据。当你从存储池分配数据时，它会返回这样一个卷标识符。卷由 `<STORAGE_ID>` 和后随的卷名标识，卷名取决于存储类型，二者以冒号分隔。有效的 `<VOLUME_ID>` 如下所示：

```text
local:230/example-image.raw
```

```text
local:iso/debian-501-amd64-netinst.iso
```

```text
local:vztmpl/debian-5.0-joomla_1.5.9-1_i386.tar.gz
```

```text
iscsi-storage:0.0.2.scsi-14f504e46494c4500494b5042546d2d646744372d31616d61
```

要获取 `<VOLUME_ID>` 的文件系统路径，请使用：

```text
pvesm path <VOLUME_ID>
```

## 7.3.1. 卷所有权 <a href="#volume_ownership" id="volume_ownership"></a>

对于 `image` 类型的卷，存在所有权关系。每个此类卷都归某个 VM 或容器所有。例如，卷 `local:230/example-image.raw` 归 VM 230 所有。大多数存储后端会将此所有权信息编码到卷名中。

删除 VM 或容器时，系统还会删除归该 VM 或容器所有的所有关联卷。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
