# `/cluster/sdn/vnets/{vnet}/firewall/options`

原始接口路径：`/cluster/sdn/vnets/{vnet}/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets/{vnet}/firewall/options`

获取 vnet 防火墙选项。

**方法标识：** `get_options`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    "enable": {
      "default": 0,
      "description": "启用/禁用防火墙规则。",
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
    "policy_forward": {
      "description": "转发策略。",
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

设置防火墙选项。

**方法标识：** `set_options`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `enable` | boolean | 否 | 0 | 启用/禁用防火墙规则。 |
| `log_level_forward` | string | 否 | — | 转发流量的日志级别。；可选值：`emerg`, `alert`, `crit`, `err`, `warning`, `notice`, `info`, `debug`, `nolog` |
| `policy_forward` | string | 否 | — | 转发策略。；可选值：`ACCEPT`, `DROP` |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

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
      "default": 0,
      "description": "启用/禁用防火墙规则。",
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
    "policy_forward": {
      "description": "转发策略。",
      "enum": [
        "ACCEPT",
        "DROP"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/firewall/options)。
