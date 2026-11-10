# `/nodes/{node}/scan/lvmthin`

原始接口路径：`/nodes/{node}/scan/lvmthin`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/scan/lvmthin`

List local LVM Thin Pools.

**权限**

```json
{
  "check": [
    "perm",
    "/storage",
    [
      "Datastore.Allocate"
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
| `node` | string | 是 | — | The cluster node name. |
| `vg` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "vg": {
      "maxLength": 100,
      "pattern": "[a-zA-Z0-9\\.\\+\\_][a-zA-Z0-9\\.\\+\\_\\-]+",
      "type": "string"
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
      "lv": {
        "description": "The LVM Thin Pool name (LVM logical volume).",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/scan/lvmthin)。
