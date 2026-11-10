# 23.1. **pve-firewall** \- Proxmox VE 防火墙守护进程 <a href="#strong_pve_firewall_strong_proxmox_ve_firewall_daemon" id="strong_pve_firewall_strong_proxmox_ve_firewall_daemon"></a>

## **pve-firewall** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pve-firewall" id="cli_pve-firewall"></a>

## **pve-firewall compile** <a href="#cli_pve-firewall_compile" id="cli_pve-firewall_compile"></a>

编译并打印防火墙规则。这对测试很有用。

## **pve-firewall help** `[OPTIONS]` <a href="#cli_pve-firewall_help" id="cli_pve-firewall_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pve-firewall localnet** <a href="#cli_pve-firewall_localnet" id="cli_pve-firewall_localnet"></a>

打印本地网络信息。

## **pve-firewall restart** <a href="#cli_pve-firewall_restart" id="cli_pve-firewall_restart"></a>

重启 Proxmox VE 防火墙服务。

## **pve-firewall simulate** `[OPTIONS]` <a href="#cli_pve-firewall_simulate" id="cli_pve-firewall_simulate"></a>

模拟防火墙规则。此操作不模拟内核*路由*表，而是简单假定可以从源区域路由到目标区域。

**`--dest` `<string>`**

目标 IP 地址。

**`--dport` `<integer>`**

目标端口。

**`--from` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` （*默认值 \=* `outside`）**

源区域。

**`--protocol` `(tcp|udp)` （*默认值 \=* `tcp`）**

协议。

**`--source` `<string>`**

源 IP 地址。

**`--sport` `<integer>`**

源端口。

**`--to` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` （*默认值 \=* `host`）**

目标区域。

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

详细输出。

## **pve-firewall start** `[OPTIONS]` <a href="#cli_pve-firewall_start" id="cli_pve-firewall_start"></a>

启动 Proxmox VE 防火墙服务。

**`--debug` `<boolean>`（*默认 \=* `0`）**

调试模式，保持在前台运行

## **pve-firewall status** <a href="#cli_pve-firewall_status" id="cli_pve-firewall_status"></a>

获取防火墙状态。

## **pve-firewall stop** <a href="#cli_pve-firewall_stop" id="cli_pve-firewall_stop"></a>

停止 Proxmox VE 防火墙服务。注意，停止操作会主动移除所有与 Proxmox VE 相关的 iptable 规则，可能使宿主机失去保护。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
