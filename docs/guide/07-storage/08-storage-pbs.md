# 7.8. Proxmox Backup Server <a href="#storage_pbs" id="storage_pbs"></a>

Storage pool type: `pbs`

This backend allows direct integration of a [Proxmox Backup Server](https://www.proxmox.com/en/products/proxmox-backup-server/overview) into Proxmox VE like any other storage.

A Proxmox Backup storage can be added directly through the Proxmox VE API, CLI or the web interface.

## 7.8.1. Configuration <a href="#_configuration_5" id="_configuration_5"></a>

The backend supports all common storage properties, except the shared flag, which is always set. Additionally, the following special properties to Proxmox Backup Server are available:

**server**

Server IP or DNS name. Required.

**port**

Use this port instead of the default one, i.e. `8007`. Optional.

**username**

The username for the Proxmox Backup Server storage. Required.

{% hint style="success" %}
Do not forget to add the realm to the username. For example, `root@pam` or `archiver@pbs`.
{% endhint %}

**password**

The user password. The value will be saved in a file under `/etc/pve/priv/storage/<STORAGE-ID>.pw` with access restricted to the root user. Required.

**datastore**

The ID of the Proxmox Backup Server datastore to use. Required.

**fingerprint**

The fingerprint of the Proxmox Backup Server API TLS certificate. You can get it in the Servers Dashboard or using the `proxmox-backup-manager cert info` command. Required for self-signed certificates or any other one where the host does not trusts the servers CA.

**encryption-key**

A key to encrypt the backup data from the client side. Currently only non-password protected (no key derive function (kdf)) are supported. Will be saved in a file under `/etc/pve/priv/storage/<STORAGE-ID>.enc` with access restricted to the root user. Use the magic value `autogen` to automatically generate a new one using `proxmox-backup-client key create --kdf none <path>`. Optional.

**master-pubkey**

A public RSA key used to encrypt the backup encryption key as part of the backup task. Will be saved in a file under `/etc/pve/priv/storage/<STORAGE-ID>.master.pem` with access restricted to the root user. The encrypted copy of the backup encryption key will be appended to each backup and stored on the Proxmox Backup Server instance for recovery purposes. Optional, requires `encryption-key`.

**Configuration Example (`/etc/pve/storage.cfg`)**

```text
pbs: backup
        datastore main
        server enya.proxmox.com
        content backup
        fingerprint 09:54:ef:..snip..:88:af:47:fe:4c:3b:cf:8b:26:88:0b:4e:3c:b2
        prune-backups keep-all=1
        username archiver@pbs
        encryption-key a9:ee:c8:02:13:..snip..:2d:53:2c:98
        master-pubkey 1
```

## 7.8.2. Storage Features <a href="#_storage_features_4" id="_storage_features_4"></a>

Proxmox Backup Server only supports backups, they can be block-level or file-level based. Proxmox VE uses block-level for virtual machines and file-level for container.

<table>
<caption>Table 7. Storage features for backend <code>pbs</code></caption>





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
<td><p>backup</p></td>
<td><p>n/a</p></td>
<td><p>yes</p></td>
<td><p>n/a</p></td>
<td><p>n/a</p></td>
</tr>
</tbody>
</table>

## 7.8.3. Encryption <a href="#storage_pbs_encryption" id="storage_pbs_encryption"></a>

[![screenshot/storage-pbs-encryption-with-key.png](../../assets/screenshot-storage-pbs-encryption-with-key-png-52aa90aa5d08.png)](https://pve.proxmox.com/pve-docs/images/screenshot/storage-pbs-encryption-with-key.png)

Optionally, you can configure client-side encryption with AES-256 in GCM mode. Encryption can be configured either via the web interface, or on the CLI with the `encryption-key` option (see above). The key will be saved in the file `/etc/pve/priv/storage/<STORAGE-ID>.enc`, which is only accessible by the root user.

{% hint style="warning" %}
Without their key, backups will be inaccessible. Thus, you should keep keys ordered and in a place that is separate from the contents being backed up. It can happen, for example, that you back up an entire system, using a key on that system. If the system then becomes inaccessible for any reason and needs to be restored, this will not be possible as the encryption key will be lost along with the broken system.
{% endhint %}

It is recommended that you keep your key safe, but easily accessible, in order for quick disaster recovery. For this reason, the best place to store it is in your password manager, where it is immediately recoverable. As a backup to this, you should also save the key to a USB flash drive and store that in a secure place. This way, it is detached from any system, but is still easy to recover from, in case of emergency. Finally, in preparation for the worst case scenario, you should also consider keeping a paper copy of your key locked away in a safe place. The `paperkey` subcommand can be used to create a QR encoded version of your key. The following command sends the output of the `paperkey` command to a text file, for easy printing.

```text
# proxmox-backup-client key paperkey /etc/pve/priv/storage/<STORAGE-ID>.enc --output-format text > qrkey.txt
```

Additionally, it is possible to use a single RSA master key pair for key recovery purposes: configure all clients doing encrypted backups to use a single public master key, and all subsequent encrypted backups will contain a RSA-encrypted copy of the used AES encryption key. The corresponding private master key allows recovering the AES key and decrypting the backup even if the client system is no longer available.

{% hint style="warning" %}
The same safe-keeping rules apply to the master key pair as to the regular encryption keys. Without a copy of the private key recovery is not possible! The `paperkey` command supports generating paper copies of private master keys for storage in a safe, physical location.
{% endhint %}

Because the encryption is managed on the client side, you can use the same datastore on the server for unencrypted backups and encrypted backups, even if they are encrypted with different keys. However, deduplication between backups with different keys is not possible, so it is often better to create separate datastores.

{% hint style="info" %}
Do not use encryption if there is no benefit from it, for example, when you are running the server locally in a trusted network. It is always easier to recover from unencrypted backups.
{% endhint %}

## 7.8.4. Example: Add Storage over CLI <a href="#_example_add_storage_over_cli" id="_example_add_storage_over_cli"></a>

You can get a list of available Proxmox Backup Server datastores with:

```text
# pvesm scan pbs <server> <username> [--password <string>] [--fingerprint <string>]
```

Then you can add one of these datastores as a storage to the whole Proxmox VE cluster with:

```text
# pvesm add pbs <id> --server <server> --datastore <datastore> --username <username> --fingerprint 00:B4:... --password
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
