# `/nodes/{node}/lxc/{vmid}/status/start`

原始接口路径：`/nodes/{node}/lxc/{vmid}/status/start`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/lxc/{vmid}/status/start`

启动容器。

**方法标识：** `vm_start`

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
| `debug` | boolean | 否 | 0 | 如果设置，则在启动时启用非常详细的 debug 日志级别。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `skiplock` | boolean | 否 | — | 忽略锁——仅 root 可使用此选项。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "debug": {
      "default": 0,
      "description": "如果设置，则在启动时启用非常详细的 debug 日志级别。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/status/start)。
