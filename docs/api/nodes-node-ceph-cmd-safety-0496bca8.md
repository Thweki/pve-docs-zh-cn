# `/nodes/{node}/ceph/cmd-safety`

原始接口路径：`/nodes/{node}/ceph/cmd-safety`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/cmd-safety`

启发式检查执行操作是否安全。

**方法标识：** `cmd_safety`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
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
| `action` | string | 是 | — | 要检查的操作；可选值：`stop`, `destroy` |
| `id` | string | 是 | — | 服务 ID |
| `node` | string | 是 | — | 集群节点名称。 |
| `service` | string | 是 | — | 服务类型；可选值：`osd`, `mon`, `mds` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "要检查的操作",
      "enum": [
        "stop",
        "destroy"
      ],
      "type": "string"
    },
    "id": {
      "description": "服务 ID",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "service": {
      "description": "服务类型",
      "enum": [
        "osd",
        "mon",
        "mds"
      ],
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "additionalProperties": 0,
  "properties": {
    "safe": {
      "description": "如果 Ceph 报告请求的操作安全，则为 true。",
      "type": "boolean"
    },
    "status": {
      "description": "Ceph 的人类可读状态消息（通常为操作不安全的原因）；Ceph 未返回消息时不存在此项。",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/cmd-safety)。
