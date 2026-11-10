# 7.13. 用户模式 iSCSI 后端 <a href="#storage_iscsidirect" id="storage_iscsidirect"></a>

存储池类型：`iscsidirect`

此后端提供的功能基本上与 Open-iSCSI 后端相同，但使用用户级库实现。需要安装 `libiscsi-bin` 软件包才能使用此后端。

需要注意的是，这不涉及任何内核驱动程序，因此可以将其视为一种性能优化。但缺点是，无法在此类 iSCSI LUN 之上使用 LVM。因此，需要在存储服务器端管理所有空间分配。

## 7.13.1. 配置 <a href="#_configuration_9" id="_configuration_9"></a>

用户模式 iSCSI 后端使用与 Open-iSCSI 后端相同的配置选项。

**配置示例（`/etc/pve/storage.cfg`）**

```text
iscsidirect: faststore
     portal 10.10.10.1
     target iqn.2006-01.openfiler.com:tsn.dcb5aaaddd
```

## 7.13.2. 存储功能 <a href="#_storage_features_9" id="_storage_features_9"></a>

{% hint style="info" %}
此后端仅适用于 VM。容器无法使用此驱动程序。
{% endhint %}

<table>
<caption>表 12. 后端 <code>iscsidirect</code> 的存储功能</caption>





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
<td><p>否</p></td>
<td><p>否</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
