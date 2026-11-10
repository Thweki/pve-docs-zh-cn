# 22.14. **pvesr** \- Proxmox VE 存储复制 <a href="#strong_pvesr_strong_proxmox_ve_storage_replication" id="strong_pvesr_strong_proxmox_ve_storage_replication"></a>

## **pvesr** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesr" id="cli_pvesr"></a>

## **pvesr create-local-job** `<id> <target>` `[OPTIONS]` <a href="#cli_pvesr_create-local-job" id="cli_pvesr_create-local-job"></a>

创建新的复制任务

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

**`<target>`: `<string>`**

目标节点。

**`--comment` `<string>`**

描述。

**`--disable` `<boolean>`**

用于禁用/停用条目的标志。

**`--rate` `<number> (1 - N)`**

以 mbps（兆字节每秒）为单位的浮点数速率限制。

**`--remove_job` `<full | local>`**

将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 *full*，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。

**`--schedule` `<string>` （*默认值 \=* `*/15`）**

存储复制计划。其格式是 `systemd` 日历事件的一个子集。

**`--source` `<string>`**

供内部使用，用于检测客户机是否被接管。

## **pvesr delete** `<id>` `[OPTIONS]` <a href="#cli_pvesr_delete" id="cli_pvesr_delete"></a>

将复制任务标记为待移除。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

**`--force` `<boolean>`（*默认 \=* `0`）**

将移除 jobconfig 条目，但不执行清理。

**`--keep` `<boolean>` （*默认值 \=* `0`）**

保留目标上的复制数据（不移除）。

## **pvesr disable** `<id>` <a href="#cli_pvesr_disable" id="cli_pvesr_disable"></a>

禁用复制任务。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

## **pvesr enable** `<id>` <a href="#cli_pvesr_enable" id="cli_pvesr_enable"></a>

启用复制任务。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

## **pvesr finalize-local-job** `<id> [<extra-args>]` `[OPTIONS]` <a href="#cli_pvesr_finalize-local-job" id="cli_pvesr_finalize-local-job"></a>

完成复制任务的收尾工作。这会移除时间戳与 \<last\_sync\> 不同的所有复制快照。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

**`<extra-args>`: `<array>`**

要考虑的卷 ID 列表。

**`--last_sync` `<integer> (0 - N)`**

上次成功同步的时间（UNIX 纪元时间）。如果未指定，则移除所有复制快照。

## **pvesr help** `[OPTIONS]` <a href="#cli_pvesr_help" id="cli_pvesr_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvesr list** <a href="#cli_pvesr_list" id="cli_pvesr_list"></a>

列出复制任务。

## **pvesr prepare-local-job** `<id> [<extra-args>]` `[OPTIONS]` <a href="#cli_pvesr_prepare-local-job" id="cli_pvesr_prepare-local-job"></a>

准备启动复制任务。在复制开始之前，在目标节点上调用。此调用供内部使用，并在 stdout 上返回 JSON 对象。此方法首先检查虚拟机 \<vmid\> 是否位于本地节点上。如果是，则立即停止。随后此方法扫描所有卷 ID，查找快照，并移除时间戳与 \<last\_sync\> 不同的所有复制快照。它也会移除任何未使用的卷。返回一个哈希，对所有存在复制快照的卷提供布尔标记。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

**`<extra-args>`: `<array>`**

要考虑的卷 ID 列表。

**`--force` `<boolean>`（*默认 \=* `0`）**

允许移除所有现有卷（卷列表为空）。

**`--last_sync` `<integer> (0 - N)`**

上次成功同步的时间（UNIX 纪元时间）。如果未指定，则移除所有复制快照。

**`--parent_snapname` `<string>`**

快照的名称。

**`--scan` `<string>`**

要扫描陈旧卷的存储 ID 列表。

## **pvesr read** `<id>` <a href="#cli_pvesr_read" id="cli_pvesr_read"></a>

读取复制任务配置。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

## **pvesr run** `[OPTIONS]` <a href="#cli_pvesr_run" id="cli_pvesr_run"></a>

此方法由 systemd-timer 调用，并执行所有同步任务或指定同步任务。

**`--id` `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

**`--mail` `<boolean>` （*默认值 \=* `0`）**

发生故障时发送电子邮件通知。

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

向 stdout 打印更详细的日志。

## **pvesr schedule-now** `<id>` <a href="#cli_pvesr_schedule-now" id="cli_pvesr_schedule-now"></a>

安排复制任务尽快启动。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

## **pvesr set-state** `<vmid> <state>` <a href="#cli_pvesr_set-state" id="cli_pvesr_set-state"></a>

在迁移时设置任务复制状态。此调用供内部使用。它接受 JSON 对象形式的任务状态。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<state>`: `<string>`**

作为 JSON 解码后字符串的任务状态。

## **pvesr status** `[OPTIONS]` <a href="#cli_pvesr_status" id="cli_pvesr_status"></a>

列出此节点上所有复制任务的状态。

**`--guest` `<integer> (100 - 999999999)`**

仅列出此客户机的复制任务。

## **pvesr update** `<id>` `[OPTIONS]` <a href="#cli_pvesr_update" id="cli_pvesr_update"></a>

更新复制任务配置。

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

复制任务 ID。此 ID 由客户机 ID 和任务编号组成，以连字符分隔，即 *\<GUEST\>-\<JOBNUM\>*。

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

用于禁用/停用条目的标志。

**`--rate` `<number> (1 - N)`**

以 mbps（兆字节每秒）为单位的浮点数速率限制。

**`--remove_job` `<full | local>`**

将复制任务标记为待移除。此任务将移除所有本地复制快照。如果设置为 *full*，还会尝试移除目标上的复制卷。然后此任务将从配置文件中移除自身。

**`--schedule` `<string>` （*默认值 \=* `*/15`）**

存储复制计划。其格式是 `systemd` 日历事件的一个子集。

**`--source` `<string>`**

供内部使用，用于检测客户机是否被接管。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
