# `/cluster/sdn/ipams`

原始接口路径：`/cluster/sdn/ipams`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/ipams`

SDN ipams index.

**权限**

```json
{
  "description": "Only list entries where you have 'SDN.Audit' or 'SDN.Allocate' permissions on '/sdn/ipams/<ipam>'",
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
| `type` | string | 否 | — | Only list sdn ipams of specific type；可选值：`netbox`, `phpipam`, `pve` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "Only list sdn ipams of specific type",
      "enum": [
        "netbox",
        "phpipam",
        "pve"
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
      "ipam": {
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
      "href": "{ipam}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/sdn/ipams`

Create a new sdn ipam object.

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/ipams",
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
| `fingerprint` | string | 否 | — | Certificate SHA 256 fingerprint. |
| `ipam` | string | 是 | — | The SDN ipam object identifier. |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `section` | integer | 否 | — |  |
| `token` | string | 否 | — |  |
| `type` | string | 是 | — | Plugin type.；可选值：`netbox`, `phpipam`, `pve` |
| `url` | string | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {
      "description": "Certificate SHA 256 fingerprint.",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "ipam": {
      "description": "The SDN ipam object identifier.",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "section": {
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "token": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "Plugin type.",
      "enum": [
        "netbox",
        "phpipam",
        "pve"
      ],
      "format": "pve-configid",
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/ipams)。
