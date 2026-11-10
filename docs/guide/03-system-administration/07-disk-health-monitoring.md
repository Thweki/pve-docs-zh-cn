# 3.7. 磁盘健康监控 <a href="#disk_health_monitoring" id="disk_health_monitoring"></a>

虽然建议使用稳健且冗余的存储，但监控本地磁盘的健康状况也非常有帮助。

从 Proxmox VE 4.3 开始，系统会安装并要求使用 smartmontools 软件包   
\[smartmontools 主页 [https://www.smartmontools.org](https://www.smartmontools.org)\]  
。这是一组用于监控和控制本地硬盘 S.M.A.R.T. 系统的工具。

您可以通过执行以下命令获取磁盘状态：

```text
# smartctl -a /dev/sdX
```

其中 /dev/sdX 是您一块本地磁盘的路径。

如果输出显示：

```text
SMART support is: Disabled
```

您可以使用以下命令启用它：

```text
# smartctl -s on /dev/sdX
```

有关如何使用 smartctl 的更多信息，请参阅 `man smartctl`。

默认情况下，smartmontools 守护进程 smartd 处于活动状态并已启用，并扫描与以下内容匹配的任何设备

- `/dev/sd[a-z]`
- `/dev/sd[a-z][a-z]`
- `/dev/hd[a-t]`
- 或 `/dev/nvme[0-99]`

每 30 分钟检查一次错误和警告，如果检测到问题，则向 root 发送电子邮件。

有关如何配置 smartd 的更多信息，请参阅 `man smartd` 和 `man smartd.conf`。

如果您将硬盘与硬件 RAID 控制器结合使用，很可能有相应的工具可监控 RAID 阵列中的磁盘及阵列本身。有关更多信息，请咨询您的 RAID 控制器供应商。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
