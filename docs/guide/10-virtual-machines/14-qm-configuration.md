# 10.14. 配置 <a href="#qm_configuration" id="qm_configuration"></a>

VM 配置文件存储在 Proxmox 集群文件系统中，可通过 `/etc/pve/qemu-server/<VMID>.conf` 访问。与存储在 `/etc/pve/` 中的其他文件一样，它们会自动复制到所有其他集群节点。

{% hint style="info" %}
VMID \< 100 保留用于内部用途，且 VMID 必须在整个集群范围内唯一。
{% endhint %}

**示例 VM 配置**

```text
boot: order=virtio0;net0
cores: 1
sockets: 1
memory: 512
name: webmail
ostype: l26
net0: e1000=EE:D2:28:5F:B6:3E,bridge=vmbr0
virtio0: local:vm-100-disk-1,size=32G
```

这些配置文件是简单的文本文件，您可以使用普通文本编辑器（`vi`、`nano`、……）进行编辑。这对于进行小幅更正有时很有用，但请记住，需要重启 VM 才能应用此类更改。

因此，通常最好使用 `qm` 命令来生成和修改这些文件，或者完全使用 GUI 完成操作。我们的工具集足够智能，可以立即将大多数更改应用到正在运行的 VM。此功能称为“热插拔”，在这种情况下无需重启 VM。

## 10.14.1. 文件格式 <a href="#_file_format" id="_file_format"></a>

VM 配置文件使用简单的冒号分隔键/值格式。每行格式如下：

```text
# this is a comment
OPTION: value
```

这些文件中的空行会被忽略，以 `#` 字符开头的行会被视为注释，同样会被忽略。

## 10.14.2. 快照 <a href="#qm_snapshots" id="qm_snapshots"></a>

创建快照时，`qm` 会将快照时的配置存储到同一配置文件中的独立快照小节。例如，创建名为“testsnapshot”的快照后，配置文件将如下所示：

**带快照的 VM 配置**

```text
memory: 512
swap: 512
parent: testsnaphot
...

[testsnaphot]
memory: 512
swap: 512
snaptime: 1457170803
...
```

有几个与快照相关的属性，例如 `parent` 和 `snaptime`。`parent` 属性用于存储快照之间的父/子关系。`snaptime` 是快照创建时间戳（Unix 纪元）。

