# `/cluster/metrics/export`

原始接口路径：`/cluster/metrics/export`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/metrics/export`

Retrieve metrics of the cluster.

**方法标识：** `export`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `history` | boolean | 否 | 0 | Also return historic values. Returns full available metric history unless `start-time` is also set |
| `local-only` | boolean | 否 | 0 | Only return metrics for the current node instead of the whole cluster |
| `node-list` | string | 否 | — | Only return metrics from nodes passed as comma-separated list |
| `start-time` | integer | 否 | 0 | Only include metrics with a timestamp &gt; start-time. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "history": {
      "default": 0,
      "description": "Also return historic values. Returns full available metric history unless `start-time` is also set",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "local-only": {
      "default": 0,
      "description": "Only return metrics for the current node instead of the whole cluster",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node-list": {
      "description": "Only return metrics from nodes passed as comma-separated list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "start-time": {
      "default": 0,
      "description": "Only include metrics with a timestamp > start-time.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
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
    "data": {
      "description": "Array of system metrics. Metrics are sorted by their timestamp.",
      "items": {
        "additionalProperties": 0,
        "properties": {
          "id": {
            "description": "Unique identifier for this metric object, for instance 'node/<nodename>' or 'qemu/<vmid>'.",
            "type": "string"
          },
          "metric": {
            "description": "Name of the metric.",
            "type": "string"
          },
          "timestamp": {
            "description": "Time at which this metric was observed",
            "type": "integer"
          },
          "type": {
            "description": "Type of the metric.",
            "enum": [
              "gauge",
              "counter",
              "derive"
            ],
            "type": "string"
          },
          "value": {
            "description": "Metric value.",
            "type": "number"
          }
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

<details>
<summary>其他接口元数据</summary>

```json
{
  "expose_credentials": 1
}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics/export)。
