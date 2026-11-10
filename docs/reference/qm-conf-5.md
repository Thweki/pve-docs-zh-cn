# qm.conf(5)

## 名称 <a href="#name" id="name"></a>

qm.conf \- Proxmox VE 虚拟机配置

## 概要 <a href="#synopsis" id="synopsis"></a>

<em>/etc/pve/qemu-server/\<VMID\>.conf</em>

## 描述 <a href="#description" id="description"></a>

`/etc/pve/qemu-server/<VMID>.conf` 文件保存虚拟机配置，其中“VMID”是给定虚拟机的数字 ID。

{% hint style="info" %}
ID \< 100 保留供内部使用。
{% endhint %}

## 文件格式 <a href="#file_format" id="file_format"></a>

该文件采用简单的冒号分隔键/值格式。每行的格式如下：

```text
OPTION: value
```

文件中的空白行会被忽略，以 `#` 字符开头的行会被视为注释，同样会被忽略。

可以使用 `qm` 命令生成和修改这些文件。

## 选项 <a href="#options" id="options"></a>

**`acpi`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用/禁用 ACPI。

**`affinity`: `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`agent`: `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`enabled`\=`<boolean>`（<em>默认值 \=</em> `0`）**

启用/禁用与 VM 中运行的 QEMU Guest Agent（QGA）的通信。

**`freeze-fs`\=`<boolean>`（<em>默认值 \=</em> `1`）**

是否发出 guest-fsfreeze-freeze 和 guest-fsfreeze-thaw QEMU 客户机代理命令。当客户机配置中启用了 QEMU Guest Agent 选项且代理正在客户机内运行时，快照模式备份、克隆、不含 RAM 的快照、从正在运行的客户机导入磁盘以及复制，通常会发出 guest-fsfreeze-freeze 和相应的 thaw 命令。

已弃用的 <em>freeze-fs-on-backup</em> 设置被视为此设置的别名。

**`fstrim_cloned_disks`\=`<boolean>`（<em>默认值 \=</em> `0`）**

移动磁盘或迁移 VM 后运行 fstrim。

**`type`\=`<isa | virtio>`（<em>默认值 \=</em> `virtio`）**

选择代理类型

**`allow-ksm`：`<boolean>`（<em>默认值 \=</em> `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`amd-sev`: `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`allow-smt`\=`<boolean>`（<em>默认值 \=</em> `1`）**

设置策略位以允许同时多线程（SMT）（除非针对 SEV-SNP，否则会被忽略）

**`kernel-hashes`\=`<boolean>`（<em>默认值 \=</em> `0`）**

将内核哈希添加到客户机固件，以实现可度量的 Linux 内核启动

**`no-debug`\=`<boolean>`（<em>默认值 \=</em> `0`）**

设置策略位以禁止调试客户机

**`no-key-sharing`\=`<boolean>`（<em>默认值 \=</em> `0`）**

设置策略位以禁止与其他客户机共享密钥（对于 SEV-SNP 会被忽略）

**`type`\=`<sev-type>`**

使用 type\=<em>std</em> 启用标准 SEV，或使用 <em>es</em> 选项启用实验性 SEV-ES，或使用 <em>snp</em> 选项启用实验性 SEV-SNP。

**`arch`: `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`args`: `<string>`**

传递给 kvm 的任意参数，例如：

args: -no-reboot -smbios <em>type\=0,vendor\=FOO</em>

{% hint style="info" %}
此选项仅供专家使用。
{% endhint %}

**`audio0`: `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`device`\=`<AC97 | ich9-intel-hda | intel-hda>`**

配置音频设备。

**`driver`\=`<none | spice>`（<em>默认值 \=</em> `spice`）**

音频设备的驱动程序后端。

**`autostart`：`<boolean>`（<em>默认值 \=</em> `0`）**

崩溃后自动重启（目前被忽略）。

**`balloon`: `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`bios`：`<ovmf | seabios>`（<em>默认值 \=</em> `seabios`）**

选择 BIOS 实现。

**`boot`: `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 <em>order\=</em> 子属性，因为不带键的用法或 <em>legacy\=</em> 已弃用。

