# `/nodes/{node}/tasks`

原始接口路径：`/nodes/{node}/tasks`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/tasks`

读取某个节点的任务列表（已完成任务）。

**方法标识：** `node_tasks`

**权限**

```json
{
  "description": "列出与当前用户关联的任务，或用户对 /nodes/<node>（任务运行所在的 <node>）具有 'Sys.Audit' 权限的所有任务。",
  "user": "all"
}
```

**允许 API 令牌**

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
| `errors` | boolean | 否 | 0 | 仅列出状态为 ERROR 的任务。 |
| `limit` | integer | 否 | 50 | 仅列出此数量的任务。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `since` | integer | 否 | — | 仅列出此 UNIX 时间戳之后的任务。 |
| `source` | string | 否 | "archive" | 列出已归档、活动或所有任务。；可选值：`archive`, `active`, `all` |
| `start` | integer | 否 | 0 | 从此偏移量开始列出任务。 |
| `statusfilter` | string | 否 | — | 应返回的任务状态列表。 |
| `typefilter` | string | 否 | — | 仅列出此类型的任务（例如 vzstart、vzdump）。 |
| `until` | integer | 否 | — | 仅列出截至此 UNIX 时间戳的任务。 |
| `userfilter` | string | 否 | — | 仅列出此用户的任务。 |
| `vmid` | integer | 否 | — | 仅列出此虚拟机的任务。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "errors": {
      "default": 0,
      "description": "仅列出状态为 ERROR 的任务。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "limit": {
      "default": 50,
      "description": "仅列出此数量的任务。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "since": {
      "description": "仅列出此 UNIX 时间戳之后的任务。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "source": {
      "default": "archive",
      "description": "列出已归档、活动或所有任务。",
      "enum": [
        "archive",
        "active",
        "all"
      ],
      "optional": 1,
      "type": "string"
    },
    "start": {
      "default": 0,
      "description": "从此偏移量开始列出任务。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "statusfilter": {
      "description": "应返回的任务状态列表。",
      "format": "pve-task-status-type-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "typefilter": {
      "description": "仅列出此类型的任务（例如 vzstart、vzdump）。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "until": {
      "description": "仅列出截至此 UNIX 时间戳的任务。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "userfilter": {
      "description": "仅列出此用户的任务。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "仅列出此虚拟机的任务。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
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
    "properties": {
      "endtime": {
        "optional": 1,
        "renderer": "timestamp",
        "title": "结束时间",
        "type": "integer"
      },
      "id": {
        "title": "ID",
        "type": "string"
      },
      "node": {
        "title": "节点",
        "type": "string"
      },
      "pid": {
        "title": "PID",
        "type": "integer"
      },
      "pstart": {
        "type": "integer"
      },
      "starttime": {
        "renderer": "timestamp",
        "title": "开始时间",
        "type": "integer"
      },
      "status": {
        "optional": 1,
        "title": "状态",
        "type": "string"
      },
      "type": {
        "title": "类型",
        "type": "string"
      },
      "upid": {
        "title": "UPID",
        "type": "string"
      },
      "user": {
        "title": "用户",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{upid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/tasks)。
