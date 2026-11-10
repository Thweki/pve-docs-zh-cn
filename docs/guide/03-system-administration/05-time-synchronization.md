# 3.5. Time Synchronization <a href="#_time_synchronization" id="_time_synchronization"></a>

Proxmox VE 集群软件栈本身高度依赖于所有节点的时间都精确同步。如果所有节点的本地时间不同步，Ceph 等其他一些组件也无法正常工作。

可以使用“网络时间协议”（`NTP`）实现节点之间的时间同步。从 Proxmox VE 7 开始，`chrony` 用作默认的 NTP 守护进程，而 Proxmox VE 6 使用 `systemd-timesyncd`。两者都预先配置为使用一组公共服务器。

{% hint style="warning" %}
如果将系统升级到 Proxmox VE 7，建议您手动安装 `chrony`、`ntp` 或 `openntpd`。
{% endhint %}

## 3.5.1. Using Custom NTP Servers <a href="#_using_custom_ntp_servers" id="_using_custom_ntp_servers"></a>

在某些情况下，可能需要使用非默认的 NTP 服务器。例如，如果您的 Proxmox VE 节点由于严格的防火墙规则而无法访问公共互联网，则需要设置本地 NTP 服务器，并告知 NTP 守护进程使用它们。

### For systems using chrony: <a href="#_for_systems_using_chrony" id="_for_systems_using_chrony"></a>

在 `chrony` 的配置文件 `/etc/chrony/chrony.conf` 中指定应使用哪些服务器：

```text
server ntp1.example.com iburst
server ntp2.example.com iburst
server ntp3.example.com iburst
```

重启 `chrony`：

```text
# systemctl restart chronyd
```

检查日志，以确认新配置的 NTP 服务器正在被使用：

```text
# journalctl --since -1h -u chrony
```

```text
...
Aug 26 13:00:09 node1 systemd[1]: Started chrony, an NTP client/server.
Aug 26 13:00:15 node1 chronyd[4873]: Selected source 10.0.0.1 (ntp1.example.com)
Aug 26 13:00:15 node1 chronyd[4873]: System clock TAI offset set to 37 seconds
...
```

### For systems using systemd-timesyncd: <a href="#_for_systems_using_systemd_timesyncd" id="_for_systems_using_systemd_timesyncd"></a>

在 `systemd-timesyncd` 的配置文件 `/etc/systemd/timesyncd.conf` 中指定应使用哪些服务器：

```text
[Time]
NTP=ntp1.example.com ntp2.example.com ntp3.example.com ntp4.example.com
```

然后，重启同步服务（`systemctl restart
systemd-timesyncd`），并通过检查日志（`journalctl --since -1h -u systemd-timesyncd`）验证新配置的 NTP 服务器是否正在使用：

```text
...
Oct 07 14:58:36 node1 systemd[1]: Stopping Network Time Synchronization...
Oct 07 14:58:36 node1 systemd[1]: Starting Network Time Synchronization...
Oct 07 14:58:36 node1 systemd[1]: Started Network Time Synchronization.
Oct 07 14:58:36 node1 systemd-timesyncd[13514]: Using NTP server 10.0.0.1:123 (ntp1.example.com).
Oct 07 14:58:36 node1 systemd-timesyncd[13514]: interval/delta/delay/jitter/drift 64s/-0.002s/0.020s/0.000s/-31ppm
...
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
