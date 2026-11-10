# `/cluster/bulk-action/guest/migrate`

原始接口路径：`/cluster/bulk-action/guest/migrate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/bulk-action/guest/migrate`

Bulk migrate all guests on the cluster.

**方法标识：** `migrate`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `max-workers` | integer | 否 | 1 | Defines the maximum number of tasks running concurrently. |
| `maxworkers` | integer | 否 | 1 | Defines the maximum number of tasks running concurrently. Deprecated, use 'max-workers' instead. |
| `online` | boolean | 否 | — | Enable live migration for VMs and restart migration for CTs. |
| `target` | string | 是 | — | Target node. |
| `vms` | array | 否 | — | Only consider guests from this list of VMIDs. |
| `with-local-disks` | boolean | 否 | — | Enable live storage migration for local disk |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 1,
      "description": "Defines the maximum number of tasks running concurrently.",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 1,
      "description": "Defines the maximum number of tasks running concurrently. Deprecated, use 'max-workers' instead.",
      "maximum": 64,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "online": {
      "description": "Enable live migration for VMs and restart migration for CTs.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/migrate)。
