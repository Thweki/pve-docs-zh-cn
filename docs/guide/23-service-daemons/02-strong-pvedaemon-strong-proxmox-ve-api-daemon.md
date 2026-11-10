# 23.2. **pvedaemon** - Proxmox VE API Daemon <a href="#_strong_pvedaemon_strong_proxmox_ve_api_daemon" id="_strong_pvedaemon_strong_proxmox_ve_api_daemon"></a>

<a id="cli_pvedaemon"></a>



**pvedaemon** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvedaemon_help"></a>



**pvedaemon help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvedaemon_restart"></a>



**pvedaemon restart**

Restart the daemon (or start if not running).

<a id="cli_pvedaemon_start"></a>



**pvedaemon start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>`（*默认 =* `0`）**

Debug mode - stay in foreground

<a id="cli_pvedaemon_status"></a>



**pvedaemon status**

Get daemon status.

<a id="cli_pvedaemon_stop"></a>



**pvedaemon stop**

Stop the daemon.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
