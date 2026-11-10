# `/nodes/{node}/certificates/custom`

原始接口路径：`/nodes/{node}/certificates/custom`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/certificates/custom`

DELETE custom certificate chain and key.

**方法标识：** `remove_custom_cert`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `restart` | boolean | 否 | 0 | Restart pveproxy. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "restart": {
      "default": 0,
      "description": "Restart pveproxy.",
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

## POST `/nodes/{node}/certificates/custom`

Upload or update custom certificate chain and key.

**方法标识：** `upload_custom_cert`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `certificates` | string | 是 | — | PEM encoded certificate (chain). |
| `force` | boolean | 否 | 0 | Overwrite existing custom or ACME certificate files. |
| `key` | string | 否 | — | PEM encoded private key. |
| `node` | string | 是 | — | The cluster node name. |
| `restart` | boolean | 否 | 0 | Restart pveproxy. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "certificates": {
      "description": "PEM encoded certificate (chain).",
      "format": "pem-certificate-chain",
      "type": "string",
      "typetext": "<string>"
    },
    "force": {
      "default": 0,
      "description": "Overwrite existing custom or ACME certificate files.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "key": {
      "description": "PEM encoded private key.",
      "format": "pem-string",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "restart": {
      "default": 0,
      "description": "Restart pveproxy.",
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
  "properties": {
    "filename": {
      "optional": 1,
      "type": "string"
    },
    "fingerprint": {
      "description": "Certificate SHA 256 fingerprint.",
      "optional": 1,
      "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
      "type": "string"
    },
    "issuer": {
      "description": "Certificate issuer name.",
      "optional": 1,
      "type": "string"
    },
    "notafter": {
      "description": "Certificate's notAfter timestamp (UNIX epoch).",
      "optional": 1,
      "renderer": "timestamp",
      "type": "integer"
    },
    "notbefore": {
      "description": "Certificate's notBefore timestamp (UNIX epoch).",
      "optional": 1,
      "renderer": "timestamp",
      "type": "integer"
    },
    "pem": {
      "description": "Certificate in PEM format",
      "format": "pem-certificate",
      "optional": 1,
      "type": "string"
    },
    "public-key-bits": {
      "description": "Certificate's public key size",
      "optional": 1,
      "type": "integer"
    },
    "public-key-type": {
      "description": "Certificate's public key algorithm",
      "optional": 1,
      "type": "string"
    },
    "san": {
      "description": "List of Certificate's SubjectAlternativeName entries.",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "renderer": "yaml",
      "type": "array"
    },
    "subject": {
      "description": "Certificate subject name.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/certificates/custom)。
