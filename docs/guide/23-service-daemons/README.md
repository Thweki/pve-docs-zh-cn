# 23\. 附录 B：服务守护进程 <a href="#service_daemons" id="service_daemons"></a>

## 23.1. <strong>pve-firewall</strong> \- Proxmox VE 防火墙守护进程 <a href="#strong_pve_firewall_strong_proxmox_ve_firewall_daemon" id="strong_pve_firewall_strong_proxmox_ve_firewall_daemon"></a>

### <strong>pve-firewall</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pve-firewall" id="cli_pve-firewall"></a>

### <strong>pve-firewall compile</strong> <a href="#cli_pve-firewall_compile" id="cli_pve-firewall_compile"></a>

编译并打印防火墙规则。这对测试很有用。

### <strong>pve-firewall help</strong> `[OPTIONS]` <a href="#cli_pve-firewall_help" id="cli_pve-firewall_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pve-firewall localnet</strong> <a href="#cli_pve-firewall_localnet" id="cli_pve-firewall_localnet"></a>

打印本地网络信息。

### <strong>pve-firewall restart</strong> <a href="#cli_pve-firewall_restart" id="cli_pve-firewall_restart"></a>

重启 Proxmox VE 防火墙服务。

### <strong>pve-firewall simulate</strong> `[OPTIONS]` <a href="#cli_pve-firewall_simulate" id="cli_pve-firewall_simulate"></a>

模拟防火墙规则。此操作不模拟内核<em>路由</em>表，而是简单假定可以从源区域路由到目标区域。

**`--dest` `<string>`**

目标 IP 地址。

**`--dport` `<integer>`**

目标端口。

**`--from` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` （<em>默认值 \=</em> `outside`）**

源区域。

**`--protocol` `(tcp|udp)` （<em>默认值 \=</em> `tcp`）**

协议。

**`--source` `<string>`**

源 IP 地址。

**`--sport` `<integer>`**

源端口。

**`--to` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` （<em>默认值 \=</em> `host`）**

目标区域。

**`--verbose` `<boolean>`（<em>默认值 \=</em> `0`）**

详细输出。

### <strong>pve-firewall start</strong> `[OPTIONS]` <a href="#cli_pve-firewall_start" id="cli_pve-firewall_start"></a>

启动 Proxmox VE 防火墙服务。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pve-firewall status</strong> <a href="#cli_pve-firewall_status" id="cli_pve-firewall_status"></a>

获取防火墙状态。

### <strong>pve-firewall stop</strong> <a href="#cli_pve-firewall_stop" id="cli_pve-firewall_stop"></a>

停止 Proxmox VE 防火墙服务。注意，停止操作会主动移除所有与 Proxmox VE 相关的 iptable 规则，可能使宿主机失去保护。

## 23.2. <strong>pvedaemon</strong> \- Proxmox VE API 守护进程 <a href="#strong_pvedaemon_strong_proxmox_ve_api_daemon" id="strong_pvedaemon_strong_proxmox_ve_api_daemon"></a>

### <strong>pvedaemon</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvedaemon" id="cli_pvedaemon"></a>

### <strong>pvedaemon help</strong> `[OPTIONS]` <a href="#cli_pvedaemon_help" id="cli_pvedaemon_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvedaemon restart</strong> <a href="#cli_pvedaemon_restart" id="cli_pvedaemon_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>pvedaemon start</strong> `[OPTIONS]` <a href="#cli_pvedaemon_start" id="cli_pvedaemon_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pvedaemon status</strong> <a href="#cli_pvedaemon_status" id="cli_pvedaemon_status"></a>

获取守护进程状态。

### <strong>pvedaemon stop</strong> <a href="#cli_pvedaemon_stop" id="cli_pvedaemon_stop"></a>

停止守护进程。

## 23.3. <strong>pveproxy</strong> \- Proxmox VE API 代理守护进程 <a href="#strong_pveproxy_strong_proxmox_ve_api_proxy_daemon" id="strong_pveproxy_strong_proxmox_ve_api_proxy_daemon"></a>

### <strong>pveproxy</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveproxy" id="cli_pveproxy"></a>

### <strong>pveproxy help</strong> `[OPTIONS]` <a href="#cli_pveproxy_help" id="cli_pveproxy_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pveproxy restart</strong> <a href="#cli_pveproxy_restart" id="cli_pveproxy_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>pveproxy start</strong> `[OPTIONS]` <a href="#cli_pveproxy_start" id="cli_pveproxy_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pveproxy status</strong> <a href="#cli_pveproxy_status" id="cli_pveproxy_status"></a>

获取守护进程状态。

### <strong>pveproxy stop</strong> <a href="#cli_pveproxy_stop" id="cli_pveproxy_stop"></a>

停止守护进程。

## 23.4. <strong>pvestatd</strong> \- Proxmox VE 状态守护进程 <a href="#strong_pvestatd_strong_proxmox_ve_status_daemon" id="strong_pvestatd_strong_proxmox_ve_status_daemon"></a>

### <strong>pvestatd</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvestatd" id="cli_pvestatd"></a>

### <strong>pvestatd help</strong> `[OPTIONS]` <a href="#cli_pvestatd_help" id="cli_pvestatd_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvestatd restart</strong> <a href="#cli_pvestatd_restart" id="cli_pvestatd_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>pvestatd start</strong> `[OPTIONS]` <a href="#cli_pvestatd_start" id="cli_pvestatd_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pvestatd status</strong> <a href="#cli_pvestatd_status" id="cli_pvestatd_status"></a>

