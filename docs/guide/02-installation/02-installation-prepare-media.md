# 2.2. Prepare Installation Media <a href="#installation_prepare_media" id="installation_prepare_media"></a>

从以下地址下载安装程序 ISO 映像：[https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso](https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso)

Proxmox VE 安装介质是混合 ISO 映像。它有以下两种使用方式：

- 可刻录到 CD 或 DVD 的 ISO 映像文件。
- 可复制到 USB 闪存驱动器（U 盘）的原始扇区（IMG）映像文件。

建议使用 USB 闪存驱动器安装 Proxmox VE，因为这种方式速度更快。

## 2.2.1. Prepare a USB Flash Drive as Installation Medium <a href="#_prepare_a_usb_flash_drive_as_installation_medium" id="_prepare_a_usb_flash_drive_as_installation_medium"></a>

闪存驱动器的容量必须大于 ISO 映像。

{% hint style="info" %}
请勿使用 UNetbootin。它无法与 Proxmox VE 安装映像配合使用。
{% endhint %}

{% hint style="warning" %}
请确保 USB 闪存驱动器未挂载，且其中不包含任何重要数据。
{% endhint %}

## 2.2.2. Instructions for GNU/Linux <a href="#_instructions_for_gnu_linux" id="_instructions_for_gnu_linux"></a>

在类 Unix 操作系统上，使用 `dd` 命令将 ISO 映像复制到 USB 闪存驱动器。首先找到 USB 闪存驱动器的正确设备名称（见下文）。然后运行 `dd` 命令。

```text
# dd bs=1M conv=fdatasync if=./proxmox-ve_*.iso of=/dev/XYZ
```

{% hint style="info" %}
请务必将 /dev/XYZ 替换为正确的设备名称，并调整输入文件名（*if*）的路径。
{% endhint %}

{% hint style="danger" %}
请务必小心，不要覆盖错误的磁盘！
{% endhint %}

### Find the Correct USB Device Name <a href="#_find_the_correct_usb_device_name" id="_find_the_correct_usb_device_name"></a>

有两种方法可以确定 USB 闪存驱动器的名称。第一种方法是比较插入闪存驱动器前后 `dmesg` 命令输出的最后几行。第二种方法是比较 `lsblk` 命令的输出。打开终端并运行：

```text
# lsblk
```

然后插入 USB 闪存驱动器，并再次运行该命令：

```text
# lsblk
```

此时会出现一个新设备。这就是您要使用的设备。为更加稳妥，请检查报告的大小是否与您的 USB 闪存驱动器相符。

## 2.2.3. Instructions for macOS <a href="#_instructions_for_macos" id="_instructions_for_macos"></a>

打开终端（在 Spotlight 中搜索 Terminal）。

将 `.iso` 文件转换为 `.dmg` 格式，可使用 `hdiutil` 的 convert 选项，例如：

```text
# hdiutil convert proxmox-ve_*.iso -format UDRW -o proxmox-ve_*.dmg
```

{% hint style="success" %}
macOS 往往会自动将 *.dmg* 附加到输出文件名中。
{% endhint %}

要获取当前设备列表，请运行以下命令：

```text
# diskutil list
```

现在插入 USB 闪存驱动器，然后再次运行此命令，以确定分配给它的设备节点（例如 /dev/diskX）。

```text
# diskutil list
# diskutil unmountDisk /dev/diskX
```

{% hint style="info" %}
将 X 替换为上一条命令中的磁盘编号。
{% endhint %}

```text
# sudo dd if=proxmox-ve_*.dmg bs=1M of=/dev/rdiskX
```

{% hint style="info" %}
上一条命令中故意使用的是 *rdiskX*，而不是 *diskX*。这样可以提高写入速度。
{% endhint %}

## 2.2.4. Instructions for Windows <a href="#_instructions_for_windows" id="_instructions_for_windows"></a>

### Using Etcher <a href="#_using_etcher" id="_using_etcher"></a>

Etcher 开箱即用。请从 [https://etcher.io](https://etcher.io) 下载 Etcher。它会引导您完成选择 ISO 和 USB 闪存盘的过程。

### Using Rufus <a href="#_using_rufus" id="_using_rufus"></a>

Rufus 是一种更轻量级的替代方案，但您需要使用 **DD 模式** 才能正常工作。请从 [https://rufus.ie/](https://rufus.ie/) 下载 Rufus。您可以安装它，也可以使用便携版。选择目标驱动器和 Proxmox VE ISO 文件。

{% hint style="warning" %}
点击 *开始* 后，在询问是否下载其他版本 GRUB 的对话框中，必须点击 *否*。在下一个对话框中选择 *DD* 模式。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
