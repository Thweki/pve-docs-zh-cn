# 15.13. Cluster Resource Scheduling <a href="#ha_manager_crs" id="ha_manager_crs"></a>

集群资源调度器（CRS）负责为 HA 资源选择新的节点安置位置，并确保 HA 资源位于其允许的节点上。

In every HA Manager round, the scheduler goes through every HA resource and checks whether the HA resource needs any new node placement. This new node placement can be caused by different actions, such as recovering HA resources from a fenced node or a new HA affinity rule. See the section [CRS Scheduling Points](#ha_manager_crs_scheduling_points) for a more thorough description of which actions the CRS takes for specific changes in the cluster.

## 15.13.1. CRS Scheduling Mode <a href="#_crs_scheduling_mode" id="_crs_scheduling_mode"></a>

[![screenshot/gui-datacenter-options-crs.png](../../assets/screenshot-gui-datacenter-options-crs-png-ef60ed8326a1.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-options-crs.png)

CRS 调度模式控制 CRS 如何计算集群的使用情况信息。这些使用情况信息将作为调度决策的依据。可以在 Web 界面（`Datacenter` → `Options` → `Cluster Resource Scheduling`）中更改 CRS 模式。默认模式为 `basic`。更改将从下一轮 HA Manager 开始生效，这应不超过 10 秒。

### 基本调度器 <a href="#ha_manager_crs_basic_scheduler" id="ha_manager_crs_basic_scheduler"></a>

根据每个节点上活动客户机的数量，为 HA 资源选择最合适的节点。

### 静态负载调度器 <a href="#ha_manager_crs_static_scheduler" id="ha_manager_crs_static_scheduler"></a>

使用每个节点上活动客户机的静态使用情况信息，为 HA 资源选择最合适的节点。这包括为活动客户机配置的 CPU 和内存配额。

### 动态负载调度器 <a href="#ha_manager_crs_dynamic_scheduler" id="ha_manager_crs_dynamic_scheduler"></a>

使用每个节点上活动客户机的动态使用情况信息，为 HA 资源选择最合适的节点。这包括活动客户机的平均 CPU 和内存使用量，以及为其配置的 CPU 和内存配额。

## 15.13.2. CRS Scheduling Points <a href="#ha_manager_crs_scheduling_points" id="ha_manager_crs_scheduling_points"></a>

在每一轮 HA Manager 中，CRS 都会检查是否有 HA 资源需要新的节点安置位置，这可能由以下任一调度点触发：

### HA 资源恢复（始终启用） <a href="#_ha_resource_recovery_always_active" id="_ha_resource_recovery_always_active"></a>

当具有活动 HA 资源的节点发生故障时，其所有 HA 资源都需要恢复到其他节点。此处将使用 CRS 算法，在其余节点之间均衡分配这些恢复任务。

### HA 规则配置更改（始终启用） <a href="#_ha_rule_config_changes_always_active" id="_ha_rule_config_changes_always_active"></a>

如果规则对 HA 资源施加了不同的约束，HA 栈将根据新规则的类型，使用 CRS 算法为受这些规则影响的 HA 资源查找新的目标节点：

- 节点亲和性规则：如果创建了节点亲和性规则，或向现有节点亲和性规则添加了 HA 资源/节点，HA 栈将使用 CRS 算法，确保根据这些 HA 资源的节点和优先级约束为其分配节点。
- 正向资源亲和性规则：如果创建了正向资源亲和性规则，或向现有正向资源亲和性规则添加了 HA 资源，HA 栈将使用 CRS 算法，确保将这些 HA 资源移动到同一节点。
- 负向资源亲和性规则：如果创建了负向资源亲和性规则，或向现有负向资源亲和性规则添加了 HA 资源，HA 栈将使用 CRS 算法，确保将这些 HA 资源移动到不同节点。

### 启动时重新均衡 HA 资源（需主动启用） <a href="#_ha_resource_rebalance_on_start_opt_in" id="_ha_resource_rebalance_on_start_opt_in"></a>

启动已启用“启动时重新均衡”的 HA 资源时，CRS 将选择最适合该 HA 资源的节点。如果所选节点不是当前节点，则将该 HA 资源迁移到所选节点。

For the [basic scheduler mode](#ha_manager_crs_basic_scheduler), the node with the fewest active guests is considered the best-suited node.

For the [static-load](#ha_manager_crs_static_scheduler) and [dynamic-load](#ha_manager_crs_dynamic_scheduler) scheduler modes, each node in turn is considered as if the HA resource was already running on it, using CPU and memory usage from the associated guest configuration. Then for each such alternative, CPU and memory usage of all nodes are considered, with memory being weighted much more, because it’s a truly limited resource. For both, CPU and memory, highest usage among nodes (weighted more, as ideally no node should be overcommitted) and average usage of all nodes (to still be able to distinguish in case there already is a more highly committed node) are considered.

此设置可通过 CRS 选项`ha-rebalance-on-start`启用，该选项位于 Web 界面的`Datacenter` → `Options` → `Cluster Resource Scheduling`下。

{% hint style="warning" %}
对于静态负载和动态负载调度器模式，此功能仍处于技术预览阶段。HA 资源越多，可能的组合就越多，因此，如果有数千个 HA 资源，目前不建议使用此功能。
{% endhint %}

## 15.13.3. CRS Load Balancer <a href="#_crs_load_balancer" id="_crs_load_balancer"></a>

各个集群节点的利用率可能会因客户机当前的运行位置以及这些客户机在任意时刻产生的负载而有很大差异。这可能导致节点利用率随时间推移变得不均衡：一个节点上的 HA 资源因资源争用而成为瓶颈，而另一个节点几乎未得到利用。

HA Manager 的自动负载均衡器可以通过自动发起重新均衡迁移来降低集群的整体不均衡程度。目前，这些迁移仅针对 HA 资源发起，并按顺序执行。此外，这些迁移始终遵循当前的 HA 亲和性规则。

为 HA 资源禁用`auto-rebalance`可防止该资源参与自动发起的重新均衡迁移。

{% hint style="info" %}
与禁用了`auto-rebalance`的 HA 资源具有正向亲和性的任何 HA 资源，也不会参与重新均衡迁移。
{% endhint %}

The automatic load balancing system can be enabled and configured in the web interface under `Datacenter` → `Options` → `Cluster Resource Scheduling`. This allows fine-tuning the various parameters as described in the next paragraph for different cluster setups and requirements. The load balancer requires either the [static-load](#ha_manager_crs_static_scheduler) or [dynamic-load](#ha_manager_crs_dynamic_scheduler) scheduler mode to be in use.

在每一轮 HA Manager 中（每轮持续约 10 秒），自动负载均衡器都会检查集群不均衡程度是否超过*不均衡阈值*。如果集群不均衡程度连续高于阈值的 HA Manager 轮数至少达到*保持时长*所指定的轮数，负载均衡器将为一项 HA 资源选择能够最大程度降低集群整体不均衡程度的重新均衡迁移。可以使用*重新均衡方法*选项设置选择最佳重新均衡迁移的方法。最后，如果所选迁移能够使当前集群不均衡程度至少降低*不均衡改善幅度*选项所指定的百分比，负载均衡器就会发起所选迁移。

集群不平衡度由各个节点负载的标准差和均值计算得出，并归一化到 0-100% 范围。*不平衡阈值*和*不平衡改善度*均以百分比配置。*不平衡阈值*默认为 30%，用于控制负载均衡器的灵敏度；值为 `0` 时，每当超过*保持时长*，它都会尝试选择一次再平衡迁移。*不平衡改善度*默认为 10%，用于筛选可接受的再平衡迁移；值为 `0` 时，即使预期不平衡度完全没有变化，它也总是会执行迁移。该值永远不能为负数，因此均衡器绝不会执行预期不平衡度比当前情况更糟的迁移。

{% hint style="info" %}
未来计划将非 HA 资源也纳入负载均衡。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
