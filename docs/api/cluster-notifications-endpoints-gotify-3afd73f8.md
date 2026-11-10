# `/cluster/notifications/endpoints/gotify`

原始接口路径：`/cluster/notifications/endpoints/gotify`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/endpoints/gotify`

返回所有 gotify 端点的列表

**方法标识：** `get_gotify_endpoints`

**权限**

```json
{
  "check": [
    "perm",
    "/mapping/notifications",
    [
      "Mapping.Audit"
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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "comment": {
        "description": "注释",
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "default": 0,
        "description": "禁用此目标",
        "optional": 1,
        "type": "boolean"
      },
      "name": {
        "description": "端点名称。",
        "format": "pve-configid",
        "type": "string"
      },
      "origin": {
        "description": "显示此条目是用户创建还是内置",
        "enum": [
          "user-created",
          "builtin",
          "modified-builtin"
        ],
        "type": "string"
      },
      "server": {
        "description": "服务器 URL",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/notifications/endpoints/gotify`

创建新的 gotify 端点

**方法标识：** `create_gotify_endpoint`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "or",
      [
        "perm",
        "/",
        [
          "Sys.Audit",
          "Sys.Modify"
        ]
      ],
      [
        "perm",
        "/",
        [
          "Sys.AccessNetwork"
        ]
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
| `comment` | string | 否 | — | 注释 |
| `disable` | boolean | 否 | 0 | 禁用此目标 |
| `name` | string | 是 | — | 端点名称。 |
| `server` | string | 是 | — | 服务器 URL |
| `token` | string | 是 | — | 秘密令牌 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "注释",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "default": 0,
      "description": "禁用此目标",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "端点名称。",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "server": {
      "description": "服务器 URL",
      "type": "string",
      "typetext": "<string>"
    },
    "token": {
      "description": "秘密令牌",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/gotify)。
