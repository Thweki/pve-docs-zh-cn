# `/nodes/{node}/migrateall`

原始接口路径：`/nodes/{node}/migrateall`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/migrateall`

Migrate all VMs and Containers.

**权限**

```json
{
  "description": "The 'VM.Migrate' permission is required on '/' or on '/vms/<ID>' for each ID passed via the 'vms' parameter.",
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
| `max-workers` | integer | 否 | — | Maximal number of parallel migration job. If not set, uses'max_workers' from datacenter.cfg. One of both must be set! |
| `maxworkers` | integer | 否 | — | Maximal number of parallel migration job. If not set, uses'max_workers' from datacenter.cfg. One of both must be set!Deprecated, use 'max-workers' instead. |
| `node` | string | 是 | — | The cluster node name. |
| `target` | string | 是 | — | Target node. |
| `vms` | string | 否 | — | Only consider Guests with these IDs. |
| `with-local-disks` | boolean | 否 | — | Enable live storage migration for local disk |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "description": "Maximal number of parallel migration job. If not set, uses'max_workers' from datacenter.cfg. One of both must be set!",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "description": "Maximal number of parallel migration job. If not set, uses'max_workers' from datacenter.cfg. One of both must be set!Deprecated, use 'max-workers' instead.",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "vms": {
      "description": "Only consider Guests with these IDs.",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "with-local-disks": {
      "description": "Enable live storage migration for local disk",
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
