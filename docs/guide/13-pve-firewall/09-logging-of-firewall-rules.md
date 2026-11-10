# 13.9. Logging of firewall rules <a href="#_logging_of_firewall_rules" id="_logging_of_firewall_rules"></a>

By default, all logging of traffic filtered by the firewall rules is disabled. To enable logging, the `loglevel` for incoming and/or outgoing traffic has to be set in **Firewall** → **Options**. This can be done for the host as well as for the VM/CT firewall individually. By this, logging of Proxmox VE’s standard firewall rules is enabled and the output can be observed in **Firewall** → **Log**. Further, only some dropped or rejected packets are logged for the standard rules (see [default firewall rules](08-pve-firewall-default-rules.md#pve_firewall_default_rules)).

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

## 13.9.1. Logging of user defined firewall rules <a href="#_logging_of_user_defined_firewall_rules" id="_logging_of_user_defined_firewall_rules"></a>

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

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
