# pvesr(1)

## 名称 <a href="#chapter_pvesr" id="chapter_pvesr"></a>

pvesr - Proxmox VE Storage Replication

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pvesr"></a>



**pvesr** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvesr_create-local-job"></a>



**pvesr create-local-job** `<id> <target>` `[OPTIONS]`

Create a new replication job

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

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

**`--schedule` `<string>` (*default =* `*/15`)**

Storage replication schedule. The format is a subset of `systemd` calendar events.

**`--source` `<string>`**

For internal use, to detect if the guest was stolen.

<a id="cli_pvesr_delete"></a>



**pvesr delete** `<id>` `[OPTIONS]`

Mark replication job for removal.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

**`--force` `<boolean>`（*默认 =* `0`）**

Will remove the jobconfig entry, but will not cleanup.

**`--keep` `<boolean>` (*default =* `0`)**

Keep replicated data at target (do not remove).

<a id="cli_pvesr_disable"></a>



**pvesr disable** `<id>`

Disable a replication job.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

<a id="cli_pvesr_enable"></a>



**pvesr enable** `<id>`

Enable a replication job.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

<a id="cli_pvesr_finalize-local-job"></a>



**pvesr finalize-local-job** `<id> [<extra-args>]` `[OPTIONS]`

Finalize a replication job. This removes all replications snapshots with timestamps different than <last_sync>.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

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

Prepare for starting a replication job. This is called on the target node before replication starts. This call is for internal use, and return a JSON object on stdout. The method first test if VM <vmid> reside on the local node. If so, stop immediately. After that the method scans all volume IDs for snapshots, and removes all replications snapshots with timestamps different than <last_sync>. It also removes any unused volumes. Returns a hash with boolean markers for all volumes with existing replication snapshots.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

**`<extra-args>`: `<array>`**

The list of volume IDs to consider.

**`--force` `<boolean>`（*默认 =* `0`）**

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

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

<a id="cli_pvesr_run"></a>



**pvesr run** `[OPTIONS]`

This method is called by the systemd-timer and executes all (or a specific) sync jobs.

