# `/cluster/mapping/usb/{id}`

原始接口路径：`/cluster/mapping/usb/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/mapping/usb/{id}`

移除硬件映射。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/usb",
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

## GET `/cluster/mapping/usb/{id}`

获取 USB 映射。

**方法标识：** `get`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/usb/{id}",
      [
        "Mapping.Audit"
      ]
    ],
    [
      "perm",
      "/mapping/usb/{id}",
      [
        "Mapping.Use"
      ]
    ],
    [
      "perm",
      "/mapping/usb/{id}",
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

## PUT `/cluster/mapping/usb/{id}`

更新硬件映射。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/usb/{id}",
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
| `description` | string | 否 | — | 逻辑 USB 设备的描述。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `id` | string | 是 | — | 逻辑 USB 映射的 ID。 |
| `map` | array | 是 | — | 集群节点的映射列表。 |

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
      "description": "逻辑 USB 设备的描述。",
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
      "description": "逻辑 USB 映射的 ID。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
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
            "description": "预期的供应商和设备 ID。如果给定 USB 路径，则此项仅用于检测硬件变化",
            "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          },
          "node": {
            "description": "集群节点名称。",
            "format": "pve-node",
            "type": "string"
          },
          "path": {
            "description": "USB 设备路径。",
            "optional": 1,
            "pattern": "(?^:^(\\d+)\\-(\\d+(\\.\\d+)*)$)",
            "type": "string"
          }
        },
        "type": "string"
      },
      "type": "array",
      "typetext": "<array>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/usb/{id})。
