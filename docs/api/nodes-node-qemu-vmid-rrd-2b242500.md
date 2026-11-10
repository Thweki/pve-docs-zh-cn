# `/nodes/{node}/qemu/{vmid}/rrd`

原始接口路径：`/nodes/{node}/qemu/{vmid}/rrd`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/rrd`

Read VM RRD statistics (returns PNG)

**方法标识：** `rrd`

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
| `cf` | string | 否 | — | The RRD consolidation function；可选值：`AVERAGE`, `MAX` |
| `ds` | string | 是 | — | The list of datasources you want to display. |
| `node` | string | 是 | — | The cluster node name. |
| `timeframe` | string | 是 | — | Specify the time frame you are interested in.；可选值：`hour`, `day`, `week`, `month`, `year` |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cf": {
      "description": "The RRD consolidation function",
      "enum": [
        "AVERAGE",
        "MAX"
      ],
      "optional": 1,
      "type": "string"
    },
    "ds": {
      "description": "The list of datasources you want to display.",
      "format": "pve-configid-list",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "timeframe": {
      "description": "Specify the time frame you are interested in.",
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
      "description": "The (unique) ID of the VM.",
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
    "filename": {
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/rrd)。
