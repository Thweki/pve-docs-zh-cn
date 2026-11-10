# `/nodes/{node}/stopall`

原始接口路径：`/nodes/{node}/stopall`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/stopall`

Stop all VMs and Containers.

**权限**

```json
{
  "description": "The 'VM.PowerMgmt' permission is required on '/' or on '/vms/<ID>' for each ID passed via the 'vms' parameter.",
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
| `force-stop` | boolean | 否 | 1 | Force a hard-stop after the timeout. |
| `max-workers` | integer | 否 | — | Defines the maximum number of tasks running concurrently. If not set, uses 'max_workers' from datacenter.cfg, and if that's not set, the available CPU threads, clamped to a maximum of 8, are used. |
| `node` | string | 是 | — | The cluster node name. |
| `timeout` | integer | 否 | 180 | Timeout for each guest shutdown task. Depending on `force-stop`, the shutdown gets then simply aborted or a hard-stop is forced. |
| `vms` | string | 否 | — | Only consider Guests with these IDs. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force-stop": {
      "default": 1,
      "description": "Force a hard-stop after the timeout.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "max-workers": {
      "description": "Defines the maximum number of tasks running concurrently. If not set, uses 'max_workers' from datacenter.cfg, and if that's not set, the available CPU threads, clamped to a maximum of 8, are used.",
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
    "timeout": {
      "default": 180,
      "description": "Timeout for each guest shutdown task. Depending on `force-stop`, the shutdown gets then simply aborted or a hard-stop is forced.",
      "maximum": 7200,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 7200)"
    },
    "vms": {
      "description": "Only consider Guests with these IDs.",
      "format": "pve-vmid-list",
      "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/stopall)。
