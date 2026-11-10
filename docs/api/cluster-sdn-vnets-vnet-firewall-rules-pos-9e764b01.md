# `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}`

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}`

删除规则。

**方法标识：** `delete_rule`

**权限**

```json
{
  "description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Allocate 权限",
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
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `pos` | integer | 否 | — | 更新位置 &lt;pos&gt; 处的规则。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "pos": {
      "description": "更新位置 <pos> 处的规则。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
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

## GET `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}`

获取单条规则数据。

**方法标识：** `get_rule`

**权限**

```json
{
  "description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Audit 或 SDN.Allocate 权限",
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
| `pos` | integer | 否 | — | 更新位置 &lt;pos&gt; 处的规则。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "pos": {
      "description": "更新位置 <pos> 处的规则。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
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
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称",
      "type": "string"
    },
    "comment": {
      "description": "描述性注释",
      "optional": 1,
      "type": "string"
    },
    "dest": {
      "description": "限制数据包目标地址",
      "optional": 1,
      "type": "string"
    },
    "dport": {
      "description": "限制 TCP/UDP 目标端口",
      "optional": 1,
      "type": "string"
    },
    "enable": {
      "description": "用于启用/禁用规则的标志",
      "optional": 1,
      "type": "integer"
    },
    "icmp-type": {
      "description": "指定 icmp-type。仅在 proto 等于 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效",
      "optional": 1,
      "type": "string"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名",
      "optional": 1,
      "type": "string"
    },
    "ipversion": {
      "description": "IP 版本（4 或 6）——根据源地址/目标地址自动确定",
      "optional": 1,
      "type": "integer"
    },
    "log": {
      "description": "防火墙规则的日志级别",
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
      "description": "使用预定义的标准宏",
      "optional": 1,
      "type": "string"
    },
    "pos": {
      "description": "规则在规则集中的位置",
      "type": "integer"
    },
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字",
      "optional": 1,
      "type": "string"
    },
    "source": {
      "description": "限制数据包源地址",
      "optional": 1,
      "type": "string"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口",
      "optional": 1,
      "type": "string"
    },
    "type": {
      "description": "规则类型",
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/sdn/vnets/{vnet}/firewall/rules/{pos}`

修改规则数据。

**方法标识：** `update_rule`

**权限**

```json
{
  "description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 SDN.Allocate 权限",
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
| `action` | string | 否 | — | 规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。 |
| `comment` | string | 否 | — | 描述性注释。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `dest` | string | 否 | — | 限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `dport` | string | 否 | — | 限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `enable` | integer | 否 | — | 用于启用/禁用规则的标志。 |
| `icmp-type` | string | 否 | — | 指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。 |
| `iface` | string | 否 | — | 网络接口名称。虚拟机和容器必须使用网络配置键名（'net\d+'）。宿主机相关规则可使用任意字符串。 |
| `log` | string | 否 | — | 防火墙规则的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macro` | string | 否 | — | 使用预定义的标准宏。 |
| `moveto` | integer | 否 | — | 将规则移至新位置 &lt;moveto&gt;。其他参数将被忽略。 |
| `pos` | integer | 否 | — | 更新位置 &lt;pos&gt; 处的规则。 |
| `proto` | string | 否 | — | IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。 |
| `source` | string | 否 | — | 限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。 |
| `sport` | string | 否 | — | 限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\d+:\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。 |
| `type` | string | 否 | — | 规则类型。；可选值：`in`, `out`, `forward`, `group` |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "action": {
      "description": "规则动作（'ACCEPT'、'DROP'、'REJECT'）或安全组名称。",
      "maxLength": 20,
      "minLength": 2,
      "optional": 1,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
      "type": "string"
    },
    "comment": {
      "description": "描述性注释。",
      "format": "pve-fw-comment-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dest": {
      "description": "限制数据包目标地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec",
      "maxLength": 512,
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
    "dport": {
      "description": "限制 TCP/UDP 目标端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-dport-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "description": "用于启用/禁用规则的标志。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "icmp-type": {
      "description": "指定 icmp-type。仅当 proto 为 'icmp' 或 'icmpv6'/'ipv6-icmp' 时有效。",
      "format": "pve-fw-icmp-type-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。虚拟机和容器必须使用网络配置键名（'net\\d+'）。宿主机相关规则可使用任意字符串。",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "log": {
      "description": "防火墙规则的日志级别。",
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
      "description": "使用预定义的标准宏。",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "moveto": {
      "description": "将规则移至新位置 <moveto>。其他参数将被忽略。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "pos": {
      "description": "更新位置 <pos> 处的规则。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "proto": {
      "description": "IP 协议。可以使用协议名称（'tcp'/'udp'）或 '/etc/protocols' 中定义的数字。",
      "format": "pve-fw-protocol-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "source": {
      "description": "限制数据包源地址。可以指定单个 IP 地址、IP 集合（'+ipsetname'）或 IP 别名定义。也可以指定地址范围，例如 '20.34.101.207-201.3.9.99'，或 IP 地址和网络列表（条目以逗号分隔）。请勿在此类列表中混用 IPv4 和 IPv6 地址。",
      "format": "pve-fw-addr-spec",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "sport": {
      "description": "限制 TCP/UDP 源端口。可以使用服务名称或 '/etc/services' 中定义的数字（0-65535）。端口范围可使用 '\\d+:\\d+' 指定，例如 '80:85'，也可使用逗号分隔的列表匹配多个端口或范围。",
      "format": "pve-fw-sport-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "规则类型。",
      "enum": [
        "in",
        "out",
        "forward",
        "group"
      ],
      "optional": 1,
      "type": "string"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/rules/{pos})。
