# 3.3. Firmware Updates <a href="#chapter_firmware_updates" id="chapter_firmware_updates"></a>

Firmware updates from this chapter should be applied when running Proxmox VE on a bare-metal server. Whether configuring firmware updates is appropriate within guests, e.g. when using device pass-through, depends strongly on your setup and is therefore out of scope.

In addition to regular software updates, firmware updates are also important for reliable and secure operation.

When obtaining and applying firmware updates, a combination of available options is recommended to get them as early as possible or at all.

The term firmware is usually divided linguistically into microcode (for CPUs) and firmware (for other devices).

## 3.3.1. Persistent Firmware <a href="#sysadmin_firmware_persistent" id="sysadmin_firmware_persistent"></a>

This section is suitable for all devices. Updated microcode, which is usually included in a BIOS/UEFI update, is stored on the motherboard, whereas other firmware is stored on the respective device. This persistent method is especially important for the CPU, as it enables the earliest possible regular loading of the updated microcode at boot time.

{% hint style="danger" %}
With some updates, such as for BIOS/UEFI or storage controller, the device configuration could be reset. Please follow the vendor’s instructions carefully and back up the current configuration.
{% endhint %}

Please check with your vendor which update methods are available.

- Convenient update methods for servers can include Dell’s Lifecycle Manager or Service Packs from HPE.
- Sometimes there are Linux utilities available as well. Examples are [*mlxup*](https://network.nvidia.com/support/firmware/mlxup-mft/) for NVIDIA ConnectX or [*bnxtnvm*/*niccli*](https://techdocs.broadcom.com/us/en/storage-and-ethernet-connectivity/ethernet-nic-controllers/bcm957xxx/adapters/software-installation/updating-the-firmware/manually-updating-the-adapter-firmware-on-linuxesx.html) for Broadcom network cards.
- [LVFS](https://fwupd.org) is also an option if there is a cooperation with the [hardware vendor](https://fwupd.org/lvfs/vendors/) and [supported hardware](https://fwupd.org/lvfs/devices/) in use. The technical requirement for this is that the system was manufactured after 2014 and is booted via UEFI.

Proxmox VE ships its own version of the `fwupd` package to enable Secure Boot Support with the Proxmox signing key. This package consciously dropped the dependency recommendation for the `udisks2` package, due to observed issues with its use on hypervisors.

{% hint style="success" %}
If the update instructions require a host reboot, make sure that it can be done safely. See also [Node Maintenance](../15-ha-manager/11-ha-manager-node-maintenance.md#ha_manager_node_maintenance).
{% endhint %}

## 3.3.2. Runtime Firmware Files <a href="#sysadmin_firmware_runtime_files" id="sysadmin_firmware_runtime_files"></a>

This method stores firmware on the Proxmox VE operating system and will pass it to a device if its [persisted firmware](#sysadmin_firmware_persistent) is less recent. It is supported by devices such as network and graphics cards, but not by those that rely on persisted firmware such as the motherboard and hard disks.

In Proxmox VE the package `pve-firmware` is already installed by default. Therefore, with the normal [system updates (APT)](02-system-software-updates.md#system_software_updates), included firmware of common hardware is automatically kept up to date.

An additional [Debian Firmware Repository](01-sysadmin-package-repositories.md#sysadmin_debian_firmware_repo) exists, but is not configured by default.

If you try to install an additional firmware package but it conflicts, APT will abort the installation. Perhaps the particular firmware can be obtained in another way.

## 3.3.3. CPU Microcode Updates <a href="#sysadmin_firmware_cpu" id="sysadmin_firmware_cpu"></a>

{% hint style="info" %}
CPU microcode updates as described in this section are specific to x86 hosts. There is no equivalent operating-system-level microcode package for arm64.
{% endhint %}

Microcode updates are intended to fix found security vulnerabilities and other serious CPU bugs. While the CPU performance can be affected, a patched microcode is usually still more performant than an unpatched microcode where the kernel itself has to do mitigations. Depending on the CPU type, it is possible that performance results of the flawed factory state can no longer be achieved without knowingly running the CPU in an unsafe state.

To get an overview of present CPU vulnerabilities and their mitigations, run `lscpu`. Current real-world known vulnerabilities can only show up if the Proxmox VE host is [up to date](02-system-software-updates.md#system_software_updates), its version not [end of life](../20-frequently-asked-questions-2/README.md#faq-support-table), and has at least been rebooted since the last kernel update.

Besides the recommended microcode update via [persistent](#sysadmin_firmware_persistent) BIOS/UEFI updates, there is also an independent method via **Early OS Microcode Updates**. It is convenient to use and also quite helpful when the motherboard vendor no longer provides BIOS/UEFI updates. Regardless of the method in use, a reboot is always needed to apply a microcode update.

### Set up Early OS Microcode Updates <a href="#_set_up_early_os_microcode_updates" id="_set_up_early_os_microcode_updates"></a>

To set up microcode updates that are applied early on boot by the Linux kernel, you need to:

1. Enable the [Debian Firmware Repository](01-sysadmin-package-repositories.md#sysadmin_debian_firmware_repo)
2. Get the latest available packages `apt update` (or use the web interface, under Node → Updates)
3. Install the CPU-vendor specific microcode package:

   - For Intel CPUs: `apt install intel-microcode`
   - For AMD CPUs: `apt install amd64-microcode`
4. Reboot the Proxmox VE host

Any future microcode update will also require a reboot to be loaded.

### Microcode Version <a href="#_microcode_version" id="_microcode_version"></a>

To get the current running microcode revision for comparison or debugging purposes:

```text
# grep microcode /proc/cpuinfo | uniq
microcode       : 0xf0
```

A microcode package has updates for many different CPUs. But updates specifically for your CPU might not come often. So, just looking at the date on the package won’t tell you when the company actually released an update for your specific CPU.

If you’ve installed a new microcode package and rebooted your Proxmox VE host, and this new microcode is newer than both, the version baked into the CPU and the one from the motherboard’s firmware, you’ll see a message in the system log saying "microcode updated early".

```text
# dmesg | grep microcode
[    0.000000] microcode: microcode updated early to revision 0xf0, date = 2021-11-12
[    0.896580] microcode: Microcode Update Driver: v2.2.
```

### Troubleshooting <a href="#sysadmin_firmware_troubleshooting" id="sysadmin_firmware_troubleshooting"></a>

For debugging purposes, the set up Early OS Microcode Update applied regularly at system boot can be temporarily disabled as follows:

1. make sure that the host can be rebooted [safely](../15-ha-manager/11-ha-manager-node-maintenance.md#ha_manager_node_maintenance)
2. reboot the host to get to the GRUB menu (hold `SHIFT` if it is hidden)
3. at the desired Proxmox VE boot entry press `E`
4. go to the line which starts with `linux` and append separated by a space **`dis_ucode_ldr`**
5. press `CTRL-X` to boot this time without an Early OS Microcode Update

If a problem related to a recent microcode update is suspected, a package downgrade should be considered instead of package removal (`apt purge <intel-microcode|amd64-microcode>`). Otherwise, a too old [persisted](#sysadmin_firmware_persistent) microcode might be loaded, even though a more recent one would run without problems.

A downgrade is possible if an earlier microcode package version is available in the Debian repository, as shown in this example:

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

Make sure (again) that the host can be rebooted [safely](../15-ha-manager/11-ha-manager-node-maintenance.md#ha_manager_node_maintenance). To apply an older microcode potentially included in the microcode package for your CPU type, reboot now.

{% hint style="success" %}
It makes sense to hold the downgraded package for a while and try more recent versions again at a later time. Even if the package version is the same in the future, system updates may have fixed the experienced problem in the meantime.

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
