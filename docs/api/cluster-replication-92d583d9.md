# `/cluster/replication`

原始接口路径：`/cluster/replication`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/replication`

List replication jobs.

**方法标识：** `index`

**权限**

```json
{
  "description": "Will only return replication jobs for which the calling user has VM.Audit permission on /vms/<vmid>.",
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
        "description": "Description.",
        "maxLength": 4096,
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

Create a new replication job

**方法标识：** `create`

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
| `disable` | boolean | 否 | — | Flag to disable/deactivate the entry. |
| `id` | string | 是 | — | Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '&lt;GUEST&gt;-&lt;JOBNUM&gt;'. |
| `rate` | number | 否 | — | Rate limit in mbps (megabytes per second) as floating point number. |
| `remove_job` | string | 否 | — | Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file.；可选值：`local`, `full` |
| `schedule` | string | 否 | "*/15" | Storage replication schedule. The format is a subset of `systemd` calendar events. |
| `source` | string | 否 | — | For internal use, to detect if the guest was stolen. |
| `target` | string | 是 | — | Target node. |
| `type` | string | 是 | — | Section type.；可选值：`local` |

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
    },
    "target": {
      "description": "Target node.",
      "format": "pve-node",
      "optional": 0,
      "type": "string",
      "typetext": "<string>"
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

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/replication)。
