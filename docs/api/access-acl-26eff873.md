# `/access/acl`

原始接口路径：`/access/acl`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/acl`

Get Access Control List (ACLs).

**权限**

```json
{
  "description": "The returned list is restricted to objects where you have rights to modify permissions.",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "additionalProperties": 0,
    "properties": {
      "path": {
        "description": "Access control path",
        "type": "string"
      },
      "propagate": {
        "default": 1,
        "description": "Allow to propagate (inherit) permissions.",
        "optional": 1,
        "type": "boolean"
      },
      "roleid": {
        "type": "string"
      },
      "type": {
        "enum": [
          "user",
          "group",
          "token"
        ],
        "type": "string"
      },
      "ugid": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

## PUT `/access/acl`

Update Access Control List (add or remove permissions).

**权限**

```json
{
  "check": [
    "perm-modify",
    "{path}"
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
| `delete` | boolean | 否 | — | Remove permissions (instead of adding it). |
| `groups` | string | 否 | — | List of groups. |
| `path` | string | 是 | — | Access control path |
| `propagate` | boolean | 否 | 1 | Allow to propagate (inherit) permissions. |
| `roles` | string | 是 | — | List of roles. |
| `tokens` | string | 否 | — | List of API tokens. |
| `users` | string | 否 | — | List of users. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "Remove permissions (instead of adding it).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "groups": {
      "description": "List of groups.",
      "format": "pve-groupid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "Access control path",
      "type": "string",
      "typetext": "<string>"
    },
    "propagate": {
      "default": 1,
      "description": "Allow to propagate (inherit) permissions.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "roles": {
      "description": "List of roles.",
      "format": "pve-roleid-list",
      "type": "string",
      "typetext": "<string>"
    },
    "tokens": {
      "description": "List of API tokens.",
      "format": "pve-tokenid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "users": {
      "description": "List of users.",
      "format": "pve-userid-list",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/acl)。
