# 7.6. NFS Backend <a href="#storage_nfs" id="storage_nfs"></a>

Storage pool type: `nfs`

The NFS backend is based on the directory backend, so it shares most properties. The directory layout and the file naming conventions are the same. The main advantage is that you can directly configure the NFS server properties, so the backend can mount the share automatically. There is no need to modify `/etc/fstab`. The backend can also test if the server is online, and provides a method to query the server for exported shares.

## 7.6.1. Configuration <a href="#_configuration_3" id="_configuration_3"></a>

The backend supports all common storage properties, except the shared flag, which is always set. Additionally, the following properties are used to configure the NFS server:

**server**

Server IP or DNS name. To avoid DNS lookup delays, it is usually preferable to use an IP address instead of a DNS name - unless you have a very reliable DNS server, or list the server in the local `/etc/hosts` file.

**export**

NFS export path (as listed by `pvesm nfsscan`).

You can also set NFS mount options:

**path**

The local mount point (defaults to `/mnt/pve/<STORAGE_ID>/`).

**content-dirs**

Overrides for the default directory layout. Optional.

**options**

NFS mount options (see `man nfs`).

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
nfs: iso-templates
        path /mnt/pve/iso-templates
        server 10.0.0.10
        export /space/iso-templates
        options vers=3,soft
        content iso,vztmpl
```

{% hint style="success" %}
After an NFS request times out, NFS request are retried indefinitely by default. This can lead to unexpected hangs on the client side. For read-only content, it is worth to consider the NFS `soft` option, which limits the number of retries to three.
{% endhint %}

## 7.6.2. Storage Features <a href="#_storage_features_2" id="_storage_features_2"></a>

NFS does not support snapshots, but the backend uses `qcow2` features to implement snapshots and cloning.

<table>
<caption>Table 5. Storage features for backend <code>nfs</code></caption>





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
<td><p>images rootdir vztmpl iso backup snippets</p></td>
<td><p>raw qcow2 vmdk</p></td>
<td><p>yes</p></td>
<td><p>qcow2</p></td>
<td><p>qcow2</p></td>
</tr>
</tbody>
</table>

## 7.6.3. Examples <a href="#_examples_3" id="_examples_3"></a>

You can get a list of exported NFS shares with:

```text
# pvesm scan nfs <server>
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
