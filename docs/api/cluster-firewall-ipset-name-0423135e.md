# `/cluster/firewall/ipset/{name}`

原始接口路径：`/cluster/firewall/ipset/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/firewall/ipset/{name}`

删除 IPSet

**方法标识：** `delete_ipset`

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
| `force` | boolean | 否 | — | 删除 IPSet 中的所有成员（如有）。 |
| `name` | string | 是 | — | IP 集合名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "description": "删除 IPSet 中的所有成员（如有）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "IP 集合名称。",
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

## GET `/cluster/firewall/ipset/{name}`

列出 IPSet 内容

**方法标识：** `get_ipset`

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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | string | 是 | — | IP 集合名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "IP 集合名称。",
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
      "nomatch": {
        "optional": 1,
        "type": "boolean"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{cidr}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/firewall/ipset/{name}`

将 IP 或网络添加到 IPSet。

**方法标识：** `create_ip`

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
| `name` | string | 是 | — | IP 集合名称。 |
| `nomatch` | boolean | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {
      "description": "CIDR 格式的网络/IP 规范。",
      "format": "IPorCIDRorAlias",
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
      "description": "IP 集合名称。",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
      "type": "string"
    },
    "nomatch": {
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/ipset/{name})。
