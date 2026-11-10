# 22.17. **ha-manager** \- Proxmox VE HA Manager <a href="#_strong_ha_manager_strong_proxmox_ve_ha_manager" id="_strong_ha_manager_strong_proxmox_ve_ha_manager"></a>

<a id="cli_ha-manager"></a>



**ha-manager** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_ha-manager_add"></a>



**ha-manager add** `<sid>` `[OPTIONS]`

创建新的 HA 资源。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`--auto-rebalance` `<boolean>` (*默认 \=* `1`)**

自动重新平衡期间可以迁移 HA 资源

**`--comment` `<string>`**

描述。

**`--failback` `<boolean>` (*默认 \=* `1`)**

如果优先级高于当前节点的节点上线，则根据其节点亲和性规则，自动将 HA 资源迁移到优先级最高的节点。

**`--group` `<string>`**

HA 组标识符。

**`--max_relocate` `<integer> (0 - N)` (*默认 \=* `1`)**

资源启动失败时，尝试重定位资源的最大次数。

**`--max_restart` `<integer> (0 - N)` (*默认 \=* `1`)**

资源启动失败后，在节点上重启该资源的最大尝试次数。达到该次数后，HA 管理器将尝试把资源重定位到符合条件的节点。

**`--state` `<disabled | enabled | ignored | started | stopped>` (*默认 \=* `started`)**

请求的资源状态。

**`--type` `<ct | vm>`**

资源类型。

<a id="cli_ha-manager_config"></a>



**ha-manager config** `[OPTIONS]`

列出 HA 资源。

**`--type` `<ct | vm>`**

仅列出特定类型的资源

<a id="cli_ha-manager_crm-command_arm-ha"></a>



**ha-manager crm-command arm-ha**

请求在 HA 堆栈解除布防后重新布防。

<a id="cli_ha-manager_crm-command_disarm-ha"></a>



**ha-manager crm-command disarm-ha** `<resource-mode>`

请求解除 HA 堆栈的布防，并释放整个集群范围内的所有看门狗。

**`<resource-mode>`: `<freeze | ignore>`**

控制解除布防期间如何处理 HA 管理的资源。资源的当前状态不受影响。*freeze*：不应用新命令和状态更改。*ignore*：从 HA 跟踪中移除资源，并可将其当作非 HA 管理的资源进行管理。

<a id="cli_ha-manager_crm-command_migrate"></a>



**ha-manager crm-command migrate** `<sid> <node>`

请求将资源在线迁移到另一个节点。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`<node>`: `<string>`**

目标节点。

<a id="cli_ha-manager_crm-command_node-maintenance_disable"></a>



**ha-manager crm-command node-maintenance disable** `<node>`

更改 node-maintenance 请求状态。

**`<node>`: `<string>`**

集群节点名称。

<a id="cli_ha-manager_crm-command_node-maintenance_enable"></a>



**ha-manager crm-command node-maintenance enable** `<node>`

更改 node-maintenance 请求状态。

**`<node>`: `<string>`**

集群节点名称。

<a id="cli_ha-manager_crm-command_relocate"></a>



**ha-manager crm-command relocate** `<sid> <node>`

请求将资源重定位到另一个节点。这会停止旧节点上的服务，并在目标节点上重新启动该服务。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`<node>`: `<string>`**

目标节点。

<a id="cli_ha-manager_crm-command_stop"></a>



**ha-manager crm-command stop** `<sid> <timeout>`

请求停止服务。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`<timeout>`: `<integer> (0 - N)`**

超时时间（秒）。如果设置为 0，将执行强制停止。

<a id="cli_ha-manager_groupadd"></a>



**ha-manager groupadd** `<group> --nodes <string>` `[OPTIONS]`

创建新的 HA 组。（已弃用，建议使用 HA 规则）

**`<group>`: `<string>`**

HA 组标识符。

**`--comment` `<string>`**

描述。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--nofailback` `<boolean>` (*默认 \=* `0`)**

CRM 会尝试在优先级最高的节点上运行服务。如果优先级更高的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。

**`--restricted` `<boolean>` (*默认 \=* `0`)**

绑定到受限组的资源只能在该组定义的节点上运行。

**`--type` `<group>`**

组类型。

<a id="cli_ha-manager_groupconfig"></a>



**ha-manager groupconfig**

获取 HA 组。（已弃用，建议使用 HA 规则）

<a id="cli_ha-manager_groupremove"></a>



**ha-manager groupremove** `<group>`

删除 HA 组配置。（已弃用，建议使用 HA 规则）

**`<group>`: `<string>`**

HA 组标识符。

<a id="cli_ha-manager_groupset"></a>



**ha-manager groupset** `<group>` `[OPTIONS]`

更新 HA 组配置。（已弃用，建议使用 HA 规则）

**`<group>`: `<string>`**

HA 组标识符。

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--nofailback` `<boolean>` (*默认 \=* `0`)**

CRM 会尝试在优先级最高的节点上运行服务。如果优先级更高的节点上线，CRM 会将服务迁移到该节点。启用 nofailback 可阻止此行为。

**`--restricted` `<boolean>` (*默认 \=* `0`)**

绑定到受限组的资源只能在该组定义的节点上运行。

<a id="cli_ha-manager_help"></a>



