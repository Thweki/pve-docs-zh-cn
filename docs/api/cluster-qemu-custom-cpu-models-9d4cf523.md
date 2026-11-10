# `/cluster/qemu/custom-cpu-models`

原始接口路径：`/cluster/qemu/custom-cpu-models`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/qemu/custom-cpu-models`

List all custom CPU model definitions visible to the user.

**方法标识：** `config`

**权限**

```json
{
  "description": "Only lists entries where the user has 'Mapping.Modify', 'Mapping.Use' or 'Mapping.Audit' permissions on '/mapping/cpu/<name>'.",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "cputype": {
        "default": "kvm64",
        "default_key": 1,
        "description": "Emulated CPU type. Can be default or custom name (custom model names must be prefixed with 'custom-').",
        "format_description": "string",
        "optional": 1,
        "type": "string"
      },
      "digest": {
        "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
        "maxLength": 64,
        "optional": 1,
        "type": "string"
      },
      "flags": {
        "description": "List of additional CPU flags separated by ';'. Use '+FLAG' to enable, '-FLAG' to disable a flag. There is a special 'nested-virt' shorthand which controls nested virtualization for the current CPU ('svm' for AMD and 'vmx' for Intel). Custom CPU models can specify any flag supported by QEMU/KVM, VM-specific flags must be from the following set for security reasons: aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
        "format_description": "+FLAG[;-FLAG...]",
        "optional": 1,
        "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
        "type": "string"
      },
      "guest-phys-bits": {
        "description": "Number of physical address bits available to the guest.",
        "maximum": 64,
        "minimum": 32,
        "optional": 1,
        "type": "integer"
      },
      "hidden": {
        "default": 0,
        "description": "Do not identify as a KVM virtual machine. Only affects vCPUs with x86-64 architecture.",
        "optional": 1,
        "type": "boolean"
      },
      "hv-vendor-id": {
        "description": "The Hyper-V vendor ID. Some drivers or programs inside Windows guests need a specific ID.",
        "format_description": "vendor-id",
        "optional": 1,
        "pattern": "(?^u:[a-zA-Z0-9]{1,12})",
        "type": "string"
      },
      "level": {
        "description": "Maximum input value for the basic CPUID leaves the guest can query - that is the vendor (leaf 0), family/model/stepping and feature bits (leaf 1), cache and topology info (leaves 4 and B), and so on. Higher-numbered leaves are hidden. Setting '30' is a common workaround for Hyper-V boot failures on Windows guests running on recent Intel hosts. Only applies when the vCPU architecture is x86_64.",
        "maximum": 4294967295,
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "phys-bits": {
        "description": "The physical memory address bits that are reported to the guest OS. Should be smaller or equal to the host's. Set to 'host' to use value from host CPU, but note that doing so will break live migration to CPUs with other values.",
        "format": "pve-phys-bits",
        "format_description": "8-64|host",
        "optional": 1,
        "type": "string"
      },
      "reported-model": {
        "default": "kvm64",
        "description": "CPU model and vendor to report to the guest. Must be a QEMU/KVM supported model. Only valid for custom CPU model definitions, default models will always report themselves to the guest OS.",
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
  },
  "links": [
    {
      "href": "{cputype}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/qemu/custom-cpu-models`

Add a custom CPU model definition.

**方法标识：** `create`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/cpu",
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
| `cputype` | string | 是 | — | Name for the custom CPU model. The 'custom-' prefix is optional. |
| `flags` | string | 否 | — | List of additional CPU flags separated by ';'. Use '+FLAG' to enable, '-FLAG' to disable a flag. There is a special 'nested-virt' shorthand which controls nested virtualization for the current CPU ('svm' for AMD and 'vmx' for Intel). Custom CPU models can specify any flag supported by QEMU/KVM, VM-specific flags must be from the following set for security reasons: aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd |
| `guest-phys-bits` | integer | 否 | — | Number of physical address bits available to the guest. |
| `hidden` | boolean | 否 | 0 | Do not identify as a KVM virtual machine. Only affects vCPUs with x86-64 architecture. |
| `hv-vendor-id` | string | 否 | — | The Hyper-V vendor ID. Some drivers or programs inside Windows guests need a specific ID. |
| `level` | integer | 否 | — | Maximum input value for the basic CPUID leaves the guest can query - that is the vendor (leaf 0), family/model/stepping and feature bits (leaf 1), cache and topology info (leaves 4 and B), and so on. Higher-numbered leaves are hidden. Setting '30' is a common workaround for Hyper-V boot failures on Windows guests running on recent Intel hosts. Only applies when the vCPU architecture is x86_64. |
| `phys-bits` | string | 否 | — | The physical memory address bits that are reported to the guest OS. Should be smaller or equal to the host's. Set to 'host' to use value from host CPU, but note that doing so will break live migration to CPUs with other values. |
| `reported-model` | string | 是 | "kvm64" | CPU model and vendor to report to the guest. Must be a QEMU/KVM supported model. Only valid for custom CPU model definitions, default models will always report themselves to the guest OS.；可选值：`486`, `a64fx`, `athlon`, `Broadwell`, `Broadwell-IBRS`, `Broadwell-noTSX`, `Broadwell-noTSX-IBRS`, `Cascadelake-Server`, `Cascadelake-Server-noTSX`, `Cascadelake-Server-v2`, `Cascadelake-Server-v4`, `Cascadelake-Server-v5`, `ClearwaterForest`, `ClearwaterForest-v2`, `ClearwaterForest-v3`, `Conroe`, `Cooperlake`, `Cooperlake-v2`, `core2duo`, `coreduo`, `cortex-a35`, `cortex-a53`, `cortex-a55`, `cortex-a57`, `cortex-a710`, `cortex-a72`, `cortex-a76`, `cortex-a78ae`, `DiamondRapids`, `EPYC`, `EPYC-Genoa`, `EPYC-Genoa-v2`, `EPYC-IBPB`, `EPYC-Milan`, `EPYC-Milan-v2`, `EPYC-Milan-v3`, `EPYC-Rome`, `EPYC-Rome-v2`, `EPYC-Rome-v3`, `EPYC-Rome-v4`, `EPYC-Rome-v5`, `EPYC-Turin`, `EPYC-v3`, `EPYC-v4`, `EPYC-v5`, `GraniteRapids`, `GraniteRapids-v2`, `GraniteRapids-v3`, `GraniteRapids-v4`, `GraniteRapids-v5`, `Haswell`, `Haswell-IBRS`, `Haswell-noTSX`, `Haswell-noTSX-IBRS`, `host`, `Icelake-Client`, `Icelake-Client-noTSX`, `Icelake-Server`, `Icelake-Server-noTSX`, `Icelake-Server-v3`, `Icelake-Server-v4`, `Icelake-Server-v5`, `Icelake-Server-v6`, `Icelake-Server-v7`, `IvyBridge`, `IvyBridge-IBRS`, `KnightsMill`, `kvm32`, `kvm64`, `max`, `Nehalem`, `Nehalem-IBRS`, `neoverse-n1`, `neoverse-n2`, `neoverse-v1`, `Opteron_G1`, `Opteron_G2`, `Opteron_G3`, `Opteron_G4`, `Opteron_G5`, `Penryn`, `pentium`, `pentium2`, `pentium3`, `phenom`, `qemu32`, `qemu64`, `SandyBridge`, `SandyBridge-IBRS`, `SapphireRapids`, `SapphireRapids-v2`, `SapphireRapids-v3`, `SapphireRapids-v4`, `SapphireRapids-v5`, `SapphireRapids-v6`, `SierraForest`, `SierraForest-v2`, `SierraForest-v3`, `SierraForest-v4`, `SierraForest-v5`, `Skylake-Client`, `Skylake-Client-IBRS`, `Skylake-Client-noTSX-IBRS`, `Skylake-Client-v4`, `Skylake-Server`, `Skylake-Server-IBRS`, `Skylake-Server-noTSX-IBRS`, `Skylake-Server-v4`, `Skylake-Server-v5`, `Westmere`, `Westmere-IBRS` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cputype": {
      "description": "Name for the custom CPU model. The 'custom-' prefix is optional.",
      "format": "pve-configid",
      "maxLength": 40,
      "type": "string",
      "typetext": "<string>"
    },
    "flags": {
      "description": "List of additional CPU flags separated by ';'. Use '+FLAG' to enable, '-FLAG' to disable a flag. There is a special 'nested-virt' shorthand which controls nested virtualization for the current CPU ('svm' for AMD and 'vmx' for Intel). Custom CPU models can specify any flag supported by QEMU/KVM, VM-specific flags must be from the following set for security reasons: aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
      "format_description": "+FLAG[;-FLAG...]",
      "optional": 1,
      "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
      "type": "string"
    },
    "guest-phys-bits": {
      "description": "Number of physical address bits available to the guest.",
      "maximum": 64,
      "minimum": 32,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (32 - 64)"
    },
    "hidden": {
      "default": 0,
      "description": "Do not identify as a KVM virtual machine. Only affects vCPUs with x86-64 architecture.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hv-vendor-id": {
      "description": "The Hyper-V vendor ID. Some drivers or programs inside Windows guests need a specific ID.",
      "format_description": "vendor-id",
      "optional": 1,
      "pattern": "(?^u:[a-zA-Z0-9]{1,12})",
      "type": "string"
    },
    "level": {
      "description": "Maximum input value for the basic CPUID leaves the guest can query - that is the vendor (leaf 0), family/model/stepping and feature bits (leaf 1), cache and topology info (leaves 4 and B), and so on. Higher-numbered leaves are hidden. Setting '30' is a common workaround for Hyper-V boot failures on Windows guests running on recent Intel hosts. Only applies when the vCPU architecture is x86_64.",
      "maximum": 4294967295,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 4294967295)"
    },
    "phys-bits": {
      "description": "The physical memory address bits that are reported to the guest OS. Should be smaller or equal to the host's. Set to 'host' to use value from host CPU, but note that doing so will break live migration to CPUs with other values.",
      "format": "pve-phys-bits",
      "format_description": "8-64|host",
      "optional": 1,
      "type": "string",
      "typetext": "<8-64|host>"
    },
    "reported-model": {
      "default": "kvm64",
      "description": "CPU model and vendor to report to the guest. Must be a QEMU/KVM supported model. Only valid for custom CPU model definitions, default models will always report themselves to the guest OS.",
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
      "optional": 0,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu/custom-cpu-models)。
