# 13.4. 安全组 <a href="#pve_firewall_security_groups" id="pve_firewall_security_groups"></a>

安全组是在集群级别定义的规则集合，可用于所有虚拟机的规则中。例如，可以定义名为“webserver”的组，包含开放 *http* 和 *https* 端口的规则。

```text
# /etc/pve/firewall/cluster.fw

[group webserver]
IN  ACCEPT -p tcp -dport 80
IN  ACCEPT -p tcp -dport 443
```

然后，可将此组添加到虚拟机的防火墙中

```text
# /etc/pve/firewall/<VMID>.fw

[RULES]
GROUP webserver
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
