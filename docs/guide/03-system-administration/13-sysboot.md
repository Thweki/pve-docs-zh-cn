# 3.13. 宿主机引导加载程序 <a href="#sysboot" id="sysboot"></a>

Proxmox VE 目前会根据安装程序中选择的磁盘设置，使用两种引导加载程序中的一种。

对于以 ZFS 作为根文件系统安装的 EFI 系统，除非启用了 Secure Boot，否则使用 `systemd-boot`。所有其他部署都使用标准的 GRUB 引导加载程序（这通常也适用于在 Debian 之上安装的系统）。

## 3.13.1. 安装程序使用的分区方案 <a href="#sysboot_installer_part_scheme" id="sysboot_installer_part_scheme"></a>

Proxmox VE 安装程序会在所有选定用于安装的磁盘上创建 3 个分区。

创建的分区如下：

- 一个 1 MB 的 BIOS 引导分区（gdisk 类型 EF02）
- 一个 512 MB 的 EFI 系统分区（ESP，gdisk 类型 EF00）
- 第三个分区，其大小由设置的 `hdsize` 参数决定，或者使用所选存储类型的剩余空间

使用 ZFS 作为根文件系统的系统，通过存储在 512 MB EFI 系统分区上的内核和 initrd 镜像引导。对于传统 BIOS 系统以及启用了 Secure Boot 的 EFI 系统，使用 GRUB；对于未启用 Secure Boot 的 EFI 系统，使用 `systemd-boot`。两者都会安装并配置为指向 ESP。

