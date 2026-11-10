# 2.1. 系统要求 <a href="#system_requirements" id="system_requirements"></a>

在生产环境运行 Proxmox VE 时，我们建议使用高质量的服务器硬件。为了进一步降低宿主机故障造成的影响，您可以在集群中运行 Proxmox VE，并使用高可用性（HA）虚拟机和容器。

Proxmox VE 可以使用本地存储（DAS）、SAN、NAS 以及 Ceph RBD 等分布式存储。详情请参阅[存储章节](../07-storage/README.md)。

## 2.1.1. 评估用途的最低要求 <a href="#install_minimal_requirements" id="install_minimal_requirements"></a>

这些最低要求仅用于评估目的，不应在生产环境中使用。

- CPU：64 位 x86（Intel 64 或 AMD64）。或者，配备 ARMv8-A 或更新 CPU 的 64 位 ARM（arm64、aarch64），请参阅[64 位 ARM（arm64）支持](#install_arm64_support)。
- 对于 x86 宿主机，需要支持 Intel VT 或 AMD-V 的 CPU 和主板，以支持 KVM 完全虚拟化。在受支持的 arm64 平台上，KVM 硬件辅助虚拟化不需要同等的 CPU 标志。
- 内存：1 GB 内存，另加客户机所需的额外内存
- 硬盘
- 一块网卡（NIC）

## 2.1.2. 推荐的系统要求 <a href="#install_recommended_requirements" id="install_recommended_requirements"></a>

- Intel 64 或 AMD64，并带有 Intel VT 或 AMD-V CPU 标志。或者，配备 ARMv9-A 或更新 CPU 的 64 位 ARM 宿主机，请参阅[64 位 ARM（arm64）支持](#install_arm64_support)。
- 内存：操作系统和 Proxmox VE 服务至少需要 2 GB，另加为客户机分配的内存。对于 Ceph 和 ZFS，还需要额外内存；每 TB 已用存储空间约需 1GB 内存。
- 快速且冗余的存储，使用 SSD 可获得最佳效果。
- 操作系统存储：使用带电池保护写缓存（“BBU”）的硬件 RAID，或使用非 RAID 配置搭配 ZFS（可选配用于 ZIL 的 SSD）。
- 虚拟机存储：

  - 对于本地存储，可使用带电池备份写缓存（BBU）的硬件 RAID，或为 ZFS 和 Ceph 使用非 RAID 配置。ZFS 和 Ceph 均不兼容硬件 RAID 控制器。
  - 可以使用共享和分布式存储。
  - 建议使用具有掉电保护（PLP）的 SSD 以获得良好性能。不建议使用消费级 SSD。
- 冗余的（多）Gbit 网卡，并根据所选的存储技术和集群设置配备额外网卡。
- 对于 PCI(e) 直通，CPU 和主板需要支持输入/输出内存管理单元（IOMMU）：x86 上的 Intel VT-d 或 AMD-Vi，或 arm64 上的系统内存管理单元（SMMU）。

{% hint style="success" %}
通常还需要在 BIOS/UEFI 中启用 IOMMU。详情请参阅[PCI(e) 直通](../10-virtual-machines/09-qm-pci-passthrough.md)章节。
{% endhint %}

## 2.1.3. 64 位 ARM（arm64）支持 <a href="#install_arm64_support" id="install_arm64_support"></a>

Proxmox VE 在 NVIDIA Grace Hopper 和 NVIDIA Vera 平台上支持原生 64 位 ARM（arm64、aarch64）。对于其他基于 UEFI 的 ARMv9-A 或更新硬件，仅提供尽力而为的支持。不支持仅使用设备树的单板计算机，例如 Raspberry Pi。

arm64 宿主机必须通过 UEFI 启动，并通过 ACPI（高级配置和电源接口）描述其硬件。Proxmox VE 不支持 arm64 上仅使用设备树或传统 BIOS 启动。

以下几项 x86 特有功能在 arm64 上不可用：

- 虚拟机无法使用 SeaBIOS。在 arm64 上，客户机始终通过 UEFI 启动，该 UEFI 由 OVMF 的 ARM 构建版本提供，也称为 AAVMF。
- AMD SEV（安全加密虚拟化）内存加密和 Intel 的 GVT-g 中介型 vGPU 仅支持 x86。
- 与 x86 上的 `intel-microcode` 和 `amd64-microcode` 不同，这里没有操作系统级的 CPU 微码软件包。

一个集群可以同时包含 x86 和 arm64 节点，但运行中的客户机不能在不同架构的节点之间移动：

- 在线迁移只能在相同架构的节点之间进行，因为运行中客户机的 CPU 状态无法跨架构传输。
- 无论是虚拟机还是容器，客户机都只能在与该客户机架构匹配的节点上运行。离线迁移、备份和恢复或共享存储可以将客户机的数据移动到不同架构的节点，但客户机仍需针对该架构重新安装或重新配置后才能启动。

## 2.1.4. 简单性能概览 <a href="#simple_performance_overview" id="simple_performance_overview"></a>

要概览已安装 Proxmox VE 系统的 CPU 和硬盘性能，请运行随附的 `pveperf` 工具。

{% hint style="info" %}
这只是一个非常快速且笼统的基准测试。建议进行更详细的测试，尤其是针对系统 I/O 性能的测试。
{% endhint %}

## 2.1.5. 访问 Web 界面支持的浏览器 <a href="#supported_web_browsers_for_accessing_the_web_interface" id="supported_web_browsers_for_accessing_the_web_interface"></a>

要访问基于 Web 的用户界面，我们建议使用以下浏览器之一：

- Firefox，当年发布的版本，或最新的延长支持版本
- Chrome，当年发布的版本
- Microsoft 当前支持的 Edge 版本
- Safari，当年发布的版本

从移动设备访问时，Proxmox VE 会显示基于触摸操作的轻量级界面。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
