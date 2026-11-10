# `/nodes/{node}/disks/smart`

原始接口路径：`/nodes/{node}/disks/smart`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/disks/smart`

获取磁盘的 SMART 健康状态。

**方法标识：** `smart`

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
| `disk` | string | 是 | — | 块设备名称 |
| `healthonly` | boolean | 否 | — | 如果为 true，则仅返回健康状态 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "disk": {
      "description": "块设备名称",
      "pattern": "^/dev/[a-zA-Z0-9\\/]+$",
      "type": "string"
    },
    "healthonly": {
      "description": "如果为 true，则仅返回健康状态",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
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
  "properties": {
    "attributes": {
      "optional": 1,
      "type": "array"
    },
    "health": {
      "type": "string"
    },
    "text": {
      "optional": 1,
      "type": "string"
    },
    "type": {
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/smart)。
