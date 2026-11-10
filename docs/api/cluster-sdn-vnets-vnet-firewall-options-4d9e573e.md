# `/cluster/sdn/vnets/{vnet}/firewall/options`

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets/{vnet}/firewall/options`

Get vnet firewall options.

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
  "properties": {
    "enable": {
      "default": 0,
      "description": "Enable/disable firewall rules.",
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
    "policy_forward": {
      "description": "Forward policy.",
      "enum": [
        "ACCEPT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/sdn/vnets/{vnet}/firewall/options`

Set Firewall options.

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `enable` | boolean | 否 | 0 | Enable/disable firewall rules. |
| `log_level_forward` | string | 否 | — | Log level for forwarded traffic.；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `policy_forward` | string | 否 | — | Forward policy.；可选值：`ACCEPT`, `DROP` |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |

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
      "default": 0,
      "description": "Enable/disable firewall rules.",
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
    "policy_forward": {
      "description": "Forward policy.",
      "enum": [
        "ACCEPT",
        "DROP"
      ],
      "optional": 1,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/options)。
