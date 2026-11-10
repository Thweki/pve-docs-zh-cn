# `/cluster/mapping/dir`

原始接口路径：`/cluster/mapping/dir`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/mapping/dir`

List directory mapping

**权限**

```json
{
  "description": "Only lists entries where you have 'Mapping.Modify', 'Mapping.Use' or 'Mapping.Audit' permissions on '/mapping/dir/<id>'.",
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
| `check-node` | string | 否 | — | If given, checks the configurations on the given node for correctness, and adds relevant diagnostics for the directory to the response. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "If given, checks the configurations on the given node for correctness, and adds relevant diagnostics for the directory to the response.",
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
        "description": "A list of checks, only present if 'check-node' is set.",
        "items": {
          "properties": {
            "message": {
              "description": "The message of the error",
              "type": "string"
            },
            "severity": {
              "description": "The severity of the error",
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
        "description": "A description of the logical mapping.",
        "type": "string"
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

## POST `/cluster/mapping/dir`

Create a new directory mapping.

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/dir",
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
| `description` | string | 否 | — | Description of the directory mapping |
| `id` | string | 是 | — | The ID of the directory mapping |
| `map` | array | 是 | — | A list of maps for the cluster nodes. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "description": {
      "description": "Description of the directory mapping",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "id": {
      "description": "The ID of the directory mapping",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "map": {
      "description": "A list of maps for the cluster nodes.",
      "items": {
        "format": {
          "node": {
            "description": "The cluster node name.",
            "format": "pve-node",
            "type": "string"
          },
          "path": {
            "description": "Absolute directory path that should be shared with the guest.",
            "format": "pve-storage-path-in-property-string",
            "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 0,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/dir)。
