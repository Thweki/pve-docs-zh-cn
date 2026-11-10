# `/nodes/{node}/replication/{id}/log`

原始接口路径：`/nodes/{node}/replication/{id}/log`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/replication/{id}/log`

读取复制作业日志。

**方法标识：** `read_job_log`

**权限**

```json
{
  "description": "需要对 /vms/<vmid> 具有 VM.Audit 权限，或对 '/nodes/<node>' 具有 'Sys.Audit' 权限",
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
| `id` | string | 是 | — | 复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '&lt;GUEST&gt;-&lt;JOBNUM&gt;'。 |
| `limit` | integer | 否 | — |  |
| `node` | string | 是 | — | 集群节点名称。 |
| `start` | integer | 否 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。",
      "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
      "type": "string"
    },
    "limit": {
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
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/replication/{id}/log)。
