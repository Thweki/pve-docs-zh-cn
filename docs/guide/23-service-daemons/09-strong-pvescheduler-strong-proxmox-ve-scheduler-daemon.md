# 23.9. **pvescheduler** \- Proxmox VE Scheduler Daemon <a href="#_strong_pvescheduler_strong_proxmox_ve_scheduler_daemon" id="_strong_pvescheduler_strong_proxmox_ve_scheduler_daemon"></a>

<a id="cli_pvescheduler"></a>



**pvescheduler** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvescheduler_help"></a>



**pvescheduler help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvescheduler_restart"></a>



**pvescheduler restart**

Restart the daemon (or start if not running).

<a id="cli_pvescheduler_start"></a>



**pvescheduler start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>`（*默认 \=* `0`）**

Debug mode \- stay in foreground

<a id="cli_pvescheduler_status"></a>



**pvescheduler status**

Get daemon status.

<a id="cli_pvescheduler_stop"></a>



**pvescheduler stop**

Stop the daemon.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
