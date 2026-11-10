# 3. Host System Administration <a href="#chapter_system_administration" id="chapter_system_administration"></a>

The following sections will focus on common virtualization tasks and explain the Proxmox VE specifics regarding the administration and management of the host machine.

Proxmox VE is based on [Debian GNU/Linux](https://www.debian.org/) with additional repositories to provide the Proxmox VE related packages. This means that the full range of Debian packages is available including security updates and bug fixes. Proxmox VE provides its own Linux kernel based on the Ubuntu kernel. It has all the necessary virtualization and container features enabled and includes [ZFS](https://zfsonlinux.org) and several extra hardware drivers.

For other topics not included in the following sections, please refer to the Debian documentation. The [Debian Administrator's Handbook](https://debian-handbook.info/get) is available online, and provides a comprehensive introduction to the Debian operating system (see [[Hertzog13]](../21-bibliography/README.md#Hertzog13)).

## 本章内容

- [3.1. Package Repositories](01-sysadmin-package-repositories.md)
- [3.2. System Software Updates](02-system-software-updates.md)
- [3.3. Firmware Updates](03-chapter-firmware-updates.md)
- [3.4. Network Configuration](04-sysadmin-network-configuration.md)
- [3.5. Time Synchronization](05-time-synchronization.md)
- [3.6. External Metric Server](06-external-metric-server.md)
- [3.7. Disk Health Monitoring](07-disk-health-monitoring.md)
- [3.8. Logical Volume Manager (LVM)](08-chapter-lvm.md)
- [3.9. ZFS on Linux](09-chapter-zfs.md)
- [3.10. BTRFS](10-chapter-btrfs.md)
- [3.11. Proxmox Node Management](11-proxmox-node-management.md)
- [3.12. Certificate Management](12-sysadmin-certificate-management.md)
- [3.13. Host Bootloader](13-sysboot.md)
- [3.14. Kernel Samepage Merging (KSM)](14-kernel-samepage-merging.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
