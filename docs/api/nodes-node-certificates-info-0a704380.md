# `/nodes/{node}/certificates/info`

原始接口路径：`/nodes/{node}/certificates/info`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/certificates/info`

获取节点证书的信息。

**方法标识：** `info`

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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
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
      "filename": {
        "optional": 1,
        "type": "string"
      },
      "fingerprint": {
        "description": "证书 SHA 256 指纹。",
        "optional": 1,
        "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}",
        "type": "string"
      },
      "issuer": {
        "description": "证书颁发者名称。",
        "optional": 1,
        "type": "string"
      },
      "notafter": {
        "description": "证书的 notAfter 时间戳（UNIX 纪元）。",
        "optional": 1,
        "renderer": "timestamp",
        "type": "integer"
      },
      "notbefore": {
        "description": "证书的 notBefore 时间戳（UNIX 纪元）。",
        "optional": 1,
        "renderer": "timestamp",
        "type": "integer"
      },
      "pem": {
        "description": "PEM 格式的证书",
        "format": "pem-certificate",
        "optional": 1,
        "type": "string"
      },
      "public-key-bits": {
        "description": "证书公钥大小",
        "optional": 1,
        "type": "integer"
      },
      "public-key-type": {
        "description": "证书公钥算法",
        "optional": 1,
        "type": "string"
      },
      "san": {
        "description": "证书 SubjectAlternativeName 条目列表。",
        "items": {
          "type": "string"
        },
        "optional": 1,
        "renderer": "yaml",
        "type": "array"
      },
      "subject": {
        "description": "证书主体名称。",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/certificates/info)。
