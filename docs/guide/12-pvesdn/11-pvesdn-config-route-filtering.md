# 12.11. 前缀列表与路由映射 <a href="#pvesdn_config_route_filtering" id="pvesdn_config_route_filtering"></a>

前缀列表和路由映射允许控制 Proxmox VE 节点与其 BGP、EVPN、OSPF 或 OpenFabric 对等方之间交换哪些路由，并在路由传入或传出时修改其属性。两者协同工作：前缀列表按目标 CIDR 对路由分类，而路由映射将匹配条件和操作串联成有序策略。

如果您以前在 FRR、Cisco IOS 或 Juniper 上使用过 `ip prefix-list` 和 `route-map`，Proxmox VE 中的实体行为与之相同。Proxmox VE 层在 `/etc/pve/sdn/` 下将配置作为集群范围的实体管理，并在应用 SDN 配置时将其转换为 FRR 的 `prefix-list` 和 `route-map` 段。合并后的 FRR 配置最终位于每个节点的 `/etc/frr/frr.conf`；`/etc/frr/frr.conf.local` 中任何节点本地的附加内容都会追加其上。

与其他 SDN 配置一样，编辑首先进入待处理状态，仅在主 `SDN` 面板应用更改后才会生效。

## 12.11.1. 前缀列表 <a href="#pvesdn_config_prefix_lists" id="pvesdn_config_prefix_lists"></a>

前缀列表是有名称的有序条目列表，每个条目匹配单个目标 CIDR（或该 CIDR 内的一组前缀长度），并对其执行 `permit` 或 `deny`。FRR 按序号顺序评估条目，在首次匹配时停止；如果没有条目匹配，前缀列表会隐式拒绝，与原生 FRR 相同。

前缀列表在 `Datacenter -> SDN -> Prefix Lists` 下管理。每个列表具有名称，并包含一个或多个带有以下属性的条目：

**序号**

条目在列表中的评估顺序。在每个列表中必须唯一，且至少为 `1`。如果创建时留空，Proxmox VE 会按 `max + 5` 的惯例自动分配下一个可用序号，为以后插入条目留出空间。

**操作**

`permit` 或 `deny`。每个列表末尾都有一个隐式的 `deny`。

**前缀**

CIDR 表示的目标网络，例如 `192.0.2.0/24` 或 `2001:db8::/32`。允许使用前缀 `0.0.0.0/0`（以及 `::/0`），它们匹配默认路由。

**前缀 \>\=（`ge`）**

可选的最小前缀长度。如果设置，条目将匹配 `prefix` 的任意子网，其长度至少为 `ge`。

**前缀 ⇐（`le`）**

可选的最大前缀长度。如果设置，条目将匹配 `prefix` 的任意子网，其长度最多为 `le`。

如果没有 `le` 或 `ge`，条目将精确匹配该前缀。如果两者均设置，则匹配给定长度范围内的任意子网。例如，`10.0.0.0/8 ge 16 le 24` 匹配每个 /16 至 /24 的子网，位于 `10.0.0.0/8` 内。这是标准的 FRR/Cisco 语义。Proxmox VE 还强制进行以下验证：`ge` 不得超过 `le`，两者都不能小于前缀自身的长度，且必须在地址族范围内（IPv4 为 /32，IPv6 为 /128）。

{% hint style="info" %}
名称 `only_default`、`only_default_v6` 和 `loopbacks_ips` 为保留名称。BGP 和 EVPN 控制器会自动生成这些名称，不能将其用作用户定义的前缀列表名称。
{% endhint %}

## 12.11.2. 路由映射 <a href="#pvesdn_config_route_maps" id="pvesdn_config_route_maps"></a>

路由映射是有序的条目列表，将传入或传出路由与条件匹配，可选择修改度量值或本地优先级等属性，然后执行 `permit`（转发路由，可能已被修改）或 `deny`（丢弃路由）。FRR 按顺序评估条目；第一个匹配决定操作。每个路由映射都隐含以一个除此之外为空的 `deny` 作为最后条目，拒绝所有未显式匹配条目的路由。

路由映射在 `Datacenter -> SDN -> Route Maps` 下管理。每个条目具有以下属性：

**顺序**

条目的评估顺序，介于 `0` 和 `65535` 之间。必填且在路由映射中必须唯一。在顺序之间留出空隙，例如为条目分配 `10`、`20`、`30`，可为以后插入条目留出空间，而无需重新编号。

**操作**

`permit` 或 `deny`。`permit` 让路由通过（执行所有 `set` 操作后）；`deny` 丢弃路由。

**匹配**

