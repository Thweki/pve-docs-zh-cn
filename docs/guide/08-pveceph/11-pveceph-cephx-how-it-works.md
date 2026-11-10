# 8.11. Cephx 身份验证 <a href="#pveceph_cephx_how_it_works" id="pveceph_cephx_how_it_works"></a>

Cephx [\[1\]](#note-997034e4-1)用于保护对 Ceph 集群的访问。

每个 Ceph 服务和客户端（包括存储使用方和工具）都以 Ceph 用户（例如 `client.admin` 或 `osd.3`）的身份，使用该用户的长期密钥向监视器进行身份验证。随后，监视器会签发称为票据的临时凭据：

<table>


<thead>
<tr>
<th>术语</th>
<th>用途</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>用户密钥</p></td>
<td><p>客户端或 Ceph 服务用于向监视器进行身份验证的长期密钥。</p></td>
</tr>
<tr>
<td><p>监视器票据</p></td>
<td><p>允许经过身份验证的 Ceph 用户请求 Ceph 服务的票据。</p></td>
</tr>
<tr>
<td><p>服务票据</p></td>
<td><p>授予对 OSD、管理器或元数据服务器的临时访问权限。</p></td>
</tr>
<tr>
<td><p>轮换服务密钥</p></td>
<td><p>允许 Ceph 服务验证服务票据。监视器会自动替换这些密钥。</p></td>
</tr>
</tbody>
</table>

运行中的客户端通常仅在启动时读取其用户密钥。更新已保存的密钥或密钥环文件并不会更新该进程。现有票据和连接也可能在一段时间内继续可用。因此，密钥轮换必须考虑正在运行以及暂时断开连接的客户端。

## 8.11.1. 密钥环位置 <a href="#pveceph_keyrings" id="pveceph_keyrings"></a>

在 Proxmox VE Ceph 集群中，权威的 `client.admin` 密钥环是 `/etc/pve/priv/ceph.client.admin.keyring`，而不是 `/etc/ceph` 中的副本。[Proxmox 集群文件系统（pmxcfs）](../06-pmxcfs/README.md)会将其同步到每个节点。受管 Ceph 存储的凭据位于 `/etc/pve/priv/ceph/` 下。

`/var/lib/ceph` 下方的密钥环属于一个 Ceph 服务，并且仅位于其所在节点本地。`/etc/pve/priv/ceph.mon.keyring` 同时包含共享的 `mon.` 密钥和 `client.admin`。请始终将更新合并到此文件中，而不是覆盖该文件。`pveceph mon create` 在初始化监视器时会使用其 `mon.` 条目。

## 8.11.2. 加密 OSD 锁箱密钥 <a href="#pveceph_cephx_lockbox" id="pveceph_cephx_lockbox"></a>

每个加密 OSD 都使用一个名为 `client.osd-lockbox.<UUID>` 的专用 Ceph 用户。其身份验证密钥称为锁箱密钥。它不是磁盘加密密钥本身：它使 OSD 能够从 Ceph 检索该密钥，并在启动时解锁其存储。Ceph 和 OSD 的块设备中必须包含相匹配的锁箱密钥副本。

{% hint style="warning" %}
切勿仅使用 `ceph auth` 轮换锁箱密钥。请使用迁移辅助工具，它会验证 OSD 身份并同时更新两份副本。
{% endhint %}

## 注释

### 注释 1 <a href="#note-997034e4-1" id="note-997034e4-1"></a>

Cephx 授权和身份验证协议 [https://docs.ceph.com/en/tentacle/dev/cephx\_protocol/](https://docs.ceph.com/en/tentacle/dev/cephx_protocol/)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