**`legacy`\=`<[acdn]{1,4}>`（<em>默认值 \=</em> `cdn`）**

从软盘（a）、硬盘（c）、CD-ROM（d）或网络（n）启动。已弃用，请改用 <em>order\=</em>。

**`order`\=`<device[;device...]>`**

客户机将尝试按照此处列出的顺序从设备启动。

磁盘、光驱和直通的 USB 存储设备将直接用于启动，NIC 将加载 PXE，PCIe 设备则将表现得像磁盘（例如 NVMe），或者加载选项 ROM（例如 RAID 控制器、硬件 NIC）。

请注意，只有此列表中的设备才会被标记为可启动，并因此由客户机固件（BIOS/UEFI）加载。如果需要使用多个磁盘启动（例如软件 RAID），则需要在此处指定所有这些磁盘。

如果指定了此选项，将覆盖已弃用的 <em>legacy\=\[acdn\]\*</em> 值。

**`bootdisk`: `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 <em>boot: order\=foo;bar</em>。

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

**`ciupgrade`：`<boolean>`（<em>默认值 \=</em> `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`ciuser`: `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`cores`: `<integer> (1 - N)` (<em>默认值 \=</em> `1`)**

每个 CPU 插槽的核心数。

**`cpu`: `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`cputype`\=`<string>` (<em>默认值 \=</em> `kvm64`)**

模拟的 CPU 类型。可以是默认类型或自定义名称（自定义型号名称必须以 <em>custom-</em> 为前缀）。

**`flags`\=`<+FLAG[;-FLAG...]>`**

以 <em>;</em> 分隔的附加 CPU 标志列表。使用 <em>\+FLAG</em> 启用标志，使用 <em>-FLAG</em> 禁用标志。有一个特殊的 <em>nested-virt</em> 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 使用 <em>svm</em>，Intel 使用 <em>vmx</em>）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，VM 特定标志必须来自以下集合：aes、amd-no-ssb、amd-ssbd、hv-evmcs、hv-tlbflush、ibpb、md-clear、nested-virt、pcid、pdpe1gb、spec-ctrl、ssbd、virt-ssbd

**`guest-phys-bits`\=`<integer> (32 - 64)`**

客户机可用的物理地址位数。

**`hidden`\=`<boolean>` (<em>默认值 \=</em> `0`)**

不要标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。

**`hv-vendor-id`\=`<vendor-id>`**

Hyper-V 供应商 ID。Windows 客户机中的某些驱动程序或程序需要特定的 ID。

**`level`\=`<integer> (0 - 4294967295)`**

客户机可查询的基本 CPUID 叶的最大输入值——即供应商（叶 0）、系列/型号/步进及功能位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶将被隐藏。将此项设置为 <em>30</em>，是解决在较新的 Intel 宿主机上运行的 Windows 客户机出现 Hyper-V 启动故障的常用变通方法。仅当 vCPU 架构为 x86\_64 时适用。

**`phys-bits`\=`<8-64|host>`**

报告给客户机操作系统的物理内存地址位数。应小于或等于宿主机的位数。设置为 <em>host</em> 可使用宿主机 CPU 的值，但请注意，这样会导致无法在线迁移到该值不同的 CPU。

