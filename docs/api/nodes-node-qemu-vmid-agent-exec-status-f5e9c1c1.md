# `/nodes/{node}/qemu/{vmid}/agent/exec-status`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/exec-status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/agent/exec-status`

获取客户机代理启动的给定 pid 的状态

**方法标识：** `exec-status`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.GuestAgent.Unrestricted"
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
| `node` | string | 是 | — | 集群节点名称。 |
| `pid` | integer | 是 | — | 要查询的 PID |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pid": {
      "description": "要查询的 PID",
      "type": "integer",
      "typetext": "<integer>"
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
  "properties": {
    "err-data": {
      "description": "进程的 stderr",
      "optional": 1,
      "type": "string"
    },
    "err-truncated": {
      "description": "如果未完整捕获 stderr，则为 true",
      "optional": 1,
      "type": "boolean"
    },
    "exitcode": {
      "description": "进程正常终止时的退出码。",
      "optional": 1,
      "type": "integer"
    },
    "exited": {
      "description": "表示给定命令是否已经退出。",
      "type": "boolean"
    },
    "out-data": {
      "description": "进程的 stdout",
      "optional": 1,
      "type": "string"
    },
    "out-truncated": {
      "description": "如果未完整捕获 stdout，则为 true",
      "optional": 1,
      "type": "boolean"
    },
    "signal": {
      "description": "进程异常终止时的信号编号或异常代码。",
      "optional": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/exec-status)。
