# `/access/acl`

原始接口路径：`/access/acl`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/acl`

获取访问控制列表（ACL）。

**方法标识：** `read_acl`

**权限**

```json
{
  "description": "返回列表仅限于您有权修改其权限的对象。",
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
        "description": "访问控制路径",
        "type": "string"
      },
      "propagate": {
        "default": 1,
        "description": "允许传播（继承）权限。",
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

更新访问控制列表（添加或移除权限）。

**方法标识：** `update_acl`

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
| `delete` | boolean | 否 | — | 移除权限（而非添加）。 |
| `groups` | string | 否 | — | 组列表。 |
| `path` | string | 是 | — | 访问控制路径 |
| `propagate` | boolean | 否 | 1 | 允许传播（继承）权限。 |
| `roles` | string | 是 | — | 角色列表。 |
| `tokens` | string | 否 | — | API 令牌列表。 |
| `users` | string | 否 | — | 用户列表。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "移除权限（而非添加）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "groups": {
      "description": "组列表。",
      "format": "pve-groupid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "访问控制路径",
      "type": "string",
      "typetext": "<string>"
    },
    "propagate": {
      "default": 1,
      "description": "允许传播（继承）权限。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "roles": {
      "description": "角色列表。",
      "format": "pve-roleid-list",
      "type": "string",
      "typetext": "<string>"
    },
    "tokens": {
      "description": "API 令牌列表。",
      "format": "pve-tokenid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "users": {
      "description": "用户列表。",
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
