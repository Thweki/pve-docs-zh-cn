# 13.9. 防火墙规则日志记录 <a href="#logging_of_firewall_rules" id="logging_of_firewall_rules"></a>

默认情况下，禁用所有由防火墙规则过滤的流量的日志记录。要启用日志记录，必须设置传入和/或传出流量的 `loglevel`，位置为 **防火墙** → **选项**。可以分别对宿主机及虚拟机/容器防火墙进行设置。这样会启用 Proxmox VE 标准防火墙规则的日志记录，输出可在 **防火墙** → **日志** 中查看。此外，标准规则仅记录部分被丢弃或拒绝的数据包（参见 [默认防火墙规则](08-pve-firewall-default-rules.md)）。

`loglevel` 不影响记录多少被过滤的流量。它会更改作为前缀附加到日志输出的 `LOGID`，以便过滤和后续处理。

`loglevel` 是以下标志之一：

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

典型的防火墙日志输出如下所示：

```text
VMID LOGID CHAIN TIMESTAMP POLICY: PACKET_DETAILS
```

对于宿主机防火墙，`VMID` 等于 0。

## 13.9.1. 用户定义防火墙规则的日志记录 <a href="#logging_of_user_defined_firewall_rules" id="logging_of_user_defined_firewall_rules"></a>

要记录被用户定义防火墙规则过滤的数据包，可以为每条规则单独设置 log-level 参数。这支持精细的日志记录，并且独立于在 **防火墙** → **选项** 中为标准规则定义的日志级别。

每条规则的 `loglevel` 可以在创建或修改规则时通过 Web UI 轻松定义或更改，也可以通过相应的 `pvesh` API 调用设置。

此外，也可以通过防火墙配置文件设置日志级别，在所选规则后附加 `-log <loglevel>`（参见 [可用日志级别](09-logging-of-firewall-rules.md)）。

例如，以下两项等价：

```text
IN REJECT -p icmp -log nolog
IN REJECT -p icmp
```

而

```text
IN REJECT -p icmp -log debug
```

会生成标记为 `debug` 级别的日志输出。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
