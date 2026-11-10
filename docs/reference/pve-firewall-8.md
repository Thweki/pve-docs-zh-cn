# pve-firewall(8)

## 名称 <a href="#chapter_pve_firewall" id="chapter_pve_firewall"></a>

pve-firewall \- PVE Firewall Daemon

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pve-firewall"></a>



**pve-firewall** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pve-firewall_compile"></a>



**pve-firewall compile**

Compile and print firewall rules. This is useful for testing.

<a id="cli_pve-firewall_help"></a>



**pve-firewall help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pve-firewall_localnet"></a>



**pve-firewall localnet**

Print information about local network.

<a id="cli_pve-firewall_restart"></a>



**pve-firewall restart**

Restart the Proxmox VE firewall service.

<a id="cli_pve-firewall_simulate"></a>



**pve-firewall simulate** `[OPTIONS]`

Simulate firewall rules. This does not simulates the kernel *routing* table, but simply assumes that routing from source zone to destination zone is possible.

**`--dest` `<string>`**

Destination IP address.

**`--dport` `<integer>`**

Destination port.

**`--from` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` (*default \=* `outside`)**

Source zone.

**`--protocol` `(tcp|udp)` (*default \=* `tcp`)**

Protocol.

**`--source` `<string>`**

Source IP address.

**`--sport` `<integer>`**

Source port.

**`--to` `(host|outside|vm\d+|ct\d+|([a-zA-Z][a-zA-Z0-9]{0,9})/(\S+))` (*default \=* `host`)**

Destination zone.

**`--verbose` `<boolean>`（*默认值 \=* `0`）**

Verbose output.

<a id="cli_pve-firewall_start"></a>



**pve-firewall start** `[OPTIONS]`

Start the Proxmox VE firewall service.

**`--debug` `<boolean>`（*默认 \=* `0`）**

Debug mode \- stay in foreground

<a id="cli_pve-firewall_status"></a>



**pve-firewall status**

Get firewall status.

<a id="cli_pve-firewall_stop"></a>



**pve-firewall stop**

Stop the Proxmox VE firewall service. Note, stopping actively removes all Proxmox VE related iptable rules rendering the host potentially unprotected.

## 描述 <a href="#_description" id="_description"></a>

Proxmox VE Firewall provides an easy way to protect your IT infrastructure. You can setup firewall rules for all hosts inside a cluster, or define rules for virtual machines and containers. Features like firewall macros, security groups, IP sets and aliases help to make that task easier.

While all configuration is stored on the cluster file system, the `iptables`-based firewall service runs on each cluster node, and thus provides full isolation between virtual machines. The distributed nature of this system also provides much higher bandwidth than a central firewall solution.

The firewall has full support for IPv4 and IPv6. IPv6 support is fully transparent, and we filter traffic for both protocols by default. So there is no need to maintain a different set of rules for IPv6.

## Directions \& Zones <a href="#_directions_amp_zones" id="_directions_amp_zones"></a>

The Proxmox VE firewall groups the network into multiple logical zones. You can define rules for each zone independently. Depending on the zone, you can define rules for incoming, outgoing or forwarded traffic.

### Directions <a href="#_directions" id="_directions"></a>

There are 3 directions that you can choose from when defining rules for a zone:

**In**

Traffic that is arriving in a zone.

**Out**

Traffic that is leaving a zone.

**Forward**

Traffic that is passing through a zone. In the host zone this can be routed traffic (when the host is acting as a gateway or performing NAT). At a VNet-level this affects all traffic that is passing by a VNet, including traffic from/to bridged network interfaces.

{% hint style="warning" %}
Creating rules for forwarded traffic is currently only possible when using the new [nftables-based proxmox-firewall](#pve_firewall_nft). Any forward rules will be ignored by the stock `pve-firewall` and have no effect!
{% endhint %}

### Zones <a href="#_zones" id="_zones"></a>

There are 3 different zones that you can define firewall rules for:

**Host**

Traffic going from/to a host, or traffic that is forwarded by a host. You can define rules for this zone either at the datacenter level or at the host level. Rules at host level take precedence over rules at datacenter level.

**VM**

Traffic going from/to a VM or CT. You cannot define rules for forwarded traffic, only for incoming / outgoing traffic.

**VNet**

Traffic passing through a SDN VNet, either from guest to guest or from host to guest and vice-versa. Since this traffic is always forwarded traffic, it is only possible to create rules with direction forward.

{% hint style="warning" %}
Creating rules on a VNet-level is currently only possible when using the new [nftables-based proxmox-firewall](#pve_firewall_nft). Any VNet-level rules will be ignored by the stock `pve-firewall` and have no effect!
{% endhint %}

## Configuration Files <a href="#_configuration_files" id="_configuration_files"></a>

All firewall related configuration is stored on the proxmox cluster file system. So those files are automatically distributed to all cluster nodes, and the `pve-firewall` service updates the underlying `iptables` rules automatically on changes.

You can configure anything using the GUI (i.e. **Datacenter** → **Firewall**, or on a **Node** → **Firewall**), or you can edit the configuration files directly using your preferred editor.

Firewall configuration files contain sections of key-value pairs. Lines beginning with a `#` and blank lines are considered comments. Sections start with a header line containing the section name enclosed in `[` and `]`.

### Cluster Wide Setup <a href="#pve_firewall_cluster_wide_setup" id="pve_firewall_cluster_wide_setup"></a>

The cluster-wide firewall configuration is stored at:

```text
/etc/pve/firewall/cluster.fw
```

The configuration can contain the following sections:

**`[OPTIONS]`**

This is used to set cluster-wide firewall options.

