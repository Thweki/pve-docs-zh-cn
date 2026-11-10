# 8.9. Ceph Pools <a href="#pve_ceph_pools" id="pve_ceph_pools"></a>

[![screenshot/gui-ceph-pools.png](../../assets/screenshot-gui-ceph-pools-png-4290e2ffb7bf.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-pools.png)

A pool is a logical group for storing objects. It holds a collection of objects, known as **P**lacement **G**roups (`PG`, `pg_num`).

## 8.9.1. Create and Edit Pools <a href="#_create_and_edit_pools" id="_create_and_edit_pools"></a>

You can create and edit pools from the command line or the web interface of any Proxmox VE host under **Ceph → Pools**.

When no options are given, we set a default of **128 PGs**, a **size of 3 replicas** and a **min_size of 2 replicas**, to ensure no data loss occurs if any OSD fails.

{% hint style="warning" %}
**Do not set a min_size of 1**. A replicated pool with min_size of 1 allows I/O on an object when it has only 1 replica, which could lead to data loss, incomplete PGs or unfound objects.
{% endhint %}

It is advised that you either enable the PG-Autoscaler or calculate the PG number based on your setup. You can find the formula and the PG calculator   
[PG calculator [https://web.archive.org/web/20210301111112/http://ceph.com/pgcalc/](https://web.archive.org/web/20210301111112/http://ceph.com/pgcalc/)]  
 online. From Ceph Nautilus onward, you can change the number of PGs <a id="_footnote_placement_groups"></a>  
[Placement Groups [https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/](https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/)]  
 after the setup.

The PG autoscaler <a id="_footnote_autoscaler"></a>  
[Automated Scaling [https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/#automated-scaling](https://docs.ceph.com/en/tentacle/rados/operations/placement-groups/#automated-scaling)]  
 can automatically scale the PG count for a pool in the background. Setting the `Target Size` or `Target Ratio` advanced parameters helps the PG-Autoscaler to make better decisions.

**Example for creating a pool over the CLI**

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool create <pool-name> --add_storages
```

{% hint style="success" %}
If you would also like to automatically define a storage for your pool, keep the ‘Add as Storage’ checkbox checked in the web interface, or use the command-line option *--add_storages* at pool creation.
{% endhint %}

### Pool Options <a href="#_pool_options" id="_pool_options"></a>

[![screenshot/gui-ceph-pool-create.png](../../assets/screenshot-gui-ceph-pool-create-png-020d880342d1.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-pool-create.png)

The following options are available on pool creation, and partially also when editing a pool.

**Name**

The name of the pool. This must be unique and can’t be changed afterwards.

**Size**

The number of replicas per object. Ceph always tries to have this many copies of an object. Default: `3`.

**PG Autoscale Mode**

The automatic PG scaling mode   
[[autoscaler]](#_footnote_autoscaler)  
 of the pool. If set to `warn`, it produces a warning message when a pool has a non-optimal PG count. Default: `warn`.

**Add as Storage**

Configure a VM or container storage using the new pool. Default: `true` (only visible on creation).

**Advanced Options**

**Min. Size**

The minimum number of replicas per object. Ceph will reject I/O on the pool if a PG has less than this many replicas. Default: `2`.

**Crush Rule**

The rule to use for mapping object placement in the cluster. These rules define how data is placed within the cluster. See [Ceph CRUSH & device classes](10-pve-ceph-device-classes.md#pve_ceph_device_classes) for information on device-based rules.

**# of PGs**

The number of placement groups   
[[placement_groups]](#_footnote_placement_groups)  
 that the pool should have at the beginning. Default: `128`.

**Target Ratio**

The ratio of data that is expected in the pool. The PG autoscaler uses the ratio relative to other ratio sets. It takes precedence over the `target size` if both are set.

**Target Size**

The estimated amount of data expected in the pool. The PG autoscaler uses this size to estimate the optimal PG count.

**Min. # of PGs**

The minimum number of placement groups. This setting is used to fine-tune the lower bound of the PG count for that pool. The PG autoscaler will not merge PGs below this threshold.

Further information on Ceph pool handling can be found in the Ceph pool operation   
[Ceph pool operation [https://docs.ceph.com/en/tentacle/rados/operations/pools/](https://docs.ceph.com/en/tentacle/rados/operations/pools/)]  
 manual.

## 8.9.2. Erasure Coded Pools <a href="#pve_ceph_ec_pools" id="pve_ceph_ec_pools"></a>

Erasure coding (EC) is a form of ‘forward error correction’ codes that allows to recover from a certain amount of data loss. Erasure coded pools can offer more usable space compared to replicated pools, but they do that for the price of performance.

For comparison: in classic, replicated pools, multiple replicas of the data are stored (`size`) while in erasure coded pool, data is split into `k` data chunks with additional `m` coding (checking) chunks. Those coding chunks can be used to recreate data should data chunks be missing.

The number of coding chunks, `m`, defines how many OSDs can be lost without losing any data. The total amount of objects stored is `k + m`.

### Creating EC Pools <a href="#_creating_ec_pools" id="_creating_ec_pools"></a>

Erasure coded (EC) pools can be created with the `pveceph` CLI tooling. Planning an EC pool needs to account for the fact, that they work differently than replicated pools.

The default `min_size` of an EC pool depends on the `m` parameter. If `m = 1`, the `min_size` of the EC pool will be `k`. The `min_size` will be `k + 1` if `m > 1`. The Ceph documentation recommends a conservative `min_size` of `k + 2`   
[Ceph Erasure Coded Pool Recovery [https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-coded-pool-recovery](https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-coded-pool-recovery)]  
.

If there are less than `min_size` OSDs available, any IO to the pool will be blocked until there are enough OSDs available again.

{% hint style="info" %}
When planning an erasure coded pool, keep an eye on the `min_size` as it defines how many OSDs need to be available. Otherwise, IO will be blocked.
{% endhint %}

For example, an EC pool with `k = 2` and `m = 1` will have `size = 3`, `min_size = 2` and will stay operational if one OSD fails. If the pool is configured with `k = 2`, `m = 2`, it will have a `size = 4` and `min_size = 3` and stay operational if one OSD is lost.

To create a new EC pool, run the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool create <pool-name> --erasure-coding k=2,m=1
```

Optional parameters are `failure-domain` and `device-class`. If you need to change any EC profile settings used by the pool, you will have to create a new pool with a new profile.

This will create a new EC pool plus the needed replicated pool to store the RBD omap and other metadata. In the end, there will be a `<pool name>-data` and `<pool name>-metadata` pool. The default behavior is to create a matching storage configuration as well. If that behavior is not wanted, you can disable it by providing the `--add_storages 0` parameter. When configuring the storage configuration manually, keep in mind that the `data-pool` parameter needs to be set. Only then will the EC pool be used to store the data objects. For example:

{% hint style="info" %}
The optional parameters `--size`, `--min_size` and `--crush_rule` will be used for the replicated metadata pool, but not for the erasure coded data pool. If you need to change the `min_size` on the data pool, you can do it later. The `size` and `crush_rule` parameters cannot be changed on erasure coded pools.
{% endhint %}

If there is a need to further customize the EC profile, you can do so by creating it with the Ceph tools directly   
[Ceph Erasure Code Profile [https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-code-profiles](https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/#erasure-code-profiles)]  
, and specify the profile to use with the `profile` parameter.

For example:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool create <pool-name> --erasure-coding profile=<profile-name>
```

### FastEC (`allow_ec_optimizations`) <a href="#_fastec_span_class_monospaced_allow_ec_optimizations_span" id="_fastec_span_class_monospaced_allow_ec_optimizations_span"></a>

Ceph Tentacle introduces a new erasure coding I/O path called FastEC, enabled per pool via the `allow_ec_optimizations` flag. FastEC adds partial reads and partial writes on EC pools, substantially improving small random I/O performance — the dominant access pattern of virtual machine disk I/O. Upstream recommends it for RBD and CephFS backed storage   
[Ceph Erasure Code [https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/](https://docs.ceph.com/en/tentacle/rados/operations/erasure-code/)]  
.

FastEC has four requirements that the Ceph monitor enforces:

- the pool must be erasure coded;
- the cluster must be at `require_osd_release` tentacle or later;
- the erasure code profile must use a plugin and technique combination that supports the optimized EC path:

  <table>



  <thead>
  <tr>
  <th>Plugin</th>
  <th>Technique</th>
  <th>FastEC</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><p><code>isa</code></p></td>
  <td><p><code>reed_sol_van</code></p></td>
  <td><p>yes</p></td>
  </tr>
  <tr>
  <td><p><code>isa</code></p></td>
  <td><p><code>cauchy</code></p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>jerasure</code></p></td>
  <td><p><code>reed_sol_van</code></p></td>
  <td><p>yes</p></td>
  </tr>
  <tr>
  <td><p><code>jerasure</code></p></td>
  <td><p>all others</p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>lrc</code></p></td>
  <td><p>(any)</p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>shec</code></p></td>
  <td><p>(any)</p></td>
  <td><p>no</p></td>
  </tr>
  <tr>
  <td><p><code>clay</code></p></td>
  <td><p>(any)</p></td>
  <td><p>no</p></td>
  </tr>
  </tbody>
  </table>
- the pool’s stripe unit must be a multiple of 4096 bytes. The default stripe unit satisfies this, so this is only relevant for pools created with a custom `stripe_unit` in their erasure code profile.

If any precondition is not met, `ceph osd pool set <pool>-data allow_ec_optimizations 1` fails with a descriptive error — no silent degradation.

`pveceph` does not set the plugin or technique explicitly when creating an EC profile — both are seeded from the monitor’s `osd_pool_default_erasure_code_profile` option (`reed_sol_van` by default on both Squid and Tentacle). The technique requirement is therefore satisfied out of the box unless the operator has overridden this setting. Verify with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph config get mon osd_pool_default_erasure_code_profile
```

If the output shows a technique other than `reed_sol_van`, either update the cluster-wide default or create a compatible profile explicitly and pass it via the `profile` property when creating the pool (see above).

Check the cluster release with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd dump | grep require_osd_release
```

If this reports a release older than `tentacle`, run `ceph osd require-osd-release tentacle` after all OSDs have been upgraded.

{% hint style="warning" %}
`allow_ec_optimizations` is a one-way switch. Once enabled on a pool, the Ceph monitor refuses to clear the flag again, so rolling back requires draining and recreating the pool. Enable it only after validating that FastEC works for your workload on a test pool.
{% endhint %}

#### Enabling FastEC on a pool <a href="#_enabling_fastec_on_a_pool" id="_enabling_fastec_on_a_pool"></a>

FastEC is enabled per pool via the `ceph` CLI. It can be set on both new and existing (populated) pools. No data migration or re-encoding takes place; only pool metadata changes.

To enable FastEC on a pool, run the following command against the data pool (typically named `<pool-name>-data`):

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd pool set <pool-name>-data allow_ec_optimizations 1
```

Verify the result with:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd pool get <pool-name>-data allow_ec_optimizations
```

The same command reports the current state for any EC pool, which is useful when auditing a cluster.

When the flag is set on a populated pool, be aware of the following:

- **Primary re-election.** FastEC marks data shards 1 through k-1 as non-primary, so PGs whose primary was on one of those shards will re-peer. This is a normal peering event and causes a brief I/O pause per affected PG.
- **Scrub interaction.** Re-peering cancels any in-flight scrub on affected PGs. Those PGs will need to be re-scrubbed after peering completes.

### Adding EC Pools as Storage <a href="#_adding_ec_pools_as_storage" id="_adding_ec_pools_as_storage"></a>

You can add an already existing EC pool as storage to Proxmox VE. It works the same way as adding an `RBD` pool but requires the extra `data-pool` option.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pvesm add rbd <storage-name> --pool <replicated-pool> --data-pool <ec-pool>
```

{% hint style="success" %}
Do not forget to add the `keyring` and `monhost` option for any external Ceph clusters, not managed by the local Proxmox VE cluster.
{% endhint %}

## 8.9.3. Destroy Pools <a href="#_destroy_pools" id="_destroy_pools"></a>

To destroy a pool via the GUI, select a node in the tree view and go to the **Ceph → Pools** panel. Select the pool to destroy and click the **Destroy** button. To confirm the destruction of the pool, you need to enter the pool name.

Run the following command to destroy a pool. Specify the *-remove_storages* to also remove the associated storage.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph pool destroy <name>
```

{% hint style="info" %}
Pool deletion runs in the background and can take some time. You will notice the data usage in the cluster decreasing throughout this process.
{% endhint %}

## 8.9.4. PG Autoscaler <a href="#_pg_autoscaler" id="_pg_autoscaler"></a>

The PG autoscaler allows the cluster to consider the amount of (expected) data stored in each pool and to choose the appropriate pg_num values automatically. It is available since Ceph Nautilus.

You may need to activate the PG autoscaler module before adjustments can take effect.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph mgr module enable pg_autoscaler
```

The autoscaler is configured on a per pool basis and has the following modes:

<table>
<tr>
<td>warn <br/></td>
<td>
<p>A health warning is issued if the suggested <code>pg_num</code> value differs too much from the current value.</p>
</td>
</tr>
<tr>
<td>on <br/></td>
<td>
<p>The <code>pg_num</code> is adjusted automatically with no need for any manual interaction.</p>
</td>
</tr>
<tr>
<td>off <br/></td>
<td>
<p>No automatic <code>pg_num</code> adjustments are made, and no warning will be issued if the PG count is not optimal.</p>
</td>
</tr>
</table>

The scaling factor can be adjusted to facilitate future data storage with the `target_size`, `target_size_ratio` and the `pg_num_min` options.

{% hint style="warning" %}
By default, the autoscaler considers tuning the PG count of a pool if it is off by a factor of 3. This will lead to a considerable shift in data placement and might introduce a high load on the cluster.
{% endhint %}

You can find a more in-depth introduction to the PG autoscaler on Ceph’s Blog - [New in Nautilus: PG merging and autotuning](https://ceph.io/rados/new-in-nautilus-pg-merging-and-autotuning/).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
