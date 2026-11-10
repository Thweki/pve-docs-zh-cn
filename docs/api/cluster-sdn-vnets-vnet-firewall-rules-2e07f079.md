# `/cluster/sdn/vnets/{vnet}/firewall/rules`

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/rules`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets/{vnet}/firewall/rules`

List rules.

**方法标识：** `get_rules`

**权限**

```json
{
  "description": "Needs SDN.Audit or SDN.Allocate permissions on '/sdn/zones/<zone>/<vnet>'",
  "user": "all"
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
| `vnet` | string | 是 | — | The SDN vnet object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "vnet": {
      "description": "The SDN vnet object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
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
  },
  "links": [
    {
      "href": "{pos}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/sdn/vnets/{vnet}/firewall/rules`

Create new rule.

**方法标识：** `create_rule`

**权限**

```json
{
  "description": "Needs SDN.Allocate permissions on '/sdn/zones/<zone>/<vnet>'",
  "user": "all"
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
| `action` | string | 是 | — | Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name. |
| `comment` | string | 否 | — | Descriptive comment. |
| `dest` | string | 否 | — | Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `dport` | string | 否 | — | Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges. |
| `enable` | integer | 否 | — | Flag to enable/disable a rule. |
| `icmp-type` | string | 否 | — | Specify icmp-type. Only valid if proto equals 'icmp' or 'icmpv6'/'ipv6-icmp'. |
| `iface` | string | 否 | — | Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings. |
| `log` | string | 否 | — | Log level for firewall rule.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | string | 否 | — | Use predefined standard macro. |
| `pos` | integer | 否 | — | Update rule at position &lt;pos&gt;. |
| `proto` | string | 否 | — | IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'. |
| `source` | string | 否 | — | Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists. |
| `sport` | string | 否 | — | Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges. |
| `type` | string | 是 | — | Rule type.；可选值：`in`, `out`, `forward`, `group` |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |

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
      "optional": 0,
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
      "optional": 0,
      "type": "string"
    },
    "vnet": {
      "description": "The SDN vnet object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/rules)。
