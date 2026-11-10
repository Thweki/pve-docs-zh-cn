# 13.10. 提示与技巧 <a href="#tips_and_tricks" id="tips_and_tricks"></a>

## 13.10.1. 如何允许 FTP <a href="#how_to_allow_ftp" id="how_to_allow_ftp"></a>

FTP 是一种旧式协议，使用端口 21 及若干其他动态端口。因此需要一条接受端口 21 的规则。此外，需要加载 `ip_conntrack_ftp` 模块。请运行：

```text
modprobe ip_conntrack_ftp
```

并将 `ip_conntrack_ftp` 添加到 `/etc/modules`（以便重启后仍然有效）。

## 13.10.2. Suricata IPS 集成 <a href="#suricata_ips_integration" id="suricata_ips_integration"></a>

如果希望使用 [Suricata IPS](https://suricata.io/)（入侵防御系统），这是可行的。

只有防火墙 ACCEPT 的数据包才会转发到 IPS。

防火墙拒绝/丢弃的数据包不会进入 IPS。

在 proxmox 宿主机上安装 suricata：

```text
# apt-get install suricata
# modprobe nfnetlink_queue
```

不要忘记将 `nfnetlink_queue` 添加到 `/etc/modules`，以便下次重启时生效。

然后，使用以下命令为特定虚拟机启用 IPS：

```text
# /etc/pve/firewall/<VMID>.fw

[OPTIONS]
ips: 1
ips_queues: 0
```

`ips_queues` 会为此虚拟机绑定特定的 cpu 队列。

可用队列定义在

```text
# /etc/default/suricata
NFQUEUE=0
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