可以选择使用 `vmstate` 选项保存正在运行的 VM 的内存。有关如何为 VM 状态选择目标存储的详细信息，请参阅 [状态存储选择](11-qm-hibernate.md#qm_vmstatestorage)，其位于 [休眠](11-qm-hibernate.md) 一章。

## 10.14.3. 选项 <a href="#qm_options" id="qm_options"></a>

**`acpi`：`<boolean>`（*默认值 \=* `1`）**

启用/禁用 ACPI。

**`affinity`: `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`agent`: `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`enabled`\=`<boolean>`（*默认值 \=* `0`）**

启用/禁用与 VM 中运行的 QEMU Guest Agent（QGA）的通信。

**`freeze-fs`\=`<boolean>`（*默认值 \=* `1`）**

是否发出 guest-fsfreeze-freeze 和 guest-fsfreeze-thaw QEMU 客户机代理命令。当客户机配置中启用了 QEMU Guest Agent 选项且代理正在客户机内运行时，快照模式备份、克隆、不含 RAM 的快照、从正在运行的客户机导入磁盘以及复制，通常会发出 guest-fsfreeze-freeze 和相应的 thaw 命令。

已弃用的 *freeze-fs-on-backup* 设置被视为此设置的别名。

**`fstrim_cloned_disks`\=`<boolean>`（*默认值 \=* `0`）**

移动磁盘或迁移 VM 后运行 fstrim。

**`type`\=`<isa | virtio>`（*默认值 \=* `virtio`）**

选择代理类型

**`allow-ksm`：`<boolean>`（*默认值 \=* `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`amd-sev`: `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`allow-smt`\=`<boolean>`（*默认值 \=* `1`）**

设置策略位以允许同时多线程（SMT）（除非针对 SEV-SNP，否则会被忽略）

**`kernel-hashes`\=`<boolean>`（*默认值 \=* `0`）**

将内核哈希添加到客户机固件，以实现可度量的 Linux 内核启动

**`no-debug`\=`<boolean>`（*默认值 \=* `0`）**

设置策略位以禁止调试客户机

**`no-key-sharing`\=`<boolean>`（*默认值 \=* `0`）**

设置策略位以禁止与其他客户机共享密钥（对于 SEV-SNP 会被忽略）

**`type`\=`<sev-type>`**

使用 type\=*std* 启用标准 SEV，或使用 *es* 选项启用实验性 SEV-ES，或使用 *snp* 选项启用实验性 SEV-SNP。

**`arch`: `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`args`: `<string>`**

传递给 kvm 的任意参数，例如：

args: -no-reboot -smbios *type\=0,vendor\=FOO*

{% hint style="info" %}
此选项仅供专家使用。
{% endhint %}

**`audio0`: `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`device`\=`<AC97 | ich9-intel-hda | intel-hda>`**

配置音频设备。

**`driver`\=`<none | spice>`（*默认值 \=* `spice`）**

音频设备的驱动程序后端。

**`autostart`：`<boolean>`（*默认值 \=* `0`）**

崩溃后自动重启（目前被忽略）。

**`balloon`: `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`bios`：`<ovmf | seabios>`（*默认值 \=* `seabios`）**

选择 BIOS 实现。

**`boot`: `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 *order\=* 子属性，因为不带键的用法或 *legacy\=* 已弃用。

**`legacy`\=`<[acdn]{1,4}>`（*默认值 \=* `cdn`）**

从软盘（a）、硬盘（c）、CD-ROM（d）或网络（n）启动。已弃用，请改用 *order\=*。

**`order`\=`<device[;device...]>`**

客户机将尝试按照此处列出的顺序从设备启动。

磁盘、光驱和直通的 USB 存储设备将直接用于启动，NIC 将加载 PXE，PCIe 设备则将表现得像磁盘（例如 NVMe），或者加载选项 ROM（例如 RAID 控制器、硬件 NIC）。

请注意，只有此列表中的设备才会被标记为可启动，并因此由客户机固件（BIOS/UEFI）加载。如果需要使用多个磁盘启动（例如软件 RAID），则需要在此处指定所有这些磁盘。

如果指定了此选项，将覆盖已弃用的 *legacy\=\[acdn\]\** 值。

**`bootdisk`: `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 *boot: order\=foo;bar*。

**`cdrom`: `<volume>`**

这是选项 -ide2 的别名

**`cicustom`: `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`meta`\=`<volume>`**

指定一个自定义文件，其中包含通过 cloud-init 传递给虚拟机的所有元数据。这是特定于提供商的，也就是说 configdrive2 和 nocloud 有所不同。

**`network`\=`<volume>`**

用于通过 cloud-init 将包含所有网络数据的自定义文件传递给虚拟机。

**`user`\=`<volume>`**

用于通过 cloud-init 将包含所有用户数据的自定义文件传递给虚拟机。

**`vendor`\=`<volume>`**

用于通过 cloud-init 将包含所有供应商数据的自定义文件传递给虚拟机。

**`cipassword`: `<string>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`citype`: `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`ciupgrade`：`<boolean>`（*默认值 \=* `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`ciuser`: `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`cores`: `<integer> (1 - N)` (*默认值 \=* `1`)**

每个 CPU 插槽的核心数。

**`cpu`: `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`cputype`\=`<string>` (*默认值 \=* `kvm64`)**

模拟的 CPU 类型。可以是默认类型或自定义名称（自定义型号名称必须以 *custom-* 为前缀）。

**`flags`\=`<+FLAG[;-FLAG...]>`**

以 *;* 分隔的附加 CPU 标志列表。使用 *\+FLAG* 启用标志，使用 *-FLAG* 禁用标志。有一个特殊的 *nested-virt* 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 使用 *svm*，Intel 使用 *vmx*）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，VM 特定标志必须来自以下集合：aes、amd-no-ssb、amd-ssbd、hv-evmcs、hv-tlbflush、ibpb、md-clear、nested-virt、pcid、pdpe1gb、spec-ctrl、ssbd、virt-ssbd

**`guest-phys-bits`\=`<integer> (32 - 64)`**

客户机可用的物理地址位数。

**`hidden`\=`<boolean>` (*默认值 \=* `0`)**

不要标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。

**`hv-vendor-id`\=`<vendor-id>`**

Hyper-V 供应商 ID。Windows 客户机中的某些驱动程序或程序需要特定的 ID。

**`level`\=`<integer> (0 - 4294967295)`**

客户机可查询的基本 CPUID 叶的最大输入值——即供应商（叶 0）、系列/型号/步进及功能位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶将被隐藏。将此项设置为 *30*，是解决在较新的 Intel 宿主机上运行的 Windows 客户机出现 Hyper-V 启动故障的常用变通方法。仅当 vCPU 架构为 x86\_64 时适用。

**`phys-bits`\=`<8-64|host>`**

报告给客户机操作系统的物理内存地址位数。应小于或等于宿主机的位数。设置为 *host* 可使用宿主机 CPU 的值，但请注意，这样会导致无法在线迁移到该值不同的 CPU。

**`reported-model`\=`<486 | Broadwell | Broadwell-IBRS | Broadwell-noTSX | Broadwell-noTSX-IBRS | Cascadelake-Server | Cascadelake-Server-noTSX | Cascadelake-Server-v2 | Cascadelake-Server-v4 | Cascadelake-Server-v5 | ClearwaterForest | ClearwaterForest-v2 | ClearwaterForest-v3 | Conroe | Cooperlake | Cooperlake-v2 | DiamondRapids | EPYC | EPYC-Genoa | EPYC-Genoa-v2 | EPYC-IBPB | EPYC-Milan | EPYC-Milan-v2 | EPYC-Milan-v3 | EPYC-Rome | EPYC-Rome-v2 | EPYC-Rome-v3 | EPYC-Rome-v4 | EPYC-Rome-v5 | EPYC-Turin | EPYC-v3 | EPYC-v4 | EPYC-v5 | GraniteRapids | GraniteRapids-v2 | GraniteRapids-v3 | GraniteRapids-v4 | GraniteRapids-v5 | Haswell | Haswell-IBRS | Haswell-noTSX | Haswell-noTSX-IBRS | Icelake-Client | Icelake-Client-noTSX | Icelake-Server | Icelake-Server-noTSX | Icelake-Server-v3 | Icelake-Server-v4 | Icelake-Server-v5 | Icelake-Server-v6 | Icelake-Server-v7 | IvyBridge | IvyBridge-IBRS | KnightsMill | Nehalem | Nehalem-IBRS | Opteron_G1 | Opteron_G2 | Opteron_G3 | Opteron_G4 | Opteron_G5 | Penryn | SandyBridge | SandyBridge-IBRS | SapphireRapids | SapphireRapids-v2 | SapphireRapids-v3 | SapphireRapids-v4 | SapphireRapids-v5 | SapphireRapids-v6 | SierraForest | SierraForest-v2 | SierraForest-v3 | SierraForest-v4 | SierraForest-v5 | Skylake-Client | Skylake-Client-IBRS | Skylake-Client-noTSX-IBRS | Skylake-Client-v4 | Skylake-Server | Skylake-Server-IBRS | Skylake-Server-noTSX-IBRS | Skylake-Server-v4 | Skylake-Server-v5 | Westmere | Westmere-IBRS | a64fx | athlon | core2duo | coreduo | cortex-a35 | cortex-a53 | cortex-a55 | cortex-a57 | cortex-a710 | cortex-a72 | cortex-a76 | cortex-a78ae | host | kvm32 | kvm64 | max | neoverse-n1 | neoverse-n2 | neoverse-v1 | pentium | pentium2 | pentium3 | phenom | qemu32 | qemu64>` (*默认值 \=* `kvm64`)**

报告给客户机的 CPU 模型和供应商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效；默认模型始终会向客户机操作系统报告其自身。

**`cpulimit`: `<number> (0 - 128)` (*默认值 \=* `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总计为 *2*。值 *0* 表示不限制 CPU。
{% endhint %}

**`cpuunits`: `<integer> (1 - 262144)` (*默认值 \=* `cgroup v1: 1024, cgroup v2: 100`)**

虚拟机的 CPU 权重。该参数用于内核公平调度器。数值越大，此虚拟机获得的 CPU 时间就越多。该数值是相对于所有其他正在运行的虚拟机的权重而言的。

**`description`: `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`efidisk0`: `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。

**`efitype`\=`<2m | 4m>` (*默认值 \=* `2m`)**

OVMF EFI 变量的大小和类型。*4m* 较新且推荐使用，并且是安全启动所必需的。为保持向后兼容，如果未另行指定，则使用 *2m*。对于 arch\=aarch64 (ARM) 的虚拟机，此设置会被忽略。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

驱动器后端文件的数据格式。

**`ms-cert`\=`<2011 | 2023 | 2023k | 2023w>` (*默认值 \=* `2011`)**

信息性标记，指示 Proxmox VE 已注册的最新 Microsoft UEFI 证书的版本。值 *2023k* 表示包含 *Microsoft UEFI CA 2023*、*Windows UEFI CA 2023* 和 *Microsoft Corporation KEK 2K CA 2023* 证书。值 *2023* 和 *2023w* 已弃用，仅为兼容性保留。

**`pre-enrolled-keys`\=`<boolean>` (*默认值 \=* `0`)**

与 *efitype\=4m* 一起使用时，使用已注册特定发行版密钥和 Microsoft 标准密钥的 EFI 变量模板。请注意，这将默认启用安全启动，但仍可在虚拟机内将其关闭。

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`freeze`: `<boolean>`**

启动时冻结 CPU（使用 *c* 监视器命令开始执行）。

**`hookscript`: `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`hostpci[n]`: `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

{% hint style="info" %}
此选项允许直接访问宿主机硬件。因此，此类机器将无法再迁移——请特别谨慎使用。
{% endhint %}

{% hint style="danger" %}
实验性功能！有用户报告此选项存在问题。
{% endhint %}

**`device-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 设备 ID

**`driver`\=`<keep | vfio>` (*默认值 \=* `vfio`)**

如果设置为 *keep*，设备既不会重置，也不会绑定到 *vfio-pci* 驱动程序。适用于已加载正确驱动程序的设备。

**`host`\=`<HOSTPCIID[;HOSTPCIID2...]>`**

宿主机 PCI 设备直通。宿主机 PCI 设备的 PCI ID，或宿主机的 PCI 虚拟功能列表。HOSTPCIID 语法为：

*bus:dev.func*（十六进制数字）

可以使用 *lspci* 命令列出现有 PCI 设备。

必须设置此项或 *mapping* 键。

**`legacy-igd`\=`<boolean>` (*默认值 \=* `0`)**

以传统 IGD 模式直通此设备，使其成为虚拟机中的主显卡和唯一显卡。需要 *pc-i440fx* 机器类型，并将 VGA 设置为 *none*。

**`mapping`\=`<mapping-id>`**

集群范围映射的 ID。必须设置此项或默认键 *host*。

**`mdev`\=`<string>`**

要使用的中介设备类型。虚拟机启动时将创建此类型的一个实例，并在虚拟机停止时清理该实例。

**`pcie`\=`<boolean>` (*默认值 \=* `0`)**

选择 PCI-express 总线（需要 *q35* 机器型号）。

**`rombar`\=`<boolean>` (*默认值 \=* `1`)**

指定设备的 ROM 是否在客户机的内存映射中可见。

**`romfile`\=`<string>`**

自定义 PCI 设备 ROM 文件名（必须位于 /usr/share/kvm/ 中）。

**`sub-device-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 子系统设备 ID

**`sub-vendor-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 子系统供应商 ID

**`vendor-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 供应商 ID

**`x-vga`\=`<boolean>` (*默认值 \=* `0`)**

启用 vfio-vga 设备支持。

**`hotplug`: `<string>` (*默认值 \=* `network,disk,usb`)**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：*network*、*disk*、*cpu*、*memory*、*usb* 和 *cloudinit*。使用 *0* 完全禁用热插拔。将 *1* 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`hugepages`: `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 *any*，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`ide[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。

**`aio`\=`<io_uring | native | threads>`**

要使用的 AIO 类型。

**`backup`\=`<boolean>`**

备份时是否应包含该驱动器。

**`bps`\=`<bps>`**

最大读写速度，单位为字节/秒。

**`bps_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`bps_rd`\=`<bps>`**

最大读取速度，单位为字节/秒。

**`bps_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`bps_wr`\=`<bps>`**

最大写入速度，单位为字节/秒。

**`bps_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

驱动器的缓存模式

**`detect_zeroes`\=`<boolean>`**

控制是否检测并尝试优化零值写入。

**`discard`\=`<ignore | on>`**

控制是否将 discard/trim 请求传递给底层存储。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

驱动器后端文件的数据格式。

**`iops`\=`<iops>`**

每秒最大读写 I/O 操作数。

**`iops_max`\=`<iops>`**

最大未限速读写 I/O 池，单位为每秒操作数。

**`iops_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`iops_rd`\=`<iops>`**

每秒最大读取 I/O 操作数。

**`iops_rd_max`\=`<iops>`**

最大未限速读取 I/O 池，单位为每秒操作数。

**`iops_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`iops_wr`\=`<iops>`**

每秒最大写入 I/O 操作数。

**`iops_wr_max`\=`<iops>`**

最大未限速写入 I/O 池，单位为每秒操作数。

**`iops_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`mbps`\=`<mbps>`**

最大读写速度，单位为 MB/秒。

**`mbps_max`\=`<mbps>`**

最大未限速读写池，单位为 MB/秒。

**`mbps_rd`\=`<mbps>`**

最大读取速度，单位为 MB/秒。

**`mbps_rd_max`\=`<mbps>`**

最大未限速读取池，单位为 MB/秒。

**`mbps_wr`\=`<mbps>`**

最大写入速度，单位为 MB/秒。

**`mbps_wr_max`\=`<mbps>`**

最大未限速写入池，单位为 MB/秒。

**`media`\=`<cdrom | disk>` (*默认值 \=* `disk`)**

驱动器的介质类型。

**`model`\=`<model>`**

驱动器报告的型号名称，采用 URL 编码，最长 40 字节。

**`replicate`\=`<boolean>`（*默认 \=* `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（*默认 \=* `0`）**

将此本地管理的卷标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享卷，而是假定该卷已经共享！
{% endhint %}

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`snapshot`\=`<boolean>`**

控制 qemu 的快照模式功能。激活后，对磁盘所做的更改是临时的，并将在虚拟机关机时丢弃。

**`ssd`\=`<boolean>`**

是否将此驱动器呈现为 SSD，而非旋转式硬盘。

**`werror`\=`<enospc | ignore | report | stop>`**

写入错误时的操作。

**`wwn`\=`<wwn>`**

驱动器的全球唯一名称，编码为 16 字节十六进制字符串，以 *0x* 为前缀。

**`intel-tdx`: `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`attestation`\=`<boolean>` (*默认值 \=* `1`)**

通过包含 quote-generation-socket 启用 TDX 证明

**`type`\=`<tdx-type>`**

启用 TDX

**`vsock-cid`\=`<integer> (2 - N)` (*默认值 \=* `2`)**

Quote Generation Service 的 vsock CID

**`vsock-port`\=`<integer> (0 - N)` (*默认值 \=* `4050`)**

Quote Generation Service 的 vsock 端口

**`ipconfig[n]`: `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 *dhcp* 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 *auto* 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`gw`\=`<GatewayIPv4>`**

IPv4 流量的默认网关。

{% hint style="info" %}
需要选项：`ip`
{% endhint %}

**`gw6`\=`<GatewayIPv6>`**

IPv6 流量的默认网关。

{% hint style="info" %}
需要选项：`ip6`
{% endhint %}

**`ip`\=`<IPv4Format/CIDR>`（*默认值 \=* `dhcp`）**

CIDR 格式的 IPv4 地址。

**`ip6`\=`<IPv6Format/CIDR>`（*默认值 \=* `dhcp`）**

CIDR 格式的 IPv6 地址。

**`ivshmem`: `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`name`\=`<string>`**

文件名。将以 *pve-shm-* 为前缀。默认为 VMID。该文件将在虚拟机停止时删除。

**`size`\=`<integer> (1 - N)`**

文件大小，单位为 MB。

**`keephugepages`: `<boolean>` (*default \=* `0`)**

Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts.

**`keyboard`: `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

Keyboard layout for VNC server. This option is generally not required and is often better handled from within the guest OS.

**`kvm`: `<boolean>` (*default \=* `1`)**

Enable/disable KVM hardware virtualization.

**`localtime`: `<boolean>`**

Set the real time clock (RTC) to local time. This is enabled by default if the `ostype` indicates a Microsoft Windows OS.

**`lock`: `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

Lock/unlock the VM.

**`machine`: `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`aw-bits`\=`<number> (32 - 64)`**

Specifies the vIOMMU address space bit width.

Intel vIOMMU supports a bit width of either 39 or 48 bits and VirtIO vIOMMU supports any bit width between 32 and 64 bits.

**`enable-s3`\=`<boolean>`**

Enables S3 power state. Defaults to false beginning with machine types 9.2\+pve1, true before.

**`enable-s4`\=`<boolean>`**

Enables S4 power state. Defaults to false beginning with machine types 9.2\+pve1, true before.

**`type`\=`<machine type>`**

Specifies the QEMU machine type.

**`viommu`\=`<intel | virtio>`**

Enable and set guest vIOMMU variant (Intel vIOMMU needs q35 to be set as machine type).

**`memory`: `[current=]<integer>`**

Memory properties.

**`current`\=`<integer> (16 - N)` (*default \=* `512`)**

Current amount of online RAM for the VM in MiB. This is the maximum available memory when you use the balloon device.

**`migrate_downtime`: `<number> (0 - N)` (*default \=* `0.1`)**

Set maximum tolerated downtime (in seconds) for migrations. Should the migration not be able to converge in the very end, because too much newly dirtied RAM needs to be transferred, the limit will be increased automatically step-by-step until migration can converge. Will be capped to 2000 seconds (maximum in QEMU).

**`migrate_speed`: `<integer> (0 - N)` (*default \=* `0`)**

Set maximum speed (in MB/s) for migrations. Value 0 is no limit.

**`name`: `<string>`**

Set a name for the VM. Only used on the configuration web interface.

**`nameserver`: `<string>`**

cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`net[n]`: `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

Specify network devices.

**`bridge`\=`<bridge>`**

Bridge to attach the network device to. The Proxmox VE standard bridge is called *vmbr0*.

If you do not specify a bridge, we create a kvm user (NATed) network device, which provides DHCP and DNS services. The following addresses are used:

```text
10.0.2.2   Gateway
10.0.2.3   DNS Server
10.0.2.4   SMB Server
```

The DHCP server assign addresses to the guest starting from 10.0.2.15.

**`firewall`\=`<boolean>`**

Whether this interface should be protected by the firewall.

**`host-tunnel`\=`<boolean>`**

Enable host GSO over UDP tunnel offload (VirtIO only). Requires QEMU \> 10.2 and guest and host kernel support. Disabled by default starting with machine version 11.0\+pve1 to work around an issue with the virtio-net driver in guest kernels. With machine versions 10.2 and 11.0, this is enabled by default.

**`link_down`\=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`macaddr`\=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`model`\=`<e1000 | e1000-82540em | e1000-82544gc | e1000-82545em | e1000e | i82551 | i82557b | i82559er | ne2k_isa | ne2k_pci | pcnet | rtl8139 | virtio | vmxnet3>`**

Network Card Model. The *virtio* model provides the best performance with very low CPU overhead. If your guest does not support this driver, it is usually best to use *e1000*.

**`mtu`\=`<integer> (1 - 65520)`**

Force MTU of network device (VirtIO only). Setting to *1* or empty will use the bridge MTU

**`queues`\=`<integer> (0 - 64)`**

Number of packet queues to be used on the device.

**`rate`\=`<number> (0 - N)`**

Rate limit in mbps (megabytes per second) as floating point number.

**`tag`\=`<integer> (1 - 4094)`**

VLAN tag to apply to packets on this interface.

**`trunks`\=`<vlanid[;vlanid...]>`**

VLAN trunks to pass through this interface.

**`numa`: `<boolean>` (*default \=* `0`)**

Enable/disable NUMA.

**`numa[n]`: `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA topology.

**`cpus`\=`<id[-id];...>`**

CPUs accessing this NUMA node.

**`hostnodes`\=`<id[-id];...>`**

Host NUMA nodes to use.

**`memory`\=`<number>`**

Amount of memory this NUMA node provides.

**`policy`\=`<bind | interleave | preferred>`**

NUMA allocation policy.

**`onboot`: `<boolean>` (*默认 \=* `0`)**

Specifies whether a VM will be started during system bootup.

**`ostype`: `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` (*default \=* `other`)**

Specify guest operating system. This is used to enable special optimization/features for specific operating systems:

<table>
<tr>
<td>other <br/></td>
<td>
<p>unspecified OS</p>
</td>
</tr>
<tr>
<td>wxp <br/></td>
<td>
<p>Microsoft Windows XP</p>
</td>
</tr>
<tr>
<td>
w2k
<br/>
</td>
<td>
<p>Microsoft Windows 2000</p>
</td>
</tr>
<tr>
<td>
w2k3
<br/>
</td>
<td>
<p>Microsoft Windows 2003</p>
</td>
</tr>
<tr>
<td>
w2k8
<br/>
</td>
<td>
<p>Microsoft Windows 2008</p>
</td>
</tr>
<tr>
<td>wvista <br/></td>
<td>
<p>Microsoft Windows Vista</p>
</td>
</tr>
<tr>
<td>win7 <br/></td>
<td>
<p>Microsoft Windows 7</p>
</td>
</tr>
<tr>
<td>win8 <br/></td>
<td>
<p>Microsoft Windows 8/2012/2012r2</p>
</td>
</tr>
<tr>
<td>win10 <br/></td>
<td>
<p>Microsoft Windows 10/2016/2019</p>
</td>
</tr>
<tr>
<td>win11 <br/></td>
<td>
<p>Microsoft Windows 11/2022/2025</p>
</td>
</tr>
<tr>
<td>
l24
<br/>
</td>
<td>
<p>Linux 2.4 Kernel</p>
</td>
</tr>
<tr>
<td>
l26
<br/>
</td>
<td>
<p>Linux 2.6 - 7.X Kernel</p>
</td>
</tr>
<tr>
<td>solaris <br/></td>
<td>
<p>Solaris/OpenSolaris/OpenIndiania kernel</p>
</td>
</tr>
</table>

**`parallel[n]`: `/dev/parport\d+|/dev/usb/lp\d+`**

Map host parallel devices (n is 0 to 2).

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

{% hint style="danger" %}
实验性功能！有用户报告此选项存在问题。
{% endhint %}

**`protection`: `<boolean>` (*默认 \=* `0`)**

Sets the protection flag of the VM. This will disable the remove VM and remove disk operations.

**`reboot`: `<boolean>` (*default \=* `1`)**

Allow reboot. If set to *0* the VM exit on reboot.

**`rng0`: `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

Configure a VirtIO-based Random Number Generator.

**`max_bytes`\=`<integer>` (*default \=* `1024`)**

Maximum bytes of entropy allowed to get injected into the guest every *period* milliseconds. Use `0` to disable limiting (potentially dangerous!).

**`period`\=`<integer>` (*default \=* `1000`)**

Every *period* milliseconds the entropy-injection quota is reset, allowing the guest to retrieve another *max\_bytes* of entropy.

**`source`\=`</dev/hwrng | /dev/random | /dev/urandom>`**

The file on the host to gather entropy from. Using urandom does **not** decrease security in any meaningful way, as it’s still seeded from real entropy, and the bytes provided will most likely be mixed with real entropy on the guest as well. */dev/hwrng* can be used to pass through a hardware RNG from the host.

**`sata[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SATA hard disk or CD-ROM (n is 0 to 5).

**`aio`\=`<io_uring | native | threads>`**

要使用的 AIO 类型。

**`backup`\=`<boolean>`**

备份时是否应包含该驱动器。

**`bps`\=`<bps>`**

最大读写速度，单位为字节/秒。

**`bps_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`bps_rd`\=`<bps>`**

最大读取速度，单位为字节/秒。

**`bps_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`bps_wr`\=`<bps>`**

最大写入速度，单位为字节/秒。

**`bps_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

驱动器的缓存模式

**`detect_zeroes`\=`<boolean>`**

控制是否检测并尝试优化零值写入。

**`discard`\=`<ignore | on>`**

控制是否将 discard/trim 请求传递给底层存储。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

驱动器后端文件的数据格式。

**`iops`\=`<iops>`**

每秒最大读写 I/O 操作数。

**`iops_max`\=`<iops>`**

最大未限速读写 I/O 池，单位为每秒操作数。

**`iops_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`iops_rd`\=`<iops>`**

每秒最大读取 I/O 操作数。

**`iops_rd_max`\=`<iops>`**

最大未限速读取 I/O 池，单位为每秒操作数。

**`iops_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`iops_wr`\=`<iops>`**

每秒最大写入 I/O 操作数。

**`iops_wr_max`\=`<iops>`**

最大未限速写入 I/O 池，单位为每秒操作数。

**`iops_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`mbps`\=`<mbps>`**

最大读写速度，单位为 MB/秒。

**`mbps_max`\=`<mbps>`**

最大未限速读写池，单位为 MB/秒。

**`mbps_rd`\=`<mbps>`**

最大读取速度，单位为 MB/秒。

**`mbps_rd_max`\=`<mbps>`**

最大未限速读取池，单位为 MB/秒。

**`mbps_wr`\=`<mbps>`**

最大写入速度，单位为 MB/秒。

**`mbps_wr_max`\=`<mbps>`**

最大未限速写入池，单位为 MB/秒。

**`media`\=`<cdrom | disk>` (*默认值 \=* `disk`)**

驱动器的介质类型。

**`replicate`\=`<boolean>`（*默认 \=* `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（*默认 \=* `0`）**

将此本地管理的卷标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享卷，而是假定该卷已经共享！
{% endhint %}

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`snapshot`\=`<boolean>`**

控制 qemu 的快照模式功能。激活后，对磁盘所做的更改是临时的，并将在虚拟机关机时丢弃。

**`ssd`\=`<boolean>`**

是否将此驱动器呈现为 SSD，而非旋转式硬盘。

**`werror`\=`<enospc | ignore | report | stop>`**

写入错误时的操作。

**`wwn`\=`<wwn>`**

驱动器的全球唯一名称，编码为 16 字节十六进制字符串，以 *0x* 为前缀。

**`scsi[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SCSI hard disk or CD-ROM (n is 0 to 30).

**`aio`\=`<io_uring | native | threads>`**

要使用的 AIO 类型。

**`backup`\=`<boolean>`**

备份时是否应包含该驱动器。

**`bps`\=`<bps>`**

最大读写速度，单位为字节/秒。

**`bps_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`bps_rd`\=`<bps>`**

最大读取速度，单位为字节/秒。

**`bps_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`bps_wr`\=`<bps>`**

最大写入速度，单位为字节/秒。

**`bps_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

驱动器的缓存模式

**`detect_zeroes`\=`<boolean>`**

控制是否检测并尝试优化零值写入。

**`discard`\=`<ignore | on>`**

控制是否将 discard/trim 请求传递给底层存储。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

驱动器后端文件的数据格式。

**`iops`\=`<iops>`**

每秒最大读写 I/O 操作数。

**`iops_max`\=`<iops>`**

最大未限速读写 I/O 池，单位为每秒操作数。

**`iops_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`iops_rd`\=`<iops>`**

每秒最大读取 I/O 操作数。

**`iops_rd_max`\=`<iops>`**

最大未限速读取 I/O 池，单位为每秒操作数。

**`iops_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`iops_wr`\=`<iops>`**

每秒最大写入 I/O 操作数。

**`iops_wr_max`\=`<iops>`**

最大未限速写入 I/O 池，单位为每秒操作数。

**`iops_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`iothread`\=`<boolean>`**

Whether to use iothreads for this drive

**`mbps`\=`<mbps>`**

最大读写速度，单位为 MB/秒。

**`mbps_max`\=`<mbps>`**

最大未限速读写池，单位为 MB/秒。

**`mbps_rd`\=`<mbps>`**

最大读取速度，单位为 MB/秒。

**`mbps_rd_max`\=`<mbps>`**

最大未限速读取池，单位为 MB/秒。

**`mbps_wr`\=`<mbps>`**

最大写入速度，单位为 MB/秒。

**`mbps_wr_max`\=`<mbps>`**

最大未限速写入池，单位为 MB/秒。

**`media`\=`<cdrom | disk>` (*默认值 \=* `disk`)**

驱动器的介质类型。

**`product`\=`<product>`**

The drive’s product name, up to 16 bytes long.

**`queues`\=`<integer> (2 - N)`**

Number of queues.

**`replicate`\=`<boolean>`（*默认 \=* `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`ro`\=`<boolean>`**

Whether the drive is read-only.

**`scsiblock`\=`<boolean>` (*default \=* `0`)**

whether to use scsi-block for full passthrough of host block device

{% hint style="warning" %}
can lead to I/O errors in combination with low memory or high memory fragmentation on host
{% endhint %}

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（*默认 \=* `0`）**

将此本地管理的卷标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享卷，而是假定该卷已经共享！
{% endhint %}

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`snapshot`\=`<boolean>`**

控制 qemu 的快照模式功能。激活后，对磁盘所做的更改是临时的，并将在虚拟机关机时丢弃。

**`ssd`\=`<boolean>`**

是否将此驱动器呈现为 SSD，而非旋转式硬盘。

**`vendor`\=`<vendor>`**

The drive’s vendor name, up to 8 bytes long.

**`werror`\=`<enospc | ignore | report | stop>`**

写入错误时的操作。

**`wwn`\=`<wwn>`**

驱动器的全球唯一名称，编码为 16 字节十六进制字符串，以 *0x* 为前缀。

**`scsihw`: `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` (*default \=* `lsi`)**

SCSI controller model

**`searchdomain`: `<string>`**

cloud-init: Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`serial[n]`: `(/dev/[^,]+|socket)`**

Create a serial device inside the VM (n is 0 to 3), and pass through a host serial device (i.e. /dev/ttyS0), or create a unix socket on the host side (use *qm terminal* to open a terminal connection).

{% hint style="info" %}
If you pass through a host serial device, it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

{% hint style="danger" %}
实验性功能！有用户报告此选项存在问题。
{% endhint %}

**`shares`: `<integer> (0 - 50000)` (*default \=* `1000`)**

Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd.

**`smbios1`: `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

Specify SMBIOS type 1 fields.

**`base64`\=`<boolean>`**

Flag to indicate that the SMBIOS values are base64 encoded

**`family`\=`<Base64 encoded string>`**

Set SMBIOS1 family string.

**`manufacturer`\=`<Base64 encoded string>`**

Set SMBIOS1 manufacturer.

**`product`\=`<Base64 encoded string>`**

Set SMBIOS1 product ID.

**`serial`\=`<Base64 encoded string>`**

Set SMBIOS1 serial number.

**`sku`\=`<Base64 encoded string>`**

Set SMBIOS1 SKU string.

**`uuid`\=`<UUID>`**

Set SMBIOS1 UUID.

**`version`\=`<Base64 encoded string>`**

Set SMBIOS1 version.

**`smp`: `<integer> (1 - N)` (*default \=* `1`)**

The number of CPUs. Please use option -sockets instead.

**`sockets`: `<integer> (1 - N)` (*default \=* `1`)**

The number of CPU sockets.

**`spice_enhancements`: `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

Configure additional enhancements for SPICE.

**`foldersharing`\=`<boolean>` (*default \=* `0`)**

Enable folder sharing via SPICE. Needs Spice-WebDAV daemon installed in the VM.

**`videostreaming`\=`<all | filter | off>` (*default \=* `off`)**

Enable video streaming. Uses compression for detected video streams.

**`sshkeys`: `<string>`**

cloud-init: Setup public SSH keys (one key per line, OpenSSH format).

**`startdate`: `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` (*default \=* `now`)**

Set the initial date of the real time clock. Valid format for date are:'now' or *2006-06-17T16:01:21* or *2006-06-17*.

**`startup`: \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`tablet`: `<boolean>` (*default \=* `1`)**

Enable/disable the USB tablet device. This device is usually needed to allow absolute mouse positioning with VNC. Else the mouse runs out of sync with normal VNC clients. If you’re running lots of console-only guests on one host, you may consider disabling this to save some context switches. This is turned off by default if you use spice (`qm set <vmid> --vga qxl`).

**`tags`: `<string>`**

Tags of the VM. This is only meta information.

**`tdf`: `<boolean>` (*default \=* `0`)**

Enable/disable time drift fix.

**`template`: `<boolean>` (*默认 \=* `0`)**

启用/禁用模板。

**`tpmstate0`: `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

Configure a Disk for storing TPM state. The format is fixed to *raw*.

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<qcow2 | raw | vmdk>`**

Format of the image.

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`version`\=`<v1.2 | v2.0>` (*default \=* `v1.2`)**

The TPM interface version. v2.0 is newer and should be preferred. Note that this cannot be changed later on.

**`unused[n]`: `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`file`\=`<volume>`**

驱动器的后端卷。

**`usb[n]`: `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

Configure an USB device (n is 0 to 4, for machine version \>\= 7.1 and ostype l26 or windows \> 7, n can be up to 14).

**`host`\=`<HOSTUSBDEVICE|spice>`**

The Host USB device or port or the value *spice*. HOSTUSBDEVICE syntax is:

```text
'bus-port(.port)*' (decimal numbers) or
'vendor_id:product_id' (hexadecimal numbers) or
'spice'
```

You can use the *lsusb -t* command to list existing usb devices.

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

The value *spice* can be used to add a usb redirection devices for spice.

必须设置此项或 *mapping* 键。

**`mapping`\=`<mapping-id>`**

集群范围映射的 ID。必须设置此项或默认键 *host*。

**`usb3`\=`<boolean>` (*default \=* `0`)**

Specifies whether if given host option is a USB3 device or port. For modern guests (machine version \>\= 7.1 and ostype l26 and windows \> 7), this flag is irrelevant (all devices are plugged into a xhci controller).

**`vcpus`: `<integer> (1 - N)` (*default \=* `0`)**

Number of hotplugged vcpus.

**`vga`: `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

Configure the VGA Hardware. If you want to use high resolution modes (\>\= 1280x1024x16) you may need to increase the vga memory option. Since QEMU 2.9 the default VGA display type is *std* for all OS types besides some Windows versions (XP and older) which use *cirrus*. The *qxl* option enables the SPICE display server. For win\* OS you can select how many independent displays you want, Linux guests can add displays them self. You can also run without any graphic card, using a serial device as terminal.

**`clipboard`\=`<vnc>`**

Enable a specific clipboard. If not set, depending on the display type the SPICE one will be added. Live migration with a VNC clipboard is not possible with QEMU machine version \< 10.1.

**`memory`\=`<integer> (4 - 512)`**

Sets the VGA memory (in MiB). Has no effect with serial display.

**`type`\=`<cirrus | none | qxl | qxl2 | qxl3 | qxl4 | serial0 | serial1 | serial2 | serial3 | std | virtio | virtio-gl | vmware>` (*default \=* `std`)**

Select the VGA type. Using type *cirrus* is not recommended.

**`virtio[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

Use volume as VIRTIO hard disk (n is 0 to 15).

**`aio`\=`<io_uring | native | threads>`**

要使用的 AIO 类型。

**`backup`\=`<boolean>`**

备份时是否应包含该驱动器。

**`bps`\=`<bps>`**

最大读写速度，单位为字节/秒。

**`bps_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`bps_rd`\=`<bps>`**

最大读取速度，单位为字节/秒。

**`bps_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`bps_wr`\=`<bps>`**

最大写入速度，单位为字节/秒。

**`bps_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

驱动器的缓存模式

**`detect_zeroes`\=`<boolean>`**

控制是否检测并尝试优化零值写入。

**`discard`\=`<ignore | on>`**

控制是否将 discard/trim 请求传递给底层存储。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

驱动器后端文件的数据格式。

**`iops`\=`<iops>`**

每秒最大读写 I/O 操作数。

**`iops_max`\=`<iops>`**

最大未限速读写 I/O 池，单位为每秒操作数。

**`iops_max_length`\=`<seconds>`**

I/O 突发的最大持续时间，单位为秒。

**`iops_rd`\=`<iops>`**

每秒最大读取 I/O 操作数。

**`iops_rd_max`\=`<iops>`**

最大未限速读取 I/O 池，单位为每秒操作数。

**`iops_rd_max_length`\=`<seconds>`**

读取 I/O 突发的最大持续时间，单位为秒。

**`iops_wr`\=`<iops>`**

每秒最大写入 I/O 操作数。

**`iops_wr_max`\=`<iops>`**

最大未限速写入 I/O 池，单位为每秒操作数。

**`iops_wr_max_length`\=`<seconds>`**

写入 I/O 突发的最大持续时间，单位为秒。

**`iothread`\=`<boolean>`**

Whether to use iothreads for this drive

**`mbps`\=`<mbps>`**

最大读写速度，单位为 MB/秒。

**`mbps_max`\=`<mbps>`**

最大未限速读写池，单位为 MB/秒。

**`mbps_rd`\=`<mbps>`**

最大读取速度，单位为 MB/秒。

**`mbps_rd_max`\=`<mbps>`**

最大未限速读取池，单位为 MB/秒。

**`mbps_wr`\=`<mbps>`**

最大写入速度，单位为 MB/秒。

**`mbps_wr_max`\=`<mbps>`**

最大未限速写入池，单位为 MB/秒。

**`media`\=`<cdrom | disk>` (*默认值 \=* `disk`)**

驱动器的介质类型。

**`replicate`\=`<boolean>`（*默认 \=* `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`ro`\=`<boolean>`**

Whether the drive is read-only.

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（*默认 \=* `0`）**

将此本地管理的卷标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享卷，而是假定该卷已经共享！
{% endhint %}

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`snapshot`\=`<boolean>`**

控制 qemu 的快照模式功能。激活后，对磁盘所做的更改是临时的，并将在虚拟机关机时丢弃。

**`werror`\=`<enospc | ignore | report | stop>`**

写入错误时的操作。

**`virtiofs[n]`: `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

Configuration for sharing a directory between host and guest using Virtio-fs.

**`cache`\=`<always | auto | metadata | never>` (*default \=* `auto`)**

The caching policy the file system should use (auto, always, metadata, never).

**`direct-io`\=`<boolean>` (*default \=* `0`)**

Honor the O\_DIRECT flag passed down by guest applications.

**`dirid`\=`<mapping-id>`**

Mapping identifier of the directory mapping to be shared with the guest. Also used as a mount tag inside the VM.

**`expose-acl`\=`<boolean>` (*default \=* `0`)**

Enable support for POSIX ACLs (enabled ACL implies xattr) for this mount.

**`expose-xattr`\=`<boolean>` (*default \=* `0`)**

Enable support for extended attributes for this mount.

**`vmgenid`: `<UUID>` (*default \=* `1 (autogenerated)`)**

The VM generation ID (vmgenid) device exposes a 128-bit integer value identifier to the guest OS. This allows to notify the guest operating system when the virtual machine is executed with a different configuration (e.g. snapshot execution or creation from a template). The guest operating system notices the change, and is then able to react as appropriate by marking its copies of distributed databases as dirty, re-initializing its random number generator, etc. Note that auto-creation only works when done through API/CLI create or update methods, but not when manually editing the config file.

**`vmstatestorage`: `<storage ID>`**

Default storage for VM state volumes/files.

**`watchdog`: `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the watchdog will reset the guest (or execute the respective action specified)

**`action`\=`<debug | none | pause | poweroff | reset | shutdown>`**

The action to perform if after activation the guest fails to poll the watchdog in time.

**`model`\=`<i6300esb | ib700>` (*default \=* `i6300esb`)**

Watchdog type to emulate.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
