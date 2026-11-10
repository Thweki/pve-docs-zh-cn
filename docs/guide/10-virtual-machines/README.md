# 10\. QEMU/KVM Virtual Machines <a href="#chapter_virtual_machines" id="chapter_virtual_machines"></a>

QEMU（Quick Emulator 的缩写）是一种开源虚拟机监控程序，用于模拟物理计算机。从运行 QEMU 的宿主系统的角度来看，QEMU 是一个用户程序，可以访问分区、文件、网卡等多种本地资源，然后将这些资源传递给模拟计算机，后者将它们视为真实设备。

在模拟计算机中运行的客户机操作系统会访问这些设备，并像在真实硬件上运行一样工作。例如，可以将 ISO 镜像作为参数传递给 QEMU，在模拟计算机中运行的操作系统就会看到 CD 驱动器中插入了一张真实的 CD-ROM。

QEMU 可以模拟从 ARM 到 Sparc 的多种硬件。在 x86 宿主机上，Proxmox VE 关注 32 位和 64 位 PC 兼容机模拟，因为它们代表了绝大多数服务器硬件。在 arm64 宿主机上，Proxmox VE 则模拟 64 位 ARM（aarch64）机器。模拟与宿主机相同的架构也是最快的选项之一，因为当模拟架构与宿主机架构匹配时，可用的处理器扩展可以大幅加速 QEMU。

{% hint style="info" %}
有时您会遇到术语 *KVM*（Kernel-based Virtual Machine，基于内核的虚拟机）。它表示 QEMU 通过 Linux KVM 模块，在处理器虚拟化扩展的支持下运行。在 Proxmox VE 的语境中，*QEMU* 和 *KVM* 可以互换使用，因为 Proxmox VE 中的 QEMU 始终会尝试加载 KVM 模块。
{% endhint %}

Proxmox VE 内部的 QEMU 以 root 进程运行，因为访问块设备和 PCI 设备需要这样做。

## 本章内容

- [10.1. Emulated devices and paravirtualized devices](01-emulated-devices-and-paravirtualized-devices.md)
- [10.2. Virtual Machines Settings](02-qm-virtual-machines-settings.md)
- [10.3. Migration](03-qm-migration.md)
- [10.4. Copies and Clones](04-qm-copy-and-clone.md)
- [10.5. Virtual Machine Templates](05-qm-templates.md)
- [10.6. VM Generation ID](06-vm-generation-id.md)
- [10.7. Importing Virtual Machines](07-qm-import-virtual-machines.md)
- [10.8. Cloud-Init Support](08-qm-cloud-init.md)
- [10.9. PCI(e) Passthrough](09-qm-pci-passthrough.md)
- [10.10. Hookscripts](10-hookscripts.md)
- [10.11. Hibernation](11-qm-hibernate.md)
- [10.12. Resource Mapping](12-resource-mapping.md)
- [10.13. Managing Virtual Machines with qm](13-managing-virtual-machines-with-span-class-monospaced-qm-span.md)
- [10.14. Configuration](14-qm-configuration.md)
- [10.15. Locks](15-locks.md)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
