# 11.5. 安全注意事项 <a href="#security_considerations" id="security_considerations"></a>

容器使用宿主机系统的内核。这会为恶意用户暴露攻击面。一般来说，完整的虚拟机可以提供更好的隔离性。如果向未知或不受信任的人员提供容器，应考虑这一点。

为了减少攻击面，LXC 使用了 AppArmor、CGroups 和内核命名空间等许多安全功能。

## 11.5.1. AppArmor <a href="#apparmor" id="apparmor"></a>

AppArmor 配置文件用于限制对可能危险的操作的访问。某些系统调用（即 `mount`）会被禁止执行。

要跟踪 AppArmor 活动，请使用：

```text
# dmesg | grep apparmor
```

尽管不建议这样做，但可以为容器禁用 AppArmor。这会带来安全风险。如果系统配置不当，或者 LXC 或 Linux Kernel 存在漏洞，在容器内执行的某些系统调用可能会导致权限提升。

要为容器禁用 AppArmor，请将以下行添加到位于 `/etc/pve/lxc/CTID.conf` 的容器配置文件中：

```text
lxc.apparmor.profile = unconfined
```

{% hint style="warning" %}
请注意，不建议在生产环境中这样做。
{% endhint %}

## 11.5.2. 控制组（*cgroup*） <a href="#pct_cgroup" id="pct_cgroup"></a>

*cgroup* 是一种内核机制，用于按层次组织进程并分配系统资源。

通过 *cgroups* 控制的主要资源包括 CPU 时间、内存和交换空间限制，以及对设备节点的访问。*cgroups* 还用于在创建快照之前“冻结”容器。

*cgroups* 的当前版本是 [*cgroupv2*](https://www.kernel.org/doc/html/v6.14/admin-guide/cgroup-v2.html)。随着 Proxmox VE 7.0 的发布，cgroup 子系统的 [v1 版本](https://www.kernel.org/doc/html/v6.14/admin-guide/cgroup-v1/index.html)已被弃用，并在 Proxmox VE 9.0 中被完全移除。在 Proxmox VE 7.0 之前，默认使用“混合”模式。

### CGroup 版本兼容性 <a href="#pct_cgroup_compat" id="pct_cgroup_compat"></a>

就 Proxmox VE 而言，纯 *cgroupv2* 与旧混合环境的主要区别在于，使用 *cgroupv2* 时，内存和交换空间现在可以独立控制。容器的内存和交换空间设置可以直接映射到这些值，而以前只能限制内存上限以及内存与交换空间**总和**的上限。

另一个重要区别是 *devices* 控制器的配置方式完全不同。因此，纯 *cgroupv2* 环境目前不支持文件系统配额。

容器操作系统需要支持 *cgroupv2*，才能在纯 *cgroupv2* 环境中运行。运行 *systemd* 231 或更新版本的容器支持 *cgroupv2* [\[1\]](#note-d942b21b-1)，不使用 *systemd* 作为 init 系统的容器也支持 [\[2\]](#note-d942b21b-2)。

{% hint style="info" %}
CentOS 7 和 Ubuntu 16.10 是两个知名的 Linux 发行版版本，其 *systemd* 版本太旧，无法在 *cgroupv2* 环境中运行。您可以：

- 将整个发行版升级到较新的版本。对于上述示例，可以升级到 Ubuntu 18.04 或 20.04，以及 CentOS 8（或 AlmaLinux、Rocky Linux 等 RHEL/CentOS 衍生版本）。这样做的好处是可以获得最新的缺陷修复和安全修复，通常还能获得新功能，并将 EOL 日期延后。
- 升级容器中的 systemd 版本。如果发行版提供 backports 软件仓库，这可以是一种简单快捷的临时措施。
- 将容器或其服务迁移到虚拟机。虚拟机与宿主机的交互要少得多，因此可以在其中顺利安装几十年前的操作系统版本。
{% endhint %}

### 更改 CGroup 版本 <a href="#pct_cgroup_change_version" id="pct_cgroup_change_version"></a>

在 Proxmox VE 9.0 之前，您可以使用以下内核命令行参数切换回以前的版本：

```text
systemd.unified_cgroup_hierarchy=0
```

有关应在何处添加该参数，请参阅介绍如何编辑内核启动命令行的 [本节](../03-system-administration/13-sysboot.md#sysboot_edit_kernel_cmdline)。

## 注释

### 注释 1 <a href="#note-d942b21b-1" id="note-d942b21b-1"></a>

这包括 Proxmox VE 提供的所有容器模板的最新主要版本

### 注释 2 <a href="#note-d942b21b-2" id="note-d942b21b-2"></a>

例如 Alpine Linux

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
