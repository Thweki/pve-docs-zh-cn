# `/cluster/mapping/pci`

原始接口路径：`/cluster/mapping/pci`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/mapping/pci`

列出 PCI 硬件映射

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/mapping/pci/<id>' 具有 'Mapping.Modify'、'Mapping.Use' 或 'Mapping.Audit' 权限的条目。",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `check-node` | string | 否 | — | 如果指定，则检查给定节点上的配置是否正确，并将与设备相关的诊断信息加入响应。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "如果指定，则检查给定节点上的配置是否正确，并将与设备相关的诊断信息加入响应。",
      "format": "pve-node",
      "optional": 1,
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
  "items": {
    "properties": {
      "checks": {
        "description": "检查列表，仅在设置了 'check_node' 时存在。",
        "items": {
          "properties": {
            "message": {
              "description": "错误消息",
              "type": "string"
            },
            "severity": {
              "description": "错误严重程度",
              "enum": [
                "warning",
                "error"
              ],
              "type": "string"
            }
          },
          "type": "object"
        },
        "optional": 1,
        "type": "array"
      },
      "description": {
        "description": "逻辑映射的描述。",
        "type": "string"
      },
      "id": {
        "description": "映射的逻辑 ID。",
        "type": "string"
      },
      "map": {
        "description": "映射条目。",
        "items": {
          "description": "节点的映射。",
          "type": "string"
        },
        "type": "array"
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

## POST `/cluster/mapping/pci`

创建新的硬件映射。

**方法标识：** `create`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/pci",
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
| `description` | string | 否 | — | 逻辑 PCI 设备的描述。 |
| `id` | string | 是 | — | 逻辑 PCI 映射的 ID。 |
| `live-migration-capable` | boolean | 否 | 0 | 将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。 |
| `map` | array | 是 | — | 集群节点的映射列表。 |
| `mdev` | boolean | 否 | 0 | 将设备标记为能够提供中介设备。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "逻辑 PCI 设备的描述。",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "id": {
      "description": "逻辑 PCI 映射的 ID。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "live-migration-capable": {
      "default": 0,
      "description": "将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "description": {
            "description": "节点特定设备的描述。",
            "maxLength": 4096,
            "optional": 1,
            "type": "string"
          },
          "id": {
            "description": "预期的供应商和设备 ID。用于检测硬件变化",
            "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          },
          "iommugroup": {
            "description": "预期设备所在的 IOMMU 组。用于检测硬件变化。",
            "optional": 1,
            "type": "integer"
          },
          "node": {
            "description": "集群节点名称。",
            "format": "pve-node",
            "type": "string"
          },
          "path": {
            "description": "设备路径。如果省略功能号，则映射整个设备。此时使用第一个设备的属性。可以提供以分号分隔的多个路径，客户机启动时将选择第一个可用路径。",
            "pattern": "(?:[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?;)*[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?",
            "type": "string"
          },
          "subsystem-id": {
            "description": "预期的子系统供应商和设备 ID。用于检测硬件变化。",
            "optional": 1,
            "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 0,
      "type": "array",
      "typetext": "<array>"
    },
    "mdev": {
      "default": 0,
      "description": "将设备标记为能够提供中介设备。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/pci)。
