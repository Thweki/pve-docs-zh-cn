# `/nodes/{node}/storage/{storage}/upload`

原始接口路径：`/nodes/{node}/storage/{storage}/upload`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/storage/{storage}/upload`

上传模板、ISO 镜像、OVA 和虚拟机镜像。

**方法标识：** `upload`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.AllocateTemplate"
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
| `checksum` | string | 否 | — | 文件的预期校验和。 |
| `checksum-algorithm` | string | 否 | — | 计算文件校验和的算法。；可选值：`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512` |
| `content` | string | 是 | — | 内容类型。；可选值：`iso`, `vztmpl`, `import` |
| `filename` | string | 是 | — | 要创建的文件名称。注意：此名称将被规范化！ |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `tmpfilename` | string | 否 | — | 源文件名。此参数通常由 REST 处理程序设置。仅在连接到 localhost 的受信任端口时才能覆盖。 |

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
    "tmpfilename": {
      "description": "源文件名。此参数通常由 REST 处理程序设置。仅在连接到 localhost 的受信任端口时才能覆盖。",
      "optional": 1,
      "pattern": "/var/tmp/pveupload-[0-9a-f]+",
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/upload)。
