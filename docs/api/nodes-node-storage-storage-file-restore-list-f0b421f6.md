# `/nodes/{node}/storage/{storage}/file-restore/list`

原始接口路径：`/nodes/{node}/storage/{storage}/file-restore/list`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/file-restore/list`

List files and directories for single file restore under the given path.

**方法标识：** `list`

**权限**

```json
{
  "description": "You need read access for the volume.",
  "user": "all"
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
| `filepath` | string | 是 | — | base64-path to the directory or file being listed, or "/". |
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 是 | — | The storage identifier. |
| `volume` | string | 是 | — | Backup volume ID or name. Currently only PBS snapshots are supported. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "filepath": {
      "description": "base64-path to the directory or file being listed, or \"/\".",
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
    "volume": {
      "description": "Backup volume ID or name. Currently only PBS snapshots are supported.",
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
      "filepath": {
        "description": "base64 path of the current entry",
        "type": "string"
      },
      "leaf": {
        "description": "If this entry is a leaf in the directory graph.",
        "type": "boolean"
      },
      "mtime": {
        "description": "Entry last-modified time (unix timestamp).",
        "optional": 1,
        "type": "integer"
      },
      "size": {
        "description": "Entry file size.",
        "optional": 1,
        "type": "integer"
      },
      "text": {
        "description": "Entry display text.",
        "type": "string"
      },
      "type": {
        "description": "Entry type.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/file-restore/list)。
