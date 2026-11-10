# `/cluster/metrics/export`

原始接口路径：`/cluster/metrics/export`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/metrics/export`

获取集群指标。

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
| `history` | boolean | 否 | 0 | 还返回历史值。除非同时设置 `start-time`，否则返回所有可用的指标历史记录 |
| `local-only` | boolean | 否 | 0 | 仅返回当前节点的指标，而不是整个集群的指标 |
| `node-list` | string | 否 | — | 仅返回以逗号分隔列表传入的节点的指标 |
| `start-time` | integer | 否 | 0 | 仅包含时间戳 &gt; start-time 的指标。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "history": {
      "default": 0,
      "description": "还返回历史值。除非同时设置 `start-time`，否则返回所有可用的指标历史记录",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "local-only": {
      "default": 0,
      "description": "仅返回当前节点的指标，而不是整个集群的指标",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node-list": {
      "description": "仅返回以逗号分隔列表传入的节点的指标",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "start-time": {
      "default": 0,
      "description": "仅包含时间戳 > start-time 的指标。",
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
      "description": "系统指标数组。指标按时间戳排序。",
      "items": {
        "additionalProperties": 0,
        "properties": {
          "id": {
            "description": "此指标对象的唯一标识符，例如 'node/<nodename>' 或 'qemu/<vmid>'。",
            "type": "string"
          },
          "metric": {
            "description": "指标名称。",
            "type": "string"
          },
          "timestamp": {
            "description": "观测到此指标的时间",
            "type": "integer"
          },
          "type": {
            "description": "指标类型。",
            "enum": [
              "gauge",
              "counter",
              "derive"
            ],
            "type": "string"
          },
          "value": {
            "description": "指标值。",
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
