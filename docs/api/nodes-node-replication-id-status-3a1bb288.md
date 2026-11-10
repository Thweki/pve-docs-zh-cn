# `/nodes/{node}/replication/{id}/status`

原始接口路径：`/nodes/{node}/replication/{id}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/replication/{id}/status`

获取复制作业状态。

**方法标识：** `job_status`

**权限**

```json
{
  "description": "需要在 /vms/<vmid> 上拥有 VM.Audit 权限。",
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
| `node` | string | 是 | — | 集群节点名称。 |

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
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
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
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/replication/{id}/status)。
