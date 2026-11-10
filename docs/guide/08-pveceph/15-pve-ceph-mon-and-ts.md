# 8.15. Ceph 监控与故障排除 <a href="#pve_ceph_mon_and_ts" id="pve_ceph_mon_and_ts"></a>

从一开始就持续监控 Ceph 部署的健康状况非常重要，可以使用 Ceph 工具，也可以通过 Proxmox VE [API](../../api/README.md) 访问状态。

以下 Ceph 命令可用于查看集群是否健康（*HEALTH\_OK*）、是否存在警告（*HEALTH\_WARN*），甚至是否存在错误（*HEALTH\_ERR*）。如果集群处于不健康状态，下面的状态命令还会概述当前事件和应采取的操作。要停止执行，请按 CTRL-C。

持续查看集群状态：

```text
watch ceph --status
```

打印一次集群状态（不更新），并持续追加状态事件行：

```text
ceph --watch
```

## 8.15.1. 故障排除 <a href="#pve_ceph_ts" id="pve_ceph_ts"></a>

本节包含常用的故障排除信息。更多信息可在 Ceph 官方网站的“故障排除”下找到 [\[1\]](#note-90fb47b2-1)。

<a id="pve_ceph_ts_logs"></a>



**受影响节点上的相关日志**

- [磁盘健康监控](../03-system-administration/07-disk-health-monitoring.md)
- *系统 → 系统日志*，或通过 CLI，例如查看最近 2 天的日志：

  ```text
  journalctl --since "2 days ago"
  ```
- IPMI 和 RAID 控制器日志

可以通过运行以下命令列出 Ceph 服务崩溃并查看详细信息：

```text
ceph crash ls
ceph crash info <crash_id>
```

可以通过运行以下命令确认标记为 new 的崩溃：

```text
ceph crash archive-all
```

要获得更详细的视图，每个 Ceph 服务在 `/var/log/ceph/` 下都有一个日志文件。如果需要更详细的信息，可以调整日志级别 [\[2\]](#note-90fb47b2-2)。

<a id="pve_ceph_ts_causes"></a>



**Ceph 问题的常见原因**

- 网络问题，例如拥塞、交换机故障、接口关闭或防火墙阻塞。检查所有 Proxmox VE 节点在 [corosync 集群网络](../05-pvecm/08-pvecm-cluster-network.md) 以及 [Ceph 公共网络和集群网络](04-pve-ceph-install-wizard.md) 上是否都能可靠访问。
- 磁盘或连接部件存在以下情况：

  - 有缺陷
  - 安装不牢固
  - 在较高负载下 I/O 性能不足（例如使用 HDD、消费级硬件或 [不建议使用的 RAID 控制器](03-recommendations-for-a-healthy-ceph-cluster.md#pve_ceph_recommendation_raid) 时）
- 不符合健康 Ceph 集群的 [建议](03-recommendations-for-a-healthy-ceph-cluster.md)。

<a id="pve_ceph_ts_problems"></a>



**常见 Ceph 问题**

****

**OSD `down`/crashed**

有故障的 OSD 会被报告为 `down`，并且通常会在 10 分钟后自动变为 `out`。根据原因，它也可能自动恢复为 `up` 和 `in`。要尝试通过 Web 界面手动激活，请转到 *任意节点 → Ceph → OSD*，选择该 OSD，然后依次点击 **启动**、**In** 和 **重新加载**。使用 shell 时，在受影响的节点上运行以下命令：

```text
ceph-volume lvm activate --all
```

要激活发生故障的 OSD，可能需要 [安全重启](../15-ha-manager/11-ha-manager-node-maintenance.md) 相应节点，或者作为最后手段，[重新创建或更换](14-ceph-maintenance.md#pve_ceph_osd_replace) 该 OSD。

## 注释

### 注释 1 <a href="#note-90fb47b2-1" id="note-90fb47b2-1"></a>

Ceph 故障排除 [https://docs.ceph.com/en/tentacle/rados/troubleshooting/](https://docs.ceph.com/en/tentacle/rados/troubleshooting/)

### 注释 2 <a href="#note-90fb47b2-2" id="note-90fb47b2-2"></a>

Ceph 日志和调试 [https://docs.ceph.com/en/tentacle/rados/troubleshooting/log-and-debug/](https://docs.ceph.com/en/tentacle/rados/troubleshooting/log-and-debug/)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
