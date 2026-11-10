# `/cluster/mapping/usb`

原始接口路径：`/cluster/mapping/usb`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/mapping/usb`

List USB Hardware Mappings

**方法标识：** `index`

**权限**

```json
{
  "description": "Only lists entries where you have 'Mapping.Modify', 'Mapping.Use' or 'Mapping.Audit' permissions on '/mapping/usb/<id>'.",
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
| `check-node` | string | 否 | — | If given, checks the configurations on the given node for correctness, and adds relevant errors to the devices. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "If given, checks the configurations on the given node for correctness, and adds relevant errors to the devices.",
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
        "description": "A description of the logical mapping.",
        "type": "string"
      },
      "error": {
        "description": "A list of errors when 'check_node' is given.",
        "items": {
          "properties": {
            "message": {
              "description": "The message of the error",
              "type": "string"
            },
            "severity": {
              "description": "The severity of the error",
              "type": "string"
            }
          },
          "type": "object"
        }
      },
      "id": {
        "description": "The logical ID of the mapping.",
        "type": "string"
      },
      "map": {
        "description": "The entries of the mapping.",
        "items": {
          "description": "A mapping for a node.",
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

Create a new hardware mapping.

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
| `description` | string | 否 | — | Description of the logical USB device. |
| `id` | string | 是 | — | The ID of the logical USB mapping. |
| `map` | array | 是 | — | A list of maps for the cluster nodes. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "Description of the logical USB device.",
      "maxLength": 4096,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/usb)。
