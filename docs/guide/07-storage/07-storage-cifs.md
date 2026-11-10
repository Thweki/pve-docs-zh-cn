# 7.7. CIFS 后端 <a href="#storage_cifs" id="storage_cifs"></a>

存储池类型：`cifs`

CIFS 后端扩展了目录后端，因此无需手动设置 CIFS 挂载。可以通过 Proxmox VE API 或 Web 界面直接添加此类存储，并享有我们后端的所有优势，例如服务器心跳检查或便捷地选择导出的共享。

## 7.7.1. 配置 <a href="#_configuration_4" id="_configuration_4"></a>

该后端支持除 shared 标志以外的所有通用存储属性，shared 标志始终处于设置状态。此外，还提供以下 CIFS 特有属性：

**server**

服务器 IP 或 DNS 名称。必需。

{% hint style="success" %}
为避免 DNS 查询延迟，通常最好使用 IP 地址而不是 DNS 名称，除非您有非常可靠的 DNS 服务器，或者已在本地 `/etc/hosts` 文件中列出该服务器。
{% endhint %}

**share**

要使用的 CIFS 共享（通过 `pvesm scan cifs <address>` 或 Web 界面获取可用共享）。必需。

**username**

CIFS 存储的用户名。可选，默认为“guest”。

**password**

用户密码。可选。密码将保存在只有 root 可读的文件中（`/etc/pve/priv/storage/<STORAGE-ID>.pw`）。

**domain**

为此存储设置用户域（工作组）。可选。

**smbversion**

SMB 协议版本。可选，设置为 `default` 或未设置时，协商客户端和服务器均支持的最高 SMB2\+ 版本。由于安全问题，不支持 SMB1。

**path**

本地挂载点。可选，默认为 `/mnt/pve/<STORAGE_ID>/`。

**content-dirs**

默认目录布局的覆盖设置。可选。

**options**

其他 CIFS 挂载选项（参见 `man mount.cifs`）。某些选项会自动设置，不应在此处设置。Proxmox VE 将始终设置 `soft` 选项。根据配置，以下选项会自动设置：`username`、`credentials`、`guest`、`domain`、`vers`。

**subdir**

要挂载的共享子目录。可选，默认为共享的根目录。

**配置示例（`/etc/pve/storage.cfg`）**

```text
cifs: backup
        path /mnt/pve/backup
        server 10.0.0.11
        share VMData
        content backup
        options noserverino,echo_interval=30
        username anna
        smbversion 3
        subdir /data
```

## 7.7.2. 存储功能 <a href="#_storage_features_3" id="_storage_features_3"></a>

CIFS 在存储级别不支持快照。但如果仍希望使用快照和克隆功能，可以使用 `qcow2` 后备文件。

<table>
<caption>表 6. 后端 <code>cifs</code> 的存储功能</caption>





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
<td><p>images rootdir vztmpl iso backup snippets</p></td>
<td><p>raw qcow2 vmdk</p></td>
<td><p>是</p></td>
<td><p>qcow2</p></td>
<td><p>qcow2</p></td>
</tr>
</tbody>
</table>

## 7.7.3. 示例 <a href="#_examples_4" id="_examples_4"></a>

可以通过以下命令获取已导出的 CIFS 共享列表：

```text
# pvesm scan cifs <server> [--username <username>] [--password]
```

然后，可以通过以下命令将其中一个共享作为存储添加到整个 Proxmox VE 集群：

```text
# pvesm add cifs <storagename> --server <server> --share <share> [--username <username>] [--password]
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
