# 12.11. Prefix Lists and Route Maps <a href="#pvesdn_config_route_filtering" id="pvesdn_config_route_filtering"></a>

Prefix lists and route maps let you control which routes are exchanged between the Proxmox VE nodes and their BGP, EVPN, OSPF, or OpenFabric peers, and modify attributes of those routes on the way in or out. The two work together: a prefix list classifies routes by their destination CIDR, while a route map chains match conditions and actions into an ordered policy.

If you have used `ip prefix-list` and `route-map` on FRR, Cisco IOS, or Juniper before, the Proxmox VE entities behave the same way. The Proxmox VE layer manages the configuration as cluster-wide entities under `/etc/pve/sdn/` and translates them to FRR `prefix-list` and `route-map` stanzas when applying the SDN configuration. The merged FRR configuration ends up in `/etc/frr/frr.conf` on each node; any node-local additions in `/etc/frr/frr.conf.local` are appended on top.

Like the rest of the SDN configuration, edits go to a pending state first and become active only after you apply changes in the main `SDN` panel.

## 12.11.1. Prefix Lists <a href="#pvesdn_config_prefix_lists" id="pvesdn_config_prefix_lists"></a>

A prefix list is an ordered, named list of entries that each match a single destination CIDR (or a range of prefix lengths within that CIDR) and either `permit` or `deny` it. FRR evaluates entries in order of their sequence number and stops at the first match; if no entry matches, the prefix list denies implicitly, same as plain FRR.

Prefix lists are managed under `Datacenter -> SDN -> Prefix Lists`. Each list has a name and contains one or more entries with the following properties:

**Sequence Nr.**

Order in which the entry is evaluated within the list. Must be unique per list and at least `1`. If left empty on creation, Proxmox VE auto-assigns the next free sequence number using the convention `max + 5`, leaving room for later insertions.

**Action**

Either `permit` or `deny`. There is an implicit `deny` at the end of each list.

**Prefix**

Destination network in CIDR notation, for example `192.0.2.0/24` or `2001:db8::/32`. The prefix `0.0.0.0/0` (and `::/0`) is allowed and matches the default route.

**Prefix \>\= (`ge`)**

Optional minimum prefix length. If set, the entry matches any subnet of `prefix` whose length is at least `ge`.

**Prefix ⇐ (`le`)**

Optional maximum prefix length. If set, the entry matches any subnet of `prefix` whose length is at most `le`.

Without `le` or `ge` an entry matches the prefix exactly. With both set, it matches any subnet within the given length range. For example `10.0.0.0/8 ge 16 le 24` matches every /16 to /24 subnet inside `10.0.0.0/8`. This is the standard FRR/Cisco semantics. Additional validation enforced by Proxmox VE: `ge` must not exceed `le`, neither may be smaller than the prefix’s own length, and both must stay within the address family bound (/32 for IPv4, /128 for IPv6).

{% hint style="info" %}
The names `only_default`, `only_default_v6`, and `loopbacks_ips` are reserved. The BGP and EVPN controllers generate these automatically and they cannot be used as user-defined prefix list names.
{% endhint %}

## 12.11.2. Route Maps <a href="#pvesdn_config_route_maps" id="pvesdn_config_route_maps"></a>

A route map is an ordered list of entries that match incoming or outgoing routes against criteria, optionally modify attributes such as the metric or local preference, and either `permit` (forward the route, possibly modified) or `deny` (drop the route). FRR evaluates entries in order; the first match controls the action. Every route map implicitly has an otherwise empty `deny` as its last entry, denying all routes that did not match an entry explicitly.

Route maps are managed under `Datacenter -> SDN -> Route Maps`. Each entry has the following properties:

**Order**

Order in which the entry is evaluated, between `0` and `65535`. Mandatory and must be unique within a route map. Leaving gaps between orders, for example assigning entries `10`, `20`, `30`, leaves room for later insertions without renumbering.

**Action**

Either `permit` or `deny`. `permit` lets the route pass (after any `set` actions); `deny` drops it.

**Match**

