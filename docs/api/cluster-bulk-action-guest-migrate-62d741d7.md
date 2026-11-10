# `/cluster/bulk-action/guest/migrate`

原始接口路径：`/cluster/bulk-action/guest/migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/bulk-action/guest/migrate`

批量迁移集群中的所有客户机。

**方法标识：** `migrate`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `max-workers` | integer | 否 | 1 | 定义并发运行的最大任务数。 |
| `maxworkers` | integer | 否 | 1 | 定义并发运行的最大任务数。已弃用，请改用 'max-workers'。 |
| `online` | boolean | 否 | — | 为虚拟机启用在线迁移，为容器启用重启迁移。 |
| `target` | string | 是 | — | 目标节点。 |
| `vms` | array | 否 | — | 仅考虑此 VMID 列表中的客户机。 |
| `with-local-disks` | boolean | 否 | — | 为本地磁盘启用在线存储迁移 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 1,
      "description": "定义并发运行的最大任务数。",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 1,
      "description": "定义并发运行的最大任务数。已弃用，请改用 'max-workers'。",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "online": {
      "description": "为虚拟机启用在线迁移，为容器启用重启迁移。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "target": {
      "description": "目标节点。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "vms": {
      "description": "仅考虑此 VMID 列表中的客户机。",
      "items": {
        "description": "虚拟机的（唯一）ID。",
        "format": "pve-vmid",
        "maximum": 999999999,
        "minimum": 100,
        "type": "integer"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
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
  "description": "工作任务的 UPID",
  "type": "string"
}
```

<details>
<summary>其他接口元数据</summary>

```json
{
  "expose_credentials": 1
}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/migrate)。
