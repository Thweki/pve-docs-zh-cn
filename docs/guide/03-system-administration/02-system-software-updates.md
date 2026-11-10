# 3.2. System Software Updates <a href="#system_software_updates" id="system_software_updates"></a>

Proxmox provides updates on a regular basis for all repositories. To install updates use the web-based GUI or the following CLI commands:

```text
# apt update
# apt full-upgrade
```

{% hint style="warning" %}
As Proxmox VE uses a rolling release model on top of Debian, performing an `apt upgrade` may result in a partially upgraded or broken package state. This is because `apt full-upgrade` can also remove existing packages to satisfy dependencies if needed, while `apt upgrade` cannot.
{% endhint %}

For occasionally upgrading Ceph to its succeeding major release, see [Ceph Repositories](01-sysadmin-package-repositories.md#sysadmin_package_repositories_ceph).

{% hint style="info" %}
The APT package management system is very flexible and provides many features, see `man apt`, or [[Hertzog13]](../21-bibliography/README.md#Hertzog13) for additional information.
{% endhint %}

{% hint style="success" %}
Regular updates are essential to get the latest patches and security related fixes. Major system upgrades are announced in the [Proxmox VE Community Forum](https://forum.proxmox.com/).
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
