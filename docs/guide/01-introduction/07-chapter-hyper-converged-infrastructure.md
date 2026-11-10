# 1.7. Hyper-converged Infrastructure <a href="#chapter_hyper_converged_infrastructure" id="chapter_hyper_converged_infrastructure"></a>

Proxmox VE is a virtualization platform that tightly integrates compute, storage and networking resources, manages highly available clusters, backup/restore as well as disaster recovery. All components are software-defined and compatible with one another.

Therefore it is possible to administrate them like a single system via the centralized web management interface. These capabilities make Proxmox VE an ideal choice to deploy and manage an open source [hyper-converged infrastructure](https://en.wikipedia.org/wiki/Hyper-converged_infrastructure).

## 1.7.1. Benefits of a Hyper-Converged Infrastructure (HCI) with Proxmox VE <a href="#_benefits_of_a_hyper_converged_infrastructure_hci_with_proxmox_ve" id="_benefits_of_a_hyper_converged_infrastructure_hci_with_proxmox_ve"></a>

A hyper-converged infrastructure (HCI) is especially useful for deployments in which a high infrastructure demand meets a low administration budget, for distributed setups such as remote and branch office environments or for virtual private and public clouds.

HCI provides the following advantages:

- Scalability: seamless expansion of compute, network and storage devices (i.e. scale up servers and storage quickly and independently from each other).
- Low cost: Proxmox VE is open source and integrates all components you need such as compute, storage, networking, backup, and management center. It can replace an expensive compute/storage infrastructure.
- Data protection and efficiency: services such as backup and disaster recovery are integrated.
- Simplicity: easy configuration and centralized administration.
- Open Source: No vendor lock-in.

## 1.7.2. Hyper-Converged Infrastructure: Storage <a href="#_hyper_converged_infrastructure_storage" id="_hyper_converged_infrastructure_storage"></a>

Proxmox VE has tightly integrated support for deploying a hyper-converged storage infrastructure. You can, for example, deploy and manage the following two storage technologies by using the web interface only:

- **Ceph**: a self-healing and self-managing shared, reliable and highly scalable storage system. Check out [how to manage Ceph services on Proxmox VE nodes](../08-pveceph/README.md#chapter_pveceph)
- **ZFS**: a combined file system and logical volume manager with extensive protection against data corruption, various RAID modes, fast and cheap snapshots - among other features. Find out [how to leverage the power of ZFS on Proxmox VE nodes](../03-system-administration/09-chapter-zfs.md#chapter_zfs).

Besides above, Proxmox VE has support to integrate a wide range of additional storage technologies. You can find out about them in the [Storage Manager chapter](../07-storage/README.md#chapter_storage).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
