# `/nodes/{node}/disks/lvm/{name}`

原始接口路径：`/nodes/{node}/disks/lvm/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/disks/lvm/{name}`

移除 LVM 卷组。

**方法标识：** `delete`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
  ],
  "description": "设置 'cleanup-config' 时，还需要对 /storage 具有 'Datastore.Allocate' 权限"
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
| `cleanup-config` | boolean | 否 | 0 | 将关联存储标记为在此节点上不再可用，或从配置中移除（如果仅为此节点配置）。 |
| `cleanup-disks` | boolean | 否 | 0 | 同时擦除磁盘，以便后续改作他用。 |
| `name` | string | 是 | — | 存储标识符。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cleanup-config": {
      "default": 0,
      "description": "将关联存储标记为在此节点上不再可用，或从配置中移除（如果仅为此节点配置）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cleanup-disks": {
      "default": 0,
      "description": "同时擦除磁盘，以便后续改作他用。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/lvm/{name})。
