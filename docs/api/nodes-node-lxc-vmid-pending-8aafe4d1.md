# `/nodes/{node}/lxc/{vmid}/pending`

原始接口路径：`/nodes/{node}/lxc/{vmid}/pending`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/pending`

获取容器配置，包括待处理的更改。

**方法标识：** `vm_pending`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
    ]
  ]
}
```

**允许 API 令牌**

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
  "items": {
    "properties": {
      "delete": {
        "description": "存在且不为 0 时表示有待处理的删除请求。",
        "maximum": 2,
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      },
      "key": {
        "description": "配置选项名称。",
        "type": "string"
      },
      "pending": {
        "description": "待应用的值。",
        "optional": 1,
        "type": "string"
      },
      "value": {
        "description": "当前值。",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/pending)。
