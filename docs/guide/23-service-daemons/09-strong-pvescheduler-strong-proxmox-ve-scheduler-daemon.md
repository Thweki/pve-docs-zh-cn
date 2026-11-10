# 23.9. **pvescheduler** \- Proxmox VE 调度守护进程 <a href="#strong_pvescheduler_strong_proxmox_ve_scheduler_daemon" id="strong_pvescheduler_strong_proxmox_ve_scheduler_daemon"></a>

## **pvescheduler** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvescheduler" id="cli_pvescheduler"></a>

## **pvescheduler help** `[OPTIONS]` <a href="#cli_pvescheduler_help" id="cli_pvescheduler_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvescheduler restart** <a href="#cli_pvescheduler_restart" id="cli_pvescheduler_restart"></a>

重启守护进程（如果未运行则启动）。

## **pvescheduler start** `[OPTIONS]` <a href="#cli_pvescheduler_start" id="cli_pvescheduler_start"></a>

启动守护进程。

**`--debug` `<boolean>`（*默认 \=* `0`）**

调试模式，保持在前台运行

## **pvescheduler status** <a href="#cli_pvescheduler_status" id="cli_pvescheduler_status"></a>

获取守护进程状态。

## **pvescheduler stop** <a href="#cli_pvescheduler_stop" id="cli_pvescheduler_stop"></a>

停止守护进程。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
