# `/cluster/mapping/usb`

原始接口路径：`/cluster/mapping/usb`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/mapping/usb`

列出 USB 硬件映射

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/mapping/usb/<id>' 具有 'Mapping.Modify'、'Mapping.Use' 或 'Mapping.Audit' 权限的条目。",
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
| `check-node` | string | 否 | — | 如果指定，则检查给定节点上的配置是否正确，并将相关错误加入设备。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "如果指定，则检查给定节点上的配置是否正确，并将相关错误加入设备。",
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
      "description": {
        "description": "逻辑映射的描述。",
        "type": "string"
      },
      "error": {
        "description": "指定 'check_node' 时的错误列表。",
        "items": {
          "properties": {
            "message": {
              "description": "错误消息",
              "type": "string"
            },
            "severity": {
              "description": "错误严重程度",
              "type": "string"
            }
          },
          "type": "object"
        }
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

## POST `/cluster/mapping/usb`

创建新的硬件映射。

**方法标识：** `create`

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
| `description` | string | 否 | — | 逻辑 USB 设备的描述。 |
| `id` | string | 是 | — | 逻辑 USB 映射的 ID。 |
| `map` | array | 是 | — | 集群节点的映射列表。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "逻辑 USB 设备的描述。",
      "maxLength": 4096,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/usb)。
