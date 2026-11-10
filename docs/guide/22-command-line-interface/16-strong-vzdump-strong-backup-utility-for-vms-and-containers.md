# 22.16. **vzdump** \- 虚拟机和容器备份工具 <a href="#strong_vzdump_strong_backup_utility_for_vms_and_containers" id="strong_vzdump_strong_backup_utility_for_vms_and_containers"></a>

## **vzdump** `help` <a href="#cli_vzdump_help" id="cli_vzdump_help"></a>

## **vzdump** `{<vmid>}` `[OPTIONS]` <a href="#cli_vzdump" id="cli_vzdump"></a>

创建备份。

**`<vmid>`: `<string>`**

要备份的客户机系统 ID。

**`--all` `<boolean>` （*默认值 \=* `0`）**

备份此宿主机上所有已知的客户机系统。

**`--bwlimit` `<integer> (0 - N)` （*默认值 \=* `0`）**

限制 I/O 带宽（KiB/s）。

**`--compress` `<0 | 1 | gzip | lzo | zstd>` （*默认值 \=* `0`）**

压缩转储文件。

**`--dumpdir` `<string>`**

将生成的文件存储到指定目录。

**`--exclude` `<string>`**

排除指定客户机系统（假定为 --all）

**`--exclude-path` `<array>`**

排除某些文件/目录（shell 通配模式）。以 */* 开头的路径以容器根目录为锚点，其他路径相对于每个子目录匹配。

**`--fleecing` `[[enabled=]<1|0>] [,storage=<storage ID>]`**

备份 fleecing 的选项（仅限虚拟机）。

**`--ionice` `<integer> (0 - 8)` （*默认值 \=* `7`）**

使用 BFQ 调度器时设置 IO 优先级。对于虚拟机的 snapshot 和 suspend 模式备份，这仅影响压缩程序。值为 8 表示使用空闲优先级，否则使用尽力而为优先级及指定值。

**`--job-id` `\S+`**

备份任务的 ID。如果设置，备份通知的 *backup-job* 元数据字段将设置为此值。只有 [root@pam](mailto:root@pam) 可以设置此参数。

**`--lockwait` `<integer> (0 - N)` （*默认值 \=* `180`）**

等待全局锁的最长时间（分钟）。

**`--mailnotification` `<always | failure>` （*默认值 \=* `always`）**

已弃用：请改用通知目标/匹配器。指定何时发送通知邮件

**`--mailto` `<string>`**

已弃用：请改用通知目标/匹配器。应接收电子邮件通知的电子邮件地址或用户的逗号分隔列表。

**`--mode` `<snapshot | stop | suspend>` （*默认值 \=* `snapshot`）**

备份模式。

**`--node` `<string>`**

仅在此节点上执行时运行。

**`--notes-template` `<string>`**

用于生成备份备注的模板字符串。可包含变量，这些变量会被替换为其值。目前支持 {\\{\\cluster}}、{\\{\\guestname}}、{\\{\\node}} 和 {\\{\\vmid}}，未来可能添加更多。必须为单行，换行和反斜杠分别需要转义为 *\\n* 和 *\\\\*。

{% hint style="info" %}
需要选项：`storage`
{% endhint %}

**`--notification-mode` `<auto | legacy-sendmail | notification-system>` （*默认值 \=* `auto`）**

确定要使用的通知系统。如果设为 *legacy-sendmail*，vzdump 会考虑 mailto/mailnotification 参数，并通过 *sendmail* 命令向指定地址发送电子邮件。如果设为 *notification-system*，则通过 PVE 通知系统发送通知，并忽略 mailto 和 mailnotification。如果设为 *auto*（默认设置），在设置了 mailto 时会发送电子邮件，否则使用通知系统。

**`--pbs-change-detection-mode` `<data | legacy | metadata>`**

用于检测文件更改并切换容器备份编码格式的 PBS 模式。

**`--performance` `[max-workers=<integer>] [,pbs-entries-max=<integer>]`**

其他性能相关设置。

**`--pigz` `<integer>` （*默认值 \=* `0`）**

N\>0 时使用 pigz 代替 gzip。N\=1 使用一半核心，N\>1 使用 N 作为线程数。

**`--pool` `<string>`**

备份指定池中包含的所有已知客户机系统。

**`--protected` `<boolean>`**

如果为 true，将备份标记为受保护。

{% hint style="info" %}
需要选项：`storage`
{% endhint %}

**`--prune-backups` `[keep-all=<1|0>] [,keep-daily=<N>] [,keep-hourly=<N>] [,keep-last=<N>] [,keep-monthly=<N>] [,keep-weekly=<N>] [,keep-yearly=<N>]` （*默认值 \=* `keep-all=1`）**

使用这些保留选项，替代存储配置中的保留选项。

**`--quiet` `<boolean>` （*默认值 \=* `0`）**

静默运行。

**`--remove` `<boolean>` （*默认值 \=* `1`）**

根据 *prune-backups* 清理较旧的备份。

**`--script` `<string>`**

使用指定的钩子脚本。

**`--stdexcludes` `<boolean>` （*默认值 \=* `1`）**

排除临时文件和日志。

**`--stdout` `<boolean>`**

将 tar 写入 stdout，而不是文件。

**`--stop` `<boolean>` （*默认值 \=* `0`）**

停止此宿主机上正在运行的备份任务。

**`--stopwait` `<integer> (0 - N)` （*默认值 \=* `10`）**

等待客户机系统停止的最长时间（分钟）。

**`--storage` `<storage ID>`**

将生成的文件保存到此存储。

**`--tmpdir` `<string>`**

将临时文件保存到指定目录。

**`--zstd` `<integer>` （*默认值 \=* `1`）**

Zstd 线程数。N\=0 使用可用核心的一半；如果 N 设置为大于 0 的值，则使用 N 作为线程数。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