**`reported-model`\=`<486 | Broadwell | Broadwell-IBRS | Broadwell-noTSX | Broadwell-noTSX-IBRS | Cascadelake-Server | Cascadelake-Server-noTSX | Cascadelake-Server-v2 | Cascadelake-Server-v4 | Cascadelake-Server-v5 | ClearwaterForest | ClearwaterForest-v2 | ClearwaterForest-v3 | Conroe | Cooperlake | Cooperlake-v2 | DiamondRapids | EPYC | EPYC-Genoa | EPYC-Genoa-v2 | EPYC-IBPB | EPYC-Milan | EPYC-Milan-v2 | EPYC-Milan-v3 | EPYC-Rome | EPYC-Rome-v2 | EPYC-Rome-v3 | EPYC-Rome-v4 | EPYC-Rome-v5 | EPYC-Turin | EPYC-v3 | EPYC-v4 | EPYC-v5 | GraniteRapids | GraniteRapids-v2 | GraniteRapids-v3 | GraniteRapids-v4 | GraniteRapids-v5 | Haswell | Haswell-IBRS | Haswell-noTSX | Haswell-noTSX-IBRS | Icelake-Client | Icelake-Client-noTSX | Icelake-Server | Icelake-Server-noTSX | Icelake-Server-v3 | Icelake-Server-v4 | Icelake-Server-v5 | Icelake-Server-v6 | Icelake-Server-v7 | IvyBridge | IvyBridge-IBRS | KnightsMill | Nehalem | Nehalem-IBRS | Opteron_G1 | Opteron_G2 | Opteron_G3 | Opteron_G4 | Opteron_G5 | Penryn | SandyBridge | SandyBridge-IBRS | SapphireRapids | SapphireRapids-v2 | SapphireRapids-v3 | SapphireRapids-v4 | SapphireRapids-v5 | SapphireRapids-v6 | SierraForest | SierraForest-v2 | SierraForest-v3 | SierraForest-v4 | SierraForest-v5 | Skylake-Client | Skylake-Client-IBRS | Skylake-Client-noTSX-IBRS | Skylake-Client-v4 | Skylake-Server | Skylake-Server-IBRS | Skylake-Server-noTSX-IBRS | Skylake-Server-v4 | Skylake-Server-v5 | Westmere | Westmere-IBRS | a64fx | athlon | core2duo | coreduo | cortex-a35 | cortex-a53 | cortex-a55 | cortex-a57 | cortex-a710 | cortex-a72 | cortex-a76 | cortex-a78ae | host | kvm32 | kvm64 | max | neoverse-n1 | neoverse-n2 | neoverse-v1 | pentium | pentium2 | pentium3 | phenom | qemu32 | qemu64>` (<em>默认值 \=</em> `kvm64`)**

报告给客户机的 CPU 模型和供应商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效；默认模型始终会向客户机操作系统报告其自身。

