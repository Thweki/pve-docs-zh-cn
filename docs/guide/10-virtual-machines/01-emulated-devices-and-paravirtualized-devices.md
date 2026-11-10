# 10.1. Emulated devices and paravirtualized devices <a href="#_emulated_devices_and_paravirtualized_devices" id="_emulated_devices_and_paravirtualized_devices"></a>

QEMU 模拟的 PC 硬件包括主板、网络控制器、SCSI、IDE 和 SATA 控制器、串口（完整列表见 `kvm(1)` 手册页），所有这些都由软件模拟。所有这些设备都是现有硬件设备的精确软件等效物，如果客户机中运行的操作系统具有适当的驱动程序，就会像在真实硬件上运行一样使用这些设备。这使 QEMU 能够运行*未经修改的*操作系统。

然而，这会带来性能开销，因为让原本应由硬件执行的功能通过软件运行，会给宿主机 CPU 带来大量额外工作。为缓解这一问题，QEMU 可以向客户机操作系统提供*半虚拟化设备*，此时客户机操作系统会识别出自己正在 QEMU 内运行，并与虚拟机监控程序协作。

QEMU 依赖 virtio 虚拟化标准，因此能够提供半虚拟化 virtio 设备，包括半虚拟化通用磁盘控制器、半虚拟化网卡、半虚拟化串口、半虚拟化 SCSI 控制器等……

{% hint style="success" %}
**强烈建议**尽可能使用 virtio 设备，因为它们可以显著提升性能，而且通常维护得更好。根据 `bonnie++(8)` 的测量结果，与模拟 IDE 控制器相比，使用 virtio 通用磁盘控制器可使顺序写入吞吐量翻倍。根据 `iperf(1)` 的测量结果，使用 virtio 网络接口可提供最高达模拟 Intel E1000 网卡三倍的吞吐量。[\[1\]](#note-4eca79aa-1)
{% endhint %}

## 注释

### 注释 1 <a href="#note-4eca79aa-1" id="note-4eca79aa-1"></a>

请参阅 KVM wiki 上的此基准测试 [https://www.linux-kvm.org/page/Using\_VirtIO\_NIC](https://www.linux-kvm.org/page/Using_VirtIO_NIC)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
