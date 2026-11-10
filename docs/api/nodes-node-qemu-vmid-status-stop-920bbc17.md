# `/nodes/{node}/qemu/{vmid}/status/stop`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/stop`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/stop`

停止虚拟机。qemu 进程将立即退出。这类似于拔掉运行中计算机的电源插头，可能损坏虚拟机数据。

**方法标识：** `vm_stop`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.PowerMgmt"
    ]
  ]
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
| `keepActive` | boolean | 否 | 0 | 不停用存储卷。 |
| `migratedfrom` | string | 否 | — | 集群节点名称。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `overrule-shutdown` | boolean | 否 | 0 | 停止前尝试中止活动的 'qmshutdown' 任务。 |
| `skiplock` | boolean | 否 | — | 忽略锁——仅 root 可使用此选项。 |
| `timeout` | integer | 否 | — | 最多等待 timeout 秒。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "keepActive": {
      "default": 0,
      "description": "不停用存储卷。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "migratedfrom": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "overrule-shutdown": {
      "default": 0,
      "description": "停止前尝试中止活动的 'qmshutdown' 任务。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "skiplock": {
      "description": "忽略锁——仅 root 可使用此选项。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "timeout": {
      "description": "最多等待 timeout 秒。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/stop)。
