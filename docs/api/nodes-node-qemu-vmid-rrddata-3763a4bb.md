# `/nodes/{node}/qemu/{vmid}/rrddata`

原始接口路径：`/nodes/{node}/qemu/{vmid}/rrddata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/rrddata`

读取虚拟机 RRD 统计信息

**方法标识：** `rrddata`

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

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `cf` | string | 否 | — | RRD 合并函数；可选值：`AVERAGE`, `MAX` |
| `node` | string | 是 | — | 集群节点名称。 |
| `timeframe` | string | 是 | — | 指定您关注的时间范围。；可选值：`hour`, `day`, `week`, `month`, `year` |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cf": {
      "description": "RRD 合并函数",
      "enum": [
        "AVERAGE",
        "MAX"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "timeframe": {
      "description": "指定您关注的时间范围。",
      "enum": [
        "hour",
        "day",
        "week",
        "month",
        "year"
      ],
      "type": "string"
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
    "properties": {},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/rrddata)。
