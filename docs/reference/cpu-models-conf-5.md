# cpu-models.conf(5)

## 名称 <a href="#name" id="name"></a>

cpu-models.conf \- 自定义 CPU 模型配置文件

## 概要 <a href="#synopsis" id="synopsis"></a>

<em>/etc/pve/virtual-guest/cpu-models.conf</em>

## 描述 <a href="#description" id="description"></a>

`/etc/pve/virtual-guest/cpu-models.conf` 文件存储自定义 CPU 模型，VM 可使用这些模型来访问高级 CPU 功能（例如自定义 CPU 标志）。

## 文件格式 <a href="#file_format" id="file_format"></a>

每个 CPU 模型在文件中都有各自的节，节的开头为以下标头：

```text
cpu-model: <name>
```

请注意，\<name\> 不包含 <em>custom-</em> 前缀，而在 VM 配置中表示自定义 CPU 模型时需要该前缀。

例如，如果 \<name\> 为 <em>foobar</em>，则 VM 的 CPU 需要配置为 <em>custom-foobar</em>。

每个节可以指定多个选项。这些选项须以一个 TAB 字符或多个空格缩进。每个选项与其值之间用一个空格分隔，例如：

```text
reported-model qemu64
```

所有可用选项请参见下文。

空白行以及以 `#` 开头的行会被忽略。

## 选项 <a href="#options" id="options"></a>

**`flags`: `<+FLAG[;-FLAG...]>`**

以 <em>;</em> 分隔的附加 CPU 标志列表。使用 <em>\+FLAG</em> 启用标志，使用 <em>-FLAG</em> 禁用标志。有一个特殊的 <em>nested-virt</em> 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 使用 <em>svm</em>，Intel 使用 <em>vmx</em>）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，VM 特定标志必须来自以下集合：aes、amd-no-ssb、amd-ssbd、hv-evmcs、hv-tlbflush、ibpb、md-clear、nested-virt、pcid、pdpe1gb、spec-ctrl、ssbd、virt-ssbd

**`guest-phys-bits`: `<integer> (32 - 64)`**

客户机可用的物理地址位数。

**`hidden`: `<boolean>` (<em>默认值 \=</em> `0`)**

不要标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。

**`hv-vendor-id`: `<vendor-id>`**

Hyper-V 供应商 ID。Windows 客户机中的某些驱动程序或程序需要特定的 ID。

**`level`: `<integer> (0 - 4294967295)`**

客户机可查询的基本 CPUID 叶的最大输入值——即供应商（叶 0）、系列/型号/步进及功能位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶将被隐藏。将此项设置为 <em>30</em>，是解决在较新的 Intel 宿主机上运行的 Windows 客户机出现 Hyper-V 启动故障的常用变通方法。仅当 vCPU 架构为 x86\_64 时适用。

**`phys-bits`: `<8-64|host>`**

报告给客户机操作系统的物理内存地址位数。应小于或等于宿主机的位数。设置为 <em>host</em> 可使用宿主机 CPU 的值，但请注意，这样会导致无法在线迁移到该值不同的 CPU。

**`reported-model`: `<486 | Broadwell | Broadwell-IBRS | Broadwell-noTSX | Broadwell-noTSX-IBRS | Cascadelake-Server | Cascadelake-Server-noTSX | Cascadelake-Server-v2 | Cascadelake-Server-v4 | Cascadelake-Server-v5 | ClearwaterForest | ClearwaterForest-v2 | ClearwaterForest-v3 | Conroe | Cooperlake | Cooperlake-v2 | DiamondRapids | EPYC | EPYC-Genoa | EPYC-Genoa-v2 | EPYC-IBPB | EPYC-Milan | EPYC-Milan-v2 | EPYC-Milan-v3 | EPYC-Rome | EPYC-Rome-v2 | EPYC-Rome-v3 | EPYC-Rome-v4 | EPYC-Rome-v5 | EPYC-Turin | EPYC-v3 | EPYC-v4 | EPYC-v5 | GraniteRapids | GraniteRapids-v2 | GraniteRapids-v3 | GraniteRapids-v4 | GraniteRapids-v5 | Haswell | Haswell-IBRS | Haswell-noTSX | Haswell-noTSX-IBRS | Icelake-Client | Icelake-Client-noTSX | Icelake-Server | Icelake-Server-noTSX | Icelake-Server-v3 | Icelake-Server-v4 | Icelake-Server-v5 | Icelake-Server-v6 | Icelake-Server-v7 | IvyBridge | IvyBridge-IBRS | KnightsMill | Nehalem | Nehalem-IBRS | Opteron_G1 | Opteron_G2 | Opteron_G3 | Opteron_G4 | Opteron_G5 | Penryn | SandyBridge | SandyBridge-IBRS | SapphireRapids | SapphireRapids-v2 | SapphireRapids-v3 | SapphireRapids-v4 | SapphireRapids-v5 | SapphireRapids-v6 | SierraForest | SierraForest-v2 | SierraForest-v3 | SierraForest-v4 | SierraForest-v5 | Skylake-Client | Skylake-Client-IBRS | Skylake-Client-noTSX-IBRS | Skylake-Client-v4 | Skylake-Server | Skylake-Server-IBRS | Skylake-Server-noTSX-IBRS | Skylake-Server-v4 | Skylake-Server-v5 | Westmere | Westmere-IBRS | a64fx | athlon | core2duo | coreduo | cortex-a35 | cortex-a53 | cortex-a55 | cortex-a57 | cortex-a710 | cortex-a72 | cortex-a76 | cortex-a78ae | host | kvm32 | kvm64 | max | neoverse-n1 | neoverse-n2 | neoverse-v1 | pentium | pentium2 | pentium3 | phenom | qemu32 | qemu64>` (<em>默认值 \=</em> `kvm64`)**

报告给客户机的 CPU 模型和供应商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效；默认模型始终会向客户机操作系统报告其自身。

## 示例文件 <a href="#example_file" id="example_file"></a>

```text
cpu-model: avx
    flags +avx;+avx2
    phys-bits host
    hidden 0
    hv-vendor-id proxmox
    reported-model kvm64
```

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/cpu-models.conf.5.html) · 版本 9.2.13 · 非官方中文翻译。
