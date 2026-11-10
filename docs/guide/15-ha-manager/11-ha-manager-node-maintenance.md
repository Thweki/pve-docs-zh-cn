# 15.11. Node Maintenance <a href="#ha_manager_node_maintenance" id="ha_manager_node_maintenance"></a>

有时需要对节点进行维护，例如更换硬件或只是安装新的内核映像。使用 HA 堆栈时也同样如此。

HA 堆栈主要可在以下两类维护中为你提供支持：

- for general shutdowns or reboots, the behavior can be configured, see [Shutdown Policy](#ha_manager_shutdown_policy).
- 对于不需要关机或重启的维护，或者不希望维护模式在仅重启一次后就自动关闭的情况，可以启用手动维护模式。

## 15.11.1. Maintenance Mode <a href="#_maintenance_mode" id="_maintenance_mode"></a>

可以使用手动维护模式将节点标记为不可用于 HA 操作，从而促使所有由 HA 管理的服务迁移到其他节点。

这些迁移的目标节点从其他当前可用节点中选择，并由 HA 规则配置和已配置的集群资源调度器（CRS）模式决定。每次迁移期间，原始节点都会记录在 HA 管理器的状态中，以便在禁用维护模式且节点恢复在线后，服务可以自动移回。

目前，可以使用 ha-manager CLI 工具启用或禁用维护模式。

**为节点启用维护模式**

```text
# ha-manager crm-command node-maintenance enable NODENAME
```

这将使一个 CRM 命令进入队列；管理器处理该命令时，会在管理器状态中记录进入维护模式的请求。因此，可以在任何节点上提交该命令，而不必只在要置入或退出维护模式的节点上提交。

一旦相应节点上的 LRM 获取到该命令，它就会将自身标记为不可用，但仍会处理所有迁移命令。这意味着，LRM 自我隔离看门狗将保持活动状态，直到所有活动服务都已迁走，并且所有正在运行的 worker 都已结束。

请注意，LRM 一获取到请求的状态，其状态就会显示为 `maintenance` 模式，而不是等到所有服务都迁走后才显示；未来计划改进这一用户体验。目前，可以检查节点上是否仍有任何活动 HA 服务，或留意类似 `pve-ha-lrm[PID]: watchdog closed (disabled)` 的日志行，以了解节点何时完成向维护模式的转换。

{% hint style="info" %}
手动维护模式不会在节点重启时自动删除，只有在使用 `ha-manager` CLI 手动停用，或手动清除 manager-status 时才会删除。
{% endhint %}

**为节点禁用维护模式**

```text
# ha-manager crm-command node-maintenance disable NODENAME
```

禁用手动维护模式的过程与启用过程类似。使用上面显示的 `ha-manager` CLI 命令会将一个 CRM 命令加入队列；该命令处理后，会将相应 LRM 节点重新标记为可用。

如果停用维护模式，启用维护模式时位于该节点上的所有服务都将移回。

## 15.11.2. Shutdown Policy <a href="#ha_manager_shutdown_policy" id="ha_manager_shutdown_policy"></a>

下面介绍节点关机的不同 HA 策略。目前，由于向后兼容性，*Conditional* 是默认策略。一些用户可能会发现 *Migrate* 的行为更符合预期。

可以在 Web UI（`Datacenter` → `Options` → `HA Settings`）中配置关机策略，也可以直接在 `datacenter.cfg` 中配置：

```text
ha: shutdown_policy=<value>
```

### Migrate <a href="#_migrate" id="_migrate"></a>

当本地资源管理器（LRM）收到关机请求且启用此策略后，它会将自身标记为对当前 HA 管理器不可用。这会触发当前位于此节点上的所有 HA 服务迁移。LRM 会尝试延迟关机过程，直到所有正在运行的服务都迁走。但这要求正在运行的服务**能够**迁移到另一个节点。换言之，服务不得绑定到本地，例如使用硬件直通。再比如，严格的节点亲和性规则会告知 HA 管理器，该服务不能在选定节点集之外运行。如果所有这些节点都不可用，关机将一直挂起，直到手动干预。当已关机的节点重新上线后，先前迁走的服务将移回，除非在此期间已手动迁移。

{% hint style="info" %}
关机迁移过程中，看门狗仍处于活动状态。如果节点失去仲裁，它将被隔离，服务将得到恢复。
{% endhint %}

如果在正在维护的节点上启动（先前已停止的）服务，则需要隔离该节点，以确保服务能够迁移到另一个可用节点并在其上启动。

### Failover <a href="#_failover" id="_failover"></a>

此模式可确保所有服务均会停止，但如果当前节点未能很快恢复在线，这些服务也会得到恢复。在进行集群规模的维护时，此模式可能很有用：如果同时关闭过多节点，可能无法对 VM 进行在线迁移，但你仍希望确保 HA 服务尽快恢复并重新启动。

### Freeze <a href="#_freeze" id="_freeze"></a>

此模式可确保所有服务均停止并冻结，因此在当前节点重新上线之前，它们不会得到恢复。

### Conditional <a href="#_conditional" id="_conditional"></a>

*Conditional* 关机策略会自动检测请求的是关机还是重启，并相应地更改行为。

**关机**

通常，如果计划让节点停机一段时间，就会执行关机（*poweroff*）。在这种情况下，LRM 会停止所有受管理的服务。这意味着其他节点随后将接管这些服务。

{% hint style="info" %}
近年的硬件配备大量内存（RAM）。因此，我们会先停止所有资源，再重新启动它们，以避免在线迁移所有这些 RAM。如果要使用在线迁移，需要在关闭节点之前手动调用在线迁移。
{% endhint %}

**重启**

节点的重启通过 *reboot* 命令发起。通常在安装新内核后执行此操作。请注意，这与“关机”不同，因为节点会立即重新启动。

The LRM tells the CRM that it wants to restart, and waits until the CRM puts all resources into the `freeze` state (same mechanism is used for [Package Updates](10-ha-manager-package-updates.md#ha_manager_package_updates)). This prevents those resources from being moved to other nodes. Instead, the CRM starts the resources after the reboot on the same node.

### 手动移动资源 <a href="#_manual_resource_movement" id="_manual_resource_movement"></a>

最后同样重要的是，您还可以在关闭或重启节点之前，手动将资源移动到其他节点。其优势在于您拥有完全的控制权，并且可以决定是否使用在线迁移。

{% hint style="info" %}
请不要 *kill* `pve-ha-crm`、`pve-ha-lrm` 或 `watchdog-mux` 等服务。它们管理并使用看门狗，因此这样做可能导致节点立即重启，甚至复位。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
