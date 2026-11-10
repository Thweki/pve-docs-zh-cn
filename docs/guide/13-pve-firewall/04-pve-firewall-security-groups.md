# 13.4. Security Groups <a href="#pve_firewall_security_groups" id="pve_firewall_security_groups"></a>

A security group is a collection of rules, defined at cluster level, which can be used in all VMs' rules. For example you can define a group named “webserver” with rules to open the *http* and *https* ports.

```text
# /etc/pve/firewall/cluster.fw

[group webserver]
IN  ACCEPT -p tcp -dport 80
IN  ACCEPT -p tcp -dport 443
```

Then, you can add this group to a VM’s firewall

```text
# /etc/pve/firewall/<VMID>.fw

[RULES]
GROUP webserver
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
