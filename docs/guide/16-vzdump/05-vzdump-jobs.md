# 16.5. Backup Jobs <a href="#vzdump_jobs" id="vzdump_jobs"></a>

[![screenshot/gui-cluster-backup-overview.png](../../assets/screenshot-gui-cluster-backup-overview-png-18af9966fffc.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cluster-backup-overview.png)

Besides triggering a backup manually, you can also setup periodic jobs that backup all, or a selection of virtual guest to a storage. You can manage the jobs in the UI under *Datacenter* → *Backup* or via the `/cluster/backup` API endpoint. Both will generate job entries in `/etc/pve/jobs.cfg`, which are parsed and executed by the `pvescheduler` daemon.

[![screenshot/gui-cluster-backup-edit-01-general.png](../../assets/screenshot-gui-cluster-backup-edit-01-general-png-fa4abeeaaef7.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cluster-backup-edit-01-general.png)

A job is either configured for all cluster nodes or a specific node, and is executed according to a given schedule. The format for the schedule is very similar to `systemd` calendar events, see the [calendar events](../25-calendar-events/01-chapter-calendar-events.md) section for details. The *Schedule* field in the UI can be freely edited, and it contains several examples that can be used as a starting point in its drop-down list.

You can configure job-specific [retention options](06-vzdump-retention.md) overriding those from the storage or node configuration, as well as a [template for notes](08-vzdump-notes.md) for additional information to be saved together with the backup.

Since scheduled backups miss their execution when the host was offline or the pvescheduler was disabled during the scheduled time, it is possible to configure the behaviour for catching up. By enabling the `Repeat missed` option (in the *Advanced* tab in the UI, `repeat-missed` in the config), you can tell the scheduler that it should run missed jobs as soon as possible.

[![screenshot/gui-cluster-backup-edit-04-advanced.png](../../assets/screenshot-gui-cluster-backup-edit-04-advanced-png-d0a22edf1c07.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cluster-backup-edit-04-advanced.png)

There are a few settings for tuning backup performance (some of which are exposed in the *Advanced* tab in the UI). The most notable is `bwlimit` for limiting IO bandwidth. The amount of threads used for the compressor can be controlled with the `pigz` (replacing `gzip`), respectively, `zstd` setting. Furthermore, there are `ionice` (when the BFQ scheduler is used) and, as part of the `performance` setting, `max-workers` (affects VM backups only) and `pbs-entries-max` (affects container backups only). See the [configuration options](10-vzdump-configuration.md) for details.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
