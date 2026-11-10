# 2.5. Install Proxmox VE on Debian <a href="#_install_proxmox_ve_on_debian" id="_install_proxmox_ve_on_debian"></a>

Proxmox VE ships as a set of Debian packages and can be installed on top of a standard Debian installation. [After configuring the repositories](../03-system-administration/01-sysadmin-package-repositories.md#sysadmin_package_repositories) you need to run the following commands:

```text
# apt-get update
# apt-get install proxmox-ve
```

Installing on top of an existing Debian installation looks easy, but it presumes that the base system has been installed correctly and that you know how you want to configure and use the local storage. You also need to configure the network manually.

In general, this is not trivial, especially when LVM or ZFS is used.

A detailed step-by-step how-to can be found on the [wiki](https://pve.proxmox.com/wiki/Install_Proxmox_VE_on_Debian_13_Trixie).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
