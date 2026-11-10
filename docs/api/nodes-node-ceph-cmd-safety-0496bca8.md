# `/nodes/{node}/ceph/cmd-safety`

原始接口路径：`/nodes/{node}/ceph/cmd-safety`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/cmd-safety`

Heuristical check if it is safe to perform an action.

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
| `action` | string | 是 | — | Action to check；可选值：`stop`, `destroy` |
| `id` | string | 是 | — | ID of the service |
| `node` | string | 是 | — | The cluster node name. |
| `service` | string | 是 | — | Service type；可选值：`osd`, `mon`, `mds` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "Action to check",
      "enum": [
        "stop",
        "destroy"
      ],
      "type": "string"
    },
    "id": {
      "description": "ID of the service",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "service": {
      "description": "Service type",
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
      "description": "True if Ceph reports the requested action is safe.",
      "type": "boolean"
    },
    "status": {
      "description": "Human-readable status message from Ceph (typically the reason an action is not safe); absent when Ceph returned no message.",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/cmd-safety)。
