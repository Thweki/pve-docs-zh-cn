# `/nodes/{node}/qemu/{vmid}/firewall/rules/{pos}`

原始接口路径：`/nodes/{node}/qemu/{vmid}/firewall/rules/{pos}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/qemu/{vmid}/firewall/rules/{pos}`

Delete rule.

**方法标识：** `delete_rule`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Network"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

**代理目标**

```json
null
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `node` | string | 是 | — | The cluster node name. |
| `pos` | integer | 否 | — | Update rule at position &lt;pos&gt;. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pos": {
      "description": "Update rule at position <pos>.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## GET `/nodes/{node}/qemu/{vmid}/firewall/rules/{pos}`

Get single rule data.

**方法标识：** `get_rule`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**代理目标**

```json
null
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `pos` | integer | 否 | — | Update rule at position &lt;pos&gt;. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pos": {
      "description": "Update rule at position <pos>.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "action": {
      "description": "Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name",
      "type": "string"
    },
    "comment": {
      "description": "Descriptive comment",
      "optional": 1,
      "type": "string"
    },
    "dest": {
      "description": "Restrict packet destination address",
      "optional": 1,
      "type": "string"
    },
    "dport": {
      "description": "Restrict TCP/UDP destination port",
      "optional": 1,
      "type": "string"
    },
    "enable": {
      "description": "Flag to enable/disable a rule",
      "optional": 1,
      "type": "integer"
    },
    "icmp-type": {
      "description": "Specify icmp-type. Only valid if proto equals 'icmp' or 'icmpv6'/'ipv6-icmp'",
      "optional": 1,
      "type": "string"
    },
    "iface": {
      "description": "Network interface name. You have to use network configuration key names for VMs and containers",
      "optional": 1,
      "type": "string"
    },
    "ipversion": {
      "description": "IP version (4 or 6) - automatically determined from source/dest addresses",
      "optional": 1,
      "type": "integer"
    },
    "log": {
      "description": "Log level for firewall rule",
      "enum": [
        "emerg",
        "alert",
        "crit",
        "err",
        "warning",
        "notice",
        "info",
        "debug",
        "nolog"
      ],
      "optional": 1,
      "type": "string"
    },
    "macro": {
      "description": "Use predefined standard macro",
      "optional": 1,
      "type": "string"
    },
    "pos": {
      "description": "Rule position in the ruleset",
      "type": "integer"
    },
    "proto": {
      "description": "IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'",
      "optional": 1,
      "type": "string"
    },
    "source": {
      "description": "Restrict packet source address",
      "optional": 1,
      "type": "string"
    },
    "sport": {
      "description": "Restrict TCP/UDP source port",
      "optional": 1,
      "type": "string"
    },
    "type": {
      "description": "Rule type",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/qemu/{vmid}/firewall/rules/{pos}`

Modify rule data.

**方法标识：** `update_rule`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Network"
    ]
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

**代理目标**

```json
null
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `action` | string | 否 | — | Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name. |
| `comment` | string | 否 | — | Descriptive comment. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `dest` | string | 否 | — | Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `dport` | string | 否 | — | Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges. |
| `enable` | integer | 否 | — | Flag to enable/disable a rule. |
| `icmp-type` | string | 否 | — | Specify icmp-type. Only valid if proto equals 'icmp' or 'icmpv6'/'ipv6-icmp'. |
| `iface` | string | 否 | — | Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings. |
| `log` | string | 否 | — | Log level for firewall rule.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | string | 否 | — | Use predefined standard macro. |
| `moveto` | integer | 否 | — | Move rule to new position &lt;moveto&gt;. Other arguments are ignored. |
| `node` | string | 是 | — | The cluster node name. |
| `pos` | integer | 否 | — | Update rule at position &lt;pos&gt;. |
| `proto` | string | 否 | — | IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'. |
| `source` | string | 否 | — | Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists. |
| `sport` | string | 否 | — | Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges. |
| `type` | string | 否 | — | Rule type.；可选值：`in`, `out`, `forward`, `group` |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name.",
      "maxLength": 20,
      "minLength": 2,
      "optional": 1,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
      "type": "string"
    },
    "comment": {
      "description": "Descriptive comment.",
      "format": "pve-fw-comment-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dest": {
      "description": "Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists.",
      "format": "pve-fw-addr-spec",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dport": {
      "description": "Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\\d+:\\d+', for example '80:85', and you can use comma separated list to match several ports or ranges.",
      "format": "pve-fw-dport-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "description": "Flag to enable/disable a rule.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "icmp-type": {
      "description": "Specify icmp-type. Only valid if proto equals 'icmp' or 'icmpv6'/'ipv6-icmp'.",
      "format": "pve-fw-icmp-type-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "iface": {
      "description": "Network interface name. You have to use network configuration key names for VMs and containers ('net\\d+'). Host related rules can use arbitrary strings.",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "log": {
      "description": "Log level for firewall rule.",
      "enum": [
        "emerg",
        "alert",
        "crit",
        "err",
        "warning",
        "notice",
        "info",
        "debug",
        "nolog"
      ],
      "optional": 1,
      "type": "string"
    },
    "macro": {
      "description": "Use predefined standard macro.",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "moveto": {
      "description": "Move rule to new position <moveto>. Other arguments are ignored.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "pos": {
      "description": "Update rule at position <pos>.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "proto": {
      "description": "IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'.",
      "format": "pve-fw-protocol-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "source": {
      "description": "Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists.",
      "format": "pve-fw-addr-spec",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "sport": {
      "description": "Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\\d+:\\d+', for example '80:85', and you can use comma separated list to match several ports or ranges.",
      "format": "pve-fw-sport-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "Rule type.",
      "enum": [
        "in",
        "out",
        "forward",
        "group"
      ],
      "optional": 1,
      "type": "string"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/firewall/rules/{pos})。
