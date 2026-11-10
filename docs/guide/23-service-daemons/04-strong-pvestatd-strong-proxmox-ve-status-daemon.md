# 23.4. **pvestatd** \- Proxmox VE 状态守护进程 <a href="#strong_pvestatd_strong_proxmox_ve_status_daemon" id="strong_pvestatd_strong_proxmox_ve_status_daemon"></a>

## **pvestatd** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvestatd" id="cli_pvestatd"></a>

## **pvestatd help** `[OPTIONS]` <a href="#cli_pvestatd_help" id="cli_pvestatd_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvestatd restart** <a href="#cli_pvestatd_restart" id="cli_pvestatd_restart"></a>

重启守护进程（如果未运行则启动）。

## **pvestatd start** `[OPTIONS]` <a href="#cli_pvestatd_start" id="cli_pvestatd_start"></a>

启动守护进程。

**`--debug` `<boolean>`（*默认 \=* `0`）**

调试模式，保持在前台运行

## **pvestatd status** <a href="#cli_pvestatd_status" id="cli_pvestatd_status"></a>

获取守护进程状态。

## **pvestatd stop** <a href="#cli_pvestatd_stop" id="cli_pvestatd_stop"></a>

停止守护进程。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
