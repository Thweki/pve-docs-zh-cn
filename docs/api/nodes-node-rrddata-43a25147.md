# `/nodes/{node}/rrddata`

原始接口路径：`/nodes/{node}/rrddata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/rrddata`

Read node RRD statistics

**方法标识：** `rrddata`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `cf` | string | 否 | — | The RRD consolidation function；可选值：`AVERAGE`, `MAX` |
| `node` | string | 是 | — | The cluster node name. |
| `timeframe` | string | 是 | — | Specify the time frame you are interested in.；可选值：`hour`, `day`, `week`, `month`, `year`, `decade` |

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
        "year",
        "decade"
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
  "items": {
    "properties": {},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/rrddata)。
