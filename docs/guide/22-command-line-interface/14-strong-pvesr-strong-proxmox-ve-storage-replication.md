# 22.14. **pvesr** \- Proxmox VE Storage Replication <a href="#_strong_pvesr_strong_proxmox_ve_storage_replication" id="_strong_pvesr_strong_proxmox_ve_storage_replication"></a>

<a id="cli_pvesr"></a>



**pvesr** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvesr_create-local-job"></a>



**pvesr create-local-job** `<id> <target>` `[OPTIONS]`

Create a new replication job

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

**`<target>`: `<string>`**

目标节点。

**`--comment` `<string>`**

描述。

**`--disable` `<boolean>`**

Flag to disable/deactivate the entry.

**`--rate` `<number> (1 - N)`**

Rate limit in mbps (megabytes per second) as floating point number.

**`--remove_job` `<full | local>`**

Mark the replication job for removal. The job will remove all local replication snapshots. When set to *full*, it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file.

**`--schedule` `<string>` (*default \=* `*/15`)**

Storage replication schedule. The format is a subset of `systemd` calendar events.

**`--source` `<string>`**

For internal use, to detect if the guest was stolen.

<a id="cli_pvesr_delete"></a>



**pvesr delete** `<id>` `[OPTIONS]`

Mark replication job for removal.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

**`--force` `<boolean>`（*默认 \=* `0`）**

Will remove the jobconfig entry, but will not cleanup.

**`--keep` `<boolean>` (*default \=* `0`)**

Keep replicated data at target (do not remove).

<a id="cli_pvesr_disable"></a>



**pvesr disable** `<id>`

Disable a replication job.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

<a id="cli_pvesr_enable"></a>



**pvesr enable** `<id>`

Enable a replication job.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

<a id="cli_pvesr_finalize-local-job"></a>



**pvesr finalize-local-job** `<id> [<extra-args>]` `[OPTIONS]`

Finalize a replication job. This removes all replications snapshots with timestamps different than \<last\_sync\>.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

**`<extra-args>`: `<array>`**

The list of volume IDs to consider.

**`--last_sync` `<integer> (0 - N)`**

Time (UNIX epoch) of last successful sync. If not specified, all replication snapshots gets removed.

<a id="cli_pvesr_help"></a>



**pvesr help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvesr_list"></a>



**pvesr list**

List replication jobs.

<a id="cli_pvesr_prepare-local-job"></a>



**pvesr prepare-local-job** `<id> [<extra-args>]` `[OPTIONS]`

Prepare for starting a replication job. This is called on the target node before replication starts. This call is for internal use, and return a JSON object on stdout. The method first test if VM \<vmid\> reside on the local node. If so, stop immediately. After that the method scans all volume IDs for snapshots, and removes all replications snapshots with timestamps different than \<last\_sync\>. It also removes any unused volumes. Returns a hash with boolean markers for all volumes with existing replication snapshots.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

**`<extra-args>`: `<array>`**

The list of volume IDs to consider.

**`--force` `<boolean>`（*默认 \=* `0`）**

Allow to remove all existion volumes (empty volume list).

**`--last_sync` `<integer> (0 - N)`**

Time (UNIX epoch) of last successful sync. If not specified, all replication snapshots get removed.

**`--parent_snapname` `<string>`**

快照的名称。

**`--scan` `<string>`**

List of storage IDs to scan for stale volumes.

<a id="cli_pvesr_read"></a>



**pvesr read** `<id>`

Read replication job configuration.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

<a id="cli_pvesr_run"></a>



**pvesr run** `[OPTIONS]`

This method is called by the systemd-timer and executes all (or a specific) sync jobs.

**`--id` `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

**`--mail` `<boolean>` (*default \=* `0`)**

Send an email notification in case of a failure.

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

Print more verbose logs to stdout.

<a id="cli_pvesr_schedule-now"></a>



**pvesr schedule-now** `<id>`

Schedule replication job to start as soon as possible.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

<a id="cli_pvesr_set-state"></a>



**pvesr set-state** `<vmid> <state>`

Set the job replication state on migration. This call is for internal use. It will accept the job state as ja JSON obj.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<state>`: `<string>`**

Job state as JSON decoded string.

<a id="cli_pvesr_status"></a>



**pvesr status** `[OPTIONS]`

List status of all replication jobs on this node.

**`--guest` `<integer> (100 - 999999999)`**

Only list replication jobs for this guest.

<a id="cli_pvesr_update"></a>



**pvesr update** `<id>` `[OPTIONS]`

Update replication job configuration.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *\<GUEST\>-\<JOBNUM\>*.

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

Flag to disable/deactivate the entry.

**`--rate` `<number> (1 - N)`**

Rate limit in mbps (megabytes per second) as floating point number.

**`--remove_job` `<full | local>`**

Mark the replication job for removal. The job will remove all local replication snapshots. When set to *full*, it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file.

**`--schedule` `<string>` (*default \=* `*/15`)**

Storage replication schedule. The format is a subset of `systemd` calendar events.

**`--source` `<string>`**

For internal use, to detect if the guest was stolen.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