**`ebtables`: `<boolean>` (*default \=* `1`)**

Enable ebtables rules cluster wide.

**`enable`: `<integer> (0 - N)` (*default \=* `0`)**

Enable or disable the firewall cluster wide.

**`log_ratelimit`: `[enable=]<1|0> [,burst=<integer>] [,rate=<rate>]`**

Log ratelimiting settings

**`burst`\=`<integer> (0 - N)` (*default \=* `5`)**

Initial burst of packages which will always get logged before the rate is applied

**`enable`\=`<boolean>` (*default \=* `1`)**

Enable or disable log rate limiting

**`rate`\=`<rate>` (*default \=* `1/second`)**

Frequency with which the burst bucket gets refilled

**`policy_forward`: `<ACCEPT | DROP>`**

Forward policy.

**`policy_in`: `<ACCEPT | DROP | REJECT>`**

Input policy.

**`policy_out`: `<ACCEPT | DROP | REJECT>`**

Output policy.

**`[RULES]`**

This sections contains cluster-wide firewall rules for all nodes.

**`[IPSET <name>]`**

Cluster wide IP set definitions.

**`[GROUP <name>]`**

Cluster wide security group definitions.

**`[ALIASES]`**

Cluster wide Alias definitions.

#### Enabling the Firewall <a href="#_enabling_the_firewall" id="_enabling_the_firewall"></a>

The firewall is completely disabled by default, so you need to set the enable option here:

```text
[OPTIONS]
# enable firewall (cluster-wide setting, default is disabled)
enable: 1
```

{% hint style="warning" %}
If you enable the firewall, traffic to all hosts will be blocked by default \- with some exceptions for traffic coming from the local network to the WebUI, SSH and other important services. A full list of the default firewall rules can be found at xref:pve\_firewall\_default\_rules.
{% endhint %}

Should you have other services running which communicate over the network, you will have to allow them seperately. For some common services there are `macros` available.

If you want to administrate your Proxmox VE hosts from remote, you need to create rules to allow traffic from those remote IPs to the web GUI (port 8006). You may also want to allow ssh (port 22), and maybe SPICE (port 3128).

{% hint style="success" %}
Please open a SSH connection to one of your Proxmox VE hosts before enabling the firewall. That way you still have access to the host if something goes wrong .
{% endhint %}

To simplify that task, you can instead create an IPSet called “management”, and add all remote IPs there. This creates all required firewall rules to access the GUI from remote.

### Host Specific Configuration <a href="#pve_firewall_host_specific_configuration" id="pve_firewall_host_specific_configuration"></a>

Host related configuration is read from:

```text
/etc/pve/nodes/<nodename>/host.fw
```

This is useful if you want to overwrite rules from `cluster.fw` config. You can also increase log verbosity, and set netfilter related options. The configuration can contain the following sections:

**`[OPTIONS]`**

This is used to set host related firewall options.

**`enable`: `<boolean>` (*default \=* `1`)**

Enable host firewall rules.

**`log_level_forward`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for forwarded traffic.

**`log_level_in`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for incoming traffic.

**`log_level_out`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for outgoing traffic.

**`log_nf_conntrack`: `<boolean>` (*default \=* `0`)**

Enable logging of conntrack information.

**`ndp`: `<boolean>` (*default \=* `1`)**

Enable NDP (Neighbor Discovery Protocol).

**`nf_conntrack_allow_invalid`: `<boolean>` (*default \=* `0`)**

Allow invalid packets on connection tracking.

