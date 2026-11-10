# 8.15. Ceph Monitoring and Troubleshooting <a href="#pve_ceph_mon_and_ts" id="pve_ceph_mon_and_ts"></a>

It is important to continuously monitor the health of a Ceph deployment from the beginning, either by using the Ceph tools or by accessing the status through the Proxmox VE [API](https://pve.proxmox.com/pve-docs/api-viewer/index.html).

The following Ceph commands can be used to see if the cluster is healthy (*HEALTH_OK*), if there are warnings (*HEALTH_WARN*), or even errors (*HEALTH_ERR*). If the cluster is in an unhealthy state, the status commands below will also give you an overview of the current events and actions to take. To stop their execution, press CTRL-C.

Continuously watch the cluster status:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
watch ceph --status
```

Print the cluster status once (not being updated) and continuously append lines of status events:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph --watch
```

## 8.15.1. Troubleshooting <a href="#pve_ceph_ts" id="pve_ceph_ts"></a>

This section includes frequently used troubleshooting information. More information can be found on the official Ceph website under Troubleshooting   
[Ceph troubleshooting [https://docs.ceph.com/en/tentacle/rados/troubleshooting/](https://docs.ceph.com/en/tentacle/rados/troubleshooting/)]  
.

<a id="pve_ceph_ts_logs"></a>



**Relevant Logs on Affected Node**

- [Disk Health Monitoring](../03-system-administration/07-disk-health-monitoring.md#disk_health_monitoring)
- *System → System Log* or via the CLI, for example of the last 2 days:

  Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

  ```text
  journalctl --since "2 days ago"
  ```
- IPMI and RAID controller logs

Ceph service crashes can be listed and viewed in detail by running the following commands:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph crash ls
ceph crash info <crash_id>
```

Crashes marked as new can be acknowledged by running:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph crash archive-all
```

To get a more detailed view, every Ceph service has a log file under `/var/log/ceph/`. If more detail is required, the log level can be adjusted   
[Ceph log and debugging [https://docs.ceph.com/en/tentacle/rados/troubleshooting/log-and-debug/](https://docs.ceph.com/en/tentacle/rados/troubleshooting/log-and-debug/)]  
.

<a id="pve_ceph_ts_causes"></a>



**Common Causes of Ceph Problems**

- Network problems like congestion, a faulty switch, a shut down interface or a blocking firewall. Check whether all Proxmox VE nodes are reliably reachable on the [corosync cluster network](../05-pvecm/08-pvecm-cluster-network.md#pvecm_cluster_network) and on the [Ceph public and cluster network](04-pve-ceph-install-wizard.md#pve_ceph_install_wizard).
- Disk or connection parts which are:

  - defective
  - not firmly mounted
  - lacking I/O performance under higher load (e.g. when using HDDs, consumer hardware or [inadvisable RAID controllers](03-recommendations-for-a-healthy-ceph-cluster.md#pve_ceph_recommendation_raid))
- Not fulfilling the [recommendations](03-recommendations-for-a-healthy-ceph-cluster.md#_recommendations_for_a_healthy_ceph_cluster) for a healthy Ceph cluster.

<a id="pve_ceph_ts_problems"></a>



**Common Ceph Problems**

****

**OSDs `down`/crashed**

A faulty OSD will be reported as `down` and mostly (auto) `out` 10 minutes later. Depending on the cause, it can also automatically become `up` and `in` again. To try a manual activation via web interface, go to *Any node → Ceph → OSD*, select the OSD and click on **Start**, **In** and **Reload**. When using the shell, run following command on the affected node:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
ceph-volume lvm activate --all
```

To activate a failed OSD, it may be necessary to [safely reboot](../15-ha-manager/11-ha-manager-node-maintenance.md#ha_manager_node_maintenance) the respective node or, as a last resort, to [recreate or replace](14-ceph-maintenance.md#pve_ceph_osd_replace) the OSD.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
