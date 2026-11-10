# 3.3. Firmware Updates <a href="#chapter_firmware_updates" id="chapter_firmware_updates"></a>

在裸机服务器上运行 Proxmox VE 时，应应用本章中的固件更新。是否适合在客户机内配置固件更新（例如使用设备直通时）在很大程度上取决于您的具体设置，因此不在本章讨论范围内。

除了定期软件更新外，固件更新对于可靠、安全的运行也很重要。

在获取和应用固件更新时，建议结合使用可用的选项，以便尽早获取更新，或确保能够获取更新。

固件一词通常在语言上分为微码（用于 CPU）和固件（用于其他设备）。

## 3.3.1. Persistent Firmware <a href="#sysadmin_firmware_persistent" id="sysadmin_firmware_persistent"></a>

本节适用于所有设备。更新后的微码通常包含在 BIOS/UEFI 更新中，并存储在主板上，而其他固件则存储在相应设备上。这种持久化方法对 CPU 尤其重要，因为它能够在启动时尽早正常加载更新后的微码。

{% hint style="danger" %}
对于某些更新（例如 BIOS/UEFI 或存储控制器更新），设备配置可能会被重置。请仔细遵循供应商的说明，并备份当前配置。
{% endhint %}

请向您的供应商确认有哪些可用的更新方法。

