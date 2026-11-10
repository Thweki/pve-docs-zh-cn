# `/access/roles`

原始接口路径：`/access/roles`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/roles`

Role index.

**方法标识：** `index`

**权限**

```json
{
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
    "properties": {
      "privs": {
        "format": "pve-priv-list",
        "optional": 1,
        "type": "string"
      },
      "roleid": {
        "format": "pve-roleid",
        "type": "string"
      },
      "special": {
        "default": 0,
        "optional": 1,
        "type": "boolean"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{roleid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/access/roles`

Create new role.

**方法标识：** `create_role`

**权限**

```json
{
  "check": [
    "perm",
    "/access",
    [
      "Sys.Modify"
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
| `privs` | string | 否 | — |  |
| `roleid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "privs": {
      "format": "pve-priv-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "roleid": {
      "format": "pve-roleid",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/roles)。
