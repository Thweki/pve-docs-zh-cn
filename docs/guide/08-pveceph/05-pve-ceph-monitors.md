# 8.5. Ceph Monitor <a href="#pve_ceph_monitors" id="pve_ceph_monitors"></a>

[![screenshot/gui-ceph-monitor.png](../../assets/screenshot-gui-ceph-monitor-png-5183f95d9815.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-monitor.png)

The Ceph Monitor (MON)   
\[Ceph Monitor [https://docs.ceph.com/en/tentacle/rados/configuration/mon-config-ref/](https://docs.ceph.com/en/tentacle/rados/configuration/mon-config-ref/)\]  
 maintains a master copy of the cluster map. For high availability, you need at least 3 monitors. One monitor will already be installed if you used the installation wizard. You won’t need more than 3 monitors, as long as your cluster is small to medium-sized. Only really large clusters will require more than this.

## 8.5.1. Create Monitors <a href="#pveceph_create_mon" id="pveceph_create_mon"></a>

On each node where you want to place a monitor (three monitors are recommended), create one by using the *Ceph → Monitor* tab in the GUI or run:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mon create
```

## 8.5.2. Destroy Monitors <a href="#pveceph_destroy_mon" id="pveceph_destroy_mon"></a>

To remove a Ceph Monitor via the GUI, first select a node in the tree view and go to the **Ceph → Monitor** panel. Select the MON and click the **Destroy** button.

To remove a Ceph Monitor via the CLI, first connect to the node on which the MON is running. Then execute the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mon destroy
```

{% hint style="info" %}
At least three Monitors are needed for quorum.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
