# `/cluster/jobs/schedule-analyze`

原始接口路径：`/cluster/jobs/schedule-analyze`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/jobs/schedule-analyze`

返回未来计划运行时间的列表。

**方法标识：** `schedule-analyze`

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `iterations` | integer | 否 | 10 | 要模拟并返回的事件迭代次数。 |
| `schedule` | string | 是 | — | 作业计划。格式是 `systemd` 日历事件的子集。 |
| `starttime` | integer | 否 | — | 计算起始时间的 UNIX 时间戳。默认为当前时间。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "iterations": {
      "default": 10,
      "description": "要模拟并返回的事件迭代次数。",
      "maximum": 100,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 100)"
    },
    "schedule": {
      "description": "作业计划。格式是 `systemd` 日历事件的子集。",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "starttime": {
      "description": "计算起始时间的 UNIX 时间戳。默认为当前时间。",
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
  "description": "自 <starttime> 起接下来 <iterations> 次事件的数组。",
  "items": {
    "properties": {
      "timestamp": {
        "description": "运行时间的 UNIX 时间戳。",
        "type": "integer"
      },
      "utc": {
        "description": "运行时间的 UTC 时间戳。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/schedule-analyze)。