**`cpulimit`: `<number> (0 - 128)` (<em>默认值 \=</em> `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总计为 <em>2</em>。值 <em>0</em> 表示不限制 CPU。
{% endhint %}

**`cpuunits`: `<integer> (1 - 262144)` (<em>默认值 \=</em> `cgroup v1: 1024, cgroup v2: 100`)**

虚拟机的 CPU 权重。该参数用于内核公平调度器。数值越大，此虚拟机获得的 CPU 时间就越多。该数值是相对于所有其他正在运行的虚拟机的权重而言的。

**`description`: `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`efidisk0`: `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。

**`efitype`\=`<2m | 4m>` (<em>默认值 \=</em> `2m`)**

OVMF EFI 变量的大小和类型。<em>4m</em> 较新且推荐使用，并且是安全启动所必需的。为保持向后兼容，如果未另行指定，则使用 <em>2m</em>。对于 arch\=aarch64 (ARM) 的虚拟机，此设置会被忽略。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

驱动器后端文件的数据格式。

**`ms-cert`\=`<2011 | 2023 | 2023k | 2023w>` (<em>默认值 \=</em> `2011`)**

信息性标记，指示 Proxmox VE 已注册的最新 Microsoft UEFI 证书的版本。值 <em>2023k</em> 表示包含 <em>Microsoft UEFI CA 2023</em>、<em>Windows UEFI CA 2023</em> 和 <em>Microsoft Corporation KEK 2K CA 2023</em> 证书。值 <em>2023</em> 和 <em>2023w</em> 已弃用，仅为兼容性保留。

**`pre-enrolled-keys`\=`<boolean>` (<em>默认值 \=</em> `0`)**

与 <em>efitype\=4m</em> 一起使用时，使用已注册特定发行版密钥和 Microsoft 标准密钥的 EFI 变量模板。请注意，这将默认启用安全启动，但仍可在虚拟机内将其关闭。

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`freeze`: `<boolean>`**

启动时冻结 CPU（使用 <em>c</em> 监视器命令开始执行）。

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

**`driver`\=`<keep | vfio>` (<em>默认值 \=</em> `vfio`)**

如果设置为 <em>keep</em>，设备既不会重置，也不会绑定到 <em>vfio-pci</em> 驱动程序。适用于已加载正确驱动程序的设备。

**`host`\=`<HOSTPCIID[;HOSTPCIID2...]>`**

宿主机 PCI 设备直通。宿主机 PCI 设备的 PCI ID，或宿主机的 PCI 虚拟功能列表。HOSTPCIID 语法为：

<em>bus:dev.func</em>（十六进制数字）

可以使用 <em>lspci</em> 命令列出现有 PCI 设备。

必须设置此项或 <em>mapping</em> 键。

**`legacy-igd`\=`<boolean>` (<em>默认值 \=</em> `0`)**

以传统 IGD 模式直通此设备，使其成为虚拟机中的主显卡和唯一显卡。需要 <em>pc-i440fx</em> 机器类型，并将 VGA 设置为 <em>none</em>。

**`mapping`\=`<mapping-id>`**

集群范围映射的 ID。必须设置此项或默认键 <em>host</em>。

**`mdev`\=`<string>`**

要使用的中介设备类型。虚拟机启动时将创建此类型的一个实例，并在虚拟机停止时清理该实例。

**`pcie`\=`<boolean>` (<em>默认值 \=</em> `0`)**

选择 PCI-express 总线（需要 <em>q35</em> 机器型号）。

**`rombar`\=`<boolean>` (<em>默认值 \=</em> `1`)**

指定设备的 ROM 是否在客户机的内存映射中可见。

**`romfile`\=`<string>`**

自定义 PCI 设备 ROM 文件名（必须位于 /usr/share/kvm/ 中）。

**`sub-device-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 子系统设备 ID

**`sub-vendor-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 子系统供应商 ID

**`vendor-id`\=`<hex id>`**

覆盖对客户机可见的 PCI 供应商 ID

**`x-vga`\=`<boolean>` (<em>默认值 \=</em> `0`)**

启用 vfio-vga 设备支持。

**`hotplug`: `<string>` (<em>默认值 \=</em> `network,disk,usb`)**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：<em>network</em>、<em>disk</em>、<em>cpu</em>、<em>memory</em>、<em>usb</em> 和 <em>cloudinit</em>。使用 <em>0</em> 完全禁用热插拔。将 <em>1</em> 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`hugepages`: `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 <em>any</em>，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

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

**`media`\=`<cdrom | disk>` (<em>默认值 \=</em> `disk`)**

驱动器的介质类型。

**`model`\=`<model>`**

驱动器报告的型号名称，采用 URL 编码，最长 40 字节。

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

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

驱动器的全球唯一名称，编码为 16 字节十六进制字符串，以 <em>0x</em> 为前缀。

**`intel-tdx`: `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`attestation`\=`<boolean>` (<em>默认值 \=</em> `1`)**

通过包含 quote-generation-socket 启用 TDX 证明

**`type`\=`<tdx-type>`**

启用 TDX

**`vsock-cid`\=`<integer> (2 - N)` (<em>默认值 \=</em> `2`)**

Quote Generation Service 的 vsock CID

**`vsock-port`\=`<integer> (0 - N)` (<em>默认值 \=</em> `4050`)**

Quote Generation Service 的 vsock 端口

**`ipconfig[n]`: `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 <em>dhcp</em> 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 <em>auto</em> 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

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

**`ip`\=`<IPv4Format/CIDR>`（<em>默认值 \=</em> `dhcp`）**

CIDR 格式的 IPv4 地址。

**`ip6`\=`<IPv6Format/CIDR>`（<em>默认值 \=</em> `dhcp`）**

CIDR 格式的 IPv6 地址。

**`ivshmem`: `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`name`\=`<string>`**

文件名。将以 <em>pve-shm-</em> 为前缀。默认为 VMID。该文件将在虚拟机停止时删除。

**`size`\=`<integer> (1 - N)`**

文件大小，单位为 MB。

**`keephugepages`：`<boolean>`（<em>默认值 \=</em> `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`keyboard`: `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`kvm`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用/禁用 KVM 硬件虚拟化。

**`localtime`: `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`lock`: `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`machine`: `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`aw-bits`\=`<number> (32 - 64)`**

指定 vIOMMU 地址空间的位宽。

Intel vIOMMU 支持 39 或 48 位的位宽，VirtIO vIOMMU 支持 32 至 64 位之间的任意位宽。

**`enable-s3`\=`<boolean>`**

启用 S3 电源状态。从机型 9.2\+pve1 开始默认为 false，之前为 true。

**`enable-s4`\=`<boolean>`**

启用 S4 电源状态。从机型 9.2\+pve1 开始默认为 false，之前为 true。

**`type`\=`<machine type>`**

指定 QEMU 机型。

**`viommu`\=`<intel | virtio>`**

启用并设置客户机 vIOMMU 变体（Intel vIOMMU 需要将机型设为 q35）。

**`memory`: `[current=]<integer>`**

内存属性。

**`current`\=`<integer> (16 - N)`（<em>默认值 \=</em> `512`）**

虚拟机当前在线 RAM 容量，单位为 MiB。使用气球设备时，这是最大可用内存。

**`migrate_downtime`：`<number> (0 - N)`（<em>默认值 \=</em> `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`migrate_speed`：`<integer> (0 - N)`（<em>默认值 \=</em> `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`name`: `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`nameserver`: `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`net[n]`: `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`bridge`\=`<bridge>`**

网络设备要连接的网桥。Proxmox VE 的标准网桥名为 <em>vmbr0</em>。

如果未指定网桥，将创建提供 DHCP 和 DNS 服务的 kvm 用户网络设备（使用 NAT）。使用以下地址：

```text
10.0.2.2   Gateway
10.0.2.3   DNS Server
10.0.2.4   SMB Server
```

DHCP 服务器从 10.0.2.15 开始向客户机分配地址。

**`firewall`\=`<boolean>`**

是否使用防火墙保护此接口。

**`host-tunnel`\=`<boolean>`**

启用宿主机 UDP 隧道 GSO 卸载（仅限 VirtIO）。需要 QEMU \> 10.2 及客户机和宿主机内核支持。从机型版本 11.0\+pve1 开始默认禁用，以规避客户机内核中 virtio-net 驱动的问题。机型版本 10.2 和 11.0 默认启用此功能。

**`link_down`\=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`macaddr`\=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`model`\=`<e1000 | e1000-82540em | e1000-82544gc | e1000-82545em | e1000e | i82551 | i82557b | i82559er | ne2k_isa | ne2k_pci | pcnet | rtl8139 | virtio | vmxnet3>`**

网卡型号。<em>virtio</em> 型号以极低的 CPU 开销提供最佳性能。如果客户机不支持此驱动，通常最好使用 <em>e1000</em>。

**`mtu`\=`<integer> (1 - 65520)`**

强制设置网络设备的 MTU（仅限 VirtIO）。设为 <em>1</em> 或留空将使用网桥的 MTU

**`queues`\=`<integer> (0 - 64)`**

设备使用的数据包队列数量。

**`rate`\=`<number> (0 - N)`**

以 mbps（兆字节每秒）为单位的浮点数速率限制。

**`tag`\=`<integer> (1 - 4094)`**

要应用于此接口数据包的 VLAN 标签。

**`trunks`\=`<vlanid[;vlanid...]>`**

允许通过此接口的 VLAN 中继。

**`numa`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用/禁用 NUMA。

**`numa[n]`: `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`cpus`\=`<id[-id];...>`**

访问此 NUMA 节点的 CPU。

**`hostnodes`\=`<id[-id];...>`**

要使用的宿主机 NUMA 节点。

**`memory`\=`<number>`**

此 NUMA 节点提供的内存容量。

**`policy`\=`<bind | interleave | preferred>`**

NUMA 分配策略。

**`onboot`: `<boolean>` (<em>默认 \=</em> `0`)**

指定是否在系统启动时启动虚拟机。

**`ostype`：`<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>`（<em>默认值 \=</em> `other`）**

指定客户机操作系统。用于为特定操作系统启用特殊优化/功能：

<table>
<tr>
<td>other <br/></td>
<td>
<p>未指定的操作系统</p>
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
<p>Linux 2.4 内核</p>
</td>
</tr>
<tr>
<td>
l26
<br/>
</td>
<td>
<p>Linux 2.6 - 7.X 内核</p>
</td>
</tr>
<tr>
<td>solaris <br/></td>
<td>
<p>Solaris/OpenSolaris/OpenIndiania 内核</p>
</td>
</tr>
</table>

**`parallel[n]`: `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

{% hint style="info" %}
此选项允许直接访问宿主机硬件。因此此类虚拟机将无法迁移，请格外谨慎使用。
{% endhint %}

{% hint style="danger" %}
实验性功能！有用户报告此选项存在问题。
{% endhint %}

**`protection`: `<boolean>` (<em>默认 \=</em> `0`)**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`reboot`：`<boolean>`（<em>默认值 \=</em> `1`）**

允许重启。如果设为 <em>0</em>，虚拟机将在重启时退出。

**`rng0`: `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`max_bytes`\=`<integer>`（<em>默认值 \=</em> `1024`）**

每 <em>period</em> 毫秒允许注入客户机的最大熵字节数。使用 `0` 禁用限制（可能存在危险！）。

**`period`\=`<integer>`（<em>默认值 \=</em> `1000`）**

每隔 <em>period</em> 毫秒重置熵注入配额，允许客户机再获取 <em>max\_bytes</em> 的熵。

**`source`\=`</dev/hwrng | /dev/random | /dev/urandom>`**

宿主机上用于收集熵的文件。使用 urandom <strong>不会</strong> 对安全性造成实质性降低，因为它仍以真实熵作为种子，并且所提供的字节很可能也会在客户机上与真实熵混合。<em>/dev/hwrng</em> 可用于直通宿主机上的硬件 RNG。

**`sata[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。

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

**`media`\=`<cdrom | disk>` (<em>默认值 \=</em> `disk`)**

驱动器的介质类型。

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

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

驱动器的全球唯一名称，编码为 16 字节十六进制字符串，以 <em>0x</em> 为前缀。

**`scsi[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。

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

是否为此驱动器使用 iothreads

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

**`media`\=`<cdrom | disk>` (<em>默认值 \=</em> `disk`)**

驱动器的介质类型。

**`product`\=`<product>`**

驱动器的产品名称，最长为 16 字节。

**`queues`\=`<integer> (2 - N)`**

队列数量。

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`ro`\=`<boolean>`**

驱动器是否为只读。

**`scsiblock`\=`<boolean>`（<em>默认值 \=</em> `0`）**

是否使用 scsi-block 完整直通宿主机块设备

{% hint style="warning" %}
当宿主机内存不足或内存碎片严重时，可能导致 I/O 错误
{% endhint %}

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

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

驱动器的厂商名称，最长为 8 字节。

**`werror`\=`<enospc | ignore | report | stop>`**

写入错误时的操作。

**`wwn`\=`<wwn>`**

驱动器的全球唯一名称，编码为 16 字节十六进制字符串，以 <em>0x</em> 为前缀。

**`scsihw`：`<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>`（<em>默认值 \=</em> `lsi`）**

SCSI 控制器型号

**`searchdomain`: `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`serial[n]`: `(/dev/[^,]+|socket)`**

在虚拟机内部创建串口设备（n 为 0 到 3），并直通宿主机串口设备（即 /dev/ttyS0），或在宿主机端创建 unix 套接字（使用 <em>qm terminal</em> 打开终端连接）。

{% hint style="info" %}
如果直通宿主机串口设备，此类虚拟机将无法迁移，请格外谨慎使用。
{% endhint %}

{% hint style="danger" %}
实验性功能！有用户报告此选项存在问题。
{% endhint %}

**`shares`：`<integer> (0 - 50000)`（<em>默认值 \=</em> `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`smbios1`: `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`base64`\=`<boolean>`**

表示 SMBIOS 值采用 base64 编码的标志

**`family`\=`<Base64 encoded string>`**

设置 SMBIOS1 系列字符串。

**`manufacturer`\=`<Base64 encoded string>`**

设置 SMBIOS1 制造商。

**`product`\=`<Base64 encoded string>`**

设置 SMBIOS1 产品 ID。

**`serial`\=`<Base64 encoded string>`**

设置 SMBIOS1 序列号。

**`sku`\=`<Base64 encoded string>`**

设置 SMBIOS1 SKU 字符串。

**`uuid`\=`<UUID>`**

设置 SMBIOS1 UUID。

**`version`\=`<Base64 encoded string>`**

设置 SMBIOS1 版本。

**`smp`：`<integer> (1 - N)`（<em>默认值 \=</em> `1`）**

CPU 数量。请改用 -sockets 选项。

**`sockets`：`<integer> (1 - N)`（<em>默认值 \=</em> `1`）**

CPU 插槽数量。

**`spice_enhancements`: `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`foldersharing`\=`<boolean>`（<em>默认值 \=</em> `0`）**

通过 SPICE 启用文件夹共享。需要在虚拟机中安装 Spice-WebDAV 守护进程。

**`videostreaming`\=`<all | filter | off>`（<em>默认值 \=</em> `off`）**

启用视频流传输。对检测到的视频流使用压缩。

**`sshkeys`: `<string>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`startdate`：`(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)`（<em>默认值 \=</em> `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、<em>2006-06-17T16:01:21</em> 或 <em>2006-06-17</em>。

**`startup`: \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`tablet`：`<boolean>`（<em>默认值 \=</em> `1`）**

启用/禁用 USB 平板设备。通常需要此设备来实现 VNC 的绝对鼠标定位，否则鼠标会与普通 VNC 客户端失去同步。如果在一台宿主机上运行许多仅使用控制台的客户机，可以考虑禁用此选项，以减少一些上下文切换。如果使用 spice（`qm set <vmid> --vga qxl`），默认关闭此选项。

**`tags`: `<string>`**

虚拟机的标签。这只是元信息。

**`tdf`：`<boolean>`（<em>默认值 \=</em> `0`）**

启用/禁用时间漂移修正。

**`template`: `<boolean>` (<em>默认 \=</em> `0`)**

启用/禁用模板。

**`tpmstate0`: `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 <em>raw</em>。

**`file`\=`<volume>`**

驱动器的后端卷。

**`format`\=`<qcow2 | raw | vmdk>`**

镜像的格式。

**`size`\=`<DiskSize>`**

磁盘大小。这仅供参考，不会产生任何影响。

**`version`\=`<v1.2 | v2.0>`（<em>默认值 \=</em> `v1.2`）**

TPM 接口版本。v2.0 较新，应优先使用。请注意，此值之后无法更改。

**`unused[n]`: `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`file`\=`<volume>`**

驱动器的后端卷。

**`usb[n]`: `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`host`\=`<HOSTUSBDEVICE|spice>`**

宿主机 USB 设备、端口或值 <em>spice</em>。HOSTUSBDEVICE 语法为：

```text
'bus-port(.port)*' (decimal numbers) or
'vendor_id:product_id' (hexadecimal numbers) or
'spice'
```

可以使用 <em>lsusb -t</em> 命令列出现有 USB 设备。

{% hint style="info" %}
此选项允许直接访问宿主机硬件。因此此类虚拟机将无法迁移，请格外谨慎使用。
{% endhint %}

值 <em>spice</em> 可用于为 spice 添加 USB 重定向设备。

必须设置此项或 <em>mapping</em> 键。

**`mapping`\=`<mapping-id>`**

集群范围映射的 ID。必须设置此项或默认键 <em>host</em>。

**`usb3`\=`<boolean>`（<em>默认值 \=</em> `0`）**

指定所给 host 选项是否为 USB3 设备或端口。对于较新的客户机（机型版本 \>\= 7.1 且 ostype 为 l26 和 windows \> 7），此标志无关紧要（所有设备均连接到 xhci 控制器）。

**`vcpus`：`<integer> (1 - N)`（<em>默认值 \=</em> `0`）**

热插拔的 vcpu 数量。

**`vga`: `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。如果要使用高分辨率模式（\>\= 1280x1024x16），可能需要增大 vga 内存选项。从 QEMU 2.9 开始，默认 VGA 显示类型为 <em>std</em>，适用于除某些 Windows 版本（XP 及更早版本）外的所有操作系统类型，这些 Windows 版本使用 <em>cirrus</em>。<em>qxl</em> 选项启用 SPICE 显示服务器。对于 win\* 操作系统，可以选择所需的独立显示器数量；Linux 客户机可以自行添加显示器。也可以不使用任何显卡，而使用串口设备作为终端运行。

**`clipboard`\=`<vnc>`**

启用指定剪贴板。如果未设置，将根据显示类型添加 SPICE 剪贴板。QEMU 机型版本 \< 10.1 时，无法使用 VNC 剪贴板进行在线迁移。

**`memory`\=`<integer> (4 - 512)`**

设置 VGA 内存（MiB）。对串口显示无效。

**`type`\=`<cirrus | none | qxl | qxl2 | qxl3 | qxl4 | serial0 | serial1 | serial2 | serial3 | std | virtio | virtio-gl | vmware>`（<em>默认值 \=</em> `std`）**

选择 VGA 类型。不建议使用 <em>cirrus</em> 类型。

**`virtio[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。

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

是否为此驱动器使用 iothreads

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

**`media`\=`<cdrom | disk>` (<em>默认值 \=</em> `disk`)**

驱动器的介质类型。

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

是否应将驱动器纳入复制作业。

**`rerror`\=`<ignore | report | stop>`**

读取错误时的操作。

**`ro`\=`<boolean>`**

驱动器是否为只读。

**`serial`\=`<serial>`**

驱动器报告的序列号，采用 URL 编码，最长 20 字节。

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

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

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`cache`\=`<always | auto | metadata | never>`（<em>默认值 \=</em> `auto`）**

文件系统应使用的缓存策略（auto、always、metadata、never）。

**`direct-io`\=`<boolean>`（<em>默认值 \=</em> `0`）**

遵循客户机应用程序传递的 O\_DIRECT 标志。

**`dirid`\=`<mapping-id>`**

要与客户机共享的目录映射的映射标识符。也用作虚拟机内部的挂载标签。

**`expose-acl`\=`<boolean>`（<em>默认值 \=</em> `0`）**

为此挂载启用 POSIX ACL 支持（启用 ACL 会隐含启用 xattr）。

**`expose-xattr`\=`<boolean>`（<em>默认值 \=</em> `0`）**

为此挂载启用扩展属性支持。

**`vmgenid`：`<UUID>`（<em>默认值 \=</em> `1 (autogenerated)`）**

虚拟机代次 ID（vmgenid）设备向客户机操作系统提供一个 128 位整数值标识符。当虚拟机以不同配置执行时（例如执行快照或从模板创建），可借此通知客户机操作系统。客户机操作系统会注意到更改，随后可作出适当反应，例如将其分布式数据库副本标记为脏、重新初始化随机数生成器等。请注意，自动创建仅在通过 API/CLI 创建或更新方法执行时有效，手动编辑配置文件时无效。

**`vmstatestorage`: `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`watchdog`: `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。启用后（通过客户机操作），客户机内部的代理必须定期轮询看门狗，否则看门狗会重置客户机（或执行所指定的相应操作）

**`action`\=`<debug | none | pause | poweroff | reset | shutdown>`**

激活后，如果客户机未能及时轮询看门狗，要执行的操作。

**`model`\=`<i6300esb | ib700>`（<em>默认值 \=</em> `i6300esb`）**

要模拟的看门狗类型。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/qm.conf.5.html) · 版本 9.2.13 · 非官方中文翻译。
