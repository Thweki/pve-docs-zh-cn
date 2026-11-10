# 2.2. Prepare Installation Media <a href="#installation_prepare_media" id="installation_prepare_media"></a>

Download the installer ISO image from: [https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso](https://www.proxmox.com/en/downloads/proxmox-virtual-environment/iso)

The Proxmox VE installation media is a hybrid ISO image. It works in two ways:

- An ISO image file ready to burn to a CD or DVD.
- A raw sector (IMG) image file ready to copy to a USB flash drive (USB stick).

Using a USB flash drive to install Proxmox VE is the recommended way because it is the faster option.

## 2.2.1. Prepare a USB Flash Drive as Installation Medium <a href="#_prepare_a_usb_flash_drive_as_installation_medium" id="_prepare_a_usb_flash_drive_as_installation_medium"></a>

The flash drive needs to be larger than the ISO image.

{% hint style="info" %}
Do not use UNetbootin. It does not work with the Proxmox VE installation image.
{% endhint %}

{% hint style="warning" %}
Make sure that the USB flash drive is not mounted and does not contain any important data.
{% endhint %}

## 2.2.2. Instructions for GNU/Linux <a href="#_instructions_for_gnu_linux" id="_instructions_for_gnu_linux"></a>

On Unix-like operating system use the `dd` command to copy the ISO image to the USB flash drive. First find the correct device name of the USB flash drive (see below). Then run the `dd` command.

```text
# dd bs=1M conv=fdatasync if=./proxmox-ve_*.iso of=/dev/XYZ
```

{% hint style="info" %}
Be sure to replace /dev/XYZ with the correct device name and adapt the input filename (*if*) path.
{% endhint %}

{% hint style="danger" %}
Be very careful, and do not overwrite the wrong disk!
{% endhint %}

### Find the Correct USB Device Name <a href="#_find_the_correct_usb_device_name" id="_find_the_correct_usb_device_name"></a>

There are two ways to find out the name of the USB flash drive. The first one is to compare the last lines of the `dmesg` command output before and after plugging in the flash drive. The second way is to compare the output of the `lsblk` command. Open a terminal and run:

```text
# lsblk
```

Then plug in your USB flash drive and run the command again:

```text
# lsblk
```

A new device will appear. This is the one you want to use. To be on the extra safe side check if the reported size matches your USB flash drive.

## 2.2.3. Instructions for macOS <a href="#_instructions_for_macos" id="_instructions_for_macos"></a>

Open the terminal (query Terminal in Spotlight).

Convert the `.iso` file to `.dmg` format using the convert option of `hdiutil`, for example:

```text
# hdiutil convert proxmox-ve_*.iso -format UDRW -o proxmox-ve_*.dmg
```

{% hint style="success" %}
macOS tends to automatically add *.dmg* to the output file name.
{% endhint %}

To get the current list of devices run the command:

```text
# diskutil list
```

Now insert the USB flash drive and run this command again to determine which device node has been assigned to it. (e.g., /dev/diskX).

```text
# diskutil list
# diskutil unmountDisk /dev/diskX
```

{% hint style="info" %}
replace X with the disk number from the last command.
{% endhint %}

```text
# sudo dd if=proxmox-ve_*.dmg bs=1M of=/dev/rdiskX
```

{% hint style="info" %}
*rdiskX*, instead of *diskX*, in the last command is intended. It will increase the write speed.
{% endhint %}

## 2.2.4. Instructions for Windows <a href="#_instructions_for_windows" id="_instructions_for_windows"></a>

### Using Etcher <a href="#_using_etcher" id="_using_etcher"></a>

Etcher works out of the box. Download Etcher from [https://etcher.io](https://etcher.io). It will guide you through the process of selecting the ISO and your USB flash drive.

### Using Rufus <a href="#_using_rufus" id="_using_rufus"></a>

Rufus is a more lightweight alternative, but you need to use the **DD mode** to make it work. Download Rufus from [https://rufus.ie/](https://rufus.ie/). Either install it or use the portable version. Select the destination drive and the Proxmox VE ISO file.

{% hint style="warning" %}
Once you *Start* you have to click *No* on the dialog asking to download a different version of GRUB. In the next dialog select the *DD* mode.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
