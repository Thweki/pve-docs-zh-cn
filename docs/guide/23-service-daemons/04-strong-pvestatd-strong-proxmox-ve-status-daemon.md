# 23.4. **pvestatd** \- Proxmox VE Status Daemon <a href="#_strong_pvestatd_strong_proxmox_ve_status_daemon" id="_strong_pvestatd_strong_proxmox_ve_status_daemon"></a>

<a id="cli_pvestatd"></a>



**pvestatd** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvestatd_help"></a>



**pvestatd help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvestatd_restart"></a>



**pvestatd restart**

Restart the daemon (or start if not running).

<a id="cli_pvestatd_start"></a>



**pvestatd start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>` (*default \=* `0`)**

Debug mode \- stay in foreground

<a id="cli_pvestatd_status"></a>



**pvestatd status**

Get daemon status.

<a id="cli_pvestatd_stop"></a>



**pvestatd stop**

Stop the daemon.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
