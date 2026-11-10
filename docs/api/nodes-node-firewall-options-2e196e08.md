# `/nodes/{node}/firewall/options`

原始接口路径：`/nodes/{node}/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/firewall/options`

Get host firewall options.

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Audit"
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
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |

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
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "enable": {
      "default": 1,
      "description": "Enable host firewall rules.",
      "optional": 1,
      "type": "boolean"
    },
    "log_level_forward": {
      "description": "Log level for forwarded traffic.",
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
    "log_level_in": {
      "description": "Log level for incoming traffic.",
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
    "log_level_out": {
      "description": "Log level for outgoing traffic.",
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
    "log_nf_conntrack": {
      "default": 0,
      "description": "Enable logging of conntrack information.",
      "optional": 1,
      "type": "boolean"
    },
    "ndp": {
      "default": 1,
      "description": "Enable NDP (Neighbor Discovery Protocol).",
      "optional": 1,
      "type": "boolean"
    },
    "nf_conntrack_allow_invalid": {
      "default": 0,
      "description": "Allow invalid packets on connection tracking.",
      "optional": 1,
      "type": "boolean"
    },
    "nf_conntrack_helpers": {
      "default": "",
      "description": "Enable conntrack helpers for specific protocols. Supported protocols: amanda, ftp, irc, netbios-ns, pptp, sane, sip, snmp, tftp",
      "format": "pve-fw-conntrack-helper",
      "optional": 1,
      "type": "string"
    },
    "nf_conntrack_max": {
      "default": 262144,
      "description": "Maximum number of tracked connections.",
      "minimum": 32768,
      "optional": 1,
      "type": "integer"
    },
    "nf_conntrack_tcp_timeout_established": {
      "default": 432000,
      "description": "Conntrack established timeout.",
      "minimum": 7875,
      "optional": 1,
      "type": "integer"
    },
    "nf_conntrack_tcp_timeout_syn_recv": {
      "default": 60,
      "description": "Conntrack syn recv timeout.",
      "maximum": 60,
      "minimum": 30,
      "optional": 1,
      "type": "integer"
    },
    "nftables": {
      "default": 0,
      "description": "Enable nftables based firewall (tech preview)",
      "optional": 1,
      "type": "boolean"
    },
    "nosmurfs": {
      "description": "Enable SMURFS filter.",
      "optional": 1,
      "type": "boolean"
    },
    "protection_synflood": {
      "default": 0,
      "description": "Enable synflood protection",
      "optional": 1,
      "type": "boolean"
    },
    "protection_synflood_burst": {
      "default": 1000,
      "description": "Synflood protection rate burst by ip src.",
      "optional": 1,
      "type": "integer"
    },
    "protection_synflood_rate": {
      "default": 200,
      "description": "Synflood protection rate syn/sec by ip src.",
      "optional": 1,
      "type": "integer"
    },
    "smurf_log_level": {
      "description": "Log level for SMURFS filter.",
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
    "tcp_flags_log_level": {
      "description": "Log level for illegal tcp flags filter.",
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
    "tcpflags": {
      "default": 0,
      "description": "Filter illegal combinations of TCP flags.",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/firewall/options`

Set Firewall options.

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Modify"
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
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `enable` | boolean | 否 | 1 | Enable host firewall rules. |
| `log_level_forward` | string | 否 | — | Log level for forwarded traffic.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_level_in` | string | 否 | — | Log level for incoming traffic.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_level_out` | string | 否 | — | Log level for outgoing traffic.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_nf_conntrack` | boolean | 否 | 0 | Enable logging of conntrack information. |
| `ndp` | boolean | 否 | 1 | Enable NDP (Neighbor Discovery Protocol). |
| `nf_conntrack_allow_invalid` | boolean | 否 | 0 | Allow invalid packets on connection tracking. |
| `nf_conntrack_helpers` | string | 否 | "" | Enable conntrack helpers for specific protocols. Supported protocols: amanda, ftp, irc, netbios-ns, pptp, sane, sip, snmp, tftp |
| `nf_conntrack_max` | integer | 否 | 262144 | Maximum number of tracked connections. |
| `nf_conntrack_tcp_timeout_established` | integer | 否 | 432000 | Conntrack established timeout. |
| `nf_conntrack_tcp_timeout_syn_recv` | integer | 否 | 60 | Conntrack syn recv timeout. |
| `nftables` | boolean | 否 | 0 | Enable nftables based firewall (tech preview) |
| `node` | string | 是 | — | The cluster node name. |
| `nosmurfs` | boolean | 否 | — | Enable SMURFS filter. |
| `protection_synflood` | boolean | 否 | 0 | Enable synflood protection |
| `protection_synflood_burst` | integer | 否 | 1000 | Synflood protection rate burst by ip src. |
| `protection_synflood_rate` | integer | 否 | 200 | Synflood protection rate syn/sec by ip src. |
| `smurf_log_level` | string | 否 | — | Log level for SMURFS filter.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `tcp_flags_log_level` | string | 否 | — | Log level for illegal tcp flags filter.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `tcpflags` | boolean | 否 | 0 | Filter illegal combinations of TCP flags. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
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
    "enable": {
      "default": 1,
      "description": "Enable host firewall rules.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "log_level_forward": {
      "description": "Log level for forwarded traffic.",
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
    "log_level_in": {
      "description": "Log level for incoming traffic.",
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
    "log_level_out": {
      "description": "Log level for outgoing traffic.",
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
    "log_nf_conntrack": {
      "default": 0,
      "description": "Enable logging of conntrack information.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ndp": {
      "default": 1,
      "description": "Enable NDP (Neighbor Discovery Protocol).",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nf_conntrack_allow_invalid": {
      "default": 0,
      "description": "Allow invalid packets on connection tracking.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nf_conntrack_helpers": {
      "default": "",
      "description": "Enable conntrack helpers for specific protocols. Supported protocols: amanda, ftp, irc, netbios-ns, pptp, sane, sip, snmp, tftp",
      "format": "pve-fw-conntrack-helper",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nf_conntrack_max": {
      "default": 262144,
      "description": "Maximum number of tracked connections.",
      "minimum": 32768,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (32768 - N)"
    },
    "nf_conntrack_tcp_timeout_established": {
      "default": 432000,
      "description": "Conntrack established timeout.",
      "minimum": 7875,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (7875 - N)"
    },
    "nf_conntrack_tcp_timeout_syn_recv": {
      "default": 60,
      "description": "Conntrack syn recv timeout.",
      "maximum": 60,
      "minimum": 30,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (30 - 60)"
    },
    "nftables": {
      "default": 0,
      "description": "Enable nftables based firewall (tech preview)",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "nosmurfs": {
      "description": "Enable SMURFS filter.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "protection_synflood": {
      "default": 0,
      "description": "Enable synflood protection",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "protection_synflood_burst": {
      "default": 1000,
      "description": "Synflood protection rate burst by ip src.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "protection_synflood_rate": {
      "default": 200,
      "description": "Synflood protection rate syn/sec by ip src.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "smurf_log_level": {
      "description": "Log level for SMURFS filter.",
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
    "tcp_flags_log_level": {
      "description": "Log level for illegal tcp flags filter.",
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
    "tcpflags": {
      "default": 0,
      "description": "Filter illegal combinations of TCP flags.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/firewall/options)。
