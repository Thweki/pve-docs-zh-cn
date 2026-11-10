# 8.1. Introduction <a href="#_introduction" id="_introduction"></a>

[![screenshot/gui-ceph-status-dashboard.png](../../assets/screenshot-gui-ceph-status-dashboard-png-35c265732db2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-ceph-status-dashboard.png)

Proxmox VE unifies your compute and storage systems, that is, you can use the same physical nodes within a cluster for both computing (processing VMs and containers) and replicated storage. The traditional silos of compute and storage resources can be wrapped up into a single hyper-converged appliance. Separate storage networks (SANs) and connections via network attached storage (NAS) disappear. With the integration of Ceph, an open source software-defined storage platform, Proxmox VE has the ability to run and manage Ceph storage directly on the hypervisor nodes.

Ceph is a distributed object store and file system designed to provide excellent performance, reliability and scalability.

**Some advantages of Ceph on Proxmox VE are:**

- Easy setup and management via CLI and GUI
- Thin provisioning
- Snapshot support
- 自我修复
- Scalable to the exabyte level
- Provides block, file system, and object storage
- Setup pools with different performance and redundancy characteristics
- Data is replicated, making it fault tolerant
- Runs on commodity hardware
- No need for hardware RAID controllers
- Open source

For small to medium-sized deployments, it is possible to install a Ceph server for using RADOS Block Devices (RBD) or CephFS directly on your Proxmox VE cluster nodes (see [Ceph RADOS Block Devices (RBD)](../07-storage/14-ceph-rados-block-devices.md#ceph_rados_block_devices)). Recent hardware has a lot of CPU power and RAM, so running storage services and virtual guests on the same node is possible.

To simplify management, Proxmox VE provides you native integration to install and manage [Ceph](http://ceph.com) services on Proxmox VE nodes either via the built-in web interface, or using the *pveceph* command line tool.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
