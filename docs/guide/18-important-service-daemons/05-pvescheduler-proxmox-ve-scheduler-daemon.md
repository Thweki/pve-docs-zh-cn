# 18.5. pvescheduler \- Proxmox VE 调度守护进程 <a href="#pvescheduler_proxmox_ve_scheduler_daemon" id="pvescheduler_proxmox_ve_scheduler_daemon"></a>

此守护进程负责根据计划启动任务，例如复制任务和 vzdump 任务。

对于 vzdump 任务，它从文件 `/etc/pve/jobs.cfg` 获取配置

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