One or more match conditions. Available keys are: `route-type`, `vni`, `ip-address-prefix-list`, `ip6-address-prefix-list`, `ip-next-hop-prefix-list`, `ip6-next-hop-prefix-list`, `ip-next-hop-address`, `ip6-next-hop-address`, `metric`, `local-preference`, `peer`, and `tag`. The four `*-prefix-list` keys reference a prefix list by name. `tag` matches a 32-bit route tag attribute, the same value that the `tag` set action assigns; this lets one entry mark routes with a tag and a later entry (in the same or another map) act on them. All match conditions of an entry must be true for it to apply.

**Set**

One or more attributes to set when the entry matches. Available keys are `ip-next-hop`, `ip-next-hop-peer-address`, `ip-next-hop-unchanged`, `ip6-next-hop`, `ip6-next-hop-peer-address`, `ip6-next-hop-prefer-global`, `local-preference`, `tag`, `weight`, `metric`, and `src`. The `metric` value supports `N`, `+N`, `-N` (adjust), `rtt`, `+rtt`, `-rtt`, `igp`, and `aigp`. The `tag` value accepts an integer or the literal `untagged`.

**Exit Action**

Controls how evaluation continues after a match. Leave empty for the default behavior (terminate on match). `on-match-next` proceeds with the immediately following entry. `on-match-goto <order>` jumps to the first entry whose order is greater than or equal to the given value. `continue <order>` jumps to the entry with exactly that order. All three correspond to the FRR `on-match` / `continue` directives.

**Call**

Optionally call another route map at the end of this entry’s processing. This corresponds to the FRR `call` directive.

{% hint style="info" %}
A route map referenced by a controller cannot be deleted while it is still in use. Delete the reference from the controller first. The names `MAP_VTEP_IN`, `MAP_VTEP_OUT`, `correct_src`, and any name starting with `pve_` are reserved for internally generated route maps.
{% endhint %}

## 12.11.3. Where Prefix Lists and Route Maps Are Used <a href="#pvesdn_config_route_filtering_usage" id="pvesdn_config_route_filtering_usage"></a>

The BGP and EVPN [controllers](09-pvesdn-config-controllers.md) each take an `incoming` and an `outgoing` route map. Incoming maps run against routes received from a peer before installing them; outgoing maps run against routes before announcing them. Both fields are optional and selected from the route maps configured in the SDN.

The OSPF and OpenFabric [fabrics](10-pvesdn-config-fabrics.md) take a `Route
Filter` option that references a prefix list. When set, only routes whose destinations pass the prefix list are installed in the kernel routing table. Without an explicit filter, the fabric generates a default filter from the fabric’s own `IPv4 Prefix` and `IPv6 Prefix` CIDRs (an FRR `access-list` permitting those networks); configure a route filter when you need a different policy, for example to allow a default route learned from a border node.

## 12.11.4. Examples <a href="#pvesdn_config_route_filtering_examples" id="pvesdn_config_route_filtering_examples"></a>

Allow only the IPv4 default route, for example as a route filter on a node that should learn just an upstream default:

```text
# /etc/pve/sdn/prefix-lists.cfg

prefix-list: default-only
 entries action=permit,prefix=0.0.0.0/0,seq=10
```

Allow every subnet between /16 and /24 inside `10.0.0.0/8`, and deny anything else within the `10.0.0.0/8` block:

```text
prefix-list: internal-subnets
 entries action=permit,prefix=10.0.0.0/8,ge=16,le=24,seq=10
 entries action=deny,prefix=10.0.0.0/8,le=32,seq=20
```

Outgoing BGP policy that lowers `local-preference` to 50 on routes matched by the `internal-subnets` prefix list, and otherwise leaves routes untouched. Each route map entry is its own section, with the order encoded as a suffix on the section ID:

```text
# /etc/pve/sdn/route-maps.cfg

route-map-entry: bgp-out_10
 action permit
 match key=ip-address-prefix-list,value=internal-subnets
 set key=local-preference,value=50

route-map-entry: bgp-out_20
 action permit
```

The trailing `permit` entry with no match is the FRR pattern for "allow everything else"; without it the implicit deny at the end of the route map would drop all unmatched routes.

## 12.11.5. BGP <a href="#pvesdn_bgp" id="pvesdn_bgp"></a>

BGP (Border Gateway Protocol) can be used as an eBGP unnumbered fabric. Each node has its own Autonomous System Number (ASN) and peers with its neighbors over physical interfaces without requiring IP addresses on the fabric links.

Configuration options:

