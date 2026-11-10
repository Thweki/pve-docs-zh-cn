# `/cluster/sdn/dns/{dns}`

原始接口路径：`/cluster/sdn/dns/{dns}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/dns/{dns}`

删除 SDN DNS 对象配置。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/dns",
    [
      "SDN.Allocate"
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
| `dns` | string | 是 | — | SDN DNS 对象标识符。 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dns": {
      "description": "SDN DNS 对象标识符。",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
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

## GET `/cluster/sdn/dns/{dns}`

读取 SDN DNS 配置。

**方法标识：** `read`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/dns/{dns}",
    [
      "SDN.Allocate"
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
| `dns` | string | 是 | — | SDN DNS 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dns": {
      "description": "SDN DNS 对象标识符。",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "object"
}
```

## PUT `/cluster/sdn/dns/{dns}`

更新 SDN DNS 对象配置。

**方法标识：** `update`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/dns",
    [
      "SDN.Allocate"
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
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dns` | string | 是 | — | SDN DNS 对象标识符。 |
| `fingerprint` | string | 否 | — | 证书 SHA 256 指纹。 |
| `key` | string | 否 | — |  |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `reversemaskv6` | integer | 否 | — |  |
| `ttl` | integer | 否 | — |  |
| `url` | string | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dns": {
      "description": "SDN DNS 对象标识符。",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "fingerprint": {
      "description": "证书 SHA 256 指纹。",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "key": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "reversemaskv6": {
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "ttl": {
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "url": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/dns/{dns})。
