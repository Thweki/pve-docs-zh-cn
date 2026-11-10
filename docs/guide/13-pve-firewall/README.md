# 13\. Proxmox VE 防火墙 <a href="#chapter_pve_firewall" id="chapter_pve_firewall"></a>

Proxmox VE 防火墙提供了一种简单的方法来保护您的 IT 基础设施。可以为集群内的所有宿主机设置防火墙规则，或为虚拟机和容器定义规则。防火墙宏、安全组、IP 集合和别名等功能有助于简化此任务。

所有配置都存储在集群文件系统中，而基于 `iptables` 的防火墙服务在每个集群节点上运行，因此可在虚拟机之间提供完全隔离。此系统的分布式特性还提供了远高于集中式防火墙方案的带宽。

防火墙完全支持 IPv4 和 IPv6。IPv6 支持完全透明，默认会对两种协议的流量进行过滤。因此无需为 IPv6 维护另一套规则。

## 本章内容

- [13.1. 方向与区域](01-directions-amp-zones.md)
- [13.2. 配置文件](02-configuration-files.md)
- [13.3. 防火墙规则](03-firewall-rules.md)
- [13.4. 安全组](04-pve-firewall-security-groups.md)
- [13.5. IP 别名](05-pve-firewall-ip-aliases.md)
- [13.6. IP 集合](06-pve-firewall-ip-sets.md)
- [13.7. 服务与命令](07-pve-firewall-services-commands.md)
- [13.8. 默认防火墙规则](08-pve-firewall-default-rules.md)
- [13.9. 防火墙规则日志记录](09-logging-of-firewall-rules.md)
- [13.10. 提示与技巧](10-tips-and-tricks.md)
- [13.11. 关于 IPv6 的说明](11-notes-on-ipv6.md)
- [13.12. Proxmox VE 使用的端口](12-ports-used-by-proxmox-ve.md)
- [13.13. nftables](13-pve-firewall-nft.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
