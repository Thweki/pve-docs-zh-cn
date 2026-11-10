# `/nodes/{node}/network/{iface}`

原始接口路径：`/nodes/{node}/network/{iface}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/network/{iface}`

删除网络设备配置

**方法标识：** `delete_network`

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
| `iface` | string | 是 | — | 网络接口名称。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "iface": {
      "description": "网络接口名称。",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "type": "string",
      "typetext": "<string>"
    },
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
  "type": "null"
}
```

## GET `/nodes/{node}/network/{iface}`

读取网络设备配置

**方法标识：** `network_config`

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
| `iface` | string | 是 | — | 网络接口名称。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "iface": {
      "description": "网络接口名称。",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "type": "string",
      "typetext": "<string>"
    },
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
    "method": {
      "type": "string"
    },
    "type": {
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/network/{iface}`

更新网络设备配置

**方法标识：** `update_network`

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
| `address` | string | 否 | — | IP 地址。 |
| `address6` | string | 否 | — | IP 地址。 |
| `autostart` | boolean | 否 | — | 启动时自动启用接口。 |
| `bond-primary` | string | 否 | — | 为 active-backup 绑定指定主接口。 |
| `bond_mode` | string | 否 | — | 绑定模式。；可选值：`balance-rr`, `active-backup`, `balance-xor`, `broadcast`, `802.3ad`, `balance-tlb`, `balance-alb`, `balance-slb`, `lacp-balance-slb`, `lacp-balance-tcp` |
| `bond_xmit_hash_policy` | string | 否 | — | 选择 balance-xor 和 802.3ad 模式中用于选择从接口的发送哈希策略。；可选值：`layer2`, `layer2+3`, `layer3+4` |
| `bridge_ports` | string | 否 | — | 指定要加入网桥的接口。 |
| `bridge_vids` | string | 否 | — | 指定允许的 VLAN。例如：'2 4 100-200'。仅在网桥支持 VLAN 感知时使用。 |
| `bridge_vlan_aware` | boolean | 否 | — | 启用网桥 VLAN 支持。 |
| `cidr` | string | 否 | — | IPv4 CIDR。 |
| `cidr6` | string | 否 | — | IPv6 CIDR。 |
| `comments` | string | 否 | — | 注释 |
| `comments6` | string | 否 | — | 注释 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `gateway` | string | 否 | — | 默认网关地址。 |
| `gateway6` | string | 否 | — | 默认 IPv6 网关地址。 |
| `iface` | string | 是 | — | 网络接口名称。 |
| `mtu` | integer | 否 | — | MTU。 |
| `netmask` | string | 否 | — | 网络掩码。 |
| `netmask6` | integer | 否 | — | 网络掩码。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `ovs_bonds` | string | 否 | — | 指定绑定设备使用的接口。 |
| `ovs_bridge` | string | 否 | — | 与 OVS 端口关联的 OVS 网桥。创建 OVS 端口时需要此项。 |
| `ovs_options` | string | 否 | — | OVS 接口选项。 |
| `ovs_ports` | string | 否 | — | 指定要加入网桥的接口。 |
| `ovs_tag` | integer | 否 | — | 指定 VLAN 标签（用于 OVSPort、OVSIntPort、OVSBond） |
| `slaves` | string | 否 | — | 指定绑定设备使用的接口。 |
| `type` | string | 是 | — | 网络接口类型；可选值：`bridge`, `bond`, `eth`, `alias`, `vlan`, `fabric`, `OVSBridge`, `OVSBond`, `OVSPort`, `OVSIntPort`, `vnet`, `unknown` |
| `vlan-id` | integer | 否 | — | 自定义名称的 VLAN 接口的 vlan-id（仅限 ifupdown2）。 |
| `vlan-raw-device` | string | 否 | — | 指定 VLAN 接口的原始接口。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "address": {
      "description": "IP 地址。",
      "format": "ipv4",
      "optional": 1,
      "requires": "netmask",
      "type": "string",
      "typetext": "<string>"
    },
    "address6": {
      "description": "IP 地址。",
      "format": "ipv6",
      "optional": 1,
      "requires": "netmask6",
      "type": "string",
      "typetext": "<string>"
    },
    "autostart": {
      "description": "启动时自动启用接口。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "bond-primary": {
      "description": "为 active-backup 绑定指定主接口。",
      "format": "pve-iface",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bond_mode": {
      "description": "绑定模式。",
      "enum": [
        "balance-rr",
        "active-backup",
        "balance-xor",
        "broadcast",
        "802.3ad",
        "balance-tlb",
        "balance-alb",
        "balance-slb",
        "lacp-balance-slb",
        "lacp-balance-tcp"
      ],
      "optional": 1,
      "type": "string"
    },
    "bond_xmit_hash_policy": {
      "description": "选择 balance-xor 和 802.3ad 模式中用于选择从接口的发送哈希策略。",
      "enum": [
        "layer2",
        "layer2+3",
        "layer3+4"
      ],
      "optional": 1,
      "type": "string"
    },
    "bridge_ports": {
      "description": "指定要加入网桥的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge_vids": {
      "description": "指定允许的 VLAN。例如：'2 4 100-200'。仅在网桥支持 VLAN 感知时使用。",
      "format": "pve-vlan-id-or-range-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bridge_vlan_aware": {
      "description": "启用网桥 VLAN 支持。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cidr": {
      "description": "IPv4 CIDR。",
      "format": "CIDRv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "cidr6": {
      "description": "IPv6 CIDR。",
      "format": "CIDRv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comments": {
      "description": "注释",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comments6": {
      "description": "注释",
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
    "gateway": {
      "description": "默认网关地址。",
      "format": "ipv4",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway6": {
      "description": "默认 IPv6 网关地址。",
      "format": "ipv6",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "iface": {
      "description": "网络接口名称。",
      "format": "pve-iface",
      "maxLength": 20,
      "minLength": 2,
      "type": "string",
      "typetext": "<string>"
    },
    "mtu": {
      "description": "MTU。",
      "maximum": 65520,
      "minimum": 1280,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1280 - 65520)"
    },
    "netmask": {
      "description": "网络掩码。",
      "format": "ipv4mask",
      "optional": 1,
      "requires": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "netmask6": {
      "description": "网络掩码。",
      "maximum": 128,
      "minimum": 0,
      "optional": 1,
      "requires": "address6",
      "type": "integer",
      "typetext": "<integer> (0 - 128)"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_bonds": {
      "description": "指定绑定设备使用的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_bridge": {
      "description": "与 OVS 端口关联的 OVS 网桥。创建 OVS 端口时需要此项。",
      "format": "pve-iface",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_options": {
      "description": "OVS 接口选项。",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_ports": {
      "description": "指定要加入网桥的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ovs_tag": {
      "description": "指定 VLAN 标签（用于 OVSPort、OVSIntPort、OVSBond）",
      "maximum": 4094,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 4094)"
    },
    "slaves": {
      "description": "指定绑定设备使用的接口。",
      "format": "pve-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "网络接口类型",
      "enum": [
        "bridge",
        "bond",
        "eth",
        "alias",
        "vlan",
        "fabric",
        "OVSBridge",
        "OVSBond",
        "OVSPort",
        "OVSIntPort",
        "vnet",
        "unknown"
      ],
      "type": "string"
    },
    "vlan-id": {
      "description": "自定义名称的 VLAN 接口的 vlan-id（仅限 ifupdown2）。",
      "maximum": 4094,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 4094)"
    },
    "vlan-raw-device": {
      "description": "指定 VLAN 接口的原始接口。",
      "format": "pve-iface",
      "optional": 1,
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/network/{iface})。
