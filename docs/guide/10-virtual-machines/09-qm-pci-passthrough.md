# 10.9. PCI(e) 直通 <a href="#qm_pci_passthrough" id="qm_pci_passthrough"></a>

PCI(e) 直通是一种让虚拟机控制宿主机 PCI 设备的机制。与使用虚拟化硬件相比，这可能具有一些优势，例如更低的延迟、更高的性能或更多功能（例如卸载）。

但是，如果将设备直通给虚拟机，您将无法再在宿主机或任何其他虚拟机中使用该设备。

请注意，虽然 i440fx 和 q35 机器都支持 PCI 直通，但 PCIe 直通仅适用于 q35 机器。这并不意味着作为 PCI 设备直通的 PCIe 设备只能以 PCI 速度运行。以 PCIe 方式直通设备只是为客户机设置一个标志，告知它该设备是 PCIe 设备，而不是“速度非常快的传统 PCI 设备”。某些客户机应用程序会从中受益。

## 10.9.1. 一般要求 <a href="#_general_requirements" id="_general_requirements"></a>

由于直通是在真实硬件上执行的，因此需要满足一些要求。下面简要介绍这些要求；有关特定设备的更多信息，请参阅 [PCI 直通示例](https://pve.proxmox.com/wiki/PCI_Passthrough)。

### 硬件 <a href="#_hardware_3" id="_hardware_3"></a>

您的硬件需要支持 `IOMMU`（**I**/**O** **M**emory **M**anagement **U**nit）中断重映射，其中包括 CPU 和主板。

通常，支持 VT-d 的 Intel 系统和支持 AMD-Vi 的 AMD 系统都支持此功能。在 arm64 上，等效功能是由受支持平台提供的系统内存管理单元（SMMU）。由于硬件实现不佳以及驱动程序缺失或质量不高，无法保证一切都能开箱即用。

此外，服务器级硬件通常比消费级硬件提供更好的支持，但即便如此，许多现代系统也能支持此功能。

请咨询您的硬件供应商，以确认您的特定配置在 Linux 下是否支持此功能。

### 确定 PCI 卡地址 <a href="#_determining_pci_card_address" id="_determining_pci_card_address"></a>

最简单的方法是在虚拟机的硬件选项卡中使用 GUI 添加类型为“Host PCI”的设备。或者，您也可以使用命令行。

您可以使用以下命令定位您的卡：

```text
 lspci
```

### 配置 <a href="#_configuration_12" id="_configuration_12"></a>

确认硬件支持直通后，您需要进行一些配置来启用 PCI(e) 直通。

**IOMMU**

您必须在 BIOS/UEFI 中启用 IOMMU 支持。通常，相应设置称为 `IOMMU` 或 `VT-d`，但您应在主板手册中查找确切的选项名称。

对于 AMD CPU，IOMMU 默认启用。对于较新的内核（6.8 或更高版本），Intel CPU 也是如此。对于较旧的内核，需要在 Intel CPU 上通过向 [内核命令行](../03-system-administration/13-sysboot.md#sysboot_edit_kernel_cmdline) 添加以下内容来启用它：

```text
 intel_iommu=on
```

{% hint style="info" %}
`intel_iommu=on` 参数适用于 x86 宿主机。在 arm64 上，SMMU 通过固件和 ACPI 启用，因此不需要此类内核命令行参数。
{% endhint %}

**IOMMU 直通模式**

如果您的硬件支持 IOMMU 直通模式，启用此模式可能会提高性能。这是因为虚拟机随后会绕过通常由虚拟机监控程序执行的（默认）DMA 转换，改为将 DMA 请求直接传递给硬件 IOMMU。要启用这些选项，请添加：

```text
 iommu=pt
```

到 [内核命令行](../03-system-administration/13-sysboot.md#sysboot_edit_kernel_cmdline)。

**内核模块**

通过将以下模块添加到 `'/etc/modules-load.d/'` 下的文件中（例如 `'/etc/modules-load.d/vfio.conf'`），确保加载这些模块：

{% hint style="info" %}
**中介设备直通**

如果直通的是中介设备（例如 vGPU），则不需要执行以下操作。在这些情况下，设备将直接由相应的宿主机驱动程序管理。
{% endhint %}

```text
 vfio
 vfio_iommu_type1
 vfio_pci
```

<a id="qm_pci_passthrough_update_initramfs"></a>



更改任何与模块相关的内容后，您需要刷新 `initramfs`。在 Proxmox VE 上，可以通过执行以下命令来完成：

```text
# update-initramfs -u -k all
```

要检查模块是否已加载，以下命令的输出

```text
# lsmod | grep vfio
```

应包含上述三个模块。

**完成配置**

最后，重启以使更改生效，并检查 IOMMU 是否确实已启用。

```text
# dmesg | grep -e DMAR -e IOMMU -e AMD-Vi
```

应显示 `IOMMU`、`Directed I/O` 或 `Interrupt Remapping` 已启用，具体消息可能因硬件和内核而异。

有关如何排除故障或验证 IOMMU 是否按预期工作的说明，请参阅我们 Wiki 中的 [验证 IOMMU 参数](https://pve.proxmox.com/wiki/PCI_Passthrough#Verifying_IOMMU_parameters) 部分。

同样重要的是，您要直通的设备必须位于 **独立的** `IOMMU` 组中。可以通过调用 Proxmox VE API 来检查这一点：

```text
# pvesh get /nodes/{nodename}/hardware/pci --pci-class-blacklist ""
```

如果设备与其功能（例如 GPU 与 HDMI 音频设备）或其根端口或 PCI(e) 网桥位于同一个 `IOMMU` 组中，则没有问题。

{% hint style="info" %}
**PCI(e) 插槽**

某些平台处理其物理 PCI(e) 插槽的方式有所不同。如果无法获得所需的 `IOMMU` 组隔离，有时将卡插入另一个 PCI(e) 插槽可能会有所帮助。
{% endhint %}

{% hint style="info" %}
**不安全的中断**

For some platforms, it may be necessary to allow unsafe interrupts. To do so, add the following line to a file ending in `.conf` under **/etc/modprobe.d/**:

```text
 options vfio_iommu_type1 allow_unsafe_interrupts=1
```

请注意，此选项可能会导致系统不稳定。
{% endhint %}

### GPU 直通注意事项 <a href="#_gpu_passthrough_notes" id="_gpu_passthrough_notes"></a>

无法通过 Proxmox VE Web 界面上的 NoVNC 或 SPICE 显示 GPU 的帧缓冲区。

在直通整个 GPU 或 vGPU 且需要图形输出时，必须将显示器物理连接到显卡，或者在客户机内配置远程桌面软件（例如 VNC 或 RDP）。

如果只想将 GPU 用作硬件加速器（例如供使用 OpenCL 或 CUDA 的程序使用），则无需这样做。

## 10.9.2. 宿主机设备直通 <a href="#_host_device_passthrough" id="_host_device_passthrough"></a>

PCI(e) 直通最常用的方式是直通整张 PCI(e) 卡，例如 GPU 或网卡。

### 宿主机配置 <a href="#_host_configuration" id="_host_configuration"></a>

Proxmox VE 会尝试自动使 PCI(e) 设备对宿主机不可用。但是，如果此方法无效，可以采取以下两种措施：

- 通过添加以下内容，将设备 ID 传递给 *vfio-pci* 模块的选项：

  ```text
   options vfio-pci ids=1234:5678,4321:8765
  ```

  添加到一个 `.conf` 文件中，该文件位于 **/etc/modprobe.d/**，其中 `1234:5678` 和 `4321:8765` 是通过以下命令获取的供应商 ID 和设备 ID：

  ```text
  # lspci -nn
  ```
- 通过添加以下内容，在宿主机上彻底将驱动程序列入黑名单，以确保设备可以改为绑定以用于直通：

  ```text
   blacklist DRIVERNAME
  ```

  添加到一个 `.conf` 文件中，该文件位于 **/etc/modprobe.d/**。

  要查找驱动程序名称，请执行

  ```text
  # lspci -k
  ```

  例如：

  ```text
  # lspci -k | grep -A 3 "VGA"
  ```

  将输出类似以下内容

  ```text
  01:00.0 VGA compatible controller: NVIDIA Corporation GP108 [GeForce GT 1030] (rev a1)
          Subsystem: Micro-Star International Co., Ltd. [MSI] GP108 [GeForce GT 1030]
          Kernel driver in use: <some-module>
          Kernel modules: <some-module>
  ```

  现在，可以将这些驱动程序写入一个 `.conf` 文件，将其列入黑名单：

  ```text
  echo "blacklist <some-module>" >> /etc/modprobe.d/blacklist.conf
  ```

对于这两种方法，都需要[更新 `initramfs`](#qm_pci_passthrough_update_initramfs)，然后重新启动。

如果这样仍然无效，可能需要设置软依赖，以便在加载 GPU 模块之前加载 *vfio-pci*。可以使用 *softdep* 标志来实现，更多信息另请参阅 *modprobe.d* 的手册页。

例如，如果使用的驱动程序名为 \<some-module\>：

```text
# echo "softdep <some-module> pre: vfio-pci" >> /etc/modprobe.d/<some-module>.conf
```

**验证配置**

要检查更改是否成功，可以使用

```text
# lspci -nnk
```

并检查设备条目。如果显示

```text
Kernel driver in use: vfio-pci
```

或者完全没有 *in use* 行，则该设备已可用于直通。

{% hint style="info" %}
**中介设备**

对于中介设备，此行会有所不同，因为设备将直接由宿主机驱动程序控制，而不是由 *vfio-pci* 控制。
{% endhint %}

### 虚拟机配置 <a href="#qm_pci_passthrough_vm_config" id="qm_pci_passthrough_vm_config"></a>

直通 GPU 时，使用 *q35* 作为机器类型、使用 *OVMF*（虚拟机的 *UEFI*）代替 SeaBIOS，并使用 PCIe 代替 PCI，可获得最佳兼容性。请注意，如果要使用 *OVMF* 进行 GPU 直通，GPU 必须具有支持 UEFI 的 ROM，否则请改用 SeaBIOS。要检查 ROM 是否支持 UEFI，请参阅 [PCI 直通示例](https://pve.proxmox.com/wiki/PCI_Passthrough#How_to_know_if_a_graphics_card_is_UEFI_.28OVMF.29_compatible) Wiki。

此外，使用 OVMF 时，有可能禁用 VGA 仲裁，从而减少启动时需要运行的旧式代码。要禁用 VGA 仲裁：

```text
 echo "options vfio-pci ids=<vendor-id>,<device-id> disable_vga=1" > /etc/modprobe.d/vfio.conf
```

将 \<vendor-id\> 和 \<device-id\> 替换为通过以下命令获取的值：

```text
# lspci -nn
```

可以在 Web 界面的虚拟机硬件部分添加 PCI 设备。也可以使用命令行；在虚拟机配置中设置 **hostpciX** 选项，例如执行：

```text
# qm set VMID -hostpci0 00:02.0
```

或者在虚拟机配置文件中添加一行：

```text
 hostpci0: 00:02.0
```

如果设备具有多个功能（例如“`00:02.0`”和“`00:02.1`”），可以使用简写语法 \`\`00:02\` *将它们全部一起直通。这相当于在 Web 界面中选中 \`\`All Functions\`* 复选框。

根据设备和客户机操作系统的不同，可能需要以下一些选项：

- **x-vga\=on\|off** 将 PCI(e) 设备标记为虚拟机的主 GPU。启用此选项后，**vga** 配置选项将被忽略。
- **pcie\=on\|off** 指示 Proxmox VE 使用 PCIe 或 PCI 端口。某些客户机与设备的组合需要 PCIe 而不是 PCI。PCIe 仅适用于 *q35* 机器类型。
- **rombar\=on\|off** 使固件 ROM 对客户机可见。默认为 on。某些 PCI(e) 设备需要禁用此选项。
- **romfile\=\<path\>** 是供设备使用的 ROM 文件的可选路径。这是 **/usr/share/kvm/** 下的相对路径。

**示例**

以下是一个 PCIe 直通示例，其中 GPU 被设置为主 GPU：

```text
# qm set VMID -hostpci0 02:00,pcie=on,x-vga=on
```

**PCI ID 覆盖**

可以覆盖客户机将看到的 PCI 供应商 ID、设备 ID 和子系统 ID。如果设备是某种变体，其 ID 无法被客户机驱动程序识别，但仍希望强制加载这些驱动程序，此功能会很有用（例如，已知设备与受支持的变体使用相同的芯片组）。

可用选项包括 `vendor-id`、`device-id`、`sub-vendor-id` 和 `sub-device-id`。可以设置其中任意一个或全部选项，以覆盖设备的默认 ID。

例如：

```text
# qm set VMID -hostpci0 02:00,device-id=0x10f6,sub-vendor-id=0x0000
```

## 10.9.3. SR-IOV <a href="#_sr_iov" id="_sr_iov"></a>

直通 PCI(e) 设备的另一种方式是使用设备的硬件虚拟化功能（如果可用）。

{% hint style="info" %}
**启用 SR-IOV**

要使用 SR-IOV，平台支持尤为重要。可能需要先在 BIOS/UEFI 中启用此功能，或者需要使用特定的 PCI(e) 端口才能正常工作。如有疑问，请查阅平台手册或联系其供应商。
{% endhint %}

*SR-IOV*（**S**ingle-**R**oot **I**nput/**O**utput **V**irtualization）使单个设备能够向系统提供多个 *VFs*（**V**irtual **F**unctions）。这些 *VFs* 均可用于不同的虚拟机，具有完整的硬件功能，并且与软件虚拟化设备相比，性能更好、延迟更低。

目前，最常见的用例是支持 SR-IOV 的 NIC（**N**etwork **I**nterface **C**ard），每个物理端口可以提供多个 VF。这使虚拟机内部能够使用校验和卸载等功能，从而减少（宿主机）CPU 开销。

### 宿主机配置 <a href="#_host_configuration_2" id="_host_configuration_2"></a>

通常，在设备上启用虚拟功能有两种方法。

- 有时，驱动程序模块会提供一个选项，例如某些 Intel 驱动程序

  ```text
   max_vfs=4
  ```

  可以将其放在一个以 *.conf* 结尾的文件中，该文件位于 **/etc/modprobe.d/**。（之后不要忘记更新 initramfs）

  有关准确的参数和选项，请参阅驱动程序模块文档。
- 第二种更通用的方法是使用 `sysfs`。如果设备和驱动程序支持此方法，可以动态更改 VF 数量。例如，要在设备 0000:01:00.0 上设置 4 个 VF，请执行：

  ```text
  # echo 4 > /sys/bus/pci/devices/0000:01:00.0/sriov_numvfs
  ```

  要使此更改持久化，可以使用 ‘sysfsutils\` Debian 软件包。安装后，可以通过 **/etc/sysfs.conf** 或 \`FILE.conf’ 对其进行配置，后者位于 **/etc/sysfs.d/**。

### 虚拟机配置 <a href="#_vm_configuration" id="_vm_configuration"></a>

创建 VF 后，使用 `lspci` 输出它们时，应该会将它们显示为单独的 PCI(e) 设备。获取其 ID，并像直通 [普通 PCI(e) 设备](#qm_pci_passthrough_vm_config) 一样直通它们。

## 10.9.4. 中介设备（vGPU、GVT-g） <a href="#_mediated_devices_vgpu_gvt_g" id="_mediated_devices_vgpu_gvt_g"></a>

中介设备是另一种将物理硬件的功能和性能复用于虚拟化硬件的方法。它们最常见于虚拟化 GPU 部署，例如 Intel 的 GVT-g，以及 NVIDIA 在其 GRID 技术中使用的 vGPU。

通过这种方式，物理卡可以创建虚拟卡，类似于 SR-IOV。不同之处在于，中介设备不会在宿主机上显示为 PCI(e) 设备，因此仅适用于虚拟机。

### 宿主机配置 <a href="#_host_configuration_3" id="_host_configuration_3"></a>

通常，卡的驱动程序必须支持该功能，否则将无法工作。因此，有关兼容的驱动程序及其配置方法，请咨询供应商。

Intel 的 GVT-g 驱动程序已集成到内核中，应可与第 5、第 6 和第 7 代 Intel Core 处理器以及 E3 v4、E3 v5 和 E3 v6 Xeon 处理器配合使用。

要为 Intel Graphics 启用此功能，必须确保加载 *kvmgt* 模块（例如通过 `/etc/modules-load.d/`），在 [内核命令行](../03-system-administration/13-sysboot.md#sysboot_edit_kernel_cmdline) 上启用它，并添加以下参数：

```text
 i915.enable_gvt=1
```

之后，记得[更新 `initramfs`](#qm_pci_passthrough_update_initramfs)，并重新启动宿主机。

### 虚拟机配置 <a href="#_vm_configuration_2" id="_vm_configuration_2"></a>

要使用中介设备，只需指定 `mdev` 属性，该属性位于 `hostpciX` 虚拟机配置选项中。

可以通过 *sysfs* 获取支持的设备。例如，要列出设备 *0000:00:02.0* 支持的类型，只需执行：

```text
# ls /sys/bus/pci/devices/0000:00:02.0/mdev_supported_types
```

每个条目都是一个目录，其中包含以下重要文件：

- *available\_instances* 包含此类型仍可用的实例数量；虚拟机中每使用一个 *mdev*，该数量就会减少。
- *description* 包含有关该类型功能的简短描述
- *create* 是创建此类设备的端点——如果配置了 *hostpciX* 选项且其中带有 `mdev`，Proxmox VE 会自动为你完成此操作。

使用 `Intel GVT-g vGPU`（`Intel Skylake 6700k`）的示例配置：

```text
# qm set VMID -hostpci0 00:02.0,mdev=i915-GVTg_V5_4
```

设置后，Proxmox VE 会在虚拟机启动时自动创建此类设备，并在虚拟机停止时再次清理它。

## 10.9.5. 在集群中使用 <a href="#_use_in_clusters" id="_use_in_clusters"></a>

还可以在集群级别映射设备，以便设备能够正确用于高可用性、检测硬件更改，并允许非 root 用户配置设备。有关详细信息，请参阅[资源映射](12-resource-mapping.md)。

## 10.9.6. vIOMMU（模拟 IOMMU） <a href="#qm_pci_viommu" id="qm_pci_viommu"></a>

vIOMMU 是在虚拟机内模拟硬件 IOMMU，为虚拟化 I/O 设备提供更好的内存访问控制和安全性。使用 vIOMMU 选项还可以通过[嵌套虚拟化](https://pve.proxmox.com/wiki/Nested_Virtualization)，将 PCI(e) 设备直通到第 1 级虚拟机中的第 2 级虚拟机。要将物理 PCI(e) 设备从宿主机直通到嵌套虚拟机，请遵循 PCI(e) 直通说明。

目前有两种 vIOMMU 实现：Intel 和 VirtIO。

### Intel vIOMMU <a href="#_intel_viommu" id="_intel_viommu"></a>

Intel vIOMMU 对虚拟机的特定要求：

- 无论宿主机使用 Intel 还是 AMD CPU，都必须在虚拟机的内核参数中设置 `intel_iommu=on`。
- 要使用 Intel vIOMMU，需要将 **q35** 设置为机器类型。

如果满足所有要求，可以在需要直通 PCI 设备的虚拟机配置中，将 `viommu=intel` 添加到 machine 参数。

```text
# qm set VMID -machine q35,viommu=intel
```

[VT-d 的 QEMU 文档](https://wiki.qemu.org/Features/VT-d)

### VirtIO vIOMMU <a href="#_virtio_viommu" id="_virtio_viommu"></a>

这种 vIOMMU 实现较新，限制不如 Intel vIOMMU 多，但目前在生产环境中使用较少，文档也较少。

使用 VirtIO vIOMMU 时，**无需**设置任何内核参数。也**不必**使用 q35 作为机器类型，但如果要使用 PCIe，建议这样做。

```text
# qm set VMID -machine q35,viommu=virtio
```

[Michael Zhao 撰写的 virtio-iommu 详解博客文章](https://web.archive.org/web/20230804075844/https://michael2012z.medium.com/virtio-iommu-789369049443)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
