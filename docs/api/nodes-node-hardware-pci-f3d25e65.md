# `/nodes/{node}/hardware/pci`

原始接口路径：`/nodes/{node}/hardware/pci`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/hardware/pci`

List local PCI devices.

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit",
      "Sys.Modify"
    ],
    "any",
    1
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `pci-class-blacklist` | string | 否 | "05;06;0b" | A list of blacklisted PCI classes, which will not be returned. Following are filtered by default: Memory Controller (05), Bridge (06) and Processor (0b). |
| `verbose` | boolean | 否 | 1 | If disabled, does only print the PCI IDs. Otherwise, additional information like vendor and device will be returned. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pci-class-blacklist": {
      "default": "05;06;0b",
      "description": "A list of blacklisted PCI classes, which will not be returned. Following are filtered by default: Memory Controller (05), Bridge (06) and Processor (0b).",
      "format": "string-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "verbose": {
      "default": 1,
      "description": "If disabled, does only print the PCI IDs. Otherwise, additional information like vendor and device will be returned.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "properties": {
      "class": {
        "description": "The PCI Class of the device.",
        "type": "string"
      },
      "device": {
        "description": "The Device ID.",
        "type": "string"
      },
      "device_name": {
        "optional": 1,
        "type": "string"
      },
      "id": {
        "description": "The PCI ID.",
        "type": "string"
      },
      "iommugroup": {
        "description": "The IOMMU group in which the device is in. If no IOMMU group is detected, it is set to -1.",
        "type": "integer"
      },
      "mdev": {
        "description": "If set, marks that the device is capable of creating mediated devices.",
        "optional": 1,
        "type": "boolean"
      },
      "subsystem_device": {
        "description": "The Subsystem Device ID.",
        "optional": 1,
        "type": "string"
      },
      "subsystem_device_name": {
        "optional": 1,
        "type": "string"
      },
      "subsystem_vendor": {
        "description": "The Subsystem Vendor ID.",
        "optional": 1,
        "type": "string"
      },
      "subsystem_vendor_name": {
        "optional": 1,
        "type": "string"
      },
      "vendor": {
        "description": "The Vendor ID.",
        "type": "string"
      },
      "vendor_name": {
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/hardware/pci)。
