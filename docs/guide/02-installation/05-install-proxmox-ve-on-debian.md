# 2.5. Install Proxmox VE on Debian <a href="#_install_proxmox_ve_on_debian" id="_install_proxmox_ve_on_debian"></a>

Proxmox VE 以一组 Debian 软件包的形式提供，可以安装在标准 Debian 安装之上。[配置软件仓库后](../03-system-administration/01-sysadmin-package-repositories.md)，您需要运行以下命令：

```text
# apt-get update
# apt-get install proxmox-ve
```

在现有 Debian 安装之上进行安装看起来很简单，但它假定基础系统已正确安装，并且您知道要如何配置和使用本地存储。您还需要手动配置网络。

通常，这并不简单，尤其是在使用 LVM 或 ZFS 时。

可以在 [wiki](https://pve.proxmox.com/wiki/Install_Proxmox_VE_on_Debian_13_Trixie) 上找到详细的分步操作指南。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
