# 8.6. Ceph Manager <a href="#pve_ceph_manager" id="pve_ceph_manager"></a>

The Manager daemon runs alongside the monitors. It provides an interface to monitor the cluster. Since the release of Ceph luminous, at least one ceph-mgr   
\[Ceph Manager [https://docs.ceph.com/en/tentacle/mgr/](https://docs.ceph.com/en/tentacle/mgr/)\]  
 daemon is required.

## 8.6.1. Create Manager <a href="#pveceph_create_mgr" id="pveceph_create_mgr"></a>

Multiple Managers can be installed, but only one Manager is active at any given time.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mgr create
```

{% hint style="info" %}
It is recommended to install the Ceph Manager on the monitor nodes. For high availability install more then one manager.
{% endhint %}

## 8.6.2. Destroy Manager <a href="#pveceph_destroy_mgr" id="pveceph_destroy_mgr"></a>

To remove a Ceph Manager via the GUI, first select a node in the tree view and go to the **Ceph → Monitor** panel. Select the Manager and click the **Destroy** button.

To remove a Ceph Monitor via the CLI, first connect to the node on which the Manager is running. Then execute the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pveceph mgr destroy
```

{% hint style="info" %}
While a manager is not a hard-dependency, it is crucial for a Ceph cluster, as it handles important features like PG-autoscaling, device health monitoring, telemetry and more.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
