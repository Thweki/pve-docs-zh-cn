# 7.14. Ceph RADOS Block Devices (RBD) <a href="#ceph_rados_block_devices" id="ceph_rados_block_devices"></a>

存储池类型：`rbd`

[Ceph](https://ceph.com) 是一种分布式对象存储和文件系统，旨在提供卓越的性能、可靠性和可扩展性。RADOS 块设备实现了功能丰富的块级存储，并具有以下优势：

- 精简置备
- 可调整大小的卷
- 分布式且具备冗余（跨多个 OSD 条带化）
- 完整的快照和克隆功能
- 自我修复
- 无单点故障
- 可扩展到艾字节级
- 提供内核和用户空间实现

{% hint style="info" %}
对于较小规模的部署，也可以直接在 Proxmox VE 节点上运行 Ceph 服务。现代硬件拥有充足的 CPU 性能和内存，因此可以在同一节点上运行存储服务和虚拟机。
{% endhint %}

## 7.14.1. Configuration <a href="#storage_rbd_config" id="storage_rbd_config"></a>

此后端支持通用存储属性 `nodes`、`disable`、`content`，以及以下 `rbd` 特有属性：

**monhost**

监视器守护进程 IP 列表。可选，仅当 Ceph 未在 Proxmox VE 集群上运行时才需要。设置 `monhost` 后，Proxmox VE 会将该集群视为外部集群，并为此存储保留单独的密钥副本，即使这些监视器属于此 Proxmox VE 集群的 Ceph 集群也是如此。

**pool**

Ceph 池名称。

**username**

Ceph 客户端 ID。可选，默认为 `admin`。仅使用不带 `client.` 前缀的 ID。

**krbd**

强制通过 krbd 内核模块访问 rados 块设备。可选。

{% hint style="info" %}
无论该选项的值如何，容器都将使用 `krbd`。
{% endhint %}

**外部 Ceph 集群的配置示例（`/etc/pve/storage.cfg`）**

```text
rbd: ceph-external
        monhost 10.1.1.20 10.1.1.21 10.1.1.22
        pool ceph-external
        content images
        username pve-rbd
```

{% hint style="success" %}
您可以使用 `rbd` 实用程序执行底层管理任务。
{% endhint %}

## 7.14.2. Authentication <a href="#storage_rbd_auth" id="storage_rbd_auth"></a>

{% hint style="info" %}
如果 Ceph 本地安装在 Proxmox VE 集群上，添加存储时会自动完成以下操作。
{% endhint %}

如果使用默认启用的 `cephx` 身份验证，请提供来自外部 Ceph 集群的密钥环。按照 Ceph 用户管理中的说明，获取或创建一个仅具有此存储所需权限的专用身份。[\[cephusermgmt\]](#_footnote_cephusermgmt) 以下示例使用 `client.pve-rbd`；不要将 `client.admin` 复制到存储客户端。

将密钥环复制到一个 Proxmox VE 节点：

```text
# scp <external-ceph-server>:/etc/ceph/ceph.client.pve-rbd.keyring /root/rbd.keyring
```

然后将该文件和不带 `client.` 前缀的身份传递给 `pvesm`：

```text
# pvesm add rbd <name> --monhost "10.1.1.20 10.1.1.21 10.1.1.22" \
    --pool ceph-external --content images --username pve-rbd \
    --keyring /root/rbd.keyring
```

`pvesm` 成功后，删除 `/root/rbd.keyring`，因为其中包含明文密钥。

通过 GUI 配置外部 RBD 存储时，可以将密钥环复制并粘贴到相应字段中。

密钥环将存储在

```text
# /etc/pve/priv/ceph/<STORAGE_ID>.keyring
```

如果外部集群轮换此身份，请在刷新其使用者之前替换已存储的密钥环。本地 cephx 迁移辅助程序绝不会轮换外部集群的密钥。

## 7.14.3. Ceph client configuration (optional) <a href="#_ceph_client_configuration_optional" id="_ceph_client_configuration_optional"></a>

连接外部 Ceph 存储时，并不总能在外部集群的配置数据库中设置客户端特定选项。您可以在 Ceph 密钥环旁添加一个 `ceph.conf`，以更改该存储的 Ceph 客户端配置。

ceph.conf 必须与存储同名。

```text
# /etc/pve/priv/ceph/<STORAGE_ID>.conf
```

有关可用设置，请参阅 RBD 配置参考 [\[2\]](#note-62c47476-2)。

{% hint style="info" %}
请勿轻易更改这些设置。Proxmox VE 会将 \<STORAGE\_ID\>.conf 与存储配置合并。
{% endhint %}

## 7.14.4. Storage Features <a href="#_storage_features_10" id="_storage_features_10"></a>

`rbd` 后端是块级存储，实现了完整的快照和克隆功能。

<table>
<caption>表 13. 后端 <code>rbd</code> 的存储功能</caption>





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
<td><p>images rootdir</p></td>
<td><p>raw</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
</tbody>
</table>

## 注释

### 注释 cephusermgmt <a href="#_footnote_cephusermgmt" id="_footnote_cephusermgmt"></a>

[Ceph 用户管理](https://docs.ceph.com/en/tentacle/rados/operations/user-management/)

### 注释 2 <a href="#note-62c47476-2" id="note-62c47476-2"></a>

RBD 配置参考 [https://docs.ceph.com/en/tentacle/rbd/rbd-config-ref/](https://docs.ceph.com/en/tentacle/rbd/rbd-config-ref/)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