一个或多个匹配条件。可用键为：`route-type`、`vni`、`ip-address-prefix-list`、`ip6-address-prefix-list`、`ip-next-hop-prefix-list`、`ip6-next-hop-prefix-list`、`ip-next-hop-address`、`ip6-next-hop-address`、`metric`、`local-preference`、`peer` 和 `tag`。四个 `*-prefix-list` 键通过名称引用前缀列表。`tag` 匹配 32 位路由标签属性，其值与 `tag` 设置操作分配的值相同；这样，一个条目可用标签标记路由，后续条目（位于同一或其他映射中）可对其执行操作。条目的所有匹配条件都必须为真，该条目才适用。

**设置**

条目匹配时要设置的一个或多个属性。可用键为 `ip-next-hop`、`ip-next-hop-peer-address`、`ip-next-hop-unchanged`、`ip6-next-hop`、`ip6-next-hop-peer-address`、`ip6-next-hop-prefer-global`、`local-preference`、`tag`、`weight`、`metric` 和 `src`。`metric` 值支持 `N`、`+N`、`-N`（调整）、`rtt`、`+rtt`、`-rtt`、`igp` 和 `aigp`。`tag` 值接受整数或字面值 `untagged`。

**退出操作**

控制匹配后如何继续评估。留空则使用默认行为（匹配时终止）。`on-match-next` 继续执行紧接着的下一条目。`on-match-goto <order>` 跳转到顺序大于或等于给定值的第一个条目。`continue <order>` 跳转到顺序恰好为该值的条目。三者均对应 FRR 的 `on-match` / `continue` 指令。

**调用**

可选择在此条目处理结束时调用另一个路由映射。这对应 FRR 的 `call` 指令。

{% hint style="info" %}
控制器引用的路由映射在仍被使用时不能删除。请先从控制器中删除引用。名称 `MAP_VTEP_IN`、`MAP_VTEP_OUT`、`correct_src` 以及任何以 `pve_` 开头的名称均保留给内部生成的路由映射使用。
{% endhint %}

## 12.11.3. 前缀列表和路由映射的使用位置 <a href="#pvesdn_config_route_filtering_usage" id="pvesdn_config_route_filtering_usage"></a>

BGP 和 EVPN [控制器](09-pvesdn-config-controllers.md) 各接受一个 `incoming` 和一个 `outgoing` 路由映射。传入映射在安装从对等方收到的路由之前对其执行；传出映射在通告路由之前对其执行。两个字段均可选，并从 SDN 中配置的路由映射中选择。

OSPF 和 OpenFabric [网络结构](10-pvesdn-config-fabrics.md) 接受一个引用前缀列表的 `Route
Filter` 选项。设置后，只有目标通过前缀列表的路由才会安装到内核路由表中。如果未显式指定过滤器，网络结构会根据自身的 `IPv4 Prefix` 和 `IPv6 Prefix` CIDR 生成默认过滤器（一个允许这些网络的 FRR `access-list`）；需要不同策略时，请配置路由过滤器，例如允许从边界节点学习到的默认路由。

## 12.11.4. 示例 <a href="#pvesdn_config_route_filtering_examples" id="pvesdn_config_route_filtering_examples"></a>

仅允许 IPv4 默认路由，例如作为仅应学习上游默认路由的节点上的路由过滤器：

```text
# /etc/pve/sdn/prefix-lists.cfg

prefix-list: default-only
 entries action=permit,prefix=0.0.0.0/0,seq=10
```

允许介于 /16 和 /24 之间、位于 `10.0.0.0/8` 内的所有子网，并拒绝 `10.0.0.0/8` 块内的其他所有内容：

```text
prefix-list: internal-subnets
 entries action=permit,prefix=10.0.0.0/8,ge=16,le=24,seq=10
 entries action=deny,prefix=10.0.0.0/8,le=32,seq=20
```

传出 BGP 策略：将 `local-preference` 降低到 50，针对由 `internal-subnets` 前缀列表匹配的路由，其他路由保持不变。每个路由映射条目各自占一节，顺序以节 ID 后缀编码：

```text
# /etc/pve/sdn/route-maps.cfg

route-map-entry: bgp-out_10
 action permit
 match key=ip-address-prefix-list,value=internal-subnets
 set key=local-preference,value=50

route-map-entry: bgp-out_20
 action permit
```

末尾没有匹配条件的 `permit` 条目是 FRR 中“允许其他所有内容”的模式；如果没有它，路由映射末尾的隐式拒绝将丢弃所有不匹配的路由。

## 12.11.5. BGP <a href="#pvesdn_bgp" id="pvesdn_bgp"></a>

BGP（边界网关协议）可用作 eBGP 无编号网络结构。每个节点都有自己的自治系统编号（ASN），并通过物理接口与相邻节点建立对等关系，无需为网络结构链路分配 IP 地址。

配置选项：

