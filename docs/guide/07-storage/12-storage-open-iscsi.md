# 7.12. Open-iSCSI 启动器 <a href="#storage_open_iscsi" id="storage_open_iscsi"></a>

存储池类型：`iscsi`

iSCSI 是一种广泛用于连接存储服务器的技术。几乎所有存储厂商都支持 iSCSI。此外，还有开源的 iSCSI 目标端解决方案，例如基于 Debian 的 [OpenMediaVault](https://www.openmediavault.org/)。

要使用此后端，需要安装 [Open-iSCSI](https://www.open-iscsi.com/)（`open-iscsi`）软件包。这是标准的 Debian 软件包，但为节省资源，默认不会安装。

```text
# apt-get install open-iscsi
```

可以使用 `iscsiadm` 工具执行底层 iSCSI 管理任务。

## 7.12.1. 配置 <a href="#_configuration_8" id="_configuration_8"></a>

后端支持通用存储属性 `content`、`nodes`、`disable`，以及以下 iSCSI 特定属性：

**门户**

iSCSI 门户（IP 或 DNS 名称，可选端口）。

**目标端**

iSCSI 目标端。

**配置示例（`/etc/pve/storage.cfg`）**

```text
iscsi: mynas
     portal 10.10.10.1
     target iqn.2006-01.openfiler.com:tsn.dcb5aaaddd
     content none
```

{% hint style="success" %}
如果要在 iSCSI 之上使用 LVM，设置 `content none` 是合理的。这样就无法直接使用 iSCSI LUN 创建 VM。
{% endhint %}

## 7.12.2. 文件命名约定 <a href="#_file_naming_conventions_5" id="_file_naming_conventions_5"></a>

iSCSI 协议未定义用于分配或删除数据的接口。相反，这些操作需要在目标端完成，并且因厂商而异。目标端只是将它们导出为带编号的 LUN。因此，Proxmox VE 的 iSCSI 卷名称仅编码 Linux 内核所看到的 LUN 的一些信息。

## 7.12.3. 存储功能 <a href="#_storage_features_8" id="_storage_features_8"></a>

iSCSI 是块级存储，不提供管理接口。因此，通常最好导出一个大型 LUN，并在该 LUN 之上配置 LVM。然后，就可以使用 LVM 插件管理该 iSCSI LUN 上的存储。

<table>
<caption>表 11. 后端 <code>iscsi</code> 的存储功能</caption>





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
<td><p>images none</p></td>
<td><p>raw</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
</tr>
</tbody>
</table>

## 7.12.4. 示例 <a href="#_examples_8" id="_examples_8"></a>

可以使用以下命令扫描远程 iSCSI 门户并获取可能的目标端列表：

```text
pvesm scan iscsi <HOST[:PORT]>
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
