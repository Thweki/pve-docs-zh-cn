# `/cluster/firewall/options`

原始接口路径：`/cluster/firewall/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/options`

Get Firewall options.

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
      "description": "Enable ebtables rules cluster wide.",
      "optional": 1,
      "type": "boolean"
    },
    "enable": {
      "default": 0,
      "description": "Enable or disable the firewall cluster wide.",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "log_ratelimit": {
      "description": "Log ratelimiting settings",
      "format": {
        "burst": {
          "default": 5,
          "description": "Initial burst of packages which will always get logged before the rate is applied",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "enable": {
          "default": "1",
          "default_key": 1,
          "description": "Enable or disable log rate limiting",
          "type": "boolean"
        },
        "rate": {
          "default": "1/second",
          "description": "Frequency with which the burst bucket gets refilled",
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
      "description": "Forward policy.",
      "enum": [
        "ACCEPT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
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
    }
  },
  "type": "object"
}
```

## PUT `/cluster/firewall/options`

Set Firewall options.

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
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `ebtables` | boolean | 否 | 1 | Enable ebtables rules cluster wide. |
| `enable` | integer | 否 | 0 | Enable or disable the firewall cluster wide. |
| `log_ratelimit` | string | 否 | — | Log ratelimiting settings |
| `policy_forward` | string | 否 | — | Forward policy.；可选值：`ACCEPT`, `DROP` |
| `policy_in` | string | 否 | — | Input policy.；可选值：`ACCEPT`, `REJECT`, `DROP` |
| `policy_out` | string | 否 | — | Output policy.；可选值：`ACCEPT`, `REJECT`, `DROP` |

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
    "ebtables": {
      "default": 1,
      "description": "Enable ebtables rules cluster wide.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enable": {
      "default": 0,
      "description": "Enable or disable the firewall cluster wide.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "log_ratelimit": {
      "description": "Log ratelimiting settings",
      "format": {
        "burst": {
          "default": 5,
          "description": "Initial burst of packages which will always get logged before the rate is applied",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "enable": {
          "default": "1",
          "default_key": 1,
          "description": "Enable or disable log rate limiting",
          "type": "boolean"
        },
        "rate": {
          "default": "1/second",
          "description": "Frequency with which the burst bucket gets refilled",
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
      "description": "Forward policy.",
      "enum": [
        "ACCEPT",
        "DROP"
      ],
      "optional": 1,
      "type": "string"
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
