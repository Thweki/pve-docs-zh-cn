# 11.7. 容器存储 <a href="#pct_container_storage" id="pct_container_storage"></a>

Proxmox VE LXC 容器存储模型比传统的容器存储模型更灵活。一个容器可以有多个挂载点。这样就可以为每个应用程序使用最合适的存储。

例如，容器的根文件系统可位于速度较慢、价格较低的存储上，而数据库可以通过第二个挂载点位于快速分布式存储上。更多详情请参阅 [挂载点](04-pct-settings.md#pct_mount_points) 一节。

可以使用 Proxmox VE 存储库支持的任何存储类型。这意味着容器可以存储在本地存储（例如 `lvm`、`zfs` 或目录）、共享外部存储（如 `iSCSI`、`NFS`），甚至 Ceph 等分布式存储系统上。如果底层存储支持，则可以使用快照或克隆等高级存储功能。`vzdump` 备份工具可以使用快照来提供一致的容器备份。

此外，可以使用*绑定挂载*直接挂载本地设备或本地目录。这使容器内几乎可以零开销地访问本地资源。绑定挂载可以作为在容器之间共享数据的一种简便方式。

## 11.7.1. FUSE 挂载 <a href="#fuse_mounts" id="fuse_mounts"></a>

{% hint style="warning" %}
由于 Linux 内核的 freezer 子系统存在已知问题，强烈建议不要在容器内使用 FUSE 挂载，因为在挂起或快照模式备份时需要冻结容器。
{% endhint %}

如果无法用其他挂载机制或存储技术替代 FUSE 挂载，可以在 Proxmox 宿主机上建立 FUSE 挂载，并使用绑定挂载点使其在容器内可访问。

## 11.7.2. 在容器内部使用配额 <a href="#using_quotas_inside_containers" id="using_quotas_inside_containers"></a>

配额允许在容器内为每个用户可使用的磁盘空间量设置限制。

{% hint style="info" %}
这目前需要使用旧版 *cgroups*。
{% endhint %}

{% hint style="info" %}
这仅适用于基于 ext4 镜像的存储类型，并且目前仅适用于特权容器。
{% endhint %}

启用 `quota` 选项会为挂载点使用以下挂载选项：`usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0`

这样就可以像在其他任何系统上一样使用配额。您可以通过运行以下命令来初始化 `/aquota.user` 和 `/aquota.group` 文件：

```text
# quotacheck -cmug /
# quotaon /
```

然后使用 `edquota` 命令编辑配额。有关详细信息，请参阅容器内所运行发行版的文档。

{% hint style="info" %}
您需要为每个挂载点运行上述命令，并传入挂载点的路径，而不是只传入 `/`。
{% endhint %}

## 11.7.3. 在容器内部使用 ACL <a href="#using_acls_inside_containers" id="using_acls_inside_containers"></a>

标准 Posix **访问****控制****列表**在容器内也可用。ACL 允许您设置比传统的用户/组/其他用户模型更细致的文件所有权。

## 11.7.4. 容器挂载点的备份 <a href="#backup_of_container_mount_points" id="backup_of_container_mount_points"></a>

要在备份中包含挂载点，请在容器配置中为其启用 `backup` 选项。对于现有挂载点 `mp0`

```text
mp0: guests:subvol-100-disk-1,mp=/root/files,size=8G
```

添加 `backup=1` 以启用该选项。

```text
mp0: guests:subvol-100-disk-1,mp=/root/files,size=8G,backup=1
```

{% hint style="info" %}
在 GUI 中创建新挂载点时，此选项默认启用。
{% endhint %}

要禁用挂载点备份，请按上述方式添加 `backup=0`，或在 GUI 中取消选中**备份**复选框。

## 11.7.5. 容器挂载点的复制 <a href="#replication_of_containers_mount_points" id="replication_of_containers_mount_points"></a>

默认情况下，复制根磁盘时也会复制其他挂载点。如果希望 Proxmox VE 存储复制机制跳过某个挂载点，可以为该挂载点设置**跳过复制**选项。自 Proxmox VE 5.0 起，复制需要类型为 `zfspool` 的存储。当容器已配置复制时，如果要将挂载点添加到其他类型的存储，则必须为该挂载点启用**跳过复制**。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
