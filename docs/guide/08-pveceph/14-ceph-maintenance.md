# 8.14. Ceph Maintenance <a href="#_ceph_maintenance" id="_ceph_maintenance"></a>

## 8.14.1. Replace OSDs <a href="#pve_ceph_osd_replace" id="pve_ceph_osd_replace"></a>

With the following steps you can replace the disk of an OSD, which is one of the most common maintenance tasks in Ceph. If there is a problem with an OSD while its disk still seems to be healthy, read the [troubleshooting](15-pve-ceph-mon-and-ts.md#pve_ceph_mon_and_ts) section first.

1. If the disk failed, get a [recommended](03-recommendations-for-a-healthy-ceph-cluster.md#pve_ceph_recommendation_disk) replacement disk of the same type and size.
2. [Destroy](07-pve-ceph-osds.md#pve_ceph_osd_destroy) the OSD in question.
3. Detach the old disk from the server and attach the new one.
4. [Create](07-pve-ceph-osds.md#pve_ceph_osd_create) the OSD again.
5. After automatic rebalancing, the cluster status should switch back to `HEALTH_OK`. Any still listed crashes can be acknowledged by running the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph crash archive-all
```

## 8.14.2. Trim/Discard <a href="#_trim_discard" id="_trim_discard"></a>

It is good practice to run *fstrim* (discard) regularly on VMs and containers. This releases data blocks that the filesystem isn’t using anymore. It reduces data usage and resource load. Most modern operating systems issue such discard commands to their disks regularly. You only need to ensure that the Virtual Machines enable the [disk discard option](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_hard_disk_discard).

## 8.14.3. Scrub \& Deep Scrub <a href="#pveceph_scrub" id="pveceph_scrub"></a>

Ceph ensures data integrity by *scrubbing* placement groups. Ceph checks every object in a PG for its health. There are two forms of Scrubbing, daily cheap metadata checks and weekly deep data checks. The weekly deep scrub reads the objects and uses checksums to ensure data integrity. If a running scrub interferes with business (performance) needs, you can adjust the time when scrubs   
\[Ceph scrubbing [https://docs.ceph.com/en/tentacle/rados/configuration/osd-config-ref/#scrubbing](https://docs.ceph.com/en/tentacle/rados/configuration/osd-config-ref/#scrubbing)\]  
 are executed.

## 8.14.4. Mute a Health Check <a href="#pveceph_mute_health_check" id="pveceph_mute_health_check"></a>

Muting a health check keeps it visible but excludes it from the overall health status, making new problems easier to notice. Ceph continues evaluating the check. Use a duration so that a deferred warning returns automatically, for example after two weeks:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph health mute <CHECK> 2w
```

In the web interface, expand the check under **Datacenter → Ceph**, click *Mute*, and set a duration. The check stays in the list, marked as muted; use *Unmute* in the same place to restore it earlier.

By default, a mute clears when more items become affected. Enable *Keep Mute*, or add `--sticky` to the command, only if the check should stay muted in that case. This does not change the duration: a timed sticky mute still expires.

{% hint style="info" %}
Muting does not resolve the condition. You accept its risk for as long as the mute lasts.
{% endhint %}

## 8.14.5. Migrate Cephx Keys from `aes` to `aes256k` <a href="#pveceph_cephx_migration" id="pveceph_cephx_migration"></a>

This section explains how to migrate the cluster-owned keys and the keys of compatible Ceph users from `aes` to `aes256k`. For an explanation of Ceph users, tickets, and key storage, see [Cephx Authentication](11-pveceph-cephx-how-it-works.md#pveceph_cephx_how_it_works).

### Why the Health Checks Appear <a href="#_why_the_health_checks_appear" id="_why_the_health_checks_appear"></a>

Ceph Squid 19.2.6 and Ceph Tentacle 20.2.4 add health checks for keys and temporary access credentials that use the older `aes` encryption method. The checks can therefore appear directly after an upgrade even if the cluster worked without warnings before. The older method is affected by [*CVE-2025-30156*](https://docs.ceph.com/en/latest/security/CVE-2025-30156). See the upstream release announcement for background   
\[Ceph: Squid v19.2.6 and Tentacle v20.2.4 released [https://ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/](https://ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/)\]  
.

Two checks set the cluster status to *HEALTH\_ERR*. This does not mean that storage access or a Ceph service has failed. Follow the steps below to migrate to `aes256k` and, when all clients support it, disable the vulnerable method.

### Migration Steps <a href="#pveceph_cephx_migration_helper" id="pveceph_cephx_migration_helper"></a>

The migration helper checks the cluster, rotates keys, and resumes interrupted work. Review each dry run before applying its plan; add `--verbose` for full node, keyring, and device inventories and inspection diagnostics.

Reruns do not rotate completed keys again. After each run, invoke the helper without options to check the current state and follow the next steps it prints.

**Before You Begin**

- Upgrade `pve-manager` to 9.2.19 or newer and install the latest Ceph packages on every node. Staged client-key rotation requires Ceph 19.2.6-pve3, 20.2.4-pve3, or newer on every monitor.
- Then complete the rolling restart of all Ceph services.
- Resolve health warnings and errors not listed in [Health Check Reference](#pveceph_cephx_health_check_reference). Ensure every node is reachable over SSH.
- Run the helper as `root` on one node only. Do not start another migration, a rolling restart, or change Ceph keys with other tools while it runs. The helper’s lock does not block direct Ceph authentication commands.
- If Cephx is disabled on this cluster, follow [Clusters with Cephx Disabled](#pveceph_cephx_disabled) instead.

#### 1\. Migrate the Cluster-Owned Keys <a href="#_1_migrate_the_cluster_owned_keys" id="_1_migrate_the_cluster_owned_keys"></a>

Review the cluster-owned migration in the default dry-run mode:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys --rotate-cluster-keys
```

If the plan reports no blocker, apply the same selection:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys --rotate-cluster-keys --apply
```

The helper rotates the manager, metadata server, OSD, monitor, bootstrap, crash, and [encrypted OSD lockbox keys](11-pveceph-cephx-how-it-works.md#pveceph_cephx_lockbox). It restarts services one at a time when needed, including monitors. Storage-user keys and `client.admin` stay unchanged, existing tickets remain valid, and the old cipher stays enabled.

After Ceph updates its health status, the two error-severity checks clear. The warning about rotating service keys can remain for a few hours while old rotating keys expire. You do not need to wait for this warning to clear before continuing with the migration.

#### 2\. Migrate the Keys of Compatible Ceph Users <a href="#pveceph_cephx_migration_clients" id="pveceph_cephx_migration_clients"></a>

<a id="pveceph_cipher_support"></a>



**Check compatibility**

Several workloads can share one Ceph user. Migrate its key only when every client supports `aes256k`, including disconnected and external clients. Ceph programs from the updated Proxmox VE packages support it; kernel clients require a **running** kernel version 7.0 or newer.

<table>


<tbody>
<tr>
<td><p>Virtual machine with RBD disks</p></td>
<td><p>Userspace, unless <code>krbd</code> is enabled.</p></td>
</tr>
<tr>
<td><p>Container on RBD</p></td>
<td><p>Always the kernel client.</p></td>
</tr>
<tr>
<td><p>CephFS mount</p></td>
<td><p>Kernel, unless <code>fuse</code> is enabled.</p></td>
</tr>
</tbody>
</table>

Check external systems too. If any affected client is incompatible or unknown, leave its user’s key unchanged and postpone this step.

**Stage the keys**

Use `--rotate-all-storage-keys` for the dedicated users of managed local RBD and CephFS storages, together with `--rotate-admin-key` for `client.admin`, which the command line and storages without their own user share. Every client of these users is affected; storages of external clusters are excluded.

The helper stages each new key and writes it to the managed keyring and secret files. Both keys remain valid until confirmation, allowing clients to refresh before the old key is retired. If a monitor cannot keep both keys valid, the helper refuses staging and names the monitor to update or restart.

Review the combined plan:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys \
    --rotate-all-storage-keys --rotate-admin-key
```

If the plan reports no blocker, apply it:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys \
    --rotate-all-storage-keys --rotate-admin-key --apply
```

While a key is staged, do not add or downgrade monitors or change that user’s keys with other tools. Its `AUTH_INSECURE_CLIENT_KEY_TYPE` warning remains until confirmation makes the new key current and invalidates the old one.

<a id="pveceph_cephx_refresh_clients"></a>



**Refresh Clients**

- Live-migrate affected virtual machines in the web interface, or stop and start them. A guest reboot is not enough.
- Stop and start affected containers and other RBD clients.
- Let backups, restores, disk imports, and clones on Ceph storage finish before confirmation; these operations can retain the key they started with.
- The helper refreshes idle CephFS mounts and leaves busy or unresponsive mounts alone. Once nothing uses them, rerun the helper with `--apply` to retry the outstanding mounts. If your virtual machines have ISOs from a CephFS mount attached, you may have to detach the ISOs or migrate affected virtual machines to a different node to be able to refresh the CephFS mount on that node.
- For clients outside Proxmox VE, distribute the staged credential from the [managed key files](#pveceph_cephx_external_copies), then restart or remount those clients.

The helper reports sessions that may still hold an old key. Client hints are host-wide, not session attribution or a complete workload inventory. Sockets without an owning process are listed separately. Check disconnected clients and external key copies yourself.

#### 3\. Finish or Pause the Migration <a href="#pveceph_cephx_finish" id="pveceph_cephx_finish"></a>

Run a final dry run to check for remaining old-key sessions. It offers a confirmation command when its observed checks pass, but cannot verify disconnected clients or external key copies for you.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys
```

{% hint style="warning" %}
Clients that still need an old key or cipher cannot authenticate after this step. Existing IO can appear to work until a reconnect and then fail. Do not use `--force` to bypass a blocker.
{% endhint %}

After checking disconnected clients and external copies, run the exact command the dry run prints. When every rotation is ready and no key needs the old cipher, it will print the options `--apply --confirm-all-clients-refreshed
--restrict-ciphers`.

If any client remains incompatible, keep its key unchanged and the old cipher enabled rather than restricting it. You can [mute the remaining warnings](#pveceph_mute_health_check) while waiting for those clients to upgrade.

Use `pveceph auth status` for current and pending key ciphers, as `ceph auth ls` does not list pending keys.

{% hint style="info" %}
`/etc/pve/priv/cephx-key-migration.json` records progress and contains secret old keys. Protect it and keep it until the migration is complete and every client has been refreshed. Deleting it earlier loses the records needed to resume.
{% endhint %}

### Additional Migration Details <a href="#_additional_migration_details" id="_additional_migration_details"></a>

#### Health Check Reference <a href="#pveceph_cephx_health_check_reference" id="pveceph_cephx_health_check_reference"></a>

<table>



<thead>
<tr>
<th>Health check</th>
<th>Meaning</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>AUTH_INSECURE_SERVICE_KEY_TYPE</code></p></td>
<td><p>A Ceph service key uses the old cipher.</p></td>
<td><p>Run the cluster-owned migration. This check has error severity.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_SERVICE_TICKETS</code></p></td>
<td><p>Monitors issue service tickets with the old cipher.</p></td>
<td><p>Run the cluster-owned migration. This check has error severity.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_CLIENT_KEY_TYPE</code></p></td>
<td><p>The active key of a Ceph user uses the old cipher. A staged user stays listed until its rotation is confirmed.</p></td>
<td><p>Rotate the keys of compatible users and confirm them, or mute the warning.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_ROTATING_SERVICE_KEY_TYPE</code></p></td>
<td><p>A rotating service key uses the old cipher.</p></td>
<td><p>Continue the migration; old rotating keys expire automatically and do not prevent final cipher restriction.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_KEYS_ALLOWED</code></p></td>
<td><p>Monitors accept the old cipher.</p></td>
<td><p>Finish the migration, or mute the warning while old clients remain.</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_KEYS_CREATABLE</code></p></td>
<td><p>Monitors can create old-cipher keys.</p></td>
<td><p>Finish the migration, or mute the warning while old clients remain.</p></td>
</tr>
</tbody>
</table>

#### Clusters with Cephx Disabled <a href="#pveceph_cephx_disabled" id="pveceph_cephx_disabled"></a>

Ceph evaluates these health checks from the stored keys and cipher settings, also when Cephx is disabled, that is, when `auth_cluster_required`, `auth_service_required`, and `auth_client_required` are set to `none`. Disabling Cephx therefore does not clear them, and changing the authentication method interrupts existing clients, which need a restart or remount afterwards.

On a cluster with Cephx disabled:

1. Run the helper without options and apply its plan. It migrates the manager, metadata server, and OSD keys, restarting services one at a time when needed, and switches the service tickets to the new cipher. This clears both error-severity checks. If an old `mon.` key is stored in the authentication database, the helper instead refuses and asks you to migrate that key first.
2. Optionally, migrate the bootstrap and crash keys with `--rotate-client-keys`.
3. Mute the remaining warnings without a duration. While Cephx is disabled, the helper does not migrate the keys of other Ceph users, as their clients do not authenticate with Cephx:

   Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

   ```text
   ceph health mute AUTH_INSECURE_CLIENT_KEY_TYPE --sticky
   ceph health mute AUTH_INSECURE_KEYS_ALLOWED --sticky
   ceph health mute AUTH_INSECURE_KEYS_CREATABLE --sticky
   ```

Do not restrict the allowed ciphers or forbid creating old-cipher keys by hand while the preferred cipher is still `aes`, as creating keys then fails.

Before you enable Cephx again, unmute these checks and make sure that every monitor, Ceph service, and client still has a key file matching the authentication database. Restart the monitors first, then all other Ceph services, and restart or remount the clients. Then run the migration as described in [Migration Steps](#pveceph_cephx_migration_helper).

#### Staged Keys and Confirmation <a href="#pveceph_cephx_staged_keys" id="pveceph_cephx_staged_keys"></a>

The helper disables automatic promotion of pending client keys so that the monitors keep both credentials valid. An older monitor would promote a staged key on its first use and end the grace period for the whole cluster. The helper therefore stages only when every monitor supports the feature and checks this again on every run.

With `--apply`, `--confirm-all-clients-refreshed` makes every staged key current and invalidates its previous key. The initial check refuses the entire batch if any open rotation is not ready. The helper then rechecks each key before retiring its old credential. If a client returns during the batch, completed rotations stay committed and the blocked key stays staged. To confirm ready users separately, use `--confirm-clients-refreshed <USER>` with `--apply`.

Ceph 19.2.6-pve4 and 20.2.4-pve4 or newer monitors can identify each session’s key, allowing refreshed clients to stay connected during forward or rollback confirmation. Upgrade and restart older monitors to use this feature. Without key identification, every visible client of that user must disconnect before confirmation; upgrading is preferable for a shared user such as `client.admin`.

#### Key Copies for External Clients <a href="#pveceph_cephx_external_copies" id="pveceph_cephx_external_copies"></a>

For an external client of the local cluster, copy the staged credential from the managed file for its Ceph user:

- RBD keyring: `/etc/pve/priv/ceph/<STORAGE_ID>.keyring`
- CephFS bare secret: `/etc/pve/priv/ceph/<STORAGE_ID>.secret`
- Administrative keyring: `/etc/pve/priv/ceph.client.admin.keyring`

Use the credential for that user, not `client.admin` as a substitute. Transfer it securely and update every saved copy before refreshing the client. Storage backed by an external cluster is different: the helper never rotates that cluster’s keys. Follow its administrator’s key-rotation procedure.

A storage with `monhost` set counts as external even if its monitors belong to the local cluster, so the helper does not update its key copy. If that copy holds the key of a Ceph user you migrate, update it with the staged key of the same user before confirming, or with the restored key before confirming a rollback. The helper refuses to retire a key it finds in a storage key copy; verify copies it cannot check yourself.

The helper lists local users not managed by Proxmox VE separately. Follow their client’s supported rotation procedure, or leave their keys unchanged and keep the old cipher enabled.

#### Roll Back a Staged Client Key <a href="#pveceph_cephx_rollback" id="pveceph_cephx_rollback"></a>

To return a staged user to its current key:

1. Run the helper with `--abort-staged-key <USER> --apply`. It restores the current key to every managed copy while both credentials remain valid.
2. Refresh all clients back to that key, including disconnected clients and external key copies. The helper retries managed CephFS mounts as during forward migration.
3. Run the helper with `--confirm-abort-clients-refreshed <USER> --apply` to retire the staged key. The helper refuses if monitor session collection is incomplete, a visible session uses the staged key, its key is unknown, or a storage key copy still holds the staged key.

#### Emergency Cipher Override <a href="#_emergency_cipher_override" id="_emergency_cipher_override"></a>

Monitors normally use the `auth_allowed_ciphers` list stored in the MonMap to decide which key ciphers may authenticate. The local startup option `mon_auth_emergency_allowed_ciphers` replaces that list for a monitor. It can temporarily allow the cipher of an existing administrative key after an incorrect restriction locked administrators out   
\[Ceph: Emergency Allowed Ciphers [https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#emergency-allowed-ciphers](https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#emergency-allowed-ciphers)\]  
.

Ceph raises `AUTH_EMERGENCY_CIPHERS_SET` while this override is configured. The helper refuses the final restriction because changing the MonMap would not take effect. Use the override only to recover access, then repair the normal configuration, remove it from `/etc/pve/ceph.conf`, and restart every monitor before the final dry run.

#### Interrupted Runs and Manual Fallback <a href="#_interrupted_runs_and_manual_fallback" id="_interrupted_runs_and_manual_fallback"></a>

After an interruption, run the helper without options once the affected nodes are reachable. Unfinished key updates can resume while their daemons are stopped. Keep the journal unchanged and follow the printed next steps rather than starting a manual rotation. Check the affected nodes and service logs rather than assuming a down daemon’s key needs repair.

If the helper still cannot proceed, install the latest `pve-manager` and retry. Contact Proxmox support before editing the journal or keyrings, or before using the upstream Cephx key migration procedure   
\[Ceph documentation: [https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#cephx-upgrade](https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#cephx-upgrade)\]  
. That procedure changes the Ceph authentication database, but does not account for these Proxmox VE details:

- Ensure every managed key copy below `/etc/pve/priv` and `/var/lib/ceph` contains the key that Ceph accepts. Merge changes into `/etc/pve/priv/ceph.mon.keyring`; never overwrite it.
- Update an encrypted OSD’s lockbox key in both the authentication database and its block-device LVM tag. Its temporary keyring is not the persistent copy.
- Refresh every client before invalidating its previous Ceph user key.
- Rotate `client.admin` last and prepare an independently tested recovery user before changing it.

Use manual key-rotation or cipher-restriction commands only with a complete, tested recovery plan that covers every item above.

## 8.14.6. Shutdown Proxmox VE \+ Ceph HCI Cluster <a href="#pveceph_shutdown" id="pveceph_shutdown"></a>

To shut down the whole Proxmox VE \+ Ceph cluster, first stop all Ceph clients. These will mainly be VMs and containers. If you have additional clients that might access a Ceph FS or an installed RADOS GW, stop these as well. Highly available guests will switch their state to *stopped* when powered down via the Proxmox VE tooling.

Once all clients, VMs and containers are off or not accessing the Ceph cluster anymore, verify that the Ceph cluster is in a healthy state. Either via the Web UI or the CLI:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph -s
```

In order to not cause any recovery during the shut down and later power on phases, enable the *noout* OSD flag. Either in the **Ceph → OSD** panel behind the **Manage Global Flags** button or the CLI:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd set noout
```

Start powering down your nodes without a monitor (MON). After these nodes are down, continue by shutting down nodes with monitors on them.

When powering on the cluster, start the nodes with monitors (MONs) first. Once all nodes are up and running, confirm that all Ceph services are up and running. In the end, the only warning you should see for Ceph is that the *noout* flag is still set. You can disable it via the web UI or via the CLI:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd unset noout
```

You can now start up the guests. Highly available guests will change their state to *started* when they power on.

## 8.14.7. Network Changes <a href="#pveceph_network_change" id="pveceph_network_change"></a>

It is possible to change the networks used by Ceph in a HCI setup without any downtime if **both the old and new networks can be configured at the same time**.

The procedure differs depending on which network you want to change.

{% hint style="info" %}
A word of caution! It is critical that the change of the used networks by Ceph is being done carefully. Otherwise it could lead to a broken Ceph cluster with downtime to get it back into a working state! We recommend doing a trial run of the procedure in a (virtual) test cluster before changing the production infrastructure.
{% endhint %}

After the new network has been configured on all hosts, make sure you test it before proceeding with the changes. One way is to ping all hosts on the new network. If you use a large MTU, make sure to also test that it works. For example by sending ping packets that will result in a final packet at the max MTU size.

To test an MTU of 9000, you will need the following packet sizes:

{% hint style="info" %}
We assume a simple network configuration. In more complicated setups, you might need to configure a lower MTU to account for any headers that might be added once a packet leaves the host.
{% endhint %}

<table>
<tr>
<td>IPv4 <br/></td>
<td>
<p>The overhead of IP and ICMP is <em>28</em> bytes; the resulting packet size for the ping then is <em>8972</em> bytes.</p>
</td>
</tr>
<tr>
<td>IPv6 <br/></td>
<td>
<p>The overhead is <em>48</em> bytes and the resulting packet size is <em>8952</em> bytes.</p>
</td>
</tr>
</table>

The resulting ping command will look like this for an IPv4:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ping -M do -s 8972 {target IP}
```

When you are switching between IPv4 and IPv6 networks, you need to make sure that the following options in the `ceph.conf` file are correctly set to `true` or `false`. These config options configure if Ceph services should bind to IPv4 or IPv6 addresses.

```text
ms_bind_ipv4 = true
ms_bind_ipv6 = false
```

### Change the Ceph Public Network <a href="#pveceph_network_change_public" id="pveceph_network_change_public"></a>

The Ceph Public network is the main communication channel in a Ceph cluster between the different services and clients (for example, a VM). Changing it to a different network is not as simple as changing the Ceph Cluster network. The main reason is that besides the configuration in the `ceph.conf` file, the Ceph MONs (monitors) have an internal configuration where they keep track of all the other MONs that are part of the cluster, the *monmap*.

Therefore, the procedure to change the Ceph Public network is a bit more involved:

1. Change `public_network` in the `/etc/pve/ceph.conf` file (do not change any other value)
2. Restart non MON services: OSDs, MGRs and MDS on one host
3. Wait until Ceph is back to *HEALTH\_OK*
4. Verify services are using the new network
5. Continue restarting services on the next host
6. Destroy one MON
7. Recreate MON
8. Wait until Ceph is back to *HEALTH\_OK*
9. Continue destroying and recreating MONs

You first need to edit the `/etc/pve/ceph.conf` file. Change the `public_network` line to match the new subnet.

```text
public_network = 10.9.9.30/24
```

{% hint style="warning" %}
Do not change the `mon_host` line or any `[mon.HOSTNAME]` sections. These will be updated automatically when the MONs are destroyed and recreated.
{% endhint %}

{% hint style="info" %}
Don’t worry if the host bits (for example, the last octet) are set by default, the netmask in CIDR notation defines the network part.
{% endhint %}

After you have changed the network, you need to restart the non MON services in the cluster for the changes to take effect. Do so one node at a time! To restart all non MON services on one node, you can use the following commands on that node. Ceph has `systemd` targets for each type of service.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
systemctl restart ceph-osd.target
systemctl restart ceph-mgr.target
systemctl restart ceph-mds.target
```

{% hint style="info" %}
You will only have MDS daemons (Metadata Servers) if you use CephFS.
{% endhint %}

{% hint style="info" %}
After the first OSD service got restarted, the GUI will complain that the OSD is not reachable anymore. This is not an issue; VMs can still reach them. The reason for the message is that the MGR service cannot reach the OSD anymore. The error will vanish after the MGR services get restarted.
{% endhint %}

{% hint style="warning" %}
Do not restart OSDs on multiple hosts at the same time. Chances are that for some PGs (placement groups), 2 out of the (default) 3 replicas will be down. This will result in I/O being halted until the minimum required number (`min_size`) of replicas is available again.
{% endhint %}

To verify that the services are listening on the new network, you can run the following command on each node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ss -tulpn | grep ceph
```

{% hint style="info" %}
Since OSDs will also listen on the Ceph Cluster network, expect to see that network too in the output of `ss -tulpn`.
{% endhint %}

Once the Ceph cluster is back in a fully healthy state (*HEALTH\_OK*), and the services are listening on the new network, continue to restart the services on the host.

The last services that need to be moved to the new network are the Ceph MONs themselves. The easiest way is to destroy and recreate each monitor one by one. This way, any mention of it in the `ceph.conf` and the monitor internal `monmap` is handled automatically.

Destroy the first MON and create it again. Wait a few moments before you continue on to the next MON in the cluster, and make sure the cluster reports *HEALTH\_OK* before proceeding.

Once all MONs are recreated, you can verify that any mention of MONs in the `ceph.conf` file references the new network. That means mainly the `mon_host` line and the `[mon.HOSTNAME]` sections.

One final `ss -tulpn | grep ceph` should show that the old network is not used by any Ceph service anymore.

### Change the Ceph Cluster Network <a href="#pveceph_network_change_cluster" id="pveceph_network_change_cluster"></a>

The Ceph Cluster network is used for the replication traffic between the OSDs. Therefore, it can be beneficial to place it on its own fast physical network.

The overall procedure is:

1. Change `cluster_network` in the `/etc/pve/ceph.conf` file
2. Restart OSDs on one host
3. Wait until Ceph is back to *HEALTH\_OK*
4. Verify OSDs are using the new network
5. Continue restarting OSDs on the next host

You first need to edit the `/etc/pve/ceph.conf` file. Change the `cluster_network` line to match the new subnet.

```text
cluster_network = 10.9.9.30/24
```

{% hint style="info" %}
Don’t worry if the host bits (for example, the last octet) are set by default; the netmask in CIDR notation defines the network part.
{% endhint %}

After you have changed the network, you need to restart the OSDs in the cluster for the changes to take effect. Do so one node at a time! To restart all OSDs on one node, you can use the following command on the CLI on that node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
systemctl restart ceph-osd.target
```

{% hint style="warning" %}
Do not restart OSDs on multiple hosts at the same time. Chances are that for some PGs (placement groups), 2 out of the (default) 3 replicas will be down. This will result in I/O being halted until the minimum required number (`min_size`) of replicas is available again.
{% endhint %}

To verify that the OSD services are listening on the new network, you can either check the **OSD Details → Network** tab in the **Ceph → OSD** panel or by running the following command on the host:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ss -tulpn | grep ceph-osd
```

{% hint style="info" %}
Since OSDs will also listen on the Ceph Public network, expect to see that network too in the output of `ss -tulpn`.
{% endhint %}

Once the Ceph cluster is back in a fully healthy state (*HEALTH\_OK*), and the OSDs are listening on the new network, continue to restart the OSDs on the next host.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
