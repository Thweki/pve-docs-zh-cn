# 7.13. User Mode iSCSI Backend <a href="#storage_iscsidirect" id="storage_iscsidirect"></a>

Storage pool type: `iscsidirect`

This backend provides basically the same functionality as the Open-iSCSI backed, but uses a user-level library to implement it. You need to install the `libiscsi-bin` package in order to use this backend.

It should be noted that there are no kernel drivers involved, so this can be viewed as performance optimization. But this comes with the drawback that you cannot use LVM on top of such iSCSI LUN. So you need to manage all space allocations at the storage server side.

## 7.13.1. Configuration <a href="#_configuration_9" id="_configuration_9"></a>

The user mode iSCSI backend uses the same configuration options as the Open-iSCSI backed.

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
iscsidirect: faststore
     portal 10.10.10.1
     target iqn.2006-01.openfiler.com:tsn.dcb5aaaddd
```

## 7.13.2. Storage Features <a href="#_storage_features_9" id="_storage_features_9"></a>

{% hint style="info" %}
This backend works with VMs only. Containers cannot use this driver.
{% endhint %}

<table>
<caption>Table 12. Storage features for backend <code>iscsidirect</code></caption>





<thead>
<tr>
<th>Content types</th>
<th>Image formats</th>
<th>Shared</th>
<th>Snapshots</th>
<th>Clones</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>images</p></td>
<td><p>raw</p></td>
<td><p>yes</p></td>
<td><p>no</p></td>
<td><p>no</p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
