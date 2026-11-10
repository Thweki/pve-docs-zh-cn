# `/nodes/{node}/storage/{storage}/file-restore/download`

原始接口路径：`/nodes/{node}/storage/{storage}/file-restore/download`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/file-restore/download`

从 PBS 备份提取文件或目录（作为 zip 归档）。

**方法标识：** `download`

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
| `filepath` | string | 是 | — | 要下载的目录或文件的 base64 路径。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `tar` | boolean | 否 | 0 | 将目录下载为 'tar.zst' 而非 'zip'。 |
| `volume` | string | 是 | — | 备份卷 ID 或名称。目前仅支持 PBS 快照。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "filepath": {
      "description": "要下载的目录或文件的 base64 路径。",
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
    "tar": {
      "default": 0,
      "description": "将目录下载为 'tar.zst' 而非 'zip'。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
  "type": "any"
}
```

<details>
<summary>其他接口元数据</summary>

```json
{
  "download_allowed": 1
}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/file-restore/download)。