**ha-manager help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_ha-manager_migrate"></a>



**ha-manager migrate**

*ha-manager crm-command migrate* 的别名。

<a id="cli_ha-manager_relocate"></a>



**ha-manager relocate**

*ha-manager crm-command relocate* 的别名。

<a id="cli_ha-manager_remove"></a>



**ha-manager remove** `<sid>` `[OPTIONS]`

删除资源配置。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`--purge` `<boolean>` (*默认 \=* `1`)**

从引用此资源的规则中移除此资源；如果此资源是规则中的唯一资源，则删除该规则

<a id="cli_ha-manager_rules_add"></a>



**ha-manager rules add** `<type> <rule>` `[OPTIONS]`

创建 HA 规则。

**`<type>`: `<node-affinity | resource-affinity>`**

HA 规则类型。

**`<rule>`: `<string>`**

HA 规则标识符。

`Conditional options:`

**`[type=node-affinity]`**

**`--affinity` `<negative | positive>` (*默认 \=* `positive`)**

描述 HA 资源应放置在指定节点上（*positive*），还是应放置在指定节点以外的任何节点上（*negative*）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

**`--strict` `<boolean>` (*默认 \=* `0`)**

描述节点亲和性规则是严格的还是非严格的。

**`[type=resource-affinity]`**

**`--affinity` `<negative | positive>`**

描述 HA 资源是否应保留在同一节点上（*positive*），还是应保留在不同节点上（*negative*）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

<a id="cli_ha-manager_rules_config"></a>



**ha-manager rules config** `[OPTIONS]` `[FORMAT_OPTIONS]`

获取 HA 规则。

**`--resource` `<string>`**

将返回的列表限制为影响指定资源的规则。

**`--type` `<node-affinity | resource-affinity>`**

将返回的列表限制为指定的规则类型。

<a id="cli_ha-manager_rules_list"></a>



**ha-manager rules list** `[OPTIONS]` `[FORMAT_OPTIONS]`

获取 HA 规则。

**`--resource` `<string>`**

将返回的列表限制为影响指定资源的规则。

**`--type` `<node-affinity | resource-affinity>`**

将返回的列表限制为指定的规则类型。

<a id="cli_ha-manager_rules_remove"></a>



**ha-manager rules remove** `<rule>`

删除 HA 规则。

**`<rule>`: `<string>`**

HA 规则标识符。

<a id="cli_ha-manager_rules_set"></a>



**ha-manager rules set** `<type> <rule>` `[OPTIONS]`

更新 HA 规则。

**`<type>`: `<node-affinity | resource-affinity>`**

HA 规则类型。

**`<rule>`: `<string>`**

HA 规则标识符。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

`Conditional options:`

**`[type=node-affinity]`**

**`--affinity` `<negative | positive>` (*默认 \=* `positive`)**

描述 HA 资源应放置在指定节点上（*positive*），还是应放置在指定节点以外的任何节点上（*negative*）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--nodes` `<node>[:<pri>]{,<node>[:<pri>]}*`**

带有可选优先级的集群节点名称列表。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

**`--strict` `<boolean>` (*默认 \=* `0`)**

描述节点亲和性规则是严格的还是非严格的。

**`[type=resource-affinity]`**

**`--affinity` `<negative | positive>`**

描述 HA 资源是否应保留在同一节点上（*positive*），还是应保留在不同节点上（*negative*）。

**`--comment` `<string>`**

HA 规则描述。

**`--disable` `<boolean>`**

HA 规则是否已禁用。

**`--resources` `<type>:<name>{,<type>:<name>}*`**

HA 资源 ID 列表。每个 ID 由资源类型和后随的特定于资源的名称组成，二者以冒号分隔（示例：vm:100,ct:101）。

<a id="cli_ha-manager_set"></a>



**ha-manager set** `<sid>` `[OPTIONS]`

更新资源配置。

**`<sid>`: `<type>:<name>`**

HA 资源 ID。由资源类型和特定于资源的名称组成，二者以冒号分隔（示例：vm:100 / ct:100）。对于虚拟机和容器，可以直接使用 VM 或 CT ID 作为简写（示例：100）。

**`--auto-rebalance` `<boolean>` (*默认 \=* `1`)**

自动重新平衡期间可以迁移 HA 资源

**`--comment` `<string>`**

描述。

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--failback` `<boolean>` (*默认 \=* `1`)**

如果优先级高于当前节点的节点上线，则根据其节点亲和性规则，自动将 HA 资源迁移到优先级最高的节点。

**`--group` `<string>`**

HA 组标识符。

**`--max_relocate` `<integer> (0 - N)` (*默认 \=* `1`)**

资源启动失败时，尝试重定位资源的最大次数。

**`--max_restart` `<integer> (0 - N)` (*默认 \=* `1`)**

资源启动失败后，在节点上重启该资源的最大尝试次数。达到该次数后，HA 管理器将尝试把资源重定位到符合条件的节点。

**`--state` `<disabled | enabled | ignored | started | stopped>` (*默认 \=* `started`)**

请求的资源状态。

<a id="cli_ha-manager_status"></a>



**ha-manager status** `[OPTIONS]`

显示 HA 管理器状态。

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

详细输出。包含完整的 CRM 和 LRM 状态（JSON）。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
