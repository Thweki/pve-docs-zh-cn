# `/cluster/sdn/vnets/{vnet}/ips`

原始接口路径：`/cluster/sdn/vnets/{vnet}/ips`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/sdn/vnets/{vnet}/ips`

删除 VNet 中的 IP 映射

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
| `ip` | string | 是 | — | 要删除的 IP 地址 |
| `mac` | string | 否 | — | 未设置 I/G（个体/组）位的普通 MAC 地址。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |
| `zone` | string | 是 | — | SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ip": {
      "description": "要删除的 IP 地址",
      "format": "ip",
      "type": "string",
      "typetext": "<string>"
    },
    "mac": {
      "description": "单播 MAC 地址。",
      "format": "mac-addr",
      "format_description": "XX:XX:XX:XX:XX:XX",
      "optional": 1,
      "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>",
      "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "SDN 区域对象标识符。",
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

在 VNet 中创建 IP 映射

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
| `ip` | string | 是 | — | 要与给定 MAC 地址关联的 IP 地址 |
| `mac` | string | 否 | — | 未设置 I/G（个体/组）位的普通 MAC 地址。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |
| `zone` | string | 是 | — | SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ip": {
      "description": "要与给定 MAC 地址关联的 IP 地址",
      "format": "ip",
      "type": "string",
      "typetext": "<string>"
    },
    "mac": {
      "description": "单播 MAC 地址。",
      "format": "mac-addr",
      "format_description": "XX:XX:XX:XX:XX:XX",
      "optional": 1,
      "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>",
      "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "SDN 区域对象标识符。",
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

更新 VNet 中的 IP 映射

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
| `ip` | string | 是 | — | 要与给定 MAC 地址关联的 IP 地址 |
| `mac` | string | 否 | — | 未设置 I/G（个体/组）位的普通 MAC 地址。 |
| `vmid` | integer | 否 | — | 虚拟机的（唯一）ID。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |
| `zone` | string | 是 | — | SDN 区域对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ip": {
      "description": "要与给定 MAC 地址关联的 IP 地址",
      "format": "ip",
      "type": "string",
      "typetext": "<string>"
    },
    "mac": {
      "description": "单播 MAC 地址。",
      "format": "mac-addr",
      "format_description": "XX:XX:XX:XX:XX:XX",
      "optional": 1,
      "type": "string",
      "typetext": "<XX:XX:XX:XX:XX:XX>",
      "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    },
    "zone": {
      "description": "SDN 区域对象标识符。",
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