### 网络结构上的选项 <a href="#pvesdn_bgp_fabric" id="pvesdn_bgp_fabric"></a>

**IPv4 前缀**

IPv4 CIDR 网络范围（例如 192.0.2.0/24），用于验证所有节点 IPv4 地址（BGP router-ID）都包含于此前缀中。

**IPv6 前缀**

IPv6 CIDR 网络范围（例如 2001:db8::/64），用于验证网络结构中的所有节点 IPv6 地址都包含于此前缀中。

**BFD**

为此网络结构中的所有对等会话启用双向转发检测。BFD 为节点之间的链路提供快速故障检测。

**路由过滤器**

应用于网络结构对等组入站方向的前缀列表。设置后，此前缀列表会替换隐式的“必须位于网络结构前缀内”过滤器。可用于扩大接受范围（例如接受通过网络结构重分发的其他非网络结构前缀），或使用表达能力更强的匹配。引用 SDN 下定义的前缀列表。

**传入路由映射**

通过 FRR 的 `call` 操作从网络结构对等组的隐式入站过滤器链接的路由映射。只有已通过隐式前缀检查（或路由过滤器覆盖）的前缀才会到达此路由映射。可用于转换或进一步缩小所接受的路由范围（例如调整 community 或 local-preference），但不能扩大接受集合。使用路由过滤器覆盖隐式过滤器。引用 SDN 下定义的路由映射。

**传出路由映射**

应用于网络结构对等组出站方向的路由映射。用于转换或过滤通告给网络结构邻居的内容。引用 SDN 下定义的路由映射。

**重分发**

每个节点上的 BGP 路由器应将哪些其他协议的路由重分发到网络结构中。支持的来源为 `connected`、`kernel`、`static` 和 `ospf`。可为每个来源附加可选的路由映射，在通告前调整重分发的路由。

{% hint style="info" %}
必须至少配置 IPv4 前缀或 IPv6 前缀之一。
{% endhint %}

### 节点上的选项 <a href="#pvesdn_bgp_node" id="pvesdn_bgp_node"></a>

属于网络结构的每个节点上都可用的选项：

**节点**

选择要添加到网络结构的节点。仅显示当前在集群中的节点。

**ASN**

此节点的 BGP 自治系统编号。建议使用私有 ASN 编号（16 位为 64512-65534，32 位为 4200000000-4294967294）。

**IPv4**

此节点的唯一 IPv4 地址，也用作 BGP router-id。当网络结构配置了 IPv4 前缀时必填；同一网络结构中的每个节点必须具有不同的地址。

**IPv6**

此节点的 IPv6 地址。如果仅配置 IPv6 地址（不配置 IPv4 地址），BGP router-id 会通过 FNV-1a 哈希从中推导。

**接口**

指定用于与其他 BGP 节点建立对等连接的接口。这些接口运行无编号 BGP（无需分配 IP 地址）。配置节点 IP 后，会自动创建具有该 IP 的 dummy“回环”接口。

{% hint style="info" %}
与 OSPF 和 OpenFabric 不同，无编号 BGP 接口不需要 IP 地址。对等关系通过 IPv6 链路本地地址自动建立。
{% endhint %}

{% hint style="info" %}
在 eBGP 无编号网络结构中，直接建立对等关系的节点必须具有不同的 ASN，BGP 会话才能建立。
{% endhint %}

### 将 BGP 网络结构与 EVPN 结合使用 <a href="#pvesdn_bgp_evpn" id="pvesdn_bgp_evpn"></a>

配置 EVPN 控制器时，可以选择 BGP 网络结构作为底层网络，而无需手动指定对等方地址。默认配置将 EVPN 覆盖网络（VTEP）会话作为 iBGP 运行，并为路由进程使用 EVPN 控制器的 ASN。每个节点的网络结构 ASN 通过 `local-as` 自动应用于底层邻居组。

这意味着 EVPN 控制器 ASN 和各节点网络结构 ASN 应不同。例如，三个节点的底层网络分别使用 ASN 65001、65002 和 65003 时，EVPN 控制器可为覆盖网络使用 ASN 65000。

或者，在 EVPN 控制器上将 BGP 模式设为“external”，使 VTEP 会话作为 eBGP 运行。此时，每个节点的网络结构 ASN 也会用作 VTEP 对等组的本地 ASN，因此 VTEP 会自然地在不同 ASN 下相互建立对等关系，无需单独的覆盖网络 ASN。EVPN 控制器 ASN 仍用于自动推导的 route-target 值，以使其在整个网络结构中保持一致。

{% hint style="info" %}
将 BGP 网络结构用作 EVPN 底层网络时，要求每个节点都有 IPv4 地址，因为 EVPN 会将其用作 VTEP 地址。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
