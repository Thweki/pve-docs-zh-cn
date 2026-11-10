# 7.15. Ceph 文件系统 (CephFS) <a href="#storage_cephfs" id="storage_cephfs"></a>

存储池类型：`cephfs`

CephFS 实现了一个符合 POSIX 标准的文件系统，使用 [Ceph](https://ceph.com) 存储集群来存储数据。由于 CephFS 构建于 Ceph 之上，因此它继承了 Ceph 的大部分特性，包括冗余性、可扩展性、自我修复和高可用性。

{% hint style="success" %}
Proxmox VE 可以[管理 Ceph 部署](../08-pveceph/README.md)，这使 CephFS 存储的配置更加容易。由于现代硬件具备强大的处理能力和充足的内存，在同一节点上运行存储服务和虚拟机是可行的，且不会对性能产生显著影响。
{% endhint %}

要使用 CephFS 存储插件，必须通过添加我们的 [Ceph 软件仓库](../03-system-administration/01-sysadmin-package-repositories.md#sysadmin_package_repositories_ceph) 来替换 Debian 自带的 Ceph 客户端。添加后，运行 `apt update`，然后运行 `apt dist-upgrade`，以获取最新软件包。

{% hint style="warning" %}
请确保未配置其他 Ceph 软件仓库。否则安装将失败，或者节点上会存在混合版本的软件包，从而导致意外行为。
{% endhint %}

## 7.15.1. 配置 <a href="#storage_cephfs_config" id="storage_cephfs_config"></a>

此后端支持通用存储属性 `nodes`、`disable`、`content`，以及以下 `cephfs` 特有属性：

**fs-name**

Ceph 文件系统名称。

**monhost**

监视器守护进程地址列表。可选，仅当 Ceph 未在 Proxmox VE 集群上运行时才需要。设置 `monhost` 后，Proxmox VE 会将该集群视为外部集群，并为此存储保留单独的密钥副本，即使这些监视器属于此 Proxmox VE 集群的 Ceph 集群也是如此。

**path**

本地挂载点。可选，默认为 `/mnt/pve/<STORAGE_ID>/`。

**username**

Ceph 客户端 ID。可选，默认为 `admin`。仅使用不带 `client.` 前缀的 ID。

**subdir**

要挂载的 CephFS 子目录。可选，默认为 `/`。

**fuse**

通过 FUSE 而非内核客户端访问 CephFS。可选，默认为 `0`。

**外部 Ceph 集群的配置示例（`/etc/pve/storage.cfg`）**

```text
cephfs: cephfs-external
        monhost 10.1.1.20 10.1.1.21 10.1.1.22
        path /mnt/pve/cephfs-external
        content backup
        username pve-cephfs
        fs-name cephfs
```

{% hint style="info" %}
如果未禁用 cephx，请不要忘记设置客户端的密钥文件。
{% endhint %}

## 7.15.2. 身份验证 <a href="#storage_cephfs_auth" id="storage_cephfs_auth"></a>

{% hint style="info" %}
如果 Ceph 本地安装在 Proxmox VE 集群上，添加存储时会自动完成以下操作。
{% endhint %}

如果使用默认启用的 `cephx` 身份验证，请提供一个专用身份的密钥，该身份仅具有此存储所需的权限。按照 Ceph 用户管理中的说明获取或创建该身份。  
[\[cephusermgmt\]](14-ceph-rados-block-devices.md#footnote_cephusermgmt)  
 以下示例使用 `client.pve-cephfs`；不要将 `client.admin` 用于存储客户端。

通过 SSH 将密钥本身导出到一个 Proxmox VE 节点：

```text
# ssh root@<external-ceph-server> \
    'ceph auth get-key client.pve-cephfs' > /root/cephfs.secret
```

然后将该文件和不带 `client.` 前缀的身份传递给 `pvesm`：

```text
# pvesm add cephfs <name> --monhost "10.1.1.20 10.1.1.21 10.1.1.22" \
    --fs-name cephfs --content backup --username pve-cephfs \
    --keyring /root/cephfs.secret
```

`pvesm` 成功后，删除 `/root/cephfs.secret`，因为其中包含明文密钥。

在 Web 界面中配置外部 CephFS 存储时，请将密钥粘贴到相应字段中。CephFS 使用密钥本身，而不是带有 `[client.<USER>]` 节的 RBD 密钥环格式。Proxmox VE 将密钥存储在 `/etc/pve/priv/ceph/<STORAGE_ID>.secret`。

如果外部集群轮换此身份，请在重新挂载存储之前替换已存储的密钥。本地 cephx 迁移辅助程序绝不会轮换外部集群的密钥。

## 7.15.3. 存储功能 <a href="#storage_features_11" id="storage_features_11"></a>

`cephfs` 后端是一个基于 Ceph 集群、符合 POSIX 标准的文件系统。

<table>
<caption>表 14. 后端 <code>cephfs</code> 的存储功能</caption>





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
<td><p>vztmpl iso backup snippets</p></td>
<td><p>none</p></td>
<td><p>是</p></td>
<td><p>是<sup>[1]</sup></p></td>
<td><p>否</p></td>
</tr>
</tbody>
</table>

\[1\] 尽管目前没有已知缺陷，但快照尚不能保证稳定，因为它们缺乏充分测试。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
