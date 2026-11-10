# 3.2. System Software Updates <a href="#system_software_updates" id="system_software_updates"></a>

Proxmox 定期为所有存储库提供更新。要安装更新，请使用基于 Web 的图形用户界面或以下命令行命令：

```text
# apt update
# apt full-upgrade
```

{% hint style="warning" %}
由于 Proxmox VE 在 Debian 之上采用滚动发布模式，执行 `apt upgrade` 可能会导致软件包仅部分升级或处于损坏状态。这是因为 `apt full-upgrade` 在需要时也可以移除现有软件包以满足依赖关系，而 `apt upgrade` 则不能。
{% endhint %}

有关偶尔将 Ceph 升级到下一个主要版本的信息，请参阅 [Ceph 存储库](01-sysadmin-package-repositories.md#sysadmin_package_repositories_ceph)。

{% hint style="info" %}
APT 软件包管理系统非常灵活，并提供了许多功能，有关更多信息，请参阅 `man apt` 或 [\[Hertzog13\]](../21-bibliography/README.md#Hertzog13)。
{% endhint %}

{% hint style="success" %}
定期更新对于获取最新补丁和安全相关修复至关重要。主要系统升级会在 [Proxmox VE 社区论坛](https://forum.proxmox.com/) 中发布。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
