# 11.5. Security Considerations <a href="#_security_considerations" id="_security_considerations"></a>

Containers use the kernel of the host system. This exposes an attack surface for malicious users. In general, full virtual machines provide better isolation. This should be considered if containers are provided to unknown or untrusted people.

To reduce the attack surface, LXC uses many security features like AppArmor, CGroups and kernel namespaces.

## 11.5.1. AppArmor <a href="#_apparmor" id="_apparmor"></a>

AppArmor profiles are used to restrict access to possibly dangerous actions. Some system calls, i.e. `mount`, are prohibited from execution.

To trace AppArmor activity, use:

```text
# dmesg | grep apparmor
```

Although it is not recommended, AppArmor can be disabled for a container. This brings security risks with it. Some syscalls can lead to privilege escalation when executed within a container if the system is misconfigured or if a LXC or Linux Kernel vulnerability exists.

To disable AppArmor for a container, add the following line to the container configuration file located at `/etc/pve/lxc/CTID.conf`:

```text
lxc.apparmor.profile = unconfined
```

{% hint style="warning" %}
Please note that this is not recommended for production use.
{% endhint %}

## 11.5.2. Control Groups (*cgroup*) <a href="#pct_cgroup" id="pct_cgroup"></a>

*cgroup* is a kernel mechanism used to hierarchically organize processes and distribute system resources.

The main resources controlled via *cgroups* are CPU time, memory and swap limits, and access to device nodes. *cgroups* are also used to "freeze" a container before taking snapshots.

The current version of *cgroups* is [*cgroupv2*](https://www.kernel.org/doc/html/v6.14/admin-guide/cgroup-v2.html). The [v1 version](https://www.kernel.org/doc/html/v6.14/admin-guide/cgroup-v1/index.html) of the cgroup subsystem was deprecated with the release of Proxmox VE 7.0 and removed entirely with Proxmox VE 9.0. Before Proxmox VE 7.0, a "hybrid" mode was the default.

### CGroup Version Compatibility <a href="#pct_cgroup_compat" id="pct_cgroup_compat"></a>

The main difference between pure *cgroupv2* and the old hybrid environments regarding Proxmox VE is that with *cgroupv2* memory and swap are now controlled independently. The memory and swap settings for containers can map directly to these values, whereas previously only the memory limit and the limit of the **sum** of memory and swap could be limited.

Another important difference is that the *devices* controller is configured in a completely different way. Because of this, file system quotas are currently not supported in a pure *cgroupv2* environment.

*cgroupv2* support by the container’s OS is needed to run in a pure *cgroupv2* environment. Containers running *systemd* version 231 or newer support *cgroupv2*   
[this includes all newest major versions of container templates shipped by Proxmox VE]  
, as do containers not using *systemd* as init system   
[for example Alpine Linux]  
.

{% hint style="info" %}
CentOS 7 and Ubuntu 16.10 are two prominent Linux distributions releases, which have a *systemd* version that is too old to run in a *cgroupv2* environment, you can either

- Upgrade the whole distribution to a newer release. For the examples above, that could be Ubuntu 18.04 or 20.04, and CentOS 8 (or RHEL/CentOS derivatives like AlmaLinux or Rocky Linux). This has the benefit to get the newest bug and security fixes, often also new features, and moving the EOL date in the future.
- Upgrade the Containers systemd version. If the distribution provides a backports repository this can be an easy and quick stop-gap measurement.
- Move the container, or its services, to a Virtual Machine. Virtual Machines have a much less interaction with the host, that’s why one can install decades old OS versions just fine there.
{% endhint %}

### Changing CGroup Version <a href="#pct_cgroup_change_version" id="pct_cgroup_change_version"></a>

Before Proxmox VE 9.0, you could switch back to the previous version with the following kernel command-line parameter:

```text
systemd.unified_cgroup_hierarchy=0
```

See [this section](../03-system-administration/13-sysboot.md#sysboot_edit_kernel_cmdline) on editing the kernel boot command line on where to add the parameter.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
