# `/nodes/{node}/query-url-metadata`

原始接口路径：`/nodes/{node}/query-url-metadata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/query-url-metadata`

查询 URL 的元数据：文件大小、文件名及 MIME 类型。

**方法标识：** `query_url_metadata`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/",
      [
        "Sys.Audit",
        "Sys.Modify"
      ]
    ],
    [
      "perm",
      "/nodes/{node}",
      [
        "Sys.AccessNetwork"
      ]
    ]
  ]
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
| `url` | string | 是 | — | 要查询元数据的 URL。 |
| `verify-certificates` | boolean | 否 | 1 | 如果为 false，则不验证任何 SSL/TLS 证书。 |

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
    },
    "url": {
      "description": "要查询元数据的 URL。",
      "pattern": "https?://.*",
      "type": "string"
    },
    "verify-certificates": {
      "default": 1,
      "description": "如果为 false，则不验证任何 SSL/TLS 证书。",
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
    "mimetype": {
      "optional": 1,
      "type": "string"
    },
    "size": {
      "optional": 1,
      "renderer": "bytes",
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/query-url-metadata)。
