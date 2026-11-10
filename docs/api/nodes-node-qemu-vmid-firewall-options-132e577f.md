# `/nodes/{node}/qemu/{vmid}/firewall/options`

原始接口路径：`/nodes/{node}/qemu/{vmid}/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/firewall/options`

获取虚拟机防火墙选项。

**方法标识：** `get_options`

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
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

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
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
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
    "dhcp": {
      "default": 0,
      "description": "启用 DHCP。",
      "optional": 1,
      "type": "boolean"
    },
    "enable": {
      "default": 0,
      "description": "启用/禁用防火墙规则。",
      "optional": 1,
      "type": "boolean"
    },
    "ipfilter": {
      "description": "启用默认 IP 过滤器。这相当于为每个接口添加一个空的 ipfilter-net<id> IP 集合。此类 IP 集合隐含包含合理的默认限制，例如将 IPv6 链路本地地址限制为由接口 MAC 地址派生的地址。对于容器，还会隐式添加已配置的 IP 地址。",
      "optional": 1,
      "type": "boolean"
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
    "macfilter": {
      "default": 1,
      "description": "启用/禁用 MAC 地址过滤器。",
      "optional": 1,
      "type": "boolean"
    },
    "ndp": {
      "default": 1,
      "description": "启用 NDP（邻居发现协议）。",
      "optional": 1,
      "type": "boolean"
    },
    "policy_in": {
      "description": "输入策略。",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "policy_out": {
      "description": "输出策略。",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "radv": {
      "description": "允许发送路由器通告。",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/qemu/{vmid}/firewall/options`

设置防火墙选项。

**方法标识：** `set_options`

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
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `dhcp` | boolean | 否 | 0 | 启用 DHCP。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `enable` | boolean | 否 | 0 | 启用/禁用防火墙规则。 |
| `ipfilter` | boolean | 否 | — | 启用默认 IP 过滤器。这相当于为每个接口添加一个空的 ipfilter-net&lt;id&gt; IP 集合。此类 IP 集合隐含包含合理的默认限制，例如将 IPv6 链路本地地址限制为由接口 MAC 地址派生的地址。对于容器，还会隐式添加已配置的 IP 地址。 |
| `log_level_in` | string | 否 | — | 传入流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_level_out` | string | 否 | — | 传出流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macfilter` | boolean | 否 | 1 | 启用/禁用 MAC 地址过滤器。 |
| `ndp` | boolean | 否 | 1 | 启用 NDP（邻居发现协议）。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `policy_in` | string | 否 | — | 输入策略。；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `policy_out` | string | 否 | — | 输出策略。；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `radv` | boolean | 否 | — | 允许发送路由器通告。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

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
    "dhcp": {
      "default": 0,
      "description": "启用 DHCP。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "default": 0,
      "description": "启用/禁用防火墙规则。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ipfilter": {
      "description": "启用默认 IP 过滤器。这相当于为每个接口添加一个空的 ipfilter-net<id> IP 集合。此类 IP 集合隐含包含合理的默认限制，例如将 IPv6 链路本地地址限制为由接口 MAC 地址派生的地址。对于容器，还会隐式添加已配置的 IP 地址。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "macfilter": {
      "default": 1,
      "description": "启用/禁用 MAC 地址过滤器。",
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
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "policy_in": {
      "description": "输入策略。",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "policy_out": {
      "description": "输出策略。",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "radv": {
      "description": "允许发送路由器通告。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/firewall/options)。
