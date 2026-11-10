# `/cluster/firewall/options`

原始接口路径：`/cluster/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/options`

获取防火墙选项。

**方法标识：** `get_options`

**权限**

```json
{
  "check": [
    "perm",
    "/",
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

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "properties": {
    "ebtables": {
      "default": 1,
      "description": "在整个集群中启用 ebtables 规则。",
      "optional": 1,
      "type": "boolean"
    },
    "enable": {
      "default": 0,
      "description": "在整个集群中启用或禁用防火墙。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "log_ratelimit": {
      "description": "日志速率限制设置",
      "format": {
        "burst": {
          "default": 5,
          "description": "应用速率限制前始终记录日志的初始突发数据包数量",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "enable": {
          "default": "1",
          "default_key": 1,
          "description": "启用或禁用日志速率限制",
          "type": "boolean"
        },
        "rate": {
          "default": "1/second",
          "description": "补充突发令牌桶的频率",
          "format_description": "rate",
          "optional": 1,
          "pattern": "[1-9][0-9]*\\/(second|minute|hour|day)",
          "type": "string"
        }
      },
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
    }
  },
  "type": "object"
}
```

## PUT `/cluster/firewall/options`

设置防火墙选项。

**方法标识：** `set_options`

**权限**

```json
{
  "check": [
    "perm",
    "/",
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `ebtables` | boolean | 否 | 1 | 在整个集群中启用 ebtables 规则。 |
| `enable` | integer | 否 | 0 | 在整个集群中启用或禁用防火墙。 |
| `log_ratelimit` | string | 否 | — | 日志速率限制设置 |
| `policy_forward` | string | 否 | — | 转发策略。；可选值：`ACCEPT`, `DROP` |
| `policy_in` | string | 否 | — | 输入策略。；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `policy_out` | string | 否 | — | 输出策略。；可选值：`ACCEPT`, `REJECT`, `DROP` |

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
    "ebtables": {
      "default": 1,
      "description": "在整个集群中启用 ebtables 规则。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enable": {
      "default": 0,
      "description": "在整个集群中启用或禁用防火墙。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "log_ratelimit": {
      "description": "日志速率限制设置",
      "format": {
        "burst": {
          "default": 5,
          "description": "应用速率限制前始终记录日志的初始突发数据包数量",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "enable": {
          "default": "1",
          "default_key": 1,
          "description": "启用或禁用日志速率限制",
          "type": "boolean"
        },
        "rate": {
          "default": "1/second",
          "description": "补充突发令牌桶的频率",
          "format_description": "rate",
          "optional": 1,
          "pattern": "[1-9][0-9]*\\/(second|minute|hour|day)",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[enable=]<1|0> [,burst=<integer>] [,rate=<rate>]"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/options)。
