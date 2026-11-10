# `/cluster/sdn/ipams`

原始接口路径：`/cluster/sdn/ipams`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/ipams`

SDN ipam 索引。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/sdn/ipams/<ipam>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目",
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
| `type` | string | 否 | — | 仅列出特定类型的 SDN ipam；可选值：`netbox`, `phpipam`, `pve` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "仅列出特定类型的 SDN ipam",
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

创建新的 SDN ipam 对象。

**方法标识：** `create`

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
| `fingerprint` | string | 否 | — | 证书 SHA 256 指纹。 |
| `ipam` | string | 是 | — | SDN ipam 对象标识符。 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `section` | integer | 否 | — |  |
| `token` | string | 否 | — |  |
| `type` | string | 是 | — | 插件类型。；可选值：`netbox`, `phpipam`, `pve` |
| `url` | string | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {
      "description": "证书 SHA 256 指纹。",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "ipam": {
      "description": "SDN ipam 对象标识符。",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
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
      "description": "插件类型。",
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