**`nf_conntrack_helpers`: `<string>` (*default \=* \`\`)**

Enable conntrack helpers for specific protocols. Supported protocols: amanda, ftp, irc, netbios-ns, pptp, sane, sip, snmp, tftp

**`nf_conntrack_max`: `<integer> (32768 - N)` (*default \=* `262144`)**

Maximum number of tracked connections.

**`nf_conntrack_tcp_timeout_established`: `<integer> (7875 - N)` (*default \=* `432000`)**

Conntrack established timeout.

**`nf_conntrack_tcp_timeout_syn_recv`: `<integer> (30 - 60)` (*default \=* `60`)**

Conntrack syn recv timeout.

**`nftables`: `<boolean>` (*default \=* `0`)**

Enable nftables based firewall (tech preview)

**`nosmurfs`: `<boolean>`**

Enable SMURFS filter.

**`protection_synflood`: `<boolean>` (*default \=* `0`)**

Enable synflood protection

**`protection_synflood_burst`: `<integer>` (*default \=* `1000`)**

Synflood protection rate burst by ip src.

**`protection_synflood_rate`: `<integer>` (*default \=* `200`)**

Synflood protection rate syn/sec by ip src.

**`smurf_log_level`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for SMURFS filter.

**`tcp_flags_log_level`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for illegal tcp flags filter.

**`tcpflags`: `<boolean>` (*default \=* `0`)**

Filter illegal combinations of TCP flags.

**`[RULES]`**

This sections contains host specific firewall rules.

### VM/Container Configuration <a href="#pve_firewall_vm_container_configuration" id="pve_firewall_vm_container_configuration"></a>

VM firewall configuration is read from:

```text
/etc/pve/firewall/<VMID>.fw
```

and contains the following data:

**`[OPTIONS]`**

This is used to set VM/Container related firewall options.

**`dhcp`: `<boolean>` (*default \=* `0`)**

Enable DHCP.

**`enable`: `<boolean>` (*default \=* `0`)**

Enable/disable firewall rules.

**`ipfilter`: `<boolean>`**

Enable default IP filters. This is equivalent to adding an empty ipfilter-net\<id\> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface’s MAC address. For containers the configured IP addresses will be implicitly added.

**`log_level_in`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for incoming traffic.

**`log_level_out`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for outgoing traffic.

**`macfilter`: `<boolean>` (*default \=* `1`)**

Enable/disable MAC address filter.

**`ndp`: `<boolean>` (*default \=* `1`)**

Enable NDP (Neighbor Discovery Protocol).

**`policy_in`: `<ACCEPT | DROP | REJECT>`**

Input policy.

**`policy_out`: `<ACCEPT | DROP | REJECT>`**

Output policy.

**`radv`: `<boolean>`**

Allow sending Router Advertisement.

**`[RULES]`**

This sections contains VM/Container firewall rules.

**`[IPSET <name>]`**

IP set definitions.

**`[ALIASES]`**

IP Alias definitions.

#### Enabling the Firewall for VMs and Containers <a href="#_enabling_the_firewall_for_vms_and_containers" id="_enabling_the_firewall_for_vms_and_containers"></a>

Each virtual network device has its own firewall enable flag. So you can selectively enable the firewall for each interface. This is required in addition to the general firewall `enable` option.

### VNet Configuration <a href="#pve_firewall_vnet_configuration" id="pve_firewall_vnet_configuration"></a>

VNet related configuration is read from:

```text
/etc/pve/sdn/firewall/<vnet_name>.fw
```

This can be used for setting firewall configuration globally on a VNet level, without having to set firewall rules for each VM inside the VNet separately. It can only contain rules for the `FORWARD` direction, since there is no notion of incoming or outgoing traffic. This affects all traffic travelling from one bridge port to another, including the host interface.

{% hint style="warning" %}
This feature is currently only available for the new [nftables-based proxmox-firewall](#pve_firewall_nft)
{% endhint %}

Since traffic passing the `FORWARD` chain is bi-directional, you need to create rules for both directions if you want traffic to pass both ways. For instance if HTTP traffic for a specific host should be allowed, you would need to create the following rules:

```text
FORWARD ACCEPT -dest 10.0.0.1 -dport 80
FORWARD ACCEPT -source 10.0.0.1 -sport 80
```

**`[OPTIONS]`**

This is used to set VNet related firewall options.

**`enable`: `<boolean>` (*default \=* `0`)**

Enable/disable firewall rules.

**`log_level_forward`: `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for forwarded traffic.

**`policy_forward`: `<ACCEPT | DROP>`**

Forward policy.

**`[RULES]`**

This section contains VNet specific firewall rules.

## Firewall Rules <a href="#_firewall_rules" id="_firewall_rules"></a>

Firewall rules consists of a direction (`IN`, `OUT` or `FORWARD`) and an action (`ACCEPT`, `DENY`, `REJECT`). You can also specify a macro name. Macros contain predefined sets of rules and options. Rules can be disabled by prefixing them with `|`.

**Firewall rules syntax**

```text
[RULES]

DIRECTION ACTION [OPTIONS]
|DIRECTION ACTION [OPTIONS] # disabled rule

DIRECTION MACRO(ACTION) [OPTIONS] # use predefined macro
```

The following options can be used to refine rule matches.

**`--dest` `<string>`**

Restrict packet destination address. This can refer to a single IP address, an IP set (*\+ipsetname*) or an IP alias definition. You can also specify an address range like *20.34.101.207-201.3.9.99*, or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists.

**`--dport` `<string>`**

Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in */etc/services*. Port ranges can be specified with *\\d\+:\\d\+*, for example *80:85*, and you can use comma separated list to match several ports or ranges.

**`--icmp-type` `<string>`**

Specify icmp-type. Only valid if proto equals *icmp* or *icmpv6*/*ipv6-icmp*.

**`--iface` `<string>`**

Network interface name. You have to use network configuration key names for VMs and containers (*net\\d\+*). Host related rules can use arbitrary strings.

**`--log` `<alert | crit | debug | emerg | err | info | nolog | notice | warning>`**

Log level for firewall rule.

**`--proto` `<string>`**

IP protocol. You can use protocol names (*tcp*/*udp*) or simple numbers, as defined in */etc/protocols*.

**`--source` `<string>`**

Restrict packet source address. This can refer to a single IP address, an IP set (*\+ipsetname*) or an IP alias definition. You can also specify an address range like *20.34.101.207-201.3.9.99*, or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists.

**`--sport` `<string>`**

Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in */etc/services*. Port ranges can be specified with *\\d\+:\\d\+*, for example *80:85*, and you can use comma separated list to match several ports or ranges.

Here are some examples:

```text
[RULES]
IN SSH(ACCEPT) -i net0
IN SSH(ACCEPT) -i net0 # a comment
IN SSH(ACCEPT) -i net0 -source 192.168.2.192 # only allow SSH from 192.168.2.192
IN SSH(ACCEPT) -i net0 -source 10.0.0.1-10.0.0.10 # accept SSH for IP range
IN SSH(ACCEPT) -i net0 -source 10.0.0.1,10.0.0.2,10.0.0.3 #accept ssh for IP list
IN SSH(ACCEPT) -i net0 -source +mynetgroup # accept ssh for ipset mynetgroup
IN SSH(ACCEPT) -i net0 -source myserveralias #accept ssh for alias myserveralias

|IN SSH(ACCEPT) -i net0 # disabled rule

IN  DROP # drop all incoming packages
OUT ACCEPT # accept all outgoing packages
```

## Security Groups <a href="#pve_firewall_security_groups" id="pve_firewall_security_groups"></a>

A security group is a collection of rules, defined at cluster level, which can be used in all VMs' rules. For example you can define a group named “webserver” with rules to open the *http* and *https* ports.

