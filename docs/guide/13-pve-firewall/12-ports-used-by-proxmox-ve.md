# 13.12. Proxmox VE 使用的端口 <a href="#ports_used_by_proxmox_ve" id="ports_used_by_proxmox_ve"></a>

- Web 界面：8006（TCP，基于 TLS 的 HTTP/1.1）
- VNC Web 控制台：5900-5999（TCP，WebSocket）
- SPICE 代理：3128（TCP）
- sshd（用于集群操作）：22（TCP）
- rpcbind：111（UDP）
- sendmail：25（TCP，传出）
- corosync 集群流量：5405-5412 UDP
- 在线迁移（虚拟机内存和本地磁盘数据）：60000-60050（TCP）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
