# `/cluster/mapping/pci/{id}`

原始接口路径：`/cluster/mapping/pci/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/mapping/pci/{id}`

移除硬件映射。

**方法标识：** `delete`

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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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

## GET `/cluster/mapping/pci/{id}`

获取 PCI 映射。

**方法标识：** `get`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/pci/{id}",
      [
        "Mapping.Use"
      ]
    ],
    [
      "perm",
      "/mapping/pci/{id}",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "perm",
      "/mapping/pci/{id}",
      [
        "Mapping.Audit"
      ]
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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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
  "type": "object"
}
```

## PUT `/cluster/mapping/pci/{id}`

更新硬件映射。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/pci/{id}",
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
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `description` | string | 否 | — | 逻辑 PCI 设备的描述。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `id` | string | 是 | — | 逻辑 PCI 映射的 ID。 |
| `live-migration-capable` | boolean | 否 | 0 | 将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。 |
| `map` | array | 否 | — | 集群节点的映射列表。 |
| `mdev` | boolean | 否 | 0 | 将设备标记为能够提供中介设备。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "逻辑 PCI 设备的描述。",
      "maxLength": 4096,
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
      "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/pci/{id})。
