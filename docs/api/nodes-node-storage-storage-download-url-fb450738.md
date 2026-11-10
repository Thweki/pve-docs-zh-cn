# `/nodes/{node}/storage/{storage}/download-url`

原始接口路径：`/nodes/{node}/storage/{storage}/download-url`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/storage/{storage}/download-url`

Download templates, ISO images, OVAs and VM images by using an URL.

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
  "description": "Requires allocation access on the storage and as this allows one to probe the (local!) host network indirectly it also requires one of Sys.Modify on / (for backwards compatibility) or the newer Sys.AccessNetwork privilege on the node."
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
| `checksum` | string | 否 | — | The expected checksum of the file. |
| `checksum-algorithm` | string | 否 | — | The algorithm to calculate the checksum of the file.；可选值：`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512` |
| `compression` | string | 否 | — | Decompress the downloaded file using the specified compression algorithm. |
| `content` | string | 是 | — | Content type.；可选值：`iso`, `vztmpl`, `import` |
| `filename` | string | 是 | — | The name of the file to create. Caution: This will be normalized! |
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 是 | — | The storage identifier. |
| `url` | string | 是 | — | The URL to download the file from. |
| `verify-certificates` | boolean | 否 | 1 | If false, no SSL/TLS certificates will be verified. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "checksum": {
      "description": "The expected checksum of the file.",
      "optional": 1,
      "requires": "checksum-algorithm",
      "type": "string",
      "typetext": "<string>"
    },
    "checksum-algorithm": {
      "description": "The algorithm to calculate the checksum of the file.",
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
      "description": "Decompress the downloaded file using the specified compression algorithm.",
      "enum": null,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "content": {
      "description": "Content type.",
      "enum": [
        "iso",
        "vztmpl",
        "import"
      ],
      "format": "pve-storage-content",
      "type": "string"
    },
    "filename": {
      "description": "The name of the file to create. Caution: This will be normalized!",
      "maxLength": 255,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "url": {
      "description": "The URL to download the file from.",
      "pattern": "https?://.*",
      "type": "string"
    },
    "verify-certificates": {
      "default": 1,
      "description": "If false, no SSL/TLS certificates will be verified.",
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
