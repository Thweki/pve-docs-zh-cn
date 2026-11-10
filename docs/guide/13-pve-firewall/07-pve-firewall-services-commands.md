# 13.7. 服务与命令 <a href="#pve_firewall_services_commands" id="pve_firewall_services_commands"></a>

防火墙在每个节点上运行两个服务守护进程：

- pvefw-logger：NFLOG 守护进程（ulogd 的替代品）。
- pve-firewall：更新 iptables 规则

还有一个名为 `pve-firewall` 的 CLI 命令，可用于启动和停止防火墙服务：

```text
# pve-firewall start
# pve-firewall stop
```

要获取状态，请使用：

```text
# pve-firewall status
```

上述命令会读取并编译所有防火墙规则，因此如果防火墙配置包含任何错误，您将看到警告。

如果希望查看生成的 iptables 规则，可以使用：

```text
# iptables-save
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
