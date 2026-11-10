# cluster API

本章包含此资源组的全部接口，按路径和 HTTP 方法在同一页展开。接口路径、方法、参数、类型、约束和默认值保持原值。

## `/cluster` <a href="#api-cluster-76d574b0" id="api-cluster-76d574b0"></a>

原始接口路径：`/cluster`。

### GET `/cluster` <a href="#api-cluster-76d574b0-get" id="api-cluster-76d574b0-get"></a>

集群索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-76d574b0-get-parameters" id="api-cluster-76d574b0-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-76d574b0-get-returns" id="api-cluster-76d574b0-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster)。

## `/cluster/replication` <a href="#api-cluster-replication-92d583d9" id="api-cluster-replication-92d583d9"></a>

原始接口路径：`/cluster/replication`。

### GET `/cluster/replication` <a href="#api-cluster-replication-92d583d9-get" id="api-cluster-replication-92d583d9-get"></a>

列出复制任务。

**方法标识：** `index`

**权限**

```text
{"description": "仅返回调用用户在 /vms/<vmid> 上拥有 VM.Audit 权限的复制任务。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-replication-92d583d9-get-parameters" id="api-cluster-replication-92d583d9-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-replication-92d583d9-get-returns" id="api-cluster-replication-92d583d9-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string"},
      "disable": {"description": "用于禁用/停用条目的标志。", "optional": 1, "type": "boolean"}, "guest": {"description": "客户机 ID。", "type": "integer"},
      "id": {
        "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。", "format": "pve-replication-job-id",
        "pattern": "[1-9][0-9]{2,8}-\\d{1,9}", "type": "string"
      },
      "jobnum": {"description": "分配给每个任务的唯一连续 ID。", "type": "integer"},
      "rate": {"description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。", "minimum": 1, "optional": 1, "type": "number"},
      "remove_job": {
        "description": "将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。",
        "enum": ["local", "full"], "optional": 1, "type": "string"
      },
      "schedule": {
        "default": "*/15", "description": "存储复制计划。其格式是 `systemd` 日历事件的一个子集。", "format": "pve-calendar-event", "maxLength": 128,
        "optional": 1, "type": "string"
      },
      "source": {"description": "供内部使用，用于检测客户机是否被接管。", "format": "pve-node", "optional": 1, "type": "string"},
      "target": {"description": "目标节点。", "format": "pve-node", "optional": 0, "type": "string"},
      "type": {"description": "节类型。", "enum": ["local"], "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/replication` <a href="#api-cluster-replication-92d583d9-post" id="api-cluster-replication-92d583d9-post"></a>

创建新的复制任务

**方法标识：** `create`

**权限**

```text
{"description": "需要在 /vms/<vmid> 上拥有 VM.Replicate 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-replication-92d583d9-post-parameters" id="api-cluster-replication-92d583d9-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用/停用条目的标志。 |
| `id` | 类型：string；必填：是；默认值：—<br>复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '&lt;GUEST&gt;-&lt;JOBNUM&gt;'。 |
| `rate` | 类型：number；必填：否；默认值：—<br>速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。 |
| `remove_job` | 类型：string；必填：否；默认值：—<br>将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。；可选值：`local`, `full` |
| `schedule` | 类型：string；必填：否；默认值："*/15"<br>存储复制计划。其格式是 `systemd` 日历事件的一个子集。 |
| `source` | 类型：string；必填：否；默认值：—<br>供内部使用，用于检测客户机是否被接管。 |
| `target` | 类型：string；必填：是；默认值：—<br>目标节点。 |
| `type` | 类型：string；必填：是；默认值：—<br>节类型。；可选值：`local` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"description": "用于禁用/停用条目的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。", "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}", "type": "string"
    },
    "rate": {
      "description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。", "minimum": 1, "optional": 1, "type": "number", "typetext": "<number> (1 - N)"
    },
    "remove_job": {
      "description": "将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。",
      "enum": ["local", "full"], "optional": 1, "type": "string"
    },
    "schedule": {
      "default": "*/15", "description": "存储复制计划。其格式是 `systemd` 日历事件的一个子集。", "format": "pve-calendar-event", "maxLength": 128,
      "optional": 1, "type": "string", "typetext": "<string>"
    },
    "source": {"description": "供内部使用，用于检测客户机是否被接管。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "target": {"description": "目标节点。", "format": "pve-node", "optional": 0, "type": "string", "typetext": "<string>"},
    "type": {"description": "节类型。", "enum": ["local"], "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-replication-92d583d9-post-returns" id="api-cluster-replication-92d583d9-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/replication)。

## `/cluster/replication/{id}` <a href="#api-cluster-replication-id-46e95f47" id="api-cluster-replication-id-46e95f47"></a>

原始接口路径：`/cluster/replication/{id}`。

### DELETE `/cluster/replication/{id}` <a href="#api-cluster-replication-id-46e95f47-delete" id="api-cluster-replication-id-46e95f47-delete"></a>

将复制任务标记为待移除。

**方法标识：** `delete`

**权限**

```text
{"description": "需要在 /vms/<vmid> 上拥有 VM.Replicate 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-replication-id-46e95f47-delete-parameters" id="api-cluster-replication-id-46e95f47-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `force` | 类型：boolean；必填：否；默认值：0<br>将移除 jobconfig 条目，但不执行清理。 |
| `id` | 类型：string；必填：是；默认值：—<br>复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '&lt;GUEST&gt;-&lt;JOBNUM&gt;'。 |
| `keep` | 类型：boolean；必填：否；默认值：0<br>保留目标上的复制数据（不移除）。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "force": {"default": 0, "description": "将移除 jobconfig 条目，但不执行清理。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。", "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}", "type": "string"
    },
    "keep": {"default": 0, "description": "保留目标上的复制数据（不移除）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-replication-id-46e95f47-delete-returns" id="api-cluster-replication-id-46e95f47-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/replication/{id}` <a href="#api-cluster-replication-id-46e95f47-get" id="api-cluster-replication-id-46e95f47-get"></a>

读取复制任务配置。

**方法标识：** `read`

**权限**

```text
{"description": "需要在 /vms/<vmid> 上拥有 VM.Audit 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-replication-id-46e95f47-get-parameters" id="api-cluster-replication-id-46e95f47-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '&lt;GUEST&gt;-&lt;JOBNUM&gt;'。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。", "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}", "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-replication-id-46e95f47-get-returns" id="api-cluster-replication-id-46e95f47-get-returns"></a>

```text
{
  "properties": {
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"description": "用于禁用/停用条目的标志。", "optional": 1, "type": "boolean"}, "guest": {"description": "客户机 ID。", "type": "integer"},
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。", "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}", "type": "string"
    },
    "jobnum": {"description": "分配给每个任务的唯一连续 ID。", "type": "integer"},
    "rate": {"description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。", "minimum": 1, "optional": 1, "type": "number"},
    "remove_job": {
      "description": "将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。",
      "enum": ["local", "full"], "optional": 1, "type": "string"
    },
    "schedule": {
      "default": "*/15", "description": "存储复制计划。其格式是 `systemd` 日历事件的一个子集。", "format": "pve-calendar-event", "maxLength": 128,
      "optional": 1, "type": "string"
    },
    "source": {"description": "供内部使用，用于检测客户机是否被接管。", "format": "pve-node", "optional": 1, "type": "string"},
    "target": {"description": "目标节点。", "format": "pve-node", "optional": 0, "type": "string"},
    "type": {"description": "节类型。", "enum": ["local"], "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/replication/{id}` <a href="#api-cluster-replication-id-46e95f47-put" id="api-cluster-replication-id-46e95f47-put"></a>

更新复制任务配置。

**方法标识：** `update`

**权限**

```text
{"description": "需要在 /vms/<vmid> 上拥有 VM.Replicate 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-replication-id-46e95f47-put-parameters" id="api-cluster-replication-id-46e95f47-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用/停用条目的标志。 |
| `id` | 类型：string；必填：是；默认值：—<br>复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '&lt;GUEST&gt;-&lt;JOBNUM&gt;'。 |
| `rate` | 类型：number；必填：否；默认值：—<br>速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。 |
| `remove_job` | 类型：string；必填：否；默认值：—<br>将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。；可选值：`local`, `full` |
| `schedule` | 类型：string；必填：否；默认值："*/15"<br>存储复制计划。其格式是 `systemd` 日历事件的一个子集。 |
| `source` | 类型：string；必填：否；默认值：—<br>供内部使用，用于检测客户机是否被接管。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"description": "用于禁用/停用条目的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {
      "description": "复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 '<GUEST>-<JOBNUM>'。", "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}", "type": "string"
    },
    "rate": {
      "description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。", "minimum": 1, "optional": 1, "type": "number", "typetext": "<number> (1 - N)"
    },
    "remove_job": {
      "description": "将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 'full'，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。",
      "enum": ["local", "full"], "optional": 1, "type": "string"
    },
    "schedule": {
      "default": "*/15", "description": "存储复制计划。其格式是 `systemd` 日历事件的一个子集。", "format": "pve-calendar-event", "maxLength": 128,
      "optional": 1, "type": "string", "typetext": "<string>"
    },
    "source": {"description": "供内部使用，用于检测客户机是否被接管。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-replication-id-46e95f47-put-returns" id="api-cluster-replication-id-46e95f47-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/replication/{id})。

## `/cluster/metrics` <a href="#api-cluster-metrics-c2310197" id="api-cluster-metrics-c2310197"></a>

原始接口路径：`/cluster/metrics`。

### GET `/cluster/metrics` <a href="#api-cluster-metrics-c2310197-get" id="api-cluster-metrics-c2310197-get"></a>

指标索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-metrics-c2310197-get-parameters" id="api-cluster-metrics-c2310197-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-metrics-c2310197-get-returns" id="api-cluster-metrics-c2310197-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics)。

## `/cluster/metrics/server` <a href="#api-cluster-metrics-server-cdd8f7b0" id="api-cluster-metrics-server-cdd8f7b0"></a>

原始接口路径：`/cluster/metrics/server`。

### GET `/cluster/metrics/server` <a href="#api-cluster-metrics-server-cdd8f7b0-get" id="api-cluster-metrics-server-cdd8f7b0-get"></a>

列出已配置的指标服务器。

**方法标识：** `server_index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-metrics-server-cdd8f7b0-get-parameters" id="api-cluster-metrics-server-cdd8f7b0-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-metrics-server-cdd8f7b0-get-returns" id="api-cluster-metrics-server-cdd8f7b0-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "disable": {"description": "用于禁用插件的标志。", "type": "boolean"}, "id": {"description": "条目的 ID。", "type": "string"},
      "port": {"description": "服务器网络端口", "type": "integer"}, "server": {"description": "服务器 DNS 名称或 IP 地址", "type": "string"},
      "type": {"description": "插件类型。", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics/server)。

## `/cluster/metrics/server/{id}` <a href="#api-cluster-metrics-server-id-368f49a1" id="api-cluster-metrics-server-id-368f49a1"></a>

原始接口路径：`/cluster/metrics/server/{id}`。

### DELETE `/cluster/metrics/server/{id}` <a href="#api-cluster-metrics-server-id-368f49a1-delete" id="api-cluster-metrics-server-id-368f49a1-delete"></a>

移除指标服务器。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-metrics-server-id-368f49a1-delete-parameters" id="api-cluster-metrics-server-id-368f49a1-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-metrics-server-id-368f49a1-delete-returns" id="api-cluster-metrics-server-id-368f49a1-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/metrics/server/{id}` <a href="#api-cluster-metrics-server-id-368f49a1-get" id="api-cluster-metrics-server-id-368f49a1-get"></a>

读取指标服务器配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-metrics-server-id-368f49a1-get-parameters" id="api-cluster-metrics-server-id-368f49a1-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-metrics-server-id-368f49a1-get-returns" id="api-cluster-metrics-server-id-368f49a1-get-returns"></a>

```text
{"type": "object"}
```

### POST `/cluster/metrics/server/{id}` <a href="#api-cluster-metrics-server-id-368f49a1-post" id="api-cluster-metrics-server-id-368f49a1-post"></a>

创建新的外部指标服务器配置

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-metrics-server-id-368f49a1-post-parameters" id="api-cluster-metrics-server-id-368f49a1-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `api-path-prefix` | 类型：string；必填：否；默认值：—<br>插入在 '&lt;host&gt;:&lt;port&gt;/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。 |
| `bucket` | 类型：string；必填：否；默认值：—<br>InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用插件的标志。 |
| `id` | 类型：string；必填：是；默认值：—<br>条目的 ID。 |
| `influxdbproto` | 类型：string；必填：否；默认值："udp"<br>；可选值：`udp`, `http`, `https` |
| `max-body-size` | 类型：integer；必填：否；默认值：25000000<br>InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。 |
| `mtu` | 类型：integer；必填：否；默认值：1500<br>通过 UDP 传输指标的 MTU |
| `organization` | 类型：string；必填：否；默认值：—<br>InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。 |
| `otel-compression` | 类型：string；必填：否；默认值："gzip"<br>请求的压缩算法；可选值：`none`, `gzip` |
| `otel-headers` | 类型：string；必填：否；默认值：—<br>自定义 HTTP 标头（JSON 格式，base64 编码） |
| `otel-max-body-size` | 类型：integer；必填：否；默认值：10000000<br>最大请求正文大小，单位为字节 |
| `otel-path` | 类型：string；必填：否；默认值："/v1/metrics"<br>OTLP 端点路径 |
| `otel-protocol` | 类型：string；必填：否；默认值："https"<br>HTTP 协议；可选值：`http`, `https` |
| `otel-resource-attributes` | 类型：string；必填：否；默认值：—<br>JSON 形式的额外资源属性，采用 base64 编码 |
| `otel-timeout` | 类型：integer；必填：否；默认值：5<br>HTTP 请求超时时间，单位为秒 |
| `otel-verify-ssl` | 类型：boolean；必填：否；默认值：1<br>验证 SSL 证书 |
| `path` | 类型：string；必填：否；默认值：—<br>graphite 根路径（例如：proxmox.mycluster.mykey） |
| `port` | 类型：integer；必填：是；默认值：—<br>服务器网络端口 |
| `proto` | 类型：string；必填：否；默认值：—<br>发送 graphite 数据的协议。TCP 或 UDP（默认）；可选值：`udp`, `tcp` |
| `server` | 类型：string；必填：是；默认值：—<br>服务器 DNS 名称或 IP 地址 |
| `timeout` | 类型：integer；必填：否；默认值：1<br>graphite TCP 套接字超时时间（默认值=1） |
| `token` | 类型：string；必填：否；默认值：—<br>InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。 |
| `type` | 类型：string；必填：是；默认值：—<br>插件类型。；可选值：`graphite`, `influxdb`, `opentelemetry` |
| `verify-certificate` | 类型：boolean；必填：否；默认值：1<br>设置为 0 可禁用 https 端点的证书验证。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "api-path-prefix": {
      "description": "插入在 '<host>:<port>/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "bucket": {"description": "InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"description": "用于禁用插件的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "条目的 ID。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "influxdbproto": {"default": "udp", "enum": ["udp", "http", "https"], "optional": 1, "type": "string"},
    "max-body-size": {
      "default": 25000000, "description": "InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。", "minimum": 1, "optional": 1,
      "type": "integer", "typetext": "<integer> (1 - N)"
    },
    "mtu": {
      "default": 1500, "description": "通过 UDP 传输指标的 MTU", "maximum": 65536, "minimum": 512, "optional": 1, "type": "integer",
      "typetext": "<integer> (512 - 65536)"
    },
    "organization": {
      "description": "InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "otel-compression": {"default": "gzip", "description": "请求的压缩算法", "enum": ["none", "gzip"], "optional": 1, "type": "string"},
    "otel-headers": {"description": "自定义 HTTP 标头（JSON 格式，base64 编码）", "maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"},
    "otel-max-body-size": {
      "default": 10000000, "description": "最大请求正文大小，单位为字节", "minimum": 1024, "optional": 1, "type": "integer", "typetext": "<integer> (1024 - N)"
    },
    "otel-path": {"default": "/v1/metrics", "description": "OTLP 端点路径", "optional": 1, "type": "string", "typetext": "<string>"},
    "otel-protocol": {"default": "https", "description": "HTTP 协议", "enum": ["http", "https"], "optional": 1, "type": "string"},
    "otel-resource-attributes": {
      "description": "JSON 形式的额外资源属性，采用 base64 编码", "maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "otel-timeout": {
      "default": 5, "description": "HTTP 请求超时时间，单位为秒", "maximum": 10, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 10)"
    },
    "otel-verify-ssl": {"default": 1, "description": "验证 SSL 证书", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "path": {
      "description": "graphite 根路径（例如：proxmox.mycluster.mykey）", "format": "graphite-path", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "port": {"description": "服务器网络端口", "maximum": 65536, "minimum": 1, "type": "integer", "typetext": "<integer> (1 - 65536)"},
    "proto": {"description": "发送 graphite 数据的协议。TCP 或 UDP（默认）", "enum": ["udp", "tcp"], "optional": 1, "type": "string"},
    "server": {"description": "服务器 DNS 名称或 IP 地址", "format": "address", "type": "string", "typetext": "<string>"},
    "timeout": {
      "default": 1, "description": "graphite TCP 套接字超时时间（默认值=1）", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "token": {
      "description": "InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。", "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "type": {"description": "插件类型。", "enum": ["graphite", "influxdb", "opentelemetry"], "format": "pve-configid", "type": "string"},
    "verify-certificate": {"default": 1, "description": "设置为 0 可禁用 https 端点的证书验证。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-metrics-server-id-368f49a1-post-returns" id="api-cluster-metrics-server-id-368f49a1-post-returns"></a>

```text
{"type": "null"}
```

### PUT `/cluster/metrics/server/{id}` <a href="#api-cluster-metrics-server-id-368f49a1-put" id="api-cluster-metrics-server-id-368f49a1-put"></a>

更新指标服务器配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-metrics-server-id-368f49a1-put-parameters" id="api-cluster-metrics-server-id-368f49a1-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `api-path-prefix` | 类型：string；必填：否；默认值：—<br>插入在 '&lt;host&gt;:&lt;port&gt;/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。 |
| `bucket` | 类型：string；必填：否；默认值：—<br>InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用插件的标志。 |
| `id` | 类型：string；必填：是；默认值：—<br>条目的 ID。 |
| `influxdbproto` | 类型：string；必填：否；默认值："udp"<br>；可选值：`udp`, `http`, `https` |
| `max-body-size` | 类型：integer；必填：否；默认值：25000000<br>InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。 |
| `mtu` | 类型：integer；必填：否；默认值：1500<br>通过 UDP 传输指标的 MTU |
| `organization` | 类型：string；必填：否；默认值：—<br>InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。 |
| `otel-compression` | 类型：string；必填：否；默认值："gzip"<br>请求的压缩算法；可选值：`none`, `gzip` |
| `otel-headers` | 类型：string；必填：否；默认值：—<br>自定义 HTTP 标头（JSON 格式，base64 编码） |
| `otel-max-body-size` | 类型：integer；必填：否；默认值：10000000<br>最大请求正文大小，单位为字节 |
| `otel-path` | 类型：string；必填：否；默认值："/v1/metrics"<br>OTLP 端点路径 |
| `otel-protocol` | 类型：string；必填：否；默认值："https"<br>HTTP 协议；可选值：`http`, `https` |
| `otel-resource-attributes` | 类型：string；必填：否；默认值：—<br>JSON 形式的额外资源属性，采用 base64 编码 |
| `otel-timeout` | 类型：integer；必填：否；默认值：5<br>HTTP 请求超时时间，单位为秒 |
| `otel-verify-ssl` | 类型：boolean；必填：否；默认值：1<br>验证 SSL 证书 |
| `path` | 类型：string；必填：否；默认值：—<br>graphite 根路径（例如：proxmox.mycluster.mykey） |
| `port` | 类型：integer；必填：是；默认值：—<br>服务器网络端口 |
| `proto` | 类型：string；必填：否；默认值：—<br>发送 graphite 数据的协议。TCP 或 UDP（默认）；可选值：`udp`, `tcp` |
| `server` | 类型：string；必填：是；默认值：—<br>服务器 DNS 名称或 IP 地址 |
| `timeout` | 类型：integer；必填：否；默认值：1<br>graphite TCP 套接字超时时间（默认值=1） |
| `token` | 类型：string；必填：否；默认值：—<br>InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。 |
| `verify-certificate` | 类型：boolean；必填：否；默认值：1<br>设置为 0 可禁用 https 端点的证书验证。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "api-path-prefix": {
      "description": "插入在 '<host>:<port>/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "bucket": {"description": "InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"description": "用于禁用插件的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "条目的 ID。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "influxdbproto": {"default": "udp", "enum": ["udp", "http", "https"], "optional": 1, "type": "string"},
    "max-body-size": {
      "default": 25000000, "description": "InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。", "minimum": 1, "optional": 1,
      "type": "integer", "typetext": "<integer> (1 - N)"
    },
    "mtu": {
      "default": 1500, "description": "通过 UDP 传输指标的 MTU", "maximum": 65536, "minimum": 512, "optional": 1, "type": "integer",
      "typetext": "<integer> (512 - 65536)"
    },
    "organization": {
      "description": "InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "otel-compression": {"default": "gzip", "description": "请求的压缩算法", "enum": ["none", "gzip"], "optional": 1, "type": "string"},
    "otel-headers": {"description": "自定义 HTTP 标头（JSON 格式，base64 编码）", "maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"},
    "otel-max-body-size": {
      "default": 10000000, "description": "最大请求正文大小，单位为字节", "minimum": 1024, "optional": 1, "type": "integer", "typetext": "<integer> (1024 - N)"
    },
    "otel-path": {"default": "/v1/metrics", "description": "OTLP 端点路径", "optional": 1, "type": "string", "typetext": "<string>"},
    "otel-protocol": {"default": "https", "description": "HTTP 协议", "enum": ["http", "https"], "optional": 1, "type": "string"},
    "otel-resource-attributes": {
      "description": "JSON 形式的额外资源属性，采用 base64 编码", "maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "otel-timeout": {
      "default": 5, "description": "HTTP 请求超时时间，单位为秒", "maximum": 10, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 10)"
    },
    "otel-verify-ssl": {"default": 1, "description": "验证 SSL 证书", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "path": {
      "description": "graphite 根路径（例如：proxmox.mycluster.mykey）", "format": "graphite-path", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "port": {"description": "服务器网络端口", "maximum": 65536, "minimum": 1, "type": "integer", "typetext": "<integer> (1 - 65536)"},
    "proto": {"description": "发送 graphite 数据的协议。TCP 或 UDP（默认）", "enum": ["udp", "tcp"], "optional": 1, "type": "string"},
    "server": {"description": "服务器 DNS 名称或 IP 地址", "format": "address", "type": "string", "typetext": "<string>"},
    "timeout": {
      "default": 1, "description": "graphite TCP 套接字超时时间（默认值=1）", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "token": {
      "description": "InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。", "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "verify-certificate": {"default": 1, "description": "设置为 0 可禁用 https 端点的证书验证。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-metrics-server-id-368f49a1-put-returns" id="api-cluster-metrics-server-id-368f49a1-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics/server/{id})。

## `/cluster/metrics/export` <a href="#api-cluster-metrics-export-8d34a581" id="api-cluster-metrics-export-8d34a581"></a>

原始接口路径：`/cluster/metrics/export`。

### GET `/cluster/metrics/export` <a href="#api-cluster-metrics-export-8d34a581-get" id="api-cluster-metrics-export-8d34a581-get"></a>

获取集群指标。

**方法标识：** `export`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-metrics-export-8d34a581-get-parameters" id="api-cluster-metrics-export-8d34a581-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `history` | 类型：boolean；必填：否；默认值：0<br>还返回历史值。除非同时设置 `start-time`，否则返回所有可用的指标历史记录 |
| `local-only` | 类型：boolean；必填：否；默认值：0<br>仅返回当前节点的指标，而不是整个集群的指标 |
| `node-list` | 类型：string；必填：否；默认值：—<br>仅返回以逗号分隔列表传入的节点的指标 |
| `start-time` | 类型：integer；必填：否；默认值：0<br>仅包含时间戳 &gt; start-time 的指标。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "history": {
      "default": 0, "description": "还返回历史值。除非同时设置 `start-time`，否则返回所有可用的指标历史记录", "optional": 1, "type": "boolean",
      "typetext": "<boolean>"
    },
    "local-only": {"default": 0, "description": "仅返回当前节点的指标，而不是整个集群的指标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "node-list": {"description": "仅返回以逗号分隔列表传入的节点的指标", "optional": 1, "type": "string", "typetext": "<string>"},
    "start-time": {"default": 0, "description": "仅包含时间戳 > start-time 的指标。", "optional": 1, "type": "integer", "typetext": "<integer>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-metrics-export-8d34a581-get-returns" id="api-cluster-metrics-export-8d34a581-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "data": {
      "description": "系统指标数组。指标按时间戳排序。",
      "items": {
        "additionalProperties": 0,
        "properties": {
          "id": {"description": "此指标对象的唯一标识符，例如 'node/<nodename>' 或 'qemu/<vmid>'。", "type": "string"},
          "metric": {"description": "指标名称。", "type": "string"}, "timestamp": {"description": "观测到此指标的时间", "type": "integer"},
          "type": {"description": "指标类型。", "enum": ["gauge", "counter", "derive"], "type": "string"},
          "value": {"description": "指标值。", "type": "number"}
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

```text
{"expose_credentials": 1}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics/export)。

## `/cluster/notifications` <a href="#api-cluster-notifications-4311ac17" id="api-cluster-notifications-4311ac17"></a>

原始接口路径：`/cluster/notifications`。

### GET `/cluster/notifications` <a href="#api-cluster-notifications-4311ac17-get" id="api-cluster-notifications-4311ac17-get"></a>

通知相关 API 端点的索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-notifications-4311ac17-get-parameters" id="api-cluster-notifications-4311ac17-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-4311ac17-get-returns" id="api-cluster-notifications-4311ac17-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications)。

## `/cluster/notifications/matcher-fields` <a href="#api-cluster-notifications-matcher-fields-265de9d8" id="api-cluster-notifications-matcher-fields-265de9d8"></a>

原始接口路径：`/cluster/notifications/matcher-fields`。

### GET `/cluster/notifications/matcher-fields` <a href="#api-cluster-notifications-matcher-fields-265de9d8-get" id="api-cluster-notifications-matcher-fields-265de9d8-get"></a>

返回已知的通知元数据字段

**方法标识：** `get_matcher_fields`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `0`

#### 请求参数 <a href="#api-cluster-notifications-matcher-fields-265de9d8-get-parameters" id="api-cluster-notifications-matcher-fields-265de9d8-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-matcher-fields-265de9d8-get-returns" id="api-cluster-notifications-matcher-fields-265de9d8-get-returns"></a>

```text
{
  "items": {"properties": {"name": {"description": "字段名称。", "type": "string"}}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matcher-fields)。

## `/cluster/notifications/matcher-field-values` <a href="#api-cluster-notifications-matcher-field-values-62224854" id="api-cluster-notifications-matcher-field-values-62224854"></a>

原始接口路径：`/cluster/notifications/matcher-field-values`。

### GET `/cluster/notifications/matcher-field-values` <a href="#api-cluster-notifications-matcher-field-values-62224854-get" id="api-cluster-notifications-matcher-field-values-62224854-get"></a>

返回已知的通知元数据字段及其已知值

**方法标识：** `get_matcher_field_values`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-matcher-field-values-62224854-get-parameters" id="api-cluster-notifications-matcher-field-values-62224854-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-matcher-field-values-62224854-get-returns" id="api-cluster-notifications-matcher-field-values-62224854-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "此值的额外注释。", "optional": 1, "type": "string"}, "field": {"description": "此值所属的字段。", "type": "string"},
      "value": {"description": "系统已知的通知元数据值。", "type": "string"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matcher-field-values)。

## `/cluster/notifications/endpoints` <a href="#api-cluster-notifications-endpoints-1e456d97" id="api-cluster-notifications-endpoints-1e456d97"></a>

原始接口路径：`/cluster/notifications/endpoints`。

### GET `/cluster/notifications/endpoints` <a href="#api-cluster-notifications-endpoints-1e456d97-get" id="api-cluster-notifications-endpoints-1e456d97-get"></a>

所有可用端点类型的索引。

**方法标识：** `endpoints_index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-1e456d97-get-parameters" id="api-cluster-notifications-endpoints-1e456d97-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-endpoints-1e456d97-get-returns" id="api-cluster-notifications-endpoints-1e456d97-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints)。

## `/cluster/notifications/endpoints/sendmail` <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85"></a>

原始接口路径：`/cluster/notifications/endpoints/sendmail`。

### GET `/cluster/notifications/endpoints/sendmail` <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85-get" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85-get"></a>

返回所有 sendmail 端点的列表

**方法标识：** `get_sendmail_endpoints`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85-get-parameters" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85-get-returns" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "author": {"description": "邮件作者", "optional": 1, "type": "string"}, "comment": {"description": "注释", "optional": 1, "type": "string"},
      "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
      "from-address": {"description": "邮件的 `From` 地址", "optional": 1, "type": "string"},
      "mailto": {"description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array"},
      "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array"},
      "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"},
      "origin": {"description": "显示此条目是用户创建还是内置", "enum": ["user-created", "builtin", "modified-builtin"], "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/notifications/endpoints/sendmail` <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85-post" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85-post"></a>

创建新的 sendmail 端点

**方法标识：** `create_sendmail_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85-post-parameters" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `author` | 类型：string；必填：否；默认值：—<br>邮件作者 |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `from-address` | 类型：string；必填：否；默认值：—<br>邮件的 `From` 地址 |
| `mailto` | 类型：array；必填：否；默认值：—<br>电子邮件收件人列表 |
| `mailto-user` | 类型：array；必填：否；默认值：—<br>用户列表 |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "author": {"description": "邮件作者", "optional": 1, "type": "string", "typetext": "<string>"},
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "from-address": {"description": "邮件的 `From` 地址", "optional": 1, "type": "string", "typetext": "<string>"},
    "mailto": {
      "description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-sendmail-bd1bbd85-post-returns" id="api-cluster-notifications-endpoints-sendmail-bd1bbd85-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/sendmail)。

## `/cluster/notifications/endpoints/sendmail/{name}` <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe"></a>

原始接口路径：`/cluster/notifications/endpoints/sendmail/{name}`。

### DELETE `/cluster/notifications/endpoints/sendmail/{name}` <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-delete" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-delete"></a>

移除 sendmail 端点

**方法标识：** `delete_sendmail_endpoint`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-delete-parameters" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-delete-returns" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/notifications/endpoints/sendmail/{name}` <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-get" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-get"></a>

返回指定的 sendmail 端点

**方法标识：** `get_sendmail_endpoint`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-get-parameters" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-get-returns" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-get-returns"></a>

```text
{
  "properties": {
    "author": {"description": "邮件作者", "optional": 1, "type": "string"}, "comment": {"description": "注释", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
    "from-address": {"description": "邮件的 `From` 地址", "optional": 1, "type": "string"},
    "mailto": {"description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array"},
    "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/notifications/endpoints/sendmail/{name}` <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-put" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-put"></a>

更新现有 sendmail 端点

**方法标识：** `update_sendmail_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-put-parameters" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `author` | 类型：string；必填：否；默认值：—<br>邮件作者 |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `delete` | 类型：array；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `from-address` | 类型：string；必填：否；默认值：—<br>邮件的 `From` 地址 |
| `mailto` | 类型：array；必填：否；默认值：—<br>电子邮件收件人列表 |
| `mailto-user` | 类型：array；必填：否；默认值：—<br>用户列表 |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "author": {"description": "邮件作者", "optional": 1, "type": "string", "typetext": "<string>"},
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {
      "description": "要删除的设置列表。", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "from-address": {"description": "邮件的 `From` 地址", "optional": 1, "type": "string", "typetext": "<string>"},
    "mailto": {
      "description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-put-returns" id="api-cluster-notifications-endpoints-sendmail-name-8baf2dfe-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/sendmail/{name})。

## `/cluster/notifications/endpoints/gotify` <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8" id="api-cluster-notifications-endpoints-gotify-3afd73f8"></a>

原始接口路径：`/cluster/notifications/endpoints/gotify`。

### GET `/cluster/notifications/endpoints/gotify` <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8-get" id="api-cluster-notifications-endpoints-gotify-3afd73f8-get"></a>

返回所有 gotify 端点的列表

**方法标识：** `get_gotify_endpoints`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8-get-parameters" id="api-cluster-notifications-endpoints-gotify-3afd73f8-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8-get-returns" id="api-cluster-notifications-endpoints-gotify-3afd73f8-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "注释", "optional": 1, "type": "string"},
      "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
      "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"},
      "origin": {"description": "显示此条目是用户创建还是内置", "enum": ["user-created", "builtin", "modified-builtin"], "type": "string"},
      "server": {"description": "服务器 URL", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/notifications/endpoints/gotify` <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8-post" id="api-cluster-notifications-endpoints-gotify-3afd73f8-post"></a>

创建新的 gotify 端点

**方法标识：** `create_gotify_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8-post-parameters" id="api-cluster-notifications-endpoints-gotify-3afd73f8-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |
| `server` | 类型：string；必填：是；默认值：—<br>服务器 URL |
| `token` | 类型：string；必填：是；默认值：—<br>秘密令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "server": {"description": "服务器 URL", "type": "string", "typetext": "<string>"},
    "token": {"description": "秘密令牌", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-gotify-3afd73f8-post-returns" id="api-cluster-notifications-endpoints-gotify-3afd73f8-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/gotify)。

## `/cluster/notifications/endpoints/gotify/{name}` <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef" id="api-cluster-notifications-endpoints-gotify-name-a017cfef"></a>

原始接口路径：`/cluster/notifications/endpoints/gotify/{name}`。

### DELETE `/cluster/notifications/endpoints/gotify/{name}` <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-delete" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-delete"></a>

移除 gotify 端点

**方法标识：** `delete_gotify_endpoint`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-delete-parameters" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-delete-returns" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/notifications/endpoints/gotify/{name}` <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-get" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-get"></a>

返回指定的 gotify 端点

**方法标识：** `get_gotify_endpoint`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-get-parameters" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-get-returns" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-get-returns"></a>

```text
{
  "properties": {
    "comment": {"description": "注释", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"}, "server": {"description": "服务器 URL", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/notifications/endpoints/gotify/{name}` <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-put" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-put"></a>

更新现有 gotify 端点

**方法标识：** `update_gotify_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-put-parameters" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `delete` | 类型：array；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |
| `server` | 类型：string；必填：否；默认值：—<br>服务器 URL |
| `token` | 类型：string；必填：否；默认值：—<br>秘密令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {
      "description": "要删除的设置列表。", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "server": {"description": "服务器 URL", "optional": 1, "type": "string", "typetext": "<string>"},
    "token": {"description": "秘密令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-gotify-name-a017cfef-put-returns" id="api-cluster-notifications-endpoints-gotify-name-a017cfef-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/gotify/{name})。

## `/cluster/notifications/endpoints/smtp` <a href="#api-cluster-notifications-endpoints-smtp-69d956eb" id="api-cluster-notifications-endpoints-smtp-69d956eb"></a>

原始接口路径：`/cluster/notifications/endpoints/smtp`。

### GET `/cluster/notifications/endpoints/smtp` <a href="#api-cluster-notifications-endpoints-smtp-69d956eb-get" id="api-cluster-notifications-endpoints-smtp-69d956eb-get"></a>

返回所有 smtp 端点的列表

**方法标识：** `get_smtp_endpoints`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-smtp-69d956eb-get-parameters" id="api-cluster-notifications-endpoints-smtp-69d956eb-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-endpoints-smtp-69d956eb-get-returns" id="api-cluster-notifications-endpoints-smtp-69d956eb-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "author": {"description": "邮件作者。默认为 'Proxmox VE'。", "optional": 1, "type": "string"},
      "comment": {"description": "注释", "optional": 1, "type": "string"},
      "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
      "from-address": {"description": "邮件的 `From` 地址", "type": "string"},
      "mailto": {"description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array"},
      "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array"},
      "mode": {"default": "tls", "description": "确定连接应使用哪种加密方法。", "enum": ["insecure", "starttls", "tls"], "optional": 1, "type": "string"},
      "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"},
      "origin": {"description": "显示此条目是用户创建还是内置", "enum": ["user-created", "builtin", "modified-builtin"], "type": "string"},
      "port": {
        "description": "使用的端口。基于 TLS 的连接默认为 465，基于 STARTTLS 的连接默认为 587，不安全的纯文本连接默认为端口 25。", "optional": 1,
        "type": "integer"
      },
      "server": {"description": "SMTP 服务器地址。", "type": "string"}, "username": {"description": "SMTP 认证的用户名", "optional": 1, "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/notifications/endpoints/smtp` <a href="#api-cluster-notifications-endpoints-smtp-69d956eb-post" id="api-cluster-notifications-endpoints-smtp-69d956eb-post"></a>

创建新的 smtp 端点

**方法标识：** `create_smtp_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-smtp-69d956eb-post-parameters" id="api-cluster-notifications-endpoints-smtp-69d956eb-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `author` | 类型：string；必填：否；默认值：—<br>邮件作者。默认为 'Proxmox VE'。 |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `from-address` | 类型：string；必填：是；默认值：—<br>邮件的 `From` 地址 |
| `mailto` | 类型：array；必填：否；默认值：—<br>电子邮件收件人列表 |
| `mailto-user` | 类型：array；必填：否；默认值：—<br>用户列表 |
| `mode` | 类型：string；必填：否；默认值："tls"<br>确定连接应使用哪种加密方法。；可选值：`insecure`, `starttls`, `tls` |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |
| `password` | 类型：string；必填：否；默认值：—<br>SMTP 认证的密码 |
| `port` | 类型：integer；必填：否；默认值：—<br>使用的端口。基于 TLS 的连接默认为 465，基于 STARTTLS 的连接默认为 587，不安全的纯文本连接默认为端口 25。 |
| `server` | 类型：string；必填：是；默认值：—<br>SMTP 服务器地址。 |
| `username` | 类型：string；必填：否；默认值：—<br>SMTP 认证的用户名 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "author": {"description": "邮件作者。默认为 'Proxmox VE'。", "optional": 1, "type": "string", "typetext": "<string>"},
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "from-address": {"description": "邮件的 `From` 地址", "type": "string", "typetext": "<string>"},
    "mailto": {
      "description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "mode": {"default": "tls", "description": "确定连接应使用哪种加密方法。", "enum": ["insecure", "starttls", "tls"], "optional": 1, "type": "string"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "password": {"description": "SMTP 认证的密码", "optional": 1, "type": "string", "typetext": "<string>"},
    "port": {
      "description": "使用的端口。基于 TLS 的连接默认为 465，基于 STARTTLS 的连接默认为 587，不安全的纯文本连接默认为端口 25。", "optional": 1,
      "type": "integer", "typetext": "<integer>"
    },
    "server": {"description": "SMTP 服务器地址。", "type": "string", "typetext": "<string>"},
    "username": {"description": "SMTP 认证的用户名", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-smtp-69d956eb-post-returns" id="api-cluster-notifications-endpoints-smtp-69d956eb-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/smtp)。

## `/cluster/notifications/endpoints/smtp/{name}` <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92" id="api-cluster-notifications-endpoints-smtp-name-da6bad92"></a>

原始接口路径：`/cluster/notifications/endpoints/smtp/{name}`。

### DELETE `/cluster/notifications/endpoints/smtp/{name}` <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-delete" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-delete"></a>

移除 smtp 端点

**方法标识：** `delete_smtp_endpoint`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-delete-parameters" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-delete-returns" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/notifications/endpoints/smtp/{name}` <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-get" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-get"></a>

返回指定的 smtp 端点

**方法标识：** `get_smtp_endpoint`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-get-parameters" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-get-returns" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-get-returns"></a>

```text
{
  "properties": {
    "author": {"description": "邮件作者。默认为 'Proxmox VE'。", "optional": 1, "type": "string"},
    "comment": {"description": "注释", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
    "from-address": {"description": "邮件的 `From` 地址", "type": "string"},
    "mailto": {"description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array"},
    "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array"},
    "mode": {"default": "tls", "description": "确定连接应使用哪种加密方法。", "enum": ["insecure", "starttls", "tls"], "optional": 1, "type": "string"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"},
    "port": {
      "description": "使用的端口。基于 TLS 的连接默认为 465，基于 STARTTLS 的连接默认为 587，不安全的纯文本连接默认为端口 25。", "optional": 1,
      "type": "integer"
    },
    "server": {"description": "SMTP 服务器地址。", "type": "string"}, "username": {"description": "SMTP 认证的用户名", "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/notifications/endpoints/smtp/{name}` <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-put" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-put"></a>

更新现有 smtp 端点

**方法标识：** `update_smtp_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-put-parameters" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `author` | 类型：string；必填：否；默认值：—<br>邮件作者。默认为 'Proxmox VE'。 |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `delete` | 类型：array；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `from-address` | 类型：string；必填：否；默认值：—<br>邮件的 `From` 地址 |
| `mailto` | 类型：array；必填：否；默认值：—<br>电子邮件收件人列表 |
| `mailto-user` | 类型：array；必填：否；默认值：—<br>用户列表 |
| `mode` | 类型：string；必填：否；默认值："tls"<br>确定连接应使用哪种加密方法。；可选值：`insecure`, `starttls`, `tls` |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |
| `password` | 类型：string；必填：否；默认值：—<br>SMTP 认证的密码 |
| `port` | 类型：integer；必填：否；默认值：—<br>使用的端口。基于 TLS 的连接默认为 465，基于 STARTTLS 的连接默认为 587，不安全的纯文本连接默认为端口 25。 |
| `server` | 类型：string；必填：否；默认值：—<br>SMTP 服务器地址。 |
| `username` | 类型：string；必填：否；默认值：—<br>SMTP 认证的用户名 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "author": {"description": "邮件作者。默认为 'Proxmox VE'。", "optional": 1, "type": "string", "typetext": "<string>"},
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {
      "description": "要删除的设置列表。", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "from-address": {"description": "邮件的 `From` 地址", "optional": 1, "type": "string", "typetext": "<string>"},
    "mailto": {
      "description": "电子邮件收件人列表", "items": {"format": "email-or-username", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "mailto-user": {"description": "用户列表", "items": {"format": "pve-userid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "mode": {"default": "tls", "description": "确定连接应使用哪种加密方法。", "enum": ["insecure", "starttls", "tls"], "optional": 1, "type": "string"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "password": {"description": "SMTP 认证的密码", "optional": 1, "type": "string", "typetext": "<string>"},
    "port": {
      "description": "使用的端口。基于 TLS 的连接默认为 465，基于 STARTTLS 的连接默认为 587，不安全的纯文本连接默认为端口 25。", "optional": 1,
      "type": "integer", "typetext": "<integer>"
    },
    "server": {"description": "SMTP 服务器地址。", "optional": 1, "type": "string", "typetext": "<string>"},
    "username": {"description": "SMTP 认证的用户名", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-smtp-name-da6bad92-put-returns" id="api-cluster-notifications-endpoints-smtp-name-da6bad92-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/smtp/{name})。

## `/cluster/notifications/endpoints/webhook` <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f" id="api-cluster-notifications-endpoints-webhook-4dcdce7f"></a>

原始接口路径：`/cluster/notifications/endpoints/webhook`。

### GET `/cluster/notifications/endpoints/webhook` <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f-get" id="api-cluster-notifications-endpoints-webhook-4dcdce7f-get"></a>

返回所有 webhook 端点的列表

**方法标识：** `get_webhook_endpoints`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f-get-parameters" id="api-cluster-notifications-endpoints-webhook-4dcdce7f-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f-get-returns" id="api-cluster-notifications-endpoints-webhook-4dcdce7f-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "body": {"description": "HTTP 正文，采用 base64 编码", "optional": 1, "type": "string"},
      "comment": {"description": "注释", "optional": 1, "type": "string"},
      "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
      "header": {
        "description": "要设置的 HTTP 标头。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
        "type": "array"
      },
      "method": {"description": "HTTP 方法", "enum": ["post", "put", "get"], "type": "string"},
      "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"},
      "origin": {"description": "显示此条目是用户创建还是内置", "enum": ["user-created", "builtin", "modified-builtin"], "type": "string"},
      "secret": {
        "description": "要设置的秘密信息。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
        "type": "array"
      },
      "url": {"description": "服务器 URL", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/notifications/endpoints/webhook` <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f-post" id="api-cluster-notifications-endpoints-webhook-4dcdce7f-post"></a>

创建新的 webhook 端点

**方法标识：** `create_webhook_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f-post-parameters" id="api-cluster-notifications-endpoints-webhook-4dcdce7f-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `body` | 类型：string；必填：否；默认值：—<br>HTTP 正文，采用 base64 编码 |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `header` | 类型：array；必填：否；默认值：—<br>要设置的 HTTP 标头。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `method` | 类型：string；必填：是；默认值：—<br>HTTP 方法；可选值：`post`, `put`, `get` |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |
| `secret` | 类型：array；必填：否；默认值：—<br>要设置的秘密信息。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `url` | 类型：string；必填：是；默认值：—<br>服务器 URL |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "body": {"description": "HTTP 正文，采用 base64 编码", "optional": 1, "type": "string", "typetext": "<string>"},
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "header": {
      "description": "要设置的 HTTP 标头。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "method": {"description": "HTTP 方法", "enum": ["post", "put", "get"], "type": "string"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "secret": {
      "description": "要设置的秘密信息。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "url": {"description": "服务器 URL", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-webhook-4dcdce7f-post-returns" id="api-cluster-notifications-endpoints-webhook-4dcdce7f-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/webhook)。

## `/cluster/notifications/endpoints/webhook/{name}` <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49" id="api-cluster-notifications-endpoints-webhook-name-1e127b49"></a>

原始接口路径：`/cluster/notifications/endpoints/webhook/{name}`。

### DELETE `/cluster/notifications/endpoints/webhook/{name}` <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-delete" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-delete"></a>

移除 webhook 端点

**方法标识：** `delete_webhook_endpoint`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-delete-parameters" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-delete-returns" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/notifications/endpoints/webhook/{name}` <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-get" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-get"></a>

返回指定的 webhook 端点

**方法标识：** `get_webhook_endpoint`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-get-parameters" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-get-returns" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-get-returns"></a>

```text
{
  "properties": {
    "body": {"description": "HTTP 正文，采用 base64 编码", "optional": 1, "type": "string"},
    "comment": {"description": "注释", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean"},
    "header": {
      "description": "要设置的 HTTP 标头。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
      "type": "array"
    },
    "method": {"description": "HTTP 方法", "enum": ["post", "put", "get"], "type": "string"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string"},
    "secret": {
      "description": "要设置的秘密信息。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
      "type": "array"
    },
    "url": {"description": "服务器 URL", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/notifications/endpoints/webhook/{name}` <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-put" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-put"></a>

更新现有 webhook 端点

**方法标识：** `update_webhook_endpoint`

**权限**

```text
{
  "check": [
    "and", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["or", ["perm", "/", ["Sys.Audit", "Sys.Modify"]], ["perm", "/", ["Sys.AccessNetwork"]]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-put-parameters" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `body` | 类型：string；必填：否；默认值：—<br>HTTP 正文，采用 base64 编码 |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `delete` | 类型：array；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此目标 |
| `header` | 类型：array；必填：否；默认值：—<br>要设置的 HTTP 标头。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `method` | 类型：string；必填：否；默认值：—<br>HTTP 方法；可选值：`post`, `put`, `get` |
| `name` | 类型：string；必填：是；默认值：—<br>端点名称。 |
| `secret` | 类型：array；必填：否；默认值：—<br>要设置的秘密信息。必须采用属性字符串格式：name=&lt;name&gt;,value=&lt;base64 of value&gt; |
| `url` | 类型：string；必填：否；默认值：—<br>服务器 URL |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "body": {"description": "HTTP 正文，采用 base64 编码", "optional": 1, "type": "string", "typetext": "<string>"},
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {
      "description": "要删除的设置列表。", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"default": 0, "description": "禁用此目标", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "header": {
      "description": "要设置的 HTTP 标头。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "method": {"description": "HTTP 方法", "enum": ["post", "put", "get"], "optional": 1, "type": "string"},
    "name": {"description": "端点名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "secret": {
      "description": "要设置的秘密信息。必须采用属性字符串格式：name=<name>,value=<base64 of value>", "items": {"type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "url": {"description": "服务器 URL", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-endpoints-webhook-name-1e127b49-put-returns" id="api-cluster-notifications-endpoints-webhook-name-1e127b49-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/webhook/{name})。

## `/cluster/notifications/targets` <a href="#api-cluster-notifications-targets-44cf3da5" id="api-cluster-notifications-targets-44cf3da5"></a>

原始接口路径：`/cluster/notifications/targets`。

### GET `/cluster/notifications/targets` <a href="#api-cluster-notifications-targets-44cf3da5-get" id="api-cluster-notifications-targets-44cf3da5-get"></a>

返回所有可用作通知目标的实体列表。

**方法标识：** `get_all_targets`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]],
    ["perm", "/mapping/notifications", ["Mapping.Use"]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-targets-44cf3da5-get-parameters" id="api-cluster-notifications-targets-44cf3da5-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-targets-44cf3da5-get-returns" id="api-cluster-notifications-targets-44cf3da5-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "注释", "optional": 1, "type": "string"},
      "disable": {"default": 0, "description": "显示此目标是否已禁用", "optional": 1, "type": "boolean"},
      "name": {"description": "目标名称。", "format": "pve-configid", "type": "string"},
      "origin": {"description": "显示此条目是用户创建还是内置", "enum": ["user-created", "builtin", "modified-builtin"], "type": "string"},
      "type": {"description": "目标类型。", "enum": ["sendmail", "gotify", "smtp", "webhook"], "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/targets)。

## `/cluster/notifications/targets/{name}/test` <a href="#api-cluster-notifications-targets-name-test-4406e6d7" id="api-cluster-notifications-targets-name-test-4406e6d7"></a>

原始接口路径：`/cluster/notifications/targets/{name}/test`。

### POST `/cluster/notifications/targets/{name}/test` <a href="#api-cluster-notifications-targets-name-test-4406e6d7-post" id="api-cluster-notifications-targets-name-test-4406e6d7-post"></a>

向提供的目标发送测试通知。

**方法标识：** `test_target`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]],
    ["perm", "/mapping/notifications", ["Mapping.Use"]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-targets-name-test-4406e6d7-post-parameters" id="api-cluster-notifications-targets-name-test-4406e6d7-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br>目标名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"description": "目标名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-targets-name-test-4406e6d7-post-returns" id="api-cluster-notifications-targets-name-test-4406e6d7-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/targets/{name}/test)。

## `/cluster/notifications/matchers` <a href="#api-cluster-notifications-matchers-d91fc9d7" id="api-cluster-notifications-matchers-d91fc9d7"></a>

原始接口路径：`/cluster/notifications/matchers`。

### GET `/cluster/notifications/matchers` <a href="#api-cluster-notifications-matchers-d91fc9d7-get" id="api-cluster-notifications-matchers-d91fc9d7-get"></a>

返回所有匹配器的列表

**方法标识：** `get_matchers`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]],
    ["perm", "/mapping/notifications", ["Mapping.Use"]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-matchers-d91fc9d7-get-parameters" id="api-cluster-notifications-matchers-d91fc9d7-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-notifications-matchers-d91fc9d7-get-returns" id="api-cluster-notifications-matchers-d91fc9d7-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "注释", "optional": 1, "type": "string"},
      "disable": {"default": 0, "description": "禁用此匹配器", "optional": 1, "type": "boolean"},
      "invert-match": {"description": "反转整个匹配器的匹配结果", "optional": 1, "type": "boolean"},
      "match-calendar": {"description": "匹配通知时间戳", "items": {"type": "string"}, "optional": 1, "type": "array"},
      "match-field": {
        "description": "要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex|exact):<field>=<value>", "items": {"type": "string"}, "optional": 1,
        "type": "array"
      },
      "match-severity": {"description": "要匹配的通知严重性", "items": {"type": "string"}, "optional": 1, "type": "array"},
      "mode": {"default": "all", "description": "指定多个属性时，在 'all' 和 'any' 之间选择", "enum": ["all", "any"], "optional": 1, "type": "string"},
      "name": {"description": "匹配器名称。", "format": "pve-configid", "type": "string"},
      "origin": {"description": "显示此条目是用户创建还是内置", "enum": ["user-created", "builtin", "modified-builtin"], "type": "string"},
      "target": {"description": "匹配时要通知的目标", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/notifications/matchers` <a href="#api-cluster-notifications-matchers-d91fc9d7-post" id="api-cluster-notifications-matchers-d91fc9d7-post"></a>

创建新的匹配器

**方法标识：** `create_matcher`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-matchers-d91fc9d7-post-parameters" id="api-cluster-notifications-matchers-d91fc9d7-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此匹配器 |
| `invert-match` | 类型：boolean；必填：否；默认值：—<br>反转整个匹配器的匹配结果 |
| `match-calendar` | 类型：array；必填：否；默认值：—<br>匹配通知时间戳 |
| `match-field` | 类型：array；必填：否；默认值：—<br>要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex\|exact):&lt;field&gt;=&lt;value&gt; |
| `match-severity` | 类型：array；必填：否；默认值：—<br>要匹配的通知严重性 |
| `mode` | 类型：string；必填：否；默认值："all"<br>指定多个属性时，在 'all' 和 'any' 之间选择；可选值：`all`, `any` |
| `name` | 类型：string；必填：是；默认值：—<br>匹配器名称。 |
| `target` | 类型：array；必填：否；默认值：—<br>匹配时要通知的目标 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"default": 0, "description": "禁用此匹配器", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "invert-match": {"description": "反转整个匹配器的匹配结果", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "match-calendar": {"description": "匹配通知时间戳", "items": {"type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "match-field": {
      "description": "要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex|exact):<field>=<value>", "items": {"type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "match-severity": {"description": "要匹配的通知严重性", "items": {"type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "mode": {"default": "all", "description": "指定多个属性时，在 'all' 和 'any' 之间选择", "enum": ["all", "any"], "optional": 1, "type": "string"},
    "name": {"description": "匹配器名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "target": {
      "description": "匹配时要通知的目标", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-matchers-d91fc9d7-post-returns" id="api-cluster-notifications-matchers-d91fc9d7-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matchers)。

## `/cluster/notifications/matchers/{name}` <a href="#api-cluster-notifications-matchers-name-c6629c60" id="api-cluster-notifications-matchers-name-c6629c60"></a>

原始接口路径：`/cluster/notifications/matchers/{name}`。

### DELETE `/cluster/notifications/matchers/{name}` <a href="#api-cluster-notifications-matchers-name-c6629c60-delete" id="api-cluster-notifications-matchers-name-c6629c60-delete"></a>

移除匹配器

**方法标识：** `delete_matcher`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-matchers-name-c6629c60-delete-parameters" id="api-cluster-notifications-matchers-name-c6629c60-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-matchers-name-c6629c60-delete-returns" id="api-cluster-notifications-matchers-name-c6629c60-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/notifications/matchers/{name}` <a href="#api-cluster-notifications-matchers-name-c6629c60-get" id="api-cluster-notifications-matchers-name-c6629c60-get"></a>

返回指定的匹配器

**方法标识：** `get_matcher`

**权限**

```text
{"check": ["or", ["perm", "/mapping/notifications", ["Mapping.Modify"]], ["perm", "/mapping/notifications", ["Mapping.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-matchers-name-c6629c60-get-parameters" id="api-cluster-notifications-matchers-name-c6629c60-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"name": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-matchers-name-c6629c60-get-returns" id="api-cluster-notifications-matchers-name-c6629c60-get-returns"></a>

```text
{
  "properties": {
    "comment": {"description": "注释", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"default": 0, "description": "禁用此匹配器", "optional": 1, "type": "boolean"},
    "invert-match": {"description": "反转整个匹配器的匹配结果", "optional": 1, "type": "boolean"},
    "match-calendar": {"description": "匹配通知时间戳", "items": {"type": "string"}, "optional": 1, "type": "array"},
    "match-field": {
      "description": "要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex|exact):<field>=<value>", "items": {"type": "string"}, "optional": 1,
      "type": "array"
    },
    "match-severity": {"description": "要匹配的通知严重性", "items": {"type": "string"}, "optional": 1, "type": "array"},
    "mode": {"default": "all", "description": "指定多个属性时，在 'all' 和 'any' 之间选择", "enum": ["all", "any"], "optional": 1, "type": "string"},
    "name": {"description": "匹配器名称。", "format": "pve-configid", "type": "string"},
    "target": {"description": "匹配时要通知的目标", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array"}
  },
  "type": "object"
}
```

### PUT `/cluster/notifications/matchers/{name}` <a href="#api-cluster-notifications-matchers-name-c6629c60-put" id="api-cluster-notifications-matchers-name-c6629c60-put"></a>

更新现有匹配器

**方法标识：** `update_matcher`

**权限**

```text
{"check": ["perm", "/mapping/notifications", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-notifications-matchers-name-c6629c60-put-parameters" id="api-cluster-notifications-matchers-name-c6629c60-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>注释 |
| `delete` | 类型：array；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：0<br>禁用此匹配器 |
| `invert-match` | 类型：boolean；必填：否；默认值：—<br>反转整个匹配器的匹配结果 |
| `match-calendar` | 类型：array；必填：否；默认值：—<br>匹配通知时间戳 |
| `match-field` | 类型：array；必填：否；默认值：—<br>要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex\|exact):&lt;field&gt;=&lt;value&gt; |
| `match-severity` | 类型：array；必填：否；默认值：—<br>要匹配的通知严重性 |
| `mode` | 类型：string；必填：否；默认值："all"<br>指定多个属性时，在 'all' 和 'any' 之间选择；可选值：`all`, `any` |
| `name` | 类型：string；必填：是；默认值：—<br>匹配器名称。 |
| `target` | 类型：array；必填：否；默认值：—<br>匹配时要通知的目标 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "注释", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {
      "description": "要删除的设置列表。", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"default": 0, "description": "禁用此匹配器", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "invert-match": {"description": "反转整个匹配器的匹配结果", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "match-calendar": {"description": "匹配通知时间戳", "items": {"type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "match-field": {
      "description": "要匹配的元数据字段（正则表达式或精确匹配）。必须采用格式 (regex|exact):<field>=<value>", "items": {"type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "match-severity": {"description": "要匹配的通知严重性", "items": {"type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "mode": {"default": "all", "description": "指定多个属性时，在 'all' 和 'any' 之间选择", "enum": ["all", "any"], "optional": 1, "type": "string"},
    "name": {"description": "匹配器名称。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "target": {
      "description": "匹配时要通知的目标", "items": {"format": "pve-configid", "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-notifications-matchers-name-c6629c60-put-returns" id="api-cluster-notifications-matchers-name-c6629c60-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/matchers/{name})。

## `/cluster/qemu` <a href="#api-cluster-qemu-6a09d254" id="api-cluster-qemu-6a09d254"></a>

原始接口路径：`/cluster/qemu`。

### GET `/cluster/qemu` <a href="#api-cluster-qemu-6a09d254-get" id="api-cluster-qemu-6a09d254-get"></a>

集群范围的 QEMU 索引

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-qemu-6a09d254-get-parameters" id="api-cluster-qemu-6a09d254-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-qemu-6a09d254-get-returns" id="api-cluster-qemu-6a09d254-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu)。

## `/cluster/qemu/cpu-flags` <a href="#api-cluster-qemu-cpu-flags-7542d748" id="api-cluster-qemu-cpu-flags-7542d748"></a>

原始接口路径：`/cluster/qemu/cpu-flags`。

### GET `/cluster/qemu/cpu-flags` <a href="#api-cluster-qemu-cpu-flags-7542d748-get" id="api-cluster-qemu-cpu-flags-7542d748-get"></a>

可用 CPU 标志列表。目前仅针对 x86_64 实现，对于 aarch64 返回空列表。

**方法标识：** `index`

**权限**

```text
{"check": ["or", ["perm", "/nodes", ["Sys.Audit"]], ["perm", "/mapping/cpu", ["Mapping.Audit", "Mapping.Use", "Mapping.Modify"], "any", 1]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-qemu-cpu-flags-7542d748-get-parameters" id="api-cluster-qemu-cpu-flags-7542d748-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `accel` | 类型：string；必填：否；默认值："kvm"<br>要检查节点兼容性的加速类型。；可选值：`kvm`, `tcg` |
| `arch` | 类型：string；必填：否；默认值：—<br>虚拟处理器架构。默认为宿主机架构。；可选值：`x86_64`, `aarch64` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "accel": {"default": "kvm", "description": "要检查节点兼容性的加速类型。", "enum": ["kvm", "tcg"], "optional": 1, "type": "string"},
    "arch": {"description": "虚拟处理器架构。默认为宿主机架构。", "enum": ["x86_64", "aarch64"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-qemu-cpu-flags-7542d748-get-returns" id="api-cluster-qemu-cpu-flags-7542d748-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "description": {"description": "CPU 标志描述。", "optional": 1, "type": "string"}, "name": {"description": "CPU 标志名称。", "type": "string"},
      "supported-on": {
        "description": "使用所选加速类型（“accel”）时支持此标志的节点列表。",
        "items": {"description": "集群节点名称。", "format": "pve-node", "type": "string"}, "optional": 1, "type": "array"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu/cpu-flags)。

## `/cluster/qemu/custom-cpu-models` <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523" id="api-cluster-qemu-custom-cpu-models-9d4cf523"></a>

原始接口路径：`/cluster/qemu/custom-cpu-models`。

### GET `/cluster/qemu/custom-cpu-models` <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523-get" id="api-cluster-qemu-custom-cpu-models-9d4cf523-get"></a>

列出用户可见的所有自定义 CPU 模型定义。

**方法标识：** `config`

**权限**

```text
{"description": "仅列出用户在 '/mapping/cpu/<name>' 上拥有 'Mapping.Modify'、'Mapping.Use' 或 'Mapping.Audit' 权限的条目。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523-get-parameters" id="api-cluster-qemu-custom-cpu-models-9d4cf523-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523-get-returns" id="api-cluster-qemu-custom-cpu-models-9d4cf523-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "cputype": {
        "default": "kvm64", "default_key": 1, "description": "模拟的 CPU 类型。可以是默认名称或自定义名称（自定义模型名称必须带有 'custom-' 前缀）。",
        "format_description": "string", "optional": 1, "type": "string"
      },
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "flags": {
        "description": "以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
        "format_description": "+FLAG[;-FLAG...]", "optional": 1, "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
        "type": "string"
      },
      "guest-phys-bits": {"description": "客户机可用的物理地址位数。", "maximum": 64, "minimum": 32, "optional": 1, "type": "integer"},
      "hidden": {"default": 0, "description": "不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。", "optional": 1, "type": "boolean"},
      "hv-vendor-id": {
        "description": "Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。", "format_description": "vendor-id", "optional": 1,
        "pattern": "(?^u:[a-zA-Z0-9]{1,12})", "type": "string"
      },
      "level": {
        "description": "客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。",
        "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer"
      },
      "phys-bits": {
        "description": "向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。",
        "format": "pve-phys-bits", "format_description": "8-64|host", "optional": 1, "type": "string"
      },
      "reported-model": {
        "default": "kvm64",
        "description": "向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。",
        "enum": [
          "486", "a64fx", "athlon", "Broadwell", "Broadwell-IBRS", "Broadwell-noTSX", "Broadwell-noTSX-IBRS", "Cascadelake-Server", "Cascadelake-Server-noTSX",
          "Cascadelake-Server-v2", "Cascadelake-Server-v4", "Cascadelake-Server-v5", "ClearwaterForest", "ClearwaterForest-v2", "ClearwaterForest-v3", "Conroe",
          "Cooperlake", "Cooperlake-v2", "core2duo", "coreduo", "cortex-a35", "cortex-a53", "cortex-a55", "cortex-a57", "cortex-a710", "cortex-a72",
          "cortex-a76", "cortex-a78ae", "DiamondRapids", "EPYC", "EPYC-Genoa", "EPYC-Genoa-v2", "EPYC-IBPB", "EPYC-Milan", "EPYC-Milan-v2", "EPYC-Milan-v3",
          "EPYC-Rome", "EPYC-Rome-v2", "EPYC-Rome-v3", "EPYC-Rome-v4", "EPYC-Rome-v5", "EPYC-Turin", "EPYC-v3", "EPYC-v4", "EPYC-v5", "GraniteRapids",
          "GraniteRapids-v2", "GraniteRapids-v3", "GraniteRapids-v4", "GraniteRapids-v5", "Haswell", "Haswell-IBRS", "Haswell-noTSX", "Haswell-noTSX-IBRS",
          "host", "Icelake-Client", "Icelake-Client-noTSX", "Icelake-Server", "Icelake-Server-noTSX", "Icelake-Server-v3", "Icelake-Server-v4",
          "Icelake-Server-v5", "Icelake-Server-v6", "Icelake-Server-v7", "IvyBridge", "IvyBridge-IBRS", "KnightsMill", "kvm32", "kvm64", "max", "Nehalem",
          "Nehalem-IBRS", "neoverse-n1", "neoverse-n2", "neoverse-v1", "Opteron_G1", "Opteron_G2", "Opteron_G3", "Opteron_G4", "Opteron_G5", "Penryn",
          "pentium", "pentium2", "pentium3", "phenom", "qemu32", "qemu64", "SandyBridge", "SandyBridge-IBRS", "SapphireRapids", "SapphireRapids-v2",
          "SapphireRapids-v3", "SapphireRapids-v4", "SapphireRapids-v5", "SapphireRapids-v6", "SierraForest", "SierraForest-v2", "SierraForest-v3",
          "SierraForest-v4", "SierraForest-v5", "Skylake-Client", "Skylake-Client-IBRS", "Skylake-Client-noTSX-IBRS", "Skylake-Client-v4", "Skylake-Server",
          "Skylake-Server-IBRS", "Skylake-Server-noTSX-IBRS", "Skylake-Server-v4", "Skylake-Server-v5", "Westmere", "Westmere-IBRS"
        ],
        "optional": 1, "type": "string"
      }
    },
    "type": "object"
  },
  "links": [{"href": "{cputype}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/qemu/custom-cpu-models` <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523-post" id="api-cluster-qemu-custom-cpu-models-9d4cf523-post"></a>

添加自定义 CPU 模型定义。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/mapping/cpu", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523-post-parameters" id="api-cluster-qemu-custom-cpu-models-9d4cf523-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cputype` | 类型：string；必填：是；默认值：—<br>自定义 CPU 模型名称。'custom-' 前缀可选。 |
| `flags` | 类型：string；必填：否；默认值：—<br>以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd |
| `guest-phys-bits` | 类型：integer；必填：否；默认值：—<br>客户机可用的物理地址位数。 |
| `hidden` | 类型：boolean；必填：否；默认值：0<br>不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。 |
| `hv-vendor-id` | 类型：string；必填：否；默认值：—<br>Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。 |
| `level` | 类型：integer；必填：否；默认值：—<br>客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。 |
| `phys-bits` | 类型：string；必填：否；默认值：—<br>向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。 |
| `reported-model` | 类型：string；必填：是；默认值："kvm64"<br>向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。；可选值：`486`, `a64fx`, `athlon`, `Broadwell`, `Broadwell-IBRS`, `Broadwell-noTSX`, `Broadwell-noTSX-IBRS`, `Cascadelake-Server`, `Cascadelake-Server-noTSX`, `Cascadelake-Server-v2`, `Cascadelake-Server-v4`, `Cascadelake-Server-v5`, `ClearwaterForest`, `ClearwaterForest-v2`, `ClearwaterForest-v3`, `Conroe`, `Cooperlake`, `Cooperlake-v2`, `core2duo`, `coreduo`, `cortex-a35`, `cortex-a53`, `cortex-a55`, `cortex-a57`, `cortex-a710`, `cortex-a72`, `cortex-a76`, `cortex-a78ae`, `DiamondRapids`, `EPYC`, `EPYC-Genoa`, `EPYC-Genoa-v2`, `EPYC-IBPB`, `EPYC-Milan`, `EPYC-Milan-v2`, `EPYC-Milan-v3`, `EPYC-Rome`, `EPYC-Rome-v2`, `EPYC-Rome-v3`, `EPYC-Rome-v4`, `EPYC-Rome-v5`, `EPYC-Turin`, `EPYC-v3`, `EPYC-v4`, `EPYC-v5`, `GraniteRapids`, `GraniteRapids-v2`, `GraniteRapids-v3`, `GraniteRapids-v4`, `GraniteRapids-v5`, `Haswell`, `Haswell-IBRS`, `Haswell-noTSX`, `Haswell-noTSX-IBRS`, `host`, `Icelake-Client`, `Icelake-Client-noTSX`, `Icelake-Server`, `Icelake-Server-noTSX`, `Icelake-Server-v3`, `Icelake-Server-v4`, `Icelake-Server-v5`, `Icelake-Server-v6`, `Icelake-Server-v7`, `IvyBridge`, `IvyBridge-IBRS`, `KnightsMill`, `kvm32`, `kvm64`, `max`, `Nehalem`, `Nehalem-IBRS`, `neoverse-n1`, `neoverse-n2`, `neoverse-v1`, `Opteron_G1`, `Opteron_G2`, `Opteron_G3`, `Opteron_G4`, `Opteron_G5`, `Penryn`, `pentium`, `pentium2`, `pentium3`, `phenom`, `qemu32`, `qemu64`, `SandyBridge`, `SandyBridge-IBRS`, `SapphireRapids`, `SapphireRapids-v2`, `SapphireRapids-v3`, `SapphireRapids-v4`, `SapphireRapids-v5`, `SapphireRapids-v6`, `SierraForest`, `SierraForest-v2`, `SierraForest-v3`, `SierraForest-v4`, `SierraForest-v5`, `Skylake-Client`, `Skylake-Client-IBRS`, `Skylake-Client-noTSX-IBRS`, `Skylake-Client-v4`, `Skylake-Server`, `Skylake-Server-IBRS`, `Skylake-Server-noTSX-IBRS`, `Skylake-Server-v4`, `Skylake-Server-v5`, `Westmere`, `Westmere-IBRS` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cputype": {
      "description": "自定义 CPU 模型名称。'custom-' 前缀可选。", "format": "pve-configid", "maxLength": 40, "type": "string", "typetext": "<string>"
    },
    "flags": {
      "description": "以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
      "format_description": "+FLAG[;-FLAG...]", "optional": 1, "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
      "type": "string"
    },
    "guest-phys-bits": {
      "description": "客户机可用的物理地址位数。", "maximum": 64, "minimum": 32, "optional": 1, "type": "integer", "typetext": "<integer> (32 - 64)"
    },
    "hidden": {"default": 0, "description": "不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "hv-vendor-id": {
      "description": "Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。", "format_description": "vendor-id", "optional": 1,
      "pattern": "(?^u:[a-zA-Z0-9]{1,12})", "type": "string"
    },
    "level": {
      "description": "客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。",
      "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 4294967295)"
    },
    "phys-bits": {
      "description": "向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。",
      "format": "pve-phys-bits", "format_description": "8-64|host", "optional": 1, "type": "string", "typetext": "<8-64|host>"
    },
    "reported-model": {
      "default": "kvm64",
      "description": "向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。",
      "enum": [
        "486", "a64fx", "athlon", "Broadwell", "Broadwell-IBRS", "Broadwell-noTSX", "Broadwell-noTSX-IBRS", "Cascadelake-Server", "Cascadelake-Server-noTSX",
        "Cascadelake-Server-v2", "Cascadelake-Server-v4", "Cascadelake-Server-v5", "ClearwaterForest", "ClearwaterForest-v2", "ClearwaterForest-v3", "Conroe",
        "Cooperlake", "Cooperlake-v2", "core2duo", "coreduo", "cortex-a35", "cortex-a53", "cortex-a55", "cortex-a57", "cortex-a710", "cortex-a72", "cortex-a76",
        "cortex-a78ae", "DiamondRapids", "EPYC", "EPYC-Genoa", "EPYC-Genoa-v2", "EPYC-IBPB", "EPYC-Milan", "EPYC-Milan-v2", "EPYC-Milan-v3", "EPYC-Rome",
        "EPYC-Rome-v2", "EPYC-Rome-v3", "EPYC-Rome-v4", "EPYC-Rome-v5", "EPYC-Turin", "EPYC-v3", "EPYC-v4", "EPYC-v5", "GraniteRapids", "GraniteRapids-v2",
        "GraniteRapids-v3", "GraniteRapids-v4", "GraniteRapids-v5", "Haswell", "Haswell-IBRS", "Haswell-noTSX", "Haswell-noTSX-IBRS", "host", "Icelake-Client",
        "Icelake-Client-noTSX", "Icelake-Server", "Icelake-Server-noTSX", "Icelake-Server-v3", "Icelake-Server-v4", "Icelake-Server-v5", "Icelake-Server-v6",
        "Icelake-Server-v7", "IvyBridge", "IvyBridge-IBRS", "KnightsMill", "kvm32", "kvm64", "max", "Nehalem", "Nehalem-IBRS", "neoverse-n1", "neoverse-n2",
        "neoverse-v1", "Opteron_G1", "Opteron_G2", "Opteron_G3", "Opteron_G4", "Opteron_G5", "Penryn", "pentium", "pentium2", "pentium3", "phenom", "qemu32",
        "qemu64", "SandyBridge", "SandyBridge-IBRS", "SapphireRapids", "SapphireRapids-v2", "SapphireRapids-v3", "SapphireRapids-v4", "SapphireRapids-v5",
        "SapphireRapids-v6", "SierraForest", "SierraForest-v2", "SierraForest-v3", "SierraForest-v4", "SierraForest-v5", "Skylake-Client",
        "Skylake-Client-IBRS", "Skylake-Client-noTSX-IBRS", "Skylake-Client-v4", "Skylake-Server", "Skylake-Server-IBRS", "Skylake-Server-noTSX-IBRS",
        "Skylake-Server-v4", "Skylake-Server-v5", "Westmere", "Westmere-IBRS"
      ],
      "optional": 0, "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-qemu-custom-cpu-models-9d4cf523-post-returns" id="api-cluster-qemu-custom-cpu-models-9d4cf523-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu/custom-cpu-models)。

## `/cluster/qemu/custom-cpu-models/{cputype}` <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a"></a>

原始接口路径：`/cluster/qemu/custom-cpu-models/{cputype}`。

### DELETE `/cluster/qemu/custom-cpu-models/{cputype}` <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-delete" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-delete"></a>

删除自定义 CPU 模型定义。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/mapping/cpu/{cputype}", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-delete-parameters" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cputype` | 类型：string；必填：是；默认值：—<br>要删除的自定义模型。'custom-' 前缀可选。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"cputype": {"description": "要删除的自定义模型。'custom-' 前缀可选。", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-delete-returns" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/qemu/custom-cpu-models/{cputype}` <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-get" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-get"></a>

获取指定自定义 CPU 模型的详细信息。

**方法标识：** `info`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/cpu/{cputype}", ["Mapping.Audit"]], ["perm", "/mapping/cpu/{cputype}", ["Mapping.Use"]],
    ["perm", "/mapping/cpu/{cputype}", ["Mapping.Modify"]]
  ]
}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-get-parameters" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cputype` | 类型：string；必填：是；默认值：—<br>要查询的 CPU 模型名称。'custom-' 前缀可选。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"cputype": {"description": "要查询的 CPU 模型名称。'custom-' 前缀可选。", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-get-returns" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-get-returns"></a>

```text
{
  "properties": {
    "cputype": {
      "default": "kvm64", "default_key": 1, "description": "模拟的 CPU 类型。可以是默认名称或自定义名称（自定义模型名称必须带有 'custom-' 前缀）。",
      "format_description": "string", "optional": 1, "type": "string"
    },
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "flags": {
      "description": "以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
      "format_description": "+FLAG[;-FLAG...]", "optional": 1, "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
      "type": "string"
    },
    "guest-phys-bits": {"description": "客户机可用的物理地址位数。", "maximum": 64, "minimum": 32, "optional": 1, "type": "integer"},
    "hidden": {"default": 0, "description": "不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。", "optional": 1, "type": "boolean"},
    "hv-vendor-id": {
      "description": "Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。", "format_description": "vendor-id", "optional": 1,
      "pattern": "(?^u:[a-zA-Z0-9]{1,12})", "type": "string"
    },
    "level": {
      "description": "客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。",
      "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer"
    },
    "phys-bits": {
      "description": "向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。",
      "format": "pve-phys-bits", "format_description": "8-64|host", "optional": 1, "type": "string"
    },
    "reported-model": {
      "default": "kvm64",
      "description": "向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。",
      "enum": [
        "486", "a64fx", "athlon", "Broadwell", "Broadwell-IBRS", "Broadwell-noTSX", "Broadwell-noTSX-IBRS", "Cascadelake-Server", "Cascadelake-Server-noTSX",
        "Cascadelake-Server-v2", "Cascadelake-Server-v4", "Cascadelake-Server-v5", "ClearwaterForest", "ClearwaterForest-v2", "ClearwaterForest-v3", "Conroe",
        "Cooperlake", "Cooperlake-v2", "core2duo", "coreduo", "cortex-a35", "cortex-a53", "cortex-a55", "cortex-a57", "cortex-a710", "cortex-a72", "cortex-a76",
        "cortex-a78ae", "DiamondRapids", "EPYC", "EPYC-Genoa", "EPYC-Genoa-v2", "EPYC-IBPB", "EPYC-Milan", "EPYC-Milan-v2", "EPYC-Milan-v3", "EPYC-Rome",
        "EPYC-Rome-v2", "EPYC-Rome-v3", "EPYC-Rome-v4", "EPYC-Rome-v5", "EPYC-Turin", "EPYC-v3", "EPYC-v4", "EPYC-v5", "GraniteRapids", "GraniteRapids-v2",
        "GraniteRapids-v3", "GraniteRapids-v4", "GraniteRapids-v5", "Haswell", "Haswell-IBRS", "Haswell-noTSX", "Haswell-noTSX-IBRS", "host", "Icelake-Client",
        "Icelake-Client-noTSX", "Icelake-Server", "Icelake-Server-noTSX", "Icelake-Server-v3", "Icelake-Server-v4", "Icelake-Server-v5", "Icelake-Server-v6",
        "Icelake-Server-v7", "IvyBridge", "IvyBridge-IBRS", "KnightsMill", "kvm32", "kvm64", "max", "Nehalem", "Nehalem-IBRS", "neoverse-n1", "neoverse-n2",
        "neoverse-v1", "Opteron_G1", "Opteron_G2", "Opteron_G3", "Opteron_G4", "Opteron_G5", "Penryn", "pentium", "pentium2", "pentium3", "phenom", "qemu32",
        "qemu64", "SandyBridge", "SandyBridge-IBRS", "SapphireRapids", "SapphireRapids-v2", "SapphireRapids-v3", "SapphireRapids-v4", "SapphireRapids-v5",
        "SapphireRapids-v6", "SierraForest", "SierraForest-v2", "SierraForest-v3", "SierraForest-v4", "SierraForest-v5", "Skylake-Client",
        "Skylake-Client-IBRS", "Skylake-Client-noTSX-IBRS", "Skylake-Client-v4", "Skylake-Server", "Skylake-Server-IBRS", "Skylake-Server-noTSX-IBRS",
        "Skylake-Server-v4", "Skylake-Server-v5", "Westmere", "Westmere-IBRS"
      ],
      "optional": 1, "type": "string"
    }
  },
  "type": "object"
}
```

### PUT `/cluster/qemu/custom-cpu-models/{cputype}` <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-put" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-put"></a>

更新自定义 CPU 模型定义。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/mapping/cpu/{cputype}", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-put-parameters" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cputype` | 类型：string；必填：是；默认值：—<br>自定义 CPU 模型名称。'custom-' 前缀可选。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的属性列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `flags` | 类型：string；必填：否；默认值：—<br>以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd |
| `guest-phys-bits` | 类型：integer；必填：否；默认值：—<br>客户机可用的物理地址位数。 |
| `hidden` | 类型：boolean；必填：否；默认值：0<br>不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。 |
| `hv-vendor-id` | 类型：string；必填：否；默认值：—<br>Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。 |
| `level` | 类型：integer；必填：否；默认值：—<br>客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。 |
| `phys-bits` | 类型：string；必填：否；默认值：—<br>向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。 |
| `reported-model` | 类型：string；必填：否；默认值："kvm64"<br>向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。；可选值：`486`, `a64fx`, `athlon`, `Broadwell`, `Broadwell-IBRS`, `Broadwell-noTSX`, `Broadwell-noTSX-IBRS`, `Cascadelake-Server`, `Cascadelake-Server-noTSX`, `Cascadelake-Server-v2`, `Cascadelake-Server-v4`, `Cascadelake-Server-v5`, `ClearwaterForest`, `ClearwaterForest-v2`, `ClearwaterForest-v3`, `Conroe`, `Cooperlake`, `Cooperlake-v2`, `core2duo`, `coreduo`, `cortex-a35`, `cortex-a53`, `cortex-a55`, `cortex-a57`, `cortex-a710`, `cortex-a72`, `cortex-a76`, `cortex-a78ae`, `DiamondRapids`, `EPYC`, `EPYC-Genoa`, `EPYC-Genoa-v2`, `EPYC-IBPB`, `EPYC-Milan`, `EPYC-Milan-v2`, `EPYC-Milan-v3`, `EPYC-Rome`, `EPYC-Rome-v2`, `EPYC-Rome-v3`, `EPYC-Rome-v4`, `EPYC-Rome-v5`, `EPYC-Turin`, `EPYC-v3`, `EPYC-v4`, `EPYC-v5`, `GraniteRapids`, `GraniteRapids-v2`, `GraniteRapids-v3`, `GraniteRapids-v4`, `GraniteRapids-v5`, `Haswell`, `Haswell-IBRS`, `Haswell-noTSX`, `Haswell-noTSX-IBRS`, `host`, `Icelake-Client`, `Icelake-Client-noTSX`, `Icelake-Server`, `Icelake-Server-noTSX`, `Icelake-Server-v3`, `Icelake-Server-v4`, `Icelake-Server-v5`, `Icelake-Server-v6`, `Icelake-Server-v7`, `IvyBridge`, `IvyBridge-IBRS`, `KnightsMill`, `kvm32`, `kvm64`, `max`, `Nehalem`, `Nehalem-IBRS`, `neoverse-n1`, `neoverse-n2`, `neoverse-v1`, `Opteron_G1`, `Opteron_G2`, `Opteron_G3`, `Opteron_G4`, `Opteron_G5`, `Penryn`, `pentium`, `pentium2`, `pentium3`, `phenom`, `qemu32`, `qemu64`, `SandyBridge`, `SandyBridge-IBRS`, `SapphireRapids`, `SapphireRapids-v2`, `SapphireRapids-v3`, `SapphireRapids-v4`, `SapphireRapids-v5`, `SapphireRapids-v6`, `SierraForest`, `SierraForest-v2`, `SierraForest-v3`, `SierraForest-v4`, `SierraForest-v5`, `Skylake-Client`, `Skylake-Client-IBRS`, `Skylake-Client-noTSX-IBRS`, `Skylake-Client-v4`, `Skylake-Server`, `Skylake-Server-IBRS`, `Skylake-Server-noTSX-IBRS`, `Skylake-Server-v4`, `Skylake-Server-v5`, `Westmere`, `Westmere-IBRS` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cputype": {
      "description": "自定义 CPU 模型名称。'custom-' 前缀可选。", "format": "pve-configid", "maxLength": 40, "type": "string", "typetext": "<string>"
    },
    "delete": {"description": "要删除的属性列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "flags": {
      "description": "以 ';' 分隔的额外 CPU 标志列表。使用 '+FLAG' 启用标志，使用 '-FLAG' 禁用标志。有一个特殊的 'nested-virt' 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 为 'svm'，Intel 为 'vmx'）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，虚拟机特定标志必须来自以下集合：aes, amd-no-ssb, amd-ssbd, hv-evmcs, hv-tlbflush, ibpb, md-clear, nested-virt, pcid, pdpe1gb, spec-ctrl, ssbd, virt-ssbd",
      "format_description": "+FLAG[;-FLAG...]", "optional": 1, "pattern": "(?^u:(?^u:([+-])([a-zA-Z0-9\\-_\\.]+))(;(?^u:([+-])([a-zA-Z0-9\\-_\\.]+)))*)",
      "type": "string"
    },
    "guest-phys-bits": {
      "description": "客户机可用的物理地址位数。", "maximum": 64, "minimum": 32, "optional": 1, "type": "integer", "typetext": "<integer> (32 - 64)"
    },
    "hidden": {"default": 0, "description": "不标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "hv-vendor-id": {
      "description": "Hyper-V 厂商 ID。Windows 客户机中的某些驱动程序或程序需要特定 ID。", "format_description": "vendor-id", "optional": 1,
      "pattern": "(?^u:[a-zA-Z0-9]{1,12})", "type": "string"
    },
    "level": {
      "description": "客户机可查询的基本 CPUID 叶的最大输入值，即厂商（叶 0）、系列/型号/步进及特性位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶会被隐藏。在较新的 Intel 宿主机上运行的 Windows 客户机中，将其设置为 '30' 是解决 Hyper-V 启动失败的常见方法。仅在 vCPU 架构为 x86_64 时适用。",
      "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 4294967295)"
    },
    "phys-bits": {
      "description": "向客户机操作系统报告的物理内存地址位数。应小于或等于宿主机的值。设置为 'host' 可使用宿主机 CPU 的值，但请注意，这样做会导致无法在线迁移到具有其他值的 CPU。",
      "format": "pve-phys-bits", "format_description": "8-64|host", "optional": 1, "type": "string", "typetext": "<8-64|host>"
    },
    "reported-model": {
      "default": "kvm64",
      "description": "向客户机报告的 CPU 模型和厂商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效，默认模型始终向客户机操作系统报告自身。",
      "enum": [
        "486", "a64fx", "athlon", "Broadwell", "Broadwell-IBRS", "Broadwell-noTSX", "Broadwell-noTSX-IBRS", "Cascadelake-Server", "Cascadelake-Server-noTSX",
        "Cascadelake-Server-v2", "Cascadelake-Server-v4", "Cascadelake-Server-v5", "ClearwaterForest", "ClearwaterForest-v2", "ClearwaterForest-v3", "Conroe",
        "Cooperlake", "Cooperlake-v2", "core2duo", "coreduo", "cortex-a35", "cortex-a53", "cortex-a55", "cortex-a57", "cortex-a710", "cortex-a72", "cortex-a76",
        "cortex-a78ae", "DiamondRapids", "EPYC", "EPYC-Genoa", "EPYC-Genoa-v2", "EPYC-IBPB", "EPYC-Milan", "EPYC-Milan-v2", "EPYC-Milan-v3", "EPYC-Rome",
        "EPYC-Rome-v2", "EPYC-Rome-v3", "EPYC-Rome-v4", "EPYC-Rome-v5", "EPYC-Turin", "EPYC-v3", "EPYC-v4", "EPYC-v5", "GraniteRapids", "GraniteRapids-v2",
        "GraniteRapids-v3", "GraniteRapids-v4", "GraniteRapids-v5", "Haswell", "Haswell-IBRS", "Haswell-noTSX", "Haswell-noTSX-IBRS", "host", "Icelake-Client",
        "Icelake-Client-noTSX", "Icelake-Server", "Icelake-Server-noTSX", "Icelake-Server-v3", "Icelake-Server-v4", "Icelake-Server-v5", "Icelake-Server-v6",
        "Icelake-Server-v7", "IvyBridge", "IvyBridge-IBRS", "KnightsMill", "kvm32", "kvm64", "max", "Nehalem", "Nehalem-IBRS", "neoverse-n1", "neoverse-n2",
        "neoverse-v1", "Opteron_G1", "Opteron_G2", "Opteron_G3", "Opteron_G4", "Opteron_G5", "Penryn", "pentium", "pentium2", "pentium3", "phenom", "qemu32",
        "qemu64", "SandyBridge", "SandyBridge-IBRS", "SapphireRapids", "SapphireRapids-v2", "SapphireRapids-v3", "SapphireRapids-v4", "SapphireRapids-v5",
        "SapphireRapids-v6", "SierraForest", "SierraForest-v2", "SierraForest-v3", "SierraForest-v4", "SierraForest-v5", "Skylake-Client",
        "Skylake-Client-IBRS", "Skylake-Client-noTSX-IBRS", "Skylake-Client-v4", "Skylake-Server", "Skylake-Server-IBRS", "Skylake-Server-noTSX-IBRS",
        "Skylake-Server-v4", "Skylake-Server-v5", "Westmere", "Westmere-IBRS"
      ],
      "optional": 1, "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-qemu-custom-cpu-models-cputype-892d833a-put-returns" id="api-cluster-qemu-custom-cpu-models-cputype-892d833a-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu/custom-cpu-models/{cputype})。

## `/cluster/config` <a href="#api-cluster-config-0e41d22c" id="api-cluster-config-0e41d22c"></a>

原始接口路径：`/cluster/config`。

### GET `/cluster/config` <a href="#api-cluster-config-0e41d22c-get" id="api-cluster-config-0e41d22c-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-config-0e41d22c-get-parameters" id="api-cluster-config-0e41d22c-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-config-0e41d22c-get-returns" id="api-cluster-config-0e41d22c-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/config` <a href="#api-cluster-config-0e41d22c-post" id="api-cluster-config-0e41d22c-post"></a>

生成新的集群配置。如果未提供链路，则默认将本地 IP 地址用作 link0。

**方法标识：** `create`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-config-0e41d22c-post-parameters" id="api-cluster-config-0e41d22c-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `clustername` | 类型：string；必填：是；默认值：—<br>集群名称。 |
| `link[n]` | 类型：string；必填：否；默认值：—<br>单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7） |
| `nodeid` | 类型：integer；必填：否；默认值：—<br>此节点的节点 ID。 |
| `token-coefficient` | 类型：integer；必填：否；默认值：125<br>用于确定 Corosync 令牌超时时间的系数。详情请参阅 corosync.conf(5) 手册。 |
| `votes` | 类型：integer；必填：否；默认值：—<br>此节点的票数。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "clustername": {"description": "集群名称。", "format": "pve-node", "maxLength": 15, "type": "string", "typetext": "<string>"},
    "link[n]": {
      "description": "单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7）",
      "format": {
        "address": {
          "default_key": 1, "description": "此 corosync 链路地址的主机名（或 IP）。", "format": "address", "format_description": "IP", "type": "string"
        },
        "priority": {
          "default": 0, "description": "knet 在 'passive' 模式（默认）下使用时的链路优先级。值越小，优先级越高。仅对创建集群有效，添加节点时忽略。",
          "maximum": 255, "minimum": 0, "optional": 1, "type": "integer"
        }
      },
      "optional": 1, "type": "string", "typetext": "[address=]<IP> [,priority=<integer>]"
    },
    "nodeid": {"description": "此节点的节点 ID。", "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - N)"},
    "token-coefficient": {
      "default": 125, "description": "用于确定 Corosync 令牌超时时间的系数。详情请参阅 corosync.conf(5) 手册。", "minimum": 0, "optional": 1, "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "votes": {"description": "此节点的票数。", "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - N)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-config-0e41d22c-post-returns" id="api-cluster-config-0e41d22c-post-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config)。

## `/cluster/config/apiversion` <a href="#api-cluster-config-apiversion-11d00179" id="api-cluster-config-apiversion-11d00179"></a>

原始接口路径：`/cluster/config/apiversion`。

### GET `/cluster/config/apiversion` <a href="#api-cluster-config-apiversion-11d00179-get" id="api-cluster-config-apiversion-11d00179-get"></a>

返回此节点上可用的集群加入 API 版本。

**方法标识：** `join_api_version`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-config-apiversion-11d00179-get-parameters" id="api-cluster-config-apiversion-11d00179-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-config-apiversion-11d00179-get-returns" id="api-cluster-config-apiversion-11d00179-get-returns"></a>

```text
{"description": "集群加入 API 版本，目前为 1", "minimum": 0, "type": "integer"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/apiversion)。

## `/cluster/config/nodes` <a href="#api-cluster-config-nodes-20707639" id="api-cluster-config-nodes-20707639"></a>

原始接口路径：`/cluster/config/nodes`。

### GET `/cluster/config/nodes` <a href="#api-cluster-config-nodes-20707639-get" id="api-cluster-config-nodes-20707639-get"></a>

Corosync 节点列表。

**方法标识：** `nodes`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-config-nodes-20707639-get-parameters" id="api-cluster-config-nodes-20707639-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-config-nodes-20707639-get-returns" id="api-cluster-config-nodes-20707639-get-returns"></a>

```text
{"items": {"properties": {"node": {"type": "string"}}, "type": "object"}, "links": [{"href": "{node}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/nodes)。

## `/cluster/config/nodes/{node}` <a href="#api-cluster-config-nodes-node-637ac634" id="api-cluster-config-nodes-node-637ac634"></a>

原始接口路径：`/cluster/config/nodes/{node}`。

### DELETE `/cluster/config/nodes/{node}` <a href="#api-cluster-config-nodes-node-637ac634-delete" id="api-cluster-config-nodes-node-637ac634-delete"></a>

从集群配置中移除节点。

**方法标识：** `delnode`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-config-nodes-node-637ac634-delete-parameters" id="api-cluster-config-nodes-node-637ac634-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `node` | 类型：string；必填：是；默认值：—<br>集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"node": {"description": "集群节点名称。", "format": "pve-node", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-config-nodes-node-637ac634-delete-returns" id="api-cluster-config-nodes-node-637ac634-delete-returns"></a>

```text
{"type": "null"}
```

### POST `/cluster/config/nodes/{node}` <a href="#api-cluster-config-nodes-node-637ac634-post" id="api-cluster-config-nodes-node-637ac634-post"></a>

将节点添加到集群配置。此调用供内部使用。

**方法标识：** `addnode`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-config-nodes-node-637ac634-post-parameters" id="api-cluster-config-nodes-node-637ac634-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `apiversion` | 类型：integer；必填：否；默认值：—<br>新节点的 JOIN_API_VERSION。 |
| `force` | 类型：boolean；必填：否；默认值：—<br>如果节点已存在，则不抛出错误。 |
| `link[n]` | 类型：string；必填：否；默认值：—<br>单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7） |
| `new_node_ip` | 类型：string；必填：否；默认值：—<br>要添加节点的 IP 地址。未提供链路时用作回退值。 |
| `node` | 类型：string；必填：是；默认值：—<br>集群节点名称。 |
| `nodeid` | 类型：integer；必填：否；默认值：—<br>此节点的节点 ID。 |
| `votes` | 类型：integer；必填：否；默认值：—<br>此节点的票数 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "apiversion": {"description": "新节点的 JOIN_API_VERSION。", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "force": {"description": "如果节点已存在，则不抛出错误。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "link[n]": {
      "description": "单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7）",
      "format": {
        "address": {
          "default_key": 1, "description": "此 corosync 链路地址的主机名（或 IP）。", "format": "address", "format_description": "IP", "type": "string"
        },
        "priority": {
          "default": 0, "description": "knet 在 'passive' 模式（默认）下使用时的链路优先级。值越小，优先级越高。仅对创建集群有效，添加节点时忽略。",
          "maximum": 255, "minimum": 0, "optional": 1, "type": "integer"
        }
      },
      "optional": 1, "type": "string", "typetext": "[address=]<IP> [,priority=<integer>]"
    },
    "new_node_ip": {"description": "要添加节点的 IP 地址。未提供链路时用作回退值。", "format": "ip", "optional": 1, "type": "string", "typetext": "<string>"},
    "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string", "typetext": "<string>"},
    "nodeid": {"description": "此节点的节点 ID。", "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - N)"},
    "votes": {"description": "此节点的票数", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-config-nodes-node-637ac634-post-returns" id="api-cluster-config-nodes-node-637ac634-post-returns"></a>

```text
{
  "properties": {"corosync_authkey": {"type": "string"}, "corosync_conf": {"type": "string"}, "warnings": {"items": {"type": "string"}, "type": "array"}},
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/nodes/{node})。

## `/cluster/config/join` <a href="#api-cluster-config-join-75bce18b" id="api-cluster-config-join-75bce18b"></a>

原始接口路径：`/cluster/config/join`。

### GET `/cluster/config/join` <a href="#api-cluster-config-join-75bce18b-get" id="api-cluster-config-join-75bce18b-get"></a>

通过已连接的节点获取加入此集群所需的信息。

**方法标识：** `join_info`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-config-join-75bce18b-get-parameters" id="api-cluster-config-join-75bce18b-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `node` | 类型：string；必填：否；默认值："current connected node"<br>加入者要获取其 nodeinfo 的节点。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "default": "current connected node", "description": "加入者要获取其 nodeinfo 的节点。", "format": "pve-node", "optional": 1, "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-config-join-75bce18b-get-returns" id="api-cluster-config-join-75bce18b-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "config_digest": {"type": "string"},
    "nodelist": {
      "items": {
        "additionalProperties": 1,
        "properties": {
          "name": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "nodeid": {"description": "此节点的节点 ID。", "minimum": 1, "optional": 1, "type": "integer"}, "pve_addr": {"format": "ip", "type": "string"},
          "pve_fp": {"description": "证书 SHA 256 指纹。", "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
          "quorum_votes": {"minimum": 0, "type": "integer"},
          "ring0_addr": {
            "description": "单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7）",
            "format": {
              "address": {
                "default_key": 1, "description": "此 corosync 链路地址的主机名（或 IP）。", "format": "address", "format_description": "IP", "type": "string"
              },
              "priority": {
                "default": 0, "description": "knet 在 'passive' 模式（默认）下使用时的链路优先级。值越小，优先级越高。仅对创建集群有效，添加节点时忽略。",
                "maximum": 255, "minimum": 0, "optional": 1, "type": "integer"
              }
            },
            "optional": 1, "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "preferred_node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"}, "totem": {"type": "object"}
  },
  "type": "object"
}
```

### POST `/cluster/config/join` <a href="#api-cluster-config-join-75bce18b-post" id="api-cluster-config-join-75bce18b-post"></a>

将此节点加入现有集群。如果未提供链路，则默认在单条链路上使用由节点主机名解析得到的 IP（对于具有多条链路的集群，回退会失败）。

**方法标识：** `join`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-config-join-75bce18b-post-parameters" id="api-cluster-config-join-75bce18b-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `fingerprint` | 类型：string；必填：是；默认值：—<br>证书 SHA 256 指纹。 |
| `force` | 类型：boolean；必填：否；默认值：—<br>如果节点已存在，则不抛出错误。 |
| `hostname` | 类型：string；必填：是；默认值：—<br>现有集群成员的主机名（或 IP）。 |
| `link[n]` | 类型：string；必填：否；默认值：—<br>单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7） |
| `nodeid` | 类型：integer；必填：否；默认值：—<br>此节点的节点 ID。 |
| `password` | 类型：string；必填：是；默认值：—<br>对端节点的超级用户（root）密码。 |
| `votes` | 类型：integer；必填：否；默认值：—<br>此节点的票数 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {"description": "证书 SHA 256 指纹。", "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
    "force": {"description": "如果节点已存在，则不抛出错误。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "hostname": {"description": "现有集群成员的主机名（或 IP）。", "type": "string", "typetext": "<string>"},
    "link[n]": {
      "description": "单个 corosync 链路的地址和优先级信息。（最多支持 8 条链路；link0..link7）",
      "format": {
        "address": {
          "default_key": 1, "description": "此 corosync 链路地址的主机名（或 IP）。", "format": "address", "format_description": "IP", "type": "string"
        },
        "priority": {
          "default": 0, "description": "knet 在 'passive' 模式（默认）下使用时的链路优先级。值越小，优先级越高。仅对创建集群有效，添加节点时忽略。",
          "maximum": 255, "minimum": 0, "optional": 1, "type": "integer"
        }
      },
      "optional": 1, "type": "string", "typetext": "[address=]<IP> [,priority=<integer>]"
    },
    "nodeid": {"description": "此节点的节点 ID。", "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - N)"},
    "password": {"description": "对端节点的超级用户（root）密码。", "maxLength": 128, "type": "string", "typetext": "<string>"},
    "votes": {"description": "此节点的票数", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-config-join-75bce18b-post-returns" id="api-cluster-config-join-75bce18b-post-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/join)。

## `/cluster/config/totem` <a href="#api-cluster-config-totem-4cf727f7" id="api-cluster-config-totem-4cf727f7"></a>

原始接口路径：`/cluster/config/totem`。

### GET `/cluster/config/totem` <a href="#api-cluster-config-totem-4cf727f7-get" id="api-cluster-config-totem-4cf727f7-get"></a>

获取 corosync totem 协议设置。

**方法标识：** `totem`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-config-totem-4cf727f7-get-parameters" id="api-cluster-config-totem-4cf727f7-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-config-totem-4cf727f7-get-returns" id="api-cluster-config-totem-4cf727f7-get-returns"></a>

```text
{"type": "object"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/totem)。

## `/cluster/config/qdevice` <a href="#api-cluster-config-qdevice-316ec3f3" id="api-cluster-config-qdevice-316ec3f3"></a>

原始接口路径：`/cluster/config/qdevice`。

### GET `/cluster/config/qdevice` <a href="#api-cluster-config-qdevice-316ec3f3-get" id="api-cluster-config-qdevice-316ec3f3-get"></a>

获取 QDevice 状态

**方法标识：** `status`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-config-qdevice-316ec3f3-get-parameters" id="api-cluster-config-qdevice-316ec3f3-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-config-qdevice-316ec3f3-get-returns" id="api-cluster-config-qdevice-316ec3f3-get-returns"></a>

```text
{"type": "object"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/config/qdevice)。

## `/cluster/firewall` <a href="#api-cluster-firewall-f1f6b12c" id="api-cluster-firewall-f1f6b12c"></a>

原始接口路径：`/cluster/firewall`。

### GET `/cluster/firewall` <a href="#api-cluster-firewall-f1f6b12c-get" id="api-cluster-firewall-f1f6b12c-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-f1f6b12c-get-parameters" id="api-cluster-firewall-f1f6b12c-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-f1f6b12c-get-returns" id="api-cluster-firewall-f1f6b12c-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall)。

## `/cluster/firewall/groups` <a href="#api-cluster-firewall-groups-033bedae" id="api-cluster-firewall-groups-033bedae"></a>

原始接口路径：`/cluster/firewall/groups`。

### GET `/cluster/firewall/groups` <a href="#api-cluster-firewall-groups-033bedae-get" id="api-cluster-firewall-groups-033bedae-get"></a>

列出安全组。

**方法标识：** `list_security_groups`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-groups-033bedae-get-parameters" id="api-cluster-firewall-groups-033bedae-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-groups-033bedae-get-returns" id="api-cluster-firewall-groups-033bedae-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "可选注释或描述。", "optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 0, "type": "string"},
      "group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{group}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/firewall/groups` <a href="#api-cluster-firewall-groups-033bedae-post" id="api-cluster-firewall-groups-033bedae-post"></a>

创建新安全组。

**方法标识：** `create_security_group`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-groups-033bedae-post-parameters" id="api-cluster-firewall-groups-033bedae-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |
| `rename` | 类型：string；必填：否；默认值：—<br>重命名/更新现有安全组。可以将 'rename' 设为与 'name' 相同的值，以更新现有组的 'comment'。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "rename": {
      "description": "重命名/更新现有安全组。可以将 'rename' 设为与 'name' 相同的值，以更新现有组的 'comment'。", "maxLength": 18, "minLength": 2,
      "optional": 1, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-033bedae-post-returns" id="api-cluster-firewall-groups-033bedae-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/groups)。

## `/cluster/firewall/groups/{group}` <a href="#api-cluster-firewall-groups-group-b1883633" id="api-cluster-firewall-groups-group-b1883633"></a>

原始接口路径：`/cluster/firewall/groups/{group}`。

### DELETE `/cluster/firewall/groups/{group}` <a href="#api-cluster-firewall-groups-group-b1883633-delete" id="api-cluster-firewall-groups-group-b1883633-delete"></a>

删除安全组。

**方法标识：** `delete_security_group`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-groups-group-b1883633-delete-parameters" id="api-cluster-firewall-groups-group-b1883633-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-group-b1883633-delete-returns" id="api-cluster-firewall-groups-group-b1883633-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/firewall/groups/{group}` <a href="#api-cluster-firewall-groups-group-b1883633-get" id="api-cluster-firewall-groups-group-b1883633-get"></a>

列出规则。

**方法标识：** `get_rules`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-groups-group-b1883633-get-parameters" id="api-cluster-firewall-groups-group-b1883633-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-group-b1883633-get-returns" id="api-cluster-firewall-groups-group-b1883633-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "action": {"description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称", "type": "string"},
      "comment": {"description": "描述性注释", "optional": 1, "type": "string"}, "dest": {"description": "限制数据包目标地址", "optional": 1, "type": "string"},
      "dport": {"description": "限制 TCP/UDP 目标端口", "optional": 1, "type": "string"},
      "enable": {"description": "用于启用/禁用规则的标志", "optional": 1, "type": "integer"},
      "icmp-type": {"description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效", "optional": 1, "type": "string"},
      "iface": {"description": "网络接口名称。虚拟机和容器必须使用网络配置键名", "optional": 1, "type": "string"},
      "ipversion": {"description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定", "optional": 1, "type": "integer"},
      "log": {
        "description": "防火墙规则的日志级别", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
        "type": "string"
      },
      "macro": {"description": "使用预定义的标准宏", "optional": 1, "type": "string"}, "pos": {"description": "规则在规则集中的位置", "type": "integer"},
      "proto": {"description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字", "optional": 1, "type": "string"},
      "source": {"description": "限制数据包源地址", "optional": 1, "type": "string"},
      "sport": {"description": "限制 TCP/UDP 源端口", "optional": 1, "type": "string"}, "type": {"description": "规则类型", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{pos}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/firewall/groups/{group}` <a href="#api-cluster-firewall-groups-group-b1883633-post" id="api-cluster-firewall-groups-group-b1883633-post"></a>

创建新规则。

**方法标识：** `create_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-groups-group-b1883633-post-parameters" id="api-cluster-firewall-groups-group-b1883633-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：是；默认值：—<br>规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述性注释。 |
| `dest` | 类型：string；必填：否；默认值：—<br>限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | 类型：integer；必填：否；默认值：—<br>用于启用/禁用规则的标志。 |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |
| `icmp-type` | 类型：string；必填：否；默认值：—<br>指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | 类型：string；必填：否；默认值：—<br>网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | 类型：string；必填：否；默认值：—<br>防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | 类型：string；必填：否；默认值：—<br>使用预定义的标准宏。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | 类型：string；必填：否；默认值：—<br>IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | 类型：string；必填：否；默认值：—<br>限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | 类型：string；必填：是；默认值：—<br>规则类型。；可选值：`in`, `out`, `forward`, `group` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。", "maxLength": 20, "minLength": 2, "optional": 0,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    },
    "comment": {"description": "描述性注释。", "format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "enable": {"description": "用于启用/禁用规则的标志。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。", "format": "pve-fw-icmp-type-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。", "format": "pve-iface", "maxLength": 20,
      "minLength": 2, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏。", "maxLength": 128, "optional": 1, "type": "string", "typetext": "<string>"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。", "format": "pve-fw-protocol-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "type": {"description": "规则类型。", "enum": ["in", "out", "forward", "group"], "optional": 0, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-group-b1883633-post-returns" id="api-cluster-firewall-groups-group-b1883633-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/groups/{group})。

## `/cluster/firewall/groups/{group}/{pos}` <a href="#api-cluster-firewall-groups-group-pos-f899a8db" id="api-cluster-firewall-groups-group-pos-f899a8db"></a>

原始接口路径：`/cluster/firewall/groups/{group}/{pos}`。

### DELETE `/cluster/firewall/groups/{group}/{pos}` <a href="#api-cluster-firewall-groups-group-pos-f899a8db-delete" id="api-cluster-firewall-groups-group-pos-f899a8db-delete"></a>

删除规则。

**方法标识：** `delete_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-groups-group-pos-f899a8db-delete-parameters" id="api-cluster-firewall-groups-group-pos-f899a8db-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-group-pos-f899a8db-delete-returns" id="api-cluster-firewall-groups-group-pos-f899a8db-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/firewall/groups/{group}/{pos}` <a href="#api-cluster-firewall-groups-group-pos-f899a8db-get" id="api-cluster-firewall-groups-group-pos-f899a8db-get"></a>

获取单条规则数据。

**方法标识：** `get_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-groups-group-pos-f899a8db-get-parameters" id="api-cluster-firewall-groups-group-pos-f899a8db-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-group-pos-f899a8db-get-returns" id="api-cluster-firewall-groups-group-pos-f899a8db-get-returns"></a>

```text
{
  "properties": {
    "action": {"description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称", "type": "string"},
    "comment": {"description": "描述性注释", "optional": 1, "type": "string"}, "dest": {"description": "限制数据包目标地址", "optional": 1, "type": "string"},
    "dport": {"description": "限制 TCP/UDP 目标端口", "optional": 1, "type": "string"},
    "enable": {"description": "用于启用/禁用规则的标志", "optional": 1, "type": "integer"},
    "icmp-type": {"description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效", "optional": 1, "type": "string"},
    "iface": {"description": "网络接口名称。虚拟机和容器必须使用网络配置键名", "optional": 1, "type": "string"},
    "ipversion": {"description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定", "optional": 1, "type": "integer"},
    "log": {
      "description": "防火墙规则的日志级别", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏", "optional": 1, "type": "string"}, "pos": {"description": "规则在规则集中的位置", "type": "integer"},
    "proto": {"description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字", "optional": 1, "type": "string"},
    "source": {"description": "限制数据包源地址", "optional": 1, "type": "string"},
    "sport": {"description": "限制 TCP/UDP 源端口", "optional": 1, "type": "string"}, "type": {"description": "规则类型", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/firewall/groups/{group}/{pos}` <a href="#api-cluster-firewall-groups-group-pos-f899a8db-put" id="api-cluster-firewall-groups-group-pos-f899a8db-put"></a>

修改规则数据。

**方法标识：** `update_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-groups-group-pos-f899a8db-put-parameters" id="api-cluster-firewall-groups-group-pos-f899a8db-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：否；默认值：—<br>规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述性注释。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `dest` | 类型：string；必填：否；默认值：—<br>限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | 类型：integer；必填：否；默认值：—<br>用于启用/禁用规则的标志。 |
| `group` | 类型：string；必填：是；默认值：—<br>安全组名称。 |
| `icmp-type` | 类型：string；必填：否；默认值：—<br>指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | 类型：string；必填：否；默认值：—<br>网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | 类型：string；必填：否；默认值：—<br>防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | 类型：string；必填：否；默认值：—<br>使用预定义的标准宏。 |
| `moveto` | 类型：integer；必填：否；默认值：—<br>将规则移至新位置 &lt;moveto&gt;。其他参数将被忽略。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | 类型：string；必填：否；默认值：—<br>IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | 类型：string；必填：否；默认值：—<br>限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | 类型：string；必填：否；默认值：—<br>规则类型。；可选值：`in`, `out`, `forward`, `group` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。", "maxLength": 20, "minLength": 2, "optional": 1,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    },
    "comment": {"description": "描述性注释。", "format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "enable": {"description": "用于启用/禁用规则的标志。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "group": {"description": "安全组名称。", "maxLength": 18, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。", "format": "pve-fw-icmp-type-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。", "format": "pve-iface", "maxLength": 20,
      "minLength": 2, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏。", "maxLength": 128, "optional": 1, "type": "string", "typetext": "<string>"},
    "moveto": {"description": "将规则移至新位置 <moveto>。其他参数将被忽略。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。", "format": "pve-fw-protocol-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "type": {"description": "规则类型。", "enum": ["in", "out", "forward", "group"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-groups-group-pos-f899a8db-put-returns" id="api-cluster-firewall-groups-group-pos-f899a8db-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/groups/{group}/{pos})。

## `/cluster/firewall/rules` <a href="#api-cluster-firewall-rules-959883a1" id="api-cluster-firewall-rules-959883a1"></a>

原始接口路径：`/cluster/firewall/rules`。

### GET `/cluster/firewall/rules` <a href="#api-cluster-firewall-rules-959883a1-get" id="api-cluster-firewall-rules-959883a1-get"></a>

列出规则。

**方法标识：** `get_rules`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-rules-959883a1-get-parameters" id="api-cluster-firewall-rules-959883a1-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-rules-959883a1-get-returns" id="api-cluster-firewall-rules-959883a1-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "action": {"description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称", "type": "string"},
      "comment": {"description": "描述性注释", "optional": 1, "type": "string"}, "dest": {"description": "限制数据包目标地址", "optional": 1, "type": "string"},
      "dport": {"description": "限制 TCP/UDP 目标端口", "optional": 1, "type": "string"},
      "enable": {"description": "用于启用/禁用规则的标志", "optional": 1, "type": "integer"},
      "icmp-type": {"description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效", "optional": 1, "type": "string"},
      "iface": {"description": "网络接口名称。虚拟机和容器必须使用网络配置键名", "optional": 1, "type": "string"},
      "ipversion": {"description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定", "optional": 1, "type": "integer"},
      "log": {
        "description": "防火墙规则的日志级别", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
        "type": "string"
      },
      "macro": {"description": "使用预定义的标准宏", "optional": 1, "type": "string"}, "pos": {"description": "规则在规则集中的位置", "type": "integer"},
      "proto": {"description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字", "optional": 1, "type": "string"},
      "source": {"description": "限制数据包源地址", "optional": 1, "type": "string"},
      "sport": {"description": "限制 TCP/UDP 源端口", "optional": 1, "type": "string"}, "type": {"description": "规则类型", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{pos}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/firewall/rules` <a href="#api-cluster-firewall-rules-959883a1-post" id="api-cluster-firewall-rules-959883a1-post"></a>

创建新规则。

**方法标识：** `create_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-rules-959883a1-post-parameters" id="api-cluster-firewall-rules-959883a1-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：是；默认值：—<br>规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述性注释。 |
| `dest` | 类型：string；必填：否；默认值：—<br>限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | 类型：integer；必填：否；默认值：—<br>用于启用/禁用规则的标志。 |
| `icmp-type` | 类型：string；必填：否；默认值：—<br>指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | 类型：string；必填：否；默认值：—<br>网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | 类型：string；必填：否；默认值：—<br>防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | 类型：string；必填：否；默认值：—<br>使用预定义的标准宏。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | 类型：string；必填：否；默认值：—<br>IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | 类型：string；必填：否；默认值：—<br>限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | 类型：string；必填：是；默认值：—<br>规则类型。；可选值：`in`, `out`, `forward`, `group` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。", "maxLength": 20, "minLength": 2, "optional": 0,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    },
    "comment": {"description": "描述性注释。", "format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "enable": {"description": "用于启用/禁用规则的标志。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。", "format": "pve-fw-icmp-type-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。", "format": "pve-iface", "maxLength": 20,
      "minLength": 2, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏。", "maxLength": 128, "optional": 1, "type": "string", "typetext": "<string>"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。", "format": "pve-fw-protocol-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "type": {"description": "规则类型。", "enum": ["in", "out", "forward", "group"], "optional": 0, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-rules-959883a1-post-returns" id="api-cluster-firewall-rules-959883a1-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/rules)。

## `/cluster/firewall/rules/{pos}` <a href="#api-cluster-firewall-rules-pos-c553646f" id="api-cluster-firewall-rules-pos-c553646f"></a>

原始接口路径：`/cluster/firewall/rules/{pos}`。

### DELETE `/cluster/firewall/rules/{pos}` <a href="#api-cluster-firewall-rules-pos-c553646f-delete" id="api-cluster-firewall-rules-pos-c553646f-delete"></a>

删除规则。

**方法标识：** `delete_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-rules-pos-c553646f-delete-parameters" id="api-cluster-firewall-rules-pos-c553646f-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-rules-pos-c553646f-delete-returns" id="api-cluster-firewall-rules-pos-c553646f-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/firewall/rules/{pos}` <a href="#api-cluster-firewall-rules-pos-c553646f-get" id="api-cluster-firewall-rules-pos-c553646f-get"></a>

获取单条规则数据。

**方法标识：** `get_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-rules-pos-c553646f-get-parameters" id="api-cluster-firewall-rules-pos-c553646f-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-rules-pos-c553646f-get-returns" id="api-cluster-firewall-rules-pos-c553646f-get-returns"></a>

```text
{
  "properties": {
    "action": {"description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称", "type": "string"},
    "comment": {"description": "描述性注释", "optional": 1, "type": "string"}, "dest": {"description": "限制数据包目标地址", "optional": 1, "type": "string"},
    "dport": {"description": "限制 TCP/UDP 目标端口", "optional": 1, "type": "string"},
    "enable": {"description": "用于启用/禁用规则的标志", "optional": 1, "type": "integer"},
    "icmp-type": {"description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效", "optional": 1, "type": "string"},
    "iface": {"description": "网络接口名称。虚拟机和容器必须使用网络配置键名", "optional": 1, "type": "string"},
    "ipversion": {"description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定", "optional": 1, "type": "integer"},
    "log": {
      "description": "防火墙规则的日志级别", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏", "optional": 1, "type": "string"}, "pos": {"description": "规则在规则集中的位置", "type": "integer"},
    "proto": {"description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字", "optional": 1, "type": "string"},
    "source": {"description": "限制数据包源地址", "optional": 1, "type": "string"},
    "sport": {"description": "限制 TCP/UDP 源端口", "optional": 1, "type": "string"}, "type": {"description": "规则类型", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/firewall/rules/{pos}` <a href="#api-cluster-firewall-rules-pos-c553646f-put" id="api-cluster-firewall-rules-pos-c553646f-put"></a>

修改规则数据。

**方法标识：** `update_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-firewall-rules-pos-c553646f-put-parameters" id="api-cluster-firewall-rules-pos-c553646f-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：否；默认值：—<br>规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述性注释。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `dest` | 类型：string；必填：否；默认值：—<br>限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | 类型：integer；必填：否；默认值：—<br>用于启用/禁用规则的标志。 |
| `icmp-type` | 类型：string；必填：否；默认值：—<br>指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | 类型：string；必填：否；默认值：—<br>网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | 类型：string；必填：否；默认值：—<br>防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | 类型：string；必填：否；默认值：—<br>使用预定义的标准宏。 |
| `moveto` | 类型：integer；必填：否；默认值：—<br>将规则移至新位置 &lt;moveto&gt;。其他参数将被忽略。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | 类型：string；必填：否；默认值：—<br>IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | 类型：string；必填：否；默认值：—<br>限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | 类型：string；必填：否；默认值：—<br>规则类型。；可选值：`in`, `out`, `forward`, `group` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。", "maxLength": 20, "minLength": 2, "optional": 1,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    },
    "comment": {"description": "描述性注释。", "format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "enable": {"description": "用于启用/禁用规则的标志。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。", "format": "pve-fw-icmp-type-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。", "format": "pve-iface", "maxLength": 20,
      "minLength": 2, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏。", "maxLength": 128, "optional": 1, "type": "string", "typetext": "<string>"},
    "moveto": {"description": "将规则移至新位置 <moveto>。其他参数将被忽略。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。", "format": "pve-fw-protocol-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "type": {"description": "规则类型。", "enum": ["in", "out", "forward", "group"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-rules-pos-c553646f-put-returns" id="api-cluster-firewall-rules-pos-c553646f-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/rules/{pos})。

## `/cluster/firewall/ipset` <a href="#api-cluster-firewall-ipset-e989b25a" id="api-cluster-firewall-ipset-e989b25a"></a>

原始接口路径：`/cluster/firewall/ipset`。

### GET `/cluster/firewall/ipset` <a href="#api-cluster-firewall-ipset-e989b25a-get" id="api-cluster-firewall-ipset-e989b25a-get"></a>

列出 IPSet

**方法标识：** `ipset_index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-e989b25a-get-parameters" id="api-cluster-firewall-ipset-e989b25a-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-ipset-e989b25a-get-returns" id="api-cluster-firewall-ipset-e989b25a-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 0, "type": "string"},
      "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/firewall/ipset` <a href="#api-cluster-firewall-ipset-e989b25a-post" id="api-cluster-firewall-ipset-e989b25a-post"></a>

创建新 IPSet

**方法标识：** `create_ipset`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-e989b25a-post-parameters" id="api-cluster-firewall-ipset-e989b25a-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |
| `rename` | 类型：string；必填：否；默认值：—<br>重命名现有 IPSet。可以将 'rename' 设为与 'name' 相同的值，以更新现有 IPSet 的 'comment'。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "rename": {
      "description": "重命名现有 IPSet。可以将 'rename' 设为与 'name' 相同的值，以更新现有 IPSet 的 'comment'。", "maxLength": 64, "minLength": 2,
      "optional": 1, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-e989b25a-post-returns" id="api-cluster-firewall-ipset-e989b25a-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/ipset)。

## `/cluster/firewall/ipset/{name}` <a href="#api-cluster-firewall-ipset-name-0423135e" id="api-cluster-firewall-ipset-name-0423135e"></a>

原始接口路径：`/cluster/firewall/ipset/{name}`。

### DELETE `/cluster/firewall/ipset/{name}` <a href="#api-cluster-firewall-ipset-name-0423135e-delete" id="api-cluster-firewall-ipset-name-0423135e-delete"></a>

删除 IPSet

**方法标识：** `delete_ipset`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-name-0423135e-delete-parameters" id="api-cluster-firewall-ipset-name-0423135e-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `force` | 类型：boolean；必填：否；默认值：—<br>删除 IPSet 中的所有成员（如有）。 |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "force": {"description": "删除 IPSet 中的所有成员（如有）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-name-0423135e-delete-returns" id="api-cluster-firewall-ipset-name-0423135e-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/firewall/ipset/{name}` <a href="#api-cluster-firewall-ipset-name-0423135e-get" id="api-cluster-firewall-ipset-name-0423135e-get"></a>

列出 IPSet 内容

**方法标识：** `get_ipset`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-name-0423135e-get-parameters" id="api-cluster-firewall-ipset-name-0423135e-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-name-0423135e-get-returns" id="api-cluster-firewall-ipset-name-0423135e-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "cidr": {"type": "string"}, "comment": {"optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 0, "type": "string"},
      "nomatch": {"optional": 1, "type": "boolean"}
    },
    "type": "object"
  },
  "links": [{"href": "{cidr}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/firewall/ipset/{name}` <a href="#api-cluster-firewall-ipset-name-0423135e-post" id="api-cluster-firewall-ipset-name-0423135e-post"></a>

将 IP 或网络添加到 IPSet。

**方法标识：** `create_ip`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-name-0423135e-post-parameters" id="api-cluster-firewall-ipset-name-0423135e-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cidr` | 类型：string；必填：是；默认值：—<br>CIDR 格式的网络/IP 规范。 |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |
| `nomatch` | 类型：boolean；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {"description": "CIDR 格式的网络/IP 规范。", "format": "IPorCIDRorAlias", "type": "string", "typetext": "<string>"},
    "comment": {"format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "nomatch": {"optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-name-0423135e-post-returns" id="api-cluster-firewall-ipset-name-0423135e-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/ipset/{name})。

## `/cluster/firewall/ipset/{name}/{cidr}` <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b" id="api-cluster-firewall-ipset-name-cidr-c8e4021b"></a>

原始接口路径：`/cluster/firewall/ipset/{name}/{cidr}`。

### DELETE `/cluster/firewall/ipset/{name}/{cidr}` <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-delete" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-delete"></a>

从 IPSet 中移除 IP 或网络。

**方法标识：** `remove_ip`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-delete-parameters" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cidr` | 类型：string；必填：是；默认值：—<br>CIDR 格式的网络/IP 规范。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {"description": "CIDR 格式的网络/IP 规范。", "format": "IPorCIDRorAlias", "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-delete-returns" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/firewall/ipset/{name}/{cidr}` <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-get" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-get"></a>

从 IPSet 读取 IP 或网络设置。

**方法标识：** `read_ip`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-get-parameters" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cidr` | 类型：string；必填：是；默认值：—<br>CIDR 格式的网络/IP 规范。 |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {"description": "CIDR 格式的网络/IP 规范。", "format": "IPorCIDRorAlias", "type": "string", "typetext": "<string>"},
    "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-get-returns" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/firewall/ipset/{name}/{cidr}` <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-put" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-put"></a>

更新 IP 或网络设置

**方法标识：** `update_ip`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-put-parameters" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cidr` | 类型：string；必填：是；默认值：—<br>CIDR 格式的网络/IP 规范。 |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `name` | 类型：string；必填：是；默认值：—<br>IP 集合名称。 |
| `nomatch` | 类型：boolean；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {"description": "CIDR 格式的网络/IP 规范。", "format": "IPorCIDRorAlias", "type": "string", "typetext": "<string>"},
    "comment": {"format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "name": {"description": "IP 集合名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "nomatch": {"optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-ipset-name-cidr-c8e4021b-put-returns" id="api-cluster-firewall-ipset-name-cidr-c8e4021b-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/ipset/{name}/{cidr})。

## `/cluster/firewall/aliases` <a href="#api-cluster-firewall-aliases-8ded026b" id="api-cluster-firewall-aliases-8ded026b"></a>

原始接口路径：`/cluster/firewall/aliases`。

### GET `/cluster/firewall/aliases` <a href="#api-cluster-firewall-aliases-8ded026b-get" id="api-cluster-firewall-aliases-8ded026b-get"></a>

列出别名

**方法标识：** `get_aliases`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-aliases-8ded026b-get-parameters" id="api-cluster-firewall-aliases-8ded026b-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-aliases-8ded026b-get-returns" id="api-cluster-firewall-aliases-8ded026b-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "cidr": {"type": "string"}, "comment": {"optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 0, "type": "string"},
      "name": {"type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/firewall/aliases` <a href="#api-cluster-firewall-aliases-8ded026b-post" id="api-cluster-firewall-aliases-8ded026b-post"></a>

创建 IP 或网络别名。

**方法标识：** `create_alias`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-aliases-8ded026b-post-parameters" id="api-cluster-firewall-aliases-8ded026b-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cidr` | 类型：string；必填：是；默认值：—<br>CIDR 格式的网络/IP 规范。 |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `name` | 类型：string；必填：是；默认值：—<br>别名名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {"description": "CIDR 格式的网络/IP 规范。", "format": "IPorCIDR", "type": "string", "typetext": "<string>"},
    "comment": {"format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "name": {"description": "别名名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-aliases-8ded026b-post-returns" id="api-cluster-firewall-aliases-8ded026b-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/aliases)。

## `/cluster/firewall/aliases/{name}` <a href="#api-cluster-firewall-aliases-name-bd4edefe" id="api-cluster-firewall-aliases-name-bd4edefe"></a>

原始接口路径：`/cluster/firewall/aliases/{name}`。

### DELETE `/cluster/firewall/aliases/{name}` <a href="#api-cluster-firewall-aliases-name-bd4edefe-delete" id="api-cluster-firewall-aliases-name-bd4edefe-delete"></a>

移除 IP 或网络别名。

**方法标识：** `remove_alias`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-aliases-name-bd4edefe-delete-parameters" id="api-cluster-firewall-aliases-name-bd4edefe-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `name` | 类型：string；必填：是；默认值：—<br>别名名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "name": {"description": "别名名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-aliases-name-bd4edefe-delete-returns" id="api-cluster-firewall-aliases-name-bd4edefe-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/firewall/aliases/{name}` <a href="#api-cluster-firewall-aliases-name-bd4edefe-get" id="api-cluster-firewall-aliases-name-bd4edefe-get"></a>

读取别名。

**方法标识：** `read_alias`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-aliases-name-bd4edefe-get-parameters" id="api-cluster-firewall-aliases-name-bd4edefe-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：是；默认值：—<br>别名名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"name": {"description": "别名名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-aliases-name-bd4edefe-get-returns" id="api-cluster-firewall-aliases-name-bd4edefe-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/firewall/aliases/{name}` <a href="#api-cluster-firewall-aliases-name-bd4edefe-put" id="api-cluster-firewall-aliases-name-bd4edefe-put"></a>

更新 IP 或网络别名。

**方法标识：** `update_alias`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-aliases-name-bd4edefe-put-parameters" id="api-cluster-firewall-aliases-name-bd4edefe-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `cidr` | 类型：string；必填：是；默认值：—<br>CIDR 格式的网络/IP 规范。 |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `name` | 类型：string；必填：是；默认值：—<br>别名名称。 |
| `rename` | 类型：string；必填：否；默认值：—<br>重命名现有别名。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {"description": "CIDR 格式的网络/IP 规范。", "format": "IPorCIDR", "type": "string", "typetext": "<string>"},
    "comment": {"format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "name": {"description": "别名名称。", "maxLength": 64, "minLength": 2, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"},
    "rename": {"description": "重命名现有别名。", "maxLength": 64, "minLength": 2, "optional": 1, "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-aliases-name-bd4edefe-put-returns" id="api-cluster-firewall-aliases-name-bd4edefe-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/aliases/{name})。

## `/cluster/firewall/options` <a href="#api-cluster-firewall-options-ba499b8b" id="api-cluster-firewall-options-ba499b8b"></a>

原始接口路径：`/cluster/firewall/options`。

### GET `/cluster/firewall/options` <a href="#api-cluster-firewall-options-ba499b8b-get" id="api-cluster-firewall-options-ba499b8b-get"></a>

获取防火墙选项。

**方法标识：** `get_options`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-options-ba499b8b-get-parameters" id="api-cluster-firewall-options-ba499b8b-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-options-ba499b8b-get-returns" id="api-cluster-firewall-options-ba499b8b-get-returns"></a>

```text
{
  "properties": {
    "ebtables": {"default": 1, "description": "在整个集群中启用 ebtables 规则。", "optional": 1, "type": "boolean"},
    "enable": {"default": 0, "description": "在整个集群中启用或禁用防火墙。", "minimum": 0, "optional": 1, "type": "integer"},
    "log_ratelimit": {
      "description": "日志速率限制设置",
      "format": {
        "burst": {"default": 5, "description": "应用速率限制前始终记录日志的初始突发数据包数量", "minimum": 0, "optional": 1, "type": "integer"},
        "enable": {"default": "1", "default_key": 1, "description": "启用或禁用日志速率限制", "type": "boolean"},
        "rate": {
          "default": "1/second", "description": "补充突发令牌桶的频率", "format_description": "rate", "optional": 1,
          "pattern": "[1-9][0-9]*\\/(second|minute|hour|day)", "type": "string"
        }
      },
      "optional": 1, "type": "string"
    },
    "policy_forward": {"description": "转发策略。", "enum": ["ACCEPT", "DROP"], "optional": 1, "type": "string"},
    "policy_in": {"description": "输入策略。", "enum": ["ACCEPT", "REJECT", "DROP"], "optional": 1, "type": "string"},
    "policy_out": {"description": "输出策略。", "enum": ["ACCEPT", "REJECT", "DROP"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/firewall/options` <a href="#api-cluster-firewall-options-ba499b8b-put" id="api-cluster-firewall-options-ba499b8b-put"></a>

设置防火墙选项。

**方法标识：** `set_options`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-firewall-options-ba499b8b-put-parameters" id="api-cluster-firewall-options-ba499b8b-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `ebtables` | 类型：boolean；必填：否；默认值：1<br>在整个集群中启用 ebtables 规则。 |
| `enable` | 类型：integer；必填：否；默认值：0<br>在整个集群中启用或禁用防火墙。 |
| `log_ratelimit` | 类型：string；必填：否；默认值：—<br>日志速率限制设置 |
| `policy_forward` | 类型：string；必填：否；默认值：—<br>转发策略。；可选值：`ACCEPT`, `DROP` |
| `policy_in` | 类型：string；必填：否；默认值：—<br>输入策略。；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `policy_out` | 类型：string；必填：否；默认值：—<br>输出策略。；可选值：`ACCEPT`, `REJECT`, `DROP` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "ebtables": {"default": 1, "description": "在整个集群中启用 ebtables 规则。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "enable": {"default": 0, "description": "在整个集群中启用或禁用防火墙。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "log_ratelimit": {
      "description": "日志速率限制设置",
      "format": {
        "burst": {"default": 5, "description": "应用速率限制前始终记录日志的初始突发数据包数量", "minimum": 0, "optional": 1, "type": "integer"},
        "enable": {"default": "1", "default_key": 1, "description": "启用或禁用日志速率限制", "type": "boolean"},
        "rate": {
          "default": "1/second", "description": "补充突发令牌桶的频率", "format_description": "rate", "optional": 1,
          "pattern": "[1-9][0-9]*\\/(second|minute|hour|day)", "type": "string"
        }
      },
      "optional": 1, "type": "string", "typetext": "[enable=]<1|0> [,burst=<integer>] [,rate=<rate>]"
    },
    "policy_forward": {"description": "转发策略。", "enum": ["ACCEPT", "DROP"], "optional": 1, "type": "string"},
    "policy_in": {"description": "输入策略。", "enum": ["ACCEPT", "REJECT", "DROP"], "optional": 1, "type": "string"},
    "policy_out": {"description": "输出策略。", "enum": ["ACCEPT", "REJECT", "DROP"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-options-ba499b8b-put-returns" id="api-cluster-firewall-options-ba499b8b-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/options)。

## `/cluster/firewall/macros` <a href="#api-cluster-firewall-macros-588dda87" id="api-cluster-firewall-macros-588dda87"></a>

原始接口路径：`/cluster/firewall/macros`。

### GET `/cluster/firewall/macros` <a href="#api-cluster-firewall-macros-588dda87-get" id="api-cluster-firewall-macros-588dda87-get"></a>

列出可用宏

**方法标识：** `get_macros`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-macros-588dda87-get-parameters" id="api-cluster-firewall-macros-588dda87-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-firewall-macros-588dda87-get-returns" id="api-cluster-firewall-macros-588dda87-get-returns"></a>

```text
{
  "items": {
    "properties": {"descr": {"description": "更详细的描述（如有）。", "type": "string"}, "macro": {"description": "宏名称。", "type": "string"}},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/macros)。

## `/cluster/firewall/refs` <a href="#api-cluster-firewall-refs-4c8d1da9" id="api-cluster-firewall-refs-4c8d1da9"></a>

原始接口路径：`/cluster/firewall/refs`。

### GET `/cluster/firewall/refs` <a href="#api-cluster-firewall-refs-4c8d1da9-get" id="api-cluster-firewall-refs-4c8d1da9-get"></a>

列出源地址/目标地址属性中允许使用的 IPSet/别名引用。

**方法标识：** `refs`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-firewall-refs-4c8d1da9-get-parameters" id="api-cluster-firewall-refs-4c8d1da9-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出指定类型的引用。；可选值：`alias`, `ipset` |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"type": {"description": "仅列出指定类型的引用。", "enum": ["alias", "ipset"], "optional": 1, "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-firewall-refs-4c8d1da9-get-returns" id="api-cluster-firewall-refs-4c8d1da9-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "可选注释或描述。", "optional": 1, "type": "string"}, "name": {"description": "别名或 ipset 的名称。", "type": "string"},
      "ref": {"description": "防火墙规则中使用的引用字符串。", "type": "string"}, "scope": {"description": "引用的作用域（例如 SDN）。", "type": "string"},
      "type": {"description": "引用类型（alias 或 ipset）。", "enum": ["alias", "ipset"], "type": "string"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/refs)。

## `/cluster/backup` <a href="#api-cluster-backup-904ad991" id="api-cluster-backup-904ad991"></a>

原始接口路径：`/cluster/backup`。

### GET `/cluster/backup` <a href="#api-cluster-backup-904ad991-get" id="api-cluster-backup-904ad991-get"></a>

列出 vzdump 备份计划。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-backup-904ad991-get-parameters" id="api-cluster-backup-904ad991-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-backup-904ad991-get-returns" id="api-cluster-backup-904ad991-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "all": {"default": 0, "description": "备份此宿主机上所有已知的客户机系统。", "optional": 1, "type": "boolean"},
      "bwlimit": {"default": 0, "description": "限制 I/O 带宽（单位为 KiB/s）。", "minimum": 0, "optional": 1, "type": "integer"},
      "comment": {"description": "作业描述。", "maxLength": 512, "optional": 1, "type": "string"},
      "compress": {"default": "0", "description": "压缩转储文件。", "enum": ["0", "1", "gzip", "lzo", "zstd"], "optional": 1, "type": "string"},
      "dumpdir": {"description": "将生成的文件保存到指定目录。", "optional": 1, "type": "string"},
      "enabled": {"default": "1", "description": "启用或禁用此作业。", "optional": 1, "type": "boolean"},
      "exclude": {"description": "排除指定客户机系统（假定 --all）", "format": "pve-vmid-list", "optional": 1, "type": "string"},
      "exclude-path": {
        "description": "排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。",
        "items": {"type": "string"}, "optional": 1, "type": "array"
      },
      "fleecing": {
        "description": "备份 fleecing 选项（仅适用于虚拟机）。", "optional": 1,
        "properties": {
          "enabled": {
            "default": 0, "default_key": 1,
            "description": "启用备份 fleecing。客户机发生新写入时，将对应块的备份数据缓存在指定存储上，而非直接复制到备份目标。这有助于提高客户机 IO 性能，甚至避免挂起，代价是需要更多存储空间。",
            "optional": 1, "type": "boolean"
          },
          "storage": {
            "description": "使用此存储保存 fleecing 镜像。为了高效利用空间，最好使用支持 discard 且支持精简置备或稀疏文件的本地存储。",
            "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string"
          }
        },
        "type": "object"
      },
      "id": {"description": "作业 ID。", "maxLength": 50, "pattern": "\\S+", "type": "string"},
      "ionice": {
        "default": 7,
        "description": "使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。",
        "maximum": 8, "minimum": 0, "optional": 1, "type": "integer"
      },
      "lockwait": {"default": 180, "description": "等待全局锁的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer"},
      "mailnotification": {
        "default": "always", "description": "已弃用：请改用通知目标/匹配器。指定何时发送通知邮件", "enum": ["always", "failure"], "optional": 1,
        "type": "string"
      },
      "mailto": {
        "description": "已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。", "format": "email-or-username-list", "optional": 1,
        "type": "string"
      },
      "mode": {"default": "snapshot", "description": "备份模式。", "enum": ["snapshot", "suspend", "stop"], "optional": 1, "type": "string"},
      "next-run": {"description": "此备份作业下次执行时间的 UNIX 时间戳", "optional": 1, "type": "integer"},
      "node": {"description": "仅在此节点上执行时运行。", "format": "pve-node", "optional": 1, "type": "string"},
      "notes-template": {
        "description": "用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\\n' 和 '\\\\'。",
        "maxLength": 1024, "optional": 1, "requires": "storage", "type": "string"
      },
      "notification-mode": {
        "default": "auto",
        "description": "确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。",
        "enum": ["auto", "legacy-sendmail", "notification-system"], "optional": 1, "type": "string"
      },
      "pbs-change-detection-mode": {
        "description": "用于检测文件更改并切换容器备份编码格式的 PBS 模式。", "enum": ["legacy", "data", "metadata"], "optional": 1, "type": "string"
      },
      "performance": {
        "description": "其他性能相关设置。", "optional": 1,
        "properties": {
          "max-workers": {
            "default": 16, "description": "适用于虚拟机。允许同时运行的 IO 工作线程数量上限。", "maximum": 256, "minimum": 1, "optional": 1, "type": "integer"
          },
          "pbs-entries-max": {
            "default": 1048576,
            "description": "适用于发送到 PBS 的容器备份。限制任意时刻内存中允许的条目数量，以避免意外的 OOM 情况。增大此值可备份包含大量文件的容器。",
            "minimum": 1, "optional": 1, "type": "integer"
          }
        },
        "type": "object"
      },
      "pigz": {"default": 0, "description": "当 N>0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N>1 则将 N 用作线程数。", "optional": 1, "type": "integer"},
      "pool": {"description": "备份指定池中包含的所有已知客户机系统。", "optional": 1, "type": "string"},
      "protected": {"description": "如果为 true，则将备份标记为受保护。", "optional": 1, "requires": "storage", "type": "boolean"},
      "prune-backups": {
        "description": "使用这些保留选项，而非存储配置中的选项。", "optional": 1,
        "properties": {
          "keep-all": {"description": "保留所有备份。为 true 时与其他选项冲突。", "optional": 1, "type": "boolean"},
          "keep-daily": {
            "description": "保留最近 <N> 个不同日期的备份。如果同一天有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
            "type": "integer"
          },
          "keep-hourly": {
            "description": "保留最近 <N> 个不同小时的备份。如果同一小时有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0",
            "optional": 1, "type": "integer"
          },
          "keep-last": {"description": "保留最近 <N> 个备份。", "format_description": "N", "minimum": "0", "optional": 1, "type": "integer"},
          "keep-monthly": {
            "description": "保留最近 <N> 个不同月份的备份。如果同一个月有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0",
            "optional": 1, "type": "integer"
          },
          "keep-weekly": {
            "description": "保留最近 <N> 个不同周的备份。如果同一周有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
            "type": "integer"
          },
          "keep-yearly": {
            "description": "保留最近 <N> 个不同年份的备份。如果同一年有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
            "type": "integer"
          }
        },
        "type": "object"
      },
      "quiet": {"default": 0, "description": "静默运行。", "optional": 1, "type": "boolean"},
      "remove": {"default": 1, "description": "根据 'prune-backups' 清理旧备份。", "optional": 1, "type": "boolean"},
      "repeat-missed": {"default": 0, "description": "如果为 true，则在调度器未运行期间错过的作业将尽快补执行。", "optional": 1, "type": "boolean"},
      "schedule": {
        "description": "备份计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "optional": 1, "type": "string"
      },
      "script": {"description": "使用指定的钩子脚本。", "optional": 1, "type": "string"},
      "stdexcludes": {"default": 1, "description": "排除临时文件和日志。", "optional": 1, "type": "boolean"},
      "stop": {"default": 0, "description": "停止此宿主机上正在运行的备份作业。", "optional": 1, "type": "boolean"},
      "stopwait": {"default": 10, "description": "等待客户机系统停止的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer"},
      "storage": {"description": "将生成的文件保存到此存储。", "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string"},
      "tmpdir": {"description": "将临时文件保存到指定目录。", "optional": 1, "type": "string"},
      "vmid": {"description": "要备份的客户机系统 ID。", "format": "pve-vmid-list", "optional": 1, "type": "string"},
      "zstd": {"default": 1, "description": "Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。", "optional": 1, "type": "integer"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/backup` <a href="#api-cluster-backup-904ad991-post" id="api-cluster-backup-904ad991-post"></a>

创建新的 vzdump 备份作业。

**方法标识：** `create_job`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]], "description": "'tmpdir'、'dumpdir' 和 'script' 参数另外限制为仅 'root@pam' 用户可用。"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-backup-904ad991-post-parameters" id="api-cluster-backup-904ad991-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `all` | 类型：boolean；必填：否；默认值：0<br>备份此宿主机上所有已知的客户机系统。 |
| `bwlimit` | 类型：integer；必填：否；默认值：0<br>限制 I/O 带宽（单位为 KiB/s）。 |
| `comment` | 类型：string；必填：否；默认值：—<br>作业描述。 |
| `compress` | 类型：string；必填：否；默认值："0"<br>压缩转储文件。；可选值：`0`, `1`, `gzip`, `lzo`, `zstd` |
| `dow` | 类型：string；必填：否；默认值："mon,tue,wed,thu,fri,sat,sun"<br>已弃用：请改用 'schedule'。选择星期几。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。 |
| `dumpdir` | 类型：string；必填：否；默认值：—<br>将生成的文件保存到指定目录。 |
| `enabled` | 类型：boolean；必填：否；默认值："1"<br>启用或禁用此作业。 |
| `exclude` | 类型：string；必填：否；默认值：—<br>排除指定客户机系统（假定 --all） |
| `exclude-path` | 类型：array；必填：否；默认值：—<br>排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。 |
| `fleecing` | 类型：string；必填：否；默认值：—<br>备份 fleecing 选项（仅适用于虚拟机）。 |
| `id` | 类型：string；必填：否；默认值：—<br>作业 ID（将自动生成）。 |
| `ionice` | 类型：integer；必填：否；默认值：7<br>使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。 |
| `lockwait` | 类型：integer；必填：否；默认值：180<br>等待全局锁的最长时间（分钟）。 |
| `mailnotification` | 类型：string；必填：否；默认值："always"<br>已弃用：请改用通知目标/匹配器。指定何时发送通知邮件；可选值：`always`, `failure` |
| `mailto` | 类型：string；必填：否；默认值：—<br>已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。 |
| `mode` | 类型：string；必填：否；默认值："snapshot"<br>备份模式。；可选值：`snapshot`, `suspend`, `stop` |
| `node` | 类型：string；必填：否；默认值：—<br>仅在此节点上执行时运行。 |
| `notes-template` | 类型：string；必填：否；默认值：—<br>用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\n' 和 '\\'。 |
| `notification-mode` | 类型：string；必填：否；默认值："auto"<br>确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。；可选值：`auto`, `legacy-sendmail`, `notification-system` |
| `pbs-change-detection-mode` | 类型：string；必填：否；默认值：—<br>用于检测文件更改并切换容器备份编码格式的 PBS 模式。；可选值：`legacy`, `data`, `metadata` |
| `performance` | 类型：string；必填：否；默认值：—<br>其他性能相关设置。 |
| `pigz` | 类型：integer；必填：否；默认值：0<br>当 N&gt;0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N&gt;1 则将 N 用作线程数。 |
| `pool` | 类型：string；必填：否；默认值：—<br>备份指定池中包含的所有已知客户机系统。 |
| `protected` | 类型：boolean；必填：否；默认值：—<br>如果为 true，则将备份标记为受保护。 |
| `prune-backups` | 类型：string；必填：否；默认值："keep-all=1"<br>使用这些保留选项，而非存储配置中的选项。 |
| `quiet` | 类型：boolean；必填：否；默认值：0<br>静默运行。 |
| `remove` | 类型：boolean；必填：否；默认值：1<br>根据 'prune-backups' 清理旧备份。 |
| `repeat-missed` | 类型：boolean；必填：否；默认值：0<br>如果为 true，则在调度器未运行期间错过的作业将尽快补执行。 |
| `schedule` | 类型：string；必填：否；默认值：—<br>备份计划。格式是 `systemd` 日历事件的子集。 |
| `script` | 类型：string；必填：否；默认值：—<br>使用指定的钩子脚本。 |
| `starttime` | 类型：string；必填：否；默认值：—<br>已弃用：请改用 'schedule'。作业开始时间。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。 |
| `stdexcludes` | 类型：boolean；必填：否；默认值：1<br>排除临时文件和日志。 |
| `stop` | 类型：boolean；必填：否；默认值：0<br>停止此宿主机上正在运行的备份作业。 |
| `stopwait` | 类型：integer；必填：否；默认值：10<br>等待客户机系统停止的最长时间（分钟）。 |
| `storage` | 类型：string；必填：否；默认值：—<br>将生成的文件保存到此存储。 |
| `tmpdir` | 类型：string；必填：否；默认值：—<br>将临时文件保存到指定目录。 |
| `vmid` | 类型：string；必填：否；默认值：—<br>要备份的客户机系统 ID。 |
| `zstd` | 类型：integer；必填：否；默认值：1<br>Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "all": {"default": 0, "description": "备份此宿主机上所有已知的客户机系统。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "bwlimit": {
      "default": 0, "description": "限制 I/O 带宽（单位为 KiB/s）。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "comment": {"description": "作业描述。", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"},
    "compress": {"default": "0", "description": "压缩转储文件。", "enum": ["0", "1", "gzip", "lzo", "zstd"], "optional": 1, "type": "string"},
    "dow": {
      "default": "mon,tue,wed,thu,fri,sat,sun", "description": "已弃用：请改用 'schedule'。选择星期几。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。",
      "format": "pve-day-of-week-list", "optional": 1, "requires": "starttime", "type": "string", "typetext": "<string>"
    },
    "dumpdir": {"description": "将生成的文件保存到指定目录。", "optional": 1, "type": "string", "typetext": "<string>"},
    "enabled": {"default": "1", "description": "启用或禁用此作业。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "exclude": {"description": "排除指定客户机系统（假定 --all）", "format": "pve-vmid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "exclude-path": {
      "description": "排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。", "items": {"type": "string"},
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "fleecing": {
      "description": "备份 fleecing 选项（仅适用于虚拟机）。", "format": "backup-fleecing", "optional": 1, "type": "string",
      "typetext": "[[enabled=]<1|0>] [,storage=<storage ID>]"
    },
    "id": {"description": "作业 ID（将自动生成）。", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"},
    "ionice": {
      "default": 7,
      "description": "使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。",
      "maximum": 8, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 8)"
    },
    "lockwait": {
      "default": 180, "description": "等待全局锁的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "mailnotification": {
      "default": "always", "description": "已弃用：请改用通知目标/匹配器。指定何时发送通知邮件", "enum": ["always", "failure"], "optional": 1, "type": "string"
    },
    "mailto": {
      "description": "已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。", "format": "email-or-username-list", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "mode": {"default": "snapshot", "description": "备份模式。", "enum": ["snapshot", "suspend", "stop"], "optional": 1, "type": "string"},
    "node": {"description": "仅在此节点上执行时运行。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "notes-template": {
      "description": "用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\\n' 和 '\\\\'。",
      "maxLength": 1024, "optional": 1, "requires": "storage", "type": "string", "typetext": "<string>"
    },
    "notification-mode": {
      "default": "auto",
      "description": "确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。",
      "enum": ["auto", "legacy-sendmail", "notification-system"], "optional": 1, "type": "string"
    },
    "pbs-change-detection-mode": {
      "description": "用于检测文件更改并切换容器备份编码格式的 PBS 模式。", "enum": ["legacy", "data", "metadata"], "optional": 1, "type": "string"
    },
    "performance": {
      "description": "其他性能相关设置。", "format": "backup-performance", "optional": 1, "type": "string",
      "typetext": "[max-workers=<integer>] [,pbs-entries-max=<integer>]"
    },
    "pigz": {
      "default": 0, "description": "当 N>0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N>1 则将 N 用作线程数。", "optional": 1, "type": "integer",
      "typetext": "<integer>"
    },
    "pool": {"description": "备份指定池中包含的所有已知客户机系统。", "optional": 1, "type": "string", "typetext": "<string>"},
    "protected": {"description": "如果为 true，则将备份标记为受保护。", "optional": 1, "requires": "storage", "type": "boolean", "typetext": "<boolean>"},
    "prune-backups": {
      "default": "keep-all=1", "description": "使用这些保留选项，而非存储配置中的选项。", "format": "prune-backups", "optional": 1, "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "quiet": {"default": 0, "description": "静默运行。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "remove": {"default": 1, "description": "根据 'prune-backups' 清理旧备份。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "repeat-missed": {
      "default": 0, "description": "如果为 true，则在调度器未运行期间错过的作业将尽快补执行。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "script": {"description": "使用指定的钩子脚本。", "optional": 1, "type": "string", "typetext": "<string>"},
    "starttime": {
      "description": "已弃用：请改用 'schedule'。作业开始时间。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。", "optional": 1,
      "pattern": "\\d{1,2}:\\d{1,2}", "type": "string", "typetext": "HH:MM"
    },
    "stdexcludes": {"default": 1, "description": "排除临时文件和日志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "stop": {"default": 0, "description": "停止此宿主机上正在运行的备份作业。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "stopwait": {
      "default": 10, "description": "等待客户机系统停止的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "storage": {
      "description": "将生成的文件保存到此存储。", "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string",
      "typetext": "<storage ID>"
    },
    "tmpdir": {"description": "将临时文件保存到指定目录。", "optional": 1, "type": "string", "typetext": "<string>"},
    "vmid": {"description": "要备份的客户机系统 ID。", "format": "pve-vmid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "zstd": {
      "default": 1, "description": "Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。", "optional": 1, "type": "integer",
      "typetext": "<integer>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-backup-904ad991-post-returns" id="api-cluster-backup-904ad991-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup)。

## `/cluster/backup/{id}` <a href="#api-cluster-backup-id-8eee5aec" id="api-cluster-backup-id-8eee5aec"></a>

原始接口路径：`/cluster/backup/{id}`。

### DELETE `/cluster/backup/{id}` <a href="#api-cluster-backup-id-8eee5aec-delete" id="api-cluster-backup-id-8eee5aec-delete"></a>

删除 vzdump 备份作业定义。

**方法标识：** `delete_job`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-backup-id-8eee5aec-delete-parameters" id="api-cluster-backup-id-8eee5aec-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>作业 ID。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"description": "作业 ID。", "maxLength": 50, "pattern": "\\S+", "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-backup-id-8eee5aec-delete-returns" id="api-cluster-backup-id-8eee5aec-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/backup/{id}` <a href="#api-cluster-backup-id-8eee5aec-get" id="api-cluster-backup-id-8eee5aec-get"></a>

读取 vzdump 备份作业定义。

**方法标识：** `read_job`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-backup-id-8eee5aec-get-parameters" id="api-cluster-backup-id-8eee5aec-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>作业 ID。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"description": "作业 ID。", "maxLength": 50, "pattern": "\\S+", "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-backup-id-8eee5aec-get-returns" id="api-cluster-backup-id-8eee5aec-get-returns"></a>

```text
{
  "properties": {
    "all": {"default": 0, "description": "备份此宿主机上所有已知的客户机系统。", "optional": 1, "type": "boolean"},
    "bwlimit": {"default": 0, "description": "限制 I/O 带宽（单位为 KiB/s）。", "minimum": 0, "optional": 1, "type": "integer"},
    "comment": {"description": "作业描述。", "maxLength": 512, "optional": 1, "type": "string"},
    "compress": {"default": "0", "description": "压缩转储文件。", "enum": ["0", "1", "gzip", "lzo", "zstd"], "optional": 1, "type": "string"},
    "dumpdir": {"description": "将生成的文件保存到指定目录。", "optional": 1, "type": "string"},
    "enabled": {"default": "1", "description": "启用或禁用此作业。", "optional": 1, "type": "boolean"},
    "exclude": {"description": "排除指定客户机系统（假定 --all）", "format": "pve-vmid-list", "optional": 1, "type": "string"},
    "exclude-path": {
      "description": "排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。", "items": {"type": "string"},
      "optional": 1, "type": "array"
    },
    "fleecing": {
      "description": "备份 fleecing 选项（仅适用于虚拟机）。", "optional": 1,
      "properties": {
        "enabled": {
          "default": 0, "default_key": 1,
          "description": "启用备份 fleecing。客户机发生新写入时，将对应块的备份数据缓存在指定存储上，而非直接复制到备份目标。这有助于提高客户机 IO 性能，甚至避免挂起，代价是需要更多存储空间。",
          "optional": 1, "type": "boolean"
        },
        "storage": {
          "description": "使用此存储保存 fleecing 镜像。为了高效利用空间，最好使用支持 discard 且支持精简置备或稀疏文件的本地存储。",
          "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string"
        }
      },
      "type": "object"
    },
    "id": {"description": "作业 ID。", "maxLength": 50, "pattern": "\\S+", "type": "string"},
    "ionice": {
      "default": 7,
      "description": "使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。",
      "maximum": 8, "minimum": 0, "optional": 1, "type": "integer"
    },
    "lockwait": {"default": 180, "description": "等待全局锁的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer"},
    "mailnotification": {
      "default": "always", "description": "已弃用：请改用通知目标/匹配器。指定何时发送通知邮件", "enum": ["always", "failure"], "optional": 1, "type": "string"
    },
    "mailto": {
      "description": "已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。", "format": "email-or-username-list", "optional": 1,
      "type": "string"
    },
    "mode": {"default": "snapshot", "description": "备份模式。", "enum": ["snapshot", "suspend", "stop"], "optional": 1, "type": "string"},
    "next-run": {"description": "此备份作业下次执行时间的 UNIX 时间戳", "optional": 1, "type": "integer"},
    "node": {"description": "仅在此节点上执行时运行。", "format": "pve-node", "optional": 1, "type": "string"},
    "notes-template": {
      "description": "用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\\n' 和 '\\\\'。",
      "maxLength": 1024, "optional": 1, "requires": "storage", "type": "string"
    },
    "notification-mode": {
      "default": "auto",
      "description": "确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。",
      "enum": ["auto", "legacy-sendmail", "notification-system"], "optional": 1, "type": "string"
    },
    "pbs-change-detection-mode": {
      "description": "用于检测文件更改并切换容器备份编码格式的 PBS 模式。", "enum": ["legacy", "data", "metadata"], "optional": 1, "type": "string"
    },
    "performance": {
      "description": "其他性能相关设置。", "optional": 1,
      "properties": {
        "max-workers": {
          "default": 16, "description": "适用于虚拟机。允许同时运行的 IO 工作线程数量上限。", "maximum": 256, "minimum": 1, "optional": 1, "type": "integer"
        },
        "pbs-entries-max": {
          "default": 1048576,
          "description": "适用于发送到 PBS 的容器备份。限制任意时刻内存中允许的条目数量，以避免意外的 OOM 情况。增大此值可备份包含大量文件的容器。",
          "minimum": 1, "optional": 1, "type": "integer"
        }
      },
      "type": "object"
    },
    "pigz": {"default": 0, "description": "当 N>0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N>1 则将 N 用作线程数。", "optional": 1, "type": "integer"},
    "pool": {"description": "备份指定池中包含的所有已知客户机系统。", "optional": 1, "type": "string"},
    "protected": {"description": "如果为 true，则将备份标记为受保护。", "optional": 1, "requires": "storage", "type": "boolean"},
    "prune-backups": {
      "description": "使用这些保留选项，而非存储配置中的选项。", "optional": 1,
      "properties": {
        "keep-all": {"description": "保留所有备份。为 true 时与其他选项冲突。", "optional": 1, "type": "boolean"},
        "keep-daily": {
          "description": "保留最近 <N> 个不同日期的备份。如果同一天有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
          "type": "integer"
        },
        "keep-hourly": {
          "description": "保留最近 <N> 个不同小时的备份。如果同一小时有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
          "type": "integer"
        },
        "keep-last": {"description": "保留最近 <N> 个备份。", "format_description": "N", "minimum": "0", "optional": 1, "type": "integer"},
        "keep-monthly": {
          "description": "保留最近 <N> 个不同月份的备份。如果同一个月有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
          "type": "integer"
        },
        "keep-weekly": {
          "description": "保留最近 <N> 个不同周的备份。如果同一周有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
          "type": "integer"
        },
        "keep-yearly": {
          "description": "保留最近 <N> 个不同年份的备份。如果同一年有多个备份，则仅保留最新备份。", "format_description": "N", "minimum": "0", "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "quiet": {"default": 0, "description": "静默运行。", "optional": 1, "type": "boolean"},
    "remove": {"default": 1, "description": "根据 'prune-backups' 清理旧备份。", "optional": 1, "type": "boolean"},
    "repeat-missed": {"default": 0, "description": "如果为 true，则在调度器未运行期间错过的作业将尽快补执行。", "optional": 1, "type": "boolean"},
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "optional": 1, "type": "string"
    },
    "script": {"description": "使用指定的钩子脚本。", "optional": 1, "type": "string"},
    "stdexcludes": {"default": 1, "description": "排除临时文件和日志。", "optional": 1, "type": "boolean"},
    "stop": {"default": 0, "description": "停止此宿主机上正在运行的备份作业。", "optional": 1, "type": "boolean"},
    "stopwait": {"default": 10, "description": "等待客户机系统停止的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer"},
    "storage": {"description": "将生成的文件保存到此存储。", "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string"},
    "tmpdir": {"description": "将临时文件保存到指定目录。", "optional": 1, "type": "string"},
    "vmid": {"description": "要备份的客户机系统 ID。", "format": "pve-vmid-list", "optional": 1, "type": "string"},
    "zstd": {"default": 1, "description": "Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。", "optional": 1, "type": "integer"}
  },
  "type": "object"
}
```

### PUT `/cluster/backup/{id}` <a href="#api-cluster-backup-id-8eee5aec-put" id="api-cluster-backup-id-8eee5aec-put"></a>

更新 vzdump 备份作业定义。

**方法标识：** `update_job`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]], "description": "'tmpdir'、'dumpdir' 和 'script' 参数另外限制为仅 'root@pam' 用户可用。"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-backup-id-8eee5aec-put-parameters" id="api-cluster-backup-id-8eee5aec-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `all` | 类型：boolean；必填：否；默认值：0<br>备份此宿主机上所有已知的客户机系统。 |
| `bwlimit` | 类型：integer；必填：否；默认值：0<br>限制 I/O 带宽（单位为 KiB/s）。 |
| `comment` | 类型：string；必填：否；默认值：—<br>作业描述。 |
| `compress` | 类型：string；必填：否；默认值："0"<br>压缩转储文件。；可选值：`0`, `1`, `gzip`, `lzo`, `zstd` |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `dow` | 类型：string；必填：否；默认值：—<br>已弃用：请改用 'schedule'。选择星期几。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。 |
| `dumpdir` | 类型：string；必填：否；默认值：—<br>将生成的文件保存到指定目录。 |
| `enabled` | 类型：boolean；必填：否；默认值："1"<br>启用或禁用此作业。 |
| `exclude` | 类型：string；必填：否；默认值：—<br>排除指定客户机系统（假定 --all） |
| `exclude-path` | 类型：array；必填：否；默认值：—<br>排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。 |
| `fleecing` | 类型：string；必填：否；默认值：—<br>备份 fleecing 选项（仅适用于虚拟机）。 |
| `id` | 类型：string；必填：是；默认值：—<br>作业 ID。 |
| `ionice` | 类型：integer；必填：否；默认值：7<br>使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。 |
| `lockwait` | 类型：integer；必填：否；默认值：180<br>等待全局锁的最长时间（分钟）。 |
| `mailnotification` | 类型：string；必填：否；默认值："always"<br>已弃用：请改用通知目标/匹配器。指定何时发送通知邮件；可选值：`always`, `failure` |
| `mailto` | 类型：string；必填：否；默认值：—<br>已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。 |
| `mode` | 类型：string；必填：否；默认值："snapshot"<br>备份模式。；可选值：`snapshot`, `suspend`, `stop` |
| `node` | 类型：string；必填：否；默认值：—<br>仅在此节点上执行时运行。 |
| `notes-template` | 类型：string；必填：否；默认值：—<br>用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\n' 和 '\\'。 |
| `notification-mode` | 类型：string；必填：否；默认值："auto"<br>确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。；可选值：`auto`, `legacy-sendmail`, `notification-system` |
| `pbs-change-detection-mode` | 类型：string；必填：否；默认值：—<br>用于检测文件更改并切换容器备份编码格式的 PBS 模式。；可选值：`legacy`, `data`, `metadata` |
| `performance` | 类型：string；必填：否；默认值：—<br>其他性能相关设置。 |
| `pigz` | 类型：integer；必填：否；默认值：0<br>当 N&gt;0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N&gt;1 则将 N 用作线程数。 |
| `pool` | 类型：string；必填：否；默认值：—<br>备份指定池中包含的所有已知客户机系统。 |
| `protected` | 类型：boolean；必填：否；默认值：—<br>如果为 true，则将备份标记为受保护。 |
| `prune-backups` | 类型：string；必填：否；默认值："keep-all=1"<br>使用这些保留选项，而非存储配置中的选项。 |
| `quiet` | 类型：boolean；必填：否；默认值：0<br>静默运行。 |
| `remove` | 类型：boolean；必填：否；默认值：1<br>根据 'prune-backups' 清理旧备份。 |
| `repeat-missed` | 类型：boolean；必填：否；默认值：0<br>如果为 true，则在调度器未运行期间错过的作业将尽快补执行。 |
| `schedule` | 类型：string；必填：否；默认值：—<br>备份计划。格式是 `systemd` 日历事件的子集。 |
| `script` | 类型：string；必填：否；默认值：—<br>使用指定的钩子脚本。 |
| `starttime` | 类型：string；必填：否；默认值：—<br>已弃用：请改用 'schedule'。作业开始时间。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。 |
| `stdexcludes` | 类型：boolean；必填：否；默认值：1<br>排除临时文件和日志。 |
| `stop` | 类型：boolean；必填：否；默认值：0<br>停止此宿主机上正在运行的备份作业。 |
| `stopwait` | 类型：integer；必填：否；默认值：10<br>等待客户机系统停止的最长时间（分钟）。 |
| `storage` | 类型：string；必填：否；默认值：—<br>将生成的文件保存到此存储。 |
| `tmpdir` | 类型：string；必填：否；默认值：—<br>将临时文件保存到指定目录。 |
| `vmid` | 类型：string；必填：否；默认值：—<br>要备份的客户机系统 ID。 |
| `zstd` | 类型：integer；必填：否；默认值：1<br>Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "all": {"default": 0, "description": "备份此宿主机上所有已知的客户机系统。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "bwlimit": {
      "default": 0, "description": "限制 I/O 带宽（单位为 KiB/s）。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "comment": {"description": "作业描述。", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"},
    "compress": {"default": "0", "description": "压缩转储文件。", "enum": ["0", "1", "gzip", "lzo", "zstd"], "optional": 1, "type": "string"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "dow": {
      "description": "已弃用：请改用 'schedule'。选择星期几。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。", "format": "pve-day-of-week-list",
      "optional": 1, "requires": "starttime", "type": "string", "typetext": "<string>"
    },
    "dumpdir": {"description": "将生成的文件保存到指定目录。", "optional": 1, "type": "string", "typetext": "<string>"},
    "enabled": {"default": "1", "description": "启用或禁用此作业。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "exclude": {"description": "排除指定客户机系统（假定 --all）", "format": "pve-vmid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "exclude-path": {
      "description": "排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。", "items": {"type": "string"},
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "fleecing": {
      "description": "备份 fleecing 选项（仅适用于虚拟机）。", "format": "backup-fleecing", "optional": 1, "type": "string",
      "typetext": "[[enabled=]<1|0>] [,storage=<storage ID>]"
    },
    "id": {"description": "作业 ID。", "maxLength": 50, "pattern": "\\S+", "type": "string"},
    "ionice": {
      "default": 7,
      "description": "使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。",
      "maximum": 8, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 8)"
    },
    "lockwait": {
      "default": 180, "description": "等待全局锁的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "mailnotification": {
      "default": "always", "description": "已弃用：请改用通知目标/匹配器。指定何时发送通知邮件", "enum": ["always", "failure"], "optional": 1, "type": "string"
    },
    "mailto": {
      "description": "已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。", "format": "email-or-username-list", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "mode": {"default": "snapshot", "description": "备份模式。", "enum": ["snapshot", "suspend", "stop"], "optional": 1, "type": "string"},
    "node": {"description": "仅在此节点上执行时运行。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "notes-template": {
      "description": "用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\\n' 和 '\\\\'。",
      "maxLength": 1024, "optional": 1, "requires": "storage", "type": "string", "typetext": "<string>"
    },
    "notification-mode": {
      "default": "auto",
      "description": "确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。",
      "enum": ["auto", "legacy-sendmail", "notification-system"], "optional": 1, "type": "string"
    },
    "pbs-change-detection-mode": {
      "description": "用于检测文件更改并切换容器备份编码格式的 PBS 模式。", "enum": ["legacy", "data", "metadata"], "optional": 1, "type": "string"
    },
    "performance": {
      "description": "其他性能相关设置。", "format": "backup-performance", "optional": 1, "type": "string",
      "typetext": "[max-workers=<integer>] [,pbs-entries-max=<integer>]"
    },
    "pigz": {
      "default": 0, "description": "当 N>0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N>1 则将 N 用作线程数。", "optional": 1, "type": "integer",
      "typetext": "<integer>"
    },
    "pool": {"description": "备份指定池中包含的所有已知客户机系统。", "optional": 1, "type": "string", "typetext": "<string>"},
    "protected": {"description": "如果为 true，则将备份标记为受保护。", "optional": 1, "requires": "storage", "type": "boolean", "typetext": "<boolean>"},
    "prune-backups": {
      "default": "keep-all=1", "description": "使用这些保留选项，而非存储配置中的选项。", "format": "prune-backups", "optional": 1, "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "quiet": {"default": 0, "description": "静默运行。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "remove": {"default": 1, "description": "根据 'prune-backups' 清理旧备份。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "repeat-missed": {
      "default": 0, "description": "如果为 true，则在调度器未运行期间错过的作业将尽快补执行。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "script": {"description": "使用指定的钩子脚本。", "optional": 1, "type": "string", "typetext": "<string>"},
    "starttime": {
      "description": "已弃用：请改用 'schedule'。作业开始时间。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。", "optional": 1,
      "pattern": "\\d{1,2}:\\d{1,2}", "type": "string", "typetext": "HH:MM"
    },
    "stdexcludes": {"default": 1, "description": "排除临时文件和日志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "stop": {"default": 0, "description": "停止此宿主机上正在运行的备份作业。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "stopwait": {
      "default": 10, "description": "等待客户机系统停止的最长时间（分钟）。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "storage": {
      "description": "将生成的文件保存到此存储。", "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string",
      "typetext": "<storage ID>"
    },
    "tmpdir": {"description": "将临时文件保存到指定目录。", "optional": 1, "type": "string", "typetext": "<string>"},
    "vmid": {"description": "要备份的客户机系统 ID。", "format": "pve-vmid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "zstd": {
      "default": 1, "description": "Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。", "optional": 1, "type": "integer",
      "typetext": "<integer>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-backup-id-8eee5aec-put-returns" id="api-cluster-backup-id-8eee5aec-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup/{id})。

## `/cluster/backup/{id}/included_volumes` <a href="#api-cluster-backup-id-included-volumes-5a3fa353" id="api-cluster-backup-id-included-volumes-5a3fa353"></a>

原始接口路径：`/cluster/backup/{id}/included_volumes`。

### GET `/cluster/backup/{id}/included_volumes` <a href="#api-cluster-backup-id-included-volumes-5a3fa353-get" id="api-cluster-backup-id-included-volumes-5a3fa353-get"></a>

返回包含的客户机及其磁盘的备份状态。已针对 ExtJS 树视图进行优化。

**方法标识：** `get_volume_backup_included`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-backup-id-included-volumes-5a3fa353-get-parameters" id="api-cluster-backup-id-included-volumes-5a3fa353-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>作业 ID。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"description": "作业 ID。", "maxLength": 50, "pattern": "\\S+", "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-backup-id-included-volumes-5a3fa353-get-returns" id="api-cluster-backup-id-included-volumes-5a3fa353-get-returns"></a>

```text
{
  "description": "树对象的根节点。子节点表示客户机，孙节点表示该客户机的卷。",
  "properties": {
    "children": {
      "items": {
        "properties": {
          "children": {
            "description": "客户机的卷及其是否包含在备份中的信息。",
            "items": {
              "properties": {
                "id": {"description": "卷的配置键。", "type": "string"}, "included": {"description": "卷是否包含在备份中。", "type": "boolean"},
                "name": {"description": "卷名称。", "type": "string"}, "reason": {"description": "包含（或排除）该卷的原因。", "type": "string"}
              },
              "type": "object"
            },
            "optional": 1, "type": "array"
          },
          "id": {"description": "客户机的 VMID。", "type": "integer"}, "name": {"description": "客户机名称", "optional": 1, "type": "string"},
          "type": {"description": "客户机类型：VM、CT，或对于已移除但未清除的客户机为 unknown。", "enum": ["qemu", "lxc", "unknown"], "type": "string"}
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup/{id}/included_volumes)。

## `/cluster/backup-info` <a href="#api-cluster-backup-info-1b57f5f1" id="api-cluster-backup-info-1b57f5f1"></a>

原始接口路径：`/cluster/backup-info`。

### GET `/cluster/backup-info` <a href="#api-cluster-backup-info-1b57f5f1-get" id="api-cluster-backup-info-1b57f5f1-get"></a>

备份信息相关端点的索引

**方法标识：** `index`

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-backup-info-1b57f5f1-get-parameters" id="api-cluster-backup-info-1b57f5f1-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-backup-info-1b57f5f1-get-returns" id="api-cluster-backup-info-1b57f5f1-get-returns"></a>

```text
{
  "description": "目录索引。", "items": {"properties": {"subdir": {"description": "API 子目录端点", "type": "string"}}, "type": "object"},
  "links": [{"href": "{subdir}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup-info)。

## `/cluster/backup-info/not-backed-up` <a href="#api-cluster-backup-info-not-backed-up-24dcc746" id="api-cluster-backup-info-not-backed-up-24dcc746"></a>

原始接口路径：`/cluster/backup-info/not-backed-up`。

### GET `/cluster/backup-info/not-backed-up` <a href="#api-cluster-backup-info-not-backed-up-24dcc746-get" id="api-cluster-backup-info-not-backed-up-24dcc746-get"></a>

显示未被任何备份作业覆盖的所有客户机。

**方法标识：** `get_guests_not_in_backup`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-backup-info-not-backed-up-24dcc746-get-parameters" id="api-cluster-backup-info-not-backed-up-24dcc746-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-backup-info-not-backed-up-24dcc746-get-returns" id="api-cluster-backup-info-not-backed-up-24dcc746-get-returns"></a>

```text
{
  "description": "包含客户机对象。",
  "items": {
    "properties": {
      "name": {"description": "客户机名称", "optional": 1, "type": "string"},
      "type": {"description": "客户机类型。", "enum": ["qemu", "lxc"], "type": "string"}, "vmid": {"description": "客户机的 VMID。", "type": "integer"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup-info/not-backed-up)。

## `/cluster/ha` <a href="#api-cluster-ha-5c97873a" id="api-cluster-ha-5c97873a"></a>

原始接口路径：`/cluster/ha`。

### GET `/cluster/ha` <a href="#api-cluster-ha-5c97873a-get" id="api-cluster-ha-5c97873a-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-5c97873a-get-parameters" id="api-cluster-ha-5c97873a-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-5c97873a-get-returns" id="api-cluster-ha-5c97873a-get-returns"></a>

```text
{"items": {"properties": {"id": {"type": "string"}}, "type": "object"}, "links": [{"href": "{id}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha)。

## `/cluster/ha/resources` <a href="#api-cluster-ha-resources-88692530" id="api-cluster-ha-resources-88692530"></a>

原始接口路径：`/cluster/ha/resources`。

### GET `/cluster/ha/resources` <a href="#api-cluster-ha-resources-88692530-get" id="api-cluster-ha-resources-88692530-get"></a>

列出 HA 资源。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-88692530-get-parameters" id="api-cluster-ha-resources-88692530-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的资源；可选值：`ct`, `vm` |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"type": {"description": "仅列出特定类型的资源", "enum": ["ct", "vm"], "optional": 1, "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-88692530-get-returns" id="api-cluster-ha-resources-88692530-get-returns"></a>

```text
{"items": {"properties": {"sid": {"type": "string"}}, "type": "object"}, "links": [{"href": "{sid}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/ha/resources` <a href="#api-cluster-ha-resources-88692530-post" id="api-cluster-ha-resources-88692530-post"></a>

创建新的 HA 资源。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-88692530-post-parameters" id="api-cluster-ha-resources-88692530-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `auto-rebalance` | 类型：boolean；必填：否；默认值：1<br>HA 资源可以在自动重新均衡期间迁移 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `failback` | 类型：boolean；必填：否；默认值：1<br>如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。 |
| `group` | 类型：string；必填：否；默认值：—<br>HA 组标识符。 |
| `max_relocate` | 类型：integer；必填：否；默认值：1<br>资源启动失败时尝试重新安置资源的最大次数。 |
| `max_restart` | 类型：integer；必填：否；默认值：1<br>资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。 |
| `sid` | 类型：string；必填：是；默认值：—<br>HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |
| `state` | 类型：string；必填：否；默认值："started"<br>请求的资源状态。CRM 读取此状态并据此采取操作。<br>请注意，`enabled` 只是 `started` 的别名。<br><br>`started`;;<br><br>CRM 尝试启动资源。服务状态<br>在成功启动后设为 `started`。发生节点故障或启动<br>失败时，它会尝试恢复资源。  如果所有尝试均失败，服务<br>状态将设为 `error`。<br><br>`stopped`;;<br><br>CRM 尝试使资源保持 `stopped` 状态，但<br>在节点故障时仍会尝试重新安置资源。<br><br>`disabled`;;<br><br>CRM 尝试将资源置于 `stopped` 状态，但不会尝试<br>在节点故障时重新安置资源。此<br>状态主要用于错误恢复，因为这是使资源脱离<br>`error` 状态的唯一方式。<br><br>`ignored`;;<br><br>资源会从管理器状态中移除，因此 CRM 和 LRM 将<br>不再操作此资源。所有影响此资源的 {pve} API 调用<br>都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢<br>弃。发生节点故障时，此资源不会被重新安置<br>。<br><br>；可选值：`started`, `stopped`, `enabled`, `disabled`, `ignored` |
| `type` | 类型：string；必填：否；默认值：—<br>资源类型。；可选值：`ct`, `vm` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "auto-rebalance": {"default": 1, "description": "HA 资源可以在自动重新均衡期间迁移", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "failback": {
      "default": 1, "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。", "optional": 1,
      "type": "boolean", "typetext": "<boolean>"
    },
    "group": {"description": "HA 组标识符。", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"},
    "max_relocate": {
      "default": 1, "description": "资源启动失败时尝试重新安置资源的最大次数。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "max_restart": {
      "default": 1, "description": "资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。",
      "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    },
    "state": {
      "default": "started", "description": "请求的资源状态。", "enum": ["started", "stopped", "enabled", "disabled", "ignored"], "optional": 1,
      "type": "string",
      "verbose_description": "请求的资源状态。CRM 读取此状态并据此采取操作。\n请注意，`enabled` 只是 `started` 的别名。\n\n`started`;;\n\nCRM 尝试启动资源。服务状态\n在成功启动后设为 `started`。发生节点故障或启动\n失败时，它会尝试恢复资源。  如果所有尝试均失败，服务\n状态将设为 `error`。\n\n`stopped`;;\n\nCRM 尝试使资源保持 `stopped` 状态，但\n在节点故障时仍会尝试重新安置资源。\n\n`disabled`;;\n\nCRM 尝试将资源置于 `stopped` 状态，但不会尝试\n在节点故障时重新安置资源。此\n状态主要用于错误恢复，因为这是使资源脱离\n`error` 状态的唯一方式。\n\n`ignored`;;\n\n资源会从管理器状态中移除，因此 CRM 和 LRM 将\n不再操作此资源。所有影响此资源的 {pve} API 调用\n都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢\n弃。发生节点故障时，此资源不会被重新安置\n。\n\n"
    },
    "type": {"description": "资源类型。", "enum": ["ct", "vm"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-88692530-post-returns" id="api-cluster-ha-resources-88692530-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources)。

## `/cluster/ha/resources/{sid}` <a href="#api-cluster-ha-resources-sid-ae318576" id="api-cluster-ha-resources-sid-ae318576"></a>

原始接口路径：`/cluster/ha/resources/{sid}`。

### DELETE `/cluster/ha/resources/{sid}` <a href="#api-cluster-ha-resources-sid-ae318576-delete" id="api-cluster-ha-resources-sid-ae318576-delete"></a>

删除资源配置。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-sid-ae318576-delete-parameters" id="api-cluster-ha-resources-sid-ae318576-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `purge` | 类型：boolean；必填：否；默认值：1<br>从引用此资源的规则中移除此资源；如果此资源是规则中的唯一资源，则删除该规则 |
| `sid` | 类型：string；必填：是；默认值：—<br>HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "purge": {
      "default": 1, "description": "从引用此资源的规则中移除此资源；如果此资源是规则中的唯一资源，则删除该规则", "optional": 1, "type": "boolean",
      "typetext": "<boolean>"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-sid-ae318576-delete-returns" id="api-cluster-ha-resources-sid-ae318576-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/ha/resources/{sid}` <a href="#api-cluster-ha-resources-sid-ae318576-get" id="api-cluster-ha-resources-sid-ae318576-get"></a>

读取资源配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-sid-ae318576-get-parameters" id="api-cluster-ha-resources-sid-ae318576-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `sid` | 类型：string；必填：是；默认值：—<br>HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-sid-ae318576-get-returns" id="api-cluster-ha-resources-sid-ae318576-get-returns"></a>

```text
{
  "properties": {
    "auto-rebalance": {"default": 1, "description": "HA 资源可以在自动重新均衡期间迁移。", "optional": 1, "type": "boolean"},
    "comment": {"description": "描述。", "optional": 1, "type": "string"}, "digest": {"description": "可用于防止并发修改。", "type": "string"},
    "failback": {
      "default": 1, "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性规则，将 HA 资源自动迁移到优先级最高的节点。", "optional": 1,
      "type": "boolean"
    },
    "group": {"description": "HA 组标识符。", "format": "pve-configid", "optional": 1, "type": "string"},
    "max_relocate": {"description": "服务启动失败时尝试重新安置服务的最大次数。", "optional": 1, "type": "integer"},
    "max_restart": {"description": "服务启动失败后在节点上尝试重新启动服务的最大次数。", "optional": 1, "type": "integer"},
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    },
    "state": {"description": "请求的资源状态。", "enum": ["started", "stopped", "enabled", "disabled", "ignored"], "optional": 1, "type": "string"},
    "type": {"description": "资源类型。", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/ha/resources/{sid}` <a href="#api-cluster-ha-resources-sid-ae318576-put" id="api-cluster-ha-resources-sid-ae318576-put"></a>

更新资源配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-sid-ae318576-put-parameters" id="api-cluster-ha-resources-sid-ae318576-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `auto-rebalance` | 类型：boolean；必填：否；默认值：1<br>HA 资源可以在自动重新均衡期间迁移 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `failback` | 类型：boolean；必填：否；默认值：1<br>如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。 |
| `group` | 类型：string；必填：否；默认值：—<br>HA 组标识符。 |
| `max_relocate` | 类型：integer；必填：否；默认值：1<br>资源启动失败时尝试重新安置资源的最大次数。 |
| `max_restart` | 类型：integer；必填：否；默认值：1<br>资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。 |
| `sid` | 类型：string；必填：是；默认值：—<br>HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |
| `state` | 类型：string；必填：否；默认值："started"<br>请求的资源状态。CRM 读取此状态并据此采取操作。<br>请注意，`enabled` 只是 `started` 的别名。<br><br>`started`;;<br><br>CRM 尝试启动资源。服务状态<br>在成功启动后设为 `started`。发生节点故障或启动<br>失败时，它会尝试恢复资源。  如果所有尝试均失败，服务<br>状态将设为 `error`。<br><br>`stopped`;;<br><br>CRM 尝试使资源保持 `stopped` 状态，但<br>在节点故障时仍会尝试重新安置资源。<br><br>`disabled`;;<br><br>CRM 尝试将资源置于 `stopped` 状态，但不会尝试<br>在节点故障时重新安置资源。此<br>状态主要用于错误恢复，因为这是使资源脱离<br>`error` 状态的唯一方式。<br><br>`ignored`;;<br><br>资源会从管理器状态中移除，因此 CRM 和 LRM 将<br>不再操作此资源。所有影响此资源的 {pve} API 调用<br>都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢<br>弃。发生节点故障时，此资源不会被重新安置<br>。<br><br>；可选值：`started`, `stopped`, `enabled`, `disabled`, `ignored` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "auto-rebalance": {"default": 1, "description": "HA 资源可以在自动重新均衡期间迁移", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "failback": {
      "default": 1, "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性  规则，将 HA 资源自动迁移到优先级最高的节点。", "optional": 1,
      "type": "boolean", "typetext": "<boolean>"
    },
    "group": {"description": "HA 组标识符。", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"},
    "max_relocate": {
      "default": 1, "description": "资源启动失败时尝试重新安置资源的最大次数。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "max_restart": {
      "default": 1, "description": "资源启动失败后在节点上尝试重新启动资源的最大次数。达到此次数后，HA 管理器将尝试将资源重新安置到符合条件的节点。",
      "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    },
    "state": {
      "default": "started", "description": "请求的资源状态。", "enum": ["started", "stopped", "enabled", "disabled", "ignored"], "optional": 1,
      "type": "string",
      "verbose_description": "请求的资源状态。CRM 读取此状态并据此采取操作。\n请注意，`enabled` 只是 `started` 的别名。\n\n`started`;;\n\nCRM 尝试启动资源。服务状态\n在成功启动后设为 `started`。发生节点故障或启动\n失败时，它会尝试恢复资源。  如果所有尝试均失败，服务\n状态将设为 `error`。\n\n`stopped`;;\n\nCRM 尝试使资源保持 `stopped` 状态，但\n在节点故障时仍会尝试重新安置资源。\n\n`disabled`;;\n\nCRM 尝试将资源置于 `stopped` 状态，但不会尝试\n在节点故障时重新安置资源。此\n状态主要用于错误恢复，因为这是使资源脱离\n`error` 状态的唯一方式。\n\n`ignored`;;\n\n资源会从管理器状态中移除，因此 CRM 和 LRM 将\n不再操作此资源。所有影响此资源的 {pve} API 调用\n都将直接执行，绕过 HA 栈。此资源处于此状态时，CRM 命令将被丢\n弃。发生节点故障时，此资源不会被重新安置\n。\n\n"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-sid-ae318576-put-returns" id="api-cluster-ha-resources-sid-ae318576-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources/{sid})。

## `/cluster/ha/resources/{sid}/migrate` <a href="#api-cluster-ha-resources-sid-migrate-94224403" id="api-cluster-ha-resources-sid-migrate-94224403"></a>

原始接口路径：`/cluster/ha/resources/{sid}/migrate`。

### POST `/cluster/ha/resources/{sid}/migrate` <a href="#api-cluster-ha-resources-sid-migrate-94224403-post" id="api-cluster-ha-resources-sid-migrate-94224403-post"></a>

请求将资源在线迁移到另一个节点。

**方法标识：** `migrate`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-sid-migrate-94224403-post-parameters" id="api-cluster-ha-resources-sid-migrate-94224403-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `node` | 类型：string；必填：是；默认值：—<br>目标节点。 |
| `sid` | 类型：string；必填：是；默认值：—<br>HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "node": {"description": "目标节点。", "format": "pve-node", "type": "string", "typetext": "<string>"},
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-sid-migrate-94224403-post-returns" id="api-cluster-ha-resources-sid-migrate-94224403-post-returns"></a>

```text
{
  "properties": {
    "blocking-resources": {
      "description": "阻止将给定 HA 资源迁移到请求的目标节点的 HA 资源。",
      "items": {
        "description": "阻塞迁移的 HA 资源",
        "properties": {
          "cause": {"description": "此 HA 资源阻塞迁移的原因。", "enum": ["node-affinity", "resource-affinity"], "type": "string"},
          "sid": {"description": "阻塞迁移的 HA 资源 ID", "type": "string"}
        },
        "type": "object"
      },
      "optional": 1, "type": "array"
    },
    "comigrated-resources": {"description": "由于与给定 HA 资源具有正向亲和性，而迁移到相同请求目标节点的 HA 资源。", "optional": 1, "type": "array"},
    "requested-node": {"description": "请求迁移到的节点。", "optional": 0, "type": "string"},
    "sid": {"description": "请求迁移的 HA 资源。", "optional": 0, "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources/{sid}/migrate)。

## `/cluster/ha/resources/{sid}/relocate` <a href="#api-cluster-ha-resources-sid-relocate-1125a342" id="api-cluster-ha-resources-sid-relocate-1125a342"></a>

原始接口路径：`/cluster/ha/resources/{sid}/relocate`。

### POST `/cluster/ha/resources/{sid}/relocate` <a href="#api-cluster-ha-resources-sid-relocate-1125a342-post" id="api-cluster-ha-resources-sid-relocate-1125a342-post"></a>

请求将资源重新安置到另一节点。此操作会停止旧节点上的服务，并在目标节点上重新启动。

**方法标识：** `relocate`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-resources-sid-relocate-1125a342-post-parameters" id="api-cluster-ha-resources-sid-relocate-1125a342-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `node` | 类型：string；必填：是；默认值：—<br>目标节点。 |
| `sid` | 类型：string；必填：是；默认值：—<br>HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "node": {"description": "目标节点。", "format": "pve-node", "type": "string", "typetext": "<string>"},
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id", "type": "string", "typetext": "<type>:<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-resources-sid-relocate-1125a342-post-returns" id="api-cluster-ha-resources-sid-relocate-1125a342-post-returns"></a>

```text
{
  "properties": {
    "blocking-resources": {
      "description": "阻止将给定 HA 资源重新安置到请求的目标节点的 HA 资源。",
      "items": {
        "description": "阻塞迁移的 HA 资源",
        "properties": {
          "cause": {"description": "此 HA 资源阻塞重新安置的原因。", "enum": ["node-affinity", "resource-affinity"], "type": "string"},
          "sid": {"description": "阻塞迁移的 HA 资源 ID", "type": "string"}
        },
        "type": "object"
      },
      "optional": 1, "type": "array"
    },
    "comigrated-resources": {
      "description": "由于与给定 HA 资源具有正向亲和性，而重新安置到相同请求目标节点的 HA 资源。",
      "items": {"description": "一同迁移的 HA 资源", "type": "string"}, "optional": 1, "type": "array"
    },
    "requested-node": {"description": "请求重新安置到的节点。", "optional": 0, "type": "string"},
    "sid": {"description": "请求重新安置的 HA 资源。", "optional": 0, "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources/{sid}/relocate)。

## `/cluster/ha/groups` <a href="#api-cluster-ha-groups-04915cfc" id="api-cluster-ha-groups-04915cfc"></a>

原始接口路径：`/cluster/ha/groups`。

### GET `/cluster/ha/groups` <a href="#api-cluster-ha-groups-04915cfc-get" id="api-cluster-ha-groups-04915cfc-get"></a>

获取 HA 组。（已弃用，建议使用 HA 规则）

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-groups-04915cfc-get-parameters" id="api-cluster-ha-groups-04915cfc-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-groups-04915cfc-get-returns" id="api-cluster-ha-groups-04915cfc-get-returns"></a>

```text
{"items": {"properties": {"group": {"type": "string"}}, "type": "object"}, "links": [{"href": "{group}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/ha/groups` <a href="#api-cluster-ha-groups-04915cfc-post" id="api-cluster-ha-groups-04915cfc-post"></a>

创建新的 HA 组。（已弃用，建议使用 HA 规则）

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-groups-04915cfc-post-parameters" id="api-cluster-ha-groups-04915cfc-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `group` | 类型：string；必填：是；默认值：—<br>HA 组标识符。 |
| `nodes` | 类型：string；必填：是；默认值：—<br>集群节点成员列表，可为每个节点指定优先级。资源将在可用节点中优先级最高的节点上运行。如果最高优先级有多个节点，则资源将分布到这些节点上。优先级仅具有相对意义。数值越大，优先级越高。 |
| `nofailback` | 类型：boolean；必填：否；默认值：0<br>CRM 尝试在优先级最高的节点上运行服务。如果更高优先级的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。 |
| `restricted` | 类型：boolean；必填：否；默认值：0<br>绑定到受限组的资源只能在该组定义的节点上运行。如果没有组成员节点在线，资源将进入停止状态。非受限组中的资源在所有组成员离线时可在任意集群节点上运行，但一旦有组成员上线就会迁回。使用仅含一个成员的非受限组，可实现“首选节点”行为。 |
| `type` | 类型：string；必填：否；默认值：—<br>组类型。；可选值：`group` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "group": {"description": "HA 组标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "nodes": {
      "description": "集群节点名称列表，可选择指定优先级。", "format": "pve-ha-node-list", "optional": 0, "type": "string",
      "typetext": "<node>[:<pri>]{,<node>[:<pri>]}*",
      "verbose_description": "集群节点成员列表，可为每个节点指定优先级。资源将在可用节点中优先级最高的节点上运行。如果最高优先级有多个节点，则资源将分布到这些节点上。优先级仅具有相对意义。数值越大，优先级越高。"
    },
    "nofailback": {
      "default": 0, "description": "CRM 尝试在优先级最高的节点上运行服务。如果更高优先级的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。",
      "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "restricted": {
      "default": 0, "description": "绑定到受限组的资源只能在该组定义的节点上运行。", "optional": 1, "type": "boolean", "typetext": "<boolean>",
      "verbose_description": "绑定到受限组的资源只能在该组定义的节点上运行。如果没有组成员节点在线，资源将进入停止状态。非受限组中的资源在所有组成员离线时可在任意集群节点上运行，但一旦有组成员上线就会迁回。使用仅含一个成员的非受限组，可实现“首选节点”行为。"
    },
    "type": {"description": "组类型。", "enum": ["group"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-groups-04915cfc-post-returns" id="api-cluster-ha-groups-04915cfc-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/groups)。

## `/cluster/ha/groups/{group}` <a href="#api-cluster-ha-groups-group-8889ce37" id="api-cluster-ha-groups-group-8889ce37"></a>

原始接口路径：`/cluster/ha/groups/{group}`。

### DELETE `/cluster/ha/groups/{group}` <a href="#api-cluster-ha-groups-group-8889ce37-delete" id="api-cluster-ha-groups-group-8889ce37-delete"></a>

删除 HA 组配置。（已弃用，建议使用 HA 规则）

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-groups-group-8889ce37-delete-parameters" id="api-cluster-ha-groups-group-8889ce37-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `group` | 类型：string；必填：是；默认值：—<br>HA 组标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"group": {"description": "HA 组标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-ha-groups-group-8889ce37-delete-returns" id="api-cluster-ha-groups-group-8889ce37-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/ha/groups/{group}` <a href="#api-cluster-ha-groups-group-8889ce37-get" id="api-cluster-ha-groups-group-8889ce37-get"></a>

读取 HA 组配置。（已弃用，改用 HA 规则）

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-groups-group-8889ce37-get-parameters" id="api-cluster-ha-groups-group-8889ce37-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `group` | 类型：string；必填：是；默认值：—<br>HA 组标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"group": {"description": "HA 组标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-ha-groups-group-8889ce37-get-returns" id="api-cluster-ha-groups-group-8889ce37-get-returns"></a>

```text
{}
```

### PUT `/cluster/ha/groups/{group}` <a href="#api-cluster-ha-groups-group-8889ce37-put" id="api-cluster-ha-groups-group-8889ce37-put"></a>

更新 HA 组配置。（已弃用，建议使用 HA 规则）

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-groups-group-8889ce37-put-parameters" id="api-cluster-ha-groups-group-8889ce37-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `group` | 类型：string；必填：是；默认值：—<br>HA 组标识符。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点成员列表，可为每个节点指定优先级。资源将在可用节点中优先级最高的节点上运行。如果最高优先级有多个节点，则资源将分布到这些节点上。优先级仅具有相对意义。数值越大，优先级越高。 |
| `nofailback` | 类型：boolean；必填：否；默认值：0<br>CRM 尝试在优先级最高的节点上运行服务。如果更高优先级的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。 |
| `restricted` | 类型：boolean；必填：否；默认值：0<br>绑定到受限组的资源只能在该组定义的节点上运行。如果没有组成员节点在线，资源将进入停止状态。非受限组中的资源在所有组成员离线时可在任意集群节点上运行，但一旦有组成员上线就会迁回。使用仅含一个成员的非受限组，可实现“首选节点”行为。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "group": {"description": "HA 组标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "nodes": {
      "description": "集群节点名称列表，可选择指定优先级。", "format": "pve-ha-node-list", "optional": 1, "type": "string",
      "typetext": "<node>[:<pri>]{,<node>[:<pri>]}*",
      "verbose_description": "集群节点成员列表，可为每个节点指定优先级。资源将在可用节点中优先级最高的节点上运行。如果最高优先级有多个节点，则资源将分布到这些节点上。优先级仅具有相对意义。数值越大，优先级越高。"
    },
    "nofailback": {
      "default": 0, "description": "CRM 尝试在优先级最高的节点上运行服务。如果更高优先级的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。",
      "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "restricted": {
      "default": 0, "description": "绑定到受限组的资源只能在该组定义的节点上运行。", "optional": 1, "type": "boolean", "typetext": "<boolean>",
      "verbose_description": "绑定到受限组的资源只能在该组定义的节点上运行。如果没有组成员节点在线，资源将进入停止状态。非受限组中的资源在所有组成员离线时可在任意集群节点上运行，但一旦有组成员上线就会迁回。使用仅含一个成员的非受限组，可实现“首选节点”行为。"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-groups-group-8889ce37-put-returns" id="api-cluster-ha-groups-group-8889ce37-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/groups/{group})。

## `/cluster/ha/rules` <a href="#api-cluster-ha-rules-59e5af64" id="api-cluster-ha-rules-59e5af64"></a>

原始接口路径：`/cluster/ha/rules`。

### GET `/cluster/ha/rules` <a href="#api-cluster-ha-rules-59e5af64-get" id="api-cluster-ha-rules-59e5af64-get"></a>

获取 HA 规则。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-rules-59e5af64-get-parameters" id="api-cluster-ha-rules-59e5af64-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `resource` | 类型：string；必填：否；默认值：—<br>将返回列表限制为影响指定资源的规则。 |
| `type` | 类型：string；必填：否；默认值：—<br>将返回列表限制为指定规则类型。；可选值：`node-affinity`, `resource-affinity` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "resource": {"description": "将返回列表限制为影响指定资源的规则。", "optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"description": "将返回列表限制为指定规则类型。", "enum": ["node-affinity", "resource-affinity"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-rules-59e5af64-get-returns" id="api-cluster-ha-rules-59e5af64-get-returns"></a>

```text
{"items": {"links": [{"href": "{rule}", "rel": "child"}], "properties": {"rule": {"type": "string"}}, "type": "object"}, "type": "array"}
```

### POST `/cluster/ha/rules` <a href="#api-cluster-ha-rules-59e5af64-post" id="api-cluster-ha-rules-59e5af64-post"></a>

创建 HA 规则。

**方法标识：** `create_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-rules-59e5af64-post-parameters" id="api-cluster-ha-rules-59e5af64-post-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-rules-59e5af64-post-returns" id="api-cluster-ha-rules-59e5af64-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/rules)。

## `/cluster/ha/rules/{rule}` <a href="#api-cluster-ha-rules-rule-cc218e5b" id="api-cluster-ha-rules-rule-cc218e5b"></a>

原始接口路径：`/cluster/ha/rules/{rule}`。

### DELETE `/cluster/ha/rules/{rule}` <a href="#api-cluster-ha-rules-rule-cc218e5b-delete" id="api-cluster-ha-rules-rule-cc218e5b-delete"></a>

删除 HA 规则。

**方法标识：** `delete_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-rules-rule-cc218e5b-delete-parameters" id="api-cluster-ha-rules-rule-cc218e5b-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `rule` | 类型：string；必填：是；默认值：—<br>HA 规则标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"rule": {"description": "HA 规则标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-ha-rules-rule-cc218e5b-delete-returns" id="api-cluster-ha-rules-rule-cc218e5b-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/ha/rules/{rule}` <a href="#api-cluster-ha-rules-rule-cc218e5b-get" id="api-cluster-ha-rules-rule-cc218e5b-get"></a>

读取 HA 规则。

**方法标识：** `read_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-rules-rule-cc218e5b-get-parameters" id="api-cluster-ha-rules-rule-cc218e5b-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `rule` | 类型：string；必填：是；默认值：—<br>HA 规则标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"rule": {"description": "HA 规则标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-ha-rules-rule-cc218e5b-get-returns" id="api-cluster-ha-rules-rule-cc218e5b-get-returns"></a>

```text
{
  "properties": {
    "rule": {"description": "HA 规则标识符。", "format": "pve-configid", "type": "string"},
    "type": {"description": "HA 规则类型。", "enum": ["node-affinity", "resource-affinity"], "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/ha/rules/{rule}` <a href="#api-cluster-ha-rules-rule-cc218e5b-put" id="api-cluster-ha-rules-rule-cc218e5b-put"></a>

更新 HA 规则。

**方法标识：** `update_rule`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-rules-rule-cc218e5b-put-parameters" id="api-cluster-ha-rules-rule-cc218e5b-put-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-rules-rule-cc218e5b-put-returns" id="api-cluster-ha-rules-rule-cc218e5b-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/rules/{rule})。

## `/cluster/ha/status` <a href="#api-cluster-ha-status-6803f961" id="api-cluster-ha-status-6803f961"></a>

原始接口路径：`/cluster/ha/status`。

### GET `/cluster/ha/status` <a href="#api-cluster-ha-status-6803f961-get" id="api-cluster-ha-status-6803f961-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-status-6803f961-get-parameters" id="api-cluster-ha-status-6803f961-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-status-6803f961-get-returns" id="api-cluster-ha-status-6803f961-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status)。

## `/cluster/ha/status/current` <a href="#api-cluster-ha-status-current-aa0de642" id="api-cluster-ha-status-current-aa0de642"></a>

原始接口路径：`/cluster/ha/status/current`。

### GET `/cluster/ha/status/current` <a href="#api-cluster-ha-status-current-aa0de642-get" id="api-cluster-ha-status-current-aa0de642-get"></a>

获取 HA 管理器状态。

**方法标识：** `status`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-status-current-aa0de642-get-parameters" id="api-cluster-ha-status-current-aa0de642-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-status-current-aa0de642-get-returns" id="api-cluster-ha-status-current-aa0de642-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "armed-state": {
        "description": "用于 'fencing' 类型。HA 是已启用、待机、正在解除还是已解除。", "enum": ["armed", "standby", "disarming", "disarmed"], "optional": 1,
        "type": "string"
      },
      "auto-rebalance": {"default": 1, "description": "HA 资源可以在自动重新均衡期间迁移。", "optional": 1, "type": "boolean"},
      "crm_state": {"description": "用于 'service' 类型。CRM 所见的服务状态。", "optional": 1, "type": "string"},
      "failback": {
        "default": 1, "description": "如果优先级高于当前节点的节点上线，则根据节点亲和性规则，将 HA 资源自动迁移到优先级最高的节点。", "optional": 1,
        "type": "boolean"
      },
      "id": {"description": "状态条目 ID（quorum、master、lrm:<node>、service:<sid>）。", "type": "string"},
      "max_relocate": {"description": "用于 'service' 类型。", "optional": 1, "type": "integer"},
      "max_restart": {"description": "用于 'service' 类型。", "optional": 1, "type": "integer"},
      "node": {"description": "与状态条目关联的节点。", "type": "string"},
      "quorate": {"description": "用于 'quorum' 类型。集群是否达到仲裁。", "optional": 1, "type": "boolean"},
      "request_state": {"description": "用于 'service' 类型。请求的服务状态。", "optional": 1, "type": "string"},
      "resource_mode": {"description": "用于 'fencing' 类型。解除后如何处理资源。", "enum": ["freeze", "ignore"], "optional": 1, "type": "string"},
      "sid": {"description": "用于 'service' 类型。服务 ID。", "optional": 1, "type": "string"},
      "state": {"description": "用于 'service' 类型。详细服务状态。", "optional": 1, "type": "string"},
      "status": {"description": "条目状态（值取决于类型）。", "type": "string"},
      "timestamp": {"description": "用于 'lrm'、'master' 类型。状态信息的时间戳。", "optional": 1, "type": "integer"},
      "type": {"description": "状态条目类型。", "enum": ["quorum", "master", "lrm", "service", "fencing"]}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/current)。

## `/cluster/ha/status/manager_status` <a href="#api-cluster-ha-status-manager-status-2de56102" id="api-cluster-ha-status-manager-status-2de56102"></a>

原始接口路径：`/cluster/ha/status/manager_status`。

### GET `/cluster/ha/status/manager_status` <a href="#api-cluster-ha-status-manager-status-2de56102-get" id="api-cluster-ha-status-manager-status-2de56102-get"></a>

获取完整的 HA 管理器状态，包括 LRM 状态。

**方法标识：** `manager_status`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ha-status-manager-status-2de56102-get-parameters" id="api-cluster-ha-status-manager-status-2de56102-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-status-manager-status-2de56102-get-returns" id="api-cluster-ha-status-manager-status-2de56102-get-returns"></a>

```text
{"type": "object"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/manager_status)。

## `/cluster/ha/status/disarm-ha` <a href="#api-cluster-ha-status-disarm-ha-bafece41" id="api-cluster-ha-status-disarm-ha-bafece41"></a>

原始接口路径：`/cluster/ha/status/disarm-ha`。

### POST `/cluster/ha/status/disarm-ha` <a href="#api-cluster-ha-status-disarm-ha-bafece41-post" id="api-cluster-ha-status-disarm-ha-bafece41-post"></a>

请求解除 HA 堆栈的布防，并释放整个集群范围内的所有看门狗。

**方法标识：** `disarm-ha`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-status-disarm-ha-bafece41-post-parameters" id="api-cluster-ha-status-disarm-ha-bafece41-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `resource-mode` | 类型：string；必填：是；默认值：—<br>控制解除后如何处理 HA 管理的资源。资源的当前状态不受影响。'freeze'：不应用新命令和状态更改。'ignore'：将资源移出 HA 跟踪，此后可按未受 HA 管理的资源进行管理。；可选值：`freeze`, `ignore` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "resource-mode": {
      "description": "控制解除后如何处理 HA 管理的资源。资源的当前状态不受影响。'freeze'：不应用新命令和状态更改。'ignore'：将资源移出 HA 跟踪，此后可按未受 HA 管理的资源进行管理。",
      "enum": ["freeze", "ignore"], "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ha-status-disarm-ha-bafece41-post-returns" id="api-cluster-ha-status-disarm-ha-bafece41-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/disarm-ha)。

## `/cluster/ha/status/arm-ha` <a href="#api-cluster-ha-status-arm-ha-fd3fb558" id="api-cluster-ha-status-arm-ha-fd3fb558"></a>

原始接口路径：`/cluster/ha/status/arm-ha`。

### POST `/cluster/ha/status/arm-ha` <a href="#api-cluster-ha-status-arm-ha-fd3fb558-post" id="api-cluster-ha-status-arm-ha-fd3fb558-post"></a>

请求在 HA 堆栈解除布防后重新布防。

**方法标识：** `arm-ha`

**权限**

```text
{"check": ["perm", "/", ["Sys.Console"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ha-status-arm-ha-fd3fb558-post-parameters" id="api-cluster-ha-status-arm-ha-fd3fb558-post-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ha-status-arm-ha-fd3fb558-post-returns" id="api-cluster-ha-status-arm-ha-fd3fb558-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/arm-ha)。

## `/cluster/acme` <a href="#api-cluster-acme-7e2ce7e3" id="api-cluster-acme-7e2ce7e3"></a>

原始接口路径：`/cluster/acme`。

### GET `/cluster/acme` <a href="#api-cluster-acme-7e2ce7e3-get" id="api-cluster-acme-7e2ce7e3-get"></a>

ACMEAccount 索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-acme-7e2ce7e3-get-parameters" id="api-cluster-acme-7e2ce7e3-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-acme-7e2ce7e3-get-returns" id="api-cluster-acme-7e2ce7e3-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme)。

## `/cluster/acme/plugins` <a href="#api-cluster-acme-plugins-aa24154c" id="api-cluster-acme-plugins-aa24154c"></a>

原始接口路径：`/cluster/acme/plugins`。

### GET `/cluster/acme/plugins` <a href="#api-cluster-acme-plugins-aa24154c-get" id="api-cluster-acme-plugins-aa24154c-get"></a>

ACME 插件索引。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-plugins-aa24154c-get-parameters" id="api-cluster-acme-plugins-aa24154c-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的 ACME 插件；可选值：`dns`, `standalone` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"type": {"description": "仅列出特定类型的 ACME 插件", "enum": ["dns", "standalone"], "optional": 1, "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-plugins-aa24154c-get-returns" id="api-cluster-acme-plugins-aa24154c-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "api": {
        "description": "API 插件名称",
        "enum": [
          "1984hosting", "acmedns", "acmeproxy", "active24", "ad", "ali", "alviy", "anx", "artfiles", "arvan", "aurora", "autodns", "aws", "azion", "azure",
          "beget", "bookmyname", "bunny", "cf", "clouddns", "cloudns", "cn", "conoha", "constellix", "cpanel", "curanet", "cyon", "da", "ddnss", "desec", "df",
          "dgon", "dnsexit", "dnshome", "dnsimple", "dnsservices", "doapi", "domeneshop", "dp", "dpi", "dreamhost", "duckdns", "durabledns", "dyn", "dynu",
          "dynv6", "easydns", "edgecenter", "edgedns", "euserv", "exoscale", "fornex", "freedns", "freemyip", "gandi_livedns", "gcloud", "gcore", "gd",
          "geoscaling", "googledomains", "he", "he_ddns", "hetzner", "hetznercloud", "hexonet", "hostingde", "huaweicloud", "infoblox", "infomaniak",
          "internetbs", "inwx", "ionos", "ionos_cloud", "ipv64", "ispconfig", "jd", "joker", "kappernet", "kas", "kinghost", "knot", "la", "leaseweb",
          "lexicon", "limacity", "linode", "linode_v4", "loopia", "lua", "maradns", "me", "miab", "mijnhost", "misaka", "myapi", "mydevil", "mydnsjp",
          "mythic_beasts", "namecheap", "namecom", "namesilo", "nanelo", "nederhost", "neodigit", "netcup", "netlify", "nic", "njalla", "nm", "nsd", "nsone",
          "nsupdate", "nw", "oci", "omglol", "one", "online", "openprovider", "openprovider_rest", "openstack", "opnsense", "ovh", "pdns", "pleskxml",
          "pointhq", "porkbun", "rackcorp", "rackspace", "rage4", "rcode0", "regru", "scaleway", "schlundtech", "selectel", "selfhost", "servercow", "simply",
          "spaceship", "technitium", "tele3", "tencent", "timeweb", "transip", "udr", "ultra", "unoeuro", "variomedia", "veesp", "vercel", "vscale", "vultr",
          "websupport", "west_cn", "world4you", "yandex360", "yc", "zilore", "zone", "zoneedit", "zonomi"
        ],
        "optional": 1, "type": "string"
      },
      "data": {"description": "DNS 插件数据。（base64 编码）", "optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "disable": {"description": "用于禁用此配置的标志。", "optional": 1, "type": "boolean"},
      "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string"},
      "plugin": {"description": "ACME 插件实例的唯一标识符。", "format": "pve-configid", "type": "string"},
      "type": {"description": "ACME 质询类型。", "enum": ["dns", "standalone"], "type": "string"},
      "validation-delay": {
        "default": 30, "description": "请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。", "maximum": 172800, "minimum": 0, "optional": 1,
        "type": "integer"
      }
    },
    "type": "object"
  },
  "links": [{"href": "{plugin}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/acme/plugins` <a href="#api-cluster-acme-plugins-aa24154c-post" id="api-cluster-acme-plugins-aa24154c-post"></a>

添加 ACME 插件配置。

**方法标识：** `add_plugin`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-plugins-aa24154c-post-parameters" id="api-cluster-acme-plugins-aa24154c-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `api` | 类型：string；必填：否；默认值：—<br>API 插件名称；可选值：`1984hosting`, `acmedns`, `acmeproxy`, `active24`, `ad`, `ali`, `alviy`, `anx`, `artfiles`, `arvan`, `aurora`, `autodns`, `aws`, `azion`, `azure`, `beget`, `bookmyname`, `bunny`, `cf`, `clouddns`, `cloudns`, `cn`, `conoha`, `constellix`, `cpanel`, `curanet`, `cyon`, `da`, `ddnss`, `desec`, `df`, `dgon`, `dnsexit`, `dnshome`, `dnsimple`, `dnsservices`, `doapi`, `domeneshop`, `dp`, `dpi`, `dreamhost`, `duckdns`, `durabledns`, `dyn`, `dynu`, `dynv6`, `easydns`, `edgecenter`, `edgedns`, `euserv`, `exoscale`, `fornex`, `freedns`, `freemyip`, `gandi_livedns`, `gcloud`, `gcore`, `gd`, `geoscaling`, `googledomains`, `he`, `he_ddns`, `hetzner`, `hetznercloud`, `hexonet`, `hostingde`, `huaweicloud`, `infoblox`, `infomaniak`, `internetbs`, `inwx`, `ionos`, `ionos_cloud`, `ipv64`, `ispconfig`, `jd`, `joker`, `kappernet`, `kas`, `kinghost`, `knot`, `la`, `leaseweb`, `lexicon`, `limacity`, `linode`, `linode_v4`, `loopia`, `lua`, `maradns`, `me`, `miab`, `mijnhost`, `misaka`, `myapi`, `mydevil`, `mydnsjp`, `mythic_beasts`, `namecheap`, `namecom`, `namesilo`, `nanelo`, `nederhost`, `neodigit`, `netcup`, `netlify`, `nic`, `njalla`, `nm`, `nsd`, `nsone`, `nsupdate`, `nw`, `oci`, `omglol`, `one`, `online`, `openprovider`, `openprovider_rest`, `openstack`, `opnsense`, `ovh`, `pdns`, `pleskxml`, `pointhq`, `porkbun`, `rackcorp`, `rackspace`, `rage4`, `rcode0`, `regru`, `scaleway`, `schlundtech`, `selectel`, `selfhost`, `servercow`, `simply`, `spaceship`, `technitium`, `tele3`, `tencent`, `timeweb`, `transip`, `udr`, `ultra`, `unoeuro`, `variomedia`, `veesp`, `vercel`, `vscale`, `vultr`, `websupport`, `west_cn`, `world4you`, `yandex360`, `yc`, `zilore`, `zone`, `zoneedit`, `zonomi` |
| `data` | 类型：string；必填：否；默认值：—<br>DNS 插件数据。（base64 编码） |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用此配置的标志。 |
| `id` | 类型：string；必填：是；默认值：—<br>ACME 插件 ID 名称 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `type` | 类型：string；必填：是；默认值：—<br>ACME 质询类型。；可选值：`dns`, `standalone` |
| `validation-delay` | 类型：integer；必填：否；默认值：30<br>请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "api": {
      "description": "API 插件名称",
      "enum": [
        "1984hosting", "acmedns", "acmeproxy", "active24", "ad", "ali", "alviy", "anx", "artfiles", "arvan", "aurora", "autodns", "aws", "azion", "azure",
        "beget", "bookmyname", "bunny", "cf", "clouddns", "cloudns", "cn", "conoha", "constellix", "cpanel", "curanet", "cyon", "da", "ddnss", "desec", "df",
        "dgon", "dnsexit", "dnshome", "dnsimple", "dnsservices", "doapi", "domeneshop", "dp", "dpi", "dreamhost", "duckdns", "durabledns", "dyn", "dynu",
        "dynv6", "easydns", "edgecenter", "edgedns", "euserv", "exoscale", "fornex", "freedns", "freemyip", "gandi_livedns", "gcloud", "gcore", "gd",
        "geoscaling", "googledomains", "he", "he_ddns", "hetzner", "hetznercloud", "hexonet", "hostingde", "huaweicloud", "infoblox", "infomaniak",
        "internetbs", "inwx", "ionos", "ionos_cloud", "ipv64", "ispconfig", "jd", "joker", "kappernet", "kas", "kinghost", "knot", "la", "leaseweb", "lexicon",
        "limacity", "linode", "linode_v4", "loopia", "lua", "maradns", "me", "miab", "mijnhost", "misaka", "myapi", "mydevil", "mydnsjp", "mythic_beasts",
        "namecheap", "namecom", "namesilo", "nanelo", "nederhost", "neodigit", "netcup", "netlify", "nic", "njalla", "nm", "nsd", "nsone", "nsupdate", "nw",
        "oci", "omglol", "one", "online", "openprovider", "openprovider_rest", "openstack", "opnsense", "ovh", "pdns", "pleskxml", "pointhq", "porkbun",
        "rackcorp", "rackspace", "rage4", "rcode0", "regru", "scaleway", "schlundtech", "selectel", "selfhost", "servercow", "simply", "spaceship",
        "technitium", "tele3", "tencent", "timeweb", "transip", "udr", "ultra", "unoeuro", "variomedia", "veesp", "vercel", "vscale", "vultr", "websupport",
        "west_cn", "world4you", "yandex360", "yc", "zilore", "zone", "zoneedit", "zonomi"
      ],
      "optional": 1, "type": "string"
    },
    "data": {"description": "DNS 插件数据。（base64 编码）", "optional": 1, "type": "string", "typetext": "<string>"},
    "disable": {"description": "用于禁用此配置的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "ACME 插件 ID 名称", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"description": "ACME 质询类型。", "enum": ["dns", "standalone"], "type": "string"},
    "validation-delay": {
      "default": 30, "description": "请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。", "maximum": 172800, "minimum": 0, "optional": 1,
      "type": "integer", "typetext": "<integer> (0 - 172800)"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-plugins-aa24154c-post-returns" id="api-cluster-acme-plugins-aa24154c-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/plugins)。

## `/cluster/acme/plugins/{id}` <a href="#api-cluster-acme-plugins-id-eb72844a" id="api-cluster-acme-plugins-id-eb72844a"></a>

原始接口路径：`/cluster/acme/plugins/{id}`。

### DELETE `/cluster/acme/plugins/{id}` <a href="#api-cluster-acme-plugins-id-eb72844a-delete" id="api-cluster-acme-plugins-id-eb72844a-delete"></a>

删除 ACME 插件配置。

**方法标识：** `delete_plugin`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-plugins-id-eb72844a-delete-parameters" id="api-cluster-acme-plugins-id-eb72844a-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>ACME 插件实例的唯一标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"id": {"description": "ACME 插件实例的唯一标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-plugins-id-eb72844a-delete-returns" id="api-cluster-acme-plugins-id-eb72844a-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/acme/plugins/{id}` <a href="#api-cluster-acme-plugins-id-eb72844a-get" id="api-cluster-acme-plugins-id-eb72844a-get"></a>

获取 ACME 插件配置。

**方法标识：** `get_plugin_config`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-plugins-id-eb72844a-get-parameters" id="api-cluster-acme-plugins-id-eb72844a-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>ACME 插件实例的唯一标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"id": {"description": "ACME 插件实例的唯一标识符。", "format": "pve-configid", "type": "string", "typetext": "<string>"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-plugins-id-eb72844a-get-returns" id="api-cluster-acme-plugins-id-eb72844a-get-returns"></a>

```text
{
  "properties": {
    "api": {
      "description": "API 插件名称",
      "enum": [
        "1984hosting", "acmedns", "acmeproxy", "active24", "ad", "ali", "alviy", "anx", "artfiles", "arvan", "aurora", "autodns", "aws", "azion", "azure",
        "beget", "bookmyname", "bunny", "cf", "clouddns", "cloudns", "cn", "conoha", "constellix", "cpanel", "curanet", "cyon", "da", "ddnss", "desec", "df",
        "dgon", "dnsexit", "dnshome", "dnsimple", "dnsservices", "doapi", "domeneshop", "dp", "dpi", "dreamhost", "duckdns", "durabledns", "dyn", "dynu",
        "dynv6", "easydns", "edgecenter", "edgedns", "euserv", "exoscale", "fornex", "freedns", "freemyip", "gandi_livedns", "gcloud", "gcore", "gd",
        "geoscaling", "googledomains", "he", "he_ddns", "hetzner", "hetznercloud", "hexonet", "hostingde", "huaweicloud", "infoblox", "infomaniak",
        "internetbs", "inwx", "ionos", "ionos_cloud", "ipv64", "ispconfig", "jd", "joker", "kappernet", "kas", "kinghost", "knot", "la", "leaseweb", "lexicon",
        "limacity", "linode", "linode_v4", "loopia", "lua", "maradns", "me", "miab", "mijnhost", "misaka", "myapi", "mydevil", "mydnsjp", "mythic_beasts",
        "namecheap", "namecom", "namesilo", "nanelo", "nederhost", "neodigit", "netcup", "netlify", "nic", "njalla", "nm", "nsd", "nsone", "nsupdate", "nw",
        "oci", "omglol", "one", "online", "openprovider", "openprovider_rest", "openstack", "opnsense", "ovh", "pdns", "pleskxml", "pointhq", "porkbun",
        "rackcorp", "rackspace", "rage4", "rcode0", "regru", "scaleway", "schlundtech", "selectel", "selfhost", "servercow", "simply", "spaceship",
        "technitium", "tele3", "tencent", "timeweb", "transip", "udr", "ultra", "unoeuro", "variomedia", "veesp", "vercel", "vscale", "vultr", "websupport",
        "west_cn", "world4you", "yandex360", "yc", "zilore", "zone", "zoneedit", "zonomi"
      ],
      "optional": 1, "type": "string"
    },
    "data": {"description": "DNS 插件数据。（base64 编码）", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "disable": {"description": "用于禁用此配置的标志。", "optional": 1, "type": "boolean"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string"},
    "plugin": {"description": "ACME 插件实例的唯一标识符。", "format": "pve-configid", "type": "string"},
    "type": {"description": "ACME 质询类型。", "enum": ["dns", "standalone"], "type": "string"},
    "validation-delay": {
      "default": 30, "description": "请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。", "maximum": 172800, "minimum": 0, "optional": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

### PUT `/cluster/acme/plugins/{id}` <a href="#api-cluster-acme-plugins-id-eb72844a-put" id="api-cluster-acme-plugins-id-eb72844a-put"></a>

更新 ACME 插件配置。

**方法标识：** `update_plugin`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-plugins-id-eb72844a-put-parameters" id="api-cluster-acme-plugins-id-eb72844a-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `api` | 类型：string；必填：否；默认值：—<br>API 插件名称；可选值：`1984hosting`, `acmedns`, `acmeproxy`, `active24`, `ad`, `ali`, `alviy`, `anx`, `artfiles`, `arvan`, `aurora`, `autodns`, `aws`, `azion`, `azure`, `beget`, `bookmyname`, `bunny`, `cf`, `clouddns`, `cloudns`, `cn`, `conoha`, `constellix`, `cpanel`, `curanet`, `cyon`, `da`, `ddnss`, `desec`, `df`, `dgon`, `dnsexit`, `dnshome`, `dnsimple`, `dnsservices`, `doapi`, `domeneshop`, `dp`, `dpi`, `dreamhost`, `duckdns`, `durabledns`, `dyn`, `dynu`, `dynv6`, `easydns`, `edgecenter`, `edgedns`, `euserv`, `exoscale`, `fornex`, `freedns`, `freemyip`, `gandi_livedns`, `gcloud`, `gcore`, `gd`, `geoscaling`, `googledomains`, `he`, `he_ddns`, `hetzner`, `hetznercloud`, `hexonet`, `hostingde`, `huaweicloud`, `infoblox`, `infomaniak`, `internetbs`, `inwx`, `ionos`, `ionos_cloud`, `ipv64`, `ispconfig`, `jd`, `joker`, `kappernet`, `kas`, `kinghost`, `knot`, `la`, `leaseweb`, `lexicon`, `limacity`, `linode`, `linode_v4`, `loopia`, `lua`, `maradns`, `me`, `miab`, `mijnhost`, `misaka`, `myapi`, `mydevil`, `mydnsjp`, `mythic_beasts`, `namecheap`, `namecom`, `namesilo`, `nanelo`, `nederhost`, `neodigit`, `netcup`, `netlify`, `nic`, `njalla`, `nm`, `nsd`, `nsone`, `nsupdate`, `nw`, `oci`, `omglol`, `one`, `online`, `openprovider`, `openprovider_rest`, `openstack`, `opnsense`, `ovh`, `pdns`, `pleskxml`, `pointhq`, `porkbun`, `rackcorp`, `rackspace`, `rage4`, `rcode0`, `regru`, `scaleway`, `schlundtech`, `selectel`, `selfhost`, `servercow`, `simply`, `spaceship`, `technitium`, `tele3`, `tencent`, `timeweb`, `transip`, `udr`, `ultra`, `unoeuro`, `variomedia`, `veesp`, `vercel`, `vscale`, `vultr`, `websupport`, `west_cn`, `world4you`, `yandex360`, `yc`, `zilore`, `zone`, `zoneedit`, `zonomi` |
| `data` | 类型：string；必填：否；默认值：—<br>DNS 插件数据。（base64 编码） |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | 类型：boolean；必填：否；默认值：—<br>用于禁用此配置的标志。 |
| `id` | 类型：string；必填：是；默认值：—<br>ACME 插件 ID 名称 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `validation-delay` | 类型：integer；必填：否；默认值：30<br>请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "api": {
      "description": "API 插件名称",
      "enum": [
        "1984hosting", "acmedns", "acmeproxy", "active24", "ad", "ali", "alviy", "anx", "artfiles", "arvan", "aurora", "autodns", "aws", "azion", "azure",
        "beget", "bookmyname", "bunny", "cf", "clouddns", "cloudns", "cn", "conoha", "constellix", "cpanel", "curanet", "cyon", "da", "ddnss", "desec", "df",
        "dgon", "dnsexit", "dnshome", "dnsimple", "dnsservices", "doapi", "domeneshop", "dp", "dpi", "dreamhost", "duckdns", "durabledns", "dyn", "dynu",
        "dynv6", "easydns", "edgecenter", "edgedns", "euserv", "exoscale", "fornex", "freedns", "freemyip", "gandi_livedns", "gcloud", "gcore", "gd",
        "geoscaling", "googledomains", "he", "he_ddns", "hetzner", "hetznercloud", "hexonet", "hostingde", "huaweicloud", "infoblox", "infomaniak",
        "internetbs", "inwx", "ionos", "ionos_cloud", "ipv64", "ispconfig", "jd", "joker", "kappernet", "kas", "kinghost", "knot", "la", "leaseweb", "lexicon",
        "limacity", "linode", "linode_v4", "loopia", "lua", "maradns", "me", "miab", "mijnhost", "misaka", "myapi", "mydevil", "mydnsjp", "mythic_beasts",
        "namecheap", "namecom", "namesilo", "nanelo", "nederhost", "neodigit", "netcup", "netlify", "nic", "njalla", "nm", "nsd", "nsone", "nsupdate", "nw",
        "oci", "omglol", "one", "online", "openprovider", "openprovider_rest", "openstack", "opnsense", "ovh", "pdns", "pleskxml", "pointhq", "porkbun",
        "rackcorp", "rackspace", "rage4", "rcode0", "regru", "scaleway", "schlundtech", "selectel", "selfhost", "servercow", "simply", "spaceship",
        "technitium", "tele3", "tencent", "timeweb", "transip", "udr", "ultra", "unoeuro", "variomedia", "veesp", "vercel", "vscale", "vultr", "websupport",
        "west_cn", "world4you", "yandex360", "yc", "zilore", "zone", "zoneedit", "zonomi"
      ],
      "optional": 1, "type": "string"
    },
    "data": {"description": "DNS 插件数据。（base64 编码）", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable": {"description": "用于禁用此配置的标志。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "ACME 插件 ID 名称", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "validation-delay": {
      "default": 30, "description": "请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。", "maximum": 172800, "minimum": 0, "optional": 1,
      "type": "integer", "typetext": "<integer> (0 - 172800)"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-plugins-id-eb72844a-put-returns" id="api-cluster-acme-plugins-id-eb72844a-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/plugins/{id})。

## `/cluster/acme/account` <a href="#api-cluster-acme-account-cc4d64ad" id="api-cluster-acme-account-cc4d64ad"></a>

原始接口路径：`/cluster/acme/account`。

### GET `/cluster/acme/account` <a href="#api-cluster-acme-account-cc4d64ad-get" id="api-cluster-acme-account-cc4d64ad-get"></a>

ACMEAccount 索引。

**方法标识：** `account_index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-account-cc4d64ad-get-parameters" id="api-cluster-acme-account-cc4d64ad-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-acme-account-cc4d64ad-get-returns" id="api-cluster-acme-account-cc4d64ad-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/acme/account` <a href="#api-cluster-acme-account-cc4d64ad-post" id="api-cluster-acme-account-cc4d64ad-post"></a>

向 CA 注册新的 ACME 账户。

**方法标识：** `register_account`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-account-cc4d64ad-post-parameters" id="api-cluster-acme-account-cc4d64ad-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `contact` | 类型：string；必填：是；默认值：—<br>联系电子邮件地址。 |
| `directory` | 类型：string；必填：否；默认值："https://acme-v02.api.letsencrypt.org/directory"<br>ACME CA 目录端点的 URL。 |
| `eab-hmac-key` | 类型：string；必填：否；默认值：—<br>外部账户绑定的 HMAC 密钥。 |
| `eab-kid` | 类型：string；必填：否；默认值：—<br>外部账户绑定的密钥标识符。 |
| `name` | 类型：string；必填：否；默认值："default"<br>ACME 账户配置文件名。 |
| `tos_url` | 类型：string；必填：否；默认值：—<br>CA 服务条款的 URL——设置此项表示同意条款。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "contact": {"description": "联系电子邮件地址。", "format": "email-list", "type": "string", "typetext": "<string>"},
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory", "description": "ACME CA 目录端点的 URL。", "optional": 1, "pattern": "^https?://.*",
      "type": "string"
    },
    "eab-hmac-key": {"description": "外部账户绑定的 HMAC 密钥。", "optional": 1, "requires": "eab-kid", "type": "string", "typetext": "<string>"},
    "eab-kid": {"description": "外部账户绑定的密钥标识符。", "optional": 1, "requires": "eab-hmac-key", "type": "string", "typetext": "<string>"},
    "name": {
      "default": "default", "description": "ACME 账户配置文件名。", "format": "pve-configid", "format_description": "name", "optional": 1, "type": "string",
      "typetext": "<name>"
    },
    "tos_url": {"description": "CA 服务条款的 URL——设置此项表示同意条款。", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-account-cc4d64ad-post-returns" id="api-cluster-acme-account-cc4d64ad-post-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/account)。

## `/cluster/acme/account/{name}` <a href="#api-cluster-acme-account-name-9ef4bf1c" id="api-cluster-acme-account-name-9ef4bf1c"></a>

原始接口路径：`/cluster/acme/account/{name}`。

### DELETE `/cluster/acme/account/{name}` <a href="#api-cluster-acme-account-name-9ef4bf1c-delete" id="api-cluster-acme-account-name-9ef4bf1c-delete"></a>

在 CA 处停用现有 ACME 账户。

**方法标识：** `deactivate_account`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-account-name-9ef4bf1c-delete-parameters" id="api-cluster-acme-account-name-9ef4bf1c-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：否；默认值："default"<br>ACME 账户配置文件名。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "default": "default", "description": "ACME 账户配置文件名。", "format": "pve-configid", "format_description": "name", "optional": 1, "type": "string",
      "typetext": "<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-account-name-9ef4bf1c-delete-returns" id="api-cluster-acme-account-name-9ef4bf1c-delete-returns"></a>

```text
{"type": "string"}
```

### GET `/cluster/acme/account/{name}` <a href="#api-cluster-acme-account-name-9ef4bf1c-get" id="api-cluster-acme-account-name-9ef4bf1c-get"></a>

返回现有 ACME 账户信息。

**方法标识：** `get_account`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-account-name-9ef4bf1c-get-parameters" id="api-cluster-acme-account-name-9ef4bf1c-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `name` | 类型：string；必填：否；默认值："default"<br>ACME 账户配置文件名。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "default": "default", "description": "ACME 账户配置文件名。", "format": "pve-configid", "format_description": "name", "optional": 1, "type": "string",
      "typetext": "<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-account-name-9ef4bf1c-get-returns" id="api-cluster-acme-account-name-9ef4bf1c-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "account": {"optional": 1, "renderer": "yaml", "type": "object"},
    "directory": {"description": "ACME CA 目录端点的 URL。", "optional": 1, "pattern": "^https?://.*", "type": "string"},
    "location": {"optional": 1, "type": "string"}, "tos": {"optional": 1, "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/acme/account/{name}` <a href="#api-cluster-acme-account-name-9ef4bf1c-put" id="api-cluster-acme-account-name-9ef4bf1c-put"></a>

向 CA 更新现有 ACME 账户信息。注意：不指定任何新账户信息会触发刷新。

**方法标识：** `update_account`

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-acme-account-name-9ef4bf1c-put-parameters" id="api-cluster-acme-account-name-9ef4bf1c-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `contact` | 类型：string；必填：否；默认值：—<br>联系电子邮件地址。 |
| `name` | 类型：string；必填：否；默认值："default"<br>ACME 账户配置文件名。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "contact": {"description": "联系电子邮件地址。", "format": "email-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "name": {
      "default": "default", "description": "ACME 账户配置文件名。", "format": "pve-configid", "format_description": "name", "optional": 1, "type": "string",
      "typetext": "<name>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-account-name-9ef4bf1c-put-returns" id="api-cluster-acme-account-name-9ef4bf1c-put-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/account/{name})。

## `/cluster/acme/tos` <a href="#api-cluster-acme-tos-55372fea" id="api-cluster-acme-tos-55372fea"></a>

原始接口路径：`/cluster/acme/tos`。

### GET `/cluster/acme/tos` <a href="#api-cluster-acme-tos-55372fea-get" id="api-cluster-acme-tos-55372fea-get"></a>

从 CA 获取 ACME 服务条款 URL。已弃用，请使用 /cluster/acme/meta.

**方法标识：** `get_tos`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-acme-tos-55372fea-get-parameters" id="api-cluster-acme-tos-55372fea-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `directory` | 类型：string；必填：否；默认值："https://acme-v02.api.letsencrypt.org/directory"<br>ACME CA 目录端点的 URL。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory", "description": "ACME CA 目录端点的 URL。", "optional": 1, "pattern": "^https?://.*",
      "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-tos-55372fea-get-returns" id="api-cluster-acme-tos-55372fea-get-returns"></a>

```text
{"description": "ACME 服务条款 URL。", "optional": 1, "type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/tos)。

## `/cluster/acme/meta` <a href="#api-cluster-acme-meta-2e3ea328" id="api-cluster-acme-meta-2e3ea328"></a>

原始接口路径：`/cluster/acme/meta`。

### GET `/cluster/acme/meta` <a href="#api-cluster-acme-meta-2e3ea328-get" id="api-cluster-acme-meta-2e3ea328-get"></a>

获取 ACME 目录元信息

**方法标识：** `get_meta`

**权限**

```text
{"check": ["perm", "/nodes/{node}", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-acme-meta-2e3ea328-get-parameters" id="api-cluster-acme-meta-2e3ea328-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `directory` | 类型：string；必填：否；默认值："https://acme-v02.api.letsencrypt.org/directory"<br>ACME CA 目录端点的 URL。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "directory": {
      "default": "https://acme-v02.api.letsencrypt.org/directory", "description": "ACME CA 目录端点的 URL。", "optional": 1, "pattern": "^https?://.*",
      "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-acme-meta-2e3ea328-get-returns" id="api-cluster-acme-meta-2e3ea328-get-returns"></a>

```text
{
  "additionalProperties": 1,
  "properties": {
    "caaIdentities": {"description": "指向 ACME 服务器的主机名。", "items": {"type": "string"}, "optional": 1, "type": "array"},
    "externalAccountRequired": {"description": "需要 EAB", "optional": 1, "type": "boolean"},
    "termsOfService": {"description": "ACME 服务条款 URL。", "optional": 1, "type": "string"},
    "website": {"description": "指向 ACME 服务器更多信息的 URL。", "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/meta)。

## `/cluster/acme/directories` <a href="#api-cluster-acme-directories-97ae9688" id="api-cluster-acme-directories-97ae9688"></a>

原始接口路径：`/cluster/acme/directories`。

### GET `/cluster/acme/directories` <a href="#api-cluster-acme-directories-97ae9688-get" id="api-cluster-acme-directories-97ae9688-get"></a>

获取具有名称的已知 ACME 目录端点。

**方法标识：** `get_directories`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-acme-directories-97ae9688-get-parameters" id="api-cluster-acme-directories-97ae9688-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-acme-directories-97ae9688-get-returns" id="api-cluster-acme-directories-97ae9688-get-returns"></a>

```text
{
  "items": {
    "additionalProperties": 0,
    "properties": {"name": {"type": "string"}, "url": {"description": "ACME CA 目录端点的 URL。", "pattern": "^https?://.*", "type": "string"}},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/directories)。

## `/cluster/acme/challenge-schema` <a href="#api-cluster-acme-challenge-schema-3a19ea02" id="api-cluster-acme-challenge-schema-3a19ea02"></a>

原始接口路径：`/cluster/acme/challenge-schema`。

### GET `/cluster/acme/challenge-schema` <a href="#api-cluster-acme-challenge-schema-3a19ea02-get" id="api-cluster-acme-challenge-schema-3a19ea02-get"></a>

获取 ACME 质询类型的模式。

**方法标识：** `challengeschema`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-acme-challenge-schema-3a19ea02-get-parameters" id="api-cluster-acme-challenge-schema-3a19ea02-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-acme-challenge-schema-3a19ea02-get-returns" id="api-cluster-acme-challenge-schema-3a19ea02-get-returns"></a>

```text
{
  "items": {
    "additionalProperties": 0,
    "properties": {
      "id": {"type": "string"}, "name": {"description": "人类可读的名称，缺省时使用 id", "type": "string"}, "schema": {"type": "object"},
      "type": {"type": "string"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/challenge-schema)。

## `/cluster/ceph` <a href="#api-cluster-ceph-64b903a5" id="api-cluster-ceph-64b903a5"></a>

原始接口路径：`/cluster/ceph`。

### GET `/cluster/ceph` <a href="#api-cluster-ceph-64b903a5-get" id="api-cluster-ceph-64b903a5-get"></a>

集群 ceph 索引。

**方法标识：** `cephindex`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-ceph-64b903a5-get-parameters" id="api-cluster-ceph-64b903a5-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ceph-64b903a5-get-returns" id="api-cluster-ceph-64b903a5-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph)。

## `/cluster/ceph/metadata` <a href="#api-cluster-ceph-metadata-87462e1f" id="api-cluster-ceph-metadata-87462e1f"></a>

原始接口路径：`/cluster/ceph/metadata`。

### GET `/cluster/ceph/metadata` <a href="#api-cluster-ceph-metadata-87462e1f-get" id="api-cluster-ceph-metadata-87462e1f-get"></a>

获取 ceph 元数据。

**方法标识：** `metadata`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit", "Datastore.Audit"], "any", 1]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-metadata-87462e1f-get-parameters" id="api-cluster-ceph-metadata-87462e1f-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `scope` | 类型：string；必填：否；默认值："all"<br>要返回的元数据类别：'all' 在每个守护进程的元数据中加入 PVE 端的服务状态（单元、数据目录是否存在）；'versions' 仅收集各节点的 Ceph 二进制程序版本数据。；可选值：`all`, `versions` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "scope": {
      "default": "all",
      "description": "要返回的元数据类别：'all' 在每个守护进程的元数据中加入 PVE 端的服务状态（单元、数据目录是否存在）；'versions' 仅收集各节点的 Ceph 二进制程序版本数据。",
      "enum": ["all", "versions"], "optional": 1, "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ceph-metadata-87462e1f-get-returns" id="api-cluster-ceph-metadata-87462e1f-get-returns"></a>

```text
{
  "description": "每种服务类型的条目，包含各实例的对象。",
  "properties": {
    "mds": {
      "additionalProperties": {
        "additionalProperties": 1, "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "addr": {"description": "绑定地址和端口。", "optional": 1, "type": "string"},
          "ceph_release": {"description": "当前使用的 Ceph 发行版代号。", "type": "string"},
          "ceph_version": {"description": "服务当前使用的版本信息。", "type": "string"},
          "ceph_version_short": {"description": "服务当前使用的简短版本（数字）信息。", "type": "string"},
          "hostname": {"description": "运行此服务的主机名。", "type": "string"},
          "mem_swap_kb": {"description": "此服务当前位于交换空间中的内存。", "type": "integer"},
          "mem_total_kb": {"description": "此服务的内存用量。", "type": "integer"}, "name": {"description": "服务实例名称。", "optional": 1, "type": "string"}
        },
        "type": "object"
      },
      "description": "集群中配置的元数据服务器及其属性，以 '<name>@<host>' 为键。", "type": "object"
    },
    "mgr": {
      "additionalProperties": {
        "additionalProperties": 1, "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "addr": {"description": "绑定地址。", "optional": 1, "type": "string"},
          "ceph_release": {"description": "当前使用的 Ceph 发行版代号。", "type": "string"},
          "ceph_version": {"description": "服务当前使用的版本信息。", "type": "string"},
          "ceph_version_short": {"description": "服务当前使用的简短版本（数字）信息。", "type": "string"},
          "hostname": {"description": "运行此服务的主机名。", "type": "string"},
          "mem_swap_kb": {"description": "此服务当前位于交换空间中的内存。", "type": "integer"},
          "mem_total_kb": {"description": "此服务的内存用量。", "type": "integer"}, "name": {"description": "服务实例名称。", "optional": 1, "type": "string"}
        },
        "type": "object"
      },
      "description": "集群中配置的管理器及其属性，以 '<name>@<host>' 为键。", "type": "object"
    },
    "mon": {
      "additionalProperties": {
        "additionalProperties": 1, "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "addrs": {"description": "绑定地址和端口。", "optional": 1, "type": "string"},
          "ceph_release": {"description": "当前使用的 Ceph 发行版代号。", "type": "string"},
          "ceph_version": {"description": "服务当前使用的版本信息。", "type": "string"},
          "ceph_version_short": {"description": "服务当前使用的简短版本（数字）信息。", "type": "string"},
          "hostname": {"description": "运行此服务的主机名。", "type": "string"},
          "mem_swap_kb": {"description": "此服务当前位于交换空间中的内存。", "type": "integer"},
          "mem_total_kb": {"description": "此服务的内存用量。", "type": "integer"}, "name": {"description": "服务实例名称。", "optional": 1, "type": "string"}
        },
        "type": "object"
      },
      "description": "集群中配置的监视器及其属性，以 '<name>@<host>' 为键。", "type": "object"
    },
    "node": {
      "additionalProperties": {
        "additionalProperties": 1,
        "properties": {
          "buildcommit": {"description": "构建所用的 GIT 提交。", "type": "string"},
          "version": {
            "description": "版本信息。",
            "properties": {
              "parts": {"description": "主版本号、次版本号和补丁版本号。", "items": {"description": "版本组成部分字符串。", "type": "string"}, "type": "array"},
              "str": {"description": "以单个字符串表示的版本。", "type": "string"}
            },
            "type": "object"
          }
        },
        "type": "object"
      },
      "description": "节点上安装的 Ceph 版本，以节点名称为键。", "type": "object"
    },
    "osd": {
      "description": "集群中配置的 OSD 及其属性。",
      "items": {
        "description": "列出了一些有用的属性，并非完整列表。",
        "properties": {
          "back_addr": {"description": "OSD 之间后端流量的绑定地址和端口。", "type": "string"},
          "ceph_release": {"description": "当前使用的 Ceph 发行版代号。", "type": "string"},
          "ceph_version": {"description": "服务当前使用的版本信息。", "type": "string"},
          "ceph_version_short": {"description": "服务当前使用的简短版本（数字）信息。", "type": "string"},
          "device_ids": {"description": "以逗号连接的设备标识符列表（例如 'sdb=<serial>,sdc=<serial>'）。", "optional": 1, "type": "string"},
          "device_paths": {"description": "底层设备的 /dev/disk/by-path 条目列表，以逗号连接。", "optional": 1, "type": "string"},
          "devices": {"description": "以逗号连接的底层设备名称列表（例如 'sdb,sdc'）。", "optional": 1, "type": "string"},
          "front_addr": {"description": "到 OSD 的前端流量的绑定地址和端口。", "type": "string"},
          "hostname": {"description": "运行此服务的主机名。", "type": "string"}, "id": {"description": "OSD ID。", "type": "integer"},
          "mem_swap_kb": {"description": "此服务当前位于交换空间中的内存。", "type": "integer"},
          "mem_total_kb": {"description": "此服务的内存用量。", "type": "integer"}, "osd_data": {"description": "OSD 数据目录的路径。", "type": "string"},
          "osd_objectstore": {"description": "OSD 对象存储类型。", "type": "string"}
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/metadata)。

## `/cluster/ceph/status` <a href="#api-cluster-ceph-status-a80fb0bc" id="api-cluster-ceph-status-a80fb0bc"></a>

原始接口路径：`/cluster/ceph/status`。

### GET `/cluster/ceph/status` <a href="#api-cluster-ceph-status-a80fb0bc-get" id="api-cluster-ceph-status-a80fb0bc-get"></a>

获取 ceph 状态。

**方法标识：** `status`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit", "Datastore.Audit"], "any", 1]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-status-a80fb0bc-get-parameters" id="api-cluster-ceph-status-a80fb0bc-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ceph-status-a80fb0bc-get-returns" id="api-cluster-ceph-status-a80fb0bc-get-returns"></a>

```text
{"type": "object"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/status)。

## `/cluster/ceph/restart-bulk` <a href="#api-cluster-ceph-restart-bulk-c7351887" id="api-cluster-ceph-restart-bulk-c7351887"></a>

原始接口路径：`/cluster/ceph/restart-bulk`。

### POST `/cluster/ceph/restart-bulk` <a href="#api-cluster-ceph-restart-bulk-c7351887-post" id="api-cluster-ceph-restart-bulk-c7351887-post"></a>

在整个集群中滚动重启给定类型的所有 Ceph 守护进程。对于 MON/MGR/MDS，只有在 Ceph 报告上一个守护进程已恢复运行且下一个可以安全停止后，才会重启该守护进程。对于 OSD，集群路径会依次编排各节点上的 /nodes/{node}/ceph/restart-bulk 节点级端点，沿用该端点的每个 OSD 的 'noout' 处理和恢复执行支持。此端点不直接提供 'noout' 标志，因为它仅适用于 OSD（对于 OSD，由各节点子任务处理）。

**方法标识：** `restart_bulk`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-restart-bulk-c7351887-post-parameters" id="api-cluster-ceph-restart-bulk-c7351887-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `dry-run` | 类型：boolean；必填：否；默认值：0<br>记录计划（将重启哪些守护进程及其顺序），但不执行实际操作。 |
| `force` | 类型：boolean；必填：否；默认值：0<br>对于带有非良性检查的 HEALTH_WARN，例如 PG_DEGRADED、SLOW_OPS 或 MON_DOWN，继续执行。无论此标志如何，阻塞性 HEALTH_ERR 都是致命错误。ceph 报告为已静默的检查以及已知对滚动重启无害的检查永远不会阻塞操作，并会在任务日志中列明。集群范围的 OSD 映射标志仅在重启 OSD 时才会评估，因为重启 mon、mgr 或 mds 不会涉及其控制的内容。操作人员有责任确认集群足够稳定，能够承受滚动重启。 |
| `only-outdated` | 类型：boolean；必填：否；默认值：0<br>仅适用于 OSD：只重启运行版本与其宿主机本地安装的 ceph-osd 二进制程序版本不同的 OSD。此选项会传递到每个节点级子任务，以使用各宿主机安装的版本（可正确处理某个宿主机采用较新构建版本的部分升级情形）。 |
| `service-type` | 类型：string；必填：是；默认值：—<br>要在整个集群中重启的 Ceph 守护进程类型。；可选值：`mon`, `mgr`, `mds`, `osd` |
| `timeout` | 类型：integer；必填：否；默认值：600<br>每个守护进程等待上线阶段的超时时间（秒）。注意：对于远程节点上的守护进程，同一超时时间也会约束远程重启任务，因此每个守护进程的总时间预算可达此值的 2 倍。默认值考虑了繁忙集群中缓慢的 MDS 日志重放或 MON paxos 稳定过程；如果集群在守护进程重启后通常需要更长时间才能稳定，请增大此值。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0, "description": "记录计划（将重启哪些守护进程及其顺序），但不执行实际操作。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "force": {
      "default": 0,
      "description": "对于带有非良性检查的 HEALTH_WARN，例如 PG_DEGRADED、SLOW_OPS 或 MON_DOWN，继续执行。无论此标志如何，阻塞性 HEALTH_ERR 都是致命错误。ceph 报告为已静默的检查以及已知对滚动重启无害的检查永远不会阻塞操作，并会在任务日志中列明。集群范围的 OSD 映射标志仅在重启 OSD 时才会评估，因为重启 mon、mgr 或 mds 不会涉及其控制的内容。操作人员有责任确认集群足够稳定，能够承受滚动重启。",
      "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "only-outdated": {
      "default": 0,
      "description": "仅适用于 OSD：只重启运行版本与其宿主机本地安装的 ceph-osd 二进制程序版本不同的 OSD。此选项会传递到每个节点级子任务，以使用各宿主机安装的版本（可正确处理某个宿主机采用较新构建版本的部分升级情形）。",
      "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "service-type": {"description": "要在整个集群中重启的 Ceph 守护进程类型。", "enum": ["mon", "mgr", "mds", "osd"], "type": "string"},
    "timeout": {
      "default": 600,
      "description": "每个守护进程等待上线阶段的超时时间（秒）。注意：对于远程节点上的守护进程，同一超时时间也会约束远程重启任务，因此每个守护进程的总时间预算可达此值的 2 倍。默认值考虑了繁忙集群中缓慢的 MDS 日志重放或 MON paxos 稳定过程；如果集群在守护进程重启后通常需要更长时间才能稳定，请增大此值。",
      "maximum": 1800, "minimum": 30, "optional": 1, "type": "integer", "typetext": "<integer> (30 - 1800)"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ceph-restart-bulk-c7351887-post-returns" id="api-cluster-ceph-restart-bulk-c7351887-post-returns"></a>

```text
{"type": "string"}
```

<details>
<summary>其他接口元数据</summary>

```text
{"expose_credentials": 1}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/restart-bulk)。

## `/cluster/ceph/flags` <a href="#api-cluster-ceph-flags-3d19a402" id="api-cluster-ceph-flags-3d19a402"></a>

原始接口路径：`/cluster/ceph/flags`。

### GET `/cluster/ceph/flags` <a href="#api-cluster-ceph-flags-3d19a402-get" id="api-cluster-ceph-flags-3d19a402-get"></a>

获取所有 ceph 标志的状态

**方法标识：** `get_all_flags`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-flags-3d19a402-get-parameters" id="api-cluster-ceph-flags-3d19a402-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ceph-flags-3d19a402-get-returns" id="api-cluster-ceph-flags-3d19a402-get-returns"></a>

```text
{
  "items": {
    "additionalProperties": 1,
    "properties": {
      "description": {"description": "标志描述。", "type": "string"},
      "name": {
        "description": "标志名称。",
        "enum": ["nobackfill", "nodeep-scrub", "nodown", "noin", "noout", "norebalance", "norecover", "noscrub", "notieragent", "noup", "pause"],
        "type": "string"
      },
      "value": {"description": "标志值。", "type": "boolean"}
    },
    "type": "object"
  },
  "links": [{"href": "{name}", "rel": "child"}], "type": "array"
}
```

### PUT `/cluster/ceph/flags` <a href="#api-cluster-ceph-flags-3d19a402-put" id="api-cluster-ceph-flags-3d19a402-put"></a>

一次设置/取消设置多个 Ceph 标志。每个标志都是顶层可选布尔值：传入 true 设置标志，false 取消设置，省略则保留当前状态。以工作任务运行；返回可用于跟踪的 UPID。

**方法标识：** `set_flags`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-flags-3d19a402-put-parameters" id="api-cluster-ceph-flags-3d19a402-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `nobackfill` | 类型：boolean；必填：否；默认值：—<br>暂停 PG 回填。 |
| `nodeep-scrub` | 类型：boolean；必填：否；默认值：—<br>禁用深度清理检查。 |
| `nodown` | 类型：boolean；必填：否；默认值：—<br>忽略 OSD 故障报告，因此监视器不会将 OSD 标记为 down。 |
| `noin` | 类型：boolean；必填：否；默认值：—<br>先前标记为 out 的 OSD 在启动时不会重新标记为 in。 |
| `noout` | 类型：boolean；必填：否；默认值：—<br>OSD 不会在配置的时间间隔后自动标记为 out。 |
| `norebalance` | 类型：boolean；必填：否；默认值：—<br>暂停 PG 重新均衡。 |
| `norecover` | 类型：boolean；必填：否；默认值：—<br>暂停 PG 恢复。 |
| `noscrub` | 类型：boolean；必填：否；默认值：—<br>禁用清理检查。 |
| `notieragent` | 类型：boolean；必填：否；默认值：—<br>暂停缓存分层活动。 |
| `noup` | 类型：boolean；必填：否；默认值：—<br>不允许 OSD 启动。 |
| `pause` | 类型：boolean；必填：否；默认值：—<br>暂停读写。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "nobackfill": {"description": "暂停 PG 回填。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "nodeep-scrub": {"description": "禁用深度清理检查。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "nodown": {"description": "忽略 OSD 故障报告，因此监视器不会将 OSD 标记为 down。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "noin": {"description": "先前标记为 out 的 OSD 在启动时不会重新标记为 in。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "noout": {"description": "OSD 不会在配置的时间间隔后自动标记为 out。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "norebalance": {"description": "暂停 PG 重新均衡。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "norecover": {"description": "暂停 PG 恢复。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "noscrub": {"description": "禁用清理检查。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "notieragent": {"description": "暂停缓存分层活动。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "noup": {"description": "不允许 OSD 启动。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "pause": {"description": "暂停读写。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ceph-flags-3d19a402-put-returns" id="api-cluster-ceph-flags-3d19a402-put-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/flags)。

## `/cluster/ceph/flags/{flag}` <a href="#api-cluster-ceph-flags-flag-16233181" id="api-cluster-ceph-flags-flag-16233181"></a>

原始接口路径：`/cluster/ceph/flags/{flag}`。

### GET `/cluster/ceph/flags/{flag}` <a href="#api-cluster-ceph-flags-flag-16233181-get" id="api-cluster-ceph-flags-flag-16233181-get"></a>

获取特定 ceph 标志的状态。

**方法标识：** `get_flag`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-flags-flag-16233181-get-parameters" id="api-cluster-ceph-flags-flag-16233181-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `flag` | 类型：string；必填：是；默认值：—<br>要获取的标志名称。；可选值：`nobackfill`, `nodeep-scrub`, `nodown`, `noin`, `noout`, `norebalance`, `norecover`, `noscrub`, `notieragent`, `noup`, `pause` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "flag": {
      "description": "要获取的标志名称。",
      "enum": ["nobackfill", "nodeep-scrub", "nodown", "noin", "noout", "norebalance", "norecover", "noscrub", "notieragent", "noup", "pause"], "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ceph-flags-flag-16233181-get-returns" id="api-cluster-ceph-flags-flag-16233181-get-returns"></a>

```text
{"type": "boolean"}
```

### PUT `/cluster/ceph/flags/{flag}` <a href="#api-cluster-ceph-flags-flag-16233181-put" id="api-cluster-ceph-flags-flag-16233181-put"></a>

设置或清除（取消设置）特定 Ceph 标志。同步运行（不同于会派生工作任务的批量 PUT /cluster/ceph/flags 端点）。

**方法标识：** `update_flag`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-flags-flag-16233181-put-parameters" id="api-cluster-ceph-flags-flag-16233181-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `flag` | 类型：string；必填：是；默认值：—<br>要更新的 ceph 标志；可选值：`nobackfill`, `nodeep-scrub`, `nodown`, `noin`, `noout`, `norebalance`, `norecover`, `noscrub`, `notieragent`, `noup`, `pause` |
| `value` | 类型：boolean；必填：是；默认值：—<br>标志的新值 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "flag": {
      "description": "要更新的 ceph 标志",
      "enum": ["nobackfill", "nodeep-scrub", "nodown", "noin", "noout", "norebalance", "norecover", "noscrub", "notieragent", "noup", "pause"], "type": "string"
    },
    "value": {"description": "标志的新值", "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ceph-flags-flag-16233181-put-returns" id="api-cluster-ceph-flags-flag-16233181-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/flags/{flag})。

## `/cluster/ceph/health-mute` <a href="#api-cluster-ceph-health-mute-285ae4b0" id="api-cluster-ceph-health-mute-285ae4b0"></a>

原始接口路径：`/cluster/ceph/health-mute`。

### GET `/cluster/ceph/health-mute` <a href="#api-cluster-ceph-health-mute-285ae4b0-get" id="api-cluster-ceph-health-mute-285ae4b0-get"></a>

获取当前已静默的 Ceph 健康检查。

**方法标识：** `health_mute_index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit", "Datastore.Audit"], "any", 1]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-health-mute-285ae4b0-get-parameters" id="api-cluster-ceph-health-mute-285ae4b0-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-ceph-health-mute-285ae4b0-get-returns" id="api-cluster-ceph-health-mute-285ae4b0-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "code": {"description": "已静默的健康检查。", "type": "string"}, "sticky": {"description": "检查情况恶化后是否仍保持静默。", "type": "boolean"},
      "summary": {"description": "检查报告的内容。", "optional": 1, "type": "string"},
      "ttl": {"description": "静默到期时间。若不会到期则不存在此项。", "optional": 1, "type": "string"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/health-mute)。

## `/cluster/ceph/health-mute/{code}` <a href="#api-cluster-ceph-health-mute-code-6c051ab6" id="api-cluster-ceph-health-mute-code-6c051ab6"></a>

原始接口路径：`/cluster/ceph/health-mute/{code}`。

### PUT `/cluster/ceph/health-mute/{code}` <a href="#api-cluster-ceph-health-mute-code-6c051ab6-put" id="api-cluster-ceph-health-mute-code-6c051ab6-put"></a>

静默或取消静默 Ceph 健康检查。静默的检查不再计入集群状态，但仍然可见且会继续评估。

**方法标识：** `health_mute`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-ceph-health-mute-code-6c051ab6-put-parameters" id="api-cluster-ceph-health-mute-code-6c051ab6-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `code` | 类型：string；必填：是；默认值：—<br>要静默的健康检查，使用 'ceph health' 报告的名称，例如 'AUTH_INSECURE_CLIENT_KEY_TYPE'。 |
| `sticky` | 类型：boolean；必填：否；默认值：0<br>即使检查情况恶化也保持静默。若不启用，则受影响条目数量一旦增加，静默便会自动解除，使该检查重新引起注意。仅在静默时使用。 |
| `ttl` | 类型：string；必填：否；默认值：—<br>静默持续时间，例如 '2h'、'3d' 或 '1w'。省略则静默永不过期。仅在静默时使用。 |
| `value` | 类型：boolean；必填：是；默认值：—<br>是静默（true）还是取消静默（false）此检查。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "code": {
      "description": "要静默的健康检查，使用 'ceph health' 报告的名称，例如 'AUTH_INSECURE_CLIENT_KEY_TYPE'。", "maxLength": 64, "pattern": "[A-Z][A-Z0-9_]+",
      "type": "string"
    },
    "sticky": {
      "default": 0, "description": "即使检查情况恶化也保持静默。若不启用，则受影响条目数量一旦增加，静默便会自动解除，使该检查重新引起注意。仅在静默时使用。",
      "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "ttl": {
      "description": "静默持续时间，例如 '2h'、'3d' 或 '1w'。省略则静默永不过期。仅在静默时使用。", "optional": 1,
      "pattern": "\\d+[ \\t]*(?:s|sec|seconds?|m|min|minutes?|h|hr|hours?|d|days?|w|wk|weeks?|mo|months?|y|yr|years?)(?:[ \\t]*\\d+[ \\t]*(?:s|sec|seconds?|m|min|minutes?|h|hr|hours?|d|days?|w|wk|weeks?|mo|months?|y|yr|years?))*(?!\\n)",
      "type": "string"
    },
    "value": {"description": "是静默（true）还是取消静默（false）此检查。", "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-ceph-health-mute-code-6c051ab6-put-returns" id="api-cluster-ceph-health-mute-code-6c051ab6-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/health-mute/{code})。

## `/cluster/jobs` <a href="#api-cluster-jobs-7f6abac7" id="api-cluster-jobs-7f6abac7"></a>

原始接口路径：`/cluster/jobs`。

### GET `/cluster/jobs` <a href="#api-cluster-jobs-7f6abac7-get" id="api-cluster-jobs-7f6abac7-get"></a>

作业相关端点的索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-jobs-7f6abac7-get-parameters" id="api-cluster-jobs-7f6abac7-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-jobs-7f6abac7-get-returns" id="api-cluster-jobs-7f6abac7-get-returns"></a>

```text
{
  "description": "目录索引。", "items": {"properties": {"subdir": {"description": "API 子目录端点", "type": "string"}}, "type": "object"},
  "links": [{"href": "{subdir}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs)。

## `/cluster/jobs/realm-sync` <a href="#api-cluster-jobs-realm-sync-3a48aec7" id="api-cluster-jobs-realm-sync-3a48aec7"></a>

原始接口路径：`/cluster/jobs/realm-sync`。

### GET `/cluster/jobs/realm-sync` <a href="#api-cluster-jobs-realm-sync-3a48aec7-get" id="api-cluster-jobs-realm-sync-3a48aec7-get"></a>

列出已配置的 realm-sync 作业。

**方法标识：** `syncjob_index`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-jobs-realm-sync-3a48aec7-get-parameters" id="api-cluster-jobs-realm-sync-3a48aec7-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-jobs-realm-sync-3a48aec7-get-returns" id="api-cluster-jobs-realm-sync-3a48aec7-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"description": "作业注释。", "optional": 1, "type": "string"}, "enabled": {"description": "作业是否启用。", "type": "boolean"},
      "id": {"description": "条目的 ID。", "type": "string"},
      "last-run": {"description": "作业上次执行时间，以自 UNIX 纪元起的秒数表示", "optional": 1, "type": "integer"},
      "next-run": {"description": "作业下次计划执行时间，以自 UNIX 纪元起的秒数表示。", "optional": 1, "type": "integer"},
      "realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string"},
      "remove-vanished": {
        "default": "none",
        "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
        "optional": "1", "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none", "type": "string",
        "typetext": "([acl];[properties];[entry])|none"
      },
      "schedule": {"description": "已配置的同步计划。", "type": "string"},
      "scope": {"description": "选择要同步的内容。", "enum": ["users", "groups", "both"], "optional": "1", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/realm-sync)。

## `/cluster/jobs/realm-sync/{id}` <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5" id="api-cluster-jobs-realm-sync-id-2c5d49d5"></a>

原始接口路径：`/cluster/jobs/realm-sync/{id}`。

### DELETE `/cluster/jobs/realm-sync/{id}` <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-delete" id="api-cluster-jobs-realm-sync-id-2c5d49d5-delete"></a>

删除 realm-sync 作业定义。

**方法标识：** `delete_job`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-delete-parameters" id="api-cluster-jobs-realm-sync-id-2c5d49d5-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-delete-returns" id="api-cluster-jobs-realm-sync-id-2c5d49d5-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/jobs/realm-sync/{id}` <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-get" id="api-cluster-jobs-realm-sync-id-2c5d49d5-get"></a>

读取 realm-sync 作业定义。

**方法标识：** `read_job`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-get-parameters" id="api-cluster-jobs-realm-sync-id-2c5d49d5-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-get-returns" id="api-cluster-jobs-realm-sync-id-2c5d49d5-get-returns"></a>

```text
{"type": "object"}
```

### POST `/cluster/jobs/realm-sync/{id}` <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-post" id="api-cluster-jobs-realm-sync-id-2c5d49d5-post"></a>

创建新的 realm-sync 作业。

**方法标识：** `create_job`

**权限**

```text
{
  "check": ["and", ["perm", "/access/realm/{realm}", ["Realm.AllocateUser"]], ["perm", "/access/groups", ["User.Modify"]]],
  "description": "需要对 '/access/realm/<realm>' 的 'Realm.AllocateUser' 权限以及对 '/access/groups/' 的 'User.Modify' 权限。"
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-post-parameters" id="api-cluster-jobs-realm-sync-id-2c5d49d5-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>作业描述。 |
| `enable-new` | 类型：boolean；必填：否；默认值："1"<br>立即启用新同步的用户。 |
| `enabled` | 类型：boolean；必填：否；默认值：1<br>确定是否启用作业。 |
| `id` | 类型：string；必填：是；默认值：—<br>作业 ID。 |
| `realm` | 类型：string；必填：否；默认值：—<br>认证域 ID |
| `remove-vanished` | 类型：string；必填：否；默认值："none"<br>以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。 |
| `schedule` | 类型：string；必填：是；默认值：—<br>备份计划。格式是 `systemd` 日历事件的子集。 |
| `scope` | 类型：string；必填：否；默认值：—<br>选择要同步的内容。；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "作业描述。", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"},
    "enable-new": {"default": "1", "description": "立即启用新同步的用户。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "enabled": {"default": 1, "description": "确定是否启用作业。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "作业 ID。", "format": "pve-configid", "maxLength": 64, "type": "string", "typetext": "<string>"},
    "realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "optional": 1, "type": "string", "typetext": "<string>"},
    "remove-vanished": {
      "default": "none",
      "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
      "optional": 1, "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none", "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "type": "string", "typetext": "<string>"
    },
    "scope": {"description": "选择要同步的内容。", "enum": ["users", "groups", "both"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-post-returns" id="api-cluster-jobs-realm-sync-id-2c5d49d5-post-returns"></a>

```text
{"type": "null"}
```

### PUT `/cluster/jobs/realm-sync/{id}` <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-put" id="api-cluster-jobs-realm-sync-id-2c5d49d5-put"></a>

更新 realm-sync 作业定义。

**方法标识：** `update_job`

**权限**

```text
{
  "check": ["and", ["perm", "/access/realm/{realm}", ["Realm.AllocateUser"]], ["perm", "/access/groups", ["User.Modify"]]],
  "description": "需要对 '/access/realm/<realm>' 的 'Realm.AllocateUser' 权限以及对 '/access/groups/' 的 'User.Modify' 权限。"
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-put-parameters" id="api-cluster-jobs-realm-sync-id-2c5d49d5-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br>作业描述。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `enable-new` | 类型：boolean；必填：否；默认值："1"<br>立即启用新同步的用户。 |
| `enabled` | 类型：boolean；必填：否；默认值：1<br>确定是否启用作业。 |
| `id` | 类型：string；必填：是；默认值：—<br>作业 ID。 |
| `remove-vanished` | 类型：string；必填：否；默认值："none"<br>以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。 |
| `schedule` | 类型：string；必填：是；默认值：—<br>备份计划。格式是 `systemd` 日历事件的子集。 |
| `scope` | 类型：string；必填：否；默认值：—<br>选择要同步的内容。；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"description": "作业描述。", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "enable-new": {"default": "1", "description": "立即启用新同步的用户。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "enabled": {"default": 1, "description": "确定是否启用作业。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "作业 ID。", "format": "pve-configid", "maxLength": 64, "type": "string", "typetext": "<string>"},
    "remove-vanished": {
      "default": "none",
      "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
      "optional": 1, "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none", "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "type": "string", "typetext": "<string>"
    },
    "scope": {"description": "选择要同步的内容。", "enum": ["users", "groups", "both"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-jobs-realm-sync-id-2c5d49d5-put-returns" id="api-cluster-jobs-realm-sync-id-2c5d49d5-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/realm-sync/{id})。

## `/cluster/jobs/schedule-analyze` <a href="#api-cluster-jobs-schedule-analyze-1c086080" id="api-cluster-jobs-schedule-analyze-1c086080"></a>

原始接口路径：`/cluster/jobs/schedule-analyze`。

### GET `/cluster/jobs/schedule-analyze` <a href="#api-cluster-jobs-schedule-analyze-1c086080-get" id="api-cluster-jobs-schedule-analyze-1c086080-get"></a>

返回未来计划运行时间的列表。

**方法标识：** `schedule-analyze`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-jobs-schedule-analyze-1c086080-get-parameters" id="api-cluster-jobs-schedule-analyze-1c086080-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `iterations` | 类型：integer；必填：否；默认值：10<br>要模拟并返回的事件迭代次数。 |
| `schedule` | 类型：string；必填：是；默认值：—<br>作业计划。格式是 `systemd` 日历事件的子集。 |
| `starttime` | 类型：integer；必填：否；默认值：—<br>计算起始时间的 UNIX 时间戳。默认为当前时间。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "iterations": {
      "default": 10, "description": "要模拟并返回的事件迭代次数。", "maximum": 100, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 100)"
    },
    "schedule": {
      "description": "作业计划。格式是 `systemd` 日历事件的子集。", "format": "pve-calendar-event", "maxLength": 128, "type": "string", "typetext": "<string>"
    },
    "starttime": {"description": "计算起始时间的 UNIX 时间戳。默认为当前时间。", "optional": 1, "type": "integer", "typetext": "<integer>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-jobs-schedule-analyze-1c086080-get-returns" id="api-cluster-jobs-schedule-analyze-1c086080-get-returns"></a>

```text
{
  "description": "自 <starttime> 起接下来 <iterations> 次事件的数组。",
  "items": {
    "properties": {
      "timestamp": {"description": "运行时间的 UNIX 时间戳。", "type": "integer"}, "utc": {"description": "运行时间的 UTC 时间戳。", "type": "string"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/schedule-analyze)。

## `/cluster/mapping` <a href="#api-cluster-mapping-3795482f" id="api-cluster-mapping-3795482f"></a>

原始接口路径：`/cluster/mapping`。

### GET `/cluster/mapping` <a href="#api-cluster-mapping-3795482f-get" id="api-cluster-mapping-3795482f-get"></a>

列出资源类型。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-mapping-3795482f-get-parameters" id="api-cluster-mapping-3795482f-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-mapping-3795482f-get-returns" id="api-cluster-mapping-3795482f-get-returns"></a>

```text
{"items": {"type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping)。

## `/cluster/mapping/dir` <a href="#api-cluster-mapping-dir-be5cae7e" id="api-cluster-mapping-dir-be5cae7e"></a>

原始接口路径：`/cluster/mapping/dir`。

### GET `/cluster/mapping/dir` <a href="#api-cluster-mapping-dir-be5cae7e-get" id="api-cluster-mapping-dir-be5cae7e-get"></a>

列出目录映射

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/mapping/dir/<id>' 具有 'Mapping.Modify'、'Mapping.Use' 或 'Mapping.Audit' 权限的条目。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-mapping-dir-be5cae7e-get-parameters" id="api-cluster-mapping-dir-be5cae7e-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `check-node` | 类型：string；必填：否；默认值：—<br>如果指定，则检查给定节点上的配置是否正确，并将与该目录相关的诊断信息加入响应。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "如果指定，则检查给定节点上的配置是否正确，并将与该目录相关的诊断信息加入响应。", "format": "pve-node", "optional": 1, "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-dir-be5cae7e-get-returns" id="api-cluster-mapping-dir-be5cae7e-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "checks": {
        "description": "检查列表，仅在设置了 'check-node' 时存在。",
        "items": {
          "properties": {
            "message": {"description": "错误消息", "type": "string"},
            "severity": {"description": "错误严重程度", "enum": ["warning", "error"], "type": "string"}
          },
          "type": "object"
        },
        "optional": 1, "type": "array"
      },
      "description": {"description": "逻辑映射的描述。", "type": "string"}, "id": {"description": "映射的逻辑 ID。", "type": "string"},
      "map": {"description": "映射条目。", "items": {"description": "节点的映射。", "type": "string"}, "type": "array"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/mapping/dir` <a href="#api-cluster-mapping-dir-be5cae7e-post" id="api-cluster-mapping-dir-be5cae7e-post"></a>

创建新的目录映射。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/mapping/dir", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-dir-be5cae7e-post-parameters" id="api-cluster-mapping-dir-be5cae7e-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `description` | 类型：string；必填：否；默认值：—<br>目录映射的描述 |
| `id` | 类型：string；必填：是；默认值：—<br>目录映射的 ID |
| `map` | 类型：array；必填：是；默认值：—<br>集群节点的映射列表。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "description": {"description": "目录映射的描述", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "id": {"description": "目录映射的 ID", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "path": {"description": "应与客户机共享的目录的绝对路径。", "format": "pve-storage-path-in-property-string", "type": "string"}
        },
        "type": "string"
      },
      "optional": 0, "type": "array", "typetext": "<array>"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-dir-be5cae7e-post-returns" id="api-cluster-mapping-dir-be5cae7e-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/dir)。

## `/cluster/mapping/dir/{id}` <a href="#api-cluster-mapping-dir-id-e3e8b099" id="api-cluster-mapping-dir-id-e3e8b099"></a>

原始接口路径：`/cluster/mapping/dir/{id}`。

### DELETE `/cluster/mapping/dir/{id}` <a href="#api-cluster-mapping-dir-id-e3e8b099-delete" id="api-cluster-mapping-dir-id-e3e8b099-delete"></a>

移除目录映射。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/mapping/dir", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-dir-id-e3e8b099-delete-parameters" id="api-cluster-mapping-dir-id-e3e8b099-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-dir-id-e3e8b099-delete-returns" id="api-cluster-mapping-dir-id-e3e8b099-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/mapping/dir/{id}` <a href="#api-cluster-mapping-dir-id-e3e8b099-get" id="api-cluster-mapping-dir-id-e3e8b099-get"></a>

获取目录映射。

**方法标识：** `get`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/dir/{id}", ["Mapping.Use"]], ["perm", "/mapping/dir/{id}", ["Mapping.Modify"]], ["perm", "/mapping/dir/{id}", ["Mapping.Audit"]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-dir-id-e3e8b099-get-parameters" id="api-cluster-mapping-dir-id-e3e8b099-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-dir-id-e3e8b099-get-returns" id="api-cluster-mapping-dir-id-e3e8b099-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/mapping/dir/{id}` <a href="#api-cluster-mapping-dir-id-e3e8b099-put" id="api-cluster-mapping-dir-id-e3e8b099-put"></a>

更新目录映射。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/mapping/dir/{id}", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-dir-id-e3e8b099-put-parameters" id="api-cluster-mapping-dir-id-e3e8b099-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `description` | 类型：string；必填：否；默认值：—<br>目录映射的描述 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `id` | 类型：string；必填：是；默认值：—<br>目录映射的 ID |
| `map` | 类型：array；必填：否；默认值：—<br>集群节点的映射列表。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "description": {"description": "目录映射的描述", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "id": {"description": "目录映射的 ID", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "path": {"description": "应与客户机共享的目录的绝对路径。", "format": "pve-storage-path-in-property-string", "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-dir-id-e3e8b099-put-returns" id="api-cluster-mapping-dir-id-e3e8b099-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/dir/{id})。

## `/cluster/mapping/pci` <a href="#api-cluster-mapping-pci-a7aadf85" id="api-cluster-mapping-pci-a7aadf85"></a>

原始接口路径：`/cluster/mapping/pci`。

### GET `/cluster/mapping/pci` <a href="#api-cluster-mapping-pci-a7aadf85-get" id="api-cluster-mapping-pci-a7aadf85-get"></a>

列出 PCI 硬件映射

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/mapping/pci/<id>' 具有 'Mapping.Modify'、'Mapping.Use' 或 'Mapping.Audit' 权限的条目。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-mapping-pci-a7aadf85-get-parameters" id="api-cluster-mapping-pci-a7aadf85-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `check-node` | 类型：string；必填：否；默认值：—<br>如果指定，则检查给定节点上的配置是否正确，并将与设备相关的诊断信息加入响应。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "如果指定，则检查给定节点上的配置是否正确，并将与设备相关的诊断信息加入响应。", "format": "pve-node", "optional": 1, "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-pci-a7aadf85-get-returns" id="api-cluster-mapping-pci-a7aadf85-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "checks": {
        "description": "检查列表，仅在设置了 'check_node' 时存在。",
        "items": {
          "properties": {
            "message": {"description": "错误消息", "type": "string"},
            "severity": {"description": "错误严重程度", "enum": ["warning", "error"], "type": "string"}
          },
          "type": "object"
        },
        "optional": 1, "type": "array"
      },
      "description": {"description": "逻辑映射的描述。", "type": "string"}, "id": {"description": "映射的逻辑 ID。", "type": "string"},
      "map": {"description": "映射条目。", "items": {"description": "节点的映射。", "type": "string"}, "type": "array"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/mapping/pci` <a href="#api-cluster-mapping-pci-a7aadf85-post" id="api-cluster-mapping-pci-a7aadf85-post"></a>

创建新的硬件映射。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/mapping/pci", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-pci-a7aadf85-post-parameters" id="api-cluster-mapping-pci-a7aadf85-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `description` | 类型：string；必填：否；默认值：—<br>逻辑 PCI 设备的描述。 |
| `id` | 类型：string；必填：是；默认值：—<br>逻辑 PCI 映射的 ID。 |
| `live-migration-capable` | 类型：boolean；必填：否；默认值：0<br>将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。 |
| `map` | 类型：array；必填：是；默认值：—<br>集群节点的映射列表。 |
| `mdev` | 类型：boolean；必填：否；默认值：0<br>将设备标记为能够提供中介设备。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "description": {"description": "逻辑 PCI 设备的描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "id": {"description": "逻辑 PCI 映射的 ID。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "live-migration-capable": {
      "default": 0, "description": "将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "description": {"description": "节点特定设备的描述。", "maxLength": 4096, "optional": 1, "type": "string"},
          "id": {"description": "预期的供应商和设备 ID。用于检测硬件变化", "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)", "type": "string"},
          "iommugroup": {"description": "预期设备所在的 IOMMU 组。用于检测硬件变化。", "optional": 1, "type": "integer"},
          "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "path": {
            "description": "设备路径。如果省略功能号，则映射整个设备。此时使用第一个设备的属性。可以提供以分号分隔的多个路径，客户机启动时将选择第一个可用路径。",
            "pattern": "(?:[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?;)*[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?", "type": "string"
          },
          "subsystem-id": {
            "description": "预期的子系统供应商和设备 ID。用于检测硬件变化。", "optional": 1, "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)", "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 0, "type": "array", "typetext": "<array>"
    },
    "mdev": {"default": 0, "description": "将设备标记为能够提供中介设备。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-pci-a7aadf85-post-returns" id="api-cluster-mapping-pci-a7aadf85-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/pci)。

## `/cluster/mapping/pci/{id}` <a href="#api-cluster-mapping-pci-id-80b107bb" id="api-cluster-mapping-pci-id-80b107bb"></a>

原始接口路径：`/cluster/mapping/pci/{id}`。

### DELETE `/cluster/mapping/pci/{id}` <a href="#api-cluster-mapping-pci-id-80b107bb-delete" id="api-cluster-mapping-pci-id-80b107bb-delete"></a>

移除硬件映射。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/mapping/pci", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-pci-id-80b107bb-delete-parameters" id="api-cluster-mapping-pci-id-80b107bb-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-pci-id-80b107bb-delete-returns" id="api-cluster-mapping-pci-id-80b107bb-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/mapping/pci/{id}` <a href="#api-cluster-mapping-pci-id-80b107bb-get" id="api-cluster-mapping-pci-id-80b107bb-get"></a>

获取 PCI 映射。

**方法标识：** `get`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/pci/{id}", ["Mapping.Use"]], ["perm", "/mapping/pci/{id}", ["Mapping.Modify"]], ["perm", "/mapping/pci/{id}", ["Mapping.Audit"]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-pci-id-80b107bb-get-parameters" id="api-cluster-mapping-pci-id-80b107bb-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-pci-id-80b107bb-get-returns" id="api-cluster-mapping-pci-id-80b107bb-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/mapping/pci/{id}` <a href="#api-cluster-mapping-pci-id-80b107bb-put" id="api-cluster-mapping-pci-id-80b107bb-put"></a>

更新硬件映射。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/mapping/pci/{id}", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-pci-id-80b107bb-put-parameters" id="api-cluster-mapping-pci-id-80b107bb-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `description` | 类型：string；必填：否；默认值：—<br>逻辑 PCI 设备的描述。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `id` | 类型：string；必填：是；默认值：—<br>逻辑 PCI 映射的 ID。 |
| `live-migration-capable` | 类型：boolean；必填：否；默认值：0<br>将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。 |
| `map` | 类型：array；必填：否；默认值：—<br>集群节点的映射列表。 |
| `mdev` | 类型：boolean；必填：否；默认值：0<br>将设备标记为能够提供中介设备。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "description": {"description": "逻辑 PCI 设备的描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "id": {"description": "逻辑 PCI 映射的 ID。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "live-migration-capable": {
      "default": 0, "description": "将设备标记为支持在线迁移（实验性）。此功能需要硬件和驱动支持。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "description": {"description": "节点特定设备的描述。", "maxLength": 4096, "optional": 1, "type": "string"},
          "id": {"description": "预期的供应商和设备 ID。用于检测硬件变化", "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)", "type": "string"},
          "iommugroup": {"description": "预期设备所在的 IOMMU 组。用于检测硬件变化。", "optional": 1, "type": "integer"},
          "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "path": {
            "description": "设备路径。如果省略功能号，则映射整个设备。此时使用第一个设备的属性。可以提供以分号分隔的多个路径，客户机启动时将选择第一个可用路径。",
            "pattern": "(?:[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?;)*[a-f0-9]{4,}:[a-f0-9]{2}:[a-f0-9]{2}(?:.[a-f0-9])?", "type": "string"
          },
          "subsystem-id": {
            "description": "预期的子系统供应商和设备 ID。用于检测硬件变化。", "optional": 1, "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)", "type": "string"
          }
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "mdev": {"default": 0, "description": "将设备标记为能够提供中介设备。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-pci-id-80b107bb-put-returns" id="api-cluster-mapping-pci-id-80b107bb-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/pci/{id})。

## `/cluster/mapping/usb` <a href="#api-cluster-mapping-usb-677dac0a" id="api-cluster-mapping-usb-677dac0a"></a>

原始接口路径：`/cluster/mapping/usb`。

### GET `/cluster/mapping/usb` <a href="#api-cluster-mapping-usb-677dac0a-get" id="api-cluster-mapping-usb-677dac0a-get"></a>

列出 USB 硬件映射

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/mapping/usb/<id>' 具有 'Mapping.Modify'、'Mapping.Use' 或 'Mapping.Audit' 权限的条目。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-mapping-usb-677dac0a-get-parameters" id="api-cluster-mapping-usb-677dac0a-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `check-node` | 类型：string；必填：否；默认值：—<br>如果指定，则检查给定节点上的配置是否正确，并将相关错误加入设备。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "check-node": {
      "description": "如果指定，则检查给定节点上的配置是否正确，并将相关错误加入设备。", "format": "pve-node", "optional": 1, "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-usb-677dac0a-get-returns" id="api-cluster-mapping-usb-677dac0a-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "description": {"description": "逻辑映射的描述。", "type": "string"},
      "error": {
        "description": "指定 'check_node' 时的错误列表。",
        "items": {
          "properties": {"message": {"description": "错误消息", "type": "string"}, "severity": {"description": "错误严重程度", "type": "string"}},
          "type": "object"
        }
      },
      "id": {"description": "映射的逻辑 ID。", "type": "string"},
      "map": {"description": "映射条目。", "items": {"description": "节点的映射。", "type": "string"}, "type": "array"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/mapping/usb` <a href="#api-cluster-mapping-usb-677dac0a-post" id="api-cluster-mapping-usb-677dac0a-post"></a>

创建新的硬件映射。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/mapping/usb", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-usb-677dac0a-post-parameters" id="api-cluster-mapping-usb-677dac0a-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `description` | 类型：string；必填：否；默认值：—<br>逻辑 USB 设备的描述。 |
| `id` | 类型：string；必填：是；默认值：—<br>逻辑 USB 映射的 ID。 |
| `map` | 类型：array；必填：是；默认值：—<br>集群节点的映射列表。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "description": {"description": "逻辑 USB 设备的描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "id": {"description": "逻辑 USB 映射的 ID。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "description": {"description": "节点特定设备的描述。", "maxLength": 4096, "optional": 1, "type": "string"},
          "id": {
            "description": "预期的供应商和设备 ID。如果给定 USB 路径，则此项仅用于检测硬件变化", "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          },
          "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "path": {"description": "USB 设备路径。", "optional": 1, "pattern": "(?^:^(\\d+)\\-(\\d+(\\.\\d+)*)$)", "type": "string"}
        },
        "type": "string"
      },
      "type": "array", "typetext": "<array>"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-usb-677dac0a-post-returns" id="api-cluster-mapping-usb-677dac0a-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/usb)。

## `/cluster/mapping/usb/{id}` <a href="#api-cluster-mapping-usb-id-2ec5bd1f" id="api-cluster-mapping-usb-id-2ec5bd1f"></a>

原始接口路径：`/cluster/mapping/usb/{id}`。

### DELETE `/cluster/mapping/usb/{id}` <a href="#api-cluster-mapping-usb-id-2ec5bd1f-delete" id="api-cluster-mapping-usb-id-2ec5bd1f-delete"></a>

移除硬件映射。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/mapping/usb", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-usb-id-2ec5bd1f-delete-parameters" id="api-cluster-mapping-usb-id-2ec5bd1f-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-usb-id-2ec5bd1f-delete-returns" id="api-cluster-mapping-usb-id-2ec5bd1f-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/mapping/usb/{id}` <a href="#api-cluster-mapping-usb-id-2ec5bd1f-get" id="api-cluster-mapping-usb-id-2ec5bd1f-get"></a>

获取 USB 映射。

**方法标识：** `get`

**权限**

```text
{
  "check": [
    "or", ["perm", "/mapping/usb/{id}", ["Mapping.Audit"]], ["perm", "/mapping/usb/{id}", ["Mapping.Use"]], ["perm", "/mapping/usb/{id}", ["Mapping.Modify"]]
  ]
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-usb-id-2ec5bd1f-get-parameters" id="api-cluster-mapping-usb-id-2ec5bd1f-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"format": "pve-configid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-usb-id-2ec5bd1f-get-returns" id="api-cluster-mapping-usb-id-2ec5bd1f-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/mapping/usb/{id}` <a href="#api-cluster-mapping-usb-id-2ec5bd1f-put" id="api-cluster-mapping-usb-id-2ec5bd1f-put"></a>

更新硬件映射。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/mapping/usb/{id}", ["Mapping.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-mapping-usb-id-2ec5bd1f-put-parameters" id="api-cluster-mapping-usb-id-2ec5bd1f-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `description` | 类型：string；必填：否；默认值：—<br>逻辑 USB 设备的描述。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `id` | 类型：string；必填：是；默认值：—<br>逻辑 USB 映射的 ID。 |
| `map` | 类型：array；必填：是；默认值：—<br>集群节点的映射列表。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "description": {"description": "逻辑 USB 设备的描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "id": {"description": "逻辑 USB 映射的 ID。", "format": "pve-configid", "type": "string", "typetext": "<string>"},
    "map": {
      "description": "集群节点的映射列表。",
      "items": {
        "format": {
          "description": {"description": "节点特定设备的描述。", "maxLength": 4096, "optional": 1, "type": "string"},
          "id": {
            "description": "预期的供应商和设备 ID。如果给定 USB 路径，则此项仅用于检测硬件变化", "pattern": "(?^:^[0-9A-Fa-f]{4}:[0-9A-Fa-f]{4}$)",
            "type": "string"
          },
          "node": {"description": "集群节点名称。", "format": "pve-node", "type": "string"},
          "path": {"description": "USB 设备路径。", "optional": 1, "pattern": "(?^:^(\\d+)\\-(\\d+(\\.\\d+)*)$)", "type": "string"}
        },
        "type": "string"
      },
      "type": "array", "typetext": "<array>"
    }
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-mapping-usb-id-2ec5bd1f-put-returns" id="api-cluster-mapping-usb-id-2ec5bd1f-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/mapping/usb/{id})。

## `/cluster/bulk-action` <a href="#api-cluster-bulk-action-9ecda72c" id="api-cluster-bulk-action-9ecda72c"></a>

原始接口路径：`/cluster/bulk-action`。

### GET `/cluster/bulk-action` <a href="#api-cluster-bulk-action-9ecda72c-get" id="api-cluster-bulk-action-9ecda72c-get"></a>

列出资源类型。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-bulk-action-9ecda72c-get-parameters" id="api-cluster-bulk-action-9ecda72c-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-bulk-action-9ecda72c-get-returns" id="api-cluster-bulk-action-9ecda72c-get-returns"></a>

```text
{"items": {"type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action)。

## `/cluster/bulk-action/guest` <a href="#api-cluster-bulk-action-guest-4e0ad08a" id="api-cluster-bulk-action-guest-4e0ad08a"></a>

原始接口路径：`/cluster/bulk-action/guest`。

### GET `/cluster/bulk-action/guest` <a href="#api-cluster-bulk-action-guest-4e0ad08a-get" id="api-cluster-bulk-action-guest-4e0ad08a-get"></a>

批量操作索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-bulk-action-guest-4e0ad08a-get-parameters" id="api-cluster-bulk-action-guest-4e0ad08a-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-bulk-action-guest-4e0ad08a-get-returns" id="api-cluster-bulk-action-guest-4e0ad08a-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest)。

## `/cluster/bulk-action/guest/start` <a href="#api-cluster-bulk-action-guest-start-9c3d3d17" id="api-cluster-bulk-action-guest-start-9c3d3d17"></a>

原始接口路径：`/cluster/bulk-action/guest/start`。

### POST `/cluster/bulk-action/guest/start` <a href="#api-cluster-bulk-action-guest-start-9c3d3d17-post" id="api-cluster-bulk-action-guest-start-9c3d3d17-post"></a>

批量启动或恢复集群中的所有客户机。

**方法标识：** `start`

**权限**

```text
{"description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.PowerMgmt' 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-bulk-action-guest-start-9c3d3d17-post-parameters" id="api-cluster-bulk-action-guest-start-9c3d3d17-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `max-workers` | 类型：integer；必填：否；默认值：4<br>定义并发运行的最大任务数。 |
| `maxworkers` | 类型：integer；必填：否；默认值：4<br>定义并发运行的最大任务数。已弃用，请改用 'max-workers'。 |
| `timeout` | 类型：integer；必填：否；默认值：—<br>默认启动超时时间，单位为秒。仅适用于虚拟机。（默认值取决于客户机配置）。 |
| `vms` | 类型：array；必填：否；默认值：—<br>仅考虑此 VMID 列表中的客户机。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 4, "description": "定义并发运行的最大任务数。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 4, "description": "定义并发运行的最大任务数。已弃用，请改用 'max-workers'。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "timeout": {
      "description": "默认启动超时时间，单位为秒。仅适用于虚拟机。（默认值取决于客户机配置）。", "optional": 1, "type": "integer", "typetext": "<integer>"
    },
    "vms": {
      "description": "仅考虑此 VMID 列表中的客户机。",
      "items": {"description": "虚拟机的（唯一）ID。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "type": "integer"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-bulk-action-guest-start-9c3d3d17-post-returns" id="api-cluster-bulk-action-guest-start-9c3d3d17-post-returns"></a>

```text
{"description": "工作任务的 UPID", "type": "string"}
```

<details>
<summary>其他接口元数据</summary>

```text
{"expose_credentials": 1}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/start)。

## `/cluster/bulk-action/guest/shutdown` <a href="#api-cluster-bulk-action-guest-shutdown-2b6d3381" id="api-cluster-bulk-action-guest-shutdown-2b6d3381"></a>

原始接口路径：`/cluster/bulk-action/guest/shutdown`。

### POST `/cluster/bulk-action/guest/shutdown` <a href="#api-cluster-bulk-action-guest-shutdown-2b6d3381-post" id="api-cluster-bulk-action-guest-shutdown-2b6d3381-post"></a>

批量关闭集群中的所有客户机。

**方法标识：** `shutdown`

**权限**

```text
{"description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.PowerMgmt' 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-bulk-action-guest-shutdown-2b6d3381-post-parameters" id="api-cluster-bulk-action-guest-shutdown-2b6d3381-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `force-stop` | 类型：boolean；必填：否；默认值：1<br>确保客户机在超时后停止。 |
| `max-workers` | 类型：integer；必填：否；默认值：4<br>定义并发运行的最大任务数。 |
| `maxworkers` | 类型：integer；必填：否；默认值：4<br>定义并发运行的最大任务数。已弃用，请改用 'max-workers'。 |
| `timeout` | 类型：integer；必填：否；默认值：180<br>客户机未配置时使用的默认关机超时时间，单位为秒。 |
| `vms` | 类型：array；必填：否；默认值：—<br>仅考虑此 VMID 列表中的客户机。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "force-stop": {"default": 1, "description": "确保客户机在超时后停止。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "max-workers": {
      "default": 4, "description": "定义并发运行的最大任务数。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 4, "description": "定义并发运行的最大任务数。已弃用，请改用 'max-workers'。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "timeout": {"default": 180, "description": "客户机未配置时使用的默认关机超时时间，单位为秒。", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "vms": {
      "description": "仅考虑此 VMID 列表中的客户机。",
      "items": {"description": "虚拟机的（唯一）ID。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "type": "integer"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-bulk-action-guest-shutdown-2b6d3381-post-returns" id="api-cluster-bulk-action-guest-shutdown-2b6d3381-post-returns"></a>

```text
{"description": "工作任务的 UPID", "type": "string"}
```

<details>
<summary>其他接口元数据</summary>

```text
{"expose_credentials": 1}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/shutdown)。

## `/cluster/bulk-action/guest/suspend` <a href="#api-cluster-bulk-action-guest-suspend-06b42be1" id="api-cluster-bulk-action-guest-suspend-06b42be1"></a>

原始接口路径：`/cluster/bulk-action/guest/suspend`。

### POST `/cluster/bulk-action/guest/suspend` <a href="#api-cluster-bulk-action-guest-suspend-06b42be1-post" id="api-cluster-bulk-action-guest-suspend-06b42be1-post"></a>

批量挂起集群中的所有客户机。

**方法标识：** `suspend`

**权限**

```text
{
  "description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.PowerMgmt' 权限。另外，还需要对 '/vms/{vmid}' 路径具有 'VM.Config.Disk' 权限，以及对已配置的状态存储具有 'Datastore.AllocateSpace' 权限",
  "user": "all"
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-bulk-action-guest-suspend-06b42be1-post-parameters" id="api-cluster-bulk-action-guest-suspend-06b42be1-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `max-workers` | 类型：integer；必填：否；默认值：4<br>定义并发运行的最大任务数。 |
| `maxworkers` | 类型：integer；必填：否；默认值：4<br>定义并发运行的最大任务数。已弃用，请改用 'max-workers'。 |
| `statestorage` | 类型：string；必填：否；默认值：—<br>存放虚拟机状态的存储。 |
| `to-disk` | 类型：boolean；必填：否；默认值：0<br>如果设置，则将客户机挂起到磁盘。下次启动时将恢复。 |
| `vms` | 类型：array；必填：否；默认值：—<br>仅考虑此 VMID 列表中的客户机。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 4, "description": "定义并发运行的最大任务数。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 4, "description": "定义并发运行的最大任务数。已弃用，请改用 'max-workers'。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "statestorage": {
      "description": "存放虚拟机状态的存储。", "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "requires": "to-disk",
      "type": "string", "typetext": "<storage ID>"
    },
    "to-disk": {"default": 0, "description": "如果设置，则将客户机挂起到磁盘。下次启动时将恢复。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "vms": {
      "description": "仅考虑此 VMID 列表中的客户机。",
      "items": {"description": "虚拟机的（唯一）ID。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "type": "integer"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-bulk-action-guest-suspend-06b42be1-post-returns" id="api-cluster-bulk-action-guest-suspend-06b42be1-post-returns"></a>

```text
{"description": "工作任务的 UPID", "type": "string"}
```

<details>
<summary>其他接口元数据</summary>

```text
{"expose_credentials": 1}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/suspend)。

## `/cluster/bulk-action/guest/migrate` <a href="#api-cluster-bulk-action-guest-migrate-62d741d7" id="api-cluster-bulk-action-guest-migrate-62d741d7"></a>

原始接口路径：`/cluster/bulk-action/guest/migrate`。

### POST `/cluster/bulk-action/guest/migrate` <a href="#api-cluster-bulk-action-guest-migrate-62d741d7-post" id="api-cluster-bulk-action-guest-migrate-62d741d7-post"></a>

批量迁移集群中的所有客户机。

**方法标识：** `migrate`

**权限**

```text
{"description": "对于通过 'vms' 参数传入的每个 ID，需要对 '/' 或 '/vms/<ID>' 具有 'VM.Migrate' 权限。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-bulk-action-guest-migrate-62d741d7-post-parameters" id="api-cluster-bulk-action-guest-migrate-62d741d7-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `max-workers` | 类型：integer；必填：否；默认值：1<br>定义并发运行的最大任务数。 |
| `maxworkers` | 类型：integer；必填：否；默认值：1<br>定义并发运行的最大任务数。已弃用，请改用 'max-workers'。 |
| `online` | 类型：boolean；必填：否；默认值：—<br>为虚拟机启用在线迁移，为容器启用重启迁移。 |
| `target` | 类型：string；必填：是；默认值：—<br>目标节点。 |
| `vms` | 类型：array；必填：否；默认值：—<br>仅考虑此 VMID 列表中的客户机。 |
| `with-local-disks` | 类型：boolean；必填：否；默认值：—<br>为本地磁盘启用在线存储迁移 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "max-workers": {
      "default": 1, "description": "定义并发运行的最大任务数。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 64)"
    },
    "maxworkers": {
      "default": 1, "description": "定义并发运行的最大任务数。已弃用，请改用 'max-workers'。", "maximum": 64, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 64)"
    },
    "online": {"description": "为虚拟机启用在线迁移，为容器启用重启迁移。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "target": {"description": "目标节点。", "format": "pve-node", "type": "string", "typetext": "<string>"},
    "vms": {
      "description": "仅考虑此 VMID 列表中的客户机。",
      "items": {"description": "虚拟机的（唯一）ID。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "type": "integer"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "with-local-disks": {"description": "为本地磁盘启用在线存储迁移", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-bulk-action-guest-migrate-62d741d7-post-returns" id="api-cluster-bulk-action-guest-migrate-62d741d7-post-returns"></a>

```text
{"description": "工作任务的 UPID", "type": "string"}
```

<details>
<summary>其他接口元数据</summary>

```text
{"expose_credentials": 1}
```

</details>

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/bulk-action/guest/migrate)。

## `/cluster/sdn` <a href="#api-cluster-sdn-a5d61349" id="api-cluster-sdn-a5d61349"></a>

原始接口路径：`/cluster/sdn`。

### GET `/cluster/sdn` <a href="#api-cluster-sdn-a5d61349-get" id="api-cluster-sdn-a5d61349-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/sdn", ["SDN.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-a5d61349-get-parameters" id="api-cluster-sdn-a5d61349-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-sdn-a5d61349-get-returns" id="api-cluster-sdn-a5d61349-get-returns"></a>

```text
{"items": {"properties": {"id": {"type": "string"}}, "type": "object"}, "links": [{"href": "{id}", "rel": "child"}], "type": "array"}
```

### PUT `/cluster/sdn` <a href="#api-cluster-sdn-a5d61349-put" id="api-cluster-sdn-a5d61349-put"></a>

应用 SDN 控制器更改并重新加载。

**方法标识：** `reload`

**权限**

```text
{"check": ["perm", "/sdn", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-a5d61349-put-parameters" id="api-cluster-sdn-a5d61349-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `release-lock` | 类型：boolean；必填：否；默认值：1<br>提供 lock-token 且配置成功提交后，自动释放锁 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "release-lock": {"default": 1, "description": "提供 lock-token 且配置成功提交后，自动释放锁", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-a5d61349-put-returns" id="api-cluster-sdn-a5d61349-put-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn)。

## `/cluster/sdn/vnets` <a href="#api-cluster-sdn-vnets-dcadb0c4" id="api-cluster-sdn-vnets-dcadb0c4"></a>

原始接口路径：`/cluster/sdn/vnets`。

### GET `/cluster/sdn/vnets` <a href="#api-cluster-sdn-vnets-dcadb0c4-get" id="api-cluster-sdn-vnets-dcadb0c4-get"></a>

SDN vnet 索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-dcadb0c4-get-parameters" id="api-cluster-sdn-vnets-dcadb0c4-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-dcadb0c4-get-returns" id="api-cluster-sdn-vnets-dcadb0c4-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "alias": {"description": "VNet 的别名。", "maxLength": 256, "optional": 1, "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})", "type": "string"},
      "digest": {"description": "VNet 配置节的摘要。", "optional": 1, "type": "string"},
      "isolate-ports": {"description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。", "optional": 1, "type": "boolean"},
      "pending": {
        "description": "尚未应用到运行配置的更改。", "optional": 1,
        "properties": {
          "alias": {"description": "VNet 的别名。", "maxLength": 256, "optional": 1, "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})", "type": "string"},
          "isolate-ports": {"description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。", "optional": 1, "type": "boolean"},
          "tag": {
            "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。", "maximum": 16777215, "minimum": 1, "optional": 1,
            "type": "integer"
          },
          "vlanaware": {"description": "允许 VLAN 穿过此 VNet。", "optional": 1, "type": "boolean"},
          "zone": {"description": "此 VNet 所属区域的名称。", "optional": 1, "type": "string"}
        },
        "type": "object"
      },
      "state": {"description": "SDN 配置对象的状态。", "enum": ["new", "changed", "deleted"], "optional": 1, "type": "string"},
      "tag": {
        "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。", "maximum": 16777215, "minimum": 1, "optional": 1,
        "type": "integer"
      },
      "type": {"description": "VNet 的类型。", "enum": ["vnet"], "optional": 0, "type": "string"},
      "vlanaware": {"description": "允许 VLAN 穿过此 VNet。", "optional": 1, "type": "boolean"},
      "vnet": {"description": "VNet 的名称。", "optional": 0, "type": "string"},
      "zone": {"description": "此 VNet 所属区域的名称。", "optional": 1, "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{vnet}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/vnets` <a href="#api-cluster-sdn-vnets-dcadb0c4-post" id="api-cluster-sdn-vnets-dcadb0c4-post"></a>

创建新的 SDN vnet 对象。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-dcadb0c4-post-parameters" id="api-cluster-sdn-vnets-dcadb0c4-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `alias` | 类型：string；必填：否；默认值：—<br>VNet 的别名。 |
| `isolate-ports` | 类型：boolean；必填：否；默认值：—<br>如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `tag` | 类型：integer；必填：否；默认值：—<br>VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。 |
| `type` | 类型：string；必填：否；默认值：—<br>VNet 的类型。；可选值：`vnet` |
| `vlanaware` | 类型：boolean；必填：否；默认值：—<br>允许 VLAN 穿过此 vnet。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |
| `zone` | 类型：string；必填：是；默认值：—<br>此 VNet 所属区域的名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "alias": {"description": "VNet 的别名。", "maxLength": 256, "optional": 1, "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})", "type": "string"},
    "isolate-ports": {
      "description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "tag": {
      "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。", "maximum": 16777215, "minimum": 1, "optional": 1,
      "type": "integer", "typetext": "<integer> (1 - 16777215)"
    },
    "type": {"description": "VNet 的类型。", "enum": ["vnet"], "optional": 1, "type": "string"},
    "vlanaware": {"description": "允许 VLAN 穿过此 vnet。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "zone": {"description": "此 VNet 所属区域的名称。", "optional": 0, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-dcadb0c4-post-returns" id="api-cluster-sdn-vnets-dcadb0c4-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets)。

## `/cluster/sdn/vnets/{vnet}` <a href="#api-cluster-sdn-vnets-vnet-afce4b42" id="api-cluster-sdn-vnets-vnet-afce4b42"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}`。

### DELETE `/cluster/sdn/vnets/{vnet}` <a href="#api-cluster-sdn-vnets-vnet-afce4b42-delete" id="api-cluster-sdn-vnets-vnet-afce4b42-delete"></a>

删除 SDN vnet 对象配置。

**方法标识：** `delete`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-afce4b42-delete-parameters" id="api-cluster-sdn-vnets-vnet-afce4b42-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-afce4b42-delete-returns" id="api-cluster-sdn-vnets-vnet-afce4b42-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/vnets/{vnet}` <a href="#api-cluster-sdn-vnets-vnet-afce4b42-get" id="api-cluster-sdn-vnets-vnet-afce4b42-get"></a>

读取 SDN vnet 配置。

**方法标识：** `read`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-afce4b42-get-parameters" id="api-cluster-sdn-vnets-vnet-afce4b42-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-afce4b42-get-returns" id="api-cluster-sdn-vnets-vnet-afce4b42-get-returns"></a>

```text
{
  "properties": {
    "alias": {"description": "VNet 的别名。", "maxLength": 256, "optional": 1, "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})", "type": "string"},
    "digest": {"description": "VNet 配置节的摘要。", "optional": 1, "type": "string"},
    "isolate-ports": {"description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。", "optional": 1, "type": "boolean"},
    "pending": {
      "description": "尚未应用到运行配置的更改。", "optional": 1,
      "properties": {
        "alias": {"description": "VNet 的别名。", "maxLength": 256, "optional": 1, "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})", "type": "string"},
        "isolate-ports": {"description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。", "optional": 1, "type": "boolean"},
        "tag": {
          "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。", "maximum": 16777215, "minimum": 1, "optional": 1,
          "type": "integer"
        },
        "vlanaware": {"description": "允许 VLAN 穿过此 VNet。", "optional": 1, "type": "boolean"},
        "zone": {"description": "此 VNet 所属区域的名称。", "optional": 1, "type": "string"}
      },
      "type": "object"
    },
    "state": {"description": "SDN 配置对象的状态。", "enum": ["new", "changed", "deleted"], "optional": 1, "type": "string"},
    "tag": {
      "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。", "maximum": 16777215, "minimum": 1, "optional": 1,
      "type": "integer"
    },
    "type": {"description": "VNet 的类型。", "enum": ["vnet"], "optional": 0, "type": "string"},
    "vlanaware": {"description": "允许 VLAN 穿过此 VNet。", "optional": 1, "type": "boolean"},
    "vnet": {"description": "VNet 的名称。", "optional": 0, "type": "string"},
    "zone": {"description": "此 VNet 所属区域的名称。", "optional": 1, "type": "string"}
  }
}
```

### PUT `/cluster/sdn/vnets/{vnet}` <a href="#api-cluster-sdn-vnets-vnet-afce4b42-put" id="api-cluster-sdn-vnets-vnet-afce4b42-put"></a>

更新 SDN vnet 对象配置。

**方法标识：** `update`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-afce4b42-put-parameters" id="api-cluster-sdn-vnets-vnet-afce4b42-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `alias` | 类型：string；必填：否；默认值：—<br>VNet 的别名。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `isolate-ports` | 类型：boolean；必填：否；默认值：—<br>如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `tag` | 类型：integer；必填：否；默认值：—<br>VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。 |
| `vlanaware` | 类型：boolean；必填：否；默认值：—<br>允许 VLAN 穿过此 vnet。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |
| `zone` | 类型：string；必填：否；默认值：—<br>此 VNet 所属区域的名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "alias": {"description": "VNet 的别名。", "maxLength": 256, "optional": 1, "pattern": "(?^i:[\\(\\)-_.\\w\\d\\s]{0,256})", "type": "string"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "isolate-ports": {
      "description": "如果为 true，则为此 VNet 网桥上的所有接口设置 isolated 属性。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "tag": {
      "description": "VLAN 标签（用于 VLAN 或 QinQ 区域）或 VXLAN VNI（用于 VXLAN 或 EVPN 区域）。", "maximum": 16777215, "minimum": 1, "optional": 1,
      "type": "integer", "typetext": "<integer> (1 - 16777215)"
    },
    "vlanaware": {"description": "允许 VLAN 穿过此 vnet。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "zone": {"description": "此 VNet 所属区域的名称。", "optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-afce4b42-put-returns" id="api-cluster-sdn-vnets-vnet-afce4b42-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet})。

## `/cluster/sdn/vnets/{vnet}/firewall` <a href="#api-cluster-sdn-vnets-vnet-firewall-187c85cd" id="api-cluster-sdn-vnets-vnet-firewall-187c85cd"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall`。

### GET `/cluster/sdn/vnets/{vnet}/firewall` <a href="#api-cluster-sdn-vnets-vnet-firewall-187c85cd-get" id="api-cluster-sdn-vnets-vnet-firewall-187c85cd-get"></a>

目录索引。

**方法标识：** `index`

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-187c85cd-get-parameters" id="api-cluster-sdn-vnets-vnet-firewall-187c85cd-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-187c85cd-get-returns" id="api-cluster-sdn-vnets-vnet-firewall-187c85cd-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{name}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall)。

## `/cluster/sdn/vnets/{vnet}/firewall/rules` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/rules`。

### GET `/cluster/sdn/vnets/{vnet}/firewall/rules` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-get" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-get"></a>

列出规则。

**方法标识：** `get_rules`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Audit 或 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-get-parameters" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-get-returns" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "action": {"description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称", "type": "string"},
      "comment": {"description": "描述性注释", "optional": 1, "type": "string"}, "dest": {"description": "限制数据包目标地址", "optional": 1, "type": "string"},
      "dport": {"description": "限制 TCP/UDP 目标端口", "optional": 1, "type": "string"},
      "enable": {"description": "用于启用/禁用规则的标志", "optional": 1, "type": "integer"},
      "icmp-type": {"description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效", "optional": 1, "type": "string"},
      "iface": {"description": "网络接口名称。虚拟机和容器必须使用网络配置键名", "optional": 1, "type": "string"},
      "ipversion": {"description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定", "optional": 1, "type": "integer"},
      "log": {
        "description": "防火墙规则的日志级别", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
        "type": "string"
      },
      "macro": {"description": "使用预定义的标准宏", "optional": 1, "type": "string"}, "pos": {"description": "规则在规则集中的位置", "type": "integer"},
      "proto": {"description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字", "optional": 1, "type": "string"},
      "source": {"description": "限制数据包源地址", "optional": 1, "type": "string"},
      "sport": {"description": "限制 TCP/UDP 源端口", "optional": 1, "type": "string"}, "type": {"description": "规则类型", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{pos}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/vnets/{vnet}/firewall/rules` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-post" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-post"></a>

创建新规则。

**方法标识：** `create_rule`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-post-parameters" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：是；默认值：—<br>规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述性注释。 |
| `dest` | 类型：string；必填：否；默认值：—<br>限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | 类型：integer；必填：否；默认值：—<br>用于启用/禁用规则的标志。 |
| `icmp-type` | 类型：string；必填：否；默认值：—<br>指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | 类型：string；必填：否；默认值：—<br>网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | 类型：string；必填：否；默认值：—<br>防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | 类型：string；必填：否；默认值：—<br>使用预定义的标准宏。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | 类型：string；必填：否；默认值：—<br>IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | 类型：string；必填：否；默认值：—<br>限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | 类型：string；必填：是；默认值：—<br>规则类型。；可选值：`in`, `out`, `forward`, `group` |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。", "maxLength": 20, "minLength": 2, "optional": 0,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    },
    "comment": {"description": "描述性注释。", "format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "enable": {"description": "用于启用/禁用规则的标志。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。", "format": "pve-fw-icmp-type-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。", "format": "pve-iface", "maxLength": 20,
      "minLength": 2, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏。", "maxLength": 128, "optional": 1, "type": "string", "typetext": "<string>"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。", "format": "pve-fw-protocol-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "type": {"description": "规则类型。", "enum": ["in", "out", "forward", "group"], "optional": 0, "type": "string"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-post-returns" id="api-cluster-sdn-vnets-vnet-firewall-rules-2e07f079-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/rules)。

## `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}`。

### DELETE `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-delete" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-delete"></a>

删除规则。

**方法标识：** `delete_rule`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-delete-parameters" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-delete-returns" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-get" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-get"></a>

获取单条规则数据。

**方法标识：** `get_rule`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Audit 或 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-get-parameters" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-get-returns" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-get-returns"></a>

```text
{
  "properties": {
    "action": {"description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称", "type": "string"},
    "comment": {"description": "描述性注释", "optional": 1, "type": "string"}, "dest": {"description": "限制数据包目标地址", "optional": 1, "type": "string"},
    "dport": {"description": "限制 TCP/UDP 目标端口", "optional": 1, "type": "string"},
    "enable": {"description": "用于启用/禁用规则的标志", "optional": 1, "type": "integer"},
    "icmp-type": {"description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效", "optional": 1, "type": "string"},
    "iface": {"description": "网络接口名称。虚拟机和容器必须使用网络配置键名", "optional": 1, "type": "string"},
    "ipversion": {"description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定", "optional": 1, "type": "integer"},
    "log": {
      "description": "防火墙规则的日志级别", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏", "optional": 1, "type": "string"}, "pos": {"description": "规则在规则集中的位置", "type": "integer"},
    "proto": {"description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字", "optional": 1, "type": "string"},
    "source": {"description": "限制数据包源地址", "optional": 1, "type": "string"},
    "sport": {"description": "限制 TCP/UDP 源端口", "optional": 1, "type": "string"}, "type": {"description": "规则类型", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}` <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-put" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-put"></a>

修改规则数据。

**方法标识：** `update_rule`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `null`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-put-parameters" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：否；默认值：—<br>规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述性注释。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `dest` | 类型：string；必填：否；默认值：—<br>限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | 类型：integer；必填：否；默认值：—<br>用于启用/禁用规则的标志。 |
| `icmp-type` | 类型：string；必填：否；默认值：—<br>指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | 类型：string；必填：否；默认值：—<br>网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | 类型：string；必填：否；默认值：—<br>防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | 类型：string；必填：否；默认值：—<br>使用预定义的标准宏。 |
| `moveto` | 类型：integer；必填：否；默认值：—<br>将规则移至新位置 &lt;moveto&gt;。其他参数将被忽略。 |
| `pos` | 类型：integer；必填：否；默认值：—<br>更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | 类型：string；必填：否；默认值：—<br>IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | 类型：string；必填：否；默认值：—<br>限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | 类型：string；必填：否；默认值：—<br>限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | 类型：string；必填：否；默认值：—<br>规则类型。；可选值：`in`, `out`, `forward`, `group` |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。", "maxLength": 20, "minLength": 2, "optional": 1,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+", "type": "string"
    },
    "comment": {"description": "描述性注释。", "format": "pve-fw-comment-spec", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "enable": {"description": "用于启用/禁用规则的标志。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。", "format": "pve-fw-icmp-type-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。", "format": "pve-iface", "maxLength": 20,
      "minLength": 2, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "macro": {"description": "使用预定义的标准宏。", "maxLength": 128, "optional": 1, "type": "string", "typetext": "<string>"},
    "moveto": {"description": "将规则移至新位置 <moveto>。其他参数将被忽略。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "pos": {"description": "更新位置 <pos> 处的规则。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。", "format": "pve-fw-protocol-spec", "optional": 1,
      "type": "string", "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec", "maxLength": 512, "optional": 1, "type": "string", "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "type": {"description": "规则类型。", "enum": ["in", "out", "forward", "group"], "optional": 1, "type": "string"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-put-returns" id="api-cluster-sdn-vnets-vnet-firewall-rules-pos-9e764b01-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/rules/{pos})。

## `/cluster/sdn/vnets/{vnet}/firewall/options` <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/options`。

### GET `/cluster/sdn/vnets/{vnet}/firewall/options` <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-get" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-get"></a>

获取 vnet 防火墙选项。

**方法标识：** `get_options`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Audit 或 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-get-parameters" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-get-returns" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-get-returns"></a>

```text
{
  "properties": {
    "enable": {"default": 0, "description": "启用/禁用防火墙规则。", "optional": 1, "type": "boolean"},
    "log_level_forward": {
      "description": "转发流量的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "policy_forward": {"description": "转发策略。", "enum": ["ACCEPT", "DROP"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

### PUT `/cluster/sdn/vnets/{vnet}/firewall/options` <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-put" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-put"></a>

设置防火墙选项。

**方法标识：** `set_options`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Allocate 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-put-parameters" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `enable` | 类型：boolean；必填：否；默认值：0<br>启用/禁用防火墙规则。 |
| `log_level_forward` | 类型：string；必填：否；默认值：—<br>转发流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `policy_forward` | 类型：string；必填：否；默认值：—<br>转发策略。；可选值：`ACCEPT`, `DROP` |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "enable": {"default": 0, "description": "启用/禁用防火墙规则。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "log_level_forward": {
      "description": "转发流量的日志级别。", "enum": ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug", "nolog"], "optional": 1,
      "type": "string"
    },
    "policy_forward": {"description": "转发策略。", "enum": ["ACCEPT", "DROP"], "optional": 1, "type": "string"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-put-returns" id="api-cluster-sdn-vnets-vnet-firewall-options-4d9e573e-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/options)。

## `/cluster/sdn/vnets/{vnet}/subnets` <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/subnets`。

### GET `/cluster/sdn/vnets/{vnet}/subnets` <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-get" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-get"></a>

SDN 子网索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-get-parameters" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-get-returns" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{subnet}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/sdn/vnets/{vnet}/subnets` <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-post" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-post"></a>

创建新的 SDN 子网对象。

**方法标识：** `create`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-post-parameters" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `dhcp-dns-server` | 类型：string；必填：否；默认值：—<br>DNS 服务器的 IP 地址 |
| `dhcp-range` | 类型：array；必填：否；默认值：—<br>此子网的 DHCP 地址范围列表 |
| `dnszoneprefix` | 类型：string；必填：否；默认值：—<br>DNS 域区域前缀  例如：'adm' -&gt; &lt;hostname&gt;.adm.mydomain.com |
| `gateway` | 类型：string；必填：否；默认值：—<br>子网网关：对于 layer3 区域，将分配在 vnet 上 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `snat` | 类型：boolean；必填：否；默认值：—<br>使用 pve-firewall 时为此子网启用地址伪装 |
| `subnet` | 类型：string；必填：是；默认值：—<br>SDN 子网对象标识符。 |
| `type` | 类型：string；必填：是；默认值：—<br>；可选值：`subnet` |
| `vnet` | 类型：string；必填：是；默认值：—<br>关联的 vnet |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "dhcp-dns-server": {"description": "DNS 服务器的 IP 地址", "format": "ip", "optional": 1, "type": "string", "typetext": "<string>"},
    "dhcp-range": {
      "description": "此子网的 DHCP 地址范围列表", "items": {"format": "pve-sdn-dhcp-range", "type": "string"}, "optional": 1, "type": "array",
      "typetext": "<array>"
    },
    "dnszoneprefix": {
      "description": "DNS 域区域前缀  例如：'adm' -> <hostname>.adm.mydomain.com", "format": "dns-name", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "gateway": {"description": "子网网关：对于 layer3 区域，将分配在 vnet 上", "format": "ip", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "snat": {"description": "使用 pve-firewall 时为此子网启用地址伪装", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "subnet": {"description": "SDN 子网对象标识符。", "format": "pve-sdn-subnet-id", "type": "string", "typetext": "<string>"},
    "type": {"enum": ["subnet"], "type": "string"}, "vnet": {"description": "关联的 vnet", "optional": 0, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-post-returns" id="api-cluster-sdn-vnets-vnet-subnets-e9bf1e25-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/subnets)。

## `/cluster/sdn/vnets/{vnet}/subnets/{subnet}` <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/subnets/{subnet}`。

### DELETE `/cluster/sdn/vnets/{vnet}/subnets/{subnet}` <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-delete" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-delete"></a>

删除 SDN 子网对象配置。

**方法标识：** `delete`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-delete-parameters" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `subnet` | 类型：string；必填：是；默认值：—<br>SDN 子网对象标识符。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "subnet": {"description": "SDN 子网对象标识符。", "format": "pve-sdn-subnet-id", "type": "string", "typetext": "<string>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-delete-returns" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/vnets/{vnet}/subnets/{subnet}` <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-get" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-get"></a>

读取 SDN 子网配置。

**方法标识：** `read`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-get-parameters" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `subnet` | 类型：string；必填：是；默认值：—<br>SDN 子网对象标识符。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "subnet": {"description": "SDN 子网对象标识符。", "format": "pve-sdn-subnet-id", "type": "string", "typetext": "<string>"},
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-get-returns" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/sdn/vnets/{vnet}/subnets/{subnet}` <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-put" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-put"></a>

更新 SDN 子网对象配置。

**方法标识：** `update`

**权限**

```text
{"description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Allocate' 权限", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-put-parameters" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `dhcp-dns-server` | 类型：string；必填：否；默认值：—<br>DNS 服务器的 IP 地址 |
| `dhcp-range` | 类型：array；必填：否；默认值：—<br>此子网的 DHCP 地址范围列表 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dnszoneprefix` | 类型：string；必填：否；默认值：—<br>DNS 域区域前缀  例如：'adm' -&gt; &lt;hostname&gt;.adm.mydomain.com |
| `gateway` | 类型：string；必填：否；默认值：—<br>子网网关：对于 layer3 区域，将分配在 vnet 上 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `snat` | 类型：boolean；必填：否；默认值：—<br>使用 pve-firewall 时为此子网启用地址伪装 |
| `subnet` | 类型：string；必填：是；默认值：—<br>SDN 子网对象标识符。 |
| `vnet` | 类型：string；必填：否；默认值：—<br>关联的 vnet |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "dhcp-dns-server": {"description": "DNS 服务器的 IP 地址", "format": "ip", "optional": 1, "type": "string", "typetext": "<string>"},
    "dhcp-range": {
      "description": "此子网的 DHCP 地址范围列表", "items": {"format": "pve-sdn-dhcp-range", "type": "string"}, "optional": 1, "type": "array",
      "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dnszoneprefix": {
      "description": "DNS 域区域前缀  例如：'adm' -> <hostname>.adm.mydomain.com", "format": "dns-name", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "gateway": {"description": "子网网关：对于 layer3 区域，将分配在 vnet 上", "format": "ip", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "snat": {"description": "使用 pve-firewall 时为此子网启用地址伪装", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "subnet": {"description": "SDN 子网对象标识符。", "format": "pve-sdn-subnet-id", "type": "string", "typetext": "<string>"},
    "vnet": {"description": "关联的 vnet", "optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-put-returns" id="api-cluster-sdn-vnets-vnet-subnets-subnet-adb39970-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/subnets/{subnet})。

## `/cluster/sdn/vnets/{vnet}/ips` <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44"></a>

原始接口路径：`/cluster/sdn/vnets/{vnet}/ips`。

### DELETE `/cluster/sdn/vnets/{vnet}/ips` <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-delete" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-delete"></a>

删除 VNet 中的 IP 映射

**方法标识：** `ipdelete`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}/{vnet}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-delete-parameters" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `ip` | 类型：string；必填：是；默认值：—<br>要删除的 IP 地址 |
| `mac` | 类型：string；必填：否；默认值：—<br>未设置 I/G（个体/组）位的普通 MAC 地址。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "ip": {"description": "要删除的 IP 地址", "format": "ip", "type": "string", "typetext": "<string>"},
    "mac": {
      "description": "单播 MAC 地址。", "format": "mac-addr", "format_description": "XX:XX:XX:XX:XX:XX", "optional": 1, "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>", "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
    },
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-delete-returns" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-delete-returns"></a>

```text
{"type": "null"}
```

### POST `/cluster/sdn/vnets/{vnet}/ips` <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-post" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-post"></a>

在 VNet 中创建 IP 映射

**方法标识：** `ipcreate`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}/{vnet}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-post-parameters" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `ip` | 类型：string；必填：是；默认值：—<br>要与给定 MAC 地址关联的 IP 地址 |
| `mac` | 类型：string；必填：否；默认值：—<br>未设置 I/G（个体/组）位的普通 MAC 地址。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "ip": {"description": "要与给定 MAC 地址关联的 IP 地址", "format": "ip", "type": "string", "typetext": "<string>"},
    "mac": {
      "description": "单播 MAC 地址。", "format": "mac-addr", "format_description": "XX:XX:XX:XX:XX:XX", "optional": 1, "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>", "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
    },
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-post-returns" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-post-returns"></a>

```text
{"type": "null"}
```

### PUT `/cluster/sdn/vnets/{vnet}/ips` <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-put" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-put"></a>

更新 VNet 中的 IP 映射

**方法标识：** `ipupdate`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}/{vnet}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-put-parameters" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `ip` | 类型：string；必填：是；默认值：—<br>要与给定 MAC 地址关联的 IP 地址 |
| `mac` | 类型：string；必填：否；默认值：—<br>未设置 I/G（个体/组）位的普通 MAC 地址。 |
| `vmid` | 类型：integer；必填：否；默认值：—<br>虚拟机的（唯一）ID。 |
| `vnet` | 类型：string；必填：是；默认值：—<br>SDN vnet 对象标识符。 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "ip": {"description": "要与给定 MAC 地址关联的 IP 地址", "format": "ip", "type": "string", "typetext": "<string>"},
    "mac": {
      "description": "单播 MAC 地址。", "format": "mac-addr", "format_description": "XX:XX:XX:XX:XX:XX", "optional": 1, "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>", "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "optional": 1, "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "vnet": {"description": "SDN vnet 对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-vnets-vnet-ips-4cd47c44-put-returns" id="api-cluster-sdn-vnets-vnet-ips-4cd47c44-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/ips)。

## `/cluster/sdn/zones` <a href="#api-cluster-sdn-zones-f334f5a6" id="api-cluster-sdn-zones-f334f5a6"></a>

原始接口路径：`/cluster/sdn/zones`。

### GET `/cluster/sdn/zones` <a href="#api-cluster-sdn-zones-f334f5a6-get" id="api-cluster-sdn-zones-f334f5a6-get"></a>

SDN 区域索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/zones/<zone>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-zones-f334f5a6-get-parameters" id="api-cluster-sdn-zones-f334f5a6-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的 SDN 区域；可选值：`evpn`, `faucet`, `qinq`, `simple`, `vlan`, `vxlan` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "type": {"description": "仅列出特定类型的 SDN 区域", "enum": ["evpn", "faucet", "qinq", "simple", "vlan", "vxlan"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-zones-f334f5a6-get-returns" id="api-cluster-sdn-zones-f334f5a6-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "advertise-subnets": {
        "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"
      },
      "bridge": {"description": "要管理其 VLAN 的网桥。仅适用于 VLAN 和 QinQ 区域。", "optional": 1, "type": "string"},
      "bridge-disable-mac-learning": {"description": "禁用自动 MAC 学习。仅适用于 VLAN 区域。", "optional": 1, "type": "boolean"},
      "controller": {"description": "此区域的控制器 ID。仅适用于 EVPN 区域。", "optional": 1, "type": "string"},
      "dhcp": {"description": "此区域的 DHCP 服务器后端名称。", "enum": ["dnsmasq"], "optional": 1, "type": "string"},
      "digest": {"description": "控制器配置节的摘要。", "optional": 1, "type": "string"},
      "disable-arp-nd-suppression": {"description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
      "dns": {"description": "此区域的 DNS 服务器 ID。", "optional": 1, "type": "string"},
      "dnszone": {"description": "此区域的域名。", "optional": 1, "type": "string"},
      "exitnodes": {"description": "应充当此区域出口节点的 PVE 节点列表。仅适用于 EVPN 区域。", "format": "pve-node-list", "optional": 1, "type": "string"},
      "exitnodes-local-routing": {"description": "在出口节点上创建路由，使其能够连接 EVPN 客户机。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
      "exitnodes-primary": {"description": "强制流量首先经过此出口节点。仅适用于 EVPN 区域。", "format": "pve-node", "optional": 1, "type": "string"},
      "ipam": {"description": "此区域的 IPAM ID。", "optional": 1, "type": "string"},
      "mac": {"description": "此区域任播路由器的 MAC 地址。", "optional": 1, "type": "string"},
      "mtu": {"description": "区域的 MTU，将用于创建的 VNet 网桥。", "optional": 1, "type": "integer"},
      "nodes": {"description": "应创建此区域的节点。", "optional": 1, "type": "string"},
      "peers": {
        "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。仅适用于 VXLAN 区域。", "format": "ip-list", "optional": 1,
        "type": "string"
      },
      "pending": {
        "description": "尚未应用到运行配置的更改。", "optional": 1,
        "properties": {
          "advertise-subnets": {
            "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"
          },
          "bridge": {"description": "要管理其 VLAN 的网桥。仅适用于 VLAN 和 QinQ 区域。", "optional": 1, "type": "string"},
          "bridge-disable-mac-learning": {"description": "禁用自动 MAC 学习。仅适用于 VLAN 区域。", "optional": 1, "type": "boolean"},
          "controller": {"description": "此区域的控制器 ID。仅适用于 EVPN 区域。", "optional": 1, "type": "string"},
          "dhcp": {"description": "此区域的 DHCP 服务器后端名称。", "enum": ["dnsmasq"], "optional": 1, "type": "string"},
          "disable-arp-nd-suppression": {"description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
          "dns": {"description": "此区域的 DNS 服务器 ID。", "optional": 1, "type": "string"},
          "dnszone": {"description": "此区域的域名。", "optional": 1, "type": "string"},
          "exitnodes": {"description": "应充当此区域出口节点的 PVE 节点列表。仅适用于 EVPN 区域。", "format": "pve-node-list", "optional": 1, "type": "string"},
          "exitnodes-local-routing": {"description": "在出口节点上创建路由，使其能够连接 EVPN 客户机。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
          "exitnodes-primary": {"description": "强制流量首先经过此出口节点。仅适用于 EVPN 区域。", "format": "pve-node", "optional": 1, "type": "string"},
          "ipam": {"description": "此区域的 IPAM ID。", "optional": 1, "type": "string"},
          "mac": {"description": "此区域任播路由器的 MAC 地址。", "optional": 1, "type": "string"},
          "mtu": {"description": "区域的 MTU，将用于创建的 VNet 网桥。", "optional": 1, "type": "integer"},
          "nodes": {"description": "应创建此区域的节点。", "optional": 1, "type": "string"},
          "peers": {
            "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。仅适用于 VXLAN 区域。", "format": "ip-list", "optional": 1,
            "type": "string"
          },
          "reversedns": {"description": "此区域的反向 DNS 服务器 ID。", "optional": 1, "type": "string"},
          "rt-import": {
            "description": "应通过 BGP 导入此区域 VRF 的 Route-Target。仅适用于 EVPN 区域。", "format": "pve-sdn-bgp-rt-list", "optional": 1, "type": "string"
          },
          "secondary-controllers": {
            "description": "附加控制器。",
            "items": {"description": "控制器 ID。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
            "optional": 1, "type": "array"
          },
          "tag": {"description": "Service-VLAN 标签（外层 VLAN）。仅适用于 QinQ 区域", "minimum": 0, "optional": 1, "type": "integer"},
          "vlan-protocol": {
            "default": "802.1q", "description": "创建 QinQ 区域所用的 VLAN 协议。仅适用于 QinQ 区域。", "enum": ["802.1q", "802.1ad"], "optional": 1,
            "type": "string"
          },
          "vrf-vxlan": {"description": "区域 VRF 的 VNI。仅适用于 EVPN 区域。", "maximum": 16777215, "minimum": 1, "optional": 1, "type": "integer"},
          "vxlan-port": {
            "default": 4789, "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。仅适用于 VXLAN 区域。", "maximum": 65536, "minimum": 1, "optional": 1,
            "type": "integer"
          }
        },
        "type": "object"
      },
      "reversedns": {"description": "此区域的反向 DNS 服务器 ID。", "optional": 1, "type": "string"},
      "rt-import": {
        "description": "应通过 BGP 导入此区域 VRF 的 Route-Target。仅适用于 EVPN 区域。", "format": "pve-sdn-bgp-rt-list", "optional": 1, "type": "string"
      },
      "secondary-controllers": {
        "description": "附加控制器。",
        "items": {"description": "控制器 ID。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
        "optional": 1, "type": "array"
      },
      "state": {"description": "SDN 配置对象的状态。", "enum": ["new", "changed", "deleted"], "optional": 1, "type": "string"},
      "tag": {"description": "Service-VLAN 标签（外层 VLAN）。仅适用于 QinQ 区域", "minimum": 0, "optional": 1, "type": "integer"},
      "type": {"description": "区域类型。", "enum": ["evpn", "faucet", "qinq", "simple", "vlan", "vxlan"], "type": "string"},
      "vlan-protocol": {
        "default": "802.1q", "description": "创建 QinQ 区域所用的 VLAN 协议。仅适用于 QinQ 区域。", "enum": ["802.1q", "802.1ad"], "optional": 1,
        "type": "string"
      },
      "vrf-vxlan": {"description": "区域 VRF 的 VNI。仅适用于 EVPN 区域。", "maximum": 16777215, "minimum": 1, "optional": 1, "type": "integer"},
      "vxlan-port": {
        "default": 4789, "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。仅适用于 VXLAN 区域。", "maximum": 65536, "minimum": 1, "optional": 1,
        "type": "integer"
      },
      "zone": {"description": "区域名称。", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{zone}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/zones` <a href="#api-cluster-sdn-zones-f334f5a6-post" id="api-cluster-sdn-zones-f334f5a6-post"></a>

创建新的 SDN 区域对象。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/sdn/zones", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-zones-f334f5a6-post-parameters" id="api-cluster-sdn-zones-f334f5a6-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `advertise-subnets` | 类型：boolean；必填：否；默认值：—<br>通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。 |
| `bridge` | 类型：string；必填：否；默认值：—<br>要管理其 VLAN 的网桥。 |
| `bridge-disable-mac-learning` | 类型：boolean；必填：否；默认值：—<br>禁用自动 MAC 学习。 |
| `controller` | 类型：string；必填：否；默认值：—<br>此区域的控制器。 |
| `dhcp` | 类型：string；必填：否；默认值：—<br>此区域的 DHCP 后端类型；可选值：`dnsmasq` |
| `disable-arp-nd-suppression` | 类型：boolean；必填：否；默认值：—<br>抑制 IPv4 ARP 和 IPv6 邻居发现消息。 |
| `dns` | 类型：string；必填：否；默认值：—<br>DNS API 服务器 |
| `dnszone` | 类型：string；必填：否；默认值：—<br>DNS 域区域  例如：mydomain.com |
| `dp-id` | 类型：integer；必填：否；默认值：—<br>Faucet 数据平面 ID |
| `exitnodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `exitnodes-local-routing` | 类型：boolean；必填：否；默认值：—<br>允许出口节点连接 EVPN 客户机。 |
| `exitnodes-primary` | 类型：string；必填：否；默认值：—<br>强制流量首先经过此出口节点。 |
| `fabric` | 类型：string；必填：否；默认值：—<br>此 VXLAN 区域用作底层网络的 SDN fabric。 |
| `ipam` | 类型：string；必填：否；默认值：—<br>使用指定的 ipam |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `mac` | 类型：string；必填：否；默认值：—<br>任播逻辑路由器 MAC 地址。 |
| `mtu` | 类型：integer；必填：否；默认值：—<br>区域的 MTU，将用于创建的 VNet 网桥。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `peers` | 类型：string；必填：否；默认值：—<br>属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。 |
| `reversedns` | 类型：string；必填：否；默认值：—<br>反向 DNS API 服务器 |
| `rt-import` | 类型：string；必填：否；默认值：—<br>应导入此区域 VRF 的 Route Target 列表。 |
| `secondary-controllers` | 类型：array；必填：否；默认值：—<br>附加控制器。 |
| `tag` | 类型：integer；必填：否；默认值：—<br>Service-VLAN 标签（外层 VLAN） |
| `type` | 类型：string；必填：是；默认值：—<br>插件类型。；可选值：`evpn`, `faucet`, `qinq`, `simple`, `vlan`, `vxlan` |
| `vlan-protocol` | 类型：string；必填：否；默认值："802.1q"<br>创建 QinQ 区域应使用的 VLAN 协议。；可选值：`802.1q`, `802.1ad` |
| `vrf-vxlan` | 类型：integer；必填：否；默认值：—<br>区域 VRF 的 VNI。 |
| `vxlan-port` | 类型：integer；必填：否；默认值：4789<br>VXLAN 隧道应使用的 UDP 端口（默认 4789）。 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "advertise-subnets": {
      "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "bridge": {"description": "要管理其 VLAN 的网桥。", "optional": 1, "type": "string", "typetext": "<string>"},
    "bridge-disable-mac-learning": {"description": "禁用自动 MAC 学习。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "controller": {"description": "此区域的控制器。", "optional": 1, "type": "string", "typetext": "<string>"},
    "dhcp": {"description": "此区域的 DHCP 后端类型", "enum": ["dnsmasq"], "optional": 1, "type": "string"},
    "disable-arp-nd-suppression": {"description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "dns": {"description": "DNS API 服务器", "optional": 1, "type": "string", "typetext": "<string>"},
    "dnszone": {"description": "DNS 域区域  例如：mydomain.com", "format": "dns-name", "optional": 1, "type": "string", "typetext": "<string>"},
    "dp-id": {"description": "Faucet 数据平面 ID", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "exitnodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "exitnodes-local-routing": {"description": "允许出口节点连接 EVPN 客户机。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "exitnodes-primary": {"description": "强制流量首先经过此出口节点。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "fabric": {
      "description": "此 VXLAN 区域用作底层网络的 SDN fabric。", "format": "pve-sdn-fabric-id", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "ipam": {"description": "使用指定的 ipam", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "mac": {"description": "任播逻辑路由器 MAC 地址。", "format": "mac-addr", "optional": 1, "type": "string", "typetext": "<string>"},
    "mtu": {"description": "区域的 MTU，将用于创建的 VNet 网桥。", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "peers": {
      "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。", "format": "ip-list", "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "reversedns": {"description": "反向 DNS API 服务器", "optional": 1, "type": "string", "typetext": "<string>"},
    "rt-import": {
      "description": "应导入此区域 VRF 的 Route Target 列表。", "format": "pve-sdn-bgp-rt-list", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "secondary-controllers": {
      "description": "附加控制器。",
      "items": {"description": "控制器 ID。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "tag": {"description": "Service-VLAN 标签（外层 VLAN）", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "type": {"description": "插件类型。", "enum": ["evpn", "faucet", "qinq", "simple", "vlan", "vxlan"], "format": "pve-configid", "type": "string"},
    "vlan-protocol": {"default": "802.1q", "description": "创建 QinQ 区域应使用的 VLAN 协议。", "enum": ["802.1q", "802.1ad"], "optional": 1, "type": "string"},
    "vrf-vxlan": {
      "description": "区域 VRF 的 VNI。", "maximum": 16777215, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 16777215)"
    },
    "vxlan-port": {
      "default": 4789, "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。", "maximum": 65536, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-zones-f334f5a6-post-returns" id="api-cluster-sdn-zones-f334f5a6-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/zones)。

## `/cluster/sdn/zones/{zone}` <a href="#api-cluster-sdn-zones-zone-972e538e" id="api-cluster-sdn-zones-zone-972e538e"></a>

原始接口路径：`/cluster/sdn/zones/{zone}`。

### DELETE `/cluster/sdn/zones/{zone}` <a href="#api-cluster-sdn-zones-zone-972e538e-delete" id="api-cluster-sdn-zones-zone-972e538e-delete"></a>

删除 SDN 区域对象配置。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-zones-zone-972e538e-delete-parameters" id="api-cluster-sdn-zones-zone-972e538e-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-zones-zone-972e538e-delete-returns" id="api-cluster-sdn-zones-zone-972e538e-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/zones/{zone}` <a href="#api-cluster-sdn-zones-zone-972e538e-get" id="api-cluster-sdn-zones-zone-972e538e-get"></a>

读取 SDN 区域配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-zones-zone-972e538e-get-parameters" id="api-cluster-sdn-zones-zone-972e538e-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-zones-zone-972e538e-get-returns" id="api-cluster-sdn-zones-zone-972e538e-get-returns"></a>

```text
{
  "properties": {
    "advertise-subnets": {"description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
    "bridge": {"description": "要管理其 VLAN 的网桥。仅适用于 VLAN 和 QinQ 区域。", "optional": 1, "type": "string"},
    "bridge-disable-mac-learning": {"description": "禁用自动 MAC 学习。仅适用于 VLAN 区域。", "optional": 1, "type": "boolean"},
    "controller": {"description": "此区域的控制器 ID。仅适用于 EVPN 区域。", "optional": 1, "type": "string"},
    "dhcp": {"description": "此区域的 DHCP 服务器后端名称。", "enum": ["dnsmasq"], "optional": 1, "type": "string"},
    "digest": {"description": "控制器配置节的摘要。", "optional": 1, "type": "string"},
    "disable-arp-nd-suppression": {"description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
    "dns": {"description": "此区域的 DNS 服务器 ID。", "optional": 1, "type": "string"},
    "dnszone": {"description": "此区域的域名。", "optional": 1, "type": "string"},
    "exitnodes": {"description": "应充当此区域出口节点的 PVE 节点列表。仅适用于 EVPN 区域。", "format": "pve-node-list", "optional": 1, "type": "string"},
    "exitnodes-local-routing": {"description": "在出口节点上创建路由，使其能够连接 EVPN 客户机。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
    "exitnodes-primary": {"description": "强制流量首先经过此出口节点。仅适用于 EVPN 区域。", "format": "pve-node", "optional": 1, "type": "string"},
    "ipam": {"description": "此区域的 IPAM ID。", "optional": 1, "type": "string"},
    "mac": {"description": "此区域任播路由器的 MAC 地址。", "optional": 1, "type": "string"},
    "mtu": {"description": "区域的 MTU，将用于创建的 VNet 网桥。", "optional": 1, "type": "integer"},
    "nodes": {"description": "应创建此区域的节点。", "optional": 1, "type": "string"},
    "peers": {
      "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。仅适用于 VXLAN 区域。", "format": "ip-list", "optional": 1,
      "type": "string"
    },
    "pending": {
      "description": "尚未应用到运行配置的更改。", "optional": 1,
      "properties": {
        "advertise-subnets": {
          "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"
        },
        "bridge": {"description": "要管理其 VLAN 的网桥。仅适用于 VLAN 和 QinQ 区域。", "optional": 1, "type": "string"},
        "bridge-disable-mac-learning": {"description": "禁用自动 MAC 学习。仅适用于 VLAN 区域。", "optional": 1, "type": "boolean"},
        "controller": {"description": "此区域的控制器 ID。仅适用于 EVPN 区域。", "optional": 1, "type": "string"},
        "dhcp": {"description": "此区域的 DHCP 服务器后端名称。", "enum": ["dnsmasq"], "optional": 1, "type": "string"},
        "disable-arp-nd-suppression": {"description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
        "dns": {"description": "此区域的 DNS 服务器 ID。", "optional": 1, "type": "string"},
        "dnszone": {"description": "此区域的域名。", "optional": 1, "type": "string"},
        "exitnodes": {"description": "应充当此区域出口节点的 PVE 节点列表。仅适用于 EVPN 区域。", "format": "pve-node-list", "optional": 1, "type": "string"},
        "exitnodes-local-routing": {"description": "在出口节点上创建路由，使其能够连接 EVPN 客户机。仅适用于 EVPN 区域。", "optional": 1, "type": "boolean"},
        "exitnodes-primary": {"description": "强制流量首先经过此出口节点。仅适用于 EVPN 区域。", "format": "pve-node", "optional": 1, "type": "string"},
        "ipam": {"description": "此区域的 IPAM ID。", "optional": 1, "type": "string"},
        "mac": {"description": "此区域任播路由器的 MAC 地址。", "optional": 1, "type": "string"},
        "mtu": {"description": "区域的 MTU，将用于创建的 VNet 网桥。", "optional": 1, "type": "integer"},
        "nodes": {"description": "应创建此区域的节点。", "optional": 1, "type": "string"},
        "peers": {
          "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。仅适用于 VXLAN 区域。", "format": "ip-list", "optional": 1,
          "type": "string"
        },
        "reversedns": {"description": "此区域的反向 DNS 服务器 ID。", "optional": 1, "type": "string"},
        "rt-import": {
          "description": "应通过 BGP 导入此区域 VRF 的 Route-Target。仅适用于 EVPN 区域。", "format": "pve-sdn-bgp-rt-list", "optional": 1, "type": "string"
        },
        "secondary-controllers": {
          "description": "附加控制器。",
          "items": {"description": "控制器 ID。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
          "optional": 1, "type": "array"
        },
        "tag": {"description": "Service-VLAN 标签（外层 VLAN）。仅适用于 QinQ 区域", "minimum": 0, "optional": 1, "type": "integer"},
        "vlan-protocol": {
          "default": "802.1q", "description": "创建 QinQ 区域所用的 VLAN 协议。仅适用于 QinQ 区域。", "enum": ["802.1q", "802.1ad"], "optional": 1,
          "type": "string"
        },
        "vrf-vxlan": {"description": "区域 VRF 的 VNI。仅适用于 EVPN 区域。", "maximum": 16777215, "minimum": 1, "optional": 1, "type": "integer"},
        "vxlan-port": {
          "default": 4789, "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。仅适用于 VXLAN 区域。", "maximum": 65536, "minimum": 1, "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "reversedns": {"description": "此区域的反向 DNS 服务器 ID。", "optional": 1, "type": "string"},
    "rt-import": {
      "description": "应通过 BGP 导入此区域 VRF 的 Route-Target。仅适用于 EVPN 区域。", "format": "pve-sdn-bgp-rt-list", "optional": 1, "type": "string"
    },
    "secondary-controllers": {
      "description": "附加控制器。",
      "items": {"description": "控制器 ID。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"}, "optional": 1,
      "type": "array"
    },
    "state": {"description": "SDN 配置对象的状态。", "enum": ["new", "changed", "deleted"], "optional": 1, "type": "string"},
    "tag": {"description": "Service-VLAN 标签（外层 VLAN）。仅适用于 QinQ 区域", "minimum": 0, "optional": 1, "type": "integer"},
    "type": {"description": "区域类型。", "enum": ["evpn", "faucet", "qinq", "simple", "vlan", "vxlan"], "type": "string"},
    "vlan-protocol": {
      "default": "802.1q", "description": "创建 QinQ 区域所用的 VLAN 协议。仅适用于 QinQ 区域。", "enum": ["802.1q", "802.1ad"], "optional": 1, "type": "string"
    },
    "vrf-vxlan": {"description": "区域 VRF 的 VNI。仅适用于 EVPN 区域。", "maximum": 16777215, "minimum": 1, "optional": 1, "type": "integer"},
    "vxlan-port": {
      "default": 4789, "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。仅适用于 VXLAN 区域。", "maximum": 65536, "minimum": 1, "optional": 1,
      "type": "integer"
    },
    "zone": {"description": "区域名称。", "type": "string"}
  }
}
```

### PUT `/cluster/sdn/zones/{zone}` <a href="#api-cluster-sdn-zones-zone-972e538e-put" id="api-cluster-sdn-zones-zone-972e538e-put"></a>

更新 SDN 区域对象配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/sdn/zones/{zone}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-zones-zone-972e538e-put-parameters" id="api-cluster-sdn-zones-zone-972e538e-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `advertise-subnets` | 类型：boolean；必填：否；默认值：—<br>通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。 |
| `bridge` | 类型：string；必填：否；默认值：—<br>要管理其 VLAN 的网桥。 |
| `bridge-disable-mac-learning` | 类型：boolean；必填：否；默认值：—<br>禁用自动 MAC 学习。 |
| `controller` | 类型：string；必填：否；默认值：—<br>此区域的控制器。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `dhcp` | 类型：string；必填：否；默认值：—<br>此区域的 DHCP 后端类型；可选值：`dnsmasq` |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable-arp-nd-suppression` | 类型：boolean；必填：否；默认值：—<br>抑制 IPv4 ARP 和 IPv6 邻居发现消息。 |
| `dns` | 类型：string；必填：否；默认值：—<br>DNS API 服务器 |
| `dnszone` | 类型：string；必填：否；默认值：—<br>DNS 域区域  例如：mydomain.com |
| `dp-id` | 类型：integer；必填：否；默认值：—<br>Faucet 数据平面 ID |
| `exitnodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `exitnodes-local-routing` | 类型：boolean；必填：否；默认值：—<br>允许出口节点连接 EVPN 客户机。 |
| `exitnodes-primary` | 类型：string；必填：否；默认值：—<br>强制流量首先经过此出口节点。 |
| `fabric` | 类型：string；必填：否；默认值：—<br>此 VXLAN 区域用作底层网络的 SDN fabric。 |
| `ipam` | 类型：string；必填：否；默认值：—<br>使用指定的 ipam |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `mac` | 类型：string；必填：否；默认值：—<br>任播逻辑路由器 MAC 地址。 |
| `mtu` | 类型：integer；必填：否；默认值：—<br>区域的 MTU，将用于创建的 VNet 网桥。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `peers` | 类型：string；必填：否；默认值：—<br>属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。 |
| `reversedns` | 类型：string；必填：否；默认值：—<br>反向 DNS API 服务器 |
| `rt-import` | 类型：string；必填：否；默认值：—<br>应导入此区域 VRF 的 Route Target 列表。 |
| `secondary-controllers` | 类型：array；必填：否；默认值：—<br>附加控制器。 |
| `tag` | 类型：integer；必填：否；默认值：—<br>Service-VLAN 标签（外层 VLAN） |
| `vlan-protocol` | 类型：string；必填：否；默认值："802.1q"<br>创建 QinQ 区域应使用的 VLAN 协议。；可选值：`802.1q`, `802.1ad` |
| `vrf-vxlan` | 类型：integer；必填：否；默认值：—<br>区域 VRF 的 VNI。 |
| `vxlan-port` | 类型：integer；必填：否；默认值：4789<br>VXLAN 隧道应使用的 UDP 端口（默认 4789）。 |
| `zone` | 类型：string；必填：是；默认值：—<br>SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "advertise-subnets": {
      "description": "通告 IP 前缀（Type-5 路由），而非 MAC/IP 对（Type-2 路由）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"
    },
    "bridge": {"description": "要管理其 VLAN 的网桥。", "optional": 1, "type": "string", "typetext": "<string>"},
    "bridge-disable-mac-learning": {"description": "禁用自动 MAC 学习。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "controller": {"description": "此区域的控制器。", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "dhcp": {"description": "此区域的 DHCP 后端类型", "enum": ["dnsmasq"], "optional": 1, "type": "string"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "disable-arp-nd-suppression": {"description": "抑制 IPv4 ARP 和 IPv6 邻居发现消息。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "dns": {"description": "DNS API 服务器", "optional": 1, "type": "string", "typetext": "<string>"},
    "dnszone": {"description": "DNS 域区域  例如：mydomain.com", "format": "dns-name", "optional": 1, "type": "string", "typetext": "<string>"},
    "dp-id": {"description": "Faucet 数据平面 ID", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "exitnodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "exitnodes-local-routing": {"description": "允许出口节点连接 EVPN 客户机。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "exitnodes-primary": {"description": "强制流量首先经过此出口节点。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "fabric": {
      "description": "此 VXLAN 区域用作底层网络的 SDN fabric。", "format": "pve-sdn-fabric-id", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "ipam": {"description": "使用指定的 ipam", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "mac": {"description": "任播逻辑路由器 MAC 地址。", "format": "mac-addr", "optional": 1, "type": "string", "typetext": "<string>"},
    "mtu": {"description": "区域的 MTU，将用于创建的 VNet 网桥。", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "peers": {
      "description": "属于 VXLAN 区域的对等端列表，以逗号分隔。通常为节点的 IP 地址。", "format": "ip-list", "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "reversedns": {"description": "反向 DNS API 服务器", "optional": 1, "type": "string", "typetext": "<string>"},
    "rt-import": {
      "description": "应导入此区域 VRF 的 Route Target 列表。", "format": "pve-sdn-bgp-rt-list", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "secondary-controllers": {
      "description": "附加控制器。",
      "items": {"description": "控制器 ID。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"}, "optional": 1,
      "type": "array", "typetext": "<array>"
    },
    "tag": {"description": "Service-VLAN 标签（外层 VLAN）", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "vlan-protocol": {"default": "802.1q", "description": "创建 QinQ 区域应使用的 VLAN 协议。", "enum": ["802.1q", "802.1ad"], "optional": 1, "type": "string"},
    "vrf-vxlan": {
      "description": "区域 VRF 的 VNI。", "maximum": 16777215, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 16777215)"
    },
    "vxlan-port": {
      "default": 4789, "description": "VXLAN 隧道应使用的 UDP 端口（默认 4789）。", "maximum": 65536, "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "zone": {"description": "SDN 区域对象标识符。", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-zones-zone-972e538e-put-returns" id="api-cluster-sdn-zones-zone-972e538e-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/zones/{zone})。

## `/cluster/sdn/controllers` <a href="#api-cluster-sdn-controllers-169ade17" id="api-cluster-sdn-controllers-169ade17"></a>

原始接口路径：`/cluster/sdn/controllers`。

### GET `/cluster/sdn/controllers` <a href="#api-cluster-sdn-controllers-169ade17-get" id="api-cluster-sdn-controllers-169ade17-get"></a>

SDN 控制器索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/controllers/<controller>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-controllers-169ade17-get-parameters" id="api-cluster-sdn-controllers-169ade17-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的 SDN 控制器；可选值：`bgp`, `evpn`, `faucet`, `isis` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "type": {"description": "仅列出特定类型的 SDN 控制器", "enum": ["bgp", "evpn", "faucet", "isis"], "optional": 1, "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-controllers-169ade17-get-returns" id="api-cluster-sdn-controllers-169ade17-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "asn": {"description": "控制器的本地 ASN。仅适用于 BGP 和 EVPN。", "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer"},
      "bgp-mode": {
        "default": "auto", "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。", "enum": ["auto", "external", "internal"],
        "optional": 1, "type": "string"
      },
      "bgp-multipath-as-relax": {"description": "在多路径计算中考虑长度相等的不同 AS 路径。仅适用于 BGP。", "optional": 1, "type": "boolean"},
      "controller": {"description": "控制器名称。", "type": "string"}, "digest": {"description": "控制器配置节的摘要。", "optional": 1, "type": "string"},
      "ebgp": {"description": "启用 eBGP（remote-as external）。仅适用于 BGP。", "optional": 1, "type": "boolean"},
      "ebgp-multihop": {"description": "设置 eBGP 对等端的最大跳数。需要将 ebgp 设为 1。仅适用于 BGP。", "optional": 1, "type": "integer"},
      "isis-domain": {"description": "IS-IS 域的名称。仅适用于 IS-IS。", "optional": 1, "type": "string"},
      "isis-ifaces": {"description": "应启用 IS-IS 的接口列表，以逗号分隔。仅适用于 IS-IS。", "format": "pve-iface-list", "optional": 1, "type": "string"},
      "isis-net": {"description": "此节点在 IS-IS 网络中的网络实体名称。仅适用于 IS-IS。", "format": "pve-sdn-isis-net", "optional": 1, "type": "string"},
      "loopback": {"description": "提供 Router-IP 的 loopback/dummy 接口名称。仅适用于 BGP。", "optional": 1, "type": "string"},
      "node": {"description": "启用此控制器的节点。", "optional": 1, "type": "string"},
      "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string"},
      "peer-group-name": {"description": "此 EVPN 控制器的对等组名称", "optional": 1, "type": "string"},
      "peers": {"description": "对等端 IP 地址列表，以逗号分隔。", "optional": 1, "type": "string"},
      "pending": {
        "description": "尚未应用到运行配置的更改。", "optional": 1,
        "properties": {
          "asn": {"description": "控制器的本地 ASN。仅适用于 BGP 和 EVPN。", "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer"},
          "bgp-mode": {
            "default": "auto", "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。", "enum": ["auto", "external", "internal"],
            "optional": 1, "type": "string"
          },
          "bgp-multipath-as-relax": {"description": "在多路径计算中考虑长度相等的不同 AS 路径。仅适用于 BGP。", "optional": 1, "type": "boolean"},
          "ebgp": {"description": "启用 eBGP（remote-as external）。仅适用于 BGP。", "optional": 1, "type": "boolean"},
          "ebgp-multihop": {"description": "设置 eBGP 对等端的最大跳数。需要将 ebgp 设为 1。仅适用于 BGP。", "optional": 1, "type": "integer"},
          "isis-domain": {"description": "IS-IS 域的名称。仅适用于 IS-IS。", "optional": 1, "type": "string"},
          "isis-ifaces": {"description": "应启用 IS-IS 的接口列表，以逗号分隔。仅适用于 IS-IS。", "format": "pve-iface-list", "optional": 1, "type": "string"},
          "isis-net": {"description": "此节点在 IS-IS 网络中的网络实体名称。仅适用于 IS-IS。", "format": "pve-sdn-isis-net", "optional": 1, "type": "string"},
          "loopback": {"description": "提供 Router-IP 的 loopback/dummy 接口名称。仅适用于 BGP。", "optional": 1, "type": "string"},
          "node": {"description": "启用此控制器的节点。", "optional": 1, "type": "string"},
          "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string"},
          "peer-group-name": {"description": "此 EVPN 控制器的对等组名称", "optional": 1, "type": "string"},
          "peers": {"description": "对等端 IP 地址列表，以逗号分隔。", "optional": 1, "type": "string"}
        },
        "type": "object"
      },
      "state": {"description": "SDN 配置对象的状态。", "enum": ["new", "changed", "deleted"], "optional": 1, "type": "string"},
      "type": {"description": "控制器类型", "enum": ["bgp", "evpn", "faucet", "isis"], "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{controller}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/controllers` <a href="#api-cluster-sdn-controllers-169ade17-post" id="api-cluster-sdn-controllers-169ade17-post"></a>

创建新的 SDN 控制器对象。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/sdn/controllers", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-controllers-169ade17-post-parameters" id="api-cluster-sdn-controllers-169ade17-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `asn` | 类型：integer；必填：否；默认值：—<br>自治系统编号 |
| `bgp-mode` | 类型：string；必填：否；默认值："auto"<br>使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。；可选值：`auto`, `external`, `internal` |
| `bgp-multipath-as-path-relax` | 类型：boolean；必填：否；默认值：—<br>在多路径计算中考虑长度相等的不同 AS 路径。 |
| `controller` | 类型：string；必填：是；默认值：—<br>SDN 控制器对象标识符。 |
| `ebgp` | 类型：boolean；必填：否；默认值：—<br>启用 eBGP（remote-as external）。 |
| `ebgp-multihop` | 类型：integer；必填：否；默认值：—<br>设置 eBGP 对等端的最大跳数。 |
| `fabric` | 类型：string；必填：否；默认值：—<br>此 EVPN 控制器用作底层网络的 SDN fabric。 |
| `isis-domain` | 类型：string；必填：否；默认值：—<br>IS-IS 域的名称。 |
| `isis-ifaces` | 类型：string；必填：否；默认值：—<br>应启用 IS-IS 的接口列表，以逗号分隔。 |
| `isis-net` | 类型：string；必填：否；默认值：—<br>此节点在 IS-IS 网络中的网络实体名称。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `loopback` | 类型：string；必填：否；默认值：—<br>提供 Router-IP 的 loopback/dummy 接口名称。 |
| `node` | 类型：string；必填：否；默认值：—<br>集群节点名称。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `peer-group-name` | 类型：string；必填：否；默认值："VTEP"<br>此 EVPN 控制器的对等组名称 |
| `peers` | 类型：string；必填：否；默认值：—<br>对等端地址列表。 |
| `route-map-in` | 类型：string；必填：否；默认值：—<br>应对传入路由应用的 Route Map |
| `route-map-out` | 类型：string；必填：否；默认值：—<br>应对传出路由应用的 Route Map |
| `type` | 类型：string；必填：是；默认值：—<br>插件类型。；可选值：`bgp`, `evpn`, `faucet`, `isis` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "asn": {"description": "自治系统编号", "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 4294967295)"},
    "bgp-mode": {
      "default": "auto", "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。", "enum": ["auto", "external", "internal"],
      "optional": 1, "type": "string"
    },
    "bgp-multipath-as-path-relax": {"description": "在多路径计算中考虑长度相等的不同 AS 路径。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "controller": {"description": "SDN 控制器对象标识符。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
    "ebgp": {"description": "启用 eBGP（remote-as external）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "ebgp-multihop": {"description": "设置 eBGP 对等端的最大跳数。", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "fabric": {
      "description": "此 EVPN 控制器用作底层网络的 SDN fabric。", "format": "pve-sdn-fabric-id", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "isis-domain": {"description": "IS-IS 域的名称。", "optional": 1, "type": "string", "typetext": "<string>"},
    "isis-ifaces": {
      "description": "应启用 IS-IS 的接口列表，以逗号分隔。", "format": "pve-iface-list", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "isis-net": {
      "description": "此节点在 IS-IS 网络中的网络实体名称。", "format": "pve-sdn-isis-net", "maxLength": 50, "minLength": 20, "optional": 1,
      "pattern": "[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}", "type": "string"
    },
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "loopback": {"description": "提供 Router-IP 的 loopback/dummy 接口名称。", "optional": 1, "type": "string", "typetext": "<string>"},
    "node": {"description": "集群节点名称。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "peer-group-name": {
      "default": "VTEP", "description": "此 EVPN 控制器的对等组名称", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "peers": {"description": "对等端地址列表。", "format": "ip-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "route-map-in": {"description": "应对传入路由应用的 Route Map", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string", "typetext": "<string>"},
    "route-map-out": {"description": "应对传出路由应用的 Route Map", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"description": "插件类型。", "enum": ["bgp", "evpn", "faucet", "isis"], "format": "pve-configid", "type": "string"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-controllers-169ade17-post-returns" id="api-cluster-sdn-controllers-169ade17-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/controllers)。

## `/cluster/sdn/controllers/{controller}` <a href="#api-cluster-sdn-controllers-controller-945537d7" id="api-cluster-sdn-controllers-controller-945537d7"></a>

原始接口路径：`/cluster/sdn/controllers/{controller}`。

### DELETE `/cluster/sdn/controllers/{controller}` <a href="#api-cluster-sdn-controllers-controller-945537d7-delete" id="api-cluster-sdn-controllers-controller-945537d7-delete"></a>

删除 SDN 控制器对象配置。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/sdn/controllers", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-controllers-controller-945537d7-delete-parameters" id="api-cluster-sdn-controllers-controller-945537d7-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `controller` | 类型：string；必填：是；默认值：—<br>SDN 控制器对象标识符。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "controller": {"description": "SDN 控制器对象标识符。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-controllers-controller-945537d7-delete-returns" id="api-cluster-sdn-controllers-controller-945537d7-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/controllers/{controller}` <a href="#api-cluster-sdn-controllers-controller-945537d7-get" id="api-cluster-sdn-controllers-controller-945537d7-get"></a>

读取 SDN 控制器配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/sdn/controllers/{controller}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-controllers-controller-945537d7-get-parameters" id="api-cluster-sdn-controllers-controller-945537d7-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `controller` | 类型：string；必填：是；默认值：—<br>SDN 控制器对象标识符。 |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "controller": {"description": "SDN 控制器对象标识符。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-controllers-controller-945537d7-get-returns" id="api-cluster-sdn-controllers-controller-945537d7-get-returns"></a>

```text
{
  "properties": {
    "asn": {"description": "控制器的本地 ASN。仅适用于 BGP 和 EVPN。", "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer"},
    "bgp-mode": {
      "default": "auto", "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。", "enum": ["auto", "external", "internal"],
      "optional": 1, "type": "string"
    },
    "bgp-multipath-as-relax": {"description": "在多路径计算中考虑长度相等的不同 AS 路径。仅适用于 BGP。", "optional": 1, "type": "boolean"},
    "controller": {"description": "控制器名称。", "type": "string"}, "digest": {"description": "控制器配置节的摘要。", "optional": 1, "type": "string"},
    "ebgp": {"description": "启用 eBGP（remote-as external）。仅适用于 BGP。", "optional": 1, "type": "boolean"},
    "ebgp-multihop": {"description": "设置 eBGP 对等端的最大跳数。需要将 ebgp 设为 1。仅适用于 BGP。", "optional": 1, "type": "integer"},
    "isis-domain": {"description": "IS-IS 域的名称。仅适用于 IS-IS。", "optional": 1, "type": "string"},
    "isis-ifaces": {"description": "应启用 IS-IS 的接口列表，以逗号分隔。仅适用于 IS-IS。", "format": "pve-iface-list", "optional": 1, "type": "string"},
    "isis-net": {"description": "此节点在 IS-IS 网络中的网络实体名称。仅适用于 IS-IS。", "format": "pve-sdn-isis-net", "optional": 1, "type": "string"},
    "loopback": {"description": "提供 Router-IP 的 loopback/dummy 接口名称。仅适用于 BGP。", "optional": 1, "type": "string"},
    "node": {"description": "启用此控制器的节点。", "optional": 1, "type": "string"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string"},
    "peer-group-name": {"description": "此 EVPN 控制器的对等组名称", "optional": 1, "type": "string"},
    "peers": {"description": "对等端 IP 地址列表，以逗号分隔。", "optional": 1, "type": "string"},
    "pending": {
      "description": "尚未应用到运行配置的更改。", "optional": 1,
      "properties": {
        "asn": {"description": "控制器的本地 ASN。仅适用于 BGP 和 EVPN。", "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer"},
        "bgp-mode": {
          "default": "auto", "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。", "enum": ["auto", "external", "internal"],
          "optional": 1, "type": "string"
        },
        "bgp-multipath-as-relax": {"description": "在多路径计算中考虑长度相等的不同 AS 路径。仅适用于 BGP。", "optional": 1, "type": "boolean"},
        "ebgp": {"description": "启用 eBGP（remote-as external）。仅适用于 BGP。", "optional": 1, "type": "boolean"},
        "ebgp-multihop": {"description": "设置 eBGP 对等端的最大跳数。需要将 ebgp 设为 1。仅适用于 BGP。", "optional": 1, "type": "integer"},
        "isis-domain": {"description": "IS-IS 域的名称。仅适用于 IS-IS。", "optional": 1, "type": "string"},
        "isis-ifaces": {"description": "应启用 IS-IS 的接口列表，以逗号分隔。仅适用于 IS-IS。", "format": "pve-iface-list", "optional": 1, "type": "string"},
        "isis-net": {"description": "此节点在 IS-IS 网络中的网络实体名称。仅适用于 IS-IS。", "format": "pve-sdn-isis-net", "optional": 1, "type": "string"},
        "loopback": {"description": "提供 Router-IP 的 loopback/dummy 接口名称。仅适用于 BGP。", "optional": 1, "type": "string"},
        "node": {"description": "启用此控制器的节点。", "optional": 1, "type": "string"},
        "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string"},
        "peer-group-name": {"description": "此 EVPN 控制器的对等组名称", "optional": 1, "type": "string"},
        "peers": {"description": "对等端 IP 地址列表，以逗号分隔。", "optional": 1, "type": "string"}
      },
      "type": "object"
    },
    "state": {"description": "SDN 配置对象的状态。", "enum": ["new", "changed", "deleted"], "optional": 1, "type": "string"},
    "type": {"description": "控制器类型", "enum": ["bgp", "evpn", "faucet", "isis"], "type": "string"}
  }
}
```

### PUT `/cluster/sdn/controllers/{controller}` <a href="#api-cluster-sdn-controllers-controller-945537d7-put" id="api-cluster-sdn-controllers-controller-945537d7-put"></a>

更新 SDN 控制器对象配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/sdn/controllers", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-controllers-controller-945537d7-put-parameters" id="api-cluster-sdn-controllers-controller-945537d7-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `asn` | 类型：integer；必填：否；默认值：—<br>自治系统编号 |
| `bgp-mode` | 类型：string；必填：否；默认值："auto"<br>使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。；可选值：`auto`, `external`, `internal` |
| `bgp-multipath-as-path-relax` | 类型：boolean；必填：否；默认值：—<br>在多路径计算中考虑长度相等的不同 AS 路径。 |
| `controller` | 类型：string；必填：是；默认值：—<br>SDN 控制器对象标识符。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `ebgp` | 类型：boolean；必填：否；默认值：—<br>启用 eBGP（remote-as external）。 |
| `ebgp-multihop` | 类型：integer；必填：否；默认值：—<br>设置 eBGP 对等端的最大跳数。 |
| `fabric` | 类型：string；必填：否；默认值：—<br>此 EVPN 控制器用作底层网络的 SDN fabric。 |
| `isis-domain` | 类型：string；必填：否；默认值：—<br>IS-IS 域的名称。 |
| `isis-ifaces` | 类型：string；必填：否；默认值：—<br>应启用 IS-IS 的接口列表，以逗号分隔。 |
| `isis-net` | 类型：string；必填：否；默认值：—<br>此节点在 IS-IS 网络中的网络实体名称。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `loopback` | 类型：string；必填：否；默认值：—<br>提供 Router-IP 的 loopback/dummy 接口名称。 |
| `node` | 类型：string；必填：否；默认值：—<br>集群节点名称。 |
| `nodes` | 类型：string；必填：否；默认值：—<br>集群节点名称列表。 |
| `peer-group-name` | 类型：string；必填：否；默认值："VTEP"<br>此 EVPN 控制器的对等组名称 |
| `peers` | 类型：string；必填：否；默认值：—<br>对等端地址列表。 |
| `route-map-in` | 类型：string；必填：否；默认值：—<br>应对传入路由应用的 Route Map |
| `route-map-out` | 类型：string；必填：否；默认值：—<br>应对传出路由应用的 Route Map |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "asn": {"description": "自治系统编号", "maximum": 4294967295, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 4294967295)"},
    "bgp-mode": {
      "default": "auto", "description": "使用 eBGP 还是 iBGP。自动模式根据 BGP 控制器选择，否则回退到 iBGP。", "enum": ["auto", "external", "internal"],
      "optional": 1, "type": "string"
    },
    "bgp-multipath-as-path-relax": {"description": "在多路径计算中考虑长度相等的不同 AS 路径。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "controller": {"description": "SDN 控制器对象标识符。", "maxLength": 64, "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9]", "type": "string"},
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "ebgp": {"description": "启用 eBGP（remote-as external）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "ebgp-multihop": {"description": "设置 eBGP 对等端的最大跳数。", "optional": 1, "type": "integer", "typetext": "<integer>"},
    "fabric": {
      "description": "此 EVPN 控制器用作底层网络的 SDN fabric。", "format": "pve-sdn-fabric-id", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "isis-domain": {"description": "IS-IS 域的名称。", "optional": 1, "type": "string", "typetext": "<string>"},
    "isis-ifaces": {
      "description": "应启用 IS-IS 的接口列表，以逗号分隔。", "format": "pve-iface-list", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "isis-net": {
      "description": "此节点在 IS-IS 网络中的网络实体名称。", "format": "pve-sdn-isis-net", "maxLength": 50, "minLength": 20, "optional": 1,
      "pattern": "[a-fA-F0-9]{2}(\\.[a-fA-F0-9]{4}){3,9}\\.[a-fA-F0-9]{2}", "type": "string"
    },
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "loopback": {"description": "提供 Router-IP 的 loopback/dummy 接口名称。", "optional": 1, "type": "string", "typetext": "<string>"},
    "node": {"description": "集群节点名称。", "format": "pve-node", "optional": 1, "type": "string", "typetext": "<string>"},
    "nodes": {"description": "集群节点名称列表。", "format": "pve-node-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "peer-group-name": {
      "default": "VTEP", "description": "此 EVPN 控制器的对等组名称", "format": "pve-configid", "optional": 1, "type": "string", "typetext": "<string>"
    },
    "peers": {"description": "对等端地址列表。", "format": "ip-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "route-map-in": {"description": "应对传入路由应用的 Route Map", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string", "typetext": "<string>"},
    "route-map-out": {"description": "应对传出路由应用的 Route Map", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-controllers-controller-945537d7-put-returns" id="api-cluster-sdn-controllers-controller-945537d7-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/controllers/{controller})。

## `/cluster/sdn/ipams` <a href="#api-cluster-sdn-ipams-8dacb8c6" id="api-cluster-sdn-ipams-8dacb8c6"></a>

原始接口路径：`/cluster/sdn/ipams`。

### GET `/cluster/sdn/ipams` <a href="#api-cluster-sdn-ipams-8dacb8c6-get" id="api-cluster-sdn-ipams-8dacb8c6-get"></a>

SDN ipam 索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/ipams/<ipam>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-ipams-8dacb8c6-get-parameters" id="api-cluster-sdn-ipams-8dacb8c6-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的 SDN ipam；可选值：`netbox`, `phpipam`, `pve` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"type": {"description": "仅列出特定类型的 SDN ipam", "enum": ["netbox", "phpipam", "pve"], "optional": 1, "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-ipams-8dacb8c6-get-returns" id="api-cluster-sdn-ipams-8dacb8c6-get-returns"></a>

```text
{
  "items": {"properties": {"ipam": {"type": "string"}, "type": {"type": "string"}}, "type": "object"}, "links": [{"href": "{ipam}", "rel": "child"}],
  "type": "array"
}
```

### POST `/cluster/sdn/ipams` <a href="#api-cluster-sdn-ipams-8dacb8c6-post" id="api-cluster-sdn-ipams-8dacb8c6-post"></a>

创建新的 SDN ipam 对象。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/sdn/ipams", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-ipams-8dacb8c6-post-parameters" id="api-cluster-sdn-ipams-8dacb8c6-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `fingerprint` | 类型：string；必填：否；默认值：—<br>证书 SHA 256 指纹。 |
| `ipam` | 类型：string；必填：是；默认值：—<br>SDN ipam 对象标识符。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `section` | 类型：integer；必填：否；默认值：—<br> |
| `token` | 类型：string；必填：否；默认值：—<br> |
| `type` | 类型：string；必填：是；默认值：—<br>插件类型。；可选值：`netbox`, `phpipam`, `pve` |
| `url` | 类型：string；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "fingerprint": {"description": "证书 SHA 256 指纹。", "optional": 1, "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
    "ipam": {"description": "SDN ipam 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "section": {"optional": 1, "type": "integer", "typetext": "<integer>"}, "token": {"optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"description": "插件类型。", "enum": ["netbox", "phpipam", "pve"], "format": "pve-configid", "type": "string"},
    "url": {"optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-ipams-8dacb8c6-post-returns" id="api-cluster-sdn-ipams-8dacb8c6-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/ipams)。

## `/cluster/sdn/ipams/{ipam}` <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6" id="api-cluster-sdn-ipams-ipam-57c7d4f6"></a>

原始接口路径：`/cluster/sdn/ipams/{ipam}`。

### DELETE `/cluster/sdn/ipams/{ipam}` <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-delete" id="api-cluster-sdn-ipams-ipam-57c7d4f6-delete"></a>

删除 SDN ipam 对象配置。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/sdn/ipams", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-delete-parameters" id="api-cluster-sdn-ipams-ipam-57c7d4f6-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `ipam` | 类型：string；必填：是；默认值：—<br>SDN ipam 对象标识符。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "ipam": {"description": "SDN ipam 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-delete-returns" id="api-cluster-sdn-ipams-ipam-57c7d4f6-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/ipams/{ipam}` <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-get" id="api-cluster-sdn-ipams-ipam-57c7d4f6-get"></a>

读取 SDN ipam 配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/sdn/ipams/{ipam}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-get-parameters" id="api-cluster-sdn-ipams-ipam-57c7d4f6-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `ipam` | 类型：string；必填：是；默认值：—<br>SDN ipam 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"ipam": {"description": "SDN ipam 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-get-returns" id="api-cluster-sdn-ipams-ipam-57c7d4f6-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/sdn/ipams/{ipam}` <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-put" id="api-cluster-sdn-ipams-ipam-57c7d4f6-put"></a>

更新 SDN ipam 对象配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/sdn/ipams", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-put-parameters" id="api-cluster-sdn-ipams-ipam-57c7d4f6-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `fingerprint` | 类型：string；必填：否；默认值：—<br>证书 SHA 256 指纹。 |
| `ipam` | 类型：string；必填：是；默认值：—<br>SDN ipam 对象标识符。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `section` | 类型：integer；必填：否；默认值：—<br> |
| `token` | 类型：string；必填：否；默认值：—<br> |
| `url` | 类型：string；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "fingerprint": {"description": "证书 SHA 256 指纹。", "optional": 1, "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
    "ipam": {"description": "SDN ipam 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "section": {"optional": 1, "type": "integer", "typetext": "<integer>"}, "token": {"optional": 1, "type": "string", "typetext": "<string>"},
    "url": {"optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-ipams-ipam-57c7d4f6-put-returns" id="api-cluster-sdn-ipams-ipam-57c7d4f6-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/ipams/{ipam})。

## `/cluster/sdn/ipams/{ipam}/status` <a href="#api-cluster-sdn-ipams-ipam-status-5f7a96e8" id="api-cluster-sdn-ipams-ipam-status-5f7a96e8"></a>

原始接口路径：`/cluster/sdn/ipams/{ipam}/status`。

### GET `/cluster/sdn/ipams/{ipam}/status` <a href="#api-cluster-sdn-ipams-ipam-status-5f7a96e8-get" id="api-cluster-sdn-ipams-ipam-status-5f7a96e8-get"></a>

列出 PVE IPAM 条目

**方法标识：** `ipamindex`

**权限**

```text
{"description": "仅列出您对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-ipams-ipam-status-5f7a96e8-get-parameters" id="api-cluster-sdn-ipams-ipam-status-5f7a96e8-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `ipam` | 类型：string；必填：是；默认值：—<br>SDN ipam 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"ipam": {"description": "SDN ipam 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-ipams-ipam-status-5f7a96e8-get-returns" id="api-cluster-sdn-ipams-ipam-status-5f7a96e8-get-returns"></a>

```text
{"type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/ipams/{ipam}/status)。

## `/cluster/sdn/dns` <a href="#api-cluster-sdn-dns-205d876c" id="api-cluster-sdn-dns-205d876c"></a>

原始接口路径：`/cluster/sdn/dns`。

### GET `/cluster/sdn/dns` <a href="#api-cluster-sdn-dns-205d876c-get" id="api-cluster-sdn-dns-205d876c-get"></a>

SDN DNS 索引。

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/dns/<dns>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-dns-205d876c-get-parameters" id="api-cluster-sdn-dns-205d876c-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>仅列出特定类型的 SDN DNS；可选值：`powerdns` |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"type": {"description": "仅列出特定类型的 SDN DNS", "enum": ["powerdns"], "optional": 1, "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-dns-205d876c-get-returns" id="api-cluster-sdn-dns-205d876c-get-returns"></a>

```text
{
  "items": {"properties": {"dns": {"type": "string"}, "type": {"type": "string"}}, "type": "object"}, "links": [{"href": "{dns}", "rel": "child"}],
  "type": "array"
}
```

### POST `/cluster/sdn/dns` <a href="#api-cluster-sdn-dns-205d876c-post" id="api-cluster-sdn-dns-205d876c-post"></a>

创建新的 SDN DNS 对象。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/sdn/dns", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-dns-205d876c-post-parameters" id="api-cluster-sdn-dns-205d876c-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `dns` | 类型：string；必填：是；默认值：—<br>SDN DNS 对象标识符。 |
| `fingerprint` | 类型：string；必填：否；默认值：—<br>证书 SHA 256 指纹。 |
| `key` | 类型：string；必填：是；默认值：—<br> |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `reversemaskv6` | 类型：integer；必填：否；默认值：—<br> |
| `reversev6mask` | 类型：integer；必填：否；默认值：—<br> |
| `ttl` | 类型：integer；必填：否；默认值：—<br> |
| `type` | 类型：string；必填：是；默认值：—<br>插件类型。；可选值：`powerdns` |
| `url` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "dns": {"description": "SDN DNS 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "fingerprint": {"description": "证书 SHA 256 指纹。", "optional": 1, "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
    "key": {"optional": 0, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "reversemaskv6": {"optional": 1, "type": "integer", "typetext": "<integer>"}, "reversev6mask": {"optional": 1, "type": "integer", "typetext": "<integer>"},
    "ttl": {"optional": 1, "type": "integer", "typetext": "<integer>"},
    "type": {"description": "插件类型。", "enum": ["powerdns"], "format": "pve-configid", "type": "string"},
    "url": {"optional": 0, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-dns-205d876c-post-returns" id="api-cluster-sdn-dns-205d876c-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/dns)。

## `/cluster/sdn/dns/{dns}` <a href="#api-cluster-sdn-dns-dns-4dd13de3" id="api-cluster-sdn-dns-dns-4dd13de3"></a>

原始接口路径：`/cluster/sdn/dns/{dns}`。

### DELETE `/cluster/sdn/dns/{dns}` <a href="#api-cluster-sdn-dns-dns-4dd13de3-delete" id="api-cluster-sdn-dns-dns-4dd13de3-delete"></a>

删除 SDN DNS 对象配置。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/sdn/dns", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-dns-dns-4dd13de3-delete-parameters" id="api-cluster-sdn-dns-dns-4dd13de3-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `dns` | 类型：string；必填：是；默认值：—<br>SDN DNS 对象标识符。 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "dns": {"description": "SDN DNS 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-dns-dns-4dd13de3-delete-returns" id="api-cluster-sdn-dns-dns-4dd13de3-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/dns/{dns}` <a href="#api-cluster-sdn-dns-dns-4dd13de3-get" id="api-cluster-sdn-dns-dns-4dd13de3-get"></a>

读取 SDN DNS 配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/sdn/dns/{dns}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-dns-dns-4dd13de3-get-parameters" id="api-cluster-sdn-dns-dns-4dd13de3-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `dns` | 类型：string；必填：是；默认值：—<br>SDN DNS 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"dns": {"description": "SDN DNS 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-dns-dns-4dd13de3-get-returns" id="api-cluster-sdn-dns-dns-4dd13de3-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/sdn/dns/{dns}` <a href="#api-cluster-sdn-dns-dns-4dd13de3-put" id="api-cluster-sdn-dns-dns-4dd13de3-put"></a>

更新 SDN DNS 对象配置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/sdn/dns", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-dns-dns-4dd13de3-put-parameters" id="api-cluster-sdn-dns-dns-4dd13de3-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dns` | 类型：string；必填：是；默认值：—<br>SDN DNS 对象标识符。 |
| `fingerprint` | 类型：string；必填：否；默认值：—<br>证书 SHA 256 指纹。 |
| `key` | 类型：string；必填：否；默认值：—<br> |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `reversemaskv6` | 类型：integer；必填：否；默认值：—<br> |
| `ttl` | 类型：integer；必填：否；默认值：—<br> |
| `url` | 类型：string；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "dns": {"description": "SDN DNS 对象标识符。", "minLength": 2, "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]", "type": "string"},
    "fingerprint": {"description": "证书 SHA 256 指纹。", "optional": 1, "pattern": "([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}", "type": "string"},
    "key": {"optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "reversemaskv6": {"optional": 1, "type": "integer", "typetext": "<integer>"}, "ttl": {"optional": 1, "type": "integer", "typetext": "<integer>"},
    "url": {"optional": 1, "type": "string", "typetext": "<string>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-dns-dns-4dd13de3-put-returns" id="api-cluster-sdn-dns-dns-4dd13de3-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/dns/{dns})。

## `/cluster/sdn/fabrics` <a href="#api-cluster-sdn-fabrics-49112f80" id="api-cluster-sdn-fabrics-49112f80"></a>

原始接口路径：`/cluster/sdn/fabrics`。

### GET `/cluster/sdn/fabrics` <a href="#api-cluster-sdn-fabrics-49112f80-get" id="api-cluster-sdn-fabrics-49112f80-get"></a>

SDN Fabric 索引

**方法标识：** `index`

**权限**

```text
{"check": ["perm", "/sdn/fabrics", ["SDN.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-49112f80-get-parameters" id="api-cluster-sdn-fabrics-49112f80-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-sdn-fabrics-49112f80-get-returns" id="api-cluster-sdn-fabrics-49112f80-get-returns"></a>

```text
{"items": {"properties": {"subdir": {"type": "string"}}, "type": "object"}, "links": [{"href": "{subdir}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics)。

## `/cluster/sdn/fabrics/fabric` <a href="#api-cluster-sdn-fabrics-fabric-9f29add0" id="api-cluster-sdn-fabrics-fabric-9f29add0"></a>

原始接口路径：`/cluster/sdn/fabrics/fabric`。

### GET `/cluster/sdn/fabrics/fabric` <a href="#api-cluster-sdn-fabrics-fabric-9f29add0-get" id="api-cluster-sdn-fabrics-fabric-9f29add0-get"></a>

SDN Fabric 索引

**方法标识：** `index`

**权限**

```text
{"description": "仅列出您对 '/sdn/fabrics/<fabric>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-fabric-9f29add0-get-parameters" id="api-cluster-sdn-fabrics-fabric-9f29add0-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-fabric-9f29add0-get-returns" id="api-cluster-sdn-fabrics-fabric-9f29add0-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "area": {
        "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。", "instance-types": ["ospf"], "optional": 1, "type": "string",
        "type-property": "protocol"
      },
      "csnp_interval": {
        "description": "Openfabric 的 csnp_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
        "type-property": "protocol"
      },
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "hello_interval": {
        "description": "Openfabric 的 hello_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
        "type-property": "protocol"
      },
      "id": {
        "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2,
        "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]", "type": "string"
      },
      "ip6_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string"},
      "ip_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string"},
      "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
      "persistent_keepalive": {
        "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
        "instance-types": ["wireguard"], "maximum": 65535, "minimum": 0, "optional": 1, "type": "number", "type-property": "protocol"
      },
      "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
      "redistribute": {
        "oneOf": [
          {
            "instance-types": ["ospf"],
            "items": {
              "format": {
                "route-map": {
                  "description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"
                },
                "source": {"description": "要从中重分发路由的协议。", "enum": ["bgp", "connected", "kernel", "static"], "type": "string"}
              },
              "type": "string"
            },
            "optional": 1, "type": "array"
          },
          {
            "instance-types": ["bgp"],
            "items": {
              "format": {
                "route-map": {
                  "description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"
                },
                "source": {"description": "要从中重分发路由的协议。", "enum": ["connected", "kernel", "ospf", "static"], "type": "string"}
              },
              "type": "string"
            },
            "optional": 1, "type": "array"
          }
        ],
        "type": "array", "type-property": "protocol"
      },
      "route_filter": {
        "description": "用于过滤将安装到内核路由表中的路由的前缀列表", "format": "pve-sdn-prefix-list-id", "instance-types": ["ospf", "openfabric"],
        "optional": 1, "type": "string", "type-property": "protocol"
      }
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/fabrics/fabric` <a href="#api-cluster-sdn-fabrics-fabric-9f29add0-post" id="api-cluster-sdn-fabrics-fabric-9f29add0-post"></a>

添加 fabric

**方法标识：** `add_fabric`

**权限**

```text
{"check": ["perm", "/sdn/fabrics", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-fabric-9f29add0-post-parameters" id="api-cluster-sdn-fabrics-fabric-9f29add0-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `area` | 类型：string；必填：否；默认值：—<br>OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。 |
| `csnp_interval` | 类型：number；必填：否；默认值：—<br>Openfabric 的 csnp_interval 属性 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `hello_interval` | 类型：number；必填：否；默认值：—<br>Openfabric 的 hello_interval 属性 |
| `id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `ip6_prefix` | 类型：string；必填：否；默认值：—<br>节点 IP 的 IP 前缀 |
| `ip_prefix` | 类型：string；必填：否；默认值：—<br>节点 IP 的 IP 前缀 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `persistent_keepalive` | 类型：number；必填：否；默认值：—<br>发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用 |
| `protocol` | 类型：string；必填：是；默认值：—<br>SDN Fabric 配置节中配置条目的类型；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `redistribute` | 类型：array；必填：是；默认值：—<br> |
| `route_filter` | 类型：string；必填：否；默认值：—<br>用于过滤将安装到内核路由表中的路由的前缀列表 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "area": {
      "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。", "instance-types": ["ospf"], "optional": 1, "type": "string",
      "type-property": "protocol", "typetext": "<string>"
    },
    "csnp_interval": {
      "description": "Openfabric 的 csnp_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
      "type-property": "protocol", "typetext": "<number> (1 - 600)"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "hello_interval": {
      "description": "Openfabric 的 hello_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
      "type-property": "protocol", "typetext": "<number> (1 - 600)"
    },
    "id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "ip6_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string", "typetext": "<string>"},
    "ip_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "persistent_keepalive": {
      "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
      "instance-types": ["wireguard"], "maximum": 65535, "minimum": 0, "optional": 1, "type": "number", "type-property": "protocol",
      "typetext": "<number> (0 - 65535)"
    },
    "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
    "redistribute": {
      "oneOf": [
        {
          "instance-types": ["ospf"],
          "items": {
            "format": {
              "route-map": {"description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
              "source": {"description": "要从中重分发路由的协议。", "enum": ["bgp", "connected", "kernel", "static"], "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "instance-types": ["bgp"],
          "items": {
            "format": {
              "route-map": {"description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
              "source": {"description": "要从中重分发路由的协议。", "enum": ["connected", "kernel", "ospf", "static"], "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        }
      ],
      "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "route_filter": {
      "description": "用于过滤将安装到内核路由表中的路由的前缀列表", "format": "pve-sdn-prefix-list-id", "instance-types": ["ospf", "openfabric"],
      "optional": 1, "type": "string", "type-property": "protocol", "typetext": "<string>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-fabric-9f29add0-post-returns" id="api-cluster-sdn-fabrics-fabric-9f29add0-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/fabric)。

## `/cluster/sdn/fabrics/fabric/{id}` <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122" id="api-cluster-sdn-fabrics-fabric-id-d3231122"></a>

原始接口路径：`/cluster/sdn/fabrics/fabric/{id}`。

### DELETE `/cluster/sdn/fabrics/fabric/{id}` <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-delete" id="api-cluster-sdn-fabrics-fabric-id-d3231122-delete"></a>

添加 fabric

**方法标识：** `delete_fabric`

**权限**

```text
{"check": ["perm", "/sdn/fabrics/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-delete-parameters" id="api-cluster-sdn-fabrics-fabric-id-d3231122-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-delete-returns" id="api-cluster-sdn-fabrics-fabric-id-d3231122-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/fabrics/fabric/{id}` <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-get" id="api-cluster-sdn-fabrics-fabric-id-d3231122-get"></a>

更新 fabric

**方法标识：** `get_fabric`

**权限**

```text
{"check": ["perm", "/sdn/fabrics/{id}", ["SDN.Audit", "SDN.Allocate"], "any", 1]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-get-parameters" id="api-cluster-sdn-fabrics-fabric-id-d3231122-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-get-returns" id="api-cluster-sdn-fabrics-fabric-id-d3231122-get-returns"></a>

```text
{
  "properties": {
    "area": {
      "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。", "instance-types": ["ospf"], "optional": 1, "type": "string",
      "type-property": "protocol"
    },
    "csnp_interval": {
      "description": "Openfabric 的 csnp_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
      "type-property": "protocol"
    },
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "hello_interval": {
      "description": "Openfabric 的 hello_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
      "type-property": "protocol"
    },
    "id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "ip6_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string"},
    "ip_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
    "persistent_keepalive": {
      "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
      "instance-types": ["wireguard"], "maximum": 65535, "minimum": 0, "optional": 1, "type": "number", "type-property": "protocol"
    },
    "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
    "redistribute": {
      "oneOf": [
        {
          "instance-types": ["ospf"],
          "items": {
            "format": {
              "route-map": {"description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
              "source": {"description": "要从中重分发路由的协议。", "enum": ["bgp", "connected", "kernel", "static"], "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "instance-types": ["bgp"],
          "items": {
            "format": {
              "route-map": {"description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
              "source": {"description": "要从中重分发路由的协议。", "enum": ["connected", "kernel", "ospf", "static"], "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        }
      ],
      "type": "array", "type-property": "protocol"
    },
    "route_filter": {
      "description": "用于过滤将安装到内核路由表中的路由的前缀列表", "format": "pve-sdn-prefix-list-id", "instance-types": ["ospf", "openfabric"],
      "optional": 1, "type": "string", "type-property": "protocol"
    }
  },
  "type": "object"
}
```

### PUT `/cluster/sdn/fabrics/fabric/{id}` <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-put" id="api-cluster-sdn-fabrics-fabric-id-d3231122-put"></a>

更新 fabric

**方法标识：** `update_fabric`

**权限**

```text
{"check": ["perm", "/sdn/fabrics/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-put-parameters" id="api-cluster-sdn-fabrics-fabric-id-d3231122-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `area` | 类型：string；必填：否；默认值：—<br>OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。 |
| `csnp_interval` | 类型：number；必填：否；默认值：—<br>Openfabric 的 csnp_interval 属性 |
| `delete` | 类型：array；必填：是；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `hello_interval` | 类型：number；必填：否；默认值：—<br>Openfabric 的 hello_interval 属性 |
| `id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `ip6_prefix` | 类型：string；必填：否；默认值：—<br>节点 IP 的 IP 前缀 |
| `ip_prefix` | 类型：string；必填：否；默认值：—<br>节点 IP 的 IP 前缀 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `persistent_keepalive` | 类型：number；必填：否；默认值：—<br>发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用 |
| `protocol` | 类型：string；必填：是；默认值：—<br>SDN Fabric 配置节中配置条目的类型；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `redistribute` | 类型：array；必填：是；默认值：—<br> |
| `route_filter` | 类型：string；必填：否；默认值：—<br>用于过滤将安装到内核路由表中的路由的前缀列表 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "area": {
      "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。", "instance-types": ["ospf"], "optional": 1, "type": "string",
      "type-property": "protocol", "typetext": "<string>"
    },
    "csnp_interval": {
      "description": "Openfabric 的 csnp_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
      "type-property": "protocol", "typetext": "<number> (1 - 600)"
    },
    "delete": {
      "oneOf": [
        {
          "instance-types": ["openfabric"], "items": {"enum": ["ip_prefix", "ip6_prefix", "hello_interval", "csnp_interval", "route_filter"], "type": "string"},
          "optional": 1, "type": "array"
        },
        {
          "instance-types": ["bgp"],
          "items": {"enum": ["ip_prefix", "ip6_prefix", "redistribute", "route_filter", "route_map_in", "route_map_out"], "type": "string"}, "optional": 1,
          "type": "array"
        },
        {"instance-types": ["ospf"], "items": {"enum": ["area", "redistribute", "route_filter"], "type": "string"}, "optional": 1, "type": "array"},
        {"instance-types": ["wireguard"], "items": {"enum": ["persistent_keepalive"], "type": "string"}, "optional": 1, "type": "array"}
      ],
      "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "hello_interval": {
      "description": "Openfabric 的 hello_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
      "type-property": "protocol", "typetext": "<number> (1 - 600)"
    },
    "id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "ip6_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string", "typetext": "<string>"},
    "ip_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "persistent_keepalive": {
      "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
      "instance-types": ["wireguard"], "maximum": 65535, "minimum": 0, "optional": 1, "type": "number", "type-property": "protocol",
      "typetext": "<number> (0 - 65535)"
    },
    "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
    "redistribute": {
      "oneOf": [
        {
          "instance-types": ["ospf"],
          "items": {
            "format": {
              "route-map": {"description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
              "source": {"description": "要从中重分发路由的协议。", "enum": ["bgp", "connected", "kernel", "static"], "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "instance-types": ["bgp"],
          "items": {
            "format": {
              "route-map": {"description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
              "source": {"description": "要从中重分发路由的协议。", "enum": ["connected", "kernel", "ospf", "static"], "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        }
      ],
      "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "route_filter": {
      "description": "用于过滤将安装到内核路由表中的路由的前缀列表", "format": "pve-sdn-prefix-list-id", "instance-types": ["ospf", "openfabric"],
      "optional": 1, "type": "string", "type-property": "protocol", "typetext": "<string>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-fabric-id-d3231122-put-returns" id="api-cluster-sdn-fabrics-fabric-id-d3231122-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/fabric/{id})。

## `/cluster/sdn/fabrics/node` <a href="#api-cluster-sdn-fabrics-node-a9fc4070" id="api-cluster-sdn-fabrics-node-a9fc4070"></a>

原始接口路径：`/cluster/sdn/fabrics/node`。

### GET `/cluster/sdn/fabrics/node` <a href="#api-cluster-sdn-fabrics-node-a9fc4070-get" id="api-cluster-sdn-fabrics-node-a9fc4070-get"></a>

SDN Fabric 索引

**方法标识：** `list_nodes`

**权限**

```text
{
  "description": "仅列出您具有以下权限的节点：对\n'/sdn/fabrics/<fabric>' 的 'SDN.Audit' 或 'SDN.Allocate' 权限，以及对 /nodes/<node_id> 的 'Sys.Audit' 或 'Sys.Modify' 权限",
  "user": "all"
}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-node-a9fc4070-get-parameters" id="api-cluster-sdn-fabrics-node-a9fc4070-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-node-a9fc4070-get-returns" id="api-cluster-sdn-fabrics-node-a9fc4070-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "allowed_ips": {
        "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。", "instance-types": ["wireguard"],
        "items": {"format": "FullRangeCIDR", "type": "string"}, "optional": 1, "type": "array", "type-property": "protocol"
      },
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "endpoint": {"description": "用于连接此节点的端点。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
      "fabric_id": {
        "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2,
        "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]", "type": "string"
      },
      "interfaces": {
        "oneOf": [
          {
            "description": "OpenFabric 网络接口", "instance-types": ["openfabric"],
            "items": {
              "format": {
                "hello_multiplier": {"description": "接口的 hello_multiplier 属性", "maximum": 100, "minimum": 2, "optional": 1, "type": "integer"},
                "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
                "ip6": {"description": "此节点的 IPv6 地址", "format": "CIDRv6", "optional": 1, "type": "string"},
                "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}
              },
              "type": "string"
            },
            "optional": 1, "type": "array"
          },
          {
            "description": "OSPF 网络接口", "instance-types": ["ospf"],
            "items": {
              "format": {
                "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
                "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"},
                "network_type": {
                  "description": "OSPF 接口的网络类型", "enum": ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"], "optional": 1,
                  "type": "string"
                }
              },
              "type": "string"
            },
            "optional": 1, "type": "array"
          },
          {
            "description": "此节点的 WireGuard 网络接口列表。", "instance-types": ["wireguard"],
            "items": {"description": "WireGuard 网络接口", "format": "pve-sdn-fabric-wireguard-interface", "type": "string"}, "optional": 1, "type": "array"
          },
          {
            "description": "BGP 网络接口", "instance-types": ["bgp"],
            "items": {"format": {"name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}}, "type": "string"}, "optional": 1
          }
        ],
        "type": "array", "type-property": "protocol"
      },
      "ip": {"description": "此节点的 IPv4 地址", "format": "ipv4", "optional": 1, "type": "string"},
      "ip6": {"description": "此节点的 IPv6 地址", "format": "ipv6", "optional": 1, "type": "string"},
      "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
      "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string"},
      "peers": {
        "instance-types": ["wireguard"],
        "items": {
          "format": {
            "endpoint": {"description": "覆盖节点配置节中的端点设置。", "optional": 1, "type": "string"},
            "iface": {"description": "此节点使用此对等端定义的接口。", "type": "string"},
            "node": {"description": "所引用节点配置节的名称（外部节点或内部对等节点）。", "type": "string"},
            "node_iface": {"description": "另一个节点的接口（如果它是内部节点）", "optional": 1, "type": "string"},
            "skip_route_generation": {"default": 0, "description": "是否应在内核路由表中为允许的 IP 创建路由。", "optional": 1, "type": "boolean"},
            "type": {"enum": ["internal", "external"], "type": "string"}
          },
          "type": "string"
        },
        "optional": 1, "type": "array", "type-property": "protocol"
      },
      "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
      "public_key": {"description": "外部节点的公钥。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
      "role": {
        "description": "此节点在 WireGuard fabric 中的角色。", "enum": ["internal", "external"], "instance-types": ["wireguard"], "optional": 1,
        "type": "string", "type-property": "protocol"
      }
    },
    "type": "object"
  },
  "links": [{"href": "{fabric_id}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/node)。

## `/cluster/sdn/fabrics/node/{fabric_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0"></a>

原始接口路径：`/cluster/sdn/fabrics/node/{fabric_id}`。

### GET `/cluster/sdn/fabrics/node/{fabric_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-get" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-get"></a>

SDN Fabric 索引

**方法标识：** `list_nodes_fabric`

**权限**

```text
{"check": ["perm", "/sdn/fabrics/{fabric_id}", ["SDN.Audit"]], "description": "仅返回您具有 'Sys.Audit' 或 'Sys.Modify' 权限的节点。"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-get-parameters" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `fabric_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "fabric_id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-get-returns" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "allowed_ips": {
        "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。", "instance-types": ["wireguard"],
        "items": {"format": "FullRangeCIDR", "type": "string"}, "optional": 1, "type": "array", "type-property": "protocol"
      },
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "endpoint": {"description": "用于连接此节点的端点。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
      "fabric_id": {
        "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2,
        "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]", "type": "string"
      },
      "interfaces": {
        "oneOf": [
          {
            "description": "OpenFabric 网络接口", "instance-types": ["openfabric"],
            "items": {
              "format": {
                "hello_multiplier": {"description": "接口的 hello_multiplier 属性", "maximum": 100, "minimum": 2, "optional": 1, "type": "integer"},
                "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
                "ip6": {"description": "此节点的 IPv6 地址", "format": "CIDRv6", "optional": 1, "type": "string"},
                "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}
              },
              "type": "string"
            },
            "optional": 1, "type": "array"
          },
          {
            "description": "OSPF 网络接口", "instance-types": ["ospf"],
            "items": {
              "format": {
                "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
                "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"},
                "network_type": {
                  "description": "OSPF 接口的网络类型", "enum": ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"], "optional": 1,
                  "type": "string"
                }
              },
              "type": "string"
            },
            "optional": 1, "type": "array"
          },
          {
            "description": "此节点的 WireGuard 网络接口列表。", "instance-types": ["wireguard"],
            "items": {"description": "WireGuard 网络接口", "format": "pve-sdn-fabric-wireguard-interface", "type": "string"}, "optional": 1, "type": "array"
          },
          {
            "description": "BGP 网络接口", "instance-types": ["bgp"],
            "items": {"format": {"name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}}, "type": "string"}, "optional": 1
          }
        ],
        "type": "array", "type-property": "protocol"
      },
      "ip": {"description": "此节点的 IPv4 地址", "format": "ipv4", "optional": 1, "type": "string"},
      "ip6": {"description": "此节点的 IPv6 地址", "format": "ipv6", "optional": 1, "type": "string"},
      "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
      "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string"},
      "peers": {
        "instance-types": ["wireguard"],
        "items": {
          "format": {
            "endpoint": {"description": "覆盖节点配置节中的端点设置。", "optional": 1, "type": "string"},
            "iface": {"description": "此节点使用此对等端定义的接口。", "type": "string"},
            "node": {"description": "所引用节点配置节的名称（外部节点或内部对等节点）。", "type": "string"},
            "node_iface": {"description": "另一个节点的接口（如果它是内部节点）", "optional": 1, "type": "string"},
            "skip_route_generation": {"default": 0, "description": "是否应在内核路由表中为允许的 IP 创建路由。", "optional": 1, "type": "boolean"},
            "type": {"enum": ["internal", "external"], "type": "string"}
          },
          "type": "string"
        },
        "optional": 1, "type": "array", "type-property": "protocol"
      },
      "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
      "public_key": {"description": "外部节点的公钥。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
      "role": {
        "description": "此节点在 WireGuard fabric 中的角色。", "enum": ["internal", "external"], "instance-types": ["wireguard"], "optional": 1,
        "type": "string", "type-property": "protocol"
      }
    },
    "type": "object"
  },
  "links": [{"href": "{node_id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/fabrics/node/{fabric_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-post" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-post"></a>

添加节点

**方法标识：** `add_node`

**权限**

```text
{"check": ["and", ["perm", "/sdn/fabrics/{fabric_id}", ["SDN.Allocate"]], ["perm", "/nodes/{node_id}", ["Sys.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-post-parameters" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `allowed_ips` | 类型：array；必填：否；默认值：—<br>WireGuard fabric 中可经由此节点路由的 IP 列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `endpoint` | 类型：string；必填：否；默认值：—<br>用于连接此节点的端点。 |
| `fabric_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `interfaces` | 类型：array；必填：是；默认值：—<br> |
| `ip` | 类型：string；必填：否；默认值：—<br>此节点的 IPv4 地址 |
| `ip6` | 类型：string；必填：否；默认值：—<br>此节点的 IPv6 地址 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `node_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 中节点的标识符 |
| `peers` | 类型：array；必填：否；默认值：—<br> |
| `protocol` | 类型：string；必填：是；默认值：—<br>SDN Fabric 配置节中配置条目的类型；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `public_key` | 类型：string；必填：否；默认值：—<br>外部节点的公钥。 |
| `role` | 类型：string；必填：否；默认值：—<br>此节点在 WireGuard fabric 中的角色。；可选值：`internal`, `external` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "allowed_ips": {
      "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。", "instance-types": ["wireguard"], "items": {"format": "FullRangeCIDR", "type": "string"},
      "optional": 1, "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "endpoint": {
      "description": "用于连接此节点的端点。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol",
      "typetext": "<string>"
    },
    "fabric_id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric 网络接口", "instance-types": ["openfabric"],
          "items": {
            "format": {
              "hello_multiplier": {"description": "接口的 hello_multiplier 属性", "maximum": 100, "minimum": 2, "optional": 1, "type": "integer"},
              "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
              "ip6": {"description": "此节点的 IPv6 地址", "format": "CIDRv6", "optional": 1, "type": "string"},
              "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "description": "OSPF 网络接口", "instance-types": ["ospf"],
          "items": {
            "format": {
              "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
              "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"},
              "network_type": {
                "description": "OSPF 接口的网络类型", "enum": ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"], "optional": 1,
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "description": "此节点的 WireGuard 网络接口列表。", "instance-types": ["wireguard"],
          "items": {"description": "WireGuard 网络接口", "format": "pve-sdn-fabric-wireguard-interface", "type": "string"}, "optional": 1, "type": "array"
        },
        {
          "description": "BGP 网络接口", "instance-types": ["bgp"],
          "items": {"format": {"name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}}, "type": "string"}, "optional": 1
        }
      ],
      "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "ip": {"description": "此节点的 IPv4 地址", "format": "ipv4", "optional": 1, "type": "string", "typetext": "<string>"},
    "ip6": {"description": "此节点的 IPv6 地址", "format": "ipv6", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string", "typetext": "<string>"},
    "peers": {
      "instance-types": ["wireguard"],
      "items": {
        "format": {
          "endpoint": {"description": "覆盖节点配置节中的端点设置。", "optional": 1, "type": "string"},
          "iface": {"description": "此节点使用此对等端定义的接口。", "type": "string"},
          "node": {"description": "所引用节点配置节的名称（外部节点或内部对等节点）。", "type": "string"},
          "node_iface": {"description": "另一个节点的接口（如果它是内部节点）", "optional": 1, "type": "string"},
          "skip_route_generation": {"default": 0, "description": "是否应在内核路由表中为允许的 IP 创建路由。", "optional": 1, "type": "boolean"},
          "type": {"enum": ["internal", "external"], "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
    "public_key": {
      "description": "外部节点的公钥。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol", "typetext": "<string>"
    },
    "role": {
      "description": "此节点在 WireGuard fabric 中的角色。", "enum": ["internal", "external"], "instance-types": ["wireguard"], "optional": 1, "type": "string",
      "type-property": "protocol"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-post-returns" id="api-cluster-sdn-fabrics-node-fabric-id-2a8cbbb0-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/node/{fabric_id})。

## `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a"></a>

原始接口路径：`/cluster/sdn/fabrics/node/{fabric_id}/{node_id}`。

### DELETE `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-delete" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-delete"></a>

添加节点

**方法标识：** `delete_node`

**权限**

```text
{"check": ["and", ["perm", "/sdn/fabrics/{fabric_id}", ["SDN.Allocate"]], ["perm", "/nodes/{node_id}", ["Sys.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-delete-parameters" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `fabric_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `node_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 中节点的标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "fabric_id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-delete-returns" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-get" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-get"></a>

获取节点

**方法标识：** `get_node`

**权限**

```text
{
  "check": [
    "and", ["perm", "/sdn/fabrics/{fabric_id}", ["SDN.Audit", "SDN.Allocate"], "any", 1], ["perm", "/nodes/{node_id}", ["Sys.Audit", "Sys.Modify"], "any", 1]
  ]
}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-get-parameters" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `fabric_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `node_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 中节点的标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "fabric_id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-get-returns" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-get-returns"></a>

```text
{
  "properties": {
    "allowed_ips": {
      "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。", "instance-types": ["wireguard"], "items": {"format": "FullRangeCIDR", "type": "string"},
      "optional": 1, "type": "array", "type-property": "protocol"
    },
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "endpoint": {"description": "用于连接此节点的端点。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
    "fabric_id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric 网络接口", "instance-types": ["openfabric"],
          "items": {
            "format": {
              "hello_multiplier": {"description": "接口的 hello_multiplier 属性", "maximum": 100, "minimum": 2, "optional": 1, "type": "integer"},
              "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
              "ip6": {"description": "此节点的 IPv6 地址", "format": "CIDRv6", "optional": 1, "type": "string"},
              "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "description": "OSPF 网络接口", "instance-types": ["ospf"],
          "items": {
            "format": {
              "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
              "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"},
              "network_type": {
                "description": "OSPF 接口的网络类型", "enum": ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"], "optional": 1,
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "description": "此节点的 WireGuard 网络接口列表。", "instance-types": ["wireguard"],
          "items": {"description": "WireGuard 网络接口", "format": "pve-sdn-fabric-wireguard-interface", "type": "string"}, "optional": 1, "type": "array"
        },
        {
          "description": "BGP 网络接口", "instance-types": ["bgp"],
          "items": {"format": {"name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}}, "type": "string"}, "optional": 1
        }
      ],
      "type": "array", "type-property": "protocol"
    },
    "ip": {"description": "此节点的 IPv4 地址", "format": "ipv4", "optional": 1, "type": "string"},
    "ip6": {"description": "此节点的 IPv6 地址", "format": "ipv6", "optional": 1, "type": "string"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
    "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string"},
    "peers": {
      "instance-types": ["wireguard"],
      "items": {
        "format": {
          "endpoint": {"description": "覆盖节点配置节中的端点设置。", "optional": 1, "type": "string"},
          "iface": {"description": "此节点使用此对等端定义的接口。", "type": "string"},
          "node": {"description": "所引用节点配置节的名称（外部节点或内部对等节点）。", "type": "string"},
          "node_iface": {"description": "另一个节点的接口（如果它是内部节点）", "optional": 1, "type": "string"},
          "skip_route_generation": {"default": 0, "description": "是否应在内核路由表中为允许的 IP 创建路由。", "optional": 1, "type": "boolean"},
          "type": {"enum": ["internal", "external"], "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "type-property": "protocol"
    },
    "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
    "public_key": {"description": "外部节点的公钥。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
    "role": {
      "description": "此节点在 WireGuard fabric 中的角色。", "enum": ["internal", "external"], "instance-types": ["wireguard"], "optional": 1, "type": "string",
      "type-property": "protocol"
    }
  }
}
```

### PUT `/cluster/sdn/fabrics/node/{fabric_id}/{node_id}` <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-put" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-put"></a>

更新节点

**方法标识：** `update_node`

**权限**

```text
{"check": ["and", ["perm", "/sdn/fabrics/{fabric_id}", ["SDN.Allocate"]], ["perm", "/nodes/{node_id}", ["Sys.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-put-parameters" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `allowed_ips` | 类型：array；必填：否；默认值：—<br>WireGuard fabric 中可经由此节点路由的 IP 列表。 |
| `delete` | 类型：array；必填：是；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `endpoint` | 类型：string；必填：否；默认值：—<br>用于连接此节点的端点。 |
| `fabric_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 的标识符 |
| `interfaces` | 类型：array；必填：是；默认值：—<br> |
| `ip` | 类型：string；必填：否；默认值：—<br>此节点的 IPv4 地址 |
| `ip6` | 类型：string；必填：否；默认值：—<br>此节点的 IPv6 地址 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `node_id` | 类型：string；必填：是；默认值：—<br>SDN fabric 中节点的标识符 |
| `peers` | 类型：array；必填：否；默认值：—<br> |
| `protocol` | 类型：string；必填：是；默认值：—<br>SDN Fabric 配置节中配置条目的类型；可选值：`openfabric`, `ospf`, `wireguard`, `bgp` |
| `public_key` | 类型：string；必填：否；默认值：—<br>外部节点的公钥。 |
| `role` | 类型：string；必填：否；默认值：—<br>此节点在 WireGuard fabric 中的角色。；可选值：`internal`, `external` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "allowed_ips": {
      "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。", "instance-types": ["wireguard"], "items": {"format": "FullRangeCIDR", "type": "string"},
      "optional": 1, "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "delete": {
      "oneOf": [
        {"instance-types": ["bgp"], "items": {"enum": ["interfaces", "ip", "ip6"], "type": "string"}, "optional": 1, "type": "array"},
        {"instance-types": ["openfabric", "ospf"], "items": {"enum": ["interfaces", "ip", "ip6"], "type": "string"}, "optional": 1, "type": "array"},
        {
          "instance-types": ["wireguard"], "items": {"enum": ["allowed_ips", "endpoint", "interfaces", "ip", "ip6", "peers"], "type": "string"}, "optional": 1,
          "type": "array"
        }
      ],
      "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "endpoint": {
      "description": "用于连接此节点的端点。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol",
      "typetext": "<string>"
    },
    "fabric_id": {
      "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2, "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]",
      "type": "string"
    },
    "interfaces": {
      "oneOf": [
        {
          "description": "OpenFabric 网络接口", "instance-types": ["openfabric"],
          "items": {
            "format": {
              "hello_multiplier": {"description": "接口的 hello_multiplier 属性", "maximum": 100, "minimum": 2, "optional": 1, "type": "integer"},
              "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
              "ip6": {"description": "此节点的 IPv6 地址", "format": "CIDRv6", "optional": 1, "type": "string"},
              "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "description": "OSPF 网络接口", "instance-types": ["ospf"],
          "items": {
            "format": {
              "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
              "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"},
              "network_type": {
                "description": "OSPF 接口的网络类型", "enum": ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"], "optional": 1,
                "type": "string"
              }
            },
            "type": "string"
          },
          "optional": 1, "type": "array"
        },
        {
          "description": "此节点的 WireGuard 网络接口列表。", "instance-types": ["wireguard"],
          "items": {"description": "WireGuard 网络接口", "format": "pve-sdn-fabric-wireguard-interface", "type": "string"}, "optional": 1, "type": "array"
        },
        {
          "description": "BGP 网络接口", "instance-types": ["bgp"],
          "items": {"format": {"name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}}, "type": "string"}, "optional": 1
        }
      ],
      "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "ip": {"description": "此节点的 IPv4 地址", "format": "ipv4", "optional": 1, "type": "string", "typetext": "<string>"},
    "ip6": {"description": "此节点的 IPv6 地址", "format": "ipv6", "optional": 1, "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string", "typetext": "<string>"},
    "peers": {
      "instance-types": ["wireguard"],
      "items": {
        "format": {
          "endpoint": {"description": "覆盖节点配置节中的端点设置。", "optional": 1, "type": "string"},
          "iface": {"description": "此节点使用此对等端定义的接口。", "type": "string"},
          "node": {"description": "所引用节点配置节的名称（外部节点或内部对等节点）。", "type": "string"},
          "node_iface": {"description": "另一个节点的接口（如果它是内部节点）", "optional": 1, "type": "string"},
          "skip_route_generation": {"default": 0, "description": "是否应在内核路由表中为允许的 IP 创建路由。", "optional": 1, "type": "boolean"},
          "type": {"enum": ["internal", "external"], "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "type-property": "protocol", "typetext": "<array>"
    },
    "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
    "public_key": {
      "description": "外部节点的公钥。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol", "typetext": "<string>"
    },
    "role": {
      "description": "此节点在 WireGuard fabric 中的角色。", "enum": ["internal", "external"], "instance-types": ["wireguard"], "optional": 1, "type": "string",
      "type-property": "protocol"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-put-returns" id="api-cluster-sdn-fabrics-node-fabric-id-node-id-24a1ba5a-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/node/{fabric_id}/{node_id})。

## `/cluster/sdn/fabrics/all` <a href="#api-cluster-sdn-fabrics-all-c756e6c1" id="api-cluster-sdn-fabrics-all-c756e6c1"></a>

原始接口路径：`/cluster/sdn/fabrics/all`。

### GET `/cluster/sdn/fabrics/all` <a href="#api-cluster-sdn-fabrics-all-c756e6c1-get" id="api-cluster-sdn-fabrics-all-c756e6c1-get"></a>

SDN Fabric 索引

**方法标识：** `list_all`

**权限**

```text
{
  "description": "仅列出您具有以下权限的 fabric：对\n'/sdn/fabrics/<fabric>' 的 'SDN.Audit' 或 'SDN.Allocate' 权限；仅列出您对 /nodes/<node_id> 具有 'Sys.Audit' 或 'Sys.Modify' 权限的节点",
  "user": "all"
}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-fabrics-all-c756e6c1-get-parameters" id="api-cluster-sdn-fabrics-all-c756e6c1-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-fabrics-all-c756e6c1-get-returns" id="api-cluster-sdn-fabrics-all-c756e6c1-get-returns"></a>

```text
{
  "properties": {
    "fabrics": {
      "items": {
        "properties": {
          "area": {
            "description": "OSPF 区域。可以是 IPv4 地址或 32 位数字。在 rust 中验证。", "instance-types": ["ospf"], "optional": 1, "type": "string",
            "type-property": "protocol"
          },
          "csnp_interval": {
            "description": "Openfabric 的 csnp_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
            "type-property": "protocol"
          },
          "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
          "hello_interval": {
            "description": "Openfabric 的 hello_interval 属性", "instance-types": ["openfabric"], "maximum": 600, "minimum": 1, "optional": 1, "type": "number",
            "type-property": "protocol"
          },
          "id": {
            "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2,
            "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]", "type": "string"
          },
          "ip6_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string"},
          "ip_prefix": {"description": "节点 IP 的 IP 前缀", "format": "CIDR", "optional": 1, "type": "string"},
          "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
          "persistent_keepalive": {
            "description": "发送经过身份验证的空数据包给对等端的间隔，单位为秒，范围为 1 到 65535（含边界），用于持续保持有状态防火墙或 NAT 映射有效。例如，如果接口很少发送流量，但可能随时接收其他节点的流量，并且位于 NAT 后方，则设置 25 秒的持久保活间隔可能有帮助。未设置或设为 0 时禁用",
            "instance-types": ["wireguard"], "maximum": 65535, "minimum": 0, "optional": 1, "type": "number", "type-property": "protocol"
          },
          "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
          "redistribute": {
            "oneOf": [
              {
                "instance-types": ["ospf"],
                "items": {
                  "format": {
                    "route-map": {
                      "description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"
                    },
                    "source": {"description": "要从中重分发路由的协议。", "enum": ["bgp", "connected", "kernel", "static"], "type": "string"}
                  },
                  "type": "string"
                },
                "optional": 1, "type": "array"
              },
              {
                "instance-types": ["bgp"],
                "items": {
                  "format": {
                    "route-map": {
                      "description": "用于过滤或转换从此来源重分发的路由的路由映射。", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"
                    },
                    "source": {"description": "要从中重分发路由的协议。", "enum": ["connected", "kernel", "ospf", "static"], "type": "string"}
                  },
                  "type": "string"
                },
                "optional": 1, "type": "array"
              }
            ],
            "type": "array", "type-property": "protocol"
          },
          "route_filter": {
            "description": "用于过滤将安装到内核路由表中的路由的前缀列表", "format": "pve-sdn-prefix-list-id", "instance-types": ["ospf", "openfabric"],
            "optional": 1, "type": "string", "type-property": "protocol"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "nodes": {
      "items": {
        "properties": {
          "allowed_ips": {
            "description": "WireGuard fabric 中可经由此节点路由的 IP 列表。", "instance-types": ["wireguard"],
            "items": {"format": "FullRangeCIDR", "type": "string"}, "optional": 1, "type": "array", "type-property": "protocol"
          },
          "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
          "endpoint": {"description": "用于连接此节点的端点。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
          "fabric_id": {
            "description": "SDN fabric 的标识符", "format": "pve-sdn-fabric-id", "maxLength": 8, "minLength": 2,
            "pattern": "[a-zA-Z0-9][a-zA-Z0-9-]{0,6}[a-zA-Z0-9]", "type": "string"
          },
          "interfaces": {
            "oneOf": [
              {
                "description": "OpenFabric 网络接口", "instance-types": ["openfabric"],
                "items": {
                  "format": {
                    "hello_multiplier": {"description": "接口的 hello_multiplier 属性", "maximum": 100, "minimum": 2, "optional": 1, "type": "integer"},
                    "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
                    "ip6": {"description": "此节点的 IPv6 地址", "format": "CIDRv6", "optional": 1, "type": "string"},
                    "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}
                  },
                  "type": "string"
                },
                "optional": 1, "type": "array"
              },
              {
                "description": "OSPF 网络接口", "instance-types": ["ospf"],
                "items": {
                  "format": {
                    "ip": {"description": "此节点的 IPv4 地址", "format": "CIDRv4", "optional": 1, "type": "string"},
                    "name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"},
                    "network_type": {
                      "description": "OSPF 接口的网络类型", "enum": ["broadcast", "non-broadcast", "point-to-multipoint", "point-to-point"], "optional": 1,
                      "type": "string"
                    }
                  },
                  "type": "string"
                },
                "optional": 1, "type": "array"
              },
              {
                "description": "此节点的 WireGuard 网络接口列表。", "instance-types": ["wireguard"],
                "items": {"description": "WireGuard 网络接口", "format": "pve-sdn-fabric-wireguard-interface", "type": "string"}, "optional": 1, "type": "array"
              },
              {
                "description": "BGP 网络接口", "instance-types": ["bgp"],
                "items": {"format": {"name": {"description": "网络接口名称", "format": "pve-iface", "type": "string"}}, "type": "string"}, "optional": 1
              }
            ],
            "type": "array", "type-property": "protocol"
          },
          "ip": {"description": "此节点的 IPv4 地址", "format": "ipv4", "optional": 1, "type": "string"},
          "ip6": {"description": "此节点的 IPv6 地址", "format": "ipv6", "optional": 1, "type": "string"},
          "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string"},
          "node_id": {"description": "SDN fabric 中节点的标识符", "format": "pve-node", "type": "string"},
          "peers": {
            "instance-types": ["wireguard"],
            "items": {
              "format": {
                "endpoint": {"description": "覆盖节点配置节中的端点设置。", "optional": 1, "type": "string"},
                "iface": {"description": "此节点使用此对等端定义的接口。", "type": "string"},
                "node": {"description": "所引用节点配置节的名称（外部节点或内部对等节点）。", "type": "string"},
                "node_iface": {"description": "另一个节点的接口（如果它是内部节点）", "optional": 1, "type": "string"},
                "skip_route_generation": {"default": 0, "description": "是否应在内核路由表中为允许的 IP 创建路由。", "optional": 1, "type": "boolean"},
                "type": {"enum": ["internal", "external"], "type": "string"}
              },
              "type": "string"
            },
            "optional": 1, "type": "array", "type-property": "protocol"
          },
          "protocol": {"description": "SDN Fabric 配置节中配置条目的类型", "enum": ["openfabric", "ospf", "wireguard", "bgp"], "type": "string"},
          "public_key": {"description": "外部节点的公钥。", "instance-types": ["wireguard"], "optional": 1, "type": "string", "type-property": "protocol"},
          "role": {
            "description": "此节点在 WireGuard fabric 中的角色。", "enum": ["internal", "external"], "instance-types": ["wireguard"], "optional": 1,
            "type": "string", "type-property": "protocol"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/fabrics/all)。

## `/cluster/sdn/prefix-lists` <a href="#api-cluster-sdn-prefix-lists-13d00bf0" id="api-cluster-sdn-prefix-lists-13d00bf0"></a>

原始接口路径：`/cluster/sdn/prefix-lists`。

### GET `/cluster/sdn/prefix-lists` <a href="#api-cluster-sdn-prefix-lists-13d00bf0-get" id="api-cluster-sdn-prefix-lists-13d00bf0-get"></a>

列出前缀列表

**方法标识：** `list_prefix_lists`

**权限**

```text
{"description": "仅返回您具有 'SDN.Audit' 或 'SDN.Allocate' 权限的前缀列表条目。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-13d00bf0-get-parameters" id="api-cluster-sdn-prefix-lists-13d00bf0-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |
| `verbose` | 类型：boolean；必填：否；默认值：—<br>如果为 0，则仅返回 id；否则返回所有属性。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "verbose": {"description": "如果为 0，则仅返回 id；否则返回所有属性。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-13d00bf0-get-returns" id="api-cluster-sdn-prefix-lists-13d00bf0-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{id}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/sdn/prefix-lists` <a href="#api-cluster-sdn-prefix-lists-13d00bf0-post" id="api-cluster-sdn-prefix-lists-13d00bf0-post"></a>

创建前缀列表

**方法标识：** `create_prefix_list_entry`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-13d00bf0-post-parameters" id="api-cluster-sdn-prefix-lists-13d00bf0-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `entries` | 类型：array；必填：否；默认值：—<br> |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "entries": {
      "items": {
        "format": {
          "action": {"enum": ["permit", "deny"], "optional": 0, "type": "string"}, "ge": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer"},
          "le": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer"}, "prefix": {"format": "FullRangeCIDR", "optional": 0, "type": "string"},
          "seq": {"maximum": 4294967295, "minimum": 1, "optional": 1, "type": "integer"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-13d00bf0-post-returns" id="api-cluster-sdn-prefix-lists-13d00bf0-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/prefix-lists)。

## `/cluster/sdn/prefix-lists/{id}` <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8" id="api-cluster-sdn-prefix-lists-id-b74f6ac8"></a>

原始接口路径：`/cluster/sdn/prefix-lists/{id}`。

### DELETE `/cluster/sdn/prefix-lists/{id}` <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-delete" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-delete"></a>

删除前缀列表

**方法标识：** `delete_prefix_list`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-delete-parameters" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-delete-returns" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/prefix-lists/{id}` <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-get" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-get"></a>

获取前缀列表

**方法标识：** `get_prefix_list`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-get-parameters" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{"properties": {"id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-get-returns" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/sdn/prefix-lists/{id}` <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-put" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-put"></a>

更新前缀列表

**方法标识：** `update_prefix_list`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-put-parameters" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：array；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `entries` | 类型：array；必填：否；默认值：—<br> |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "delete": {"items": {"enum": ["entries"], "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "entries": {
      "items": {
        "format": {
          "action": {"enum": ["permit", "deny"], "optional": 1, "type": "string"}, "ge": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer"},
          "le": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer"}, "prefix": {"format": "FullRangeCIDR", "optional": 1, "type": "string"},
          "seq": {"maximum": 4294967295, "minimum": 1, "optional": 1, "type": "integer"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-b74f6ac8-put-returns" id="api-cluster-sdn-prefix-lists-id-b74f6ac8-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/prefix-lists/{id})。

## `/cluster/sdn/prefix-lists/{id}/entries` <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496"></a>

原始接口路径：`/cluster/sdn/prefix-lists/{id}/entries`。

### GET `/cluster/sdn/prefix-lists/{id}/entries` <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496-get" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496-get"></a>

列出前缀列表条目

**方法标识：** `get_prefix_list_entries`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496-get-parameters" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{"properties": {"id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496-get-returns" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "links": [{"href": "{seq}", "rel": "child"}], "type": "array"}
```

### POST `/cluster/sdn/prefix-lists/{id}/entries` <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496-post" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496-post"></a>

创建前缀列表条目

**方法标识：** `create_prefix_list_entry`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496-post-parameters" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：是；默认值：—<br>；可选值：`permit`, `deny` |
| `ge` | 类型：integer；必填：否；默认值：—<br> |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |
| `le` | 类型：integer；必填：否；默认值：—<br> |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `prefix` | 类型：string；必填：是；默认值：—<br> |
| `seq` | 类型：integer；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "action": {"enum": ["permit", "deny"], "optional": 0, "type": "string"},
    "ge": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 128)"},
    "id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"},
    "le": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 128)"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "prefix": {"format": "FullRangeCIDR", "optional": 0, "type": "string", "typetext": "<string>"},
    "seq": {"maximum": 4294967295, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 4294967295)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-entries-91d4d496-post-returns" id="api-cluster-sdn-prefix-lists-id-entries-91d4d496-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/prefix-lists/{id}/entries)。

## `/cluster/sdn/prefix-lists/{id}/entries/{url_seq}` <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3"></a>

原始接口路径：`/cluster/sdn/prefix-lists/{id}/entries/{url_seq}`。

### DELETE `/cluster/sdn/prefix-lists/{id}/entries/{url_seq}` <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-delete" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-delete"></a>

删除前缀列表条目

**方法标识：** `delete_prefix_list_entry`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-delete-parameters" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-delete-returns" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/prefix-lists/{id}/entries/{url_seq}` <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-get" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-get"></a>

获取前缀列表条目

**方法标识：** `get_prefix_list_entry`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-get-parameters" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>SDN 前缀列表标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{"properties": {"id": {"description": "SDN 前缀列表标识符", "format": "pve-sdn-prefix-list-id", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-get-returns" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-get-returns"></a>

```text
{"type": "object"}
```

### PUT `/cluster/sdn/prefix-lists/{id}/entries/{url_seq}` <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-put" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-put"></a>

更新前缀列表条目

**方法标识：** `update_prefix_list_entry`

**权限**

```text
{"check": ["perm", "/sdn/prefix-lists/{id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-put-parameters" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：否；默认值：—<br>；可选值：`permit`, `deny` |
| `delete` | 类型：array；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `ge` | 类型：integer；必填：否；默认值：—<br> |
| `le` | 类型：integer；必填：否；默认值：—<br> |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `prefix` | 类型：string；必填：否；默认值：—<br> |
| `seq` | 类型：integer；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "action": {"enum": ["permit", "deny"], "optional": 1, "type": "string"},
    "delete": {"items": {"enum": ["le", "ge", "seq"], "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "ge": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 128)"},
    "le": {"maximum": 128, "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - 128)"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "prefix": {"format": "FullRangeCIDR", "optional": 1, "type": "string", "typetext": "<string>"},
    "seq": {"maximum": 4294967295, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 4294967295)"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-put-returns" id="api-cluster-sdn-prefix-lists-id-entries-url-seq-601484c3-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/prefix-lists/{id}/entries/{url_seq})。

## `/cluster/sdn/route-maps` <a href="#api-cluster-sdn-route-maps-97fc73e0" id="api-cluster-sdn-route-maps-97fc73e0"></a>

原始接口路径：`/cluster/sdn/route-maps`。

### GET `/cluster/sdn/route-maps` <a href="#api-cluster-sdn-route-maps-97fc73e0-get" id="api-cluster-sdn-route-maps-97fc73e0-get"></a>

列出路由映射

**方法标识：** `list_route_maps`

**权限**

```text
{"description": "仅返回您具有 'SDN.Audit' 或 'SDN.Allocate' 权限的路由映射。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-97fc73e0-get-parameters" id="api-cluster-sdn-route-maps-97fc73e0-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"properties": {"running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-97fc73e0-get-returns" id="api-cluster-sdn-route-maps-97fc73e0-get-returns"></a>

```text
{
  "items": {"properties": {"id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string"}}, "type": "object"},
  "links": [{"href": "entries/{id}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/route-maps)。

## `/cluster/sdn/route-maps/entries` <a href="#api-cluster-sdn-route-maps-entries-f6225287" id="api-cluster-sdn-route-maps-entries-f6225287"></a>

原始接口路径：`/cluster/sdn/route-maps/entries`。

### GET `/cluster/sdn/route-maps/entries` <a href="#api-cluster-sdn-route-maps-entries-f6225287-get" id="api-cluster-sdn-route-maps-entries-f6225287-get"></a>

列出所有路由映射条目。

**方法标识：** `list_route_map_entries`

**权限**

```text
{"description": "仅返回您具有 'SDN.Audit' 或 'SDN.Allocate' 权限的路由映射条目。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-entries-f6225287-get-parameters" id="api-cluster-sdn-route-maps-entries-f6225287-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-entries-f6225287-get-returns" id="api-cluster-sdn-route-maps-entries-f6225287-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "action": {"description": "路由映射条目的匹配策略。", "enum": ["permit", "deny"], "optional": 0, "type": "string"},
      "call": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "exit-action": {
        "format": {
          "key": {"enum": ["on-match-goto", "on-match-next", "continue"], "type": "string"},
          "value": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "optional": 1, "type": "integer"}
        },
        "optional": 1, "type": "string"
      },
      "match": {
        "items": {
          "format": {
            "key": {
              "enum": [
                "route-type", "vni", "ip-address-prefix-list", "ip6-address-prefix-list", "ip-next-hop-prefix-list", "ip6-next-hop-prefix-list",
                "ip-next-hop-address", "ip6-next-hop-address", "metric", "local-preference", "peer", "tag"
              ],
              "type": "string"
            },
            "value": {"description": "字段 <key> 应匹配的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
          },
          "type": "string"
        },
        "optional": 1, "type": "array"
      },
      "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer"},
      "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string"},
      "set": {
        "items": {
          "format": {
            "key": {
              "enum": [
                "ip-next-hop-peer-address", "ip-next-hop", "ip-next-hop-unchanged", "ip6-next-hop-peer-address", "ip6-next-hop-prefer-global", "ip6-next-hop",
                "local-preference", "tag", "weight", "metric", "src"
              ],
              "type": "string"
            },
            "value": {"description": "字段 <key> 应设置的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
          },
          "type": "string"
        },
        "optional": 1, "type": "array"
      }
    },
    "type": "object"
  },
  "links": [{"href": "{route-map-id}", "rel": "child"}], "type": "array"
}
```

### POST `/cluster/sdn/route-maps/entries` <a href="#api-cluster-sdn-route-maps-entries-f6225287-post" id="api-cluster-sdn-route-maps-entries-f6225287-post"></a>

创建路由映射条目

**方法标识：** `create_route_map_entry`

**权限**

```text
{"check": ["perm", "/sdn/route-maps", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-entries-f6225287-post-parameters" id="api-cluster-sdn-route-maps-entries-f6225287-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：是；默认值：—<br>路由映射条目的匹配策略。；可选值：`permit`, `deny` |
| `call` | 类型：string；必填：否；默认值：—<br>SDN 路由映射标识符 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `exit-action` | 类型：string；必填：否；默认值：—<br> |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `match` | 类型：array；必填：否；默认值：—<br> |
| `order` | 类型：integer；必填：是；默认值：—<br>此路由映射条目的索引 |
| `route-map-id` | 类型：string；必填：是；默认值：—<br>SDN 路由映射标识符 |
| `set` | 类型：array；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "action": {"description": "路由映射条目的匹配策略。", "enum": ["permit", "deny"], "optional": 0, "type": "string"},
    "call": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "exit-action": {
      "format": {
        "key": {"enum": ["on-match-goto", "on-match-next", "continue"], "type": "string"},
        "value": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "optional": 1, "type": "integer"}
      },
      "optional": 1, "type": "string", "typetext": "key=<on-match-goto|on-match-next|continue> [,value=<integer>]"
    },
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "match": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "route-type", "vni", "ip-address-prefix-list", "ip6-address-prefix-list", "ip-next-hop-prefix-list", "ip6-next-hop-prefix-list",
              "ip-next-hop-address", "ip6-next-hop-address", "metric", "local-preference", "peer", "tag"
            ],
            "type": "string"
          },
          "value": {"description": "字段 <key> 应匹配的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer", "typetext": "<integer> (0 - 65535)"},
    "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string", "typetext": "<string>"},
    "set": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "ip-next-hop-peer-address", "ip-next-hop", "ip-next-hop-unchanged", "ip6-next-hop-peer-address", "ip6-next-hop-prefer-global", "ip6-next-hop",
              "local-preference", "tag", "weight", "metric", "src"
            ],
            "type": "string"
          },
          "value": {"description": "字段 <key> 应设置的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-entries-f6225287-post-returns" id="api-cluster-sdn-route-maps-entries-f6225287-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/route-maps/entries)。

## `/cluster/sdn/route-maps/entries/{route-map-id}` <a href="#api-cluster-sdn-route-maps-entries-route-map-id-44340de7" id="api-cluster-sdn-route-maps-entries-route-map-id-44340de7"></a>

原始接口路径：`/cluster/sdn/route-maps/entries/{route-map-id}`。

### GET `/cluster/sdn/route-maps/entries/{route-map-id}` <a href="#api-cluster-sdn-route-maps-entries-route-map-id-44340de7-get" id="api-cluster-sdn-route-maps-entries-route-map-id-44340de7-get"></a>

列出给定路由映射的所有条目

**方法标识：** `list_route_map_entries_for_route_map`

**权限**

```text
{"check": ["perm", "/sdn/route-maps/{route-map-id}", ["SDN.Audit", "SDN.Allocate"], "any", 1]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-44340de7-get-parameters" id="api-cluster-sdn-route-maps-entries-route-map-id-44340de7-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `pending` | 类型：boolean；必填：否；默认值：—<br>显示待应用的配置。 |
| `route-map-id` | 类型：string；必填：是；默认值：—<br>SDN 路由映射标识符 |
| `running` | 类型：boolean；必填：否；默认值：—<br>显示运行中的配置。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "pending": {"description": "显示待应用的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string", "typetext": "<string>"},
    "running": {"description": "显示运行中的配置。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-44340de7-get-returns" id="api-cluster-sdn-route-maps-entries-route-map-id-44340de7-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "action": {"description": "路由映射条目的匹配策略。", "enum": ["permit", "deny"], "optional": 0, "type": "string"},
      "call": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
      "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
      "exit-action": {
        "format": {
          "key": {"enum": ["on-match-goto", "on-match-next", "continue"], "type": "string"},
          "value": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "optional": 1, "type": "integer"}
        },
        "optional": 1, "type": "string"
      },
      "match": {
        "items": {
          "format": {
            "key": {
              "enum": [
                "route-type", "vni", "ip-address-prefix-list", "ip6-address-prefix-list", "ip-next-hop-prefix-list", "ip6-next-hop-prefix-list",
                "ip-next-hop-address", "ip6-next-hop-address", "metric", "local-preference", "peer", "tag"
              ],
              "type": "string"
            },
            "value": {"description": "字段 <key> 应匹配的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
          },
          "type": "string"
        },
        "optional": 1, "type": "array"
      },
      "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer"},
      "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string"},
      "set": {
        "items": {
          "format": {
            "key": {
              "enum": [
                "ip-next-hop-peer-address", "ip-next-hop", "ip-next-hop-unchanged", "ip6-next-hop-peer-address", "ip6-next-hop-prefer-global", "ip6-next-hop",
                "local-preference", "tag", "weight", "metric", "src"
              ],
              "type": "string"
            },
            "value": {"description": "字段 <key> 应设置的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
          },
          "type": "string"
        },
        "optional": 1, "type": "array"
      }
    },
    "type": "object"
  },
  "links": [{"href": "entry/{order}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/route-maps/entries/{route-map-id})。

## `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}` <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738"></a>

原始接口路径：`/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}`。

### DELETE `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}` <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-delete" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-delete"></a>

删除路由映射条目

**方法标识：** `delete_route_map_entry`

**权限**

```text
{"check": ["perm", "/sdn/route-maps/{route-map-id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-delete-parameters" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `order` | 类型：integer；必填：是；默认值：—<br>此路由映射条目的索引 |
| `route-map-id` | 类型：string；必填：是；默认值：—<br>SDN 路由映射标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer", "typetext": "<integer> (0 - 65535)"},
    "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-delete-returns" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}` <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-get" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-get"></a>

获取路由映射条目

**方法标识：** `get_route_map_entry`

**权限**

```text
{"check": ["perm", "/sdn/route-maps/{route-map-id}", ["SDN.Audit", "SDN.Allocate"], "any", 1]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-get-parameters" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `order` | 类型：integer；必填：是；默认值：—<br>此路由映射条目的索引 |
| `route-map-id` | 类型：string；必填：是；默认值：—<br>SDN 路由映射标识符 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer", "typetext": "<integer> (0 - 65535)"},
    "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-get-returns" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-get-returns"></a>

```text
{
  "properties": {
    "action": {"description": "路由映射条目的匹配策略。", "enum": ["permit", "deny"], "optional": 0, "type": "string"},
    "call": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string"},
    "exit-action": {
      "format": {
        "key": {"enum": ["on-match-goto", "on-match-next", "continue"], "type": "string"},
        "value": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "optional": 1, "type": "integer"}
      },
      "optional": 1, "type": "string"
    },
    "match": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "route-type", "vni", "ip-address-prefix-list", "ip6-address-prefix-list", "ip-next-hop-prefix-list", "ip6-next-hop-prefix-list",
              "ip-next-hop-address", "ip6-next-hop-address", "metric", "local-preference", "peer", "tag"
            ],
            "type": "string"
          },
          "value": {"description": "字段 <key> 应匹配的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array"
    },
    "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer"},
    "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string"},
    "set": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "ip-next-hop-peer-address", "ip-next-hop", "ip-next-hop-unchanged", "ip6-next-hop-peer-address", "ip6-next-hop-prefer-global", "ip6-next-hop",
              "local-preference", "tag", "weight", "metric", "src"
            ],
            "type": "string"
          },
          "value": {"description": "字段 <key> 应设置的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array"
    }
  },
  "type": "object"
}
```

### PUT `/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order}` <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-put" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-put"></a>

更新路由映射条目

**方法标识：** `update_route_map_entry`

**权限**

```text
{"check": ["perm", "/sdn/route-maps/{route-map-id}", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-put-parameters" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `action` | 类型：string；必填：否；默认值：—<br>路由映射条目的匹配策略。；可选值：`permit`, `deny` |
| `call` | 类型：string；必填：否；默认值：—<br>SDN 路由映射标识符 |
| `delete` | 类型：array；必填：否；默认值：—<br> |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `exit-action` | 类型：string；必填：否；默认值：—<br> |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `match` | 类型：array；必填：否；默认值：—<br> |
| `order` | 类型：integer；必填：是；默认值：—<br>此路由映射条目的索引 |
| `route-map-id` | 类型：string；必填：是；默认值：—<br>SDN 路由映射标识符 |
| `set` | 类型：array；必填：否；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "properties": {
    "action": {"description": "路由映射条目的匹配策略。", "enum": ["permit", "deny"], "optional": 1, "type": "string"},
    "call": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "optional": 1, "type": "string", "typetext": "<string>"},
    "delete": {"items": {"enum": ["set", "match", "call", "exit-action"], "type": "string"}, "optional": 1, "type": "array", "typetext": "<array>"},
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "exit-action": {
      "format": {
        "key": {"enum": ["on-match-goto", "on-match-next", "continue"], "type": "string"},
        "value": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "optional": 1, "type": "integer"}
      },
      "optional": 1, "type": "string", "typetext": "key=<on-match-goto|on-match-next|continue> [,value=<integer>]"
    },
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "match": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "route-type", "vni", "ip-address-prefix-list", "ip6-address-prefix-list", "ip-next-hop-prefix-list", "ip6-next-hop-prefix-list",
              "ip-next-hop-address", "ip6-next-hop-address", "metric", "local-preference", "peer", "tag"
            ],
            "type": "string"
          },
          "value": {"description": "字段 <key> 应匹配的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    },
    "order": {"description": "此路由映射条目的索引", "maximum": 65535, "minimum": 0, "type": "integer", "typetext": "<integer> (0 - 65535)"},
    "route-map-id": {"description": "SDN 路由映射标识符", "format": "pve-sdn-route-map-id", "type": "string", "typetext": "<string>"},
    "set": {
      "items": {
        "format": {
          "key": {
            "enum": [
              "ip-next-hop-peer-address", "ip-next-hop", "ip-next-hop-unchanged", "ip6-next-hop-peer-address", "ip6-next-hop-prefer-global", "ip6-next-hop",
              "local-preference", "tag", "weight", "metric", "src"
            ],
            "type": "string"
          },
          "value": {"description": "字段 <key> 应设置的值。", "format_description": "<key-dependent>", "optional": 1, "type": "string"}
        },
        "type": "string"
      },
      "optional": 1, "type": "array", "typetext": "<array>"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-put-returns" id="api-cluster-sdn-route-maps-entries-route-map-id-entry-order-bda0b738-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/route-maps/entries/{route-map-id}/entry/{order})。

## `/cluster/sdn/lock` <a href="#api-cluster-sdn-lock-64a794f1" id="api-cluster-sdn-lock-64a794f1"></a>

原始接口路径：`/cluster/sdn/lock`。

### DELETE `/cluster/sdn/lock` <a href="#api-cluster-sdn-lock-64a794f1-delete" id="api-cluster-sdn-lock-64a794f1-delete"></a>

释放 SDN 配置的全局锁

**方法标识：** `release_lock`

**权限**

```text
{"check": ["perm", "/sdn", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-lock-64a794f1-delete-parameters" id="api-cluster-sdn-lock-64a794f1-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `force` | 类型：boolean；必填：否；默认值：0<br>如果为 true，则允许在未提供令牌的情况下释放锁 |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "force": {"default": 0, "description": "如果为 true，则允许在未提供令牌的情况下释放锁", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-lock-64a794f1-delete-returns" id="api-cluster-sdn-lock-64a794f1-delete-returns"></a>

```text
{"type": "null"}
```

### POST `/cluster/sdn/lock` <a href="#api-cluster-sdn-lock-64a794f1-post" id="api-cluster-sdn-lock-64a794f1-post"></a>

获取 SDN 配置的全局锁

**方法标识：** `lock`

**权限**

```text
{"check": ["perm", "/sdn", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-lock-64a794f1-post-parameters" id="api-cluster-sdn-lock-64a794f1-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `allow-pending` | 类型：boolean；必填：否；默认值：0<br>如果为 true，则即使有待应用的更改，也允许获取锁 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "allow-pending": {"default": 0, "description": "如果为 true，则即使有待应用的更改，也允许获取锁", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-lock-64a794f1-post-returns" id="api-cluster-sdn-lock-64a794f1-post-returns"></a>

```text
{"type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/lock)。

## `/cluster/sdn/rollback` <a href="#api-cluster-sdn-rollback-c78eeaa9" id="api-cluster-sdn-rollback-c78eeaa9"></a>

原始接口路径：`/cluster/sdn/rollback`。

### POST `/cluster/sdn/rollback` <a href="#api-cluster-sdn-rollback-c78eeaa9-post" id="api-cluster-sdn-rollback-c78eeaa9-post"></a>

回滚 SDN 配置的待应用更改

**方法标识：** `rollback`

**权限**

```text
{"check": ["perm", "/sdn", ["SDN.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-sdn-rollback-c78eeaa9-post-parameters" id="api-cluster-sdn-rollback-c78eeaa9-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `lock-token` | 类型：string；必填：否；默认值：—<br>用于解锁全局 SDN 配置的令牌 |
| `release-lock` | 类型：boolean；必填：否；默认值：1<br>提供 lock-token 且配置成功回滚后，自动释放锁 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "lock-token": {"description": "用于解锁全局 SDN 配置的令牌", "optional": 1, "type": "string", "typetext": "<string>"},
    "release-lock": {"default": 1, "description": "提供 lock-token 且配置成功回滚后，自动释放锁", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-rollback-c78eeaa9-post-returns" id="api-cluster-sdn-rollback-c78eeaa9-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/rollback)。

## `/cluster/sdn/dry-run` <a href="#api-cluster-sdn-dry-run-4c0d2322" id="api-cluster-sdn-dry-run-4c0d2322"></a>

原始接口路径：`/cluster/sdn/dry-run`。

### GET `/cluster/sdn/dry-run` <a href="#api-cluster-sdn-dry-run-4c0d2322-get" id="api-cluster-sdn-dry-run-4c0d2322-get"></a>

试运行 SDN 应用操作，并返回当前配置与待应用配置之间的差异

**方法标识：** `dry-run`

**权限**

```text
{"check": ["perm", "/nodes/{node}", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

**代理目标：** `"node"`

#### 请求参数 <a href="#api-cluster-sdn-dry-run-4c0d2322-get-parameters" id="api-cluster-sdn-dry-run-4c0d2322-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `node` | 类型：string；必填：是；默认值：—<br>集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"node": {"description": "集群节点名称。", "format": "pve-node", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-cluster-sdn-dry-run-4c0d2322-get-returns" id="api-cluster-sdn-dry-run-4c0d2322-get-returns"></a>

```text
{
  "properties": {
    "frr-diff": {"description": "当前 FRR 配置与待应用 FRR 配置之间的差异。", "optional": 1, "type": "string"},
    "interfaces-diff": {"description": "当前 /etc/network/interfaces.d/sdn 配置与待应用配置之间的差异。", "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/dry-run)。

## `/cluster/log` <a href="#api-cluster-log-8cac6725" id="api-cluster-log-8cac6725"></a>

原始接口路径：`/cluster/log`。

### GET `/cluster/log` <a href="#api-cluster-log-8cac6725-get" id="api-cluster-log-8cac6725-get"></a>

读取集群日志

**方法标识：** `log`

**权限**

```text
{"description": "用户需要对 '/' 具有 'Sys.Syslog' 权限，才能获取所有日志。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-log-8cac6725-get-parameters" id="api-cluster-log-8cac6725-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `max` | 类型：integer；必填：否；默认值：—<br>最大条目数。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"max": {"description": "最大条目数。", "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - N)"}}
}
```

</details>

#### 返回值 <a href="#api-cluster-log-8cac6725-get-returns" id="api-cluster-log-8cac6725-get-returns"></a>

```text
{"items": {"properties": {}, "type": "object"}, "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/log)。

## `/cluster/resources` <a href="#api-cluster-resources-ec05b307" id="api-cluster-resources-ec05b307"></a>

原始接口路径：`/cluster/resources`。

### GET `/cluster/resources` <a href="#api-cluster-resources-ec05b307-get" id="api-cluster-resources-ec05b307-get"></a>

资源索引（整个集群）。

**方法标识：** `resources`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-resources-ec05b307-get-parameters" id="api-cluster-resources-ec05b307-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `type` | 类型：string；必填：否；默认值：—<br>资源类型。；可选值：`vm`, `storage`, `node`, `sdn` |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"type": {"description": "资源类型。", "enum": ["vm", "storage", "node", "sdn"], "optional": 1, "type": "string"}}}
```

</details>

#### 返回值 <a href="#api-cluster-resources-ec05b307-get-returns" id="api-cluster-resources-ec05b307-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "cgroup-mode": {"description": "节点运行所用的 cgroup 模式（用于 'node' 类型）。", "optional": 1, "type": "integer"},
      "content": {"description": "允许的存储内容类型（用于 'storage' 类型）。", "format": "pve-storage-content-list", "optional": 1, "type": "string"},
      "cpu": {
        "description": "CPU 使用率（用于 'node'、'qemu' 和 'lxc' 类型）。", "minimum": 0, "optional": 1, "renderer": "fraction_as_percentage", "type": "number"
      },
      "disk": {
        "description": "已用磁盘空间，单位为字节（用于 'storage' 类型）；虚拟机已用根镜像空间（用于 'qemu' 和 'lxc' 类型）。", "minimum": 0, "optional": 1,
        "renderer": "bytes", "type": "integer"
      },
      "diskread": {
        "description": "自客户机启动以来从其块设备读取的字节数。并非所有存储类型都提供此信息。（用于 'qemu' 和 'lxc' 类型）", "optional": 1,
        "renderer": "bytes", "type": "integer"
      },
      "diskwrite": {
        "description": "自客户机启动以来写入其块设备的字节数。并非所有存储类型都提供此信息。（用于 'qemu' 和 'lxc' 类型）", "optional": 1, "renderer": "bytes",
        "type": "integer"
      },
      "hastate": {"description": "HA 服务状态（用于 HA 管理的虚拟机）。", "optional": 1, "type": "string"},
      "host-arch": {
        "default": "x86_64", "description": "节点的 CPU 架构。（用于 'node' 类型）。", "enum": ["x86_64", "aarch64"], "optional": 1, "type": "string"
      },
      "id": {"description": "资源 ID。", "type": "string"}, "level": {"description": "支持级别（用于 'node' 类型）。", "optional": 1, "type": "string"},
      "lock": {"description": "客户机当前的配置锁（用于 'qemu' 和 'lxc' 类型）", "optional": 1, "type": "string"},
      "maxcpu": {"description": "可用 CPU 数量（用于 'node'、'qemu' 和 'lxc' 类型）。", "minimum": 0, "optional": 1, "type": "number"},
      "maxdisk": {
        "description": "存储大小，单位为字节（用于 'storage' 类型）；虚拟机根镜像大小（用于 'qemu' 和 'lxc' 类型）。", "minimum": 0, "optional": 1,
        "renderer": "bytes", "type": "integer"
      },
      "maxmem": {"description": "可用内存字节数（用于 'node'、'qemu' 和 'lxc' 类型）。", "optional": 1, "renderer": "bytes", "type": "integer"},
      "mem": {"description": "已用内存字节数（用于 'node'、'qemu' 和 'lxc' 类型）。", "minimum": 0, "optional": 1, "renderer": "bytes", "type": "integer"},
      "memhost": {"description": "从宿主机角度看到的已用内存字节数（用于 'qemu' 类型）。", "minimum": 0, "optional": 1, "renderer": "bytes", "type": "integer"},
      "name": {"description": "资源名称。", "optional": 1, "type": "string"},
      "netin": {
        "description": "自客户机启动以来通过网络向其发送的流量字节数。（用于 'qemu' 和 'lxc' 类型）", "optional": 1, "renderer": "bytes", "type": "integer"
      },
      "netout": {
        "description": "自客户机启动以来通过网络从其发送的流量字节数。（用于 'qemu' 和 'lxc' 类型）", "optional": 1, "renderer": "bytes", "type": "integer"
      },
      "network": {"description": "网络实体名称（用于 'network' 类型）。", "optional": 1, "type": "string"},
      "network-type": {"description": "网络资源类型（用于 'network' 类型）。", "enum": ["fabric", "zone"], "optional": 1, "type": "string"},
      "node": {"description": "集群节点名称（用于 'node'、'storage'、'qemu' 和 'lxc' 类型）。", "format": "pve-node", "optional": 1, "type": "string"},
      "plugintype": {"description": "更具体的类型（如有）。", "optional": 1, "type": "string"},
      "pool": {"description": "资源池名称（用于 'pool'、'qemu' 和 'lxc' 类型）。", "optional": 1, "type": "string"},
      "protocol": {"description": "fabric 协议（用于 'network' 类型、'fabric' 网络类型）。", "optional": 1, "type": "string"},
      "sdn": {"description": "SDN 实体名称（用于 'sdn' 类型）", "optional": 1, "type": "string"},
      "shared": {"description": "确定存储是否共享", "optional": 1, "type": "boolean"},
      "status": {"description": "取决于资源类型的状态。", "optional": 1, "type": "string"},
      "storage": {
        "description": "存储标识符（用于 'storage' 类型）。", "format": "pve-storage-id", "format_description": "storage ID", "optional": 1, "type": "string"
      },
      "tags": {"description": "客户机的标签（用于 'qemu' 和 'lxc' 类型）", "optional": 1, "type": "string"},
      "template": {"default": 0, "description": "确定客户机是否为模板。（用于 'qemu' 和 'lxc' 类型）", "optional": 1, "type": "boolean"},
      "type": {"description": "资源类型。", "enum": ["node", "storage", "pool", "qemu", "lxc", "openvz", "sdn", "network"], "type": "string"},
      "uptime": {
        "description": "节点或虚拟客户机的运行时间，单位为秒（用于 'node'、'qemu' 和 'lxc' 类型）。", "optional": 1, "renderer": "duration", "type": "integer"
      },
      "vmid": {
        "description": "数值形式的 vmid（用于 'qemu' 和 'lxc' 类型）。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "optional": 1,
        "type": "integer"
      },
      "zone-type": {"description": "SDN 区域类型（用于 'sdn' 类型）。", "optional": 1, "type": "string"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/resources)。

## `/cluster/tasks` <a href="#api-cluster-tasks-9bc8e199" id="api-cluster-tasks-9bc8e199"></a>

原始接口路径：`/cluster/tasks`。

### GET `/cluster/tasks` <a href="#api-cluster-tasks-9bc8e199-get" id="api-cluster-tasks-9bc8e199-get"></a>

列出近期任务（整个集群）。

**方法标识：** `tasks`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-tasks-9bc8e199-get-parameters" id="api-cluster-tasks-9bc8e199-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-tasks-9bc8e199-get-returns" id="api-cluster-tasks-9bc8e199-get-returns"></a>

```text
{"items": {"properties": {"upid": {"type": "string"}}, "type": "object"}, "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/tasks)。

## `/cluster/options` <a href="#api-cluster-options-096be758" id="api-cluster-options-096be758"></a>

原始接口路径：`/cluster/options`。

### GET `/cluster/options` <a href="#api-cluster-options-096be758-get" id="api-cluster-options-096be758-get"></a>

获取数据中心选项。如果对 '/' 没有 'Sys.Audit' 权限，则不会返回所有选项。

**方法标识：** `get_options`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]], "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-options-096be758-get-parameters" id="api-cluster-options-096be758-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-options-096be758-get-returns" id="api-cluster-options-096be758-get-returns"></a>

```text
{
  "properties": {
    "allowed-tags": {"description": "当前用户可设置和查看的标签。", "items": {"description": "标签。", "type": "string"}, "type": "array"},
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {"description": "克隆磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "default": {"description": "默认带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "migration": {
          "description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1,
          "type": "number"
        },
        "move": {"description": "移动磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "restore": {"description": "从备份还原客户机的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}
      },
      "optional": 1, "type": "string"
    },
    "consent-text": {"description": "登录前显示的同意文本。", "maxLength": 65536, "optional": 1, "type": "string"},
    "console": {
      "description": "选择默认控制台查看器。可以使用内置 java applet（VNC；已弃用，会映射到 html5）、与外部 virt-viewer 兼容的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如虚拟机未启用 SPICE），则回退到 noVNC。",
      "enum": ["applet", "vv", "html5", "xtermjs"], "optional": 1, "type": "string"
    },
    "crs": {
      "description": "集群资源调度设置。",
      "format": {
        "ha": {
          "default": "basic", "description": "为 HA 使用此资源调度器模式。", "enum": ["basic", "static", "dynamic"], "optional": 1, "type": "string",
          "verbose_description": "配置 HA 管理器应如何选择节点以启动或恢复服务：\n\n- 'basic'：仅使用服务数量，\n- 'static'：考虑服务的静态 CPU 和内存配置，\n- 'dynamic'：考虑服务的静态和动态 CPU 及内存用量。\n"
        },
        "ha-auto-rebalance": {"default": 0, "description": "是否根据当前节点不均衡程度使用 CRS 自动均衡 HA 资源。", "optional": 1, "type": "boolean"},
        "ha-auto-rebalance-hold-duration": {
          "default": 3, "description": "集群节点不均衡程度必须连续超过阈值的 HA 轮次数，达到后触发自动资源均衡迁移。", "minimum": 0, "optional": 1,
          "requires": "ha-auto-rebalance", "type": "number"
        },
        "ha-auto-rebalance-margin": {
          "default": 10, "description": "执行资源均衡迁移所需的集群节点不均衡程度最小相对改善百分比。", "maximum": 100, "minimum": 0, "optional": 1,
          "requires": "ha-auto-rebalance", "type": "number"
        },
        "ha-auto-rebalance-method": {
          "default": "bruteforce", "description": "对均衡迁移进行评分所用的方法。", "enum": ["bruteforce", "topsis"], "optional": 1,
          "requires": "ha-auto-rebalance", "type": "string"
        },
        "ha-auto-rebalance-threshold": {
          "default": 30, "description": "集群节点不均衡百分比，超过此值将触发自动资源均衡系统。", "maximum": 100, "minimum": 0, "optional": 1,
          "requires": "ha-auto-rebalance", "type": "number"
        },
        "ha-rebalance-on-start": {
          "default": 0, "description": "设置为在 HA 服务请求状态从 stop 变为 start 时使用 CRS 选择合适节点。", "optional": 1, "type": "boolean"
        }
      },
      "optional": 1, "type": "string"
    },
    "description": {
      "description": "数据中心描述。显示在 Web 界面的数据中心备注面板中。作为注释保存在配置文件中。", "maxLength": 65536, "optional": 1, "type": "string"
    },
    "email_from": {"description": "指定发送通知所用的电子邮件发件地址（默认为 root@$hostname）", "format": "email-opt", "optional": 1, "type": "string"},
    "fencing": {
      "default": "watchdog",
      "description": "设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中正确配置隔离设备。both 模式同时使用这两种模式。\n\n警告：'hardware' 和 'both' 均为实验性功能，仍在开发中",
      "enum": ["watchdog", "hardware", "both"], "optional": 1, "type": "string"
    },
    "ha": {
      "description": "集群范围的 HA 设置。",
      "format": {
        "shutdown_policy": {
          "default": "conditional",
          "description": "节点关闭时 HA 服务的策略。'freeze' 禁用自动恢复，'failover' 确保恢复，'conditional' 在关机时恢复、重启时冻结。'migrate' 在可能时将正在运行的服务迁移到其他节点。使用 'freeze' 或 'failover' 时，关闭节点始终会先停止 HA 服务。",
          "enum": ["freeze", "failover", "conditional", "migrate"], "type": "string",
          "verbose_description": "描述节点关机或重启时处理 HA 服务的策略。Freeze 总是冻结关闭时仍在该节点上的服务，这些服务不会由 HA 管理器恢复。Failover 不会将服务标记为冻结，因此如果关闭的节点未迅速恢复上线（< 1min），服务将恢复到其他节点。'conditional' 根据关闭类型自动选择，即重启时冻结服务，关机时保留服务状态，从而在约 2 分钟后恢复。Migrate 在触发重启或关机时尝试将所有正在运行的服务移至其他节点。只有当节点上不再存在运行中的服务时，关机过程才会继续。如果节点重新上线，服务将移回先前关闭的节点，前提是期间没有发生其他迁移、重新安置或恢复。"
        }
      },
      "optional": 1, "type": "string"
    },
    "http_proxy": {
      "description": "指定用于下载的外部 HTTP 代理（例如：'http://username:password@host:port/')", "optional": 1, "pattern": "http://.*", "type": "string"
    },
    "keyboard": {
      "description": "VNC 服务器的默认键盘布局。",
      "enum": [
        "de", "de-ch", "da", "en-gb", "en-us", "es", "fi", "fr", "fr-be", "fr-ca", "fr-ch", "hu", "is", "it", "ja", "lt", "mk", "nl", "no", "pl", "pt", "pt-br",
        "sv", "sl", "tr"
      ],
      "optional": 1, "type": "string"
    },
    "language": {
      "description": "默认 GUI 语言。",
      "enum": [
        "ar", "ca", "da", "de", "en", "es", "eu", "fa", "fr", "hr", "he", "it", "ja", "ka", "kr", "nb", "nl", "nn", "pl", "pt_BR", "ru", "sl", "sv", "tr",
        "ukr", "zh_CN", "zh_TW"
      ],
      "optional": 1, "type": "string"
    },
    "location": {"description": "集群位置。", "format": "pve-node-location", "optional": 1, "type": "string"},
    "mac_prefix": {
      "default": "BC:24:11",
      "description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 'BC:24:11' 是 IEEE 分配给 Proxmox Server Solutions GmbH 的 OUI，对应 24 位大型 MAC 地址块。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT 后方）。",
      "format": "mac-prefix", "optional": 1, "type": "string",
      "verbose_description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），对应大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT/地址伪装后方）。\n \n请注意，当运行多个客户机网络部分或全部共享的集群时，强烈建议扩展默认 MAC 前缀，或生成自定义的有效前缀，以减少 MAC 冲突概率。例如，为每个集群在 Proxmox OUI 后添加不同的额外十六进制位，如第一个集群使用 `BC:24:11:0`，第二个使用 `BC:24:11:1`，依此类推。\n 也可以在逻辑上分隔客户机网络，例如使用 VLAN。\n\n对于可公开访问的客户机，建议向 IEEE 注册自己的 https://standards.ieee.org/products-programs/regauth/[OUI]，或与您自身或托管服务提供商的网络管理员协调。"
    },
    "max_workers": {
      "description": "定义执行 'stopall VMs' 等操作或 HA 管理器任务时，每个节点最多启动的工作任务数  。", "minimum": 1, "optional": 1, "type": "integer"
    },
    "migration": {
      "description": "用于集群范围的迁移设置。",
      "format": {
        "network": {
          "description": "用于迁移的（子）网络的 CIDR。如果未设置复制网络设置，则复制任务将以此作为后备值", "format": "CIDR", "format_description": "CIDR",
          "optional": 1, "type": "string"
        },
        "type": {
          "default": "secure", "default_key": 1, "description": "迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": ["secure", "insecure"], "type": "string"
        }
      },
      "optional": 1, "type": "string"
    },
    "migration_unsecure": {
      "description": "默认使用 SSH 隧道保障迁移安全。在安全的私有网络上，可禁用此功能以加快迁移。已弃用，请改用 'migration' 属性！", "optional": 1,
      "type": "boolean"
    },
    "next-id": {
      "description": "控制空闲 VMID 自动选择池的范围。",
      "format": {
        "lower": {"default": 100, "description": "空闲 next-id API 范围的下限，包含此值。", "max": 999999999, "min": 100, "optional": 1, "type": "integer"},
        "upper": {
          "default": 1000000, "description": "空闲 next-id API 范围的上限，不包含此值。", "max": 1000000000, "min": 100, "optional": 1, "type": "integer"
        }
      },
      "optional": 1, "type": "string"
    },
    "notify": {
      "description": "集群范围的通知设置。",
      "format": {
        "fencing": {"description": "未使用——请改用数据中心通知设置。", "enum": ["always", "never"], "optional": 1, "type": "string"},
        "package-updates": {
          "default": "auto", "description": "已弃用：请改用数据中心通知设置。控制每日更新作业何时发送通知。", "enum": ["auto", "always", "never"],
          "optional": 1, "type": "string",
          "verbose_description": "已弃用：请改用数据中心通知设置。\n控制每日更新作业发送通知的频率：\n* 'auto' 对具有有效订阅的系统每天发送，因为假定这些系统已  用于生产环境，因此应了解待处理更新。\n* 'always' 如果有新的待处理更新，则每次更新都发送。\n* 'never' 从不发送新待处理更新的通知。\n"
        },
        "replication": {"description": "未使用——请改用数据中心通知设置。", "enum": ["always", "never"], "optional": 1, "type": "string"},
        "target-fencing": {"description": "未使用——请改用数据中心通知设置。", "format_description": "TARGET", "optional": 1, "type": "string"},
        "target-package-updates": {"description": "未使用——请改用数据中心通知设置。", "format_description": "TARGET", "optional": 1, "type": "string"},
        "target-replication": {"description": "未使用——请改用数据中心通知设置。", "format_description": "TARGET", "optional": 1, "type": "string"}
      },
      "optional": 1, "type": "string"
    },
    "registered-tags": {
      "description": "设置和删除时需要对 '/' 具有 `Sys.Modify` 权限的标签列表。此处设置且同时位于 'user-tag-access' 中的标签也需要 `Sys.Modify`。",
      "optional": 1, "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*);)*(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)", "type": "string", "typetext": "<tag>[;<tag>...]"
    },
    "replication": {
      "description": "用于集群范围的复制设置。",
      "format": {
        "network": {"description": "用于复制任务的（子）网络的 CIDR。", "format": "CIDR", "format_description": "CIDR", "optional": 1, "type": "string"},
        "type": {
          "default": "secure", "default_key": 1, "description": "复制流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": ["secure", "insecure"], "type": "string"
        }
      },
      "optional": 1, "type": "string"
    },
    "tag-style": {
      "description": "标签样式选项。",
      "format": {
        "case-sensitive": {"default": 0, "description": "控制更新时筛选唯一标签是否区分大小写。", "optional": 1, "type": "boolean"},
        "color-map": {
          "description": "手动标签颜色映射（以分号分隔）。", "optional": 1,
          "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?)(?:;(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?))*",
          "type": "string", "typetext": "<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]"
        },
        "ordering": {
          "default": "alphabetical", "description": "控制 Web 界面和 API 更新中的标签排序。", "enum": ["config", "alphabetical"], "optional": 1,
          "type": "string"
        },
        "shape": {
          "default": "circle",
          "description": "Web UI 树中的标签形状。'full' 绘制完整标签。'circle' 仅绘制带背景色的圆形。'dense' 仅绘制小矩形（适用于每个客户机分配了大量标签的情况）。'none' 禁止显示标签。",
          "enum": ["full", "circle", "dense", "none"], "optional": 1, "type": "string"
        }
      },
      "optional": 1, "type": "string"
    },
    "u2f": {
      "description": "u2f",
      "format": {
        "appid": {"description": "覆盖 U2F AppId URL。默认为源站。", "format_description": "APPID", "optional": 1, "type": "string"},
        "origin": {"description": "覆盖 U2F Origin。主要适用于只有一个 URL 的单节点。", "format_description": "URL", "optional": 1, "type": "string"}
      },
      "optional": 1, "type": "string"
    },
    "user-tag-access": {
      "description": "用户可设置标签的权限选项",
      "format": {
        "user-allow": {
          "default": "free",
          "description": "控制没有 `Sys.Modify` 权限（作用于 `/`）的用户的标签使用方式，允许 `none`、`list`、已 `existing` 或任意标签（`free`）。",
          "enum": ["none", "list", "existing", "free"], "optional": 1, "type": "string",
          "verbose_description": "控制用户可在其控制的资源（例如客户机）上设置或删除哪些标签。具有 `Sys.Modify` 权限（作用于 `/`）的用户始终不受限制。\n* 'none' 不可使用任何标签。\n* 'list' 可使用 'user-allow-list' 中的标签。\n* 'existing' 与 list 相同，但也可使用资源上已有的标签。\n* 'free' 无标签限制。\n"
        },
        "user-allow-list": {
          "description": "当 'user-allow' 为 'list' 和 'existing' 时，用户允许设置和删除的标签列表（以分号分隔）。", "optional": 1,
          "pattern": "(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)(?:;(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*))*", "type": "string", "typetext": "<tag>[;<tag>...]"
        }
      },
      "optional": 1, "type": "string"
    },
    "webauthn": {
      "description": "webauthn 配置",
      "format": {
        "allow-subdomains": {"default": 1, "description": "是否允许源站为子域，而不必是完全相同的 URL。", "optional": 1, "type": "boolean"},
        "id": {
          "description": "依赖方 ID。必须为不含协议、端口或路径的域名。更改此项必定导致现有凭据失效。", "format_description": "DOMAINNAME", "optional": 1,
          "type": "string"
        },
        "origin": {
          "description": "站点源站。必须为 `https://` URL（或 `http://localhost`）。应包含用户在浏览器中访问 Web 界面时输入的地址。更改此项可能导致现有凭据失效。",
          "format_description": "URL", "optional": 1, "type": "string"
        },
        "rp": {
          "description": "依赖方名称。任意文本标识符。更改此项可能导致现有凭据失效。", "format_description": "RELYING_PARTY", "optional": 1, "type": "string"
        }
      },
      "optional": 1, "type": "string"
    }
  },
  "type": "object"
}
```

### PUT `/cluster/options` <a href="#api-cluster-options-096be758-put" id="api-cluster-options-096be758-put"></a>

设置数据中心选项。

**方法标识：** `set_options`

**权限**

```text
{"check": ["perm", "/", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-options-096be758-put-parameters" id="api-cluster-options-096be758-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `bwlimit` | 类型：string；必填：否；默认值：—<br>为各类操作设置 I/O 带宽限制（单位为 KiB/s）。 |
| `consent-text` | 类型：string；必填：否；默认值：—<br>登录前显示的同意文本。 |
| `console` | 类型：string；必填：否；默认值：—<br>选择默认控制台查看器。可以使用内置 java applet（VNC；已弃用，会映射到 html5）、与外部 virt-viewer 兼容的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如虚拟机未启用 SPICE），则回退到 noVNC。；可选值：`applet`, `vv`, `html5`, `xtermjs` |
| `crs` | 类型：string；必填：否；默认值：—<br>集群资源调度设置。 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `description` | 类型：string；必填：否；默认值：—<br>数据中心描述。显示在 Web 界面的数据中心备注面板中。作为注释保存在配置文件中。 |
| `email_from` | 类型：string；必填：否；默认值：—<br>指定发送通知所用的电子邮件发件地址（默认为 root@$hostname） |
| `fencing` | 类型：string；必填：否；默认值："watchdog"<br>设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中正确配置隔离设备。both 模式同时使用这两种模式。<br><br>警告：'hardware' 和 'both' 均为实验性功能，仍在开发中；可选值：`watchdog`, `hardware`, `both` |
| `ha` | 类型：string；必填：否；默认值：—<br>集群范围的 HA 设置。 |
| `http_proxy` | 类型：string；必填：否；默认值：—<br>指定用于下载的外部 HTTP 代理（例如：'http://username:password@host:port/') |
| `keyboard` | 类型：string；必填：否；默认值：—<br>VNC 服务器的默认键盘布局。；可选值：`de`, `de-ch`, `da`, `en-gb`, `en-us`, `es`, `fi`, `fr`, `fr-be`, `fr-ca`, `fr-ch`, `hu`, `is`, `it`, `ja`, `lt`, `mk`, `nl`, `no`, `pl`, `pt`, `pt-br`, `sv`, `sl`, `tr` |
| `language` | 类型：string；必填：否；默认值：—<br>默认 GUI 语言。；可选值：`ar`, `ca`, `da`, `de`, `en`, `es`, `eu`, `fa`, `fr`, `hr`, `he`, `it`, `ja`, `ka`, `kr`, `nb`, `nl`, `nn`, `pl`, `pt_BR`, `ru`, `sl`, `sv`, `tr`, `ukr`, `zh_CN`, `zh_TW` |
| `location` | 类型：string；必填：否；默认值：—<br>集群位置。 |
| `mac_prefix` | 类型：string；必填：否；默认值："BC:24:11"<br>虚拟客户机自动生成的 MAC 地址前缀。默认值 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），对应大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT/地址伪装后方）。<br> <br>请注意，当运行多个客户机网络部分或全部共享的集群时，强烈建议扩展默认 MAC 前缀，或生成自定义的有效前缀，以减少 MAC 冲突概率。例如，为每个集群在 Proxmox OUI 后添加不同的额外十六进制位，如第一个集群使用 `BC:24:11:0`，第二个使用 `BC:24:11:1`，依此类推。<br> 也可以在逻辑上分隔客户机网络，例如使用 VLAN。<br><br>对于可公开访问的客户机，建议向 IEEE 注册自己的 https://standards.ieee.org/products-programs/regauth/[OUI]，或与您自身或托管服务提供商的网络管理员协调。 |
| `max_workers` | 类型：integer；必填：否；默认值：—<br>定义执行 'stopall VMs' 等操作或 HA 管理器任务时，每个节点最多启动的工作任务数  。 |
| `migration` | 类型：string；必填：否；默认值：—<br>用于集群范围的迁移设置。 |
| `migration_unsecure` | 类型：boolean；必填：否；默认值：—<br>默认使用 SSH 隧道保障迁移安全。在安全的私有网络上，可禁用此功能以加快迁移。已弃用，请改用 'migration' 属性！ |
| `next-id` | 类型：string；必填：否；默认值：—<br>控制空闲 VMID 自动选择池的范围。 |
| `notify` | 类型：string；必填：否；默认值：—<br>集群范围的通知设置。 |
| `registered-tags` | 类型：string；必填：否；默认值：—<br>设置和删除时需要对 '/' 具有 `Sys.Modify` 权限的标签列表。此处设置且同时位于 'user-tag-access' 中的标签也需要 `Sys.Modify`。 |
| `replication` | 类型：string；必填：否；默认值：—<br>用于集群范围的复制设置。 |
| `tag-style` | 类型：string；必填：否；默认值：—<br>标签样式选项。 |
| `u2f` | 类型：string；必填：否；默认值：—<br>u2f |
| `user-tag-access` | 类型：string；必填：否；默认值：—<br>用户可设置标签的权限选项 |
| `webauthn` | 类型：string；必填：否；默认值：—<br>webauthn 配置 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {"description": "克隆磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "default": {"description": "默认带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "migration": {
          "description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1,
          "type": "number"
        },
        "move": {"description": "移动磁盘的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"},
        "restore": {"description": "从备份还原客户机的带宽限制，单位为 KiB/s", "format_description": "LIMIT", "minimum": "0", "optional": 1, "type": "number"}
      },
      "optional": 1, "type": "string", "typetext": "[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]"
    },
    "consent-text": {"description": "登录前显示的同意文本。", "maxLength": 65536, "optional": 1, "type": "string", "typetext": "<string>"},
    "console": {
      "description": "选择默认控制台查看器。可以使用内置 java applet（VNC；已弃用，会映射到 html5）、与外部 virt-viewer 兼容的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如虚拟机未启用 SPICE），则回退到 noVNC。",
      "enum": ["applet", "vv", "html5", "xtermjs"], "optional": 1, "type": "string"
    },
    "crs": {
      "description": "集群资源调度设置。",
      "format": {
        "ha": {
          "default": "basic", "description": "为 HA 使用此资源调度器模式。", "enum": ["basic", "static", "dynamic"], "optional": 1, "type": "string",
          "verbose_description": "配置 HA 管理器应如何选择节点以启动或恢复服务：\n\n- 'basic'：仅使用服务数量，\n- 'static'：考虑服务的静态 CPU 和内存配置，\n- 'dynamic'：考虑服务的静态和动态 CPU 及内存用量。\n"
        },
        "ha-auto-rebalance": {"default": 0, "description": "是否根据当前节点不均衡程度使用 CRS 自动均衡 HA 资源。", "optional": 1, "type": "boolean"},
        "ha-auto-rebalance-hold-duration": {
          "default": 3, "description": "集群节点不均衡程度必须连续超过阈值的 HA 轮次数，达到后触发自动资源均衡迁移。", "minimum": 0, "optional": 1,
          "requires": "ha-auto-rebalance", "type": "number"
        },
        "ha-auto-rebalance-margin": {
          "default": 10, "description": "执行资源均衡迁移所需的集群节点不均衡程度最小相对改善百分比。", "maximum": 100, "minimum": 0, "optional": 1,
          "requires": "ha-auto-rebalance", "type": "number"
        },
        "ha-auto-rebalance-method": {
          "default": "bruteforce", "description": "对均衡迁移进行评分所用的方法。", "enum": ["bruteforce", "topsis"], "optional": 1,
          "requires": "ha-auto-rebalance", "type": "string"
        },
        "ha-auto-rebalance-threshold": {
          "default": 30, "description": "集群节点不均衡百分比，超过此值将触发自动资源均衡系统。", "maximum": 100, "minimum": 0, "optional": 1,
          "requires": "ha-auto-rebalance", "type": "number"
        },
        "ha-rebalance-on-start": {
          "default": 0, "description": "设置为在 HA 服务请求状态从 stop 变为 start 时使用 CRS 选择合适节点。", "optional": 1, "type": "boolean"
        }
      },
      "optional": 1, "type": "string",
      "typetext": "[ha=<basic|static|dynamic>] [,ha-auto-rebalance=<1|0>] [,ha-auto-rebalance-hold-duration=<number>] [,ha-auto-rebalance-margin=<number>] [,ha-auto-rebalance-method=<bruteforce|topsis>] [,ha-auto-rebalance-threshold=<number>] [,ha-rebalance-on-start=<1|0>]"
    },
    "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "description": {
      "description": "数据中心描述。显示在 Web 界面的数据中心备注面板中。作为注释保存在配置文件中。", "maxLength": 65536, "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "email_from": {
      "description": "指定发送通知所用的电子邮件发件地址（默认为 root@$hostname）", "format": "email-opt", "optional": 1, "type": "string",
      "typetext": "<string>"
    },
    "fencing": {
      "default": "watchdog",
      "description": "设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中正确配置隔离设备。both 模式同时使用这两种模式。\n\n警告：'hardware' 和 'both' 均为实验性功能，仍在开发中",
      "enum": ["watchdog", "hardware", "both"], "optional": 1, "type": "string"
    },
    "ha": {
      "description": "集群范围的 HA 设置。",
      "format": {
        "shutdown_policy": {
          "default": "conditional",
          "description": "节点关闭时 HA 服务的策略。'freeze' 禁用自动恢复，'failover' 确保恢复，'conditional' 在关机时恢复、重启时冻结。'migrate' 在可能时将正在运行的服务迁移到其他节点。使用 'freeze' 或 'failover' 时，关闭节点始终会先停止 HA 服务。",
          "enum": ["freeze", "failover", "conditional", "migrate"], "type": "string",
          "verbose_description": "描述节点关机或重启时处理 HA 服务的策略。Freeze 总是冻结关闭时仍在该节点上的服务，这些服务不会由 HA 管理器恢复。Failover 不会将服务标记为冻结，因此如果关闭的节点未迅速恢复上线（< 1min），服务将恢复到其他节点。'conditional' 根据关闭类型自动选择，即重启时冻结服务，关机时保留服务状态，从而在约 2 分钟后恢复。Migrate 在触发重启或关机时尝试将所有正在运行的服务移至其他节点。只有当节点上不再存在运行中的服务时，关机过程才会继续。如果节点重新上线，服务将移回先前关闭的节点，前提是期间没有发生其他迁移、重新安置或恢复。"
        }
      },
      "optional": 1, "type": "string", "typetext": "shutdown_policy=<enum>"
    },
    "http_proxy": {
      "description": "指定用于下载的外部 HTTP 代理（例如：'http://username:password@host:port/')", "optional": 1, "pattern": "http://.*", "type": "string"
    },
    "keyboard": {
      "description": "VNC 服务器的默认键盘布局。",
      "enum": [
        "de", "de-ch", "da", "en-gb", "en-us", "es", "fi", "fr", "fr-be", "fr-ca", "fr-ch", "hu", "is", "it", "ja", "lt", "mk", "nl", "no", "pl", "pt", "pt-br",
        "sv", "sl", "tr"
      ],
      "optional": 1, "type": "string"
    },
    "language": {
      "description": "默认 GUI 语言。",
      "enum": [
        "ar", "ca", "da", "de", "en", "es", "eu", "fa", "fr", "hr", "he", "it", "ja", "ka", "kr", "nb", "nl", "nn", "pl", "pt_BR", "ru", "sl", "sv", "tr",
        "ukr", "zh_CN", "zh_TW"
      ],
      "optional": 1, "type": "string"
    },
    "location": {
      "description": "集群位置。", "format": "pve-node-location", "optional": 1, "type": "string",
      "typetext": "latitude=<number> ,longitude=<number> [,name=<name>]"
    },
    "mac_prefix": {
      "default": "BC:24:11",
      "description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 'BC:24:11' 是 IEEE 分配给 Proxmox Server Solutions GmbH 的 OUI，对应 24 位大型 MAC 地址块。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT 后方）。",
      "format": "mac-prefix", "optional": 1, "type": "string", "typetext": "<string>",
      "verbose_description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），对应大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT/地址伪装后方）。\n \n请注意，当运行多个客户机网络部分或全部共享的集群时，强烈建议扩展默认 MAC 前缀，或生成自定义的有效前缀，以减少 MAC 冲突概率。例如，为每个集群在 Proxmox OUI 后添加不同的额外十六进制位，如第一个集群使用 `BC:24:11:0`，第二个使用 `BC:24:11:1`，依此类推。\n 也可以在逻辑上分隔客户机网络，例如使用 VLAN。\n\n对于可公开访问的客户机，建议向 IEEE 注册自己的 https://standards.ieee.org/products-programs/regauth/[OUI]，或与您自身或托管服务提供商的网络管理员协调。"
    },
    "max_workers": {
      "description": "定义执行 'stopall VMs' 等操作或 HA 管理器任务时，每个节点最多启动的工作任务数  。", "minimum": 1, "optional": 1, "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "migration": {
      "description": "用于集群范围的迁移设置。",
      "format": {
        "network": {
          "description": "用于迁移的（子）网络的 CIDR。如果未设置复制网络设置，则复制任务将以此作为后备值", "format": "CIDR", "format_description": "CIDR",
          "optional": 1, "type": "string"
        },
        "type": {
          "default": "secure", "default_key": 1, "description": "迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": ["secure", "insecure"], "type": "string"
        }
      },
      "optional": 1, "type": "string", "typetext": "[type=]<secure|insecure> [,network=<CIDR>]"
    },
    "migration_unsecure": {
      "description": "默认使用 SSH 隧道保障迁移安全。在安全的私有网络上，可禁用此功能以加快迁移。已弃用，请改用 'migration' 属性！", "optional": 1,
      "type": "boolean", "typetext": "<boolean>"
    },
    "next-id": {
      "description": "控制空闲 VMID 自动选择池的范围。",
      "format": {
        "lower": {"default": 100, "description": "空闲 next-id API 范围的下限，包含此值。", "max": 999999999, "min": 100, "optional": 1, "type": "integer"},
        "upper": {
          "default": 1000000, "description": "空闲 next-id API 范围的上限，不包含此值。", "max": 1000000000, "min": 100, "optional": 1, "type": "integer"
        }
      },
      "optional": 1, "type": "string", "typetext": "[lower=<integer>] [,upper=<integer>]"
    },
    "notify": {
      "description": "集群范围的通知设置。",
      "format": {
        "fencing": {"description": "未使用——请改用数据中心通知设置。", "enum": ["always", "never"], "optional": 1, "type": "string"},
        "package-updates": {
          "default": "auto", "description": "已弃用：请改用数据中心通知设置。控制每日更新作业何时发送通知。", "enum": ["auto", "always", "never"],
          "optional": 1, "type": "string",
          "verbose_description": "已弃用：请改用数据中心通知设置。\n控制每日更新作业发送通知的频率：\n* 'auto' 对具有有效订阅的系统每天发送，因为假定这些系统已  用于生产环境，因此应了解待处理更新。\n* 'always' 如果有新的待处理更新，则每次更新都发送。\n* 'never' 从不发送新待处理更新的通知。\n"
        },
        "replication": {"description": "未使用——请改用数据中心通知设置。", "enum": ["always", "never"], "optional": 1, "type": "string"},
        "target-fencing": {"description": "未使用——请改用数据中心通知设置。", "format_description": "TARGET", "optional": 1, "type": "string"},
        "target-package-updates": {"description": "未使用——请改用数据中心通知设置。", "format_description": "TARGET", "optional": 1, "type": "string"},
        "target-replication": {"description": "未使用——请改用数据中心通知设置。", "format_description": "TARGET", "optional": 1, "type": "string"}
      },
      "optional": 1, "type": "string",
      "typetext": "[fencing=<always|never>] [,package-updates=<auto|always|never>] [,replication=<always|never>] [,target-fencing=<TARGET>] [,target-package-updates=<TARGET>] [,target-replication=<TARGET>]"
    },
    "registered-tags": {
      "description": "设置和删除时需要对 '/' 具有 `Sys.Modify` 权限的标签列表。此处设置且同时位于 'user-tag-access' 中的标签也需要 `Sys.Modify`。",
      "optional": 1, "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*);)*(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)", "type": "string", "typetext": "<tag>[;<tag>...]"
    },
    "replication": {
      "description": "用于集群范围的复制设置。",
      "format": {
        "network": {"description": "用于复制任务的（子）网络的 CIDR。", "format": "CIDR", "format_description": "CIDR", "optional": 1, "type": "string"},
        "type": {
          "default": "secure", "default_key": 1, "description": "复制流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": ["secure", "insecure"], "type": "string"
        }
      },
      "optional": 1, "type": "string", "typetext": "[type=]<secure|insecure> [,network=<CIDR>]"
    },
    "tag-style": {
      "description": "标签样式选项。",
      "format": {
        "case-sensitive": {"default": 0, "description": "控制更新时筛选唯一标签是否区分大小写。", "optional": 1, "type": "boolean"},
        "color-map": {
          "description": "手动标签颜色映射（以分号分隔）。", "optional": 1,
          "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?)(?:;(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?))*",
          "type": "string", "typetext": "<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]"
        },
        "ordering": {
          "default": "alphabetical", "description": "控制 Web 界面和 API 更新中的标签排序。", "enum": ["config", "alphabetical"], "optional": 1,
          "type": "string"
        },
        "shape": {
          "default": "circle",
          "description": "Web UI 树中的标签形状。'full' 绘制完整标签。'circle' 仅绘制带背景色的圆形。'dense' 仅绘制小矩形（适用于每个客户机分配了大量标签的情况）。'none' 禁止显示标签。",
          "enum": ["full", "circle", "dense", "none"], "optional": 1, "type": "string"
        }
      },
      "optional": 1, "type": "string",
      "typetext": "[case-sensitive=<1|0>] [,color-map=<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]] [,ordering=<config|alphabetical>] [,shape=<enum>]"
    },
    "u2f": {
      "description": "u2f",
      "format": {
        "appid": {"description": "覆盖 U2F AppId URL。默认为源站。", "format_description": "APPID", "optional": 1, "type": "string"},
        "origin": {"description": "覆盖 U2F Origin。主要适用于只有一个 URL 的单节点。", "format_description": "URL", "optional": 1, "type": "string"}
      },
      "optional": 1, "type": "string", "typetext": "[appid=<APPID>] [,origin=<URL>]"
    },
    "user-tag-access": {
      "description": "用户可设置标签的权限选项",
      "format": {
        "user-allow": {
          "default": "free",
          "description": "控制没有 `Sys.Modify` 权限（作用于 `/`）的用户的标签使用方式，允许 `none`、`list`、已 `existing` 或任意标签（`free`）。",
          "enum": ["none", "list", "existing", "free"], "optional": 1, "type": "string",
          "verbose_description": "控制用户可在其控制的资源（例如客户机）上设置或删除哪些标签。具有 `Sys.Modify` 权限（作用于 `/`）的用户始终不受限制。\n* 'none' 不可使用任何标签。\n* 'list' 可使用 'user-allow-list' 中的标签。\n* 'existing' 与 list 相同，但也可使用资源上已有的标签。\n* 'free' 无标签限制。\n"
        },
        "user-allow-list": {
          "description": "当 'user-allow' 为 'list' 和 'existing' 时，用户允许设置和删除的标签列表（以分号分隔）。", "optional": 1,
          "pattern": "(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)(?:;(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*))*", "type": "string", "typetext": "<tag>[;<tag>...]"
        }
      },
      "optional": 1, "type": "string", "typetext": "[user-allow=<enum>] [,user-allow-list=<tag>[;<tag>...]]"
    },
    "webauthn": {
      "description": "webauthn 配置",
      "format": {
        "allow-subdomains": {"default": 1, "description": "是否允许源站为子域，而不必是完全相同的 URL。", "optional": 1, "type": "boolean"},
        "id": {
          "description": "依赖方 ID。必须为不含协议、端口或路径的域名。更改此项必定导致现有凭据失效。", "format_description": "DOMAINNAME", "optional": 1,
          "type": "string"
        },
        "origin": {
          "description": "站点源站。必须为 `https://` URL（或 `http://localhost`）。应包含用户在浏览器中访问 Web 界面时输入的地址。更改此项可能导致现有凭据失效。",
          "format_description": "URL", "optional": 1, "type": "string"
        },
        "rp": {
          "description": "依赖方名称。任意文本标识符。更改此项可能导致现有凭据失效。", "format_description": "RELYING_PARTY", "optional": 1, "type": "string"
        }
      },
      "optional": 1, "type": "string", "typetext": "[allow-subdomains=<1|0>] [,id=<DOMAINNAME>] [,origin=<URL>] [,rp=<RELYING_PARTY>]"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-options-096be758-put-returns" id="api-cluster-options-096be758-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/options)。

## `/cluster/status` <a href="#api-cluster-status-46dab962" id="api-cluster-status-46dab962"></a>

原始接口路径：`/cluster/status`。

### GET `/cluster/status` <a href="#api-cluster-status-46dab962-get" id="api-cluster-status-46dab962-get"></a>

获取集群状态信息。

**方法标识：** `get_status`

**权限**

```text
{"check": ["perm", "/", ["Sys.Audit"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-cluster-status-46dab962-get-parameters" id="api-cluster-status-46dab962-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-cluster-status-46dab962-get-returns" id="api-cluster-status-46dab962-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "id": {"type": "string"}, "ip": {"description": "[node] 解析节点名称得到的 IP 地址。", "optional": 1, "type": "string"},
      "level": {
        "description": "[node] Proxmox VE 订阅级别，表明是否有资格获得企业支持及访问稳定的 Proxmox VE Enterprise Repository。", "optional": 1, "type": "string"
      },
      "local": {"description": "[node] 表明是否为作出响应的节点。", "optional": 1, "type": "boolean"}, "name": {"type": "string"},
      "nodeid": {"description": "[node] corosync 配置中的节点 ID。", "optional": 1, "type": "integer"},
      "nodes": {"description": "[cluster] 节点数量，包括离线节点。", "optional": 1, "type": "integer"},
      "online": {"description": "[node] 表明节点在线还是离线。", "optional": 1, "type": "boolean"},
      "quorate": {"description": "[cluster] 表明是否有多数节点在线以进行决策", "optional": 1, "type": "boolean"},
      "type": {
        "description": "表明类型，为 cluster 或 node。类型定义对象属性，例如 quorate 适用于 cluster 类型。", "enum": ["cluster", "node"], "type": "string"
      },
      "version": {"description": "[cluster] corosync 配置文件的当前版本。", "optional": 1, "type": "integer"}
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/status)。

## `/cluster/nextid` <a href="#api-cluster-nextid-f730d537" id="api-cluster-nextid-f730d537"></a>

原始接口路径：`/cluster/nextid`。

### GET `/cluster/nextid` <a href="#api-cluster-nextid-f730d537-get" id="api-cluster-nextid-f730d537-get"></a>

获取下一个空闲 VMID。传入 VMID 可确认其是否空闲（以检查时为准）。

**方法标识：** `nextid`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-cluster-nextid-f730d537-get-parameters" id="api-cluster-nextid-f730d537-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `vmid` | 类型：integer；必填：否；默认值：—<br>虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "vmid": {
      "description": "虚拟机的（唯一）ID。", "format": "pve-vmid", "maximum": 999999999, "minimum": 100, "optional": 1, "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

#### 返回值 <a href="#api-cluster-nextid-f730d537-get-returns" id="api-cluster-nextid-f730d537-get-returns"></a>

```text
{"description": "下一个空闲 VMID。", "type": "integer"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/nextid)。
