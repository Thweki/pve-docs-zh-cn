# `/nodes/{node}/tasks/{upid}/status`

原始接口路径：`/nodes/{node}/tasks/{upid}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/tasks/{upid}/status`

Read task status.

**方法标识：** `read_task_status`

**权限**

```json
{
  "description": "The user needs 'Sys.Audit' permissions on '/nodes/<node>' if they are not the owner of the task.",
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
| `node` | string | 是 | — | The cluster node name. |
| `upid` | string | 是 | — | The task's unique ID. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
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
  "properties": {
    "exitstatus": {
      "optional": 1,
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "node": {
      "type": "string"
    },
    "pid": {
      "type": "integer"
    },
    "pstart": {
      "type": "integer"
    },
    "starttime": {
      "type": "integer"
    },
    "status": {
      "enum": [
        "running",
        "stopped"
      ],
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "upid": {
      "type": "string"
    },
    "user": {
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/tasks/{upid}/status)。
