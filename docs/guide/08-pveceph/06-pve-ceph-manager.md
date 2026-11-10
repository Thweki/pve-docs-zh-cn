# 8.6. Ceph 管理器 <a href="#pve_ceph_manager" id="pve_ceph_manager"></a>

Manager 守护进程与监视器一同运行。它提供用于监控集群的接口。自 Ceph luminous 发布以来，至少需要一个 ceph-mgr [\[1\]](#note-c14d5ee4-1) 守护进程。

## 8.6.1. 创建管理器 <a href="#pveceph_create_mgr" id="pveceph_create_mgr"></a>

可以安装多个管理器，但在任何给定时间只有一个管理器处于活动状态。

```text
pveceph mgr create
```

{% hint style="info" %}
建议将 Ceph 管理器安装在监视器节点上。为实现高可用性，请安装多个管理器。
{% endhint %}

## 8.6.2. 销毁管理器 <a href="#pveceph_destroy_mgr" id="pveceph_destroy_mgr"></a>

要通过 GUI 移除 Ceph 管理器，请先在树视图中选择一个节点，然后转到 **Ceph → Monitor** 面板。选择 Manager，然后单击 **Destroy** 按钮。

要通过 CLI 移除 Ceph 监视器，请先连接到正在运行 Manager 的节点。然后执行以下命令：

```text
pveceph mgr destroy
```

{% hint style="info" %}
虽然管理器不是硬性依赖，但它对 Ceph 集群至关重要，因为它负责 PG 自动缩放、设备运行状况监控、遥测等重要功能。
{% endhint %}

## 注释

### 注释 1 <a href="#note-c14d5ee4-1" id="note-c14d5ee4-1"></a>

Ceph 管理器 [https://docs.ceph.com/en/tentacle/mgr/](https://docs.ceph.com/en/tentacle/mgr/)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
