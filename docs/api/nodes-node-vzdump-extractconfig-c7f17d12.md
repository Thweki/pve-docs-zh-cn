# `/nodes/{node}/vzdump/extractconfig`

原始接口路径：`/nodes/{node}/vzdump/extractconfig`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/vzdump/extractconfig`

Extract configuration from vzdump backup archive.

**方法标识：** `extractconfig`

**权限**

```json
{
  "description": "The user needs 'VM.Backup' permissions on the backed up guest ID, and 'Datastore.AllocateSpace' on the backup storage.",
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
| `node` | string | 是 | — | The cluster node name. |
| `volume` | string | 是 | — | Volume identifier |

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
    "volume": {
      "description": "Volume identifier",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/vzdump/extractconfig)。