- 适用于服务器的便捷更新方法包括 Dell 的 Lifecycle Manager 或 HPE 的 Service Packs。
- 有时也有可用的 Linux 实用工具。例如，适用于 NVIDIA ConnectX 的 [*mlxup*](https://network.nvidia.com/support/firmware/mlxup-mft/)，或适用于 Broadcom 网卡的 [*bnxtnvm*/*niccli*](https://techdocs.broadcom.com/us/en/storage-and-ethernet-connectivity/ethernet-nic-controllers/bcm957xxx/adapters/software-installation/updating-the-firmware/manually-updating-the-adapter-firmware-on-linuxesx.html)。
- [LVFS](https://fwupd.org) is also an option if there is a cooperation with the [hardware vendor](https://fwupd.org/lvfs/vendors/) and [supported hardware](https://fwupd.org/lvfs/devices/) in use. The technical requirement for this is that the system was manufactured after 2014 and is booted via UEFI.

Proxmox VE 随附自己的 `fwupd` 软件包版本，以使用 Proxmox 签名密钥启用安全启动支持。由于在虚拟机监控程序上使用该软件包时观察到问题，此软件包有意取消了对 `udisks2` 软件包的推荐依赖。

{% hint style="success" %}
如果更新说明要求重启宿主机，请确保可以安全地执行重启。另请参阅 [节点维护](../15-ha-manager/11-ha-manager-node-maintenance.md)。
{% endhint %}

## 3.3.2. Runtime Firmware Files <a href="#sysadmin_firmware_runtime_files" id="sysadmin_firmware_runtime_files"></a>

此方法将固件存储在 Proxmox VE 操作系统上，并在设备的 [持久化固件](#sysadmin_firmware_persistent) 版本较旧时将其传递给设备。网卡和显卡等设备支持此方法，但主板和硬盘等依赖持久化固件的设备不支持。

在 Proxmox VE 中，默认已安装 `pve-firmware` 软件包。因此，通过常规的 [系统更新（APT）](02-system-software-updates.md)，其中包含的常见硬件固件会自动保持最新。

还存在一个额外的 [Debian 固件存储库](01-sysadmin-package-repositories.md#sysadmin_debian_firmware_repo)，但默认未配置。

如果您尝试安装额外的固件软件包但发生冲突，APT 将中止安装。或许可以通过其他方式获取该特定固件。

## 3.3.3. CPU Microcode Updates <a href="#sysadmin_firmware_cpu" id="sysadmin_firmware_cpu"></a>

{% hint style="info" %}
本节所述的 CPU 微码更新特定于 x86 宿主机。arm64 没有等效的操作系统级微码软件包。
{% endhint %}

微码更新旨在修复已发现的安全漏洞和其他严重的 CPU 缺陷。虽然 CPU 性能可能会受到影响，但与未打补丁、需要内核自身采取缓解措施的微码相比，打补丁后的微码通常仍具有更高的性能。根据 CPU 类型，除非明知故犯地让 CPU 在不安全状态下运行，否则可能无法再达到存在缺陷的出厂状态下的性能水平。

要概览当前 CPU 漏洞及其缓解措施，请运行 `lscpu`。只有当 Proxmox VE 宿主机处于 [最新状态](02-system-software-updates.md)、其版本未处于 [生命周期结束](../20-frequently-asked-questions-2/README.md#faq-support-table) 状态，并且自上次内核更新以来至少重启过一次时，才会显示当前已知的实际漏洞。

除了通过 [持久化](#sysadmin_firmware_persistent) BIOS/UEFI 更新来更新微码的推荐方法外，还有一种通过 **操作系统早期微码更新** 的独立方法。它使用方便，在主板供应商不再提供 BIOS/UEFI 更新时也特别有帮助。无论使用哪种方法，应用微码更新都始终需要重启。

### Set up Early OS Microcode Updates <a href="#_set_up_early_os_microcode_updates" id="_set_up_early_os_microcode_updates"></a>

要配置由 Linux 内核在启动早期应用的微码更新，您需要：

1. Enable the [Debian Firmware Repository](01-sysadmin-package-repositories.md#sysadmin_debian_firmware_repo)
2. 获取最新的可用软件包 `apt update`（或使用 Web 界面，在“节点 → 更新”下）
3. 安装特定于 CPU 供应商的微码软件包：

   - For Intel CPUs: `apt install intel-microcode`
   - For AMD CPUs: `apt install amd64-microcode`
4. 重启 Proxmox VE 宿主机

今后的任何微码更新也需要重启才能加载。

### Microcode Version <a href="#_microcode_version" id="_microcode_version"></a>

要获取当前运行的微码修订版本，以便进行比较或调试：

```text
# grep microcode /proc/cpuinfo | uniq
microcode       : 0xf0
```

一个微码软件包包含适用于许多不同 CPU 的更新。但专门针对您的 CPU 的更新可能并不常有。因此，仅查看软件包上的日期，无法得知该公司实际何时为您的特定 CPU 发布了更新。

如果您安装了新的微码软件包并重启了 Proxmox VE 宿主机，且此新微码比 CPU 内置的版本和主板固件中的版本都更新，您将在系统日志中看到一条显示 "microcode updated early" 的消息。

```text
# dmesg | grep microcode
[    0.000000] microcode: microcode updated early to revision 0xf0, date = 2021-11-12
[    0.896580] microcode: Microcode Update Driver: v2.2.
```

### Troubleshooting <a href="#sysadmin_firmware_troubleshooting" id="sysadmin_firmware_troubleshooting"></a>

出于调试目的，可以按如下方式临时禁用已配置、通常在系统启动时应用的操作系统早期微码更新：

1. make sure that the host can be rebooted [safely](../15-ha-manager/11-ha-manager-node-maintenance.md)
2. 重启宿主机以进入 GRUB 菜单（如果菜单被隐藏，请按住 `SHIFT`）
3. at the desired Proxmox VE boot entry press `E`
4. go to the line which starts with `linux` and append separated by a space **`dis_ucode_ldr`**
5. 按 `CTRL-X` 启动，此次启动将不应用操作系统早期微码更新

如果怀疑问题与最近的微码更新有关，应考虑降级软件包，而不是移除软件包（`apt purge <intel-microcode|amd64-microcode>`）。否则，即使较新的微码可以正常运行，也可能会加载过旧的 [持久化](#sysadmin_firmware_persistent) 微码。

如果 Debian 存储库中有更早的微码软件包版本，则可以降级，如以下示例所示：

```text
# apt list -a intel-microcode
Listing... Done
intel-microcode/stable-security,now 3.20230808.1~deb12u1 amd64 [installed]
intel-microcode/stable 3.20230512.1 amd64
```

```text
# apt install intel-microcode=3.202305*
...
Selected version '3.20230512.1' (Debian:12.1/stable [amd64]) for 'intel-microcode'
...
dpkg: warning: downgrading intel-microcode from 3.20230808.1~deb12u1 to 3.20230512.1
...
intel-microcode: microcode will be updated at next boot
...
```

请（再次）确保宿主机可以 [安全地](../15-ha-manager/11-ha-manager-node-maintenance.md) 重启。要立即应用微码软件包中可能包含的、适用于您的 CPU 类型的较旧微码，请现在重启。

{% hint style="success" %}
最好将降级后的软件包锁定一段时间，并在稍后重试较新的版本。即使将来软件包版本相同，系统更新也可能在此期间已修复您遇到的问题。

```text
# apt-mark hold intel-microcode
intel-microcode set on hold.
```

```text
# apt-mark unhold intel-microcode
# apt update
# apt full-upgrade
```
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
