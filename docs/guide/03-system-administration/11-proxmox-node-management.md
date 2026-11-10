# 3.11. Proxmox 节点管理 <a href="#proxmox_node_management" id="proxmox_node_management"></a>

Proxmox VE 节点管理工具（`pvenode`）允许你控制节点特定的设置和资源。

目前，`pvenode` 允许你设置节点描述、对节点上的客户机执行各种批量操作、查看节点的任务历史记录，以及管理节点的 SSL 证书；这些证书由 `pveproxy` 用于 API 和 Web GUI。

## 3.11.1. 网络唤醒（Wake-on-LAN） <a href="#wake_on_lan" id="wake_on_lan"></a>

Wake-on-LAN（WoL）允许你通过发送魔术包来唤醒网络中处于睡眠状态的计算机。至少有一个 NIC 必须支持此功能，并且需要在计算机的固件（BIOS/UEFI）配置中启用相应选项。选项名称可能从*启用 Wake-on-Lan*到*通过 PCIE 设备开机*不等；如果不确定，请查阅主板厂商手册。可以运行以下命令，使用 `ethtool` 检查 `<interface>` 的 WoL 配置：

```text
ethtool <interface> | grep Wake-on
```

`pvenode` 允许你通过 WoL 唤醒集群中处于睡眠状态的成员，命令为：

```text
pvenode wakeonlan <node>
```

这会在 UDP 端口 9 上广播 WoL 魔术包，其中包含 `<node>` 的 MAC 地址，该地址从 `wakeonlan` 属性获取。可以使用以下命令设置节点特定的 `wakeonlan` 属性：

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX
```

发送 WoL 数据包的接口由默认路由确定。可以通过以下命令设置 `bind-interface` 来覆盖该接口：

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX,bind-interface=<iface-name>
```

发送 WoL 数据包时使用的广播地址（默认为 `255.255.255.255`）也可以通过以下命令显式设置 `broadcast-address` 来更改：

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX,broadcast-address=<broadcast-address>
```

## 3.11.2. 任务历史记录 <a href="#task_history" id="task_history"></a>

排查服务器问题（例如备份作业失败）时，查看先前运行任务的日志通常会很有帮助。在 Proxmox VE 中，可以通过 `pvenode task` 命令访问节点的任务历史记录。

可以使用 `list` 子命令获取节点已完成任务的筛选列表。例如，要获取与 VM *100* 相关且以错误结束的任务列表，命令如下：

```text
pvenode task list --errors --vmid 100
```

随后可以使用任务的 UPID 打印其日志：

```text
pvenode task log UPID:pve1:00010D94:001CA6EA:6124E1B9:vzdump:100:root@pam:
```

## 3.11.3. 客户机批量电源管理 <a href="#bulk_guest_power_management" id="bulk_guest_power_management"></a>

如果拥有许多虚拟机/容器，可以通过 `startall` 和 `stopall` 子命令（属于 `pvenode`）批量启动和停止客户机。默认情况下，`pvenode startall` 仅启动已设置为开机自动启动的虚拟机/容器（参见 [虚拟机的自动启动和关闭](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_startup_and_shutdown)），不过可以使用 `--force` 标志覆盖此行为。这两个命令还都有 `--vms` 选项，可将停止/启动的客户机限制为指定的 VMID。

例如，要启动 VM *100*、*101* 和 *102*，无论它们是否设置了 `onboot`，都可以使用：

```text
pvenode startall --vms 100,101,102 --force
```

要停止这些客户机（以及可能正在运行的任何其他客户机），请使用以下命令：

```text
pvenode stopall
```

{% hint style="info" %}
stopall 命令首先尝试执行正常关闭，然后等待，直到所有客户机均成功关闭，或可覆盖的超时时间（默认为 3 分钟）到期。此后，如果 force-stop 参数未显式设置为 0（false），则所有仍在运行的虚拟客户机都会被强制停止。
{% endhint %}

## 3.11.4. 首个客户机启动延迟 <a href="#first_guest_boot_delay" id="first_guest_boot_delay"></a>

如果 VM/容器依赖启动缓慢的外部资源（例如 NFS 服务器），还可以按节点设置一段延迟，即 Proxmox VE 启动后与第一台配置为自动启动的 VM/容器启动前的间隔（参见[虚拟机的自动启动和关闭](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_startup_and_shutdown)）。

可通过以下设置实现（其中 `10` 表示以秒为单位的延迟）：

```text
pvenode config set --startall-onboot-delay 10
```

## 3.11.5. 客户机批量迁移 <a href="#bulk_guest_migration" id="bulk_guest_migration"></a>

如果升级时需要将所有客户机从一个节点迁移到另一个节点，`pvenode` 还提供用于批量迁移的 `migrateall` 子命令。默认情况下，此命令会将系统上的每个客户机迁移到目标节点，但也可以设置为仅迁移一组客户机。

例如，要将 VM *100*、*101* 和 *102* 迁移到节点 *pve2*，并启用本地磁盘的在线迁移，可以运行：

```text
pvenode migrateall pve2 --vms 100,101,102 --with-local-disks
```

## 3.11.6. 内存气球的 RAM 使用率目标 <a href="#ballooning-target" id="ballooning-target"></a>

[自动内存分配](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_ballooning)的目标百分比默认为 80%。可以通过设置 `ballooning-target` 属性，按节点自定义此目标。例如，要将目标改为宿主机内存使用率达到 90%：

```text
pvenode config set --ballooning-target 90
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
