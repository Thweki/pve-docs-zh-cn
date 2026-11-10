# `/cluster/bulk-action/guest/suspend`

原始接口路径：`/cluster/bulk-action/guest/suspend`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/bulk-action/guest/suspend`

批量挂起集群中的所有客户机。

**方法标识：** `suspend`

**权限**

```json
{
  "description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.PowerMgmt' 权限。另外，还需要对 '/vms/{vmid}' 路径具有 'VM.Config.Disk' 权限，以及对已配置的状态存储具有 'Datastore.AllocateSpace' 权限",
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
| `max-workers` | integer | 否 | 4 | 定义并发运行的最大任务数。 |
| `maxworkers` | integer | 否 | 4 | 定义并发运行的最大任务数。已弃用，请改用 'max-workers'。 |
| `statestorage` | string | 否 | — | 存放虚拟机状态的存储。 |
| `to-disk` | boolean | 否 | 0 | 如果设置，则将客户机挂起到磁盘。下次启动时将恢复。 |
| `vms` | array | 否 | — | 仅考虑此 VMID 列表中的客户机。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 4,
      "description": "定义并发运行的最大任务数。",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 4,
      "description": "定义并发运行的最大任务数。已弃用，请改用 'max-workers'。",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "statestorage": {
      "description": "存放虚拟机状态的存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "requires": "to-disk",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "to-disk": {
      "default": 0,
      "description": "如果设置，则将客户机挂起到磁盘。下次启动时将恢复。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/suspend)。
