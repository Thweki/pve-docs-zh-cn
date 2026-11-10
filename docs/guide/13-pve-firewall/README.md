# 13\. Proxmox VE Firewall <a href="#chapter_pve_firewall" id="chapter_pve_firewall"></a>

Proxmox VE Firewall provides an easy way to protect your IT infrastructure. You can setup firewall rules for all hosts inside a cluster, or define rules for virtual machines and containers. Features like firewall macros, security groups, IP sets and aliases help to make that task easier.

While all configuration is stored on the cluster file system, the `iptables`-based firewall service runs on each cluster node, and thus provides full isolation between virtual machines. The distributed nature of this system also provides much higher bandwidth than a central firewall solution.

The firewall has full support for IPv4 and IPv6. IPv6 support is fully transparent, and we filter traffic for both protocols by default. So there is no need to maintain a different set of rules for IPv6.

## 本章内容

- [13.1. Directions & Zones](01-directions-amp-zones.md)
- [13.2. Configuration Files](02-configuration-files.md)
- [13.3. Firewall Rules](03-firewall-rules.md)
- [13.4. Security Groups](04-pve-firewall-security-groups.md)
- [13.5. IP Aliases](05-pve-firewall-ip-aliases.md)
- [13.6. IP Sets](06-pve-firewall-ip-sets.md)
- [13.7. Services and Commands](07-pve-firewall-services-commands.md)
- [13.8. Default firewall rules](08-pve-firewall-default-rules.md)
- [13.9. Logging of firewall rules](09-logging-of-firewall-rules.md)
- [13.10. Tips and Tricks](10-tips-and-tricks.md)
- [13.11. Notes on IPv6](11-notes-on-ipv6.md)
- [13.12. Ports used by Proxmox VE](12-ports-used-by-proxmox-ve.md)
- [13.13. nftables](13-pve-firewall-nft.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
