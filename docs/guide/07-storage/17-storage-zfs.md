# 7.17. ISCSI 上的 ZFS 后端 <a href="#storage_zfs" id="storage_zfs"></a>

存储池类型：`zfs`

此后端通过 `ssh` 访问一台远程机器，该机器以 ZFS 池作为存储，并实现了 iSCSI 目标。它为每个客户机磁盘创建一个 ZVOL，并将其导出为 iSCSI LUN。Proxmox VE 将此 LUN 用作客户机磁盘。

支持以下 iSCSI 目标实现：

- LIO (Linux)
- IET (Linux)
- ISTGT (FreeBSD)
- Comstar (Solaris)

{% hint style="info" %}
此插件需要支持 ZFS 的远程存储设备，不能用它在我现在继续...普通存储设备/SAN 上创建 ZFS 池
{% endhint %}

## 7.17.1. 配置 <a href="#configuration_11" id="configuration_11"></a>

要使用 ZFS over iSCSI 插件，需要配置远程机器（目标），使其接受来自 Proxmox VE 节点的 `ssh` 连接。Proxmox VE 连接到目标以创建 ZVOL，并通过 iSCSI 将其导出。身份验证通过存储在 `/etc/pve/priv/zfs/<target_ip>_id_rsa` 中的 SSH 密钥（无密码保护）完成。

以下步骤创建一个 SSH 密钥，并将其分发到 IP 地址为 192.0.2.1 的存储机器：

```text
mkdir /etc/pve/priv/zfs
ssh-keygen -f /etc/pve/priv/zfs/192.0.2.1_id_rsa
ssh-copy-id -i /etc/pve/priv/zfs/192.0.2.1_id_rsa.pub root@192.0.2.1
ssh -i /etc/pve/priv/zfs/192.0.2.1_id_rsa root@192.0.2.1
```

此后端支持通用存储属性 `content`、`nodes`、`disable`，以及以下 ZFS over ISCSI 特有属性：

**pool**

iSCSI 目标上的 ZFS 池/文件系统。所有分配都在该池中进行。

**门户**

iSCSI 门户（IP 或 DNS 名称，可选端口）。

**目标端**

iSCSI 目标端。

**iscsiprovider**

远程机器上使用的 iSCSI 目标实现

**comstar\_tg**

comstar 视图的目标组。

**comstar\_hg**

comstar 视图的主机组。

**lio\_tpg**

Linux LIO 目标的目标门户组

**nowritecache**

禁用目标上的写入缓存

**blocksize**

设置 ZFS 的 blocksize 参数。

**sparse**

使用 ZFS 精简置备。稀疏卷是指预留空间不等于卷大小的卷。

**配置示例（`/etc/pve/storage.cfg`）**

```text
zfs: lio
   blocksize 4k
   iscsiprovider LIO
   pool tank
   portal 192.0.2.111
   target iqn.2003-01.org.linux-iscsi.lio.x8664:sn.xxxxxxxxxxxx
   content images
   lio_tpg tpg1
   sparse 1

zfs: solaris
   blocksize 4k
   target iqn.2010-08.org.illumos:02:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:tank1
   pool tank
   iscsiprovider comstar
   portal 192.0.2.112
   content images

zfs: freebsd
   blocksize 4k
   target iqn.2007-09.jp.ne.peach.istgt:tank1
   pool tank
   iscsiprovider istgt
   portal 192.0.2.113
   content images

zfs: iet
   blocksize 4k
   target iqn.2001-04.com.example:tank1
   pool tank
   iscsiprovider iet
   portal 192.0.2.114
   content images
```

## 7.17.2. 存储功能 <a href="#storage_features_12" id="storage_features_12"></a>

ZFS over iSCSI 插件提供支持快照的共享存储。您需要确保 ZFS 设备不会成为部署中的单点故障。

<table>
<caption>表 15. 后端 <code>iscsi</code> 的存储功能</caption>





<thead>
<tr>
<th>内容类型</th>
<th>镜像格式</th>
<th>共享</th>
<th>快照</th>
<th>克隆</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images</p></td>
<td><p>raw</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
