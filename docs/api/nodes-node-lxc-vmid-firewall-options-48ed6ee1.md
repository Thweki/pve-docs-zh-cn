# `/nodes/{node}/lxc/{vmid}/firewall/options`

原始接口路径：`/nodes/{node}/lxc/{vmid}/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/firewall/options`

Get VM firewall options.

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
| `node` | string | 是 | — | The cluster node name. |
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
    "dhcp": {
      "default": 0,
      "description": "Enable DHCP.",
      "optional": 1,
      "type": "boolean"
    },
    "enable": {
      "default": 0,
      "description": "Enable/disable firewall rules.",
      "optional": 1,
      "type": "boolean"
    },
    "ipfilter": {
      "description": "Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added.",
      "optional": 1,
      "type": "boolean"
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
    "macfilter": {
      "default": 1,
      "description": "Enable/disable MAC address filter.",
      "optional": 1,
      "type": "boolean"
    },
    "ndp": {
      "default": 1,
      "description": "Enable NDP (Neighbor Discovery Protocol).",
      "optional": 1,
      "type": "boolean"
    },
    "policy_in": {
      "description": "Input policy.",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "policy_out": {
      "description": "Output policy.",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "radv": {
      "description": "Allow sending Router Advertisement.",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/lxc/{vmid}/firewall/options`

Set Firewall options.

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
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `dhcp` | boolean | 否 | 0 | Enable DHCP. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `enable` | boolean | 否 | 0 | Enable/disable firewall rules. |
| `ipfilter` | boolean | 否 | — | Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added. |
| `log_level_in` | string | 否 | — | Log level for incoming traffic.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `log_level_out` | string | 否 | — | Log level for outgoing traffic.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `macfilter` | boolean | 否 | 1 | Enable/disable MAC address filter. |
| `ndp` | boolean | 否 | 1 | Enable NDP (Neighbor Discovery Protocol). |
| `node` | string | 是 | — | The cluster node name. |
| `policy_in` | string | 否 | — | Input policy.；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `policy_out` | string | 否 | — | Output policy.；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `radv` | boolean | 否 | — | Allow sending Router Advertisement. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

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
    "dhcp": {
      "default": 0,
      "description": "Enable DHCP.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable": {
      "default": 0,
      "description": "Enable/disable firewall rules.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ipfilter": {
      "description": "Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "macfilter": {
      "default": 1,
      "description": "Enable/disable MAC address filter.",
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
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "policy_in": {
      "description": "Input policy.",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "policy_out": {
      "description": "Output policy.",
      "enum": [
        "ACCEPT",
        "REJECT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    },
    "radv": {
      "description": "Allow sending Router Advertisement.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/firewall/options)。
