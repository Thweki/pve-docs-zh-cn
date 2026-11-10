# `/cluster/replication`

原始接口路径：`/cluster/replication`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/replication`

列出复制任务。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅返回调用用户在 /vms/<vmid> 上拥有 VM.Audit 权限的复制任务。",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "comment": {
        "description": "描述。",
        "maxLength": 4096,
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "description": "用于禁用/停用条目的标志。",
        "optional": 1,
        "type": "boolean"
      },
      "guest": {
        "description": "客户机 ID。",
        "type": "integer"
      },
      "id": {
        "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。",
        "format": "pve-replication-job-id",
        "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
        "type": "string"
      },
      "jobnum": {
        "description": "分配给每个任务的唯一连续 ID。",
        "type": "integer"
      },
      "rate": {
        "description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。",
        "minimum": 1,
        "optional": 1,
        "type": "number"
      },
      "remove_job": {
        "description": "将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。",
        "enum": [
          "local",
          "full"
        ],
        "optional": 1,
        "type": "string"
      },
      "schedule": {
        "default": "*/15",
        "description": "存储复制计划。其格式是 `systemd` 日历事件的一个子集。",
        "format": "pve-calendar-event",
        "maxLength": 128,
        "optional": 1,
        "type": "string"
      },
      "source": {
        "description": "供内部使用，用于检测客户机是否被接管。",
        "format": "pve-node",
        "optional": 1,
        "type": "string"
      },
      "target": {
        "description": "目标节点。",
        "format": "pve-node",
        "optional": 0,
        "type": "string"
      },
      "type": {
        "description": "节类型。",
        "enum": [
          "local"
        ],
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/replication`

创建新的复制任务

**方法标识：** `create`

**权限**

```json
{
  "description": "需要在 /vms/<vmid> 上拥有 VM.Replicate 权限。",
  "user": "all"
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
| `comment` | string | 否 | — | 描述。 |
| `disable` | boolean | 否 | — | 用于禁用/停用条目的标志。 |
| `id` | string | 是 | — | 复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '&lt;GUEST&gt;-&lt;JOBNUM&gt;'。 |
| `rate` | number | 否 | — | 速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。 |
| `remove_job` | string | 否 | — | 将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。；可选值：`local`, `full` |
| `schedule` | string | 否 | "*/15" | 存储复制计划。其格式是 `systemd` 日历事件的一个子集。 |
| `source` | string | 否 | — | 供内部使用，用于检测客户机是否被接管。 |
| `target` | string | 是 | — | 目标节点。 |
| `type` | string | 是 | — | 节类型。；可选值：`local` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "描述。",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "用于禁用/停用条目的标志。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。",
      "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
      "type": "string"
    },
    "rate": {
      "description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。",
      "minimum": 1,
      "optional": 1,
      "type": "number",
      "typetext": "<number> (1 - N)"
    },
    "remove_job": {
      "description": "将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。",
      "enum": [
        "local",
        "full"
      ],
      "optional": 1,
      "type": "string"
    },
    "schedule": {
      "default": "*/15",
      "description": "存储复制计划。其格式是 `systemd` 日历事件的一个子集。",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "source": {
      "description": "供内部使用，用于检测客户机是否被接管。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "target": {
      "description": "目标节点。",
      "format": "pve-node",
      "optional": 0,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "节类型。",
      "enum": [
        "local"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/replication)。
