# 15.7. Fencing <a href="#ha_manager_fencing" id="ha_manager_fencing"></a>

节点发生故障时，隔离可确保故障节点一定处于离线状态。这是必需的，以确保资源在另一个节点上恢复时不会重复运行。这是一项非常重要的任务，因为如果没有隔离，就无法在另一个节点上恢复资源。

如果某个节点未被隔离，它将处于未知状态，并且可能仍然可以访问共享资源。这非常危险！想象一下，除存储网络外，所有网络都中断了。此时，虽然无法从公共网络访问该 VM，但它仍在运行并写入共享存储。

如果随后我们直接在另一个节点上启动此 VM，就会产生危险的竞争条件，因为两个节点都会写入数据。这种情况可能会破坏所有 VM 数据，并导致整个 VM 无法使用。如果存储具有防止多重挂载的保护机制，恢复也可能失败。

## 15.7.1. How Proxmox VE Fences <a href="#_how_proxmox_ve_fences" id="_how_proxmox_ve_fences"></a>

有多种方法可以隔离节点，例如使用隔离设备切断节点电源或完全禁用其通信。这些设备通常相当昂贵，并且会给系统引入额外的关键组件，因为如果它们发生故障，您将无法恢复任何服务。

因此，我们希望集成一种更简单的隔离方法，不需要额外的外部硬件。这可以使用看门狗定时器来实现。

**可用的隔离方法**

- 外部电源开关
- 通过在交换机上禁用所有网络流量来隔离节点
- 使用看门狗定时器进行自我隔离

自微控制器出现以来，看门狗定时器就广泛应用于关键任务和高可靠性系统。它们通常是简单的独立集成电路，用于检测计算机故障并从故障中恢复。

在正常运行期间，`ha-manager` 会定期重置看门狗定时器，以防止其超时。如果计算机因硬件故障或程序错误而未能重置看门狗，定时器将超时并触发整台服务器重置（重新启动）。

近期的服务器主板通常包含此类硬件看门狗，但需要对其进行配置。如果没有可用或已配置的看门狗，我们会回退到 Linux 内核的 *softdog*。虽然它仍然可靠，但它并不独立于服务器硬件，因此可靠性低于硬件看门狗。

## 15.7.2. Configure Hardware Watchdog <a href="#_configure_hardware_watchdog" id="_configure_hardware_watchdog"></a>

默认情况下，出于安全原因，所有硬件看门狗模块均被阻止。如果未正确初始化，它们就像一把上了膛的枪。要启用硬件看门狗，需要在 */etc/default/pve-ha-manager* 中指定要加载的模块，例如：

```text
# select watchdog module (default is softdog)
WATCHDOG_MODULE=iTCO_wdt
```

此配置由 *watchdog-mux* 服务读取，该服务会在启动时加载指定的模块。

## 15.7.3. Recover Fenced Services <a href="#_recover_fenced_services" id="_recover_fenced_services"></a>

节点发生故障且隔离成功后，CRM 会尝试将服务从故障节点移动到仍在线的节点。

恢复节点的选择受以下因素影响：当前活动节点列表、根据所用调度器确定的各自负载，以及服务所属的亲和性规则（如果有）。

首先，CRM 会构建一组可供该服务使用的节点。如果服务属于节点亲和性规则，则该集合会缩减为规则中优先级最高的节点。如果服务属于资源亲和性规则，则进一步缩减该集合以满足其约束，即让该服务与某些其他服务位于同一节点，或让该服务与某些其他服务位于不同节点。最后，CRM 根据所用调度器选择负载最低的节点，以最大限度降低节点过载的可能性。

{% hint style="danger" %}
发生节点故障时，CRM 会将服务分配给其余节点。这会增加这些节点上的服务数量，并可能导致高负载，尤其是在小型集群中。请合理设计集群，使其能够应对此类最坏情况。
{% endhint %}

## 15.7.4. Fencing \& Watchdog Status <a href="#ha_manager_fencing_status" id="ha_manager_fencing_status"></a>

`ha-manager status` 的输出包含一个 fencing 条目，其中显示 CRM 看门狗状态。每个 LRM 条目还会显示其自身的看门狗状态。

**armed**

CRM 正在主动管理服务，并已打开其看门狗。每个节点的 LRM 在持有其代理锁期间也会持有一个看门狗。失去仲裁或守护进程发生故障时，相应的看门狗会触发节点重置，以确保安全故障转移。

**standby**

HA 堆栈已就绪，但没有 CRM 正在作为主节点主动运行，例如尚未配置任何 HA 资源或集群刚刚启动时。CRM 看门狗未打开。一旦有 CRM 接管为主节点，隔离状态就会自动转换为 `armed`。

**disarming**

已发出 `disarm-ha` 命令。CRM 正在冻结服务或暂停对服务的跟踪，并等待所有 LRM 释放其看门狗。在此阶段，CRM 看门狗仍处于活动状态。每个 LRM 条目确认解除看门狗后，其看门狗状态会变为 `released`。

**disarmed**

All watchdogs have been released cluster-wide. No automatic fencing, failover, or recovery takes place. See [Disarming HA for Cluster Maintenance](12-ha-manager-disarm.md).

{% hint style="info" %}
`watchdog-mux` 服务在其整个生命周期内始终保持底层 `/dev/watchdog` 设备处于打开状态，即使没有 HA 客户端连接也是如此。这可防止其他进程占用该设备，并确保 HA 堆栈始终能够重新获取它。并非所有硬件看门狗驱动程序都支持 magic close，因此关闭设备可能会触发意外重置。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
