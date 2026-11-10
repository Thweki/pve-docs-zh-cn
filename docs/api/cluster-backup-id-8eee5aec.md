# `/cluster/backup/{id}`

原始接口路径：`/cluster/backup/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/backup/{id}`

Delete vzdump backup job definition.

**方法标识：** `delete_job`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
  ]
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
| `id` | string | 是 | — | The job ID. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "The job ID.",
      "maxLength": 50,
      "pattern": "\\S+",
      "type": "string"
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

## GET `/cluster/backup/{id}`

Read vzdump backup job definition.

**方法标识：** `read_job`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | — | The job ID. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "The job ID.",
      "maxLength": 50,
      "pattern": "\\S+",
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
    "all": {
      "default": 0,
      "description": "Backup all known guest systems on this host.",
      "optional": 1,
      "type": "boolean"
    },
    "bwlimit": {
      "default": 0,
      "description": "Limit I/O bandwidth (in KiB/s).",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "comment": {
      "description": "Description for the Job.",
      "maxLength": 512,
      "optional": 1,
      "type": "string"
    },
    "compress": {
      "default": "0",
      "description": "Compress dump file.",
      "enum": [
        "0",
        "1",
        "gzip",
        "lzo",
        "zstd"
      ],
      "optional": 1,
      "type": "string"
    },
    "dumpdir": {
      "description": "Store resulting files to specified directory.",
      "optional": 1,
      "type": "string"
    },
    "enabled": {
      "default": "1",
      "description": "Enable or disable the job.",
      "optional": 1,
      "type": "boolean"
    },
    "exclude": {
      "description": "Exclude specified guest systems (assumes --all)",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string"
    },
    "exclude-path": {
      "description": "Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root, other paths match relative to each subdirectory.",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "fleecing": {
      "description": "Options for backup fleecing (VM only).",
      "optional": 1,
      "properties": {
        "enabled": {
          "default": 0,
          "default_key": 1,
          "description": "Enable backup fleecing. Cache backup data from blocks where new guest writes happen on specified storage instead of copying them directly to the backup target. This can help guest IO performance and even prevent hangs, at the cost of requiring more storage space.",
          "optional": 1,
          "type": "boolean"
        },
        "storage": {
          "description": "Use this storage to storage fleecing images. For efficient space usage, it's best to use a local storage that supports discard and either thin provisioning or sparse files.",
          "format": "pve-storage-id",
          "format_description": "storage ID",
          "optional": 1,
          "type": "string"
        }
      },
      "type": "object"
    },
    "id": {
      "description": "The job ID.",
      "maxLength": 50,
      "pattern": "\\S+",
      "type": "string"
    },
    "ionice": {
      "default": 7,
      "description": "Set IO priority when using the BFQ scheduler. For snapshot and suspend mode backups of VMs, this only affects the compressor. A value of 8 means the idle priority is used, otherwise the best-effort priority is used with the specified value.",
      "maximum": 8,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "lockwait": {
      "default": 180,
      "description": "Maximal time to wait for the global lock (minutes).",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "mailnotification": {
      "default": "always",
      "description": "Deprecated: use notification targets/matchers instead. Specify when to send a notification mail",
      "enum": [
        "always",
        "failure"
      ],
      "optional": 1,
      "type": "string"
    },
    "mailto": {
      "description": "Deprecated: Use notification targets/matchers instead. Comma-separated list of email addresses or users that should receive email notifications.",
      "format": "email-or-username-list",
      "optional": 1,
      "type": "string"
    },
    "mode": {
      "default": "snapshot",
      "description": "Backup mode.",
      "enum": [
        "snapshot",
        "suspend",
        "stop"
      ],
      "optional": 1,
      "type": "string"
    },
    "next-run": {
      "description": "UNIX timestamp when this backup job will be executed next",
      "optional": 1,
      "type": "integer"
    },
    "node": {
      "description": "Only run if executed on this node.",
      "format": "pve-node",
      "optional": 1,
      "type": "string"
    },
    "notes-template": {
      "description": "Template string for generating notes for the backup(s). It can contain variables which will be replaced by their values. Currently supported are {{cluster}}, {{guestname}}, {{node}}, and {{vmid}}, but more might be added in the future. Needs to be a single line, newline and backslash need to be escaped as '\\n' and '\\\\' respectively.",
      "maxLength": 1024,
      "optional": 1,
      "requires": "storage",
      "type": "string"
    },
    "notification-mode": {
      "default": "auto",
      "description": "Determine which notification system to use. If set to 'legacy-sendmail', vzdump will consider the mailto/mailnotification parameters and send emails to the specified address(es) via the 'sendmail' command. If set to 'notification-system', a notification will be sent via PVE's notification system, and the mailto and mailnotification will be ignored. If set to 'auto' (default setting), an email will be sent if mailto is set, and the notification system will be used if not.",
      "enum": [
        "auto",
        "legacy-sendmail",
        "notification-system"
      ],
      "optional": 1,
      "type": "string"
    },
    "pbs-change-detection-mode": {
      "description": "PBS mode used to detect file changes and switch encoding format for container backups.",
      "enum": [
        "legacy",
        "data",
        "metadata"
      ],
      "optional": 1,
      "type": "string"
    },
    "performance": {
      "description": "Other performance-related settings.",
      "optional": 1,
      "properties": {
        "max-workers": {
          "default": 16,
          "description": "Applies to VMs. Allow up to this many IO workers at the same time.",
          "maximum": 256,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "pbs-entries-max": {
          "default": 1048576,
          "description": "Applies to container backups sent to PBS. Limits the number of entries allowed in memory at a given time to avoid unintended OOM situations. Increase it to enable backups of containers with a large amount of files.",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "pigz": {
      "default": 0,
      "description": "Use pigz instead of gzip when N>0. N=1 uses half of cores, N>1 uses N as thread count.",
      "optional": 1,
      "type": "integer"
    },
    "pool": {
      "description": "Backup all known guest systems included in the specified pool.",
      "optional": 1,
      "type": "string"
    },
    "protected": {
      "description": "If true, mark backup(s) as protected.",
      "optional": 1,
      "requires": "storage",
      "type": "boolean"
    },
    "prune-backups": {
      "description": "Use these retention options instead of those from the storage configuration.",
      "optional": 1,
      "properties": {
        "keep-all": {
          "description": "Keep all backups. Conflicts with the other options when true.",
          "optional": 1,
          "type": "boolean"
        },
        "keep-daily": {
          "description": "Keep backups for the last <N> different days. If there is morethan one backup for a single day, only the latest one is kept.",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-hourly": {
          "description": "Keep backups for the last <N> different hours. If there is morethan one backup for a single hour, only the latest one is kept.",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-last": {
          "description": "Keep the last <N> backups.",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-monthly": {
          "description": "Keep backups for the last <N> different months. If there is morethan one backup for a single month, only the latest one is kept.",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-weekly": {
          "description": "Keep backups for the last <N> different weeks. If there is morethan one backup for a single week, only the latest one is kept.",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-yearly": {
          "description": "Keep backups for the last <N> different years. If there is morethan one backup for a single year, only the latest one is kept.",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "quiet": {
      "default": 0,
      "description": "Be quiet.",
      "optional": 1,
      "type": "boolean"
    },
    "remove": {
      "default": 1,
      "description": "Prune older backups according to 'prune-backups'.",
      "optional": 1,
      "type": "boolean"
    },
    "repeat-missed": {
      "default": 0,
      "description": "If true, the job will be run as soon as possible if it was missed while the scheduler was not running.",
      "optional": 1,
      "type": "boolean"
    },
    "schedule": {
      "description": "Backup schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string"
    },
    "script": {
      "description": "Use specified hook script.",
      "optional": 1,
      "type": "string"
    },
    "stdexcludes": {
      "default": 1,
      "description": "Exclude temporary files and logs.",
      "optional": 1,
      "type": "boolean"
    },
    "stop": {
      "default": 0,
      "description": "Stop running backup jobs on this host.",
      "optional": 1,
      "type": "boolean"
    },
    "stopwait": {
      "default": 10,
      "description": "Maximal time to wait until a guest system is stopped (minutes).",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "storage": {
      "description": "Store resulting file to this storage.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string"
    },
    "tmpdir": {
      "description": "Store temporary files to specified directory.",
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "The ID of the guest system you want to backup.",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string"
    },
    "zstd": {
      "default": 1,
      "description": "Zstd threads. N=0 uses half of the available cores, if N is set to a value bigger than 0, N is used as thread count.",
      "optional": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/backup/{id}`

Update vzdump backup job definition.

**方法标识：** `update_job`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Modify"
    ]
  ],
  "description": "The 'tmpdir', 'dumpdir' and 'script' parameters are additionally restricted to the 'root@pam' user."
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
| `all` | boolean | 否 | 0 | Backup all known guest systems on this host. |
| `bwlimit` | integer | 否 | 0 | Limit I/O bandwidth (in KiB/s). |
| `comment` | string | 否 | — | Description for the Job. |
| `compress` | string | 否 | "0" | Compress dump file.；可选值：`0`, `1`, `gzip`, `lzo`, `zstd` |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `dow` | string | 否 | — | Deprecated: Use 'schedule' instead. Day of week selection. 'starttime' and 'dow' will be converted into 'schedule' if used. |
| `dumpdir` | string | 否 | — | Store resulting files to specified directory. |
| `enabled` | boolean | 否 | "1" | Enable or disable the job. |
| `exclude` | string | 否 | — | Exclude specified guest systems (assumes --all) |
| `exclude-path` | array | 否 | — | Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root, other paths match relative to each subdirectory. |
| `fleecing` | string | 否 | — | Options for backup fleecing (VM only). |
| `id` | string | 是 | — | The job ID. |
| `ionice` | integer | 否 | 7 | Set IO priority when using the BFQ scheduler. For snapshot and suspend mode backups of VMs, this only affects the compressor. A value of 8 means the idle priority is used, otherwise the best-effort priority is used with the specified value. |
| `lockwait` | integer | 否 | 180 | Maximal time to wait for the global lock (minutes). |
| `mailnotification` | string | 否 | "always" | Deprecated: use notification targets/matchers instead. Specify when to send a notification mail；可选值：`always`, `failure` |
| `mailto` | string | 否 | — | Deprecated: Use notification targets/matchers instead. Comma-separated list of email addresses or users that should receive email notifications. |
| `mode` | string | 否 | "snapshot" | Backup mode.；可选值：`snapshot`, `suspend`, `stop` |
| `node` | string | 否 | — | Only run if executed on this node. |
| `notes-template` | string | 否 | — | Template string for generating notes for the backup(s). It can contain variables which will be replaced by their values. Currently supported are {{cluster}}, {{guestname}}, {{node}}, and {{vmid}}, but more might be added in the future. Needs to be a single line, newline and backslash need to be escaped as '\n' and '\\' respectively. |
| `notification-mode` | string | 否 | "auto" | Determine which notification system to use. If set to 'legacy-sendmail', vzdump will consider the mailto/mailnotification parameters and send emails to the specified address(es) via the 'sendmail' command. If set to 'notification-system', a notification will be sent via PVE's notification system, and the mailto and mailnotification will be ignored. If set to 'auto' (default setting), an email will be sent if mailto is set, and the notification system will be used if not.；可选值：`auto`, `legacy-sendmail`, `notification-system` |
| `pbs-change-detection-mode` | string | 否 | — | PBS mode used to detect file changes and switch encoding format for container backups.；可选值：`legacy`, `data`, `metadata` |
| `performance` | string | 否 | — | Other performance-related settings. |
| `pigz` | integer | 否 | 0 | Use pigz instead of gzip when N&gt;0. N=1 uses half of cores, N&gt;1 uses N as thread count. |
| `pool` | string | 否 | — | Backup all known guest systems included in the specified pool. |
| `protected` | boolean | 否 | — | If true, mark backup(s) as protected. |
| `prune-backups` | string | 否 | "keep-all=1" | Use these retention options instead of those from the storage configuration. |
| `quiet` | boolean | 否 | 0 | Be quiet. |
| `remove` | boolean | 否 | 1 | Prune older backups according to 'prune-backups'. |
| `repeat-missed` | boolean | 否 | 0 | If true, the job will be run as soon as possible if it was missed while the scheduler was not running. |
| `schedule` | string | 否 | — | Backup schedule. The format is a subset of `systemd` calendar events. |
| `script` | string | 否 | — | Use specified hook script. |
| `starttime` | string | 否 | — | Deprecated: Use 'schedule' instead. Job Start time. 'starttime' and 'dow' will be converted into 'schedule' if used. |
| `stdexcludes` | boolean | 否 | 1 | Exclude temporary files and logs. |
| `stop` | boolean | 否 | 0 | Stop running backup jobs on this host. |
| `stopwait` | integer | 否 | 10 | Maximal time to wait until a guest system is stopped (minutes). |
| `storage` | string | 否 | — | Store resulting file to this storage. |
| `tmpdir` | string | 否 | — | Store temporary files to specified directory. |
| `vmid` | string | 否 | — | The ID of the guest system you want to backup. |
| `zstd` | integer | 否 | 1 | Zstd threads. N=0 uses half of the available cores, if N is set to a value bigger than 0, N is used as thread count. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "all": {
      "default": 0,
      "description": "Backup all known guest systems on this host.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bwlimit": {
      "default": 0,
      "description": "Limit I/O bandwidth (in KiB/s).",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "comment": {
      "description": "Description for the Job.",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "compress": {
      "default": "0",
      "description": "Compress dump file.",
      "enum": [
        "0",
        "1",
        "gzip",
        "lzo",
        "zstd"
      ],
      "optional": 1,
      "type": "string"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dow": {
      "description": "Deprecated: Use 'schedule' instead. Day of week selection. 'starttime' and 'dow' will be converted into 'schedule' if used.",
      "format": "pve-day-of-week-list",
      "optional": 1,
      "requires": "starttime",
      "type": "string",
      "typetext": "<string>"
    },
    "dumpdir": {
      "description": "Store resulting files to specified directory.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enabled": {
      "default": "1",
      "description": "Enable or disable the job.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "exclude": {
      "description": "Exclude specified guest systems (assumes --all)",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "exclude-path": {
      "description": "Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root, other paths match relative to each subdirectory.",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "fleecing": {
      "description": "Options for backup fleecing (VM only).",
      "format": "backup-fleecing",
      "optional": 1,
      "type": "string",
      "typetext": "[[enabled=]<1|0>] [,storage=<storage ID>]"
    },
    "id": {
      "description": "The job ID.",
      "maxLength": 50,
      "pattern": "\\S+",
      "type": "string"
    },
    "ionice": {
      "default": 7,
      "description": "Set IO priority when using the BFQ scheduler. For snapshot and suspend mode backups of VMs, this only affects the compressor. A value of 8 means the idle priority is used, otherwise the best-effort priority is used with the specified value.",
      "maximum": 8,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 8)"
    },
    "lockwait": {
      "default": 180,
      "description": "Maximal time to wait for the global lock (minutes).",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "mailnotification": {
      "default": "always",
      "description": "Deprecated: use notification targets/matchers instead. Specify when to send a notification mail",
      "enum": [
        "always",
        "failure"
      ],
      "optional": 1,
      "type": "string"
    },
    "mailto": {
      "description": "Deprecated: Use notification targets/matchers instead. Comma-separated list of email addresses or users that should receive email notifications.",
      "format": "email-or-username-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mode": {
      "default": "snapshot",
      "description": "Backup mode.",
      "enum": [
        "snapshot",
        "suspend",
        "stop"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "Only run if executed on this node.",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "notes-template": {
      "description": "Template string for generating notes for the backup(s). It can contain variables which will be replaced by their values. Currently supported are {{cluster}}, {{guestname}}, {{node}}, and {{vmid}}, but more might be added in the future. Needs to be a single line, newline and backslash need to be escaped as '\\n' and '\\\\' respectively.",
      "maxLength": 1024,
      "optional": 1,
      "requires": "storage",
      "type": "string",
      "typetext": "<string>"
    },
    "notification-mode": {
      "default": "auto",
      "description": "Determine which notification system to use. If set to 'legacy-sendmail', vzdump will consider the mailto/mailnotification parameters and send emails to the specified address(es) via the 'sendmail' command. If set to 'notification-system', a notification will be sent via PVE's notification system, and the mailto and mailnotification will be ignored. If set to 'auto' (default setting), an email will be sent if mailto is set, and the notification system will be used if not.",
      "enum": [
        "auto",
        "legacy-sendmail",
        "notification-system"
      ],
      "optional": 1,
      "type": "string"
    },
    "pbs-change-detection-mode": {
      "description": "PBS mode used to detect file changes and switch encoding format for container backups.",
      "enum": [
        "legacy",
        "data",
        "metadata"
      ],
      "optional": 1,
      "type": "string"
    },
    "performance": {
      "description": "Other performance-related settings.",
      "format": "backup-performance",
      "optional": 1,
      "type": "string",
      "typetext": "[max-workers=<integer>] [,pbs-entries-max=<integer>]"
    },
    "pigz": {
      "default": 0,
      "description": "Use pigz instead of gzip when N>0. N=1 uses half of cores, N>1 uses N as thread count.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "pool": {
      "description": "Backup all known guest systems included in the specified pool.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "protected": {
      "description": "If true, mark backup(s) as protected.",
      "optional": 1,
      "requires": "storage",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "prune-backups": {
      "default": "keep-all=1",
      "description": "Use these retention options instead of those from the storage configuration.",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "quiet": {
      "default": 0,
      "description": "Be quiet.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "remove": {
      "default": 1,
      "description": "Prune older backups according to 'prune-backups'.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "repeat-missed": {
      "default": 0,
      "description": "If true, the job will be run as soon as possible if it was missed while the scheduler was not running.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "schedule": {
      "description": "Backup schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "script": {
      "description": "Use specified hook script.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "starttime": {
      "description": "Deprecated: Use 'schedule' instead. Job Start time. 'starttime' and 'dow' will be converted into 'schedule' if used.",
      "optional": 1,
      "pattern": "\\d{1,2}:\\d{1,2}",
      "type": "string",
      "typetext": "HH:MM"
    },
    "stdexcludes": {
      "default": 1,
      "description": "Exclude temporary files and logs.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stop": {
      "default": 0,
      "description": "Stop running backup jobs on this host.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stopwait": {
      "default": 10,
      "description": "Maximal time to wait until a guest system is stopped (minutes).",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "storage": {
      "description": "Store resulting file to this storage.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "tmpdir": {
      "description": "Store temporary files to specified directory.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "The ID of the guest system you want to backup.",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "zstd": {
      "default": 1,
      "description": "Zstd threads. N=0 uses half of the available cores, if N is set to a value bigger than 0, N is used as thread count.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup/{id})。
