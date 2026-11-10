# `/cluster/bulk-action/guest/suspend`

原始接口路径：`/cluster/bulk-action/guest/suspend`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/bulk-action/guest/suspend`

Bulk suspend all guests on the cluster.

**方法标识：** `suspend`

**权限**

```json
{
  "description": "The 'VM.PowerMgmt' permission is required on '/' or on '/vms/<ID>' for each ID passed via the 'vms' parameter. Additionally, you need 'VM.Config.Disk' on the '/vms/{vmid}' path and 'Datastore.AllocateSpace' for the configured state-storage(s)",
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
| `max-workers` | integer | 否 | 4 | Defines the maximum number of tasks running concurrently. |
| `maxworkers` | integer | 否 | 4 | Defines the maximum number of tasks running concurrently. Deprecated, use 'max-workers' instead. |
| `statestorage` | string | 否 | — | The storage for the VM state. |
| `to-disk` | boolean | 否 | 0 | If set, suspends the guests to disk. Will be resumed on next start. |
| `vms` | array | 否 | — | Only consider guests from this list of VMIDs. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 4,
      "description": "Defines the maximum number of tasks running concurrently.",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 4,
      "description": "Defines the maximum number of tasks running concurrently. Deprecated, use 'max-workers' instead.",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "statestorage": {
      "description": "The storage for the VM state.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "requires": "to-disk",
      "type": "string",
      "typetext": "<storage ID>"
    },
    "to-disk": {
      "default": 0,
      "description": "If set, suspends the guests to disk. Will be resumed on next start.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vms": {
      "description": "Only consider guests from this list of VMIDs.",
      "items": {
        "description": "The (unique) ID of the VM.",
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
  "description": "UPID of the worker",
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
