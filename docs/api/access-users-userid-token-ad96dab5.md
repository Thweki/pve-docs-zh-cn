# `/access/users/{userid}/token`

原始接口路径：`/access/users/{userid}/token`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/users/{userid}/token`

Get user API tokens.

**权限**

```json
{
  "check": [
    "or",
    [
      "userid-param",
      "self"
    ],
    [
      "userid-group",
      [
        "User.Modify"
      ]
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
      "format": "pve-userid",
      "maxLength": 64,
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
      "comment": {
        "optional": 1,
        "type": "string"
      },
      "expire": {
        "default": "same as user",
        "description": "API token expiration date (seconds since epoch). '0' means no expiration date.",
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "privsep": {
        "default": 1,
        "description": "Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.",
        "optional": 1,
        "type": "boolean"
      },
      "tokenid": {
        "description": "User-specific token identifier.",
        "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{tokenid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/token)。
