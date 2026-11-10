# `/nodes/{node}/vzdump`

原始接口路径：`/nodes/{node}/vzdump`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/vzdump`

Create backup.

**权限**

```json
{
  "description": "The user needs 'VM.Backup' permissions on any VM, and 'Datastore.AllocateSpace' on the backup storage (and fleecing storage when fleecing is used). The 'tmpdir', 'dumpdir', 'script' and 'job-id' parameters are restricted to the 'root@pam' user. The 'prune-backups' setting requires 'Datastore.Allocate' on the backup storage. The 'bwlimit', 'performance' and 'ionice' parameters require 'Sys.Modify' on '/'. The 'stop' parameter requires 'Sys.Modify' on '/nodes/{node}'",
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
| `all` | boolean | 否 | 0 | Backup all known guest systems on this host. |
| `bwlimit` | integer | 否 | 0 | Limit I/O bandwidth (in KiB/s). |
| `compress` | string | 否 | "0" | Compress dump file.；可选值：`0`, `1`, `gzip`, `lzo`, `zstd` |
| `dumpdir` | string | 否 | — | Store resulting files to specified directory. |
| `exclude` | string | 否 | — | Exclude specified guest systems (assumes --all) |
| `exclude-path` | array | 否 | — | Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root, other paths match relative to each subdirectory. |
| `fleecing` | string | 否 | — | Options for backup fleecing (VM only). |
| `ionice` | integer | 否 | 7 | Set IO priority when using the BFQ scheduler. For snapshot and suspend mode backups of VMs, this only affects the compressor. A value of 8 means the idle priority is used, otherwise the best-effort priority is used with the specified value. |
| `job-id` | string | 否 | — | The ID of the backup job. If set, the 'backup-job' metadata field of the backup notification will be set to this value. Only root@pam can set this parameter. |
| `lockwait` | integer | 否 | 180 | Maximal time to wait for the global lock (minutes). |
| `mailnotification` | string | 否 | "always" | Deprecated: use notification targets/matchers instead. Specify when to send a notification mail；可选值：`always`, `failure` |
| `mailto` | string | 否 | — | Deprecated: Use notification targets/matchers instead. Comma-separated list of email addresses or users that should receive email notifications. |
| `mode` | string | 否 | "snapshot" | Backup mode.；可选值：`snapshot`, `suspend`, `stop` |
| `node` | string | 否 | — | Only run if executed on this node. |
| `notes-template` | string | 否 | — | Template string for generating notes for the backup(s). It can contain variables which will be replaced by their values. Currently supported are {{cluster}}, {{guestname}}, {{node}}, and {{vmid}}, but more might be added in the future. Needs to be a single line, newline and backslash need to be escaped as '\n' and '\\' respectively. |
| `notification-mode` | string | 否 | "auto" | Determine which notification system to use. If set to 'legacy-sendmail', vzdump will consider the mailto/mailnotification parameters and send emails to the specified address(es) via the 'sendmail' command. If set to 'notification-system', a notification will be sent via PVE's notification system, and the mailto and mailnotification will be ignored. If set to 'auto' (default setting), an email will be sent if mailto is set, and the notification system will be used if not.；可选值：`auto`, `legacy-sendmail`, `notification-system` |
| `pbs-change-detection-mode` | string | 否 | — | PBS mode used to detect file changes and switch encoding format for container backups.；可选值：`legacy`, `data`, `metadata` |
| `performance` | string | 否 | — | Other performance-related settings. |
| `pigz` | integer | 否 | 0 | Use pigz instead of gzip when N>0. N=1 uses half of cores, N>1 uses N as thread count. |
| `pool` | string | 否 | — | Backup all known guest systems included in the specified pool. |
| `protected` | boolean | 否 | — | If true, mark backup(s) as protected. |
| `prune-backups` | string | 否 | "keep-all=1" | Use these retention options instead of those from the storage configuration. |
| `quiet` | boolean | 否 | 0 | Be quiet. |
| `remove` | boolean | 否 | 1 | Prune older backups according to 'prune-backups'. |
| `script` | string | 否 | — | Use specified hook script. |
| `stdexcludes` | boolean | 否 | 1 | Exclude temporary files and logs. |
| `stdout` | boolean | 否 | — | Write tar to stdout, not to a file. |
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
      "type": "string",
      "typetext": "<string>"
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
    "ionice": {
      "default": 7,
      "description": "Set IO priority when using the BFQ scheduler. For snapshot and suspend mode backups of VMs, this only affects the compressor. A value of 8 means the idle priority is used, otherwise the best-effort priority is used with the specified value.",
      "maximum": 8,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 8)"
    },
    "job-id": {
      "description": "The ID of the backup job. If set, the 'backup-job' metadata field of the backup notification will be set to this value. Only root@pam can set this parameter.",
      "maxLength": 50,
      "optional": 1,
      "pattern": "\\S+",
      "type": "string"
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
    "script": {
      "description": "Use specified hook script.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "stdexcludes": {
      "default": 1,
      "description": "Exclude temporary files and logs.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stdout": {
      "description": "Write tar to stdout, not to a file.",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/vzdump)。
