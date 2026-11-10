# 7.16. BTRFS 后端 <a href="#storage_btrfs" id="storage_btrfs"></a>

存储池类型：`btrfs`

从表面上看，这种存储类型与目录存储类型非常相似，因此总体概述请参阅目录后端一节。

主要区别在于，使用这种存储类型时，`raw` 格式的磁盘将放置在子卷中，以便创建快照，并支持保留快照的离线存储迁移。

{% hint style="info" %}
BTRFS 在打开文件时会遵循 `O_DIRECT` 标志，这意味着虚拟机不应使用缓存模式 `none`，否则会出现校验和错误。
{% endhint %}

## 7.16.1. 配置 <a href="#configuration_10" id="configuration_10"></a>

此后端的配置方式与目录存储类似。请注意，将本身并非挂载点的目录添加为 BTRFS 存储时，强烈建议通过 `is_mountpoint` 选项指定实际挂载点。

例如，如果 BTRFS 文件系统挂载在 `/mnt/data2`，并且要将其 `pve-storage/` 子目录（可以是快照，建议如此）添加为名为 `data2` 的存储池，可以使用以下条目：

```text
btrfs: data2
        path /mnt/data2/pve-storage
        content rootdir,images
        is_mountpoint /mnt/data2
```

## 7.16.2. 快照 <a href="#snapshots" id="snapshots"></a>

为子卷或 `raw` 文件创建快照时，快照将创建为只读子卷，其路径为原路径后接 `@` 和快照名称。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
