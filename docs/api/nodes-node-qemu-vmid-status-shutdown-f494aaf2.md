# `/nodes/{node}/qemu/{vmid}/status/shutdown`

原始接口路径：`/nodes/{node}/qemu/{vmid}/status/shutdown`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/status/shutdown`

关闭虚拟机。这类似于按下物理机的电源按钮。此操作会向客户机操作系统发送 ACPI 事件，客户机随后应正常关机。

**方法标识：** `vm_shutdown`

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
| `forceStop` | boolean | 否 | 0 | 确保虚拟机停止。 |
| `keepActive` | boolean | 否 | 0 | 不停用存储卷。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `skiplock` | boolean | 否 | — | 忽略锁——仅 root 可使用此选项。 |
| `timeout` | integer | 否 | — | 最多等待 timeout 秒。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "forceStop": {
      "default": 0,
      "description": "确保虚拟机停止。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "keepActive": {
      "default": 0,
      "description": "不停用存储卷。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/status/shutdown)。