### On the Fabric <a href="#pvesdn_bgp_fabric" id="pvesdn_bgp_fabric"></a>

**IPv4 Prefix**

IPv4 CIDR network range (e.g., 192.0.2.0/24) used to verify that all node IPv4 addresses (BGP router-IDs) are contained within this prefix.

**IPv6 Prefix**

IPv6 CIDR network range (e.g., 2001:db8::/64) used to verify that all node IPv6 addresses in the fabric are contained within this prefix.

**BFD**

Enable Bidirectional Forwarding Detection on all peering sessions in this fabric. BFD provides fast failure detection for links between nodes.

**Route Filter**

A prefix list applied to the fabric peer-group’s inbound direction. When set, this prefix list replaces the implicit "must be within the fabric prefix" filter. Useful to widen the accepted range (e.g. accept additional non-fabric prefixes redistributed via the fabric) or to use a more expressive match. References a prefix list defined under SDN.

**Incoming Route Map**

A route map chained from the fabric peer-group’s implicit inbound filter via FRR’s `call` action. Only prefixes that have already passed the implicit prefix check (or the Route Filter override) reach this route map. Useful to transform or further narrow accepted routes (e.g. adjust community or local-preference), but cannot widen the accepted set. Use Route Filter to override the implicit filter. References a route map defined under SDN.

**Outgoing Route Map**

A route map applied to the fabric peer-group’s outbound direction. Used to transform or filter what is announced to fabric neighbors. References a route map defined under SDN.

**Redistribute**

Which other-protocol routes the BGP router on each node should redistribute into the fabric. Supported sources are `connected`, `kernel`, `static`, and `ospf`. An optional per-source route map can be attached to shape the redistributed routes before they are announced.

{% hint style="info" %}
At least one of IPv4 Prefix or IPv6 Prefix must be configured.
{% endhint %}

### On the Node <a href="#pvesdn_bgp_node" id="pvesdn_bgp_node"></a>

Options that are available on every node that is part of a fabric:

**Node**

Select the node which will be added to the fabric. Only nodes that are currently in the cluster will be shown.

**ASN**

BGP Autonomous System Number for this node. It is recommended to use private ASN numbers (64512-65534 for 16-bit, 4200000000-4294967294 for 32-bit).

**IPv4**

A unique IPv4 address for this node, also used as the BGP router-id. Required when the fabric has an IPv4 prefix configured; each node in the same fabric must have a different address.

**IPv6**

IPv6 address for this node. If only an IPv6 address is configured (without an IPv4 address), the BGP router-id is derived from it via a FNV-1a hash.

**Interfaces**

Specify the interfaces used to establish peering connections with other BGP nodes. These interfaces run BGP unnumbered (no IP address assignment needed). When a node IP is configured, a dummy "loopback" interface is automatically created with that IP.

{% hint style="info" %}
Unlike OSPF and OpenFabric, BGP unnumbered interfaces do not need IP addresses. Peering is established using IPv6 link-local addresses automatically.
{% endhint %}

{% hint style="info" %}
In an eBGP unnumbered fabric, directly peering nodes must have different ASNs for BGP sessions to establish.
{% endhint %}

### Using BGP Fabrics with EVPN <a href="#pvesdn_bgp_evpn" id="pvesdn_bgp_evpn"></a>

When configuring an EVPN controller, a BGP fabric can be selected as the underlay instead of manually specifying peer addresses. The default configuration runs the EVPN overlay (VTEP) sessions as iBGP, using the EVPN controller’s ASN for the router process. The per-node fabric ASN is automatically applied via `local-as` on the underlay neighbor group.

This means the EVPN controller ASN and the per-node fabric ASNs should be different. For example, with three nodes using ASNs 65001, 65002, and 65003 for the underlay, the EVPN controller could use ASN 65000 for the overlay.

Alternatively, setting BGP Mode to "external" on the EVPN controller runs the VTEP sessions as eBGP. The per-node fabric ASN is then used as the local ASN for the VTEP peer-group as well, so the VTEPs naturally peer with each other under different ASNs without needing a separate overlay ASN. The EVPN controller ASN is still used for auto-derived route-target values to keep them consistent across the fabric.

{% hint style="info" %}
Using a BGP fabric for an EVPN underlay requires each node to have an IPv4 address, since EVPN uses it as the VTEP address.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