```text
# /etc/pve/firewall/cluster.fw

[group webserver]
IN  ACCEPT -p tcp -dport 80
IN  ACCEPT -p tcp -dport 443
```

Then, you can add this group to a VM’s firewall

```text
# /etc/pve/firewall/<VMID>.fw

[RULES]
GROUP webserver
```

## IP Aliases <a href="#pve_firewall_ip_aliases" id="pve_firewall_ip_aliases"></a>

IP Aliases allow you to associate IP addresses of networks with a name. You can then refer to those names:

- inside IP set definitions
- in `source` and `dest` properties of firewall rules

### Standard IP Alias `local_network` <a href="#_standard_ip_alias_span_class_monospaced_local_network_span" id="_standard_ip_alias_span_class_monospaced_local_network_span"></a>

This alias is automatically defined. Please use the following command to see assigned values:

```text
# pve-firewall localnet
local hostname: example
local IP address: 192.168.2.100
network auto detect: 192.168.0.0/20
using detected local_network: 192.168.0.0/20
```

The firewall automatically sets up rules to allow everything needed for cluster communication (corosync, API, SSH) using this alias.

The user can overwrite these values in the `cluster.fw` alias section. If you use a single host on a public network, it is better to explicitly assign the local IP address

```text
#  /etc/pve/firewall/cluster.fw
[ALIASES]
local_network 1.2.3.4 # use the single IP address
```

## IP Sets <a href="#pve_firewall_ip_sets" id="pve_firewall_ip_sets"></a>

IP sets can be used to define groups of networks and hosts. You can refer to them with ‘\+name\` in the firewall rules’ `source` and `dest` properties.

The following example allows HTTP traffic from the `management` IP set.

```text
IN HTTP(ACCEPT) -source +management
```

### Standard IP set `management` <a href="#_standard_ip_set_span_class_monospaced_management_span" id="_standard_ip_set_span_class_monospaced_management_span"></a>

This IP set applies only to host firewalls (not VM firewalls). Those IPs are allowed to do normal management tasks (Proxmox VE GUI, VNC, SPICE, SSH).

The local cluster network is automatically added to this IP set (alias `cluster_network`), to enable inter-host cluster communication. (multicast,ssh,…)

```text
# /etc/pve/firewall/cluster.fw

[IPSET management]
192.168.2.10
192.168.2.10/24
```

### Standard IP set `blacklist` <a href="#_standard_ip_set_span_class_monospaced_blacklist_span" id="_standard_ip_set_span_class_monospaced_blacklist_span"></a>

Traffic from these IPs is dropped by every host’s and VM’s firewall.

```text
# /etc/pve/firewall/cluster.fw

[IPSET blacklist]
77.240.159.182
213.87.123.0/24
```

### Standard IP set `ipfilter-net*` <a href="#pve_firewall_ipfilter_section" id="pve_firewall_ipfilter_section"></a>

These filters belong to a VM’s network interface and are mainly used to prevent IP spoofing. If such a set exists for an interface then any outgoing traffic with a source IP not matching its interface’s corresponding ipfilter set will be dropped.

For containers with configured IP addresses these sets, if they exist (or are activated via the general `IP Filter` option in the VM’s firewall’s **options** tab), implicitly contain the associated IP addresses.

For both virtual machines and containers they also implicitly contain the standard MAC-derived IPv6 link-local address in order to allow the neighbor discovery protocol to work.

```text
/etc/pve/firewall/<VMID>.fw

[IPSET ipfilter-net0] # only allow specified IPs on net0
192.168.2.10
```

## Services and Commands <a href="#pve_firewall_services_commands" id="pve_firewall_services_commands"></a>

The firewall runs two service daemons on each node:

- pvefw-logger: NFLOG daemon (ulogd replacement).
- pve-firewall: updates iptables rules

There is also a CLI command named `pve-firewall`, which can be used to start and stop the firewall service:

```text
# pve-firewall start
# pve-firewall stop
```

To get the status use:

```text
# pve-firewall status
```

The above command reads and compiles all firewall rules, so you will see warnings if your firewall configuration contains any errors.

If you want to see the generated iptables rules you can use:

```text
# iptables-save
```

## Default firewall rules <a href="#pve_firewall_default_rules" id="pve_firewall_default_rules"></a>

The following traffic is filtered by the default firewall configuration:

### Datacenter incoming/outgoing DROP/REJECT <a href="#_datacenter_incoming_outgoing_drop_reject" id="_datacenter_incoming_outgoing_drop_reject"></a>

If the input or output policy for the firewall is set to DROP or REJECT, the following traffic is still allowed for all Proxmox VE hosts in the cluster:

- traffic over the loopback interface
- already established connections
- traffic using the IGMP protocol
- TCP traffic from management hosts to port 8006 in order to allow access to the web interface
- TCP traffic from management hosts to the port range 5900 to 5999 allowing traffic for the VNC web console
- TCP traffic from management hosts to port 3128 for connections to the SPICE proxy
- TCP traffic from management hosts to port 22 to allow ssh access
- TCP traffic from management hots to the port range 60000 to 60050 allowing traffic for migrations
- UDP traffic in the cluster network to ports 5405-5412 for corosync
- UDP multicast traffic in the cluster network
- ICMP traffic type 3 (Destination Unreachable), 4 (congestion control) or 11 (Time Exceeded)

The following traffic is dropped, but not logged even with logging enabled:

- TCP connections with invalid connection state
- Broadcast, multicast and anycast traffic not related to corosync, i.e., not coming through ports 5405-5412
- TCP traffic to port 43
- UDP traffic to ports 135 and 445
- UDP traffic to the port range 137 to 139
- UDP traffic form source port 137 to port range 1024 to 65535
- UDP traffic to port 1900
- TCP traffic to port 135, 139 and 445
- UDP traffic originating from source port 53

The rest of the traffic is dropped or rejected, respectively, and also logged. This may vary depending on the additional options enabled in **Firewall** → **Options**, such as NDP, SMURFS and TCP flag filtering.

<a id="pve_firewall_iptables_inspect"></a>



Please inspect the output of the

```text
 # iptables-save
