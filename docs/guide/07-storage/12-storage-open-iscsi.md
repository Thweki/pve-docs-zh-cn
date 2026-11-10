# 7.12. Open-iSCSI initiator <a href="#storage_open_iscsi" id="storage_open_iscsi"></a>

Storage pool type: `iscsi`

iSCSI is a widely employed technology used to connect to storage servers. Almost all storage vendors support iSCSI. There are also open source iSCSI target solutions available, e.g. [OpenMediaVault](https://www.openmediavault.org/), which is based on Debian.

To use this backend, you need to install the [Open-iSCSI](https://www.open-iscsi.com/) (`open-iscsi`) package. This is a standard Debian package, but it is not installed by default to save resources.

```text
# apt-get install open-iscsi
```

Low-level iscsi management task can be done using the `iscsiadm` tool.

## 7.12.1. Configuration <a href="#_configuration_8" id="_configuration_8"></a>

The backend supports the common storage properties `content`, `nodes`, `disable`, and the following iSCSI specific properties:

**portal**

iSCSI portal (IP or DNS name with optional port).

**target**

iSCSI target.

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
iscsi: mynas
     portal 10.10.10.1
     target iqn.2006-01.openfiler.com:tsn.dcb5aaaddd
     content none
```

{% hint style="success" %}
If you want to use LVM on top of iSCSI, it make sense to set `content none`. That way it is not possible to create VMs using iSCSI LUNs directly.
{% endhint %}

## 7.12.2. File naming conventions <a href="#_file_naming_conventions_5" id="_file_naming_conventions_5"></a>

The iSCSI protocol does not define an interface to allocate or delete data. Instead, that needs to be done on the target side and is vendor specific. The target simply exports them as numbered LUNs. So Proxmox VE iSCSI volume names just encodes some information about the LUN as seen by the linux kernel.

## 7.12.3. Storage Features <a href="#_storage_features_8" id="_storage_features_8"></a>

iSCSI is a block level type storage, and provides no management interface. So it is usually best to export one big LUN, and setup LVM on top of that LUN. You can then use the LVM plugin to manage the storage on that iSCSI LUN.

<table>
<caption>Table 11. Storage features for backend <code>iscsi</code></caption>





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
<td><p>images none</p></td>
<td><p>raw</p></td>
<td><p>yes</p></td>
<td><p>no</p></td>
<td><p>no</p></td>
</tr>
</tbody>
</table>

## 7.12.4. Examples <a href="#_examples_8" id="_examples_8"></a>

You can scan a remote iSCSI portal and get a list of possible targets with:

```text
pvesm scan iscsi <HOST[:PORT]>
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
