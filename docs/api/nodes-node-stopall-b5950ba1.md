# `/nodes/{node}/stopall`

原始接口路径：`/nodes/{node}/stopall`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/stopall`

停止所有虚拟机和容器。

**方法标识：** `stopall`

**权限**

```json
{
  "description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.PowerMgmt' 权限。",
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
| `force-stop` | boolean | 否 | 1 | 超时后强制硬停止。 |
| `max-workers` | integer | 否 | — | 定义并发运行的最大任务数。如果  未设置，则使用 'max_workers'（来自 datacenter.cfg）；如果该项也未设置，则使用可用 CPU 线程数，最大限制为 8。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `timeout` | integer | 否 | 180 | 每个客户机关机任务的超时时间。根据 `force-stop` 的设置，超时后仅中止关机或强制硬停止。 |
| `vms` | string | 否 | — | 仅考虑具有这些 ID 的客户机。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force-stop": {
      "default": 1,
      "description": "超时后强制硬停止。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "max-workers": {
      "description": "定义并发运行的最大任务数。如果  未设置，则使用 'max_workers'（来自 datacenter.cfg）；如果该项也未设置，则使用可用 CPU 线程数，最大限制为 8。",
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
    "timeout": {
      "default": 180,
      "description": "每个客户机关机任务的超时时间。根据 `force-stop` 的设置，超时后仅中止关机或强制硬停止。",
      "maximum": 7200,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 7200)"
    },
    "vms": {
      "description": "仅考虑具有这些 ID 的客户机。",
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
