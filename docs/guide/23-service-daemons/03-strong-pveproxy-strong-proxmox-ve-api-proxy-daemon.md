# 23.3. **pveproxy** \- Proxmox VE API 代理守护进程 <a href="#strong_pveproxy_strong_proxmox_ve_api_proxy_daemon" id="strong_pveproxy_strong_proxmox_ve_api_proxy_daemon"></a>

## **pveproxy** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveproxy" id="cli_pveproxy"></a>

## **pveproxy help** `[OPTIONS]` <a href="#cli_pveproxy_help" id="cli_pveproxy_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pveproxy restart** <a href="#cli_pveproxy_restart" id="cli_pveproxy_restart"></a>

重启守护进程（如果未运行则启动）。

## **pveproxy start** `[OPTIONS]` <a href="#cli_pveproxy_start" id="cli_pveproxy_start"></a>

启动守护进程。

**`--debug` `<boolean>`（*默认 \=* `0`）**

调试模式，保持在前台运行

## **pveproxy status** <a href="#cli_pveproxy_status" id="cli_pveproxy_status"></a>

获取守护进程状态。

## **pveproxy stop** <a href="#cli_pveproxy_stop" id="cli_pveproxy_stop"></a>

停止守护进程。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