```

system command to see the firewall chains and rules active on your system. This output is also included in a `System Report`, accessible over a node’s subscription tab in the web GUI, or through the `pvereport` command-line tool.

### VM/CT incoming/outgoing DROP/REJECT <a href="#_vm_ct_incoming_outgoing_drop_reject" id="_vm_ct_incoming_outgoing_drop_reject"></a>

This drops or rejects all the traffic to the VMs, with some exceptions for DHCP, NDP, Router Advertisement, MAC and IP filtering depending on the set configuration. The same rules for dropping/rejecting packets are inherited from the datacenter, while the exceptions for accepted incoming/outgoing traffic of the host do not apply.

Again, you can use [iptables-save (see above)](#pve_firewall_iptables_inspect) to inspect all rules and chains applied.

## Logging of firewall rules <a href="#_logging_of_firewall_rules" id="_logging_of_firewall_rules"></a>

By default, all logging of traffic filtered by the firewall rules is disabled. To enable logging, the `loglevel` for incoming and/or outgoing traffic has to be set in **Firewall** → **Options**. This can be done for the host as well as for the VM/CT firewall individually. By this, logging of Proxmox VE’s standard firewall rules is enabled and the output can be observed in **Firewall** → **Log**. Further, only some dropped or rejected packets are logged for the standard rules (see [default firewall rules](#pve_firewall_default_rules)).

`loglevel` does not affect how much of the filtered traffic is logged. It changes a `LOGID` appended as prefix to the log output for easier filtering and post-processing.

`loglevel` is one of the following flags:

<table id="pve_firewall_log_levels">


<thead>
<tr>
<th>loglevel</th>
<th>LOGID</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>nolog</p></td>
<td><p> — </p></td>
</tr>
<tr>
<td><p>emerg</p></td>
<td><p>0</p></td>
</tr>
<tr>
<td><p>alert</p></td>
<td><p>1</p></td>
</tr>
<tr>
<td><p>crit</p></td>
<td><p>2</p></td>
</tr>
<tr>
<td><p>err</p></td>
<td><p>3</p></td>
</tr>
<tr>
<td><p>warning</p></td>
<td><p>4</p></td>
</tr>
<tr>
<td><p>notice</p></td>
<td><p>5</p></td>
</tr>
<tr>
<td><p>info</p></td>
<td><p>6</p></td>
</tr>
<tr>
<td><p>debug</p></td>
<td><p>7</p></td>
</tr>
</tbody>
</table>

A typical firewall log output looks like this:

```text
VMID LOGID CHAIN TIMESTAMP POLICY: PACKET_DETAILS
```

In case of the host firewall, `VMID` is equal to 0\.

### Logging of user defined firewall rules <a href="#_logging_of_user_defined_firewall_rules" id="_logging_of_user_defined_firewall_rules"></a>

In order to log packets filtered by user-defined firewall rules, it is possible to set a log-level parameter for each rule individually. This allows to log in a fine grained manner and independent of the log-level defined for the standard rules in **Firewall** → **Options**.

While the `loglevel` for each individual rule can be defined or changed easily in the web UI during creation or modification of the rule, it is possible to set this also via the corresponding `pvesh` API calls.

Further, the log-level can also be set via the firewall configuration file by appending a `-log <loglevel>` to the selected rule (see [possible log-levels](#pve_firewall_log_levels)).

For example, the following two are identical:

```text
IN REJECT -p icmp -log nolog
IN REJECT -p icmp
```

whereas

```text
IN REJECT -p icmp -log debug
```

produces a log output flagged with the `debug` level.

## Tips and Tricks <a href="#_tips_and_tricks" id="_tips_and_tricks"></a>

### How to allow FTP <a href="#_how_to_allow_ftp" id="_how_to_allow_ftp"></a>

FTP is an old style protocol which uses port 21 and several other dynamic ports. So you need a rule to accept port 21\. In addition, you need to load the `ip_conntrack_ftp` module. So please run:

```text
modprobe ip_conntrack_ftp
```

and add `ip_conntrack_ftp` to `/etc/modules` (so that it works after a reboot).

### Suricata IPS integration <a href="#_suricata_ips_integration" id="_suricata_ips_integration"></a>

If you want to use the [Suricata IPS](https://suricata.io/) (Intrusion Prevention System), it’s possible.

Packets will be forwarded to the IPS only after the firewall ACCEPTed them.

Rejected/Dropped firewall packets don’t go to the IPS.

Install suricata on proxmox host:

```text
# apt-get install suricata
# modprobe nfnetlink_queue
```

Don’t forget to add `nfnetlink_queue` to `/etc/modules` for next reboot.

Then, enable IPS for a specific VM with:

```text
# /etc/pve/firewall/<VMID>.fw

