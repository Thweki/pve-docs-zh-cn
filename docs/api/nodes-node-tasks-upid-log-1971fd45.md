# `/nodes/{node}/tasks/{upid}/log`

原始接口路径：`/nodes/{node}/tasks/{upid}/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/tasks/{upid}/log`

读取任务日志。

**方法标识：** `read_task_log`

**权限**

```json
{
  "description": "如果用户不是任务所有者，则需要对 '/nodes/<node>' 具有 'Sys.Audit' 权限。",
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
| `download` | boolean | 否 | — | 是否下载任务日志文件。此参数不能与其他参数一起使用 |
| `limit` | integer | 否 | 50 | 从任务日志读取的行数。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `start` | integer | 否 | 0 | 读取任务日志时从此行开始 |
| `upid` | string | 是 | — | 任务的唯一 ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "download": {
      "description": "是否下载任务日志文件。此参数不能与其他参数一起使用",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "limit": {
      "default": 50,
      "description": "从任务日志读取的行数。",
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
    "start": {
      "default": 0,
      "description": "读取任务日志时从此行开始",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "upid": {
      "description": "任务的唯一 ID。",
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
        "description": "行号",
        "type": "integer"
      },
      "t": {
        "description": "行文本",
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
