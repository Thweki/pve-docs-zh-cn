# `/nodes/{node}/vzdump/extractconfig`

原始接口路径：`/nodes/{node}/vzdump/extractconfig`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/vzdump/extractconfig`

从 vzdump 备份归档中提取配置。

**方法标识：** `extractconfig`

**权限**

```json
{
  "description": "用户需要对所备份的客户机 ID 具有 'VM.Backup' 权限，以及对备份存储具有 'Datastore.AllocateSpace' 权限。",
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
| `node` | string | 是 | — | 集群节点名称。 |
| `volume` | string | 是 | — | 卷标识符 |

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
    "volume": {
      "description": "卷标识符",
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
