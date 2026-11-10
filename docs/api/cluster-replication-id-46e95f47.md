# `/cluster/replication/{id}`

原始接口路径：`/cluster/replication/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/replication/{id}`

Mark replication job for removal.

**方法标识：** `delete`

**权限**

```json
{
  "description": "Requires the VM.Replicate permission on /vms/<vmid>.",
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
| `force` | boolean | 否 | 0 | Will remove the jobconfig entry, but will not cleanup. |
| `id` | string | 是 | — | Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '&lt;GUEST&gt;-&lt;JOBNUM&gt;'. |
| `keep` | boolean | 否 | 0 | Keep replicated data at target (do not remove). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "default": 0,
      "description": "Will remove the jobconfig entry, but will not cleanup.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'.",
      "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
      "type": "string"
    },
    "keep": {
      "default": 0,
      "description": "Keep replicated data at target (do not remove).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## GET `/cluster/replication/{id}`

Read replication job configuration.

**方法标识：** `read`

**权限**

```json
{
  "description": "Requires the VM.Audit permission on /vms/<vmid>.",
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
| `id` | string | 是 | — | Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '&lt;GUEST&gt;-&lt;JOBNUM&gt;'. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'.",
      "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "comment": {
      "description": "Description.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "disable": {
      "description": "Flag to disable/deactivate the entry.",
      "optional": 1,
      "type": "boolean"
    },
    "guest": {
      "description": "Guest ID.",
      "type": "integer"
    },
    "id": {
      "description": "Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'.",
      "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
      "type": "string"
    },
    "jobnum": {
      "description": "Unique, sequential ID assigned to each job.",
      "type": "integer"
    },
    "rate": {
      "description": "Rate limit in mbps (megabytes per second) as floating point number.",
      "minimum": 1,
      "optional": 1,
      "type": "number"
    },
    "remove_job": {
      "description": "Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file.",
      "enum": [
        "local",
        "full"
      ],
      "optional": 1,
      "type": "string"
    },
    "schedule": {
      "default": "*/15",
      "description": "Storage replication schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string"
    },
    "source": {
      "description": "For internal use, to detect if the guest was stolen.",
      "format": "pve-node",
      "optional": 1,
      "type": "string"
    },
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "optional": 0,
      "type": "string"
    },
    "type": {
      "description": "Section type.",
      "enum": [
        "local"
      ],
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/replication/{id}`

Update replication job configuration.

**方法标识：** `update`

**权限**

```json
{
  "description": "Requires the VM.Replicate permission on /vms/<vmid>.",
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
| `comment` | string | 否 | — | Description. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable` | boolean | 否 | — | Flag to disable/deactivate the entry. |
| `id` | string | 是 | — | Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '&lt;GUEST&gt;-&lt;JOBNUM&gt;'. |
| `rate` | number | 否 | — | Rate limit in mbps (megabytes per second) as floating point number. |
| `remove_job` | string | 否 | — | Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file.；可选值：`local`, `full` |
| `schedule` | string | 否 | "*/15" | Storage replication schedule. The format is a subset of `systemd` calendar events. |
| `source` | string | 否 | — | For internal use, to detect if the guest was stolen. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "Description.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "Flag to disable/deactivate the entry.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'.",
      "format": "pve-replication-job-id",
      "pattern": "[1-9][0-9]{2,8}-\\d{1,9}",
      "type": "string"
    },
    "rate": {
      "description": "Rate limit in mbps (megabytes per second) as floating point number.",
      "minimum": 1,
      "optional": 1,
      "type": "number",
      "typetext": "<number> (1 - N)"
    },
    "remove_job": {
      "description": "Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file.",
      "enum": [
        "local",
        "full"
      ],
      "optional": 1,
      "type": "string"
    },
    "schedule": {
      "default": "*/15",
      "description": "Storage replication schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "source": {
      "description": "For internal use, to detect if the guest was stolen.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/replication/{id})。
