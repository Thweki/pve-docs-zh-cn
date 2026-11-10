# `/nodes/{node}/storage/{storage}/file-restore/list`

原始接口路径：`/nodes/{node}/storage/{storage}/file-restore/list`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/file-restore/list`

列出给定路径下用于单文件还原的文件和目录。

**方法标识：** `list`

**权限**

```json
{
  "description": "需要具有卷的读取访问权限。",
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
| `filepath` | string | 是 | — | 要列出的目录或文件的 base64 路径，或 "/"。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `volume` | string | 是 | — | 备份卷 ID 或名称。目前仅支持 PBS 快照。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "filepath": {
      "description": "要列出的目录或文件的 base64 路径，或 \"/\"。",
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
    "volume": {
      "description": "备份卷 ID 或名称。目前仅支持 PBS 快照。",
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
        "description": "当前条目的 base64 路径",
        "type": "string"
      },
      "leaf": {
        "description": "此条目是否为目录图中的叶节点。",
        "type": "boolean"
      },
      "mtime": {
        "description": "条目最后修改时间（UNIX 时间戳）。",
        "optional": 1,
        "type": "integer"
      },
      "size": {
        "description": "条目的文件大小。",
        "optional": 1,
        "type": "integer"
      },
      "text": {
        "description": "条目显示文本。",
        "type": "string"
      },
      "type": {
        "description": "条目类型。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/file-restore/list)。