**`--id` `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

**`--mail` `<boolean>` (*default =* `0`)**

Send an email notification in case of a failure.

**`--verbose` `<boolean>`（*默认值 =* `0`）**

Print more verbose logs to stdout.

<a id="cli_pvesr_schedule-now"></a>



**pvesr schedule-now** `<id>`

Schedule replication job to start as soon as possible.

**`<id>`: `[1-9][0-9]{2,8}-\d{1,9}`**

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

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

Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. *<GUEST>-<JOBNUM>*.

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

**`--schedule` `<string>` (*default =* `*/15`)**

Storage replication schedule. The format is a subset of `systemd` calendar events.

**`--source` `<string>`**

For internal use, to detect if the guest was stolen.

## 描述 <a href="#_description" id="_description"></a>

The `pvesr` command-line tool manages the Proxmox VE storage replication framework. Storage replication brings redundancy for guests using local storage and reduces migration time.

It replicates guest volumes to another node so that all data is available without using shared storage. Replication uses snapshots to minimize traffic sent over the network. Therefore, new data is sent only incrementally after the initial full sync. In the case of a node failure, your guest data is still available on the replicated node.

The replication is done automatically in configurable intervals. The minimum replication interval is one minute, and the maximal interval once a week. The format used to specify those intervals is a subset of `systemd` calendar events, see [Schedule Format](#pvesr_schedule_time_format) section:

It is possible to replicate a guest to multiple target nodes, but not twice to the same target node.

Each replications bandwidth can be limited, to avoid overloading a storage or server.

Only changes since the last replication (so-called `deltas`) need to be transferred if the guest is migrated to a node to which it already is replicated. This reduces the time needed significantly. The replication direction automatically switches if you migrate a guest to the replication target node.

For example: VM100 is currently on `nodeA` and gets replicated to `nodeB`. You migrate it to `nodeB`, so now it gets automatically replicated back from `nodeB` to `nodeA`.

If you migrate to a node where the guest is not replicated, the whole disk data must send over. After the migration, the replication job continues to replicate this guest to the configured nodes.

{% hint style="warning" %}
High-Availability is allowed in combination with storage replication, but there may be some data loss between the last synced time and the time a node failed.
{% endhint %}

## Supported Storage Types <a href="#_supported_storage_types" id="_supported_storage_types"></a>

<table>
<caption>Table 1. Storage Types</caption>




<thead>
<tr>
<th>Description</th>
<th>Plugin type</th>
<th>Snapshots</th>
<th>Stable</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>ZFS (local)</p></td>
<td><p>zfspool</p></td>
<td><p>yes</p></td>
<td><p>yes</p></td>
</tr>
</tbody>
</table>

## Schedule Format <a href="#pvesr_schedule_time_format" id="pvesr_schedule_time_format"></a>

Replication uses calendar events for configuring the schedule.

## Error Handling <a href="#_error_handling" id="_error_handling"></a>

If a replication job encounters problems, it is placed in an error state. In this state, the configured replication intervals get suspended temporarily. The failed replication is repeatedly tried again in a 30 minute interval. Once this succeeds, the original schedule gets activated again.

### Possible issues <a href="#_possible_issues" id="_possible_issues"></a>

Some of the most common issues are in the following list. Depending on your setup there may be another cause.

- Network is not working.
- No free space left on the replication target storage.
- Storage with the same storage ID is not available on the target node.

{% hint style="info" %}
You can always use the replication log to find out what is causing the problem.
{% endhint %}

### Migrating a guest in case of Error <a href="#_migrating_a_guest_in_case_of_error" id="_migrating_a_guest_in_case_of_error"></a>

In the case of a grave error, a virtual guest may get stuck on a failed node. You then need to move it manually to a working node again.

### Example <a href="#_example" id="_example"></a>

Let’s assume that you have two guests (VM 100 and CT 200) running on node A and replicate to node B. Node A failed and can not get back online. Now you have to migrate the guest to Node B manually.

- connect to node B over ssh or open its shell via the web UI
- check if that the cluster is quorate

  ```text
  # pvecm status
  ```
- If you have no quorum, we strongly advise to fix this first and make the node operable again. Only if this is not possible at the moment, you may use the following command to enforce quorum on the current node:

  ```text
  # pvecm expected 1
  ```

{% hint style="warning" %}
Avoid changes which affect the cluster if `expected votes` are set (for example adding/removing nodes, storages, virtual guests) at all costs. Only use it to get vital guests up and running again or to resolve the quorum issue itself.
{% endhint %}

- move both guest configuration files form the origin node A to node B:

  ```text
  # mv /etc/pve/nodes/A/qemu-server/100.conf /etc/pve/nodes/B/qemu-server/100.conf
  # mv /etc/pve/nodes/A/lxc/200.conf /etc/pve/nodes/B/lxc/200.conf
  ```
- Now you can start the guests again:

  ```text
  # qm start 100
  # pct start 200
  ```

Remember to replace the VMIDs and node names with your respective values.

## Managing Jobs <a href="#_managing_jobs" id="_managing_jobs"></a>

[![screenshot/gui-qemu-add-replication-job.png](../assets/screenshot-gui-qemu-add-replication-job-png-8a556dc3f050.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-add-replication-job.png)

You can use the web GUI to create, modify, and remove replication jobs easily. Additionally, the command-line interface (CLI) tool `pvesr` can be used to do this.

You can find the replication panel on all levels (datacenter, node, virtual guest) in the web GUI. They differ in which jobs get shown: all, node- or guest-specific jobs.

When adding a new job, you need to specify the guest if not already selected as well as the target node. The replication [schedule](#pvesr_schedule_time_format) can be set if the default of `all
15 minutes` is not desired. You may impose a rate-limit on a replication job. The rate limit can help to keep the load on the storage acceptable.

A replication job is identified by a cluster-wide unique ID. This ID is composed of the VMID in addition to a job number. This ID must only be specified manually if the CLI tool is used.

## Network <a href="#_network" id="_network"></a>

By default, replication traffic will go through the same network as the guest migration traffic. If the migration network is not set, this will in turn default to the management network.

To use a different network for the replication traffic, configure the `Replication Network` in the web interface under `Datacenter -> Options ->
Replication Settings` or set the `replication` property in the `datacenter.cfg` file:

```text
# use dedicated replication network
replication: secure,network=10.1.2.0/24
```

## Command-line Interface Examples <a href="#_command_line_interface_examples" id="_command_line_interface_examples"></a>

Create a replication job which runs every 5 minutes with a limited bandwidth of 10 Mbps (megabytes per second) for the guest with ID 100.

```text
# pvesr create-local-job 100-0 pve1 --schedule "*/5" --rate 10
```

Disable an active job with ID `100-0`.

```text
# pvesr disable 100-0
```

Enable a deactivated job with ID `100-0`.

```text
# pvesr enable 100-0
```

Change the schedule interval of the job with ID `100-0` to once per hour.

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
