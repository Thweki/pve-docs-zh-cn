# `/nodes/{node}/firewall/options`

原始接口路径：`/nodes/{node}/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/firewall/options`

获取宿主机防火墙选项。

**方法标识：** `get_options`

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
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "集群节点名称。",
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
      "description": "启用宿主机防火墙规则。",
      "optional": 1,
      "type": "boolean"
    },
    "log_level_forward": {
      "description": "转发流量的日志级别。",
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
      "description": "传入流量的日志级别。",
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
      "description": "传出流量的日志级别。",
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
      "description": "启用 conntrack 信息日志记录。",
      "optional": 1,
      "type": "boolean"
    },
    "ndp": {
      "default": 1,
      "description": "启用 NDP（邻居发现协议）。",
      "optional": 1,
      "type": "boolean"
    },
    "nf_conntrack_allow_invalid": {
      "default": 0,
      "description": "在连接跟踪中允许无效数据包。",
      "optional": 1,
      "type": "boolean"
    },
    "nf_conntrack_helpers": {
      "default": "",
      "description": "为特定协议启用 conntrack 辅助模块。支持的协议：amanda、ftp、irc、netbios-ns、pptp、sane、sip、snmp、tftp",
      "format": "pve-fw-conntrack-helper",
      "optional": 1,
      "type": "string"
    },
    "nf_conntrack_max": {
      "default": 262144,
      "description": "跟踪连接的最大数量。",
      "minimum": 32768,
      "optional": 1,
      "type": "integer"
    },
    "nf_conntrack_tcp_timeout_established": {
      "default": 432000,
      "description": "Conntrack established 超时时间。",
      "minimum": 7875,
      "optional": 1,
      "type": "integer"
    },
    "nf_conntrack_tcp_timeout_syn_recv": {
      "default": 60,
      "description": "Conntrack syn recv 超时时间。",
      "maximum": 60,
      "minimum": 30,
      "optional": 1,
      "type": "integer"
    },
    "nftables": {
      "default": 0,
      "description": "启用基于 nftables 的防火墙（技术预览）",
      "optional": 1,
      "type": "boolean"
    },
    "nosmurfs": {
      "description": "启用 SMURFS 过滤器。",
      "optional": 1,
      "type": "boolean"
    },
    "protection_synflood": {
      "default": 0,
      "description": "启用 SYN 洪泛防护",
      "optional": 1,
      "type": "boolean"
    },
    "protection_synflood_burst": {
      "default": 1000,
      "description": "按源 IP 的 SYN 洪泛防护突发速率。",
      "optional": 1,
      "type": "integer"
    },
    "protection_synflood_rate": {
      "default": 200,
      "description": "按源 IP 的 SYN 洪泛防护速率，单位为 syn/sec。",
      "optional": 1,
      "type": "integer"
    },
    "smurf_log_level": {
      "description": "SMURFS 过滤器的日志级别。",
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
      "description": "非法 TCP 标志过滤器的日志级别。",
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
      "description": "过滤 TCP 标志的非法组合。",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/firewall/options`

设置防火墙选项。

**方法标识：** `set_options`

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
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `enable` | boolean | 否 | 1 | 启用宿主机防火墙规则。 |
| `log_level_forward` | string | 否 | — | 转发流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_level_in` | string | 否 | — | 传入流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_level_out` | string | 否 | — | 传出流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_nf_conntrack` | boolean | 否 | 0 | 启用 conntrack 信息日志记录。 |
| `ndp` | boolean | 否 | 1 | 启用 NDP（邻居发现协议）。 |
| `nf_conntrack_allow_invalid` | boolean | 否 | 0 | 在连接跟踪中允许无效数据包。 |
| `nf_conntrack_helpers` | string | 否 | "" | 为特定协议启用 conntrack 辅助模块。支持的协议：amanda、ftp、irc、netbios-ns、pptp、sane、sip、snmp、tftp |
| `nf_conntrack_max` | integer | 否 | 262144 | 跟踪连接的最大数量。 |
| `nf_conntrack_tcp_timeout_established` | integer | 否 | 432000 | Conntrack established 超时时间。 |
| `nf_conntrack_tcp_timeout_syn_recv` | integer | 否 | 60 | Conntrack syn recv 超时时间。 |
| `nftables` | boolean | 否 | 0 | 启用基于 nftables 的防火墙（技术预览） |
| `node` | string | 是 | — | 集群节点名称。 |
| `nosmurfs` | boolean | 否 | — | 启用 SMURFS 过滤器。 |
| `protection_synflood` | boolean | 否 | 0 | 启用 SYN 洪泛防护 |
| `protection_synflood_burst` | integer | 否 | 1000 | 按源 IP 的 SYN 洪泛防护突发速率。 |
| `protection_synflood_rate` | integer | 否 | 200 | 按源 IP 的 SYN 洪泛防护速率，单位为 syn/sec。 |
| `smurf_log_level` | string | 否 | — | SMURFS 过滤器的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `tcp_flags_log_level` | string | 否 | — | 非法 TCP 标志过滤器的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `tcpflags` | boolean | 否 | 0 | 过滤 TCP 标志的非法组合。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "default": 1,
      "description": "启用宿主机防火墙规则。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "log_level_forward": {
      "description": "转发流量的日志级别。",
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
      "description": "传入流量的日志级别。",
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
      "description": "传出流量的日志级别。",
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
      "description": "启用 conntrack 信息日志记录。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ndp": {
      "default": 1,
      "description": "启用 NDP（邻居发现协议）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nf_conntrack_allow_invalid": {
      "default": 0,
      "description": "在连接跟踪中允许无效数据包。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "nf_conntrack_helpers": {
      "default": "",
      "description": "为特定协议启用 conntrack 辅助模块。支持的协议：amanda、ftp、irc、netbios-ns、pptp、sane、sip、snmp、tftp",
      "format": "pve-fw-conntrack-helper",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nf_conntrack_max": {
      "default": 262144,
      "description": "跟踪连接的最大数量。",
      "minimum": 32768,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (32768 - N)"
    },
    "nf_conntrack_tcp_timeout_established": {
      "default": 432000,
      "description": "Conntrack established 超时时间。",
      "minimum": 7875,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (7875 - N)"
    },
    "nf_conntrack_tcp_timeout_syn_recv": {
      "default": 60,
      "description": "Conntrack syn recv 超时时间。",
      "maximum": 60,
      "minimum": 30,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (30 - 60)"
    },
    "nftables": {
      "default": 0,
      "description": "启用基于 nftables 的防火墙（技术预览）",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "nosmurfs": {
      "description": "启用 SMURFS 过滤器。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "protection_synflood": {
      "default": 0,
      "description": "启用 SYN 洪泛防护",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "protection_synflood_burst": {
      "default": 1000,
      "description": "按源 IP 的 SYN 洪泛防护突发速率。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "protection_synflood_rate": {
      "default": 200,
      "description": "按源 IP 的 SYN 洪泛防护速率，单位为 syn/sec。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "smurf_log_level": {
      "description": "SMURFS 过滤器的日志级别。",
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
      "description": "非法 TCP 标志过滤器的日志级别。",
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
      "description": "过滤 TCP 标志的非法组合。",
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