[OPTIONS]
ips: 1
ips_queues: 0
```

`ips_queues` will bind a specific cpu queue for this VM.

Available queues are defined in

```text
# /etc/default/suricata
NFQUEUE=0
```

## Notes on IPv6 <a href="#_notes_on_ipv6" id="_notes_on_ipv6"></a>

The firewall contains a few IPv6 specific options. One thing to note is that IPv6 does not use the ARP protocol anymore, and instead uses NDP (Neighbor Discovery Protocol) which works on IP level and thus needs IP addresses to succeed. For this purpose link-local addresses derived from the interface’s MAC address are used. By default the `NDP` option is enabled on both host and VM level to allow neighbor discovery (NDP) packets to be sent and received.

Beside neighbor discovery NDP is also used for a couple of other things, like auto-configuration and advertising routers.

By default VMs are allowed to send out router solicitation messages (to query for a router), and to receive router advertisement packets. This allows them to use stateless auto configuration. On the other hand VMs cannot advertise themselves as routers unless the “Allow Router Advertisement” (`radv: 1`) option is set.

As for the link local addresses required for NDP, there’s also an “IP Filter” (`ipfilter: 1`) option which can be enabled which has the same effect as adding an `ipfilter-net*` ipset for each of the VM’s network interfaces containing the corresponding link local addresses. (See the [Standard IP set `ipfilter-net*`](#pve_firewall_ipfilter_section) section for details.)

## Ports used by Proxmox VE <a href="#_ports_used_by_proxmox_ve" id="_ports_used_by_proxmox_ve"></a>

- Web interface: 8006 (TCP, HTTP/1.1 over TLS)
- VNC Web console: 5900-5999 (TCP, WebSocket)
- SPICE proxy: 3128 (TCP)
- sshd (used for cluster actions): 22 (TCP)
- rpcbind: 111 (UDP)
- sendmail: 25 (TCP, outgoing)
- corosync cluster traffic: 5405-5412 UDP
- live migration (VM memory and local-disk data): 60000-60050 (TCP)

## nftables <a href="#pve_firewall_nft" id="pve_firewall_nft"></a>

As an alternative to `pve-firewall` we offer `proxmox-firewall`, which is an implementation of the Proxmox VE firewall based on the newer [nftables](https://wiki.nftables.org/wiki-nftables/index.php/What_is_nftables%3F) rather than iptables.

{% hint style="warning" %}
`proxmox-firewall` is currently in tech preview. There might be bugs or incompatibilities with the original firewall. It is currently not suited for production use.
{% endhint %}

This implementation uses the same configuration files and configuration format, so you can use your old configuration when switching. It provides the exact same functionality with a few exceptions:

- When using Linux bridges, no additional firewall bridges (fwbrX) will be created. Guest interfaces using OVS bridges will still have firewall bridges.
- REJECT is currently not possible for guest traffic (traffic will instead be dropped).
- Using the `NDP`, `Router Advertisement` or `DHCP` options will **always** create firewall rules, irregardless of your default policy.
- firewall rules for guests are evaluated even for connections that have conntrack table entries.

### Installation and Usage <a href="#_installation_and_usage" id="_installation_and_usage"></a>

Install the `proxmox-firewall` package:

```text
apt install proxmox-firewall
```

Enable the nftables backend via the Web UI on your hosts (Host \> Firewall \> Options \> nftables), or by enabling it in the configuration file for your hosts (`/etc/pve/nodes/<node_name>/host.fw`):

```text
[OPTIONS]

nftables: 1
```

{% hint style="info" %}
After enabling/disabling `proxmox-firewall`, all running VMs and containers need to be restarted for the old/new firewall to work properly.
{% endhint %}

After setting the `nftables` configuration key, the new `proxmox-firewall` service will take over. You can check if the new service is working by checking the systemctl status of `proxmox-firewall`:

```text
systemctl status proxmox-firewall
```

You can also examine the generated ruleset. You can find more information about this in the section [Helpful Commands](#pve_firewall_nft_helpful_commands). You should also check whether `pve-firewall` is no longer generating iptables rules, you can find the respective commands in the [Services and Commands](#pve_firewall_services_commands) section.

Switching back to the old firewall can be done by simply setting the configuration value back to 0 / No.

### Usage <a href="#_usage" id="_usage"></a>

`proxmox-firewall` will create two tables that are managed by the `proxmox-firewall` service: `proxmox-firewall` and `proxmox-firewall-guests`. If you want to create custom rules that live outside the Proxmox VE firewall configuration you can create your own tables to manage your custom firewall rules. `proxmox-firewall` will only touch the tables it generates, so you can easily extend and modify the behavior of the `proxmox-firewall` by adding your own tables.

Instead of using the `pve-firewall` command, the nftables-based firewall uses `proxmox-firewall`. It is a systemd service, so you can start and stop it via `systemctl`:

```text
systemctl start proxmox-firewall
systemctl stop proxmox-firewall
```

Stopping the firewall service will remove all generated rules.

To query the status of the firewall, you can query the status of the systemctl service:

```text
systemctl status proxmox-firewall
```

### Helpful Commands <a href="#pve_firewall_nft_helpful_commands" id="pve_firewall_nft_helpful_commands"></a>

You can check the generated ruleset via the following command:

```text
nft list ruleset
```

If you want to debug `proxmox-firewall` you can dump the commands generated by the firewall via the `compile` subcommand. Additionally, setting the PVE\_LOG environment variable will print log output to STDERR, which can be useful for debugging issues during the generation of the nftables ruleset:

```text
PVE_LOG=trace /usr/libexec/proxmox/proxmox-firewall compile > firewall.json
```

The nftables ruleset consists of the skeleton ruleset, that is included in the proxmox-firewall binary, as well as the rules generated from the firewall configuration. You can obtain the base ruleset via the `skeleton` subcommand:

```text
/usr/libexec/proxmox/proxmox-firewall skeleton
```

The output of both commands can be piped directly to the `nft` executable. The following commands will re-create the whole nftables ruleset from scratch:

```text
/usr/libexec/proxmox/proxmox-firewall skeleton | nft -f -
/usr/libexec/proxmox/proxmox-firewall compile | nft -j -f -
```

You can also edit the systemctl service if you want to have detailed output for your firewall daemon while it is running:

```text
systemctl edit proxmox-firewall
```

Then you need to add the override for the `PVE_LOG` environment variable:

```text
[Service]
Environment="PVE_LOG=trace"
```

This will generate a large amount of logs very quickly, so only use this for debugging purposes. Other, less verbose, log levels are `info` and `debug`.

It can be helpful to trace packet flow through the different chains in order to debug firewall rules. This can be achieved by setting `nftrace` to 1 for packets that you want to track. It is advisable that you do not set this flag for **all** packets, in the example below we only examine ICMP packets.

```text
#!/usr/sbin/nft -f
table bridge tracebridge
delete table bridge tracebridge