在所有使用 GRUB 引导的系统上，BIOS 模式的 GRUB（`--target i386-pc`）会安装到所有选定磁盘的 BIOS 引导分区中 [\[1\]](#note-dbd1308e-1)。

{% hint style="info" %}
这适用于 x86 宿主机。在 arm64 上，Proxmox VE 仅通过 UEFI 引导，因此没有 BIOS 引导分区，也没有 `i386-pc` GRUB 目标；GRUB 会以 EFI 模式安装，并改用 `arm64-efi` 目标。
{% endhint %}

## 3.13.2. 使用 `proxmox-boot-tool` 同步 ESP 的内容 <a href="#sysboot_proxmox_boot_tool" id="sysboot_proxmox_boot_tool"></a>

`proxmox-boot-tool` 是一个实用程序，用于保持 EFI 系统分区的内容配置正确并同步。它将特定的内核版本复制到所有 ESP，并配置相应的引导加载程序，以便从采用 `vfat` 格式的 ESP 引导。在 ZFS 作为根文件系统的情况下，这意味着您可以在根池上使用所有可选功能，而不必局限于 GRUB 中 ZFS 实现也支持的功能子集，也不必创建一个独立的小型引导池 [\[2\]](#note-dbd1308e-2)。

在具有冗余的设置中，安装程序会为所有磁盘划分一个 ESP。这可以确保即使第一个引导设备发生故障，或者 BIOS 只能从特定磁盘引导，系统仍能启动。

在常规运行期间，ESP 不会保持挂载状态。这有助于防止系统崩溃时采用 `vfat` 格式的 ESP 发生文件系统损坏，也无需在主引导设备发生故障时手动调整 `/etc/fstab`。

`proxmox-boot-tool` 负责以下任务：

- 格式化并设置新分区
- 将新的内核镜像和 initrd 镜像复制并配置到所有列出的 ESP
- 在内核升级和其他维护任务期间同步配置
- 管理需要同步的内核版本列表
- 配置引导加载程序以引导特定内核版本（固定）

您可以通过运行以下命令查看当前配置的 ESP 及其状态：

```text
# proxmox-boot-tool status
```

### 设置新分区以用作同步的 ESP <a href="#sysboot_proxmox_boot_setup" id="sysboot_proxmox_boot_setup"></a>

要将分区格式化并初始化为同步的 ESP，例如在替换 rpool 中出现故障的 vdev 后，或在转换早于同步机制的现有系统时，可以使用 `proxmox-boot-tool`（来自 `proxmox-kernel-helper`）。

{% hint style="warning" %}
`format` 命令会格式化 `<partition>`，请务必传入正确的设备/分区！
{% endhint %}

例如，要将空分区 `/dev/sda2` 格式化为 ESP，请运行以下命令：

```text
# proxmox-boot-tool format /dev/sda2
```

要设置位于 `/dev/sda2` 上现有的未挂载 ESP，将其纳入 Proxmox VE 的内核更新同步机制，请使用以下命令：

```text
# proxmox-boot-tool init /dev/sda2
```

或

```text
# proxmox-boot-tool init /dev/sda2 grub
```

以强制使用 GRUB 而不是 `systemd-boot` 进行初始化，例如用于支持 Secure Boot。

之后，`/etc/kernel/proxmox-boot-uuids` 中应新增一行，其中包含新添加分区的 UUID。`init` 命令还会自动触发对所有已配置 ESP 的刷新。

### 更新所有 ESP 上的配置 <a href="#sysboot_proxmox_boot_refresh" id="sysboot_proxmox_boot_refresh"></a>

要复制并配置所有可引导的内核，并保持 `/etc/kernel/proxmox-boot-uuids` 中列出的所有 ESP 同步，您只需运行：

```text
# proxmox-boot-tool refresh
```

（这相当于运行 `update-grub`，适用于以 `ext4` 或 `xfs` 为根文件系统的系统）。

如果您更改了内核命令行，或者希望同步所有内核和 initrd，则需要执行此操作。

{% hint style="info" %}
`update-initramfs` 和 `apt`（必要时）都会自动触发刷新。
{% endhint %}

**由 `proxmox-boot-tool` 处理的内核版本**

默认配置以下内核版本：

- 当前正在运行的内核
- 软件包更新时新安装的版本
- 已安装内核中最新的两个版本
- 倒数第二个内核系列的最新版本（例如 5.0、5.3），如适用
- 任何手动选择的内核

**手动保持内核可引导**

如果您希望将某个内核和 initrd 镜像添加到可引导内核列表中，请使用 `proxmox-boot-tool kernel add`。

例如，运行以下命令，将 ABI 版本为 `5.0.15-1-pve` 的内核添加到需要保持安装并同步到所有 ESP 的内核列表中：

```text
# proxmox-boot-tool kernel add 5.0.15-1-pve
```

`proxmox-boot-tool kernel list` 将列出当前选择用于引导的所有内核版本：

```text
# proxmox-boot-tool kernel list
Manually selected kernels:
5.0.15-1-pve

Automatically selected kernels:
5.0.12-1-pve
4.15.18-18-pve
```

运行 `proxmox-boot-tool kernel remove` 可从手动选择的内核列表中移除一个内核，例如：

```text
# proxmox-boot-tool kernel remove 5.0.15-1-pve
```

{% hint style="info" %}
在上述手动添加或移除内核之后，必须运行 `proxmox-boot-tool refresh` 来更新所有 EFI 系统分区（ESP）。
{% endhint %}

## 3.13.3. 确定使用的引导加载程序 <a href="#sysboot_determine_bootloader_used" id="sysboot_determine_bootloader_used"></a>

[![screenshot/boot-grub.png](../../assets/screenshot-boot-grub-png-a99b5d180a67.png)](https://pve.proxmox.com/pve-docs/images/screenshot/boot-grub.png)

确定使用哪种引导加载程序的最简单、最可靠方法，是观察 Proxmox VE 节点的引导过程。

您会看到 GRUB 的蓝色方框，或者白底黑字的简洁 `systemd-boot` 界面。

[![screenshot/boot-systemdboot.png](../../assets/screenshot-boot-systemdboot-png-1363e5a3196a.png)](https://pve.proxmox.com/pve-docs/images/screenshot/boot-systemdboot.png)

从正在运行的系统确定引导加载程序可能并非 100% 准确。最安全的方法是运行以下命令：

```text
# efibootmgr -v
```

如果返回的消息表明不支持 EFI 变量，则说明 GRUB 以 BIOS/传统模式运行。

如果输出中包含类似下面的一行，则说明 GRUB 以 UEFI 模式运行。

```text
Boot0005* proxmox       [...] File(\EFI\proxmox\grubx64.efi)
```

如果活动引导项指向 `\EFI\proxmox\shimx64.efi`，如下例所示，则说明 GRUB 以启用了 Secure Boot 的 UEFI 模式运行。

```text
Boot0005* proxmox       [...] File(\EFI\proxmox\shimx64.efi)
```

如果输出中包含类似下面的一行，则说明使用的是 `systemd-boot`。

```text
Boot0006* Linux Boot Manager    [...] File(\EFI\systemd\systemd-bootx64.efi)
```

{% hint style="info" %}
上述文件名适用于 x86 宿主机。在 arm64 上，等效的二进制文件名为 `grubaa64.efi`、`shimaa64.efi` 和 `systemd-bootaa64.efi`。
{% endhint %}

通过运行：

```text
# proxmox-boot-tool status
```

您可以确定是否配置了 `proxmox-boot-tool`，这可以很好地指示系统的引导方式。

## 3.13.4. GRUB <a href="#sysboot_grub" id="sysboot_grub"></a>

多年来，GRUB 一直是引导 Linux 系统事实上的标准，并且具有相当完善的文档 [\[3\]](#note-dbd1308e-3)。

### 配置 <a href="#configuration" id="configuration"></a>

对 GRUB 配置的更改通过默认文件 `/etc/default/grub` 或 `/etc/default/grub.d` 中的配置片段完成。更改配置后，运行以下命令重新生成配置文件：[\[4\]](#note-dbd1308e-4)

```text
# update-grub
```

## 3.13.5. Systemd-boot <a href="#sysboot_systemd_boot" id="sysboot_systemd_boot"></a>

`systemd-boot` 是一个轻量级 EFI 引导加载程序。它直接从其安装所在的 EFI 系统分区（ESP）读取内核和 initrd 镜像。直接从 ESP 加载内核的主要优势是无需重新实现用于访问存储的驱动程序。在 Proxmox VE 中，使用 [`proxmox-boot-tool`](#sysboot_proxmox_boot_tool) 来保持 ESP 上的配置同步。

### 配置 <a href="#sysboot_systemd_boot_config" id="sysboot_systemd_boot_config"></a>

`systemd-boot` 通过 EFI 系统分区（ESP）根目录中的文件 `loader/loader.conf` 进行配置。详情请参阅 `loader.conf(5)` 手册页。

每个引导项都单独存放在目录 `loader/entries/` 下的一个文件中

示例 entry.conf 如下所示（`/` 指 ESP 的根目录）：

```text
title    Proxmox
version  5.0.15-1-pve
options   root=ZFS=rpool/ROOT/pve-1 boot=zfs
linux    /EFI/proxmox/5.0.15-1-pve/vmlinuz-5.0.15-1-pve
initrd   /EFI/proxmox/5.0.15-1-pve/initrd.img-5.0.15-1-pve
```

## 3.13.6. 编辑内核命令行 <a href="#sysboot_edit_kernel_cmdline" id="sysboot_edit_kernel_cmdline"></a>

您可以在以下位置修改内核命令行，具体取决于所使用的引导加载程序：

**GRUB**

内核命令行需要写入变量 `GRUB_CMDLINE_LINUX_DEFAULT`，该变量位于文件 `/etc/default/grub` 中。运行 `update-grub` 会将其内容附加到所有 `linux` 条目，这些条目位于 `/boot/grub/grub.cfg` 中。

**Systemd-boot**

内核命令行需要作为一行写入 `/etc/kernel/cmdline`。要应用更改，请运行 `proxmox-boot-tool refresh`，它会将其设置为 `option` 行，并应用于 `loader/entries/proxmox-*.conf` 中的所有配置文件。

完整的内核参数列表可在 *https://www.kernel.org/doc/html/v\<YOUR-KERNEL-VERSION\>/admin-guide/kernel-parameters.html* 找到。将 \<YOUR-KERNEL-VERSION\> 替换为主版本号.次版本号，例如，对于基于 6.5 版本的内核，URL 为：[https://www.kernel.org/doc/html/v6.5/admin-guide/kernel-parameters.html](https://www.kernel.org/doc/html/v6.5/admin-guide/kernel-parameters.html)

您可以通过查看 Web 界面（*节点 → 概要*）或运行以下命令来查找您的内核版本

```text
# uname -r
```

使用输出开头的两个数字。

## 3.13.7. 覆盖下次引导的内核版本 <a href="#sysboot_kernel_pin" id="sysboot_kernel_pin"></a>

要选择当前并非默认内核的内核，您可以：

- 使用在引导过程开始时显示的引导加载程序菜单
- 使用 `proxmox-boot-tool` 通过 `pin` 将系统固定到某个内核版本，可以仅固定一次，也可以永久固定（直到重置固定设置）。

这应该有助于您规避较新内核版本与硬件之间的不兼容问题。

{% hint style="info" %}
应尽快移除此类固定设置，以便最新内核的所有当前安全补丁也能应用于系统。
{% endhint %}

例如：要永久选择版本 `5.15.30-1-pve` 用于引导，您需要运行：

```text
# proxmox-boot-tool kernel pin 5.15.30-1-pve
```

{% hint style="success" %}
固定功能适用于所有 Proxmox VE 系统，而不仅限于使用 `proxmox-boot-tool` 同步 ESP 内容的系统；如果您的系统不使用 `proxmox-boot-tool` 进行同步，也可以跳过最后的 `proxmox-boot-tool refresh` 调用。
{% endhint %}

您还可以设置某个内核版本仅在下次系统引导时使用。例如，这可用于测试更新后的内核是否已解决最初导致您使用 `pin` 固定某个版本的问题：

```text
# proxmox-boot-tool kernel pin 5.15.30-1-pve --next-boot
```

要移除任何固定版本配置，请使用 `unpin` 子命令：

```text
# proxmox-boot-tool kernel unpin
```

虽然 `unpin` 也有 `--next-boot` 选项，但它用于清除通过 `--next-boot` 设置的固定版本。由于系统在引导时已经会自动执行此操作，因此手动调用它并没有多大用处。

设置或清除固定版本后，还需要通过运行 `refresh` 子命令来同步 ESP 上的内容和配置。

{% hint style="success" %}
如果以交互方式调用该工具，系统会提示您为 `proxmox-boot-tool` 管理的系统自动执行此操作。
{% endhint %}

```text
# proxmox-boot-tool refresh
```

## 3.13.8. Secure Boot <a href="#sysboot_secure_boot" id="sysboot_secure_boot"></a>

从 Proxmox VE 8.1 开始，通过签名软件包以及与 `proxmox-boot-tool` 的集成，开箱即用地支持 Secure Boot。

要使 Secure Boot 正常工作，需要以下软件包。您可以使用 ‘proxmox-secure-boot-support’ 元软件包一次性安装它们。

- `shim-signed`（由 Microsoft 签名的 shim 引导加载程序）
- `shim-helpers-amd64-signed`（回退引导加载程序和 MOKManager，由 Proxmox 签名）
- `grub-efi-amd64-signed`（GRUB EFI 引导加载程序，由 Proxmox 签名）
- `proxmox-kernel-6.X.Y-Z-pve-signed`（由 Proxmox 签名的内核镜像）

{% hint style="info" %}
`shim-helpers-amd64-signed` 和 `grub-efi-amd64-signed` 软件包名称适用于 x86 宿主机。在 arm64 上，对应的软件包为 `shim-helpers-arm64-signed` 和 `grub-efi-arm64-signed`。
{% endhint %}

开箱即用仅支持 GRUB 作为引导加载程序，因为其他引导加载程序目前不符合安全启动代码签名的条件。

Proxmox VE 的任何全新安装都会自动包含上述所有软件包。

有关安全启动的工作原理以及如何自定义设置的更多详细信息，请参阅[我们的 Wiki](https://pve.proxmox.com/wiki/Secure_Boot_Setup)。

### 将现有安装切换到安全启动 <a href="#switching_an_existing_installation_to_secure_boot" id="switching_an_existing_installation_to_secure_boot"></a>

{% hint style="warning" %}
如果操作不正确，在某些情况下可能会导致安装无法启动。如果可用，重新安装宿主机将自动设置安全启动，无需任何额外交互。**请确保您拥有 Proxmox VE 宿主机的可用且经过充分测试的备份！**
{% endhint %}

现有 UEFI 安装可以根据需要切换到安全启动，而无需从头重新安装 Proxmox VE。

首先，确保您的整个系统均为最新状态。接下来，安装 `proxmox-secure-boot-support`。GRUB 会自动创建所需的 EFI 启动项，以便通过默认 shim 启动。

**systemd-boot**

如果 `systemd-boot` 用作引导加载程序（请参阅[确定使用的引导加载程序](#sysboot_determine_bootloader_used)），则需要进行一些额外设置。仅当 Proxmox VE 以 ZFS-on-root 方式安装时才是这种情况。

要检查后者，请运行：

```text
# findmnt /
```

如果宿主机确实使用 ZFS 作为根文件系统，则 `FSTYPE` 列应包含 `zfs`：

```text
TARGET SOURCE           FSTYPE OPTIONS
/      rpool/ROOT/pve-1 zfs    rw,relatime,xattr,noacl,casesensitive
```

接下来，必须找到合适的候选 ESP（EFI 系统分区）。可以使用 `lsblk` 命令完成此操作，方法如下：

```text
# lsblk -o +FSTYPE
```

输出应类似于：

```text
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS FSTYPE
sda      8:0    0   32G  0 disk
├─sda1   8:1    0 1007K  0 part
├─sda2   8:2    0  512M  0 part             vfat
└─sda3   8:3    0 31.5G  0 part             zfs_member
sdb      8:16   0   32G  0 disk
├─sdb1   8:17   0 1007K  0 part
├─sdb2   8:18   0  512M  0 part             vfat
└─sdb3   8:19   0 31.5G  0 part             zfs_member
```

在这种情况下，目标分区为 `sda2` 和 `sdb2`。可以通过其 512M 的大小以及 `FSTYPE` 为 `vfat` 来识别它们；本例中的安装采用 ZFS RAID-1。

必须使用 `proxmox-boot-tool` 正确设置这些分区，以便通过 GRUB 启动。此命令（以 `sda2` 为例）必须针对每个 ESP 分别运行：

```text
# proxmox-boot-tool init /dev/sda2 grub
```

之后，您可以通过运行以下命令检查设置是否正确：

```text
# efibootmgr -v
```

此列表应包含一个类似以下内容的条目：

```text
[..]
Boot0009* proxmox       HD(2,GPT,..,0x800,0x100000)/File(\EFI\proxmox\shimx64.efi)
[..]
```

{% hint style="info" %}
旧的 `systemd-boot` 引导加载程序将保留，但会优先使用 GRUB。这样，如果出于任何原因无法在安全启动模式下使用 GRUB 启动，仍可在关闭安全启动的情况下使用 `systemd-boot` 启动系统。
{% endhint %}

现在可以重新启动宿主机，并在 UEFI 固件设置实用程序中启用安全启动。

重新启动后，UEFI 固件启动菜单中应出现一个名为 `proxmox` 的新条目供选择，该条目使用预签名的 EFI shim 启动。

如果出于任何原因在 UEFI 启动菜单中找不到 `proxmox` 条目，可以尝试手动添加（如果固件支持），方法是将文件 `\EFI\proxmox\shimx64.efi` 添加为自定义启动项。

{% hint style="info" %}
已知某些 UEFI 固件会在重新启动时丢弃 `proxmox` 启动选项。如果 `proxmox` 启动项指向磁盘上的 GRUB 安装，而该磁盘本身不是启动选项，就可能发生这种情况。如果可能，请尝试在 UEFI 固件设置实用程序中将该磁盘添加为启动选项，然后再次运行 `proxmox-boot-tool`。
{% endhint %}

{% hint style="success" %}
要注册自定义密钥，请参阅相关的[安全启动 Wiki 页面](https://pve.proxmox.com/wiki/Secure_Boot_Setup#Setup_instructions_for_db_key_variant)。
{% endhint %}

### 在安全启动中使用 DKMS/第三方模块 <a href="#using_dkms_third_party_modules_with_secure_boot" id="using_dkms_third_party_modules_with_secure_boot"></a>

在启用安全启动的系统上，内核将拒绝加载未经可信密钥签名的模块。内核软件包随附的默认模块集使用嵌入内核镜像中的临时密钥签名，该密钥受该特定版本内核镜像信任。

要加载其他模块（例如使用 DKMS 构建或手动构建的模块），需要使用安全启动堆栈信任的密钥对其进行签名。实现此目的最简单的方法是将其作为机器所有者密钥（`MOK`）通过 `mokutil` 进行注册。

`dkms` 工具会自动在 `/var/lib/dkms/mok.key` 和 `/var/lib/dkms/mok.pub` 中生成密钥对和证书，并使用其对所构建和安装的内核模块进行签名。

您可以使用以下命令查看证书内容：

```text
# openssl x509 -in /var/lib/dkms/mok.pub -noout -text
```

并使用以下命令将其注册到您的系统中：

```text
# mokutil --import /var/lib/dkms/mok.pub
input password:
input password again:
```

`mokutil` 命令会两次要求输入（临时）密码，在下一步操作中还需要再输入一次此密码！重新启动系统后，应自动启动到 `MOKManager` EFI 二进制文件，您可以在其中验证密钥/证书，并使用通过 `mokutil` 开始注册时所选择的密码确认注册。之后，内核应允许加载使用 DKMS 构建的模块（这些模块使用已注册的 `MOK` 签名）。如果需要，`MOK` 还可用于签名自定义 EFI 二进制文件和内核镜像。

相同的过程也可用于不受 DKMS 管理的自定义/第三方模块，但在这种情况下，需要手动完成密钥/证书生成和签名步骤。

## 注释

### 注释 1 <a href="#note-dbd1308e-1" id="note-dbd1308e-1"></a>

这包括所有根文件系统位于 `ext4` 或 `xfs` 上的安装，以及非 EFI 系统上根文件系统位于 ZFS 上的安装

### 注释 2 <a href="#note-dbd1308e-2" id="note-dbd1308e-2"></a>

使用 GRUB 从根 ZFS 引导 [https://openzfs.github.io/openzfs-docs/Getting%20Started/Debian/Debian%20Bookworm%20Root%20on%20ZFS.html](https://openzfs.github.io/openzfs-docs/Getting%20Started/Debian/Debian%20Bookworm%20Root%20on%20ZFS.html)

### 注释 3 <a href="#note-dbd1308e-3" id="note-dbd1308e-3"></a>

GRUB 手册 [https://www.gnu.org/software/grub/manual/grub/grub.html](https://www.gnu.org/software/grub/manual/grub/grub.html)

### 注释 4 <a href="#note-dbd1308e-4" id="note-dbd1308e-4"></a>

对于使用 `proxmox-boot-tool` 的系统，`proxmox-boot-tool
refresh` 将在 `update-grub` 时被调用。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
