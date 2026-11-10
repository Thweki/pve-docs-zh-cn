# 9.4. Managing Jobs <a href="#_managing_jobs" id="_managing_jobs"></a>

[![screenshot/gui-qemu-add-replication-job.png](../../assets/screenshot-gui-qemu-add-replication-job-png-8a556dc3f050.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-add-replication-job.png)

You can use the web GUI to create, modify, and remove replication jobs easily. Additionally, the command-line interface (CLI) tool `pvesr` can be used to do this.

You can find the replication panel on all levels (datacenter, node, virtual guest) in the web GUI. They differ in which jobs get shown: all, node- or guest-specific jobs.

When adding a new job, you need to specify the guest if not already selected as well as the target node. The replication [schedule](02-pvesr-schedule-time-format.md#pvesr_schedule_time_format) can be set if the default of `all
15 minutes` is not desired. You may impose a rate-limit on a replication job. The rate limit can help to keep the load on the storage acceptable.

A replication job is identified by a cluster-wide unique ID. This ID is composed of the VMID in addition to a job number. This ID must only be specified manually if the CLI tool is used.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