获取守护进程状态。

### <strong>pvestatd stop</strong> <a href="#cli_pvestatd_stop" id="cli_pvestatd_stop"></a>

停止守护进程。

## 23.5. <strong>spiceproxy</strong> \- SPICE 代理服务 <a href="#strong_spiceproxy_strong_spice_proxy_service" id="strong_spiceproxy_strong_spice_proxy_service"></a>

### <strong>spiceproxy</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_spiceproxy" id="cli_spiceproxy"></a>

### <strong>spiceproxy help</strong> `[OPTIONS]` <a href="#cli_spiceproxy_help" id="cli_spiceproxy_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>spiceproxy restart</strong> <a href="#cli_spiceproxy_restart" id="cli_spiceproxy_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>spiceproxy start</strong> `[OPTIONS]` <a href="#cli_spiceproxy_start" id="cli_spiceproxy_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>spiceproxy status</strong> <a href="#cli_spiceproxy_status" id="cli_spiceproxy_status"></a>

获取守护进程状态。

### <strong>spiceproxy stop</strong> <a href="#cli_spiceproxy_stop" id="cli_spiceproxy_stop"></a>

停止守护进程。

## 23.6. <strong>pmxcfs</strong> \- Proxmox 集群文件系统 <a href="#strong_pmxcfs_strong_proxmox_cluster_file_system" id="strong_pmxcfs_strong_proxmox_cluster_file_system"></a>

<strong>pmxcfs</strong> `[OPTIONS]`

帮助选项：

**`-h`, `--help`**

显示帮助选项

应用程序选项：

**`-d`, `--debug`**

启用调试消息

**`-f`, `--foreground`**

不要将服务器守护进程化

**`-l`, `--local`**

强制使用本地模式（忽略 corosync.conf，强制仲裁）

通常使用 systemd 工具集启动和管理此服务。该服务称为 <em>pve-cluster</em>。

```text
systemctl start pve-cluster
```

```text
systemctl stop pve-cluster
```

```text
systemctl status pve-cluster
```

## 23.7. <strong>pve-ha-crm</strong> \- 集群资源管理器守护进程 <a href="#strong_pve_ha_crm_strong_cluster_resource_manager_daemon" id="strong_pve_ha_crm_strong_cluster_resource_manager_daemon"></a>

### <strong>pve-ha-crm</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pve-ha-crm" id="cli_pve-ha-crm"></a>

### <strong>pve-ha-crm help</strong> `[OPTIONS]` <a href="#cli_pve-ha-crm_help" id="cli_pve-ha-crm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pve-ha-crm start</strong> `[OPTIONS]` <a href="#cli_pve-ha-crm_start" id="cli_pve-ha-crm_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pve-ha-crm status</strong> <a href="#cli_pve-ha-crm_status" id="cli_pve-ha-crm_status"></a>

获取守护进程状态。

### <strong>pve-ha-crm stop</strong> <a href="#cli_pve-ha-crm_stop" id="cli_pve-ha-crm_stop"></a>

停止守护进程。

## 23.8. <strong>pve-ha-lrm</strong> \- 本地资源管理器守护进程 <a href="#strong_pve_ha_lrm_strong_local_resource_manager_daemon" id="strong_pve_ha_lrm_strong_local_resource_manager_daemon"></a>

### <strong>pve-ha-lrm</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pve-ha-lrm" id="cli_pve-ha-lrm"></a>

### <strong>pve-ha-lrm help</strong> `[OPTIONS]` <a href="#cli_pve-ha-lrm_help" id="cli_pve-ha-lrm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pve-ha-lrm start</strong> `[OPTIONS]` <a href="#cli_pve-ha-lrm_start" id="cli_pve-ha-lrm_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pve-ha-lrm status</strong> <a href="#cli_pve-ha-lrm_status" id="cli_pve-ha-lrm_status"></a>

获取守护进程状态。

### <strong>pve-ha-lrm stop</strong> <a href="#cli_pve-ha-lrm_stop" id="cli_pve-ha-lrm_stop"></a>

停止守护进程。

## 23.9. <strong>pvescheduler</strong> \- Proxmox VE 调度守护进程 <a href="#strong_pvescheduler_strong_proxmox_ve_scheduler_daemon" id="strong_pvescheduler_strong_proxmox_ve_scheduler_daemon"></a>

### <strong>pvescheduler</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvescheduler" id="cli_pvescheduler"></a>

### <strong>pvescheduler help</strong> `[OPTIONS]` <a href="#cli_pvescheduler_help" id="cli_pvescheduler_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvescheduler restart</strong> <a href="#cli_pvescheduler_restart" id="cli_pvescheduler_restart"></a>

重启守护进程（如果未运行则启动）。

### <strong>pvescheduler start</strong> `[OPTIONS]` <a href="#cli_pvescheduler_start" id="cli_pvescheduler_start"></a>

启动守护进程。

**`--debug` `<boolean>`（<em>默认 \=</em> `0`）**

调试模式，保持在前台运行

### <strong>pvescheduler status</strong> <a href="#cli_pvescheduler_status" id="cli_pvescheduler_status"></a>

获取守护进程状态。

### <strong>pvescheduler stop</strong> <a href="#cli_pvescheduler_stop" id="cli_pvescheduler_stop"></a>

停止守护进程。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
