# `/cluster/jobs/schedule-analyze`

原始接口路径：`/cluster/jobs/schedule-analyze`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/jobs/schedule-analyze`

Returns a list of future schedule runtimes.

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
| `iterations` | integer | 否 | 10 | Number of event-iteration to simulate and return. |
| `schedule` | string | 是 | — | Job schedule. The format is a subset of `systemd` calendar events. |
| `starttime` | integer | 否 | — | UNIX timestamp to start the calculation from. Defaults to the current time. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "iterations": {
      "default": 10,
      "description": "Number of event-iteration to simulate and return.",
      "maximum": 100,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 100)"
    },
    "schedule": {
      "description": "Job schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "starttime": {
      "description": "UNIX timestamp to start the calculation from. Defaults to the current time.",
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
  "description": "An array of the next <iterations> events since <starttime>.",
  "items": {
    "properties": {
      "timestamp": {
        "description": "UNIX timestamp for the run.",
        "type": "integer"
      },
      "utc": {
        "description": "UTC timestamp for the run.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/schedule-analyze)。
