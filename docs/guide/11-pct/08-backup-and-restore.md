# 11.8. Backup and Restore <a href="#_backup_and_restore" id="_backup_and_restore"></a>

## 11.8.1. Container Backup <a href="#_container_backup" id="_container_backup"></a>

It is possible to use the `vzdump` tool for container backup. Please refer to the `vzdump` manual page for details.

## 11.8.2. Restoring Container Backups <a href="#_restoring_container_backups" id="_restoring_container_backups"></a>

Restoring container backups made with `vzdump` is possible using the `pct
restore` command. By default, `pct restore` will attempt to restore as much of the backed up container configuration as possible. It is possible to override the backed up configuration by manually setting container options on the command line (see the `pct` manual page for details).

{% hint style="info" %}
`pvesm extractconfig` can be used to view the backed up configuration contained in a vzdump archive.
{% endhint %}

There are two basic restore modes, only differing by their handling of mount points:

### “Simple” Restore Mode <a href="#_8220_simple_8221_restore_mode" id="_8220_simple_8221_restore_mode"></a>

If neither the `rootfs` parameter nor any of the optional `mpX` parameters are explicitly set, the mount point configuration from the backed up configuration file is restored using the following steps:

1. Extract mount points and their options from backup
2. Create volumes for storage backed mount points on the storage provided with the `storage` parameter (default: `local`).
3. Extract files from backup archive
4. Add bind and device mount points to restored configuration (limited to root user)

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
