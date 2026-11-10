# 8.10. Ceph CRUSH & Device Classes <a href="#pve_ceph_device_classes" id="pve_ceph_device_classes"></a>

[![screenshot/gui-ceph-config.png](../../assets/screenshot-gui-ceph-config-png-b4544eca3b00.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-config.png)

The   
[[https://ceph.com/assets/pdfs/weil-crush-sc06.pdf](https://ceph.com/assets/pdfs/weil-crush-sc06.pdf)]  
 (**C**ontrolled **R**eplication **U**nder **S**calable **H**ashing) algorithm is at the foundation of Ceph.

CRUSH calculates where to store and retrieve data from. This has the advantage that no central indexing service is needed. CRUSH works using a map of OSDs, buckets (device locations) and rulesets (data replication) for pools.

{% hint style="info" %}
Further information can be found in the Ceph documentation, under the section CRUSH map   
[CRUSH map [https://docs.ceph.com/en/tentacle/rados/operations/crush-map/](https://docs.ceph.com/en/tentacle/rados/operations/crush-map/)]  
.
{% endhint %}

This map can be altered to reflect different replication hierarchies. The object replicas can be separated (e.g., failure domains), while maintaining the desired distribution.

A common configuration is to use different classes of disks for different Ceph pools. For this reason, Ceph introduced device classes with luminous, to accommodate the need for easy ruleset generation.

The device classes can be seen in the *ceph osd tree* output. These classes represent their own root bucket, which can be seen with the below command.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd crush tree --show-shadow
```

Example output form the above command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ID  CLASS WEIGHT  TYPE NAME
-16  nvme 2.18307 root default~nvme
-13  nvme 0.72769     host sumi1~nvme
 12  nvme 0.72769         osd.12
-14  nvme 0.72769     host sumi2~nvme
 13  nvme 0.72769         osd.13
-15  nvme 0.72769     host sumi3~nvme
 14  nvme 0.72769         osd.14
 -1       7.70544 root default
 -3       2.56848     host sumi1
 12  nvme 0.72769         osd.12
 -5       2.56848     host sumi2
 13  nvme 0.72769         osd.13
 -7       2.56848     host sumi3
 14  nvme 0.72769         osd.14
```

To instruct a pool to only distribute objects on a specific device class, you first need to create a ruleset for the device class:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd crush rule create-replicated <rule-name> <root> <failure-domain> <class>
```

<table>


<tbody>
<tr>
<td><p>&lt;rule-name&gt;</p></td>
<td><p>name of the rule, to connect with a pool (seen in GUI &amp; CLI)</p></td>
</tr>
<tr>
<td><p>&lt;root&gt;</p></td>
<td><p>which crush root it should belong to (default Ceph root "default")</p></td>
</tr>
<tr>
<td><p>&lt;failure-domain&gt;</p></td>
<td><p>at which failure-domain the objects should be distributed (usually host)</p></td>
</tr>
<tr>
<td><p>&lt;class&gt;</p></td>
<td><p>what type of OSD backing store to use (e.g., nvme, ssd, hdd)</p></td>
</tr>
</tbody>
</table>

Once the rule is in the CRUSH map, you can tell a pool to use the ruleset.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph osd pool set <pool-name> crush_rule <rule-name>
```

{% hint style="success" %}
If the pool already contains objects, these must be moved accordingly. Depending on your setup, this may introduce a big performance impact on your cluster. As an alternative, you can create a new pool and move disks separately.
{% endhint %}

{% hint style="warning" %}
When using the PG autoscaler, all pools in the cluster are required to use CRUSH rules of the same kind, either all specifying a device class, or none. Otherwise the autoscaler will skip the affected pools and their `pg_num` will not be adjusted.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
