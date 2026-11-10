# `/nodes/{node}/storage/{storage}/upload`

原始接口路径：`/nodes/{node}/storage/{storage}/upload`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/storage/{storage}/upload`

Upload templates, ISO images, OVAs and VM images.

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
| `checksum` | string | 否 | — | The expected checksum of the file. |
| `checksum-algorithm` | string | 否 | — | The algorithm to calculate the checksum of the file.；可选值：`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512` |
| `content` | string | 是 | — | Content type.；可选值：`iso`, `vztmpl`, `import` |
| `filename` | string | 是 | — | The name of the file to create. Caution: This will be normalized! |
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 是 | — | The storage identifier. |
| `tmpfilename` | string | 否 | — | The source file name. This parameter is usually set by the REST handler. You can only overwrite it when connecting to the trusted port on localhost. |

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
    "tmpfilename": {
      "description": "The source file name. This parameter is usually set by the REST handler. You can only overwrite it when connecting to the trusted port on localhost.",
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
