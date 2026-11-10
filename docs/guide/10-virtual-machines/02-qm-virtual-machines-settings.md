# 10.2. 虚拟机设置 <a href="#qm_virtual_machines_settings" id="qm_virtual_machines_settings"></a>

一般来说，Proxmox VE 会尝试为虚拟机（VM）选择合理的默认设置。请确保理解所更改设置的含义，因为这可能会导致性能下降，或使数据面临风险。

## 10.2.1. 常规设置 <a href="#qm_general_settings" id="qm_general_settings"></a>

[![screenshot/gui-create-vm-general.png](../../assets/screenshot-gui-create-vm-general-png-60617f9d68b1.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-general.png)

虚拟机的常规设置包括

- **节点**：虚拟机将运行的物理服务器
- **VM ID**：此 Proxmox VE 安装中用于标识虚拟机的唯一编号
- **名称**：可用于描述虚拟机的自由格式文本字符串
- **资源池**：虚拟机的逻辑分组

## 10.2.2. 操作系统设置 <a href="#qm_os_settings" id="qm_os_settings"></a>

[![screenshot/gui-create-vm-os.png](../../assets/screenshot-gui-create-vm-os-png-2f840c53a6ca.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-os.png)

创建虚拟机（VM）时，设置正确的操作系统（OS）可让 Proxmox VE 优化某些底层参数。例如，Windows 操作系统期望 BIOS 时钟使用本地时间，而基于 Unix 的操作系统期望 BIOS 时钟使用 UTC 时间。

## 10.2.3. 系统设置 <a href="#qm_system_settings" id="qm_system_settings"></a>

创建虚拟机时，可以更改新虚拟机的一些基本系统组件。可以指定要使用的[显示类型](#qm_display)。

[![screenshot/gui-create-vm-system.png](../../assets/screenshot-gui-create-vm-system-png-511b121389af.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-system.png)

此外，还可以更改[SCSI 控制器](#qm_hard_disk)。如果计划安装 QEMU Guest Agent，或者所选 ISO 镜像已附带并自动安装该代理，则可能需要勾选*QEMU Agent*复选框，这样 Proxmox VE 就知道可以使用其功能来显示更多信息，并更智能地完成某些操作（例如关机或快照）。

Proxmox VE 允许使用不同的固件和机器类型启动虚拟机，即[SeaBIOS 和 OVMF](#qm_bios_and_uefi)。在大多数情况下，只有计划使用[PCIe 直通](09-qm-pci-passthrough.md)时，才需要将默认的 SeaBIOS 切换为 OVMF。在 arm64 宿主机上，OVMF 是默认且唯一的选项，因为 SeaBIOS 仅支持 x86。

### 机器类型 <a href="#qm_machine_type" id="qm_machine_type"></a>

虚拟机的*机器类型*定义了虚拟机虚拟主板的硬件布局。可以在默认的[Intel 440FX](https://en.wikipedia.org/wiki/Intel_440FX)或[Q35](https://ark.intel.com/content/www/us/en/ark/products/31918/intel-82q35-graphics-and-memory-controller.html)芯片组之间进行选择，后者还提供虚拟 PCIe 总线，因此如果需要直通 PCIe 硬件，可能需要选择后者。此外，还可以选择[vIOMMU](09-qm-pci-passthrough.md#qm_pci_viommu)实现。

{% hint style="info" %}
Intel 440FX 和 Q35 芯片组专用于 x86 客户机。在 arm64 宿主机上，虚拟机使用`virt`机器类型，该类型模拟一种通用的、基于 UEFI 的 ARM 机器。
{% endhint %}

#### 机器版本 <a href="#_machine_version" id="_machine_version"></a>

每种机器类型在 QEMU 中都有版本，并且给定的 QEMU 二进制文件支持多种机器版本。新版本可能带来对新功能的支持、修复或一般性改进。但是，它们也会更改虚拟硬件的属性。为避免从客户机角度来看发生突然变化，并确保虚拟机状态、在线迁移和包含 RAM 的快照的兼容性，新的 QEMU 实例将继续使用相同的机器版本。

对于 Windows 客户机，机器版本会在创建时固定，因为 Windows 对虚拟硬件的更改很敏感，即使是在冷启动之间也是如此。例如，不同的机器版本可能会导致网络设备的枚举不同。Linux 等其他操作系统通常可以很好地应对此类更改。对于这些操作系统，默认使用*最新*机器版本。这意味着在全新启动后，将使用 QEMU 二进制文件支持的最新机器版本（例如，QEMU 8.1 支持的每种机器类型的最新机器版本均为 8.1 版）。

在实现会更改硬件布局的新功能或修复时，机器版本还用作确保向后兼容的保障措施。对于正在运行的虚拟机上的操作（例如在线迁移），会保存正在运行的机器版本，以确保虚拟机能够完全按原样恢复，这不仅涉及 QEMU 虚拟化层面，还涉及 Proxmox VE 创建 QEMU 虚拟机实例的方式。

**PVE 机器修订版本**

有时，Proxmox VE 需要更改硬件布局或修改选项，而不能等待新的 QEMU 版本发布。为此，Proxmox VE 以`+pveX`的形式添加了额外的下游修订版本。在这些修订版本中，每个新 QEMU 机器版本的`X`均为 0，并且在这种情况下会省略，例如机器版本`pc-q35-9.2`与机器版本`pc-q35-9.2+pve0`相同。

如果 Proxmox VE 需要更改硬件布局或默认选项，则会递增修订版本，并将其用于新创建的客户机，或在始终使用最新机器版本的虚拟机重启时使用。

#### QEMU 机器版本弃用 <a href="#_qemu_machine_version_deprecation" id="_qemu_machine_version_deprecation"></a>

从 QEMU 10.1 开始，机器版本在上游 QEMU 中保留 6 年后会被移除。Proxmox VE 大约每 2 年发布一个主要版本，因此一个 Proxmox VE 主要版本将支持来自大约前两个 Proxmox VE 主要版本的机器版本。

在升级到新的 Proxmox VE 主要版本之前，应更新虚拟机配置，避免使用将在下一个 Proxmox VE 主要版本中移除的所有机器版本。这可确保客户机在该版本的整个生命周期内仍可使用。请参阅[更新到较新的机器版本](#qm_machine_update)一节。

移除策略尚未在 Proxmox VE 8 中生效，因此受支持机器版本的基线为 2.4。为 Proxmox VE 9 发布的最后一个 QEMU 二进制版本预计将是 QEMU 11.2。此 QEMU 二进制文件将移除对低于 6.0 的机器版本的支持，因此 6.0 是 Proxmox VE 9 发布生命周期的基线。预计每次 Proxmox VE 主版本发布时，基线都会提高两个主版本，例如 Proxmox VE 10 的基线为 8.0。

#### 更新到较新的机器版本 <a href="#qm_machine_update" id="qm_machine_update"></a>

如果看到弃用警告，应将机器版本更改为较新的版本。请务必先准备好可用的备份，并做好客户机识别硬件的方式可能发生变化的准备。在某些情况下，可能需要重新安装特定驱动程序。还应检查使用这些机器版本创建的含内存快照（即 `runningmachine` 配置项）。遗憾的是，无法更改快照的机器版本，因此需要加载该快照以挽救其中的任何数据。

## 10.2.4. 硬盘 <a href="#qm_hard_disk" id="qm_hard_disk"></a>

### 总线/控制器 <a href="#qm_hard_disk_bus" id="qm_hard_disk_bus"></a>

QEMU 可以模拟多种存储控制器：

{% hint style="success" %}
出于性能考虑，并且由于它们得到了更好的维护，强烈建议使用 **VirtIO SCSI** 或 **VirtIO Block** 控制器。
{% endhint %}

- **IDE** 控制器的设计可追溯至 1984 年的 PC/AT 磁盘控制器。尽管这种控制器已被较新的设计所取代，但您能想到的每一种操作系统都支持它，因此，如果要运行 2003 年之前发布的操作系统，它是一个很好的选择。此控制器最多可连接 4 个设备。
- **SATA**（Serial ATA）控制器诞生于 2003 年，采用更现代的设计，可实现更高的吞吐量并连接更多设备。此控制器最多可连接 6 个设备。
- **SCSI** 控制器设计于 1985 年，常见于服务器级硬件，最多可连接 14 个存储设备。Proxmox VE 默认模拟 LSI 53C895A 控制器。

  如果追求性能，建议使用类型为 *VirtIO SCSI single* 的 SCSI 控制器，并为连接的磁盘启用 [IO Thread](#qm_hard_disk_iothread) 设置。自 Proxmox VE 7.3 起，这是新创建 Linux VM 的默认配置。每个磁盘都有自己的 *VirtIO SCSI* 控制器，QEMU 将在专用线程中处理磁盘 I/O。Linux 发行版自 2012 年起支持此控制器，FreeBSD 自 2014 年起支持此控制器。对于 Windows 操作系统，需要在安装过程中提供包含驱动程序的额外 ISO。
- **VirtIO Block** 控制器通常简称为 VirtIO 或 virtio-blk，是一种较旧的半虚拟化控制器。在功能方面，它已被 VirtIO SCSI 控制器取代。

### 镜像格式 <a href="#qm_hard_disk_formats" id="qm_hard_disk_formats"></a>

每个控制器上都连接有若干模拟硬盘，这些硬盘由所配置存储中的文件或块设备提供后端支持。存储类型的选择将决定硬盘镜像的格式。提供块设备的存储（LVM、ZFS、Ceph）需要使用 **raw disk image format**，而基于文件的存储（如 Ext4、XFS、NFS 或 CIFS）则允许选择 **raw disk image format** 或 **QEMU image format**。

- **QEMU image format** 是一种写时复制格式，支持快照和磁盘镜像的精简置备。
- **raw disk image** 是硬盘的逐位镜像，类似于在 Linux 中对块设备执行 `dd` 命令所得到的结果。此格式本身不支持精简置备或快照，这些功能需要存储层配合实现。不过，它的速度可能比 **QEMU image format** 快最多 10%。[\[1\]](#note-0fea3830-1)
- 只有打算将磁盘镜像导入或导出到其他虚拟机管理程序时，**VMware image format** 才有意义。

### 缓存模式 <a href="#qm_hard_disk_cache" id="qm_hard_disk_cache"></a>

设置硬盘的 **Cache** 模式会影响宿主机系统如何向客户机系统通知块写入完成。默认的 **No cache** 表示当每个块到达物理存储写入队列时，客户机系统就会收到写入完成通知，并忽略宿主机页缓存。这在安全性和速度之间提供了良好的平衡。

如果希望 Proxmox VE 备份管理器在备份 VM 时跳过某个磁盘，可以在该磁盘上设置 **No backup** 选项。

如果希望 Proxmox VE 存储复制机制在启动复制任务时跳过某个磁盘，可以在该磁盘上设置 **Skip replication** 选项。自 Proxmox VE 5.0 起，复制要求磁盘镜像位于类型为 `zfspool` 的存储上，因此，当 VM 配置了复制时，如果将磁盘镜像添加到其他存储，则必须跳过此磁盘镜像的复制。

### Trim/Discard <a href="#qm_hard_disk_discard" id="qm_hard_disk_discard"></a>

If your storage supports *thin provisioning* (see the storage chapter in the Proxmox VE guide), you can activate the **Discard** option on a drive. With **Discard** set and a *TRIM*-enabled guest OS [\[2\]](#note-0fea3830-2), when the VM’s filesystem marks blocks as unused after deleting files, the controller will relay this information to the storage, which will then shrink the disk image accordingly. For the guest to be able to issue *TRIM* commands, you must enable the **Discard** option on the drive. Some guest operating systems may also require the **SSD Emulation** flag to be set. Note that **Discard** on **VirtIO Block** drives is only supported on guests using Linux Kernel 5.0 or higher.

If you would like a drive to be presented to the guest as a solid-state drive rather than a rotational hard disk, you can set the **SSD emulation** option on that drive. There is no requirement that the underlying storage actually be backed by SSDs; this feature can be used with physical media of any type. Note that **SSD emulation** is not supported on **VirtIO Block** drives.

### IO Thread <a href="#qm_hard_disk_iothread" id="qm_hard_disk_iothread"></a>

**IO thread** 选项只能用于采用以下总线/设备控制器之一的磁盘：

- **SCSI**，前提是模拟的 SCSI 控制器类型为 **VirtIO SCSI single**；或
- **VirtIO Block**

启用 **IO thread** 后，QEMU 会为每个存储控制器创建一个 I/O 线程，而不是在主事件循环或 vCPU 线程中处理所有 I/O。其好处之一是能够更好地分配工作并利用底层存储。另一个好处是，当宿主机工作负载的 I/O 非常密集时，可降低客户机中的延迟（卡顿），因为主线程和 vCPU 线程都不会被磁盘 I/O 阻塞。

## 10.2.5. CPU <a href="#qm_cpu" id="qm_cpu"></a>

[![screenshot/gui-create-vm-cpu.png](../../assets/screenshot-gui-create-vm-cpu-png-cf8772d20d7e.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-cpu.png)

**CPU socket** 是 PC 主板上用于插入 CPU 的物理插槽。该 CPU 可以包含一个或多个 **cores**，它们是独立的处理单元。从性能角度看，使用一个 4 核 CPU 插槽还是两个双核 CPU 插槽基本没有区别。但是，某些软件许可证取决于机器拥有的插槽数量，在这种情况下，将插槽数量设置为许可证允许的数量是合理的。

增加虚拟 CPU（核心和插槽）的数量通常会提升性能，但这在很大程度上取决于 VM 的用途。多线程应用程序当然会从大量虚拟 CPU 中受益，因为每添加一个虚拟 CPU，QEMU 都会在宿主机系统上创建一个新的执行线程。如果不确定 VM 的工作负载，将 **Total cores** 的数量设置为 2 通常比较稳妥。

{% hint style="info" %}
所有 VM 的核心*总数*大于服务器上的核心数量是完全安全的（例如，在只有 8 个核心的机器上运行 4 个各有 4 个核心的 VM，总计 16 个核心）。在这种情况下，宿主机系统会在服务器核心之间平衡 QEMU 执行线程，就像运行标准的多线程应用程序一样。但是，Proxmox VE 会阻止您启动虚拟 CPU 核心数超过物理可用核心数的 VM，因为这只会因上下文切换的开销而降低性能。
{% endhint %}

### 资源限制 <a href="#qm_cpu_resource_limits" id="qm_cpu_resource_limits"></a>

**cpulimit**

除了虚拟核心数量外，还可以使用 **cpulimit** 选项设置 VM 可用的“宿主机 CPU 时间”总量。它是一个浮点值，以百分比表示 CPU 时间，因此 `1.0` 等于 `100%`，`2.5` 等于 `250%`，依此类推。如果单个进程完全占用一个核心，其 CPU 时间使用率将为 `100%`。如果一个四核 VM 完全利用其所有核心，理论上将使用 `400%`。实际使用率可能还会稍高一些，因为除了 vCPU 核心线程之外，QEMU 还可以为 VM 外围设备运行额外的线程。

当 VM 因并行运行某些进程而需要多个 vCPU，但又不希望整个 VM 能够同时以 100% 的利用率运行所有 vCPU 时，此设置会很有用。

例如，假设有一台虚拟机可从 8 个虚拟 CPU 中受益，但您不希望该 VM 能够让所有 8 个核心都满载运行，因为这会使服务器过载，导致其他虚拟机和容器获得的 CPU 时间过少。要解决此问题，可以将 **cpulimit** 设置为 `4.0`（\=400%）。这意味着，如果 VM 通过同时运行 8 个进程来充分利用所有 8 个虚拟 CPU，则每个 vCPU 最多能从物理核心获得 50% 的 CPU 时间。但是，如果 VM 工作负载仅充分利用 4 个虚拟 CPU，则每个虚拟 CPU 仍可从物理核心获得最多 100% 的 CPU 时间，总计为 400%。

{% hint style="info" %}
根据配置，VM 可以使用额外的线程，例如用于网络或 I/O 操作的线程，以及用于在线迁移的线程。因此，VM 显示的 CPU 时间用量可能超过其虚拟 CPU 本身所能使用的量。要确保 VM 使用的 CPU 时间永远不会超过所分配的 vCPU 可使用的量，请将 **cpulimit** 设置为与核心总数相同的值。
{% endhint %}

**cpuunits**

通过 **cpuunits** 选项（如今通常称为 CPU 份额或 CPU 权重），可以控制 VM 与其他正在运行的 VM 相比能获得多少 CPU 时间。它是一个相对权重，默认值为 `100`（如果宿主机使用旧版 cgroup v1，则为 `1024`）。如果提高某个 VM 的此值，与权重较低的其他 VM 相比，调度器会优先调度该 VM。

例如，如果 VM 100 使用默认值 `100`，而 VM 200 被更改为 `200`，则后一个 VM 200 获得的 CPU 带宽将是前一个 VM 100 的两倍。

有关更多信息，请参阅 `man systemd.resource-control`，其中 `CPUQuota` 对应于 `cpulimit`，`CPUWeight` 对应于我们的 `cpuunits` 设置。请访问其 Notes 部分，查看参考资料和实现细节。

**affinity**

通过 **affinity** 选项，可以指定用于运行 VM vCPU 的物理 CPU 核心。I/O 等外围 VM 进程不受此设置影响。请注意，**CPU 亲和性不是一项安全功能**。

强制设置 CPU **affinity** 在某些情况下可能很有意义，但也会增加复杂性和维护工作量。例如，以后需要添加更多 VM，或将 VM 迁移到 CPU 核心数较少的节点时。如果某些 CPU 已得到充分利用，而其他 CPU 几乎处于空闲状态，还很容易造成 CPU 使用不均衡，进而导致系统性能受限。

**affinity** 通过 `taskset` CLI 工具设置。它接受宿主机 CPU 编号（参见 `lscpu`），采用 `List Format`，该格式见 `man cpuset`。这个 ASCII 十进制列表既可以包含数字，也可以包含数字范围。例如，**affinity** `0-1,8-11`（展开后为 `0, 1, 8, 9, 10, 11`）将允许 VM 仅在这六个特定的宿主机核心上运行。

### CPU 类型 <a href="#_cpu_type" id="_cpu_type"></a>

QEMU 可以模拟多种不同的 **CPU 类型**，从 486 到最新的 Xeon 处理器。每一代新处理器都会增加新功能，例如硬件辅助 3D 渲染、随机数生成、内存保护等。此外，当前一代处理器还可以通过 [微代码更新](../03-system-administration/03-chapter-firmware-updates.md) 进行升级，以修复缺陷或安全问题。

通常，应为 VM 选择与宿主机系统 CPU 尽量接近的处理器类型，这样宿主机 CPU 功能（也称为 *CPU 标志*）将在 VM 中可用。如果需要完全匹配，可以将 CPU 类型设置为 **host**，此时 VM 将具有与宿主机系统完全相同的 CPU 标志。

不过，这有一个缺点。如果要在不同宿主机之间在线迁移 VM，VM 最终可能会运行在一个 CPU 类型或微代码版本不同的新系统上。如果传递给客户机的 CPU 标志缺失，QEMU 进程将停止。为解决这一问题，QEMU 还提供了自己的虚拟 CPU 类型，Proxmox VE 默认使用这些类型。

后端默认值为 *kvm64*，它基本上适用于所有 x86\_64 宿主机 CPU；而在 UI 中创建新 VM 时，默认值为 *x86-64-v2-AES*，后者要求 Intel 宿主机 CPU 至少为 Westmere，AMD 宿主机 CPU 至少为第四代 Opteron。

{% hint style="info" %}
这里介绍的 *kvm64* 和 *x86-64-v\** CPU 模型仅适用于 x86。在 arm64 宿主机上，客户机使用 ARM CPU 模型：*host* 用于暴露物理 CPU（在受支持的硬件上建议使用），或使用 *max* 等通用模型，并搭配 `virt` 机器类型。
{% endhint %}

简而言之：

如果不关心在线迁移，或者集群是同构的，即所有节点都具有相同的 CPU 和相同的微代码版本，请将 CPU 类型设置为 host，因为理论上这将使客户机获得最大性能。

如果关心在线迁移和安全性，并且只有 Intel CPU 或只有 AMD CPU，请选择集群中最低代次的 CPU 模型。

如果关心在线迁移但不关心安全性，或者集群混用了 Intel/AMD CPU，请选择兼容的最低级别 QEMU 虚拟 CPU 类型。

{% hint style="info" %}
Intel 和 AMD 宿主机 CPU 之间的在线迁移不保证能够正常工作。
{% endhint %}

另请参阅 [QEMU 中定义的 AMD 和 Intel CPU 类型列表](../26-qemu-vcpu-list/01-chapter-qm-vcpu-list.md)。

### QEMU CPU 类型 <a href="#_qemu_cpu_types" id="_qemu_cpu_types"></a>

QEMU 还提供与 Intel 和 AMD 宿主机 CPU 均兼容的虚拟 CPU 类型。

{% hint style="info" %}
为了缓解虚拟 CPU 类型的 Spectre 漏洞，需要添加相关的 CPU 标志，请参阅 [与 Meltdown / Spectre 相关的 CPU 标志](#qm_meltdown_spectre)。
{% endhint %}

历史上，Proxmox VE 使用 *kvm64* CPU 模型，其启用的 CPU 标志处于 Pentium 4 水平，因此对于某些工作负载，性能并不理想。

2020 年夏，AMD、Intel、Red Hat 和 SUSE 合作在 x86-64 基线之上定义了三个 x86-64 微架构级别，并启用了现代标志。详情请参阅 [x86-64-ABI 规范](https://gitlab.com/x86-psABIs/x86-64-ABI)。

{% hint style="info" %}
一些较新的发行版（如 CentOS 9）现在构建时将 *x86-64-v2* 标志作为最低要求。
{% endhint %}

- *kvm64 (x86-64-v1)*：兼容 Intel CPU \>\= Pentium 4、AMD CPU \>\= Phenom。
- *x86-64-v2*：兼容 Intel CPU \>\= Nehalem、AMD CPU \>\= Opteron\_G3。与 *x86-64-v1* 相比，新增的 CPU 标志：*\+cx16*、*\+lahf-lm*、*\+popcnt*、*\+pni*、*\+sse4.1*、*\+sse4.2*、*\+ssse3*。
- *x86-64-v2-AES*：兼容 Intel CPU \>\= Westmere、AMD CPU \>\= Opteron\_G4。与 *x86-64-v2* 相比，新增的 CPU 标志：*\+aes*。
- *x86-64-v3*：兼容 Intel CPU \>\= Haswell、AMD CPU \>\= EPYC。与 *x86-64-v2-AES* 相比，新增的 CPU 标志：*\+avx*、*\+avx2*、*\+bmi1*、*\+bmi2*、*\+f16c*、*\+fma*、*\+movbe*、*\+xsave*。
- *x86-64-v4*：兼容 Intel CPU \>\= Skylake、AMD CPU \>\= EPYC v4 Genoa。与 *x86-64-v3* 相比，新增的 CPU 标志：*\+avx512f*、*\+avx512bw*、*\+avx512cd*、*\+avx512dq*、*\+avx512vl*。

### 自定义 CPU 类型 <a href="#_custom_cpu_types" id="_custom_cpu_types"></a>

可以定义自定义 CPU 类型，配置其基础模型、厂商、物理地址位数以及各标志的开关，然后像内置类型一样将其分配给 VM。在 VM 配置中，自定义类型以 `custom-<name>` 的形式引用。

在 Web UI 中的 `Datacenter -> Custom CPU Models` 下管理这些类型。模型对话框内嵌一个标志编辑器网格，支持按标志名称和描述进行自由文本搜索，提供加速器（kvm/tcg）选择器，并提供按节点选择的多选框；该多选框会突出显示每个所选集群节点当前报告为受支持的标志，有助于在确定模型之前，识别哪些标志在目标宿主机上实际可用。同一网格还用于每个 VM 的 `Processor` 编辑对话框，但在该对话框中仅限显示可为单个 VM 设置的标志；如果配置的标志不被 API 识别或不受所选加速器支持，则会在顶部显示警告。

自定义 CPU 类型仍由配置文件 `/etc/pve/virtual-guest/cpu-models.conf` 提供支持，也可以通过 CLI 维护，格式请参阅 `man cpu-models.conf`。

对自定义模型的访问通过 ACL 路径 `/mapping/cpu/<name>` 按模型分别控制。`Mapping.Audit` 允许用户在列表中查看模型，`Mapping.Modify` 控制是否可在面板中创建、更新和删除模型，`Mapping.Use` 则是将模型分配给 VM 所必需的权限。后者会在创建 VM、更新 VM 和克隆 VM 时强制执行，因此，即使用户可以克隆使用自定义模型的 VM，仍需要在该模型的 ACL 路径上拥有 `Mapping.Use` 权限。

### 与 Meltdown / Spectre 相关的 CPU 标志 <a href="#qm_meltdown_spectre" id="qm_meltdown_spectre"></a>

有多个与 Meltdown 和 Spectre 漏洞相关的 CPU 标志 [\[3\]](#note-0fea3830-3)，除非为 VM 选择的 CPU 类型默认已启用这些标志，否则需要手动设置。

要使用这些 CPU 标志，必须满足以下两个要求：

- 宿主机 CPU 必须支持该功能，并将其传递给客户机的虚拟 CPU
- 客户机操作系统必须更新到能够缓解这些攻击并能够利用该 CPU 功能的版本

否则，需要设置虚拟 CPU 所需的 CPU 标志，即设置 *flags* 属性（VM 配置文件中 *cpu* 选项的属性），或者在 Web UI 中编辑 CPU 选项。

对于 Spectre v1、v2、v4 修复，CPU 或系统厂商还需要为 CPU 提供所谓的“微代码更新”，请参阅 [固件更新一章](../03-system-administration/03-chapter-firmware-updates.md)。请注意，并非所有受影响的 CPU 都可以通过更新来支持 spec-ctrl。

要检查 Proxmox VE 宿主机是否存在漏洞，请以 root 身份执行以下命令：

```text
for f in /sys/devices/system/cpu/vulnerabilities/*; do echo "${f##*/} -" $(cat "$f"); done
```

还有一个社区脚本可用于检测宿主机是否仍存在漏洞。[\[4\]](#note-0fea3830-4)

### Intel 处理器 <a href="#_intel_processors" id="_intel_processors"></a>

- *pcid*

  这可降低称为 *内核页表隔离（KPTI）* 的 Meltdown（CVE-2017-5754）缓解措施对性能的影响；KPTI 可有效地向用户空间隐藏内核内存。如果没有 PCID，KPTI 是一种开销相当大的机制 [\[5\]](#note-0fea3830-5)。

  要检查 Proxmox VE 宿主机是否支持 PCID，请以 root 身份执行以下命令：

  ```text
  # grep ' pcid ' /proc/cpuinfo
  ```

  如果返回结果不为空，则表示宿主机的 CPU 支持 *pcid*。
- *spec-ctrl*

  在 retpoline 不足以解决问题的情况下，需要此标志来启用 Spectre v1（CVE-2017-5753）和 Spectre v2（CVE-2017-5715）修复。默认包含在带有 -IBRS 后缀的 Intel CPU 模型中。对于不带 -IBRS 后缀的 Intel CPU 模型，必须显式启用。需要更新宿主机 CPU 微代码（intel-microcode \>\= 20180425）。
- *ssbd*

  需要此标志来启用 Spectre V4（CVE-2018-3639）修复。默认不包含在任何 Intel CPU 模型中。对于所有 Intel CPU 模型，都必须显式启用。需要更新宿主机 CPU 微代码（intel-microcode \>\= 20180703）。

### AMD 处理器 <a href="#_amd_processors" id="_amd_processors"></a>

- *ibpb*

  在 retpoline 不足以解决问题的情况下，需要此标志来启用 Spectre v1（CVE-2017-5753）和 Spectre v2（CVE-2017-5715）修复。默认包含在带有 -IBPB 后缀的 AMD CPU 模型中。对于不带 -IBPB 后缀的 AMD CPU 模型，必须显式启用。宿主机 CPU 微代码必须先支持此功能，才能将其用于客户机 CPU。
- *virt-ssbd*

  需要此标志来启用 Spectre v4（CVE-2018-3639）修复。默认不包含在任何 AMD CPU 模型中。对于所有 AMD CPU 模型，都必须显式启用。即使也提供了 amd-ssbd，也应向客户机提供此标志，以最大限度地提高客户机兼容性。请注意，使用 "host" CPU 模型时必须显式启用此标志，因为这是一项物理 CPU 中不存在的虚拟功能。
- *amd-ssbd*

  需要此标志来启用 Spectre v4（CVE-2018-3639）修复。默认不包含在任何 AMD CPU 模型中。对于所有 AMD CPU 模型，都必须显式启用。此标志提供比 virt-ssbd 更高的性能，因此，如果可能，支持此功能的宿主机应始终将其暴露给客户机。尽管如此，仍应同时暴露 virt-ssbd，以最大限度地提高客户机兼容性，因为某些内核只识别 virt-ssbd。
- *amd-no-ssb*

  建议用于指示宿主机不受 Spectre V4（CVE-2018-3639）影响。默认不包含在任何 AMD CPU 模型中。未来的 CPU 硬件代次将不受 CVE-2018-3639 影响，因此应通过暴露 amd-no-ssb 告知客户机不要启用其缓解措施。此标志与 virt-ssbd 和 amd-ssbd 互斥。

### 与 Windows 相关的 CPU 设置 <a href="#qm_cpu_windows_tweaks" id="qm_cpu_windows_tweaks"></a>

一些 CPU 默认设置和属性专门针对近期 Intel 硬件上的 Windows 客户机进行了调整：

- 对于 Windows 11 机器类型，默认禁用 `cet-ibt` 和 `cet-ss`（控制流强制技术：间接分支跟踪和影子栈），因为目前它们会导致启用了基于虚拟化的安全性的 Windows 客户机无法启动。对于明确依赖这些标志的工作负载，可以通过 `Processor` 标志编辑器按 VM 重新启用它们。
- The QEMU `level` CPU property is exposed so it can be set per VM (or in a custom CPU model) without resorting to custom `args`. Setting `level=30` is a known workaround for Hyper-V boot failures of Windows guests on recent Intel hosts when the CPU type is `host` or `max`. The property only applies for x86\_64 vCPUs; it is silently ignored on other architectures.

### NUMA <a href="#_numa" id="_numa"></a>

您还可以选择在虚拟机中模拟 **NUMA** [\[6\]](#note-0fea3830-6) 架构。NUMA 架构的基本原理是，内存不再是可供所有核心使用的全局内存池，而是分布在靠近各个插槽的本地内存组中。这可以带来速度提升，因为内存总线不再是瓶颈。如果您的系统采用 NUMA 架构 [\[7\]](#note-0fea3830-7)，我们建议启用此选项，因为这将允许在宿主机系统上合理分配虚拟机资源。在虚拟机中热插拔核心或 RAM 也需要此选项。

如果使用 NUMA 选项，建议将插槽数设置为宿主机系统的节点数。

### vCPU 热插拔 <a href="#_vcpu_hot_plug" id="_vcpu_hot_plug"></a>

现代操作系统引入了在运行中的系统中热插拔 CPU 的能力，并在一定程度上支持热拔除 CPU。虚拟化使我们能够避免真实硬件在此类场景中可能造成的许多（物理）问题。不过，这仍是一项相当新且复杂的功能，因此应仅在绝对必要时使用。大多数功能都可以通过其他经过充分测试且不那么复杂的功能来实现，请参阅 [资源限制](#qm_cpu_resource_limits)。

在 Proxmox VE 中，可插入的 CPU 最大数量始终为 `cores * sockets`。若要在启动虚拟机时使用少于该总核心数的 CPU，可以使用 **vcpus** 设置，它表示虚拟机启动时应插入多少个 vCPU。

目前，此功能仅在 Linux 上受支持，需要高于 3.10 版本的内核，建议使用高于 4.7 版本的内核。

您可以使用如下 udev 规则，自动将客户机中的新 CPU 设置为在线状态：

```text
SUBSYSTEM=="cpu", ACTION=="add", TEST=="online", ATTR{online}=="0", ATTR{online}="1"
```

Save this under /etc/udev/rules.d/ as a file ending in `.rules`.

注意：CPU 热移除取决于机器类型，并且需要客户机配合。删除命令并不保证 CPU 移除会实际发生；通常，它只是通过目标相关机制（例如 x86/amd64 上的 ACPI）转发给客户机操作系统的请求。

## 10.2.6. 内存 <a href="#qm_memory" id="qm_memory"></a>

对于每台虚拟机，您可以选择设置固定大小的内存，也可以让 Proxmox VE 根据宿主机的当前 RAM 使用情况动态分配内存。

[![screenshot/gui-create-vm-memory.png](../../assets/screenshot-gui-create-vm-memory-png-3dded0eeb67d.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-memory.png)

**固定内存分配**

当将内存和最小内存设置为相同数值时，Proxmox VE 将直接按照您指定的数量为虚拟机分配内存。

即使使用固定内存大小，仍会为虚拟机添加气球设备，因为它能提供有用信息，例如客户机实际使用了多少内存。通常，您应保持启用 **ballooning**，但如果您想禁用它（例如出于调试目的），只需取消选中 **气球设备** 或进行如下设置

```text
balloon: 0
```

在配置中。

<a id="qm_ballooning"></a>



**自动内存分配**

当最小内存的设置低于内存时，Proxmox VE 会确保虚拟机始终可以使用您指定的最小内存量；如果宿主机的 RAM 使用率低于某个目标百分比，则会动态地向客户机添加内存，直至达到指定的最大内存。目标百分比默认为 80%，可以[在节点选项中](../03-system-administration/11-proxmox-node-management.md#ballooning-target)进行配置。

当宿主机 RAM 不足时，虚拟机随后会将部分内存释放回宿主机，必要时换出正在运行的进程，并在万不得已时启动 oom killer。宿主机和客户机之间的内存传递通过运行在客户机内部的特殊 `balloon` 内核驱动程序完成，该驱动程序会从宿主机获取或向宿主机释放内存页。[\[8\]](#note-0fea3830-8)

当多台虚拟机使用自动分配功能时，可以设置 **Shares** 系数，该系数表示每台虚拟机应占用的宿主机空闲内存相对比例。例如，假设您有四台虚拟机，其中三台运行 HTTP 服务器，最后一台是数据库服务器。宿主机配置的目标 RAM 使用率为 80%。为了在数据库服务器的 RAM 中缓存更多数据库块，您希望在有闲置 RAM 时优先考虑数据库虚拟机。为此，将数据库虚拟机的 Shares 属性设置为 3000，其他虚拟机则保留 Shares 的默认设置 1000。该宿主机具有 32GB RAM，当前已使用 16GB，因此在虚拟机各自配置的最小内存量之外，还有 32 \* 80/100 \- 16 \= 9GB RAM 可分配给虚拟机。数据库虚拟机将额外获得 9 \* 3000 / (3000 \+ 1000 \+ 1000 \+ 1000\) \= 4.5 GB RAM，每台 HTTP 服务器虚拟机则可额外获得 1.5 GB。

2010 年之后发布的所有 Linux 发行版都包含气球内核驱动程序。对于 Windows 操作系统，需要手动添加气球驱动程序，这可能会导致客户机速度变慢，因此我们不建议在关键系统上使用它。

为虚拟机分配 RAM 时，一个很好的经验法则是始终为宿主机保留 1GB 可用 RAM。

## 10.2.7. 内存加密 <a href="#qm_memory_encryption" id="qm_memory_encryption"></a>

### AMD SEV <a href="#qm_memory_encryption_sev" id="qm_memory_encryption_sev"></a>

SEV（安全加密虚拟化）使用 AES-128 加密和 AMD Secure Processor，为每台虚拟机启用内存加密。

SEV-ES（安全加密虚拟化 \- 加密状态）还会加密所有 CPU 寄存器内容，以防止信息泄露给虚拟机监视器。

SEV-SNP（安全加密虚拟化 \- 安全嵌套分页）还试图防止基于软件的完整性攻击。有关更多信息，请参阅 [AMD SEV SNP 白皮书](https://www.amd.com/content/dam/amd/en/documents/epyc-business-docs/white-papers/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf)。

**宿主机要求：**

- AMD EPYC CPU
- SEV-ES 仅在 AMD EPYC 7002 系列及更新的 EPYC CPU 上受支持
- SEV-SNP 仅在 AMD EPYC 7003 系列及更新的 EPYC CPU 上受支持
- SEV-SNP 要求宿主机内核版本为 6.11 或更高。
- 在宿主机的 BIOS 设置中配置 AMD 内存加密
- 如果默认未启用，请将 "kvm\_amd.sev\=1" 添加到内核参数
- 如果您想加密宿主机上的内存（SME），请将 "mem\_encrypt\=on" 添加到内核参数，请参阅 [https://www.kernel.org/doc/Documentation/x86/amd-memory-encryption.txt](https://www.kernel.org/doc/Documentation/x86/amd-memory-encryption.txt)
- 可能需要增加 SWIOTLB，请参阅 [https://github.com/AMDESE/AMDSEV#faq-4](https://github.com/AMDESE/AMDSEV#faq-4)

要检查宿主机上是否启用了 SEV，请在 dmesg 中搜索 `sev`，并打印 kvm\_amd 的 SEV 内核参数：

```text
# dmesg | grep -i sev
[...] ccp 0000:45:00.1: sev enabled
[...] ccp 0000:45:00.1: SEV API: <buildversion>
[...] SEV supported: <number> ASIDs
[...] SEV-ES supported: <number> ASIDs
# cat /sys/module/kvm_amd/parameters/sev
Y
```

**客户机要求：**

- edk2-OVMF
- 建议使用 Q35
- 客户机操作系统必须支持 SEV。

**限制：**

- 由于内存已加密，宿主机上显示的内存使用情况始终不准确。
- 涉及保存或恢复内存的操作（如快照和在线迁移）尚无法正常工作，或者[容易受到攻击](https://github.com/PSPReverse/amd-sev-migration-attack)。
- 不支持 PCI 直通。
- SEV-ES 和 SEV-SNP 仍处于高度实验性阶段。
- SEV-SNP 不支持 EFI 磁盘。
- 使用 SEV-SNP 时，虚拟机内的 `reboot` 命令只会让虚拟机关机。

**配置示例（SEV）：**

```text
# qm set <vmid> -amd-sev type=std,no-debug=1,no-key-sharing=1,kernel-hashes=1
```

**type** 定义加密技术（不需要 "type\="）。可用选项为 std、es 和 snp。

QEMU 的 **policy** 参数根据 **no-debug** 和 **no-key-sharing** 参数计算得出。这些参数分别对应 policy-bit 0 和 1。如果 **type** 为 **es**，则将 policy-bit 2 设置为 1，以启用 SEV-ES。policy-bit 3（nosend）始终设置为 1，以防止迁移攻击。有关如何计算 policy 的更多信息，请参阅：[AMD SEV API 规范第 3 章](https://www.amd.com/system/files/TechDocs/55766_SEV-KM_API_Specification.pdf)

为了向后兼容较旧的 OVMF 镜像以及不度量 kernel/initrd 的客户机，**kernel-hashes** 选项默认关闭。请参阅 [https://lists.gnu.org/archive/html/qemu-devel/2021-11/msg02598.html](https://lists.gnu.org/archive/html/qemu-devel/2021-11/msg02598.html)

**检查 SEV 是否在虚拟机中正常工作**

方法 1 \- dmesg：

输出应如下所示。

```text
# dmesg | grep -i sev
AMD Memory Encryption Features active: SEV
```

方法 2 \- MSR 0xc0010131（MSR\_AMD64\_SEV）：

输出应为 1。

```text
# apt install msr-tools
# modprobe msr
# rdmsr -a 0xc0010131
1
```

**配置示例（SEV-SNP）：**

```text
# qm set <vmid> -amd-sev type=snp,allow-smt=1,no-debug=1,kernel-hashes=1
```

默认会设置 `allow-smt` policy-bit。如果通过将 `allow-smt` 设置为 `0` 来禁用它，则必须在宿主机上禁用 SMT，虚拟机才能运行。

**检查 SEV-SNP 是否在虚拟机中正常工作**

```text
# dmesg | grep -i snp
Memory Encryption Features active: AMD SEV SEV-ES SEV-SNP
SEV: Using SNP CPUID table, 29 entries present.
SEV: SNP guest platform device initialized.
```

链接：

- [https://developer.amd.com/sev/](https://developer.amd.com/sev/)
- [https://github.com/AMDESE/AMDSEV](https://github.com/AMDESE/AMDSEV)
- [https://www.qemu.org/docs/master/system/i386/amd-memory-encryption.html](https://www.qemu.org/docs/master/system/i386/amd-memory-encryption.html)
- [https://www.amd.com/system/files/TechDocs/55766\_SEV-KM\_API\_Specification.pdf](https://www.amd.com/system/files/TechDocs/55766_SEV-KM_API_Specification.pdf)
- [https://documentation.suse.com/sles/15-SP1/html/SLES-amd-sev/index.html](https://documentation.suse.com/sles/15-SP1/html/SLES-amd-sev/index.html)
- [SEV 安全嵌套分页固件 ABI 规范](https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/specifications/56860.pdf)

## 10.2.8. 网络设备 <a href="#qm_network_device" id="qm_network_device"></a>

[![screenshot/gui-create-vm-network.png](../../assets/screenshot-gui-create-vm-network-png-52dc7176c8f4.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-network.png)

每台虚拟机都可以有多个 *网络接口控制器*（NIC），分为四种不同类型：

- **Intel E1000** 是默认类型，模拟 Intel 千兆网卡。
- 如果追求最高性能，应使用 **VirtIO** 半虚拟化 NIC。与所有 VirtIO 设备一样，客户机操作系统应安装适当的驱动程序。
- **Realtek 8139** 模拟较旧的 100 MB/s 网卡，只应在模拟较旧的操作系统（2002 年之前发布）时使用
- **vmxnet3** 是另一种半虚拟化设备，只应在从其他虚拟机监视器导入虚拟机时使用。

Proxmox VE 会为每个 NIC 生成一个随机 **MAC 地址**，从而使虚拟机能够在以太网网络中被寻址。

您添加到虚拟机的 NIC 可以采用以下两种不同模式之一：

- 在默认的 **桥接模式**下，每个虚拟 NIC 在宿主机上都有一个 *tap 设备* 作为后端（一种模拟以太网 NIC 的软件环回设备）。此 tap 设备会添加到一个网桥，在 Proxmox VE 中默认为 vmbr0。在此模式下，虚拟机可以直接访问宿主机所在的以太网 LAN。
- 在备选的 **NAT 模式**下，每个虚拟 NIC 只与 QEMU 用户网络协议栈通信，其中内置的路由器和 DHCP 服务器可以提供网络访问。此内置 DHCP 将在私有 10.0.2.0/24 范围内提供地址。NAT 模式比桥接模式慢得多，只应用于测试。此模式只能通过 CLI 或 API 使用，不能通过 Web UI 使用。

您还可以在创建虚拟机时选择 **无网络设备**，以跳过添加网络设备。

您可以手动覆盖每个虚拟机网络设备的 **MTU** 设置。将该字段留空或设置为 `mtu=1` 将从底层网桥继承 MTU。此选项仅适用于 **VirtIO** 网络设备。

**多队列**

如果您使用 VirtIO 驱动程序，可以选择启用 **Multiqueue** 选项。此选项允许客户机操作系统使用多个虚拟 CPU 处理网络数据包，从而提高传输的数据包总数。

在 Proxmox VE 中使用 VirtIO 驱动程序时，每个 NIC 网络队列都会传递给宿主机内核，队列将在该内核中由 vhost 驱动程序创建的内核线程处理。启用此选项后，可以为每个 NIC 将*多个*网络队列传递给宿主机内核。

使用 Multiqueue 时，建议将其设置为等于客户机 vCPU 数量的值。请记住，vCPU 数量是为虚拟机配置的插槽数乘以核心数。您还需要使用以下 ethtool 命令，设置虚拟机中每个 VirtIO NIC 的多用途通道数量：

`ethtool -L ens1 combined X`

其中 X 是虚拟机的 vCPU 数量。

要为 Windows 客户机配置 Multiqueue，请安装 [Redhat VirtIO Ethernet Adapter 驱动程序](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers)，然后按如下方式调整 NIC 的配置。打开设备管理器，右键单击“网络适配器”下的 NIC，然后选择“属性”。接着打开“高级”选项卡，并从左侧列表中选择“Receive Side Scaling”。确保其设置为“Enabled”。接下来，在列表中找到“Maximum number of RSS Queues”，并将其设置为 VM 的 vCPU 数量。确认设置正确后，单击“确定”以确认这些设置。

您应该注意，将 Multiqueue 参数设置为大于 1 的值时，随着流量增加，宿主机和客户机系统的 CPU 负载都会增加。我们建议仅在 VM 必须处理大量传入连接时才设置此选项，例如 VM 作为路由器、反向代理或执行长轮询的繁忙 HTTP 服务器运行时。

## 10.2.9. 显示 <a href="#qm_display" id="qm_display"></a>

QEMU 可以虚拟化几种类型的 VGA 硬件。例如：

- **std**，默认值，模拟带有 Bochs VBE 扩展的显卡。
- **cirrus**，它曾经是默认值，模拟一种非常老旧的硬件模块，并保留了其所有问题。只有在确实必要时才应使用这种显示类型[\[9\]](#note-0fea3830-9)，例如在使用 Windows XP 或更早版本时。
- **vmware**，是一种兼容 VMWare SVGA-II 的适配器。
- **qxl**，是 QXL 半虚拟化显卡。选择此项还会为 VM 启用 [SPICE](https://www.spice-space.org/)（一种远程查看器协议）。
- **virtio-gl**，通常称为 VirGL，是一种供 VM 内部使用的虚拟 3D GPU，可以将工作负载卸载到宿主机 GPU，而无需专用（昂贵的）型号和驱动程序，也不需要完全独占宿主机 GPU，从而允许多个客户机和/或宿主机重复使用该 GPU。

  {% hint style="info" %}
  VirGL 支持需要一些额外的库，这些库由于体积相对较大，而且并非适用于所有 GPU 型号/供应商的开源版本，因此默认不会安装。对于大多数设置，您只需执行：`apt install libgl1 libegl1`
  {% endhint %}

您可以通过设置 *memory* 选项来编辑分配给虚拟 GPU 的内存量。这可以在 VM 内启用更高的分辨率，尤其是在使用 SPICE/QXL 时。

由于内存由显示设备保留，为 SPICE 选择多显示器模式（例如 `qxl2` 表示双显示器）会产生一些影响：

- Windows 需要每台显示器对应一个设备，因此，如果您的 *ostype* 是某个 Windows 版本，Proxmox VE 会为 VM 的每台显示器额外提供一个设备。每个设备都会获得指定数量的内存。
- Linux VM 始终可以启用更多虚拟显示器，但选择多显示器模式会将分配给设备的内存乘以显示器数量。

选择 `serialX` 作为显示 *type* 会禁用 VGA 输出，并将 Web 控制台重定向到所选的串行端口。在这种情况下，配置的显示 *memory* 设置将被忽略。

**VNC 剪贴板**

您可以通过将 `clipboard` 设置为 `vnc` 来启用 VNC 剪贴板。

```text
# qm set <vmid> -vga <displaytype>,clipboard=vnc
```

要使用剪贴板功能，必须先安装 SPICE 客户机工具。在基于 Debian 的发行版上，可以通过安装 `spice-vdagent` 来实现。对于其他操作系统，请在官方软件仓库中搜索，或参阅：[https://www.spice-space.org/download.html](https://www.spice-space.org/download.html)

Once you have installed the spice guest tools, you can use the VNC clipboard function (e.g. in the noVNC console panel). However, if you’re using SPICE, virtio or virgl, you’ll need to choose which clipboard to use. This is because the default **SPICE** clipboard will be replaced by the **VNC** clipboard, if `clipboard` is set to `vnc`.

{% hint style="info" %}
为了启用 VNC 剪贴板，QEMU 会被配置为使用 qemu-vdagent 设备。QEMU 10.1 版本增加了对该设备在线迁移的支持。运行在低于 10.1 的 QEMU 或机器版本上且已启用 VNC 剪贴板的 VM 无法在线迁移。
{% endhint %}

## 10.2.10. USB 直通 <a href="#qm_usb_passthrough" id="qm_usb_passthrough"></a>

USB 直通设备有两种不同的类型：

- 宿主机 USB 直通
- SPICE USB 直通

宿主机 USB 直通通过将宿主机的一个 USB 设备提供给 VM 来工作。这可以通过供应商 ID 和产品 ID 完成，也可以通过宿主机总线和端口完成。

供应商/产品 ID 的格式如下：**0123:abcd**，其中 **0123** 是供应商 ID，**abcd** 是产品 ID，这意味着同一型号 USB 设备的两个实例具有相同的 ID。

总线/端口的格式如下：**1-2.3.4**，其中 **1** 是总线，**2.3.4** 是端口路径。这表示宿主机的物理端口（取决于 USB 控制器的内部顺序）。

如果 VM 启动时其配置中存在某个设备，但该设备并不存在于宿主机上，VM 仍可正常启动。一旦该设备/端口在宿主机上可用，就会被直通给 VM。

{% hint style="warning" %}
使用这种 USB 直通意味着您无法将 VM 在线迁移到另一台宿主机，因为该硬件仅在 VM 当前所在的宿主机上可用。
{% endhint %}

第二种直通类型是 SPICE USB 直通。如果为 VM 添加一个或多个 SPICE USB 端口，就可以将 SPICE 客户端上的本地 USB 设备动态直通到 VM。这对于临时重定向输入设备或硬件加密狗非常有用。

还可以在集群级别映射设备，以便它们能够正确用于 HA，并且可以检测硬件变更，同时非 root 用户也能对其进行配置。有关详细信息，请参阅[资源映射](12-resource-mapping.md)。

## 10.2.11. BIOS 和 UEFI <a href="#qm_bios_and_uefi" id="qm_bios_and_uefi"></a>

为了正确模拟计算机，QEMU 需要使用固件。在普通 PC 上通常称为 BIOS 或 (U)EFI 的固件，是 VM 启动时最早执行的步骤之一。它负责执行基本硬件初始化，并为操作系统提供固件和硬件接口。默认情况下，QEMU 使用 **SeaBIOS**，这是一种开源的 x86 BIOS 实现。对于大多数标准设置，SeaBIOS 是一个不错的选择。

{% hint style="info" %}
SeaBIOS 以及 `bios=seabios` 仅适用于 x86 客户机。在 arm64 宿主机上，虚拟机始终通过 UEFI 启动，使用 OVMF 的 ARM 构建版本（AAVMF），因此 `bios=ovmf` 是那里唯一受支持的设置。
{% endhint %}

某些操作系统（例如 Windows 11）可能要求使用兼容 UEFI 的实现。在这种情况下，必须改用 **OVMF**，它是一种开源的 UEFI 实现。[\[10\]](#note-0fea3830-10)

在其他一些场景中，SeaBIOS 可能不是理想的启动固件，例如当您想要进行 VGA 直通时。[\[11\]](#note-0fea3830-11)

如果您想使用 OVMF，需要考虑以下几点：

为了保存**启动顺序**之类的设置，需要有一个 EFI 磁盘。该磁盘将包含在备份和快照中，并且只能有一个。

您可以使用以下命令创建这样的磁盘：

```text
# qm set <vmid> -efidisk0 <storage>:1,format=<format>,efitype=4m,pre-enrolled-keys=1
```

其中 **\<storage\>** 是您希望存放该磁盘的存储，**\<format\>** 是该存储支持的格式。或者，您也可以通过 Web 界面，在 VM 的硬件部分使用 *Add* → *EFI Disk* 创建这样的磁盘。

**efitype** 选项指定应使用哪个版本的 OVMF 固件。对于新 VM，应始终使用 *4m*，因为它支持安全启动，并分配了更多空间以支持未来的开发（这是 GUI 中的默认值）。

**pre-enroll-keys** 指定 efidisk 是否应预装特定于发行版的密钥和 Microsoft 标准安全启动密钥。它还会默认启用安全启动（但仍可在 VM 内的 OVMF 菜单中禁用）。另请参阅[安全启动证书过期](#qm_secure_boot_ca_expiration)。

{% hint style="info" %}
如果您想在现有 VM（仍使用 *2m* efidisk）中开始使用安全启动，则需要重新创建 efidisk。为此，请删除旧磁盘（`qm set <vmid> -delete efidisk0`），然后按上述说明添加新磁盘。这将重置您在 OVMF 菜单中所做的任何自定义配置！
{% endhint %}

将 OVMF 与虚拟显示器一起使用时（不进行 VGA 直通），您需要在 OVMF 菜单中设置客户端分辨率（启动期间按 ESC 键即可进入该菜单），或者必须选择 SPICE 作为显示类型。

将 OVMF 与 PXE 启动一起使用时，必须向 VM 添加一个 [RNG device](#qm_virtio_rng)。出于安全原因，OVMF 固件会禁止没有随机数生成器的客户机使用 PXE 启动。

### 安全启动证书过期 <a href="#qm_secure_boot_ca_expiration" id="qm_secure_boot_ca_expiration"></a>

Windows 和常见 Linux 发行版用于安全启动的 Microsoft 2011 年原始证书集将于 2026 年 6 月过期。Microsoft 于 2023 年创建了替代证书[\[12\]](#note-0fea3830-12)。

固件只允许使用 EFI 磁盘上存在的证书所签名的引导加载程序。特别是，仅包含 2011 年证书的 EFI 磁盘将拒绝使用 2023 年证书签名的引导加载程序。VM 配置中 EFI 磁盘的 `ms-cert=2023k` 标记表示新证书已注册。

如果 `pve-edk2-firmware` 软件包版本至少为 `4.2025.05-1`，则新创建的 EFI 磁盘会同时包含 2011 年和 2023 年的证书，并带有 `ms-cert=2023k` 标记。对于此前创建的 EFI 磁盘，您需要注册这些证书：

对于使用 BitLocker 的 Windows，请在 PowerShell 中运行以下命令：

```text
manage-bde -protectors -disable <drive>
```

例如，`<drive>` 可以是 `C:`。在继续操作之前，每个使用 BitLocker 的驱动器都必须执行此操作。否则，下次启动时系统将提示您输入 BitLocker 恢复密钥！

在 UI 的 *Hardware* 视图中选择 EFI 磁盘，然后使用 *Disk Action \> Enroll Updated Certificates*。或者，通过 `/nodes/{node}/qemu/{vmid}/config` API 端点注册证书。注册将在 VM 下次启动时生效。该

```text
qm enroll-efi-keys <vmid>
```

CLI 命令可以实现相同的效果，但要求 VM 处于关机状态。

有关在 Windows 中更新安全启动以及使用新的 2023 年证书为引导加载程序签名的后续步骤，请参阅 Microsoft 关于[enterprise deployment guidance for CVE-2023-24932](https://support.microsoft.com/en-us/topic/enterprise-deployment-guidance-for-cve-2023-24932-88b8f034-20b7-4a45-80cb-c6049b0f9967)的支持文章，以及需要首先安装的[related security update](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24932)。

{% hint style="info" %}
标记 `ms-cert=2023` 和 `ms-cert=2023w` 可能表示部分注册。VM 启动任务日志会对此发出警告。您也应对这类 EFI 磁盘执行注册过程。
{% endhint %}

## 10.2.12. 可信平台模块（TPM） <a href="#qm_tpm" id="qm_tpm"></a>

**可信平台模块**是一种安全存储机密数据（例如加密密钥）的设备，并提供用于验证系统启动的防篡改功能。

某些操作系统（例如 Windows 11）要求将此类设备连接到机器（无论是物理机还是虚拟机）。

通过指定 **tpmstate** 卷来添加 TPM。其工作方式与 efidisk 类似，即创建后无法更改（只能删除）。您可以通过以下命令添加一个：

```text
# qm set <vmid> -tpmstate0 <storage>:1,version=<version>
```

其中 **\<storage\>** 是您希望存放状态的存储，**\<version\>** 可以是 *v1.2* 或 *v2.0*。您也可以通过 Web 界面，在 VM 的硬件部分选择 *Add* → *TPM State* 来添加一个。

*v2.0* TPM 规范较新且支持更好，因此除非您的特定实现需要 *v1.2* TPM，否则应优先使用它。

{% hint style="info" %}
与物理 TPM 相比，模拟 TPM **并不**能提供任何真正的安全优势。TPM 的意义在于，除非通过 TPM 规范中规定的命令，否则其中的数据无法被轻易修改。由于模拟设备的数据存储在常规卷上，因此任何有权访问该卷的人都有可能编辑这些数据。
{% endhint %}

## 10.2.13. 虚拟机间共享内存 <a href="#qm_ivshmem" id="qm_ivshmem"></a>

您可以添加虚拟机间共享内存设备（`ivshmem`），它允许在宿主机与客户机之间共享内存，也允许在多个客户机之间共享内存。

要添加此类设备，可以使用 `qm`：

```text
# qm set <vmid> -ivshmem size=32,name=foo
```

其中大小以 MiB 为单位。文件将位于 `/dev/shm/pve-shm-$name` 下（默认名称为 vmid）。

{% hint style="info" %}
目前，一旦任何使用该设备的 VM 关机或停止，该设备就会被删除。现有连接仍会保持，但无法再与同一设备建立新连接。
{% endhint %}

此类设备的一个用例是 Looking Glass [\[13\]](#note-0fea3830-13) 项目，它可在宿主机与客户机之间实现高性能、低延迟的显示镜像。

## 10.2.14. 音频设备 <a href="#qm_audio_device" id="qm_audio_device"></a>

要添加音频设备，请运行以下命令：

```text
qm set <vmid> -audio0 device=<device>
```

支持的音频设备有：

- `ich9-intel-hda`：Intel HD Audio Controller，模拟 ICH9
- `intel-hda`：Intel HD Audio Controller，模拟 ICH6
- `AC97`：Audio Codec '97，适用于 Windows XP 等较旧的操作系统

有两种可用的后端：

- *spice*
- *none*

*spice* 后端可与 [SPICE](#qm_display) 结合使用，而如果 VM 中的某些软件需要音频设备才能工作，*none* 后端可能会很有用。要使用宿主机的物理音频设备，请使用设备直通（参见 [PCI 直通](09-qm-pci-passthrough.md)和 [USB 直通](#qm_usb_passthrough)）。Microsoft 的 RDP 等远程协议提供了播放声音的选项。

## 10.2.15. VirtIO RNG <a href="#qm_virtio_rng" id="qm_virtio_rng"></a>

RNG（随机数生成器）是一种为系统提供熵（*随机性*）的设备。虚拟硬件 RNG 可用于将宿主机系统的这种熵提供给客户机 VM。这有助于避免客户机出现熵不足问题（即没有足够可用的熵，系统可能变慢或出现问题的情况），尤其是在客户机启动过程中。

要添加基于 VirtIO 的模拟 RNG，请运行以下命令：

```text
qm set <vmid> -rng0 source=<source>[,max_bytes=X,period=Y]
```

`source` 指定在宿主机上从何处读取熵，其值必须是以下之一：

- `/dev/urandom`：非阻塞内核熵池（首选）
- `/dev/random`：阻塞内核池（不推荐，可能导致宿主机系统出现熵不足）
- `/dev/hwrng`：用于直通连接到宿主机的硬件 RNG（如果有多个可用，将使用在 `/sys/devices/virtual/misc/hw_random/rng_current` 中选择的那个）

A limit can be specified via the `max_bytes` and `period` parameters, they are read as `max_bytes` per `period` in milliseconds. However, it does not represent a linear relationship: 1024B/1000ms would mean that up to 1 KiB of data becomes available on a 1 second timer, not that 1 KiB is streamed to the guest over the course of one second. Reducing the `period` can thus be used to inject entropy into the guest at a faster rate.

默认情况下，限制设置为每 1000 ms 1024 字节（1 KiB/s）。建议始终使用限制器，以避免客户机占用过多宿主机资源。如果需要，可将 *0* 用作 `max_bytes` 的值，以禁用所有限制。

## 10.2.16. Virtiofs <a href="#qm_virtiofs" id="qm_virtiofs"></a>

Virtiofs 是一种为虚拟环境设计的共享文件系统。它允许通过在 VM 内挂载宿主机上可用的目录树来共享该目录树。它不使用网络协议栈，并致力于提供与源文件系统类似的性能和语义。

要使用 virtiofs，[virtiofsd](https://gitlab.com/virtio-fs/virtiofsd) 守护进程需要在后台运行。在 Proxmox VE 中，启动使用 virtiofs 挂载的 VM 时会自动完成此操作。

内核版本 \>\=5.4 的 Linux VM 默认支持 virtiofs（[virtiofs 内核模块](https://www.kernelconfig.io/CONFIG_VIRTIO_FS)），但某些功能需要更新的内核。

要使用 virtiofs，请确保 Proxmox VE 宿主机上已安装 virtiofsd：

```text
apt install virtiofsd
```

有一篇[指南](https://github.com/virtio-win/kvm-guest-drivers-windows/wiki/Virtiofs:-Shared-file-system)介绍如何在 Windows VM 中使用 virtiofs。

### 已知限制 <a href="#_known_limitations" id="_known_limitations"></a>

- 如果 virtiofsd 崩溃，其挂载点将在 VM 中一直处于无响应状态，直到 VM 完全停止。
- virtiofsd 无响应可能会导致 VM 中的挂载卡住，类似于无法访问 NFS 的情况。
- 内存热插拔在与 virtiofs 一起使用时不起作用（也会导致访问卡住）。
- 在线迁移、快照和休眠等内存相关功能在 virtiofs 设备上不可用。
- Windows 无法理解 virtiofs 上下文中的 ACL。因此，不要向 Windows VM 暴露 ACL，否则 virtiofs 设备将在 VM 内不可见。

### 为共享目录添加映射 <a href="#_add_mapping_for_shared_directories" id="_add_mapping_for_shared_directories"></a>

要为共享目录添加映射，可以直接通过 API 使用 `pvesh`，具体方法见[资源映射](12-resource-mapping.md)一节：

```text
pvesh create /cluster/mapping/dir --id dir1 \
    --map node=node1,path=/path/to/share1 \
    --map node=node2,path=/path/to/share2 \
```

### 将 virtiofs 添加到 VM <a href="#_add_virtiofs_to_a_vm" id="_add_virtiofs_to_a_vm"></a>

要使用 virtiofs 共享目录，请将参数 `virtiofs<N>`（N 可以是 0 到 9 之间的任意值）添加到 VM 配置中，并使用已在资源映射中配置的目录 ID（dirid）。此外，可以根据需求将 `cache` 选项设置为 `always`、`never`、`metadata` 或 `auto`（默认值：`auto`）。有关不同缓存模式行为的信息，请参阅[此处的“缓存模式”一节](https://lwn.net/Articles/774495/)。

`virtiofsd` 支持 ACL 和 xattr 直通（可通过 `expose-acl` 和 `expose-xattr` 选项启用），如果底层宿主机文件系统支持 ACL 和 xattr，则允许客户机访问它们，但它们还必须与客户机文件系统兼容（例如，大多数 Linux 文件系统支持 ACL，而 Windows 文件系统不支持）。

`expose-acl` 选项会自动隐含 `expose-xattr`，也就是说，将 `expose-xattr` 设置为 `0` 时，如果 `expose-acl` 已设置为 `1`，结果不会有所不同。

如果希望 virtiofs 遵循 `O_DIRECT` 标志，可以将 `direct-io` 参数设置为 `1`（默认值：`0`）。这会降低性能，但在应用程序自行进行缓存时很有用。

```text
qm set <vmid> -virtiofs0 dirid=<dirid>,cache=always,direct-io=1
qm set <vmid> -virtiofs1 <dirid>,cache=never,expose-xattr=1
qm set <vmid> -virtiofs2 <dirid>,expose-acl=1
```

要在使用 Linux 内核 virtiofs 驱动程序的客户机 VM 中临时挂载 virtiofs，请在客户机内运行以下命令：

```text
mount -t virtiofs <dirid> <mount point>
```

要持久挂载 virtiofs，可以创建一个 fstab 条目：

```text
<dirid> <mount point> virtiofs rw,relatime 0 0
```

与当前节点上的路径关联的 dirid 也会用作挂载标签（在客户机上挂载设备时使用的名称）。

有关可用 virtiofsd 参数的更多信息，请参阅[GitLab virtiofsd 项目页面](https://gitlab.com/virtio-fs/virtiofsd)。

## 10.2.17. 设备启动顺序 <a href="#qm_bootorder" id="qm_bootorder"></a>

QEMU 可以告知客户机应从哪些设备启动以及启动顺序。可以通过配置中的 `boot` 属性指定，例如：

```text
boot: order=scsi0;net0;hostpci0
```

[![screenshot/gui-qemu-edit-bootorder.png](../../assets/screenshot-gui-qemu-edit-bootorder-png-e24815e584de.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-edit-bootorder.png)

这样，客户机会首先尝试从磁盘 `scsi0` 启动；如果失败，则会继续尝试从 `net0` 进行网络启动；如果仍然失败，最后会尝试从直通 PCIe 设备启动（对于 NVMe，该设备会被视为磁盘，否则会尝试从 option ROM 启动）。

在 GUI 中，您可以使用拖放编辑器指定启动顺序，并通过复选框启用或禁用某些设备的启动。

{% hint style="info" %}
如果您的客户机使用多个磁盘来启动操作系统或加载引导加载程序，则必须将所有这些磁盘标记为*可启动*（即必须启用相应复选框，或使其出现在配置中的列表里），客户机才能启动。这是因为较新的 SeaBIOS 和 OVMF 版本只会初始化标记为*可启动*的磁盘。
{% endhint %}

无论如何，即使设备未出现在列表中或未选中其复选框，一旦客户机的操作系统启动并初始化这些设备，它们仍可供客户机使用。*可启动*标志仅影响客户机 BIOS 和引导加载程序。

## 10.2.18. 虚拟机的自动启动和关闭 <a href="#qm_startup_and_shutdown" id="qm_startup_and_shutdown"></a>

创建 VM 后，您可能希望它们在宿主机系统启动时自动启动。为此，您需要在 Web 界面中选择 VM 的*开机启动*选项，该选项位于*选项*选项卡中，或者使用以下命令进行设置：

```text
# qm set <vmid> -onboot 1
```

[![screenshot/gui-qemu-edit-start-order.png](../../assets/screenshot-gui-qemu-edit-start-order-png-9683f539b3b2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-edit-start-order.png)

**启动和关闭顺序**

在某些情况下，您可能希望能够微调 VM 的启动顺序，例如，当您的某个 VM 为其他客户机系统提供防火墙或 DHCP 服务时。为此，可以使用以下参数：

- **启动/关闭顺序**：定义启动顺序优先级。例如，如果希望 VM 第一个启动，请将其设置为 1。（关闭时采用相反的启动顺序，因此启动顺序为 1 的机器将最后关闭）。如果宿主机上的多个 VM 定义了相同顺序，则还会按 *VMID* 升序排列。
- **启动延迟**：定义此 VM 启动与后续 VM 启动之间的时间间隔。例如，如果希望在启动其他 VM 之前等待 240 秒，请将其设置为 240。
- **关闭超时**：定义 Proxmox VE 在发出关闭命令后等待 VM 离线的时长（秒）。默认情况下，此值设置为 180，这意味着 Proxmox VE 会发出关闭请求，并等待 180 秒让机器离线。如果超时后机器仍在线，将被强制停止。

{% hint style="info" %}
目前，由 HA 堆栈管理的 VM 不遵循*开机启动*和*启动顺序*选项。这些 VM 将被启动和关闭算法跳过，因为 HA 管理器本身会确保 VM 得到启动和停止。
{% endhint %}

请注意，未设置启动/关闭顺序参数的机器始终会在设置了该参数的机器之后启动。此外，该参数只能在同一宿主机上运行的虚拟机之间强制执行，无法在整个集群范围内生效。

如果您需要在宿主机启动与第一台 VM 启动之间设置延迟，请参阅[Proxmox VE 节点管理](../03-system-administration/11-proxmox-node-management.md#first_guest_boot_delay)一节。

## 10.2.19. QEMU Guest Agent <a href="#qm_qemu_agent" id="qm_qemu_agent"></a>

QEMU Guest Agent 是一项在 VM 内运行的服务，它在宿主机与客户机之间提供通信通道。它用于交换信息，并允许宿主机向客户机发出命令。

例如，VM 摘要面板中的 IP 地址就是通过客户机代理获取的。

或者，在开始备份时，会通过客户机代理指示客户机通过 `guest-fsfreeze-freeze` 和 `guest-fsfreeze-thaw` 命令同步未完成的写入。

要使客户机代理正常工作，必须执行以下步骤：

- 在客户机中安装代理并确保其正在运行
- 在 Proxmox VE 中启用通过代理进行的通信

### 安装客户机代理 <a href="#_install_guest_agent" id="_install_guest_agent"></a>

大多数 Linux 发行版都提供客户机代理。该软件包通常名为 `qemu-guest-agent`。

对于 Windows，请参阅我们的[Windows VirtIO 驱动程序](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers)文章，了解有关如何获取和安装驱动程序的更多信息。

### 启用客户机代理通信 <a href="#qm_qga_enable" id="qm_qga_enable"></a>

可以在 VM 的**选项**面板中启用 Proxmox VE 与客户机代理之间的通信。需要重新启动 VM 才能使更改生效。

### 使用 QGA 自动执行 TRIM <a href="#qm_qga_auto_trim" id="qm_qga_auto_trim"></a>

可以启用*运行 guest-trim*选项。启用后，Proxmox VE 会在以下可能将零写入存储的操作完成后，向客户机发出 trim 命令：

- 将磁盘移动到另一个存储
- 将使用本地存储的 VM 在线迁移到另一个节点

在精简置备存储上，这可以帮助释放未使用的空间。

{% hint style="info" %}
Linux 上的 ext4 有一个注意事项，因为它使用内存中的优化来避免发出重复的 TRIM 请求。由于客户机不知道底层存储的变化，只有第一次客户机 TRIM 会按预期运行。此后直到下次重启，后续 TRIM 只会考虑自那以后发生变化的文件系统部分。
{% endhint %}

### 文件系统冻结与解冻 <a href="#qm_qga_fsfreeze" id="qm_qga_fsfreeze"></a>

默认情况下，如果在客户机配置中启用了 QEMU Guest Agent，并且该代理在客户机内部可用，那么在执行某些操作时，会通过 `guest-fsfreeze-freeze` QEMU Guest Agent 命令同步虚拟机的文件系统。这样做是为了保证数据一致性。

有关更多详细信息，请参阅 [QEMU Guest Agent 协议参考](https://www.qemu.org/docs/master/interop/qemu-ga-ref.html)。

在 VM 上执行以下任何操作时，都会发出冻结指令：

- 以快照模式执行备份
- 在 VM 运行时创建其克隆
- 在 VM 运行时进行复制
- 为正在运行的 VM 创建不含 RAM 的快照
- 从正在运行的客户机导入磁盘映像会对该正在运行的客户机发出冻结指令

在 Windows 客户机上，某些应用程序可能会通过挂接到 Windows VSS（卷影复制服务）层来自行处理一致性备份，而冻结可能会干扰此过程。例如，已观察到在某些 SQL Server 上调用 `guest-fsfreeze-freeze` 会触发 VSS 以一种模式调用 SQL Writer VSS 模块，而该模式会破坏 SQL Server 差异备份的备份链。

处理这种情况有两种方法。

1. 将 QEMU Guest Agent 配置为使用不会干扰其他 VSS 用户的不同 VSS 变体。[Proxmox VE wiki](https://pve.proxmox.com/wiki/VM_Backup_Consistency) 中有更多详细信息。
2. 或者，您可以通过禁用 `freeze-fs` 客户机代理选项，将 Proxmox VE 配置为不发出冻结和解冻周期。这也可以在 GUI 中完成：打开虚拟机的 *选项* 面板，然后打开 *QEMU Guest Agent* 对话框，并禁用 *在某些操作期间冻结/解冻客户机文件系统以保持一致性* 选项。

   {% hint style="warning" %}
   禁用此选项可能会导致备份中的文件系统不一致。因此，首选方法是调整客户机中的 QEMU Guest Agent 配置。
   {% endhint %}

### 故障排除 <a href="#_troubleshooting_2" id="_troubleshooting_2"></a>

**VM 无法关机**

确保已安装并正在运行客户机代理。

启用客户机代理后，Proxmox VE 将通过客户机代理发送 *shutdown* 等电源命令。如果客户机代理未运行，命令将无法正确执行，关机命令将因超时而失败。

## 10.2.20. SPICE 增强功能 <a href="#qm_spice_enhancements" id="qm_spice_enhancements"></a>

SPICE 增强功能是可选功能，可改善远程查看器的使用体验。

要通过 GUI 启用这些功能，请转到虚拟机的 **选项** 面板。运行以下命令以通过 CLI 启用它们：

```text
qm set <vmid> -spice_enhancements foldersharing=1,videostreaming=all
```

{% hint style="info" %}
要使用这些功能，必须将虚拟机的 [**显示**](#qm_display) 设置为 SPICE (qxl)。
{% endhint %}

### 文件夹共享 <a href="#_folder_sharing" id="_folder_sharing"></a>

与客户机共享本地文件夹。需要在客户机中安装 `spice-webdavd` 守护进程。它通过位于 [http://localhost:9843](http://localhost:9843) 的本地 WebDAV 服务器提供共享文件夹。

For Windows guests the installer for the *Spice WebDAV daemon* can be downloaded from the [official SPICE website](https://www.spice-space.org/download.html#windows-binaries).

大多数 Linux 发行版都有一个名为 `spice-webdavd` 的可安装软件包。

要在 Virt-Viewer (Remote Viewer) 中共享文件夹，请转到 *文件 → 首选项*。选择要共享的文件夹，然后勾选该复选框。

{% hint style="info" %}
文件夹共享目前仅适用于 Linux 版本的 Virt-Viewer。
{% endhint %}

{% hint style="danger" %}
实验性功能！目前此功能无法可靠工作。
{% endhint %}

### 视频流 <a href="#_video_streaming" id="_video_streaming"></a>

快速刷新的区域会被编码为视频流。有两个选项：

- **all**：任何快速刷新的区域都会被编码为视频流。
- **filter**：使用附加过滤器来决定是否应使用视频流（目前仅跳过小窗口区域）。

无法就是否应启用视频流以及应选择哪个选项给出一般性建议。实际效果可能因具体情况而异。

### 故障排除 <a href="#_troubleshooting_3" id="_troubleshooting_3"></a>

**共享文件夹未显示**

确保 WebDAV 服务已在客户机中启用并正在运行。在 Windows 上，它称为 *Spice webdav proxy*。在 Linux 中，名称为 *spice-webdavd*，但可能因发行版而异。

如果服务正在运行，请在客户机内的浏览器中打开 [http://localhost:9843](http://localhost:9843) 来检查 WebDAV 服务器。

重新启动 SPICE 会话可能会有所帮助。

## 注释

### 注释 1 <a href="#note-0fea3830-1" id="note-0fea3830-1"></a>

详情请参见此基准测试 [https://events.static.linuxfound.org/sites/events/files/slides/CloudOpen2013\_Khoa\_Huynh\_v3.pdf](https://events.static.linuxfound.org/sites/events/files/slides/CloudOpen2013_Khoa_Huynh_v3.pdf)

### 注释 2 <a href="#note-0fea3830-2" id="note-0fea3830-2"></a>

TRIM, UNMAP, and discard [https://en.wikipedia.org/wiki/Trim\_%28computing%29](https://en.wikipedia.org/wiki/Trim_%28computing%29)

### 注释 3 <a href="#note-0fea3830-3" id="note-0fea3830-3"></a>

Meltdown 攻击 [https://meltdownattack.com/](https://meltdownattack.com/)

### 注释 4 <a href="#note-0fea3830-4" id="note-0fea3830-4"></a>

spectre-meltdown-checker [https://meltdown.ovh/](https://meltdown.ovh/)

### 注释 5 <a href="#note-0fea3830-5" id="note-0fea3830-5"></a>

PCID 现已成为 x86 上一项关键的性能/安全功能 [https://groups.google.com/forum/m/#!topic/mechanical-sympathy/L9mHTbeQLNU](https://groups.google.com/forum/m/#!topic/mechanical-sympathy/L9mHTbeQLNU)

### 注释 6 <a href="#note-0fea3830-6" id="note-0fea3830-6"></a>

[https://en.wikipedia.org/wiki/Non-uniform\_memory\_access](https://en.wikipedia.org/wiki/Non-uniform_memory_access)

### 注释 7 <a href="#note-0fea3830-7" id="note-0fea3830-7"></a>

如果命令 `numactl --hardware | grep available` 返回多个节点，则说明您的宿主机系统采用 NUMA 架构

### 注释 8 <a href="#note-0fea3830-8" id="note-0fea3830-8"></a>

可以在此处找到对气球驱动程序内部工作原理的详细说明 [https://rwmj.wordpress.com/2010/07/17/virtio-balloon/](https://rwmj.wordpress.com/2010/07/17/virtio-balloon/)

### 注释 9 <a href="#note-0fea3830-9" id="note-0fea3830-9"></a>

[https://www.kraxel.org/blog/2014/10/qemu-using-cirrus-considered-harmful/](https://www.kraxel.org/blog/2014/10/qemu-using-cirrus-considered-harmful/) qemu: using cirrus considered harmful

### 注释 10 <a href="#note-0fea3830-10" id="note-0fea3830-10"></a>

See the OVMF Project [https://github.com/tianocore/tianocore.github.io/wiki/OVMF](https://github.com/tianocore/tianocore.github.io/wiki/OVMF)

### 注释 11 <a href="#note-0fea3830-11" id="note-0fea3830-11"></a>

Alex Williamson has a good blog entry about this [https://vfio.blogspot.co.at/2014/08/primary-graphics-assignment-without-vga.html](https://vfio.blogspot.co.at/2014/08/primary-graphics-assignment-without-vga.html)

### 注释 12 <a href="#note-0fea3830-12" id="note-0fea3830-12"></a>

Microsoft support article about the issue [https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e](https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e)

### 注释 13 <a href="#note-0fea3830-13" id="note-0fea3830-13"></a>

Looking Glass: [https://looking-glass.io/](https://looking-glass.io/)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
