# `/nodes/{node}/vzdump`

原始接口路径：`/nodes/{node}/vzdump`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/vzdump`

创建备份。

**方法标识：** `vzdump`

**权限**

```json
{
  "description": "用户需要对任何虚拟机具有 'VM.Backup' 权限，以及对备份存储（使用 fleecing 时也包括 fleecing 存储）具有 'Datastore.AllocateSpace' 权限。'tmpdir'、'dumpdir'、'script' 和 'job-id' 参数仅限 'root@pam' 用户使用。'prune-backups' 设置需要对备份存储具有 'Datastore.Allocate' 权限。'bwlimit'、'performance' 和 'ionice' 参数需要对 '/' 具有 'Sys.Modify' 权限。'stop' 参数需要对 '/nodes/{node}' 具有 'Sys.Modify' 权限",
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
| `all` | boolean | 否 | 0 | 备份此宿主机上所有已知的客户机系统。 |
| `bwlimit` | integer | 否 | 0 | 限制 I/O 带宽（单位为 KiB/s）。 |
| `compress` | string | 否 | "0" | 压缩转储文件。；可选值：`0`, `1`, `gzip`, `lzo`, `zstd` |
| `dumpdir` | string | 否 | — | 将生成的文件保存到指定目录。 |
| `exclude` | string | 否 | — | 排除指定客户机系统（假定 --all） |
| `exclude-path` | array | 否 | — | 排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。 |
| `fleecing` | string | 否 | — | 备份 fleecing 选项（仅适用于虚拟机）。 |
| `ionice` | integer | 否 | 7 | 使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。 |
| `job-id` | string | 否 | — | 备份作业 ID。如果设置，备份通知中的 'backup-job' 元数据字段将设为此值。仅 root@pam 可设置此参数。 |
| `lockwait` | integer | 否 | 180 | 等待全局锁的最长时间（分钟）。 |
| `mailnotification` | string | 否 | "always" | 已弃用：请改用通知目标/匹配器。指定何时发送通知邮件；可选值：`always`, `failure` |
| `mailto` | string | 否 | — | 已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。 |
| `mode` | string | 否 | "snapshot" | 备份模式。；可选值：`snapshot`, `suspend`, `stop` |
| `node` | string | 否 | — | 仅在此节点上执行时运行。 |
| `notes-template` | string | 否 | — | 用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\n' 和 '\\'。 |
| `notification-mode` | string | 否 | "auto" | 确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。；可选值：`auto`, `legacy-sendmail`, `notification-system` |
| `pbs-change-detection-mode` | string | 否 | — | 用于检测文件更改并切换容器备份编码格式的 PBS 模式。；可选值：`legacy`, `data`, `metadata` |
| `performance` | string | 否 | — | 其他性能相关设置。 |
| `pigz` | integer | 否 | 0 | 当 N&gt;0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N&gt;1 则将 N 用作线程数。 |
| `pool` | string | 否 | — | 备份指定池中包含的所有已知客户机系统。 |
| `protected` | boolean | 否 | — | 如果为 true，则将备份标记为受保护。 |
| `prune-backups` | string | 否 | "keep-all=1" | 使用这些保留选项，而非存储配置中的选项。 |
| `quiet` | boolean | 否 | 0 | 静默运行。 |
| `remove` | boolean | 否 | 1 | 根据 'prune-backups' 清理旧备份。 |
| `script` | string | 否 | — | 使用指定的钩子脚本。 |
| `stdexcludes` | boolean | 否 | 1 | 排除临时文件和日志。 |
| `stdout` | boolean | 否 | — | 将 tar 写入 stdout，而非文件。 |
| `stop` | boolean | 否 | 0 | 停止此宿主机上正在运行的备份作业。 |
| `stopwait` | integer | 否 | 10 | 等待客户机系统停止的最长时间（分钟）。 |
| `storage` | string | 否 | — | 将生成的文件保存到此存储。 |
| `tmpdir` | string | 否 | — | 将临时文件保存到指定目录。 |
| `vmid` | string | 否 | — | 要备份的客户机系统 ID。 |
| `zstd` | integer | 否 | 1 | Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "all": {
      "default": 0,
      "description": "备份此宿主机上所有已知的客户机系统。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bwlimit": {
      "default": 0,
      "description": "限制 I/O 带宽（单位为 KiB/s）。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "compress": {
      "default": "0",
      "description": "压缩转储文件。",
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
      "description": "将生成的文件保存到指定目录。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "exclude": {
      "description": "排除指定客户机系统（假定 --all）",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "exclude-path": {
      "description": "排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "fleecing": {
      "description": "备份 fleecing 选项（仅适用于虚拟机）。",
      "format": "backup-fleecing",
      "optional": 1,
      "type": "string",
      "typetext": "[[enabled=]<1|0>] [,storage=<storage ID>]"
    },
    "ionice": {
      "default": 7,
      "description": "使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。",
      "maximum": 8,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 8)"
    },
    "job-id": {
      "description": "备份作业 ID。如果设置，备份通知中的 'backup-job' 元数据字段将设为此值。仅 root@pam 可设置此参数。",
      "maxLength": 50,
      "optional": 1,
      "pattern": "\\S+",
      "type": "string"
    },
    "lockwait": {
      "default": 180,
      "description": "等待全局锁的最长时间（分钟）。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "mailnotification": {
      "default": "always",
      "description": "已弃用：请改用通知目标/匹配器。指定何时发送通知邮件",
      "enum": [
        "always",
        "failure"
      ],
      "optional": 1,
      "type": "string"
    },
    "mailto": {
      "description": "已弃用：请改用通知目标/匹配器。应接收邮件通知的电子邮件地址或用户列表，以逗号分隔。",
      "format": "email-or-username-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mode": {
      "default": "snapshot",
      "description": "备份模式。",
      "enum": [
        "snapshot",
        "suspend",
        "stop"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "仅在此节点上执行时运行。",
      "format": "pve-node",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "notes-template": {
      "description": "用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\\n' 和 '\\\\'。",
      "maxLength": 1024,
      "optional": 1,
      "requires": "storage",
      "type": "string",
      "typetext": "<string>"
    },
    "notification-mode": {
      "default": "auto",
      "description": "确定使用哪种通知系统。如果设为 'legacy-sendmail'，vzdump 将使用 mailto/mailnotification 参数，并通过 'sendmail' 命令向指定地址发送邮件。如果设为 'notification-system'，将通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 'auto'（默认设置），则在设置了 mailto 时发送邮件，否则使用通知系统。",
      "enum": [
        "auto",
        "legacy-sendmail",
        "notification-system"
      ],
      "optional": 1,
      "type": "string"
    },
    "pbs-change-detection-mode": {
      "description": "用于检测文件更改并切换容器备份编码格式的 PBS 模式。",
      "enum": [
        "legacy",
        "data",
        "metadata"
      ],
      "optional": 1,
      "type": "string"
    },
    "performance": {
      "description": "其他性能相关设置。",
      "format": "backup-performance",
      "optional": 1,
      "type": "string",
      "typetext": "[max-workers=<integer>] [,pbs-entries-max=<integer>]"
    },
    "pigz": {
      "default": 0,
      "description": "当 N>0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N>1 则将 N 用作线程数。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "pool": {
      "description": "备份指定池中包含的所有已知客户机系统。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "protected": {
      "description": "如果为 true，则将备份标记为受保护。",
      "optional": 1,
      "requires": "storage",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "prune-backups": {
      "default": "keep-all=1",
      "description": "使用这些保留选项，而非存储配置中的选项。",
      "format": "prune-backups",
      "optional": 1,
      "type": "string",
      "typetext": "[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]"
    },
    "quiet": {
      "default": 0,
      "description": "静默运行。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "remove": {
      "default": 1,
      "description": "根据 'prune-backups' 清理旧备份。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "script": {
      "description": "使用指定的钩子脚本。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "stdexcludes": {
      "default": 1,
      "description": "排除临时文件和日志。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stdout": {
      "description": "将 tar 写入 stdout，而非文件。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stop": {
      "default": 0,
      "description": "停止此宿主机上正在运行的备份作业。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "stopwait": {
      "default": 10,
      "description": "等待客户机系统停止的最长时间（分钟）。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "storage": {
      "description": "将生成的文件保存到此存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "tmpdir": {
      "description": "将临时文件保存到指定目录。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "要备份的客户机系统 ID。",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "zstd": {
      "default": 1,
      "description": "Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。",
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
