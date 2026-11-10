# `/nodes/{node}/migrateall`

原始接口路径：`/nodes/{node}/migrateall`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/migrateall`

迁移所有虚拟机和容器。

**方法标识：** `migrateall`

**权限**

```json
{
  "description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.Migrate' 权限。",
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
| `max-workers` | integer | 否 | — | 并行迁移作业的最大数量。如果未设置，则使用 'max_workers'（来自 datacenter.cfg）。两者必须至少设置一个！ |
| `maxworkers` | integer | 否 | — | 并行迁移作业的最大数量。如果未设置，则使用 'max_workers'（来自 datacenter.cfg）。两者必须至少设置一个！已弃用，请改用 'max-workers'。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `target` | string | 是 | — | 目标节点。 |
| `vms` | string | 否 | — | 仅考虑具有这些 ID 的客户机。 |
| `with-local-disks` | boolean | 否 | — | 为本地磁盘启用在线存储迁移 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "description": "并行迁移作业的最大数量。如果未设置，则使用 'max_workers'（来自 datacenter.cfg）。两者必须至少设置一个！",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "description": "并行迁移作业的最大数量。如果未设置，则使用 'max_workers'（来自 datacenter.cfg）。两者必须至少设置一个！已弃用，请改用 'max-workers'。",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "target": {
      "description": "目标节点。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "vms": {
      "description": "仅考虑具有这些 ID 的客户机。",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "with-local-disks": {
      "description": "为本地磁盘启用在线存储迁移",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/migrateall)。
