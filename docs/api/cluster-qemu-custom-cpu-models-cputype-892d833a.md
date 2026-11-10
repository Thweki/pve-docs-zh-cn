# `/cluster/qemu/custom-cpu-models/{cputype}`

原始接口路径：`/cluster/qemu/custom-cpu-models/{cputype}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/qemu/custom-cpu-models/{cputype}`

删除自定义 CPU 模型定义。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/cpu/{cputype}",
    [
      "Mapping.Modify"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `cputype` | string | 是 | — | 要删除的自定义模型。'custom-' 前缀可选。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cputype": {
      "description": "要删除的自定义模型。'custom-' 前缀可选。",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## GET `/cluster/qemu/custom-cpu-models/{cputype}`

获取指定自定义 CPU 模型的详细信息。

**方法标识：** `info`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/cpu/{cputype}",
      [
        "Mapping.Audit"
      ]
    ],
    [
      "perm",
      "/mapping/cpu/{cputype}",
      [
        "Mapping.Use"
      ]
    ],
    [
      "perm",
      "/mapping/cpu/{cputype}",
      [
        "Mapping.Modify"
      ]
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `cputype` | string | 是 | — | 要查询的 CPU 模型名称。'custom-' 前缀可选。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cputype": {
      "description": "要查询的 CPU 模型名称。'custom-' 前缀可选。",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "cputype": {
      "default": "kvm64",
      "default_key": 1,
      "description": "模拟的 CPU 类型。可以是默认名称或自定义名称（自定义模型名称必须带有 'custom-' 前缀）。",
      "format_description": "string",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "flags": {
      "description": "以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
      "format_description": "+FLAG[;-FLAG...]",
      "optional": 1,
      "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
      "type": "string"
    },
    "guest-phys-bits": {
      "description": "客户机可用的物理地址位数。",
      "maximum": 64,
      "minimum": 32,
      "optional": 1,
      "type": "integer"
    },
    "hidden": {
      "default": 0,
      "description": "不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。",
      "optional": 1,
      "type": "boolean"
    },
    "hv-vendor-id": {
      "description": "Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。",
      "format_description": "vendor-id",
      "optional": 1,
      "pattern": "(?^u:[a-zA-Z0-9]{1,12})",
      "type": "string"
    },
    "level": {
      "description": "客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。",
      "maximum": 4294967295,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "phys-bits": {
      "description": "向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。",
      "format": "pve-phys-bits",
      "format_description": "8-64|host",
      "optional": 1,
      "type": "string"
    },
    "reported-model": {
      "default": "kvm64",
      "description": "向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。",
      "enum": [
        "486",
        "a64fx",
        "athlon",
        "Broadwell",
        "Broadwell-IBRS",
        "Broadwell-noTSX",
        "Broadwell-noTSX-IBRS",
        "Cascadelake-Server",
        "Cascadelake-Server-noTSX",
        "Cascadelake-Server-v2",
        "Cascadelake-Server-v4",
        "Cascadelake-Server-v5",
        "ClearwaterForest",
        "ClearwaterForest-v2",
        "ClearwaterForest-v3",
        "Conroe",
        "Cooperlake",
        "Cooperlake-v2",
        "core2duo",
        "coreduo",
        "cortex-a35",
        "cortex-a53",
        "cortex-a55",
        "cortex-a57",
        "cortex-a710",
        "cortex-a72",
        "cortex-a76",
        "cortex-a78ae",
        "DiamondRapids",
        "EPYC",
        "EPYC-Genoa",
        "EPYC-Genoa-v2",
        "EPYC-IBPB",
        "EPYC-Milan",
        "EPYC-Milan-v2",
        "EPYC-Milan-v3",
        "EPYC-Rome",
        "EPYC-Rome-v2",
        "EPYC-Rome-v3",
        "EPYC-Rome-v4",
        "EPYC-Rome-v5",
        "EPYC-Turin",
        "EPYC-v3",
        "EPYC-v4",
        "EPYC-v5",
        "GraniteRapids",
        "GraniteRapids-v2",
        "GraniteRapids-v3",
        "GraniteRapids-v4",
        "GraniteRapids-v5",
        "Haswell",
        "Haswell-IBRS",
        "Haswell-noTSX",
        "Haswell-noTSX-IBRS",
        "host",
        "Icelake-Client",
        "Icelake-Client-noTSX",
        "Icelake-Server",
        "Icelake-Server-noTSX",
        "Icelake-Server-v3",
        "Icelake-Server-v4",
        "Icelake-Server-v5",
        "Icelake-Server-v6",
        "Icelake-Server-v7",
        "IvyBridge",
        "IvyBridge-IBRS",
        "KnightsMill",
        "kvm32",
        "kvm64",
        "max",
        "Nehalem",
        "Nehalem-IBRS",
        "neoverse-n1",
        "neoverse-n2",
        "neoverse-v1",
        "Opteron_G1",
        "Opteron_G2",
        "Opteron_G3",
        "Opteron_G4",
        "Opteron_G5",
        "Penryn",
        "pentium",
        "pentium2",
        "pentium3",
        "phenom",
        "qemu32",
        "qemu64",
        "SandyBridge",
        "SandyBridge-IBRS",
        "SapphireRapids",
        "SapphireRapids-v2",
        "SapphireRapids-v3",
        "SapphireRapids-v4",
        "SapphireRapids-v5",
        "SapphireRapids-v6",
        "SierraForest",
        "SierraForest-v2",
        "SierraForest-v3",
        "SierraForest-v4",
        "SierraForest-v5",
        "Skylake-Client",
        "Skylake-Client-IBRS",
        "Skylake-Client-noTSX-IBRS",
        "Skylake-Client-v4",
        "Skylake-Server",
        "Skylake-Server-IBRS",
        "Skylake-Server-noTSX-IBRS",
        "Skylake-Server-v4",
        "Skylake-Server-v5",
        "Westmere",
        "Westmere-IBRS"
      ],
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/qemu/custom-cpu-models/{cputype}`

更新自定义 CPU 模型定义。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/cpu/{cputype}",
    [
      "Mapping.Modify"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `cputype` | string | 是 | — | 自定义 CPU 模型名称。'custom-' 前缀可选。 |
| `delete` | string | 否 | — | 要删除的属性列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `flags` | string | 否 | — | 以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd |
| `guest-phys-bits` | integer | 否 | — | 客户机可用的物理地址位数。 |
| `hidden` | boolean | 否 | 0 | 不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。 |
| `hv-vendor-id` | string | 否 | — | Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。 |
| `level` | integer | 否 | — | 客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。 |
| `phys-bits` | string | 否 | — | 向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。 |
| `reported-model` | string | 否 | "kvm64" | 向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。；可选值：`486`, `a64fx`, `athlon`, `Broadwell`, `Broadwell-IBRS`, `Broadwell-noTSX`, `Broadwell-noTSX-IBRS`, `Cascadelake-Server`, `Cascadelake-Server-noTSX`, `Cascadelake-Server-v2`, `Cascadelake-Server-v4`, `Cascadelake-Server-v5`, `ClearwaterForest`, `ClearwaterForest-v2`, `ClearwaterForest-v3`, `Conroe`, `Cooperlake`, `Cooperlake-v2`, `core2duo`, `coreduo`, `cortex-a35`, `cortex-a53`, `cortex-a55`, `cortex-a57`, `cortex-a710`, `cortex-a72`, `cortex-a76`, `cortex-a78ae`, `DiamondRapids`, `EPYC`, `EPYC-Genoa`, `EPYC-Genoa-v2`, `EPYC-IBPB`, `EPYC-Milan`, `EPYC-Milan-v2`, `EPYC-Milan-v3`, `EPYC-Rome`, `EPYC-Rome-v2`, `EPYC-Rome-v3`, `EPYC-Rome-v4`, `EPYC-Rome-v5`, `EPYC-Turin`, `EPYC-v3`, `EPYC-v4`, `EPYC-v5`, `GraniteRapids`, `GraniteRapids-v2`, `GraniteRapids-v3`, `GraniteRapids-v4`, `GraniteRapids-v5`, `Haswell`, `Haswell-IBRS`, `Haswell-noTSX`, `Haswell-noTSX-IBRS`, `host`, `Icelake-Client`, `Icelake-Client-noTSX`, `Icelake-Server`, `Icelake-Server-noTSX`, `Icelake-Server-v3`, `Icelake-Server-v4`, `Icelake-Server-v5`, `Icelake-Server-v6`, `Icelake-Server-v7`, `IvyBridge`, `IvyBridge-IBRS`, `KnightsMill`, `kvm32`, `kvm64`, `max`, `Nehalem`, `Nehalem-IBRS`, `neoverse-n1`, `neoverse-n2`, `neoverse-v1`, `Opteron_G1`, `Opteron_G2`, `Opteron_G3`, `Opteron_G4`, `Opteron_G5`, `Penryn`, `pentium`, `pentium2`, `pentium3`, `phenom`, `qemu32`, `qemu64`, `SandyBridge`, `SandyBridge-IBRS`, `SapphireRapids`, `SapphireRapids-v2`, `SapphireRapids-v3`, `SapphireRapids-v4`, `SapphireRapids-v5`, `SapphireRapids-v6`, `SierraForest`, `SierraForest-v2`, `SierraForest-v3`, `SierraForest-v4`, `SierraForest-v5`, `Skylake-Client`, `Skylake-Client-IBRS`, `Skylake-Client-noTSX-IBRS`, `Skylake-Client-v4`, `Skylake-Server`, `Skylake-Server-IBRS`, `Skylake-Server-noTSX-IBRS`, `Skylake-Server-v4`, `Skylake-Server-v5`, `Westmere`, `Westmere-IBRS` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cputype": {
      "description": "自定义 CPU 模型名称。'custom-' 前缀可选。",
      "format": "pve-configid",
      "maxLength": 40,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的属性列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "flags": {
      "description": "以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
      "format_description": "+FLAG[;-FLAG...]",
      "optional": 1,
      "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
      "type": "string"
    },
    "guest-phys-bits": {
      "description": "客户机可用的物理地址位数。",
      "maximum": 64,
      "minimum": 32,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (32 - 64)"
    },
    "hidden": {
      "default": 0,
      "description": "不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hv-vendor-id": {
      "description": "Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。",
      "format_description": "vendor-id",
      "optional": 1,
      "pattern": "(?^u:[a-zA-Z0-9]{1,12})",
      "type": "string"
    },
    "level": {
      "description": "客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。",
      "maximum": 4294967295,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 4294967295)"
    },
    "phys-bits": {
      "description": "向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。",
      "format": "pve-phys-bits",
      "format_description": "8-64|host",
      "optional": 1,
      "type": "string",
      "typetext": "<8-64|host>"
    },
    "reported-model": {
      "default": "kvm64",
      "description": "向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。",
      "enum": [
        "486",
        "a64fx",
        "athlon",
        "Broadwell",
        "Broadwell-IBRS",
        "Broadwell-noTSX",
        "Broadwell-noTSX-IBRS",
        "Cascadelake-Server",
        "Cascadelake-Server-noTSX",
        "Cascadelake-Server-v2",
        "Cascadelake-Server-v4",
        "Cascadelake-Server-v5",
        "ClearwaterForest",
        "ClearwaterForest-v2",
        "ClearwaterForest-v3",
        "Conroe",
        "Cooperlake",
        "Cooperlake-v2",
        "core2duo",
        "coreduo",
        "cortex-a35",
        "cortex-a53",
        "cortex-a55",
        "cortex-a57",
        "cortex-a710",
        "cortex-a72",
        "cortex-a76",
        "cortex-a78ae",
        "DiamondRapids",
        "EPYC",
        "EPYC-Genoa",
        "EPYC-Genoa-v2",
        "EPYC-IBPB",
        "EPYC-Milan",
        "EPYC-Milan-v2",
        "EPYC-Milan-v3",
        "EPYC-Rome",
        "EPYC-Rome-v2",
        "EPYC-Rome-v3",
        "EPYC-Rome-v4",
        "EPYC-Rome-v5",
        "EPYC-Turin",
        "EPYC-v3",
        "EPYC-v4",
        "EPYC-v5",
        "GraniteRapids",
        "GraniteRapids-v2",
        "GraniteRapids-v3",
        "GraniteRapids-v4",
        "GraniteRapids-v5",
        "Haswell",
        "Haswell-IBRS",
        "Haswell-noTSX",
        "Haswell-noTSX-IBRS",
        "host",
        "Icelake-Client",
        "Icelake-Client-noTSX",
        "Icelake-Server",
        "Icelake-Server-noTSX",
        "Icelake-Server-v3",
        "Icelake-Server-v4",
        "Icelake-Server-v5",
        "Icelake-Server-v6",
        "Icelake-Server-v7",
        "IvyBridge",
        "IvyBridge-IBRS",
        "KnightsMill",
        "kvm32",
        "kvm64",
        "max",
        "Nehalem",
        "Nehalem-IBRS",
        "neoverse-n1",
        "neoverse-n2",
        "neoverse-v1",
        "Opteron_G1",
        "Opteron_G2",
        "Opteron_G3",
        "Opteron_G4",
        "Opteron_G5",
        "Penryn",
        "pentium",
        "pentium2",
        "pentium3",
        "phenom",
        "qemu32",
        "qemu64",
        "SandyBridge",
        "SandyBridge-IBRS",
        "SapphireRapids",
        "SapphireRapids-v2",
        "SapphireRapids-v3",
        "SapphireRapids-v4",
        "SapphireRapids-v5",
        "SapphireRapids-v6",
        "SierraForest",
        "SierraForest-v2",
        "SierraForest-v3",
        "SierraForest-v4",
        "SierraForest-v5",
        "Skylake-Client",
        "Skylake-Client-IBRS",
        "Skylake-Client-noTSX-IBRS",
        "Skylake-Client-v4",
        "Skylake-Server",
        "Skylake-Server-IBRS",
        "Skylake-Server-noTSX-IBRS",
        "Skylake-Server-v4",
        "Skylake-Server-v5",
        "Westmere",
        "Westmere-IBRS"
      ],
      "optional": 1,
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu/custom-cpu-models/{cputype})。
