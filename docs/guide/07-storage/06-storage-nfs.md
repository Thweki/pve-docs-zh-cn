# 7.6. NFS 后端 <a href="#storage_nfs" id="storage_nfs"></a>

存储池类型：`nfs`

NFS 后端基于目录后端，因此二者共享大多数属性。目录布局和文件命名约定相同。主要优势在于，您可以直接配置 NFS 服务器属性，使后端能够自动挂载共享。无需修改 `/etc/fstab`。后端还可以测试服务器是否在线，并提供查询服务器所导出共享的方法。

## 7.6.1. 配置 <a href="#configuration_3" id="configuration_3"></a>

该后端支持除 shared 标志以外的所有通用存储属性，shared 标志始终处于设置状态。此外，以下属性用于配置 NFS 服务器：

**server**

服务器 IP 或 DNS 名称。为避免 DNS 查询延迟，通常最好使用 IP 地址而不是 DNS 名称，除非您有非常可靠的 DNS 服务器，或者已在本地 `/etc/hosts` 文件中列出该服务器。

**export**

NFS 导出路径（由 `pvesm nfsscan` 列出）。

您还可以设置 NFS 挂载选项：

**path**

本地挂载点（默认为 `/mnt/pve/<STORAGE_ID>/`）。

**content-dirs**

默认目录布局的覆盖设置。可选。

**options**

NFS 挂载选项（参见 `man nfs`）。

**配置示例（`/etc/pve/storage.cfg`）**

```text
nfs: iso-templates
        path /mnt/pve/iso-templates
        server 10.0.0.10
        export /space/iso-templates
        options vers=3,soft
        content iso,vztmpl
```

{% hint style="success" %}
NFS 请求超时后，默认会无限期重试 NFS 请求。这可能导致客户端出现意外挂起。对于只读内容，值得考虑使用 NFS 的 `soft` 选项，该选项将重试次数限制为三次。
{% endhint %}

## 7.6.2. 存储功能 <a href="#storage_features_2" id="storage_features_2"></a>

NFS 不支持快照，但后端利用 `qcow2` 的功能来实现快照和克隆。

<table>
<caption>表 5. 后端 <code>nfs</code> 的存储功能</caption>





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

## 7.6.3. 示例 <a href="#examples_3" id="examples_3"></a>

可以通过以下命令获取已导出的 NFS 共享列表：

```text
# pvesm scan nfs <server>
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
