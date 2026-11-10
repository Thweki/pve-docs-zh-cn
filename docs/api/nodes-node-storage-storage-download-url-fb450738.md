# `/nodes/{node}/storage/{storage}/download-url`

原始接口路径：`/nodes/{node}/storage/{storage}/download-url`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/storage/{storage}/download-url`

通过 URL 下载模板、ISO 镜像、OVA 和虚拟机镜像。

**方法标识：** `download_url`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/storage/{storage}",
      [
        "Datastore.AllocateTemplate"
      ]
    ],
    [
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
  ],
  "description": "需要对存储具有分配访问权限；由于此操作允许间接探测宿主机的本地网络，因此还需要对 / 具有 Sys.Modify 权限（为向后兼容），或对节点具有较新的 Sys.AccessNetwork 权限。"
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
| `checksum` | string | 否 | — | 文件的预期校验和。 |
| `checksum-algorithm` | string | 否 | — | 计算文件校验和的算法。；可选值：`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512` |
| `compression` | string | 否 | — | 使用指定压缩算法解压下载的文件。 |
| `content` | string | 是 | — | 内容类型。；可选值：`iso`, `vztmpl`, `import` |
| `filename` | string | 是 | — | 要创建的文件名称。注意：此名称将被规范化！ |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `url` | string | 是 | — | 下载文件的 URL。 |
| `verify-certificates` | boolean | 否 | 1 | 如果为 false，则不验证任何 SSL/TLS 证书。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "checksum": {
      "description": "文件的预期校验和。",
      "optional": 1,
      "requires": "checksum-algorithm",
      "type": "string",
      "typetext": "<string>"
    },
    "checksum-algorithm": {
      "description": "计算文件校验和的算法。",
      "enum": [
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512"
      ],
      "optional": 1,
      "requires": "checksum",
      "type": "string"
    },
    "compression": {
      "description": "使用指定压缩算法解压下载的文件。",
      "enum": null,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "content": {
      "description": "内容类型。",
      "enum": [
        "iso",
        "vztmpl",
        "import"
      ],
      "format": "pve-storage-content",
      "type": "string"
    },
    "filename": {
      "description": "要创建的文件名称。注意：此名称将被规范化！",
      "maxLength": 255,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "url": {
      "description": "下载文件的 URL。",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/download-url)。
