# 23.1. **pve-firewall** - Proxmox VE Firewall Daemon <a href="#_strong_pve_firewall_strong_proxmox_ve_firewall_daemon" id="_strong_pve_firewall_strong_proxmox_ve_firewall_daemon"></a>

<a id="cli_pve-firewall"></a>



**pve-firewall** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pve-firewall_compile"></a>



**pve-firewall compile**

Compile and print firewall rules. This is useful for testing.

<a id="cli_pve-firewall_help"></a>



**pve-firewall help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pve-firewall_localnet"></a>



**pve-firewall localnet**

Print information about local network.

<a id="cli_pve-firewall_restart"></a>



**pve-firewall restart**

Restart the Proxmox VE firewall service.

<a id="cli_pve-firewall_simulate"></a>



**pve-firewall simulate** `[OPTIONS]`

Simulate firewall rules. This does not simulates the kernel *routing* table, but simply assumes that routing from source zone to destination zone is possible.

**`--dest` `<string>`**

Destination IP address.

**`--dport` `<integer>`**

Destination port.

**`--from` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` (*default =* `outside`)**

Source zone.

**`--protocol` `(tcp|udp)` (*default =* `tcp`)**

Protocol.

**`--source` `<string>`**

Source IP address.

**`--sport` `<integer>`**

Source port.

**`--to` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` (*default =* `host`)**

Destination zone.

**`--verbose` `<boolean>`（*默认值 =* `0`）**

Verbose output.

<a id="cli_pve-firewall_start"></a>



**pve-firewall start** `[OPTIONS]`

Start the Proxmox VE firewall service.

**`--debug` `<boolean>`（*默认 =* `0`）**

Debug mode - stay in foreground

<a id="cli_pve-firewall_status"></a>



**pve-firewall status**

Get firewall status.

<a id="cli_pve-firewall_stop"></a>



**pve-firewall stop**

Stop the Proxmox VE firewall service. Note, stopping actively removes all Proxmox VE related iptable rules rendering the host potentially unprotected.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
