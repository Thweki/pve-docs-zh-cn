# `/nodes/{node}/tasks/{upid}/log`

原始接口路径：`/nodes/{node}/tasks/{upid}/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/tasks/{upid}/log`

Read task log.

**方法标识：** `read_task_log`

**权限**

```json
{
  "description": "The user needs 'Sys.Audit' permissions on '/nodes/<node>' if they aren't the owner of the task.",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `download` | boolean | 否 | — | Whether the tasklog file should be downloaded. This parameter can't be used in conjunction with other parameters |
| `limit` | integer | 否 | 50 | The number of lines to read from the tasklog. |
| `node` | string | 是 | — | The cluster node name. |
| `start` | integer | 否 | 0 | Start at this line when reading the tasklog |
| `upid` | string | 是 | — | The task's unique ID. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "download": {
      "description": "Whether the tasklog file should be downloaded. This parameter can't be used in conjunction with other parameters",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "limit": {
      "default": 50,
      "description": "The number of lines to read from the tasklog.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "start": {
      "default": 0,
      "description": "Start at this line when reading the tasklog",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "upid": {
      "description": "The task's unique ID.",
      "type": "string",
      "typetext": "<string>"
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
      "n": {
        "description": "Line number",
        "type": "integer"
      },
      "t": {
        "description": "Line text",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

<details>
<summary>其他接口元数据</summary>

```json
{
  "download_allowed": 1
}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/tasks/{upid}/log)。
