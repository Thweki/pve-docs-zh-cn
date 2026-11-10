# `/cluster/firewall/aliases`

原始接口路径：`/cluster/firewall/aliases`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/aliases`

列出别名

**方法标识：** `get_aliases`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
    ]
  ]
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
      "cidr": {
        "type": "string"
      },
      "comment": {
        "optional": 1,
        "type": "string"
      },
      "digest": {
        "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
        "maxLength": 64,
        "optional": 0,
        "type": "string"
      },
      "name": {
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

## POST `/cluster/firewall/aliases`

创建 IP 或网络别名。

**方法标识：** `create_alias`

**权限**

```json
{
  "check": [
    "perm",
    "/",
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
| `cidr` | string | 是 | — | CIDR 格式的网络/IP 规范。 |
| `comment` | string | 否 | — |  |
| `name` | string | 是 | — | 别名名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {
      "description": "CIDR 格式的网络/IP 规范。",
      "format": "IPorCIDR",
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "format": "pve-fw-comment-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "name": {
      "description": "别名名称。",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/aliases)。
