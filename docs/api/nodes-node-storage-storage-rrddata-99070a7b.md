# `/nodes/{node}/storage/{storage}/rrddata`

原始接口路径：`/nodes/{node}/storage/{storage}/rrddata`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/rrddata`

Read storage RRD statistics.

**方法标识：** `rrddata`

**权限**

```json
{
  "check": [
    "perm",
    "/storage/{storage}",
    [
      "Datastore.Audit",
      "Datastore.AllocateSpace"
    ],
    "any",
    1
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
| `cf` | string | 否 | — | The RRD consolidation function；可选值：`AVERAGE`, `MAX` |
| `node` | string | 是 | — | The cluster node name. |
| `storage` | string | 是 | — | The storage identifier. |
| `timeframe` | string | 是 | — | Specify the time frame you are interested in.；可选值：`hour`, `day`, `week`, `month`, `year` |

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
    "storage": {
      "description": "The storage identifier.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/rrddata)。
