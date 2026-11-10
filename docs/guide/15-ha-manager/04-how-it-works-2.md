# 15.4. How It Works <a href="#_how_it_works_2" id="_how_it_works_2"></a>

本节详细介绍 Proxmox VE HA 管理器的内部机制。它描述了所有涉及的守护进程以及它们如何协同工作。为提供 HA，每个节点上运行两个守护进程：

**`pve-ha-lrm`**

本地资源管理器（LRM），控制本地节点上运行的服务。它从当前管理器状态文件中读取其服务的请求状态，并执行相应的命令。

**`pve-ha-crm`**

集群资源管理器（CRM），负责制定集群范围的决策。它向 LRM 发送命令、处理结果，并在发生故障时将资源移动到其他节点。CRM 还负责节点隔离。

{% hint style="info" %}
**Locks in the LRM \& CRM**

Locks are provided by our distributed configuration file system (pmxcfs). They are used to guarantee that each LRM is active once and working. As an LRM only executes actions when it holds its lock, we can mark a failed node as fenced if we can acquire its lock. This then lets us recover any failed HA services securely without any interference from the now unknown failed node. This all gets supervised by the CRM which currently holds the manager master lock.
{% endhint %}

## 15.4.1. Service States <a href="#ha_manager_service_states" id="ha_manager_service_states"></a>

CRM 使用服务状态枚举来记录当前服务状态。此状态显示在 GUI 中，并且可以使用`ha-manager`命令行工具查询：

```text
# ha-manager status
quorum OK
master elsa (active, Mon Nov 21 07:23:29 2016)
lrm elsa (active, Mon Nov 21 07:23:22 2016)
service ct:100 (elsa, stopped)
service ct:102 (elsa, started)
service vm:501 (elsa, started)
```

以下是可能状态的列表：

**stopped**

服务已停止（由 LRM 确认）。如果 LRM 检测到已停止的服务仍在运行，它会再次停止该服务。

**request\_stop**

服务应被停止。CRM 等待 LRM 的确认。

**stopping**

停止请求待处理。但 CRM 到目前为止尚未收到该请求。

**started**

Service is active an LRM should start it ASAP if not already running. If the Service fails and is detected to be not running the LRM restarts it (see [Start Failure Policy](08-ha-manager-start-failure-policy.md)).

**starting**

启动请求待处理。但 CRM 尚未收到 LRM 关于服务正在运行的任何确认。

**fence**

Wait for node fencing as the service node is not inside the quorate cluster partition (see [Fencing](07-ha-manager-fencing.md)). As soon as node gets fenced successfully the service will be placed into the recovery state.

**recovery**

等待服务恢复。HA 管理器会尝试寻找一个可以运行该服务的新节点。此搜索取决于在线且具有仲裁的节点列表，以及服务所属的亲和性规则（如果有）。一旦找到新的可用节点，服务就会被移动到该节点，并首先置于 stopped 状态。如果它被配置为运行，新节点就会运行它。

**freeze**

Do not touch the service state. We use this state while we reboot a node, or when we restart the LRM daemon (see [Package Updates](10-ha-manager-package-updates.md)).

**ignored**

就像服务完全不受 HA 管理一样运行。适用于需要暂时完全控制服务，但又不想将其从 HA 配置中移除的情况。

**migrate**

将服务（在线）迁移到其他节点。

**error**

Service is disabled because of LRM errors. Needs manual intervention (see [Error Recovery](09-ha-manager-error-recovery.md)).

**queued**

服务是新添加的，CRM 尚未发现它。

**disabled**

Service is stopped and marked as `disabled`

## 15.4.2. Local Resource Manager <a href="#ha_manager_lrm" id="ha_manager_lrm"></a>

本地资源管理器（`pve-ha-lrm`）在启动时作为守护进程启动，并等待 HA 集群达到仲裁，从而使集群范围的锁能够正常工作。

它可以处于三种状态：

**等待代理锁**

LRM 等待其排他锁。如果未配置任何服务，此状态也用作空闲状态。

**active**

LRM 持有其排他锁，并且已配置服务。

