# 1.11. Project History <a href="#intro_project_history" id="intro_project_history"></a>

The project started in 2007, followed by a first stable version in 2008. At the time, it used OpenVZ for containers and KVM for virtual machines. The clustering features were limited, and the user interface was simple (a server-generated web page).

The project quickly developed new features using the [Corosync](https://corosync.github.io/corosync/) cluster stack, and the introduction of the Proxmox Cluster File System (pmxcfs) was a big step forward, because it completely hides the cluster complexity from the user. Managing a cluster of 16 nodes is as simple as managing a single node.

The introduction of the REST API, with a complete declarative specification written in JSON Schema, enabled other people to integrate Proxmox VE into their infrastructure and made it easy to provide additional services.

The REST API also made it possible to replace the original user interface with a modern client-side single-page application using JavaScript. The old Java-based VNC console code was replaced with [noVNC](https://novnc.com/info.html), so only a web browser is needed to manage VMs.

The support for various storage types is another big achievement. Notably, Proxmox VE was the first distribution to ship [ZFS on Linux](https://zfsonlinux.org/) by default in 2014. Another milestone was the ability to run and manage [Ceph](https://ceph.com/) storage on the hypervisor nodes. Such setups are extremely cost effective.

When the project started, Proxmox was among the first companies providing commercial support for KVM. The KVM project itself continuously evolved and is now a widely used hypervisor. New features arrive with each release. The KVM live backup feature, developed by Proxmox, makes it possible to create snapshot backups on any storage type.

The most notable change with version 4.0 was the move from OpenVZ to [LXC](https://linuxcontainers.org/). Containers are now deeply integrated, and they can use the same storage and network features as virtual machines. At the same time, the easy-to-use [High Availability (HA) manager](../15-ha-manager/README.md#chapter_ha_manager) was introduced, simplifying the configuration and management of highly available setups.

During the development of Proxmox VE 5, asynchronous [storage replication](../09-pvesr/README.md#chapter_pvesr) as well as automated [certificate management](../03-system-administration/12-sysadmin-certificate-management.md#sysadmin_certificate_management) using ACME/Let’s Encrypt were introduced, among many other features.

The [Software Defined Network (SDN)](../12-pvesdn/README.md#chapter_pvesdn) stack was developed in cooperation with the community. It was integrated into the web interface as an experimental feature in version 6.2, simplifying the management of sophisticated network configurations. Since version 8.1, the SDN integration is fully supported and installed by default.

2020 marked the release of a new project, the [Proxmox Backup Server](https://www.proxmox.com/en/products/proxmox-backup-server/overview), written in the Rust programming language. Proxmox Backup Server is deeply integrated with Proxmox VE and significantly improves backup capabilities by implementing incremental backups, deduplication, and much more.

Another new tool, the [Proxmox Offline Mirror](https://pom.proxmox.com), was released in 2022, enabling subscriptions for systems which have no connection to the public internet.

The highly requested dark theme for the web interface was introduced in 2023. Later that year, version 8.0 integrated access to the Ceph enterprise repository. Access to the most stable Ceph repository is included with any Proxmox VE subscription.

Automated and unattended installation for the official [ISO installer](../02-installation/03-installation-installer.md#installation_installer) was introduced in version 8.2, significantly simplifying large deployments of Proxmox VE.

With the [import wizard](../10-virtual-machines/07-qm-import-virtual-machines.md#qm_import_virtual_machines), equally introduced in version 8.2, users can easily and efficiently migrate guests directly from other hypervisors like VMware ESXi   
[Migrate to Proxmox VE [https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE](https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE)]  
. Additionally, archives in Open Virtualization Format (OVF/OVA) can now be directly imported from file-based storages in the web interface.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
