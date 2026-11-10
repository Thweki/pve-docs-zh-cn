# 10\. QEMU/KVM Virtual Machines <a href="#chapter_virtual_machines" id="chapter_virtual_machines"></a>

QEMU (short form for Quick Emulator) is an open source hypervisor that emulates a physical computer. From the perspective of the host system where QEMU is running, QEMU is a user program which has access to a number of local resources like partitions, files, network cards which are then passed to an emulated computer which sees them as if they were real devices.

A guest operating system running in the emulated computer accesses these devices, and runs as if it were running on real hardware. For instance, you can pass an ISO image as a parameter to QEMU, and the OS running in the emulated computer will see a real CD-ROM inserted into a CD drive.

QEMU can emulate a great variety of hardware, from ARM to Sparc. On x86 hosts, Proxmox VE is concerned with 32-bit and 64-bit PC clone emulation, since it represents the overwhelming majority of server hardware. On arm64 hosts, Proxmox VE emulates 64-bit ARM (aarch64) machines instead. Emulating the same architecture as the host is also one of the fastest options, due to the availability of processor extensions which greatly speed up QEMU when the emulated architecture matches the host architecture.

{% hint style="info" %}
You may sometimes encounter the term *KVM* (Kernel-based Virtual Machine). It means that QEMU is running with the support of the virtualization processor extensions, via the Linux KVM module. In the context of Proxmox VE *QEMU* and *KVM* can be used interchangeably, as QEMU in Proxmox VE will always try to load the KVM module.
{% endhint %}

QEMU inside Proxmox VE runs as a root process, since this is required to access block and PCI devices.

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