**丢失代理锁**

LRM 丢失了锁，这意味着发生了故障并且失去了仲裁。

LRM 进入活动状态后，会读取 `/etc/pve/ha/manager_status` 中的管理器状态文件，并确定必须为其拥有的服务执行的命令。每个命令都会启动一个工作进程，这些工作进程并行运行，默认最多限制为 4 个。可以通过数据中心配置键 `max_worker` 更改此默认设置。工作进程完成后会被回收，其结果会被保存以供 CRM 使用。

{% hint style="info" %}
**Maximum Concurrent Worker Adjustment Tips**

The default value of at most 4 concurrent workers may be unsuited for a specific setup. For example, 4 live migrations may occur at the same time, which can lead to network congestions with slower networks and/or big (memory wise) services. Also, ensure that in the worst case, congestion is at a minimum, even if this means lowering the `max_worker` value. On the contrary, if you have a particularly powerful, high-end setup you may also want to increase it.
{% endhint %}

CRM 请求的每个命令都可以通过 UID 唯一标识。工作进程完成后，其结果会被处理并写入 LRM 状态文件 `/etc/pve/nodes/<nodename>/lrm_status`。CRM 可以在该文件中收集结果，并根据命令输出让其状态机执行相应操作。

CRM 和 LRM 之间针对每个服务的操作通常始终保持同步。这意味着 CRM 请求一个由 UID 唯一标记的状态，然后 LRM 执行此操作**一次**并写回结果，该结果同样可以通过相同的 UID 标识。这样做是为了确保 LRM 不会执行过时的命令。此行为的唯一例外是 `stop` 和 `error` 命令；这两个命令不依赖于生成的结果，在停止状态下总是执行，在错误状态下执行一次。

{% hint style="info" %}
**Read the Logs**

The HA Stack logs every action it makes. This helps to understand what and also why something happens in the cluster. Here its important to see what both daemons, the LRM and the CRM, did. You may use `journalctl -u pve-ha-lrm` on the node(s) where the service is and the same command for the pve-ha-crm on the node which is the current master.
{% endhint %}

## 15.4.3. Cluster Resource Manager <a href="#ha_manager_crm" id="ha_manager_crm"></a>

集群资源管理器（`pve-ha-crm`）在每个节点上启动，并在该节点等待管理器锁，该锁同一时间只能由一个节点持有。成功获取管理器锁的节点会提升为 CRM 主节点。

它可以处于三种状态：

**等待代理锁**

CRM 等待其排他锁。如果未配置任何服务，此状态也用作空闲状态

**active**

CRM 持有其排他锁，并且已配置服务

**丢失代理锁**

CRM 丢失了锁，这意味着发生了故障并且失去了仲裁。

它的主要任务是管理配置为高可用性的服务，并始终尝试强制执行请求的状态。例如，如果请求状态为 *started* 的服务尚未运行，则会启动该服务。如果它崩溃，会自动再次启动。因此，CRM 决定 LRM 需要执行的操作。

当节点离开集群仲裁时，其状态变为 unknown。如果当前 CRM 随后能够获取故障节点的锁，服务将被*接管*并在另一个节点上重启。

当集群成员确定自己已不再处于集群仲裁中时，LRM 会等待新的仲裁形成。在形成集群仲裁之前，该节点无法重置看门狗。如果节点上有活动服务，或者 LRM 或 CRM 进程未被调度或被终止，这将在看门狗超时后触发重启（这发生在 60 秒后）。

Note that if a node has an active CRM but the LRM is idle, a quorum loss will not trigger a self-fence reset. The reason for this is that all state files and configurations that the CRM accesses are backed up by the [clustered configuration file system](../06-pmxcfs/README.md), which becomes read-only upon quorum loss. This means that the CRM only needs to protect itself against its process being scheduled for too long, in which case another CRM could take over unaware of the situation, causing corruption of the HA state. The open watchdog ensures that this cannot happen.

如果超过 15 分钟未配置任何服务，CRM 会自动返回空闲状态并完全关闭看门狗。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
