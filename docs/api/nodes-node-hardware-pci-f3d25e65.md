# `/nodes/{node}/hardware/pci`

原始接口路径：`/nodes/{node}/hardware/pci`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/hardware/pci`

列出本地 PCI 设备。

**方法标识：** `pci_scan`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `pci-class-blacklist` | string | 否 | "05;06;0b" | PCI 类别黑名单列表，所列类别不会返回。默认过滤以下类别：内存控制器（05）、桥（06）和处理器（0b）。 |
| `verbose` | boolean | 否 | 1 | 如果禁用，则仅输出 PCI ID。否则还会返回供应商、设备等附加信息。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pci-class-blacklist": {
      "default": "05;06;0b",
      "description": "PCI 类别黑名单列表，所列类别不会返回。默认过滤以下类别：内存控制器（05）、桥（06）和处理器（0b）。",
      "format": "string-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "verbose": {
      "default": 1,
      "description": "如果禁用，则仅输出 PCI ID。否则还会返回供应商、设备等附加信息。",
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
        "description": "设备的 PCI 类别。",
        "type": "string"
      },
      "device": {
        "description": "设备 ID。",
        "type": "string"
      },
      "device_name": {
        "optional": 1,
        "type": "string"
      },
      "id": {
        "description": "PCI ID。",
        "type": "string"
      },
      "iommugroup": {
        "description": "设备所在的 IOMMU 组。如果未检测到 IOMMU 组，则设为 -1。",
        "type": "integer"
      },
      "mdev": {
        "description": "如果设置，表示设备能够创建中介设备。",
        "optional": 1,
        "type": "boolean"
      },
      "subsystem_device": {
        "description": "子系统设备 ID。",
        "optional": 1,
        "type": "string"
      },
      "subsystem_device_name": {
        "optional": 1,
        "type": "string"
      },
      "subsystem_vendor": {
        "description": "子系统供应商 ID。",
        "optional": 1,
        "type": "string"
      },
      "subsystem_vendor_name": {
        "optional": 1,
        "type": "string"
      },
      "vendor": {
        "description": "供应商 ID。",
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
