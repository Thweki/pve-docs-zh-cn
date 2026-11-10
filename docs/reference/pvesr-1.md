# pvesr(1)

## 名称 <a href="#chapter_pvesr" id="chapter_pvesr"></a>

pvesr \- Proxmox VE Storage Replication

## 概要 <a href="#_synopsis" id="_synopsis"></a>

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

## 描述 <a href="#_description" id="_description"></a>

`pvesr` 命令行工具用于管理 Proxmox VE 存储复制框架。存储复制为使用本地存储的客户机提供冗余，并缩短迁移时间。

它会将客户机卷复制到另一个节点，因此无需使用共享存储即可使所有数据可用。复制使用快照来最大限度地减少通过网络发送的流量。因此，在初始完全同步之后，仅增量发送新数据。如果节点发生故障，客户机数据仍可在副本所在节点上使用。

The replication is done automatically in configurable intervals. The minimum replication interval is one minute, and the maximal interval once a week. The format used to specify those intervals is a subset of `systemd` calendar events, see [Schedule Format](#pvesr_schedule_time_format) section:

可以将一台客户机复制到多个目标节点，但不能向同一目标节点复制两次。

可以限制每次复制的带宽，以避免存储或服务器过载。

如果客户机迁移到的节点已经是其复制目标，则只需传输自上次复制以来的更改（所谓的 `deltas`）。这可显著缩短所需时间。如果将客户机迁移到复制目标节点，复制方向会自动切换。

例如：VM100 当前位于 `nodeA`，并复制到 `nodeB`。您将其迁移到 `nodeB`，因此现在它会自动从 `nodeB` 复制回 `nodeA`。

如果迁移到的节点不是客户机的复制目标，则必须传输整个磁盘数据。迁移后，复制作业会继续将此客户机复制到配置的节点。

{% hint style="warning" %}
高可用性可以与存储复制结合使用，但在上次同步时间与节点故障时间之间可能会丢失一些数据。
{% endhint %}

## Supported Storage Types <a href="#_supported_storage_types" id="_supported_storage_types"></a>

<table>
<caption>Table 1. Storage Types</caption>




<thead>
<tr>
<th>描述</th>
<th>插件类型</th>
<th>快照</th>
<th>稳定</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>ZFS（本地）</p></td>
<td><p>zfspool</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
</tr>
</tbody>
</table>

## Schedule Format <a href="#pvesr_schedule_time_format" id="pvesr_schedule_time_format"></a>

Replication uses calendar events for configuring the schedule.

## Error Handling <a href="#_error_handling" id="_error_handling"></a>

如果复制作业遇到问题，它会进入错误状态。在此状态下，配置的复制间隔会暂时暂停。系统会每隔 30 分钟重试失败的复制。一旦成功，原来的计划就会重新激活。

### Possible issues <a href="#_possible_issues" id="_possible_issues"></a>

以下列出了一些最常见的问题。根据您的部署情况，可能还有其他原因。

- 网络未正常工作。
- 复制目标存储上没有剩余可用空间。
- 目标节点上无法使用具有相同存储 ID 的存储。

{% hint style="info" %}
您始终可以使用复制日志来找出问题的原因。
{% endhint %}

### Migrating a guest in case of Error <a href="#_migrating_a_guest_in_case_of_error" id="_migrating_a_guest_in_case_of_error"></a>

发生严重错误时，虚拟客户机可能会卡在故障节点上。此时需要手动将其重新迁移到正常工作的节点。

### Example <a href="#_example" id="_example"></a>

假设您有两个客户机（VM 100 和 CT 200）运行在节点 A 上，并复制到节点 B。节点 A 发生故障且无法重新上线。现在，您必须手动将客户机迁移到节点 B。

- 通过 ssh 连接到节点 B，或通过 Web UI 打开其 Shell
- 检查集群是否具有仲裁

  ```text
  # pvecm status
  ```
- 如果没有仲裁，我们强烈建议先解决此问题，使节点恢复可操作状态。仅当目前无法做到这一点时，才可使用以下命令在当前节点上强制达到仲裁：

  ```text
  # pvecm expected 1
  ```

{% hint style="warning" %}
设置 `expected votes` 后，务必避免任何影响集群的更改（例如添加/移除节点、存储、虚拟客户机）。仅使用它来让关键客户机恢复运行，或解决仲裁问题本身。
{% endhint %}

- 将两个客户机配置文件从原节点 A 移动到节点 B：

  ```text
  # mv /etc/pve/nodes/A/qemu-server/100.conf /etc/pve/nodes/B/qemu-server/100.conf
  # mv /etc/pve/nodes/A/lxc/200.conf /etc/pve/nodes/B/lxc/200.conf
  ```
- 现在可以重新启动这些客户机：

  ```text
  # qm start 100
  # pct start 200
  ```

请记得将 VMID 和节点名称替换为各自的值。

## Managing Jobs <a href="#_managing_jobs" id="_managing_jobs"></a>

[![screenshot/gui-qemu-add-replication-job.png](../assets/screenshot-gui-qemu-add-replication-job-png-8a556dc3f050.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-add-replication-job.png)

您可以使用 Web GUI 轻松创建、修改和删除复制作业。此外，还可以使用命令行界面（CLI）工具 `pvesr` 完成这些操作。

在 Web GUI 中，可以在所有级别（数据中心、节点、虚拟客户机）找到复制面板。它们的区别在于显示哪些作业：全部作业、节点特定作业或客户机特定作业。

When adding a new job, you need to specify the guest if not already selected as well as the target node. The replication [schedule](#pvesr_schedule_time_format) can be set if the default of `all
15 minutes` is not desired. You may impose a rate-limit on a replication job. The rate limit can help to keep the load on the storage acceptable.

复制作业由集群范围内唯一的 ID 标识。此 ID 由 VMID 和作业编号组成。只有使用 CLI 工具时才必须手动指定此 ID。

## Network <a href="#_network" id="_network"></a>

默认情况下，复制流量与客户机迁移流量使用同一网络。如果未设置迁移网络，则复制流量会转而默认使用管理网络。

To use a different network for the replication traffic, configure the `Replication Network` in the web interface under `Datacenter -> Options ->
Replication Settings` or set the `replication` property in the `datacenter.cfg` file:

```text
# use dedicated replication network
replication: secure,network=10.1.2.0/24
```

## Command-line Interface Examples <a href="#_command_line_interface_examples" id="_command_line_interface_examples"></a>

为 ID 为 100 的客户机创建一个每 5 分钟运行一次、带宽限制为 10 Mbps（兆字节每秒）的复制作业。

```text
# pvesr create-local-job 100-0 pve1 --schedule "*/5" --rate 10
```

禁用 ID 为 `100-0` 的活动作业。

```text
# pvesr disable 100-0
```

启用 ID 为 `100-0` 的已停用作业。

```text
# pvesr enable 100-0
```

将 ID 为 `100-0` 的作业的计划间隔更改为每小时一次。

```text
# pvesr update 100-0 --schedule '*/00'
```

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvesr.1.html) · 版本 9.2.13 · 非官方中文翻译。
