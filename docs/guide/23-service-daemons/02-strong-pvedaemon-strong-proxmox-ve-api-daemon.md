# 23.2. **pvedaemon** \- Proxmox VE API 守护进程 <a href="#strong_pvedaemon_strong_proxmox_ve_api_daemon" id="strong_pvedaemon_strong_proxmox_ve_api_daemon"></a>

## **pvedaemon** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvedaemon" id="cli_pvedaemon"></a>

## **pvedaemon help** `[OPTIONS]` <a href="#cli_pvedaemon_help" id="cli_pvedaemon_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvedaemon restart** <a href="#cli_pvedaemon_restart" id="cli_pvedaemon_restart"></a>

重启守护进程（如果未运行则启动）。

## **pvedaemon start** `[OPTIONS]` <a href="#cli_pvedaemon_start" id="cli_pvedaemon_start"></a>

启动守护进程。

**`--debug` `<boolean>`（*默认 \=* `0`）**

调试模式，保持在前台运行

## **pvedaemon status** <a href="#cli_pvedaemon_status" id="cli_pvedaemon_status"></a>

获取守护进程状态。

## **pvedaemon stop** <a href="#cli_pvedaemon_stop" id="cli_pvedaemon_stop"></a>

停止守护进程。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
