# 11.7. Container Storage <a href="#pct_container_storage" id="pct_container_storage"></a>

The Proxmox VE LXC container storage model is more flexible than traditional container storage models. A container can have multiple mount points. This makes it possible to use the best suited storage for each application.

For example the root file system of the container can be on slow and cheap storage while the database can be on fast and distributed storage via a second mount point. See section [Mount Points](04-pct-settings.md#pct_mount_points) for further details.

Any storage type supported by the Proxmox VE storage library can be used. This means that containers can be stored on local (for example `lvm`, `zfs` or directory), shared external (like `iSCSI`, `NFS`) or even distributed storage systems like Ceph. Advanced storage features like snapshots or clones can be used if the underlying storage supports them. The `vzdump` backup tool can use snapshots to provide consistent container backups.

Furthermore, local devices or local directories can be mounted directly using *bind mounts*. This gives access to local resources inside a container with practically zero overhead. Bind mounts can be used as an easy way to share data between containers.

## 11.7.1. FUSE Mounts <a href="#_fuse_mounts" id="_fuse_mounts"></a>

{% hint style="warning" %}
Because of existing issues in the Linux kernel’s freezer subsystem the usage of FUSE mounts inside a container is strongly advised against, as containers need to be frozen for suspend or snapshot mode backups.
{% endhint %}

If FUSE mounts cannot be replaced by other mounting mechanisms or storage technologies, it is possible to establish the FUSE mount on the Proxmox host and use a bind mount point to make it accessible inside the container.

## 11.7.2. Using Quotas Inside Containers <a href="#_using_quotas_inside_containers" id="_using_quotas_inside_containers"></a>

Quotas allow to set limits inside a container for the amount of disk space that each user can use.

{% hint style="info" %}
This currently requires the use of legacy *cgroups*.
{% endhint %}

{% hint style="info" %}
This only works on ext4 image based storage types and currently only works with privileged containers.
{% endhint %}

Activating the `quota` option causes the following mount options to be used for a mount point: `usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0`

This allows quotas to be used like on any other system. You can initialize the `/aquota.user` and `/aquota.group` files by running:

```text
# quotacheck -cmug /
# quotaon /
```

Then edit the quotas using the `edquota` command. Refer to the documentation of the distribution running inside the container for details.

{% hint style="info" %}
You need to run the above commands for every mount point by passing the mount point’s path instead of just `/`.
{% endhint %}

## 11.7.3. Using ACLs Inside Containers <a href="#_using_acls_inside_containers" id="_using_acls_inside_containers"></a>

The standard Posix **A**ccess **C**ontrol **L**ists are also available inside containers. ACLs allow you to set more detailed file ownership than the traditional user/group/others model.

## 11.7.4. Backup of Container mount points <a href="#_backup_of_container_mount_points" id="_backup_of_container_mount_points"></a>

To include a mount point in backups, enable the `backup` option for it in the container configuration. For an existing mount point `mp0`

```text
mp0: guests:subvol-100-disk-1,mp=/root/files,size=8G
```

add `backup=1` to enable it.

```text
mp0: guests:subvol-100-disk-1,mp=/root/files,size=8G,backup=1
```

{% hint style="info" %}
When creating a new mount point in the GUI, this option is enabled by default.
{% endhint %}

To disable backups for a mount point, add `backup=0` in the way described above, or uncheck the **Backup** checkbox on the GUI.

## 11.7.5. Replication of Containers mount points <a href="#_replication_of_containers_mount_points" id="_replication_of_containers_mount_points"></a>

By default, additional mount points are replicated when the Root Disk is replicated. If you want the Proxmox VE storage replication mechanism to skip a mount point, you can set the **Skip replication** option for that mount point. As of Proxmox VE 5.0, replication requires a storage of type `zfspool`. Adding a mount point to a different type of storage when the container has replication configured requires to have **Skip replication** enabled for that mount point.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
