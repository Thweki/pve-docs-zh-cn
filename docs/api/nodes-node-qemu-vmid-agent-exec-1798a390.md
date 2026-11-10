# `/nodes/{node}/qemu/{vmid}/agent/exec`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/exec`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/agent/exec`

通过 guest-agent 在虚拟机内执行给定命令，并返回包含 pid 的对象。

**方法标识：** `exec`

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
| `command` | array | 是 | — | 命令，以程序及参数列表形式提供。 |
| `input-data` | string | 否 | — | 作为 'input-data' 传递给客户机的数据。通常作为 'command' 的 STDIN。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "command": {
      "description": "命令，以程序及参数列表形式提供。",
      "items": {
        "description": "程序及参数的单个组成部分。",
        "type": "string"
      },
      "type": "array",
      "typetext": "<array>"
    },
    "input-data": {
      "description": "作为 'input-data' 传递给客户机的数据。通常作为 'command' 的 STDIN。",
      "maxLength": 65536,
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
    "pid": {
      "description": "guest-agent 启动的进程的 PID。",
      "type": "integer"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/exec)。
