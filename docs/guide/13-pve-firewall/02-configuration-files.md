# 13.2. Configuration Files <a href="#_configuration_files" id="_configuration_files"></a>

All firewall related configuration is stored on the proxmox cluster file system. So those files are automatically distributed to all cluster nodes, and the `pve-firewall` service updates the underlying `iptables` rules automatically on changes.

You can configure anything using the GUI (i.e. **Datacenter** → **Firewall**, or on a **Node** → **Firewall**), or you can edit the configuration files directly using your preferred editor.

Firewall configuration files contain sections of key-value pairs. Lines beginning with a `#` and blank lines are considered comments. Sections start with a header line containing the section name enclosed in `[` and `]`.

## 13.2.1. Cluster Wide Setup <a href="#pve_firewall_cluster_wide_setup" id="pve_firewall_cluster_wide_setup"></a>

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

### Enabling the Firewall <a href="#_enabling_the_firewall" id="_enabling_the_firewall"></a>

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

## 13.2.2. Host Specific Configuration <a href="#pve_firewall_host_specific_configuration" id="pve_firewall_host_specific_configuration"></a>

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

## 13.2.3. VM/Container Configuration <a href="#pve_firewall_vm_container_configuration" id="pve_firewall_vm_container_configuration"></a>

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

### Enabling the Firewall for VMs and Containers <a href="#_enabling_the_firewall_for_vms_and_containers" id="_enabling_the_firewall_for_vms_and_containers"></a>

Each virtual network device has its own firewall enable flag. So you can selectively enable the firewall for each interface. This is required in addition to the general firewall `enable` option.

## 13.2.4. VNet Configuration <a href="#pve_firewall_vnet_configuration" id="pve_firewall_vnet_configuration"></a>

VNet related configuration is read from:

```text
/etc/pve/sdn/firewall/<vnet_name>.fw
```

This can be used for setting firewall configuration globally on a VNet level, without having to set firewall rules for each VM inside the VNet separately. It can only contain rules for the `FORWARD` direction, since there is no notion of incoming or outgoing traffic. This affects all traffic travelling from one bridge port to another, including the host interface.

{% hint style="warning" %}
This feature is currently only available for the new [nftables-based proxmox-firewall](13-pve-firewall-nft.md)
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

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
