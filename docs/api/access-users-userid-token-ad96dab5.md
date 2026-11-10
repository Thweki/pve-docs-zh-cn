# `/access/users/{userid}/token`

原始接口路径：`/access/users/{userid}/token`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/users/{userid}/token`

获取用户 API 令牌。

**方法标识：** `token_index`

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
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "userid": {
      "description": "完整用户 ID，采用 `name@realm` 格式。",
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
        "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。",
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "privsep": {
        "default": 1,
        "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。",
        "optional": 1,
        "type": "boolean"
      },
      "tokenid": {
        "description": "用户特定的令牌标识符。",
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
