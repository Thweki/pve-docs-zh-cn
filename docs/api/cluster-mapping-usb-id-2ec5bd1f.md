# `/cluster/mapping/usb/{id}`

原始接口路径：`/cluster/mapping/usb/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/mapping/usb/{id}`

Remove Hardware Mapping.

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

Get USB Mapping.

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

Update a hardware mapping.

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
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `description` | string | 否 | — | Description of the logical USB device. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `id` | string | 是 | — | The ID of the logical USB mapping. |
| `map` | array | 是 | — | A list of maps for the cluster nodes. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "Description of the logical USB device.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "id": {
      "description": "The ID of the logical USB mapping.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "map": {
      "description": "A list of maps for the cluster nodes.",
      "items": {
        "format": {
          "description": {
            "description": "Description of the node specific device.",
            "maxLength": 4096,
            "optional": 1,
            "type": "string"
          },
          "id": {
            "description": "The vendor and device ID that is expected. If a USB path is given, it is only used for detecting hardware changes",
            "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          },
          "node": {
            "description": "The cluster node name.",
            "format": "pve-node",
            "type": "string"
          },
          "path": {
            "description": "The path to the usb device.",
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
