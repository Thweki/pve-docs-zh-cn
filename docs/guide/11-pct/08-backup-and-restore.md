# 11.8. Backup and Restore <a href="#_backup_and_restore" id="_backup_and_restore"></a>

## 11.8.1. Container Backup <a href="#_container_backup" id="_container_backup"></a>

可以使用 `vzdump` 工具进行容器备份。有关详细信息，请参阅 `vzdump` 手册页。

## 11.8.2. Restoring Container Backups <a href="#_restoring_container_backups" id="_restoring_container_backups"></a>

Restoring container backups made with `vzdump` is possible using the `pct
restore` command. By default, `pct restore` will attempt to restore as much of the backed up container configuration as possible. It is possible to override the backed up configuration by manually setting container options on the command line (see the `pct` manual page for details).

{% hint style="info" %}
`pvesm extractconfig` 可用于查看 vzdump 归档中包含的已备份配置。
{% endhint %}

有两种基本恢复模式，它们的区别仅在于对挂载点的处理方式：

### “简单”恢复模式 <a href="#_8220_simple_8221_restore_mode" id="_8220_simple_8221_restore_mode"></a>

如果既未明确设置 `rootfs` 参数，也未明确设置任何可选的 `mpX` 参数，则将通过以下步骤从备份的配置文件中恢复挂载点配置：

1. 从备份中提取挂载点及其选项
2. 在通过 `storage` 参数指定的存储上，为基于存储的挂载点创建卷（默认值：`local`）。
3. 从备份归档中提取文件
4. 将绑定挂载点和设备挂载点添加到恢复的配置中（仅限 root 用户）

{% hint style="info" %}
由于绑定挂载点和设备挂载点从不备份，最后一步不会恢复任何文件，而只会恢复配置选项。这里假定此类挂载点要么通过其他机制备份（例如，通过绑定挂载到许多容器中的 NFS 空间），要么根本不打算备份。
{% endhint %}

Web 界面中的容器恢复操作也使用这种简单模式。

### “高级”恢复模式 <a href="#_8220_advanced_8221_restore_mode" id="_8220_advanced_8221_restore_mode"></a>

通过设置 `rootfs` 参数（以及可选的任意 `mpX` 参数组合），`pct restore` 命令会自动切换到高级模式。该高级模式会完全忽略备份归档中包含的 `rootfs` 和 `mpX` 配置选项，而仅使用显式作为参数提供的选项。

此模式允许在恢复时灵活配置挂载点设置，例如：

- 为每个挂载点单独设置目标存储、卷大小和其他选项
- 根据新的挂载点方案重新分配已备份的文件
- 恢复到设备和/或绑定挂载点（仅限 root 用户）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
