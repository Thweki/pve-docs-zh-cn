# `/nodes/{node}/storage/{storage}/rrd`

原始接口路径：`/nodes/{node}/storage/{storage}/rrd`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/storage/{storage}/rrd`

读取存储 RRD 统计信息（返回 PNG）。

**方法标识：** `rrd`

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
| `cf` | string | 否 | — | RRD 合并函数；可选值：`AVERAGE`, `MAX` |
| `ds` | string | 是 | — | 要显示的数据源列表。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `storage` | string | 是 | — | 存储标识符。 |
| `timeframe` | string | 是 | — | 指定您关注的时间范围。；可选值：`hour`, `day`, `week`, `month`, `year` |

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
    "ds": {
      "description": "要显示的数据源列表。",
      "format": "pve-configid-list",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/rrd)。
