# `/cluster/backup/{id}`

原始接口路径：`/cluster/backup/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/backup/{id}`

删除 vzdump 备份作业定义。

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
| `id` | string | 是 | — | 作业 ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "作业 ID。",
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

读取 vzdump 备份作业定义。

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
| `id` | string | 是 | — | 作业 ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "作业 ID。",
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
      "description": "备份此宿主机上所有已知的客户机系统。",
      "optional": 1,
      "type": "boolean"
    },
    "bwlimit": {
      "default": 0,
      "description": "限制 I/O 带宽（单位为 KiB/s）。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "comment": {
      "description": "作业描述。",
      "maxLength": 512,
      "optional": 1,
      "type": "string"
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
      "type": "string"
    },
    "enabled": {
      "default": "1",
      "description": "启用或禁用此作业。",
      "optional": 1,
      "type": "boolean"
    },
    "exclude": {
      "description": "排除指定客户机系统（假定 --all）",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string"
    },
    "exclude-path": {
      "description": "排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。",
      "items": {
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "fleecing": {
      "description": "备份 fleecing 选项（仅适用于虚拟机）。",
      "optional": 1,
      "properties": {
        "enabled": {
          "default": 0,
          "default_key": 1,
          "description": "启用备份 fleecing。客户机发生新写入时，将对应块的备份数据缓存在指定存储上，而非直接复制到备份目标。这有助于提高客户机 IO 性能，甚至避免挂起，代价是需要更多存储空间。",
          "optional": 1,
          "type": "boolean"
        },
        "storage": {
          "description": "使用此存储保存 fleecing 镜像。为了高效利用空间，最好使用支持 discard 且支持精简置备或稀疏文件的本地存储。",
          "format": "pve-storage-id",
          "format_description": "storage ID",
          "optional": 1,
          "type": "string"
        }
      },
      "type": "object"
    },
    "id": {
      "description": "作业 ID。",
      "maxLength": 50,
      "pattern": "\\S+",
      "type": "string"
    },
    "ionice": {
      "default": 7,
      "description": "使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。",
      "maximum": 8,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "lockwait": {
      "default": 180,
      "description": "等待全局锁的最长时间（分钟）。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
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
      "type": "string"
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
    "next-run": {
      "description": "此备份作业下次执行时间的 UNIX 时间戳",
      "optional": 1,
      "type": "integer"
    },
    "node": {
      "description": "仅在此节点上执行时运行。",
      "format": "pve-node",
      "optional": 1,
      "type": "string"
    },
    "notes-template": {
      "description": "用于生成备份备注的模板字符串。可以包含将被替换为相应值的变量。目前支持 {{cluster}}、{{guestname}}、{{node}} 和 {{vmid}}，将来可能增加更多变量。必须为单行，换行符和反斜杠需要分别转义为 '\\n' 和 '\\\\'。",
      "maxLength": 1024,
      "optional": 1,
      "requires": "storage",
      "type": "string"
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
      "optional": 1,
      "properties": {
        "max-workers": {
          "default": 16,
          "description": "适用于虚拟机。允许同时运行的 IO 工作线程数量上限。",
          "maximum": 256,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "pbs-entries-max": {
          "default": 1048576,
          "description": "适用于发送到 PBS 的容器备份。限制任意时刻内存中允许的条目数量，以避免意外的 OOM 情况。增大此值可备份包含大量文件的容器。",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "pigz": {
      "default": 0,
      "description": "当 N>0 时，使用 pigz 代替 gzip。N=1 使用一半核心，N>1 则将 N 用作线程数。",
      "optional": 1,
      "type": "integer"
    },
    "pool": {
      "description": "备份指定池中包含的所有已知客户机系统。",
      "optional": 1,
      "type": "string"
    },
    "protected": {
      "description": "如果为 true，则将备份标记为受保护。",
      "optional": 1,
      "requires": "storage",
      "type": "boolean"
    },
    "prune-backups": {
      "description": "使用这些保留选项，而非存储配置中的选项。",
      "optional": 1,
      "properties": {
        "keep-all": {
          "description": "保留所有备份。为 true 时与其他选项冲突。",
          "optional": 1,
          "type": "boolean"
        },
        "keep-daily": {
          "description": "保留最近 <N> 个不同日期的备份。如果同一天有多个备份，则仅保留最新备份。",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-hourly": {
          "description": "保留最近 <N> 个不同小时的备份。如果同一小时有多个备份，则仅保留最新备份。",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-last": {
          "description": "保留最近 <N> 个备份。",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-monthly": {
          "description": "保留最近 <N> 个不同月份的备份。如果同一个月有多个备份，则仅保留最新备份。",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-weekly": {
          "description": "保留最近 <N> 个不同周的备份。如果同一周有多个备份，则仅保留最新备份。",
          "format_description": "N",
          "minimum": "0",
          "optional": 1,
          "type": "integer"
        },
        "keep-yearly": {
          "description": "保留最近 <N> 个不同年份的备份。如果同一年有多个备份，则仅保留最新备份。",
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
      "description": "静默运行。",
      "optional": 1,
      "type": "boolean"
    },
    "remove": {
      "default": 1,
      "description": "根据 'prune-backups' 清理旧备份。",
      "optional": 1,
      "type": "boolean"
    },
    "repeat-missed": {
      "default": 0,
      "description": "如果为 true，则在调度器未运行期间错过的作业将尽快补执行。",
      "optional": 1,
      "type": "boolean"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string"
    },
    "script": {
      "description": "使用指定的钩子脚本。",
      "optional": 1,
      "type": "string"
    },
    "stdexcludes": {
      "default": 1,
      "description": "排除临时文件和日志。",
      "optional": 1,
      "type": "boolean"
    },
    "stop": {
      "default": 0,
      "description": "停止此宿主机上正在运行的备份作业。",
      "optional": 1,
      "type": "boolean"
    },
    "stopwait": {
      "default": 10,
      "description": "等待客户机系统停止的最长时间（分钟）。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "storage": {
      "description": "将生成的文件保存到此存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string"
    },
    "tmpdir": {
      "description": "将临时文件保存到指定目录。",
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "要备份的客户机系统 ID。",
      "format": "pve-vmid-list",
      "optional": 1,
      "type": "string"
    },
    "zstd": {
      "default": 1,
      "description": "Zstd 线程数。N=0 使用一半可用核心；如果 N 设为大于 0 的值，则将 N 用作线程数。",
      "optional": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/backup/{id}`

更新 vzdump 备份作业定义。

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
  "description": "'tmpdir'、'dumpdir' 和 'script' 参数另外限制为仅 'root@pam' 用户可用。"
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
| `all` | boolean | 否 | 0 | 备份此宿主机上所有已知的客户机系统。 |
| `bwlimit` | integer | 否 | 0 | 限制 I/O 带宽（单位为 KiB/s）。 |
| `comment` | string | 否 | — | 作业描述。 |
| `compress` | string | 否 | "0" | 压缩转储文件。；可选值：`0`, `1`, `gzip`, `lzo`, `zstd` |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `dow` | string | 否 | — | 已弃用：请改用 'schedule'。选择星期几。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。 |
| `dumpdir` | string | 否 | — | 将生成的文件保存到指定目录。 |
| `enabled` | boolean | 否 | "1" | 启用或禁用此作业。 |
| `exclude` | string | 否 | — | 排除指定客户机系统（假定 --all） |
| `exclude-path` | array | 否 | — | 排除特定文件/目录（shell 通配模式）。以 '/' 开头的路径相对于容器根目录定位，其他路径相对于每个子目录匹配。 |
| `fleecing` | string | 否 | — | 备份 fleecing 选项（仅适用于虚拟机）。 |
| `id` | string | 是 | — | 作业 ID。 |
| `ionice` | integer | 否 | 7 | 使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，此设置仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用指定值的尽力而为优先级。 |
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
| `repeat-missed` | boolean | 否 | 0 | 如果为 true，则在调度器未运行期间错过的作业将尽快补执行。 |
| `schedule` | string | 否 | — | 备份计划。格式是 `systemd` 日历事件的子集。 |
| `script` | string | 否 | — | 使用指定的钩子脚本。 |
| `starttime` | string | 否 | — | 已弃用：请改用 'schedule'。作业开始时间。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。 |
| `stdexcludes` | boolean | 否 | 1 | 排除临时文件和日志。 |
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
    "comment": {
      "description": "作业描述。",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dow": {
      "description": "已弃用：请改用 'schedule'。选择星期几。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。",
      "format": "pve-day-of-week-list",
      "optional": 1,
      "requires": "starttime",
      "type": "string",
      "typetext": "<string>"
    },
    "dumpdir": {
      "description": "将生成的文件保存到指定目录。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enabled": {
      "default": "1",
      "description": "启用或禁用此作业。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "id": {
      "description": "作业 ID。",
      "maxLength": 50,
      "pattern": "\\S+",
      "type": "string"
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
    "repeat-missed": {
      "default": 0,
      "description": "如果为 true，则在调度器未运行期间错过的作业将尽快补执行。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "script": {
      "description": "使用指定的钩子脚本。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "starttime": {
      "description": "已弃用：请改用 'schedule'。作业开始时间。使用 'starttime' 和 'dow' 时会将其转换为 'schedule'。",
      "optional": 1,
      "pattern": "\\d{1,2}:\\d{1,2}",
      "type": "string",
      "typetext": "HH:MM"
    },
    "stdexcludes": {
      "default": 1,
      "description": "排除临时文件和日志。",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/backup/{id})。
