# `/cluster/sdn/vnets/{vnet}/ips`

原始接口路径：`/cluster/sdn/vnets/{vnet}/ips`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/vnets/{vnet}/ips`

Delete IP Mappings in a VNet

**方法标识：** `ipdelete`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}/{vnet}",
    [
      "SDN.Allocate"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `ip` | string | 是 | — | The IP address to delete |
| `mac` | string | 否 | — | A common MAC address with the I/G (Individual/Group) bit not set. |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |
| `zone` | string | 是 | — | The SDN zone object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ip": {
      "description": "The IP address to delete",
      "format": "ip",
      "type": "string",
      "typetext": "<string>"
    },
    "mac": {
      "description": "Unicast MAC address.",
      "format": "mac-addr",
      "format_description": "XX:XX:XX:XX:XX:XX",
      "optional": 1,
      "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>",
      "verbose_description": "A common MAC address with the I/G (Individual/Group) bit not set."
    },
    "vnet": {
      "description": "The SDN vnet object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "The SDN zone object identifier.",
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

## POST `/cluster/sdn/vnets/{vnet}/ips`

Create IP Mapping in a VNet

**方法标识：** `ipcreate`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}/{vnet}",
    [
      "SDN.Allocate"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `ip` | string | 是 | — | The IP address to associate with the given MAC address |
| `mac` | string | 否 | — | A common MAC address with the I/G (Individual/Group) bit not set. |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |
| `zone` | string | 是 | — | The SDN zone object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ip": {
      "description": "The IP address to associate with the given MAC address",
      "format": "ip",
      "type": "string",
      "typetext": "<string>"
    },
    "mac": {
      "description": "Unicast MAC address.",
      "format": "mac-addr",
      "format_description": "XX:XX:XX:XX:XX:XX",
      "optional": 1,
      "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>",
      "verbose_description": "A common MAC address with the I/G (Individual/Group) bit not set."
    },
    "vnet": {
      "description": "The SDN vnet object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "The SDN zone object identifier.",
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

## PUT `/cluster/sdn/vnets/{vnet}/ips`

Update IP Mapping in a VNet

**方法标识：** `ipupdate`

**权限**

```json
{
  "check": [
    "perm",
    "/sdn/zones/{zone}/{vnet}",
    [
      "SDN.Allocate"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `ip` | string | 是 | — | The IP address to associate with the given MAC address |
| `mac` | string | 否 | — | A common MAC address with the I/G (Individual/Group) bit not set. |
| `vmid` | integer | 否 | — | The (unique) ID of the VM. |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |
| `zone` | string | 是 | — | The SDN zone object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ip": {
      "description": "The IP address to associate with the given MAC address",
      "format": "ip",
      "type": "string",
      "typetext": "<string>"
    },
    "mac": {
      "description": "Unicast MAC address.",
      "format": "mac-addr",
      "format_description": "XX:XX:XX:XX:XX:XX",
      "optional": 1,
      "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>",
      "verbose_description": "A common MAC address with the I/G (Individual/Group) bit not set."
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "vnet": {
      "description": "The SDN vnet object identifier.",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "The SDN zone object identifier.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/ips)。