table bridge tracebridge {
    chain trace {
        meta l4proto icmp meta nftrace set 1
    }

    chain prerouting {
        type filter hook prerouting priority -350; policy accept;
        jump trace
    }

    chain postrouting {
        type filter hook postrouting priority -350; policy accept;
        jump trace
    }
}
```

Saving this file, making it executable, and then running it once will create the respective tracing chains. You can then inspect the tracing output via the Proxmox VE Web UI (Firewall \> Log) or via `nft monitor trace`.

The above example traces traffic on all bridges, which is usually where guest traffic flows through. If you want to examine host traffic, create those chains in the `inet` table instead of the `bridge` table.

{% hint style="info" %}
Be aware that this can generate a **lot** of log spam and slow down the performance of your networking stack significantly.
{% endhint %}

You can remove the tracing rules via running the following command:

```text
nft delete table bridge tracebridge
```

## Macro Definitions <a href="#_macro_definitions" id="_macro_definitions"></a>

<table>
<tr>
<td><em>Amanda</em> <br/></td>
<td>
<p>Amanda Backup</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>10080</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>10080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Auth</em> <br/></td>
<td>
<p>Auth (identd) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>113</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BGP</em> <br/></td>
<td>
<p>Border Gateway Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>179</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BitTorrent</em> <br/></td>
<td>
<p>BitTorrent traffic for BitTorrent 3.1 and earlier</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6881:6889</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>6881</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BitTorrent32</em> <br/></td>
<td>
<p>BitTorrent traffic for BitTorrent 3.2 and later</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6881:6999</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>6881</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>CVS</em> <br/></td>
<td>
<p>Concurrent Versions System pserver traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2401</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Ceph</em> <br/></td>
<td>
<p>Ceph Storage Cluster traffic (Ceph Monitors, OSD &amp; MDS Daemons)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6789</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3300</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6800:7300</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Citrix</em> <br/></td>
<td>
<p>Citrix/ICA traffic (ICA, ICA Browser, CGP)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1494</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1604</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2598</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DAAP</em> <br/></td>
<td>
<p>Digital Audio Access Protocol traffic (iTunes, Rythmbox daemons)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3689</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3689</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DCC</em> <br/></td>
<td>
<p>Distributed Checksum Clearinghouse spam filtering mechanism</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6277</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DHCPfwd</em> <br/></td>
<td>
<p>Forwarded DHCP traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>67:68</p></td>
<td><p>67:68</p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DHCPv6</em> <br/></td>
<td>
<p>DHCPv6 traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>546:547</p></td>
<td><p>546:547</p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DNS</em> <br/></td>
<td>
<p>Domain Name System traffic (upd and tcp)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>53</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>53</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Distcc</em> <br/></td>
<td>
<p>Distributed Compiler service</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3632</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>FTP</em> <br/></td>
<td>
<p>File Transfer Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>21</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Finger</em> <br/></td>
<td>
<p>Finger protocol (RFC 742)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>79</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>GNUnet</em> <br/></td>
<td>
<p>GNUnet secure peer-to-peer networking traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2086</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>2086</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1080</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>GRE</em> <br/></td>
<td>
<p>Generic Routing Encapsulation tunneling protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>47</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Git</em> <br/></td>
<td>
<p>Git distributed revision control traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>9418</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HKP</em> <br/></td>
<td>
<p>OpenPGP HTTP key server protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>11371</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HTTP</em> <br/></td>
<td>
<p>Hypertext Transfer Protocol (WWW)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>80</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HTTPS</em> <br/></td>
<td>
<p>Hypertext Transfer Protocol (WWW) over SSL</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>443</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>ICPV2</em> <br/></td>
<td>
<p>Internet Cache Protocol V2 (Squid) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3130</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>ICQ</em> <br/></td>
<td>
<p>AOL Instant Messenger traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5190</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IMAP</em> <br/></td>
<td>
<p>Internet Message Access Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>143</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IMAPS</em> <br/></td>
<td>
<p>Internet Message Access Protocol over SSL</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>993</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPIP</em> <br/></td>
<td>
<p>IPIP capsulation traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>94</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsec</em> <br/></td>
<td>
<p>IPsec traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p>500</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>50</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsecah</em> <br/></td>
<td>
<p>IPsec authentication (AH) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p>500</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>51</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsecnat</em> <br/></td>
<td>
<p>IPsec traffic and Nat-Traversal</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>4500</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>50</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IRC</em> <br/></td>
<td>
<p>Internet Relay Chat traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6667</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Jetdirect</em> <br/></td>
<td>
<p>HP Jetdirect printing</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>9100</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>L2TP</em> <br/></td>
<td>
<p>Layer 2 Tunneling Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1701</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>LDAP</em> <br/></td>
<td>
<p>Lightweight Directory Access Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>389</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>LDAPS</em> <br/></td>
<td>
<p>Secure Lightweight Directory Access Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>636</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MDNS</em> <br/></td>
<td>
<p>Multicast DNS</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5353</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MSNP</em> <br/></td>
<td>
<p>Microsoft Notification Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1863</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MSSQL</em> <br/></td>
<td>
<p>Microsoft SQL Server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1433</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Mail</em> <br/></td>
<td>
<p>Mail traffic (SMTP, SMTPS, Submission)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>25</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>465</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>587</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Munin</em> <br/></td>
<td>
<p>Munin networked resource monitoring traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>4949</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MySQL</em> <br/></td>
<td>
<p>MySQL server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3306</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NNTP</em> <br/></td>
<td>
<p>NNTP traffic (Usenet).</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>119</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NNTPS</em> <br/></td>
<td>
<p>Encrypted NNTP traffic (Usenet)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>563</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NTP</em> <br/></td>
<td>
<p>Network Time Protocol (ntpd)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>123</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NeighborDiscovery</em> <br/></td>
<td>
<p>IPv6 neighbor solicitation, neighbor and router advertisement</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>router-solicitation</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>router-advertisement</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>neighbor-solicitation</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>neighbor-advertisement</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>OSPF</em> <br/></td>
<td>
<p>OSPF multicast traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>89</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>OpenVPN</em> <br/></td>
<td>
<p>OpenVPN traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1194</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PCA</em> <br/></td>
<td>
<p>Symantec PCAnywere (tm)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5632</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5631</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PMG</em> <br/></td>
<td>
<p>Proxmox Mail Gateway web interface</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>8006</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>POP3</em> <br/></td>
<td>
<p>POP3 traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>110</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>POP3S</em> <br/></td>
<td>
<p>Encrypted POP3 traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>995</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PPtP</em> <br/></td>
<td>
<p>Point-to-Point Tunneling Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>47</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1723</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Ping</em> <br/></td>
<td>
<p>ICMP echo request</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>icmp</p></td>
<td><p>echo-request</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PostgreSQL</em> <br/></td>
<td>
<p>PostgreSQL server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5432</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Printer</em> <br/></td>
<td>
<p>Line Printer protocol printing</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>515</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RDP</em> <br/></td>
<td>
<p>Microsoft Remote Desktop Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3389</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RIP</em> <br/></td>
<td>
<p>Routing Information Protocol (bidirectional)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>520</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RNDC</em> <br/></td>
<td>
<p>BIND remote management protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>953</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Razor</em> <br/></td>
<td>
<p>Razor Antispam System</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2703</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Rdate</em> <br/></td>
<td>
<p>Remote time retrieval (rdate)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>37</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Rsync</em> <br/></td>
<td>
<p>Rsync server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>873</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SANE</em> <br/></td>
<td>
<p>SANE network scanning</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6566</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMB</em> <br/></td>
<td>
<p>Microsoft SMB traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>135,445</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>137:139</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1024:65535</p></td>
<td><p>137</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>135,139,445</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMBswat</em> <br/></td>
<td>
<p>Samba Web Administration Tool</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>901</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMTP</em> <br/></td>
<td>
<p>Simple Mail Transfer Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>25</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMTPS</em> <br/></td>
<td>
<p>Encrypted Simple Mail Transfer Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>465</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SNMP</em> <br/></td>
<td>
<p>Simple Network Management Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>161:162</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>161</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SPAMD</em> <br/></td>
<td>
<p>Spam Assassin SPAMD traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>783</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SPICEproxy</em> <br/></td>
<td>
<p>Proxmox VE SPICE display proxy traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3128</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SSH</em> <br/></td>
<td>
<p>Secure shell traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>22</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SVN</em> <br/></td>
<td>
<p>Subversion server (svnserve)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3690</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SixXS</em> <br/></td>
<td>
<p>SixXS IPv6 Deployment and Tunnel Broker</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3874</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3740</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>41</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5072,8374</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Squid</em> <br/></td>
<td>
<p>Squid web proxy traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3128</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Submission</em> <br/></td>
<td>
<p>Mail message submission traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>587</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Syslog</em> <br/></td>
<td>
<p>Syslog protocol (RFC 5424) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>514</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>514</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>TFTP</em> <br/></td>
<td>
<p>Trivial File Transfer Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>69</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Telnet</em> <br/></td>
<td>
<p>Telnet traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>23</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Telnets</em> <br/></td>
<td>
<p>Telnet over SSL</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>992</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Time</em> <br/></td>
<td>
<p>RFC 868 Time protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>37</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Trcrt</em> <br/></td>
<td>
<p>Traceroute (for up to 30 hops) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>33434:33524</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmp</p></td>
<td><p>echo-request</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>VNC</em> <br/></td>
<td>
<p>VNC traffic for VNC display’s 0 - 99</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5900:5999</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>VNCL</em> <br/></td>
<td>
<p>VNC traffic from Vncservers to Vncviewers in listen mode</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5500</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Web</em> <br/></td>
<td>
<p>WWW traffic (HTTP and HTTPS)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>80</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>443</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Webcache</em> <br/></td>
<td>
<p>Web Cache/Proxy traffic (port 8080)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>8080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Webmin</em> <br/></td>
<td>
<p>Webmin traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>10000</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Whois</em> <br/></td>
<td>
<p>Whois (nicname, RFC 3912) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>43</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-firewall.8.html) · 版本 9.2.13 · 非官方中文翻译。
