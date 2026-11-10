# `/cluster/sdn/dns`

原始接口路径：`/cluster/sdn/dns`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/dns`

SDN dns index.

**权限**

```json
{
  "description": "Only list entries where you have 'SDN.Audit' or 'SDN.Allocate' permissions on '/sdn/dns/<dns>'",
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
| `type` | string | 否 | — | Only list sdn dns of specific type；可选值：`powerdns` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "Only list sdn dns of specific type",
      "enum": [
        "powerdns"
      ],
      "optional": 1,
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
      "dns": {
        "type": "string"
      },
      "type": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{dns}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/sdn/dns`

Create a new sdn dns object.

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
| `dns` | string | 是 | — | The SDN dns object identifier. |
| `fingerprint` | string | 否 | — | Certificate SHA 256 fingerprint. |
| `key` | string | 是 | — |  |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `reversemaskv6` | integer | 否 | — |  |
| `reversev6mask` | integer | 否 | — |  |
| `ttl` | integer | 否 | — |  |
| `type` | string | 是 | — | Plugin type.；可选值：`powerdns` |
| `url` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dns": {
      "description": "The SDN dns object identifier.",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "fingerprint": {
      "description": "Certificate SHA 256 fingerprint.",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "key": {
      "optional": 0,
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "reversemaskv6": {
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "reversev6mask": {
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "ttl": {
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "type": {
      "description": "Plugin type.",
      "enum": [
        "powerdns"
      ],
      "format": "pve-configid",
      "type": "string"
    },
    "url": {
      "optional": 0,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/dns)。
