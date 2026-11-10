# `/cluster/acme/account/{name}`

原始接口路径：`/cluster/acme/account/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/acme/account/{name}`

在 CA 处停用现有 ACME 账户。

**方法标识：** `deactivate_account`

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
| `name` | string | 否 | "default" | ACME 账户配置文件名。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "default": "default",
      "description": "ACME 账户配置文件名。",
      "format": "pve-configid",
      "format_description": "name",
      "optional": 1,
      "type": "string",
      "typetext": "<name>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

## GET `/cluster/acme/account/{name}`

返回现有 ACME 账户信息。

**方法标识：** `get_account`

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
| `name` | string | 否 | "default" | ACME 账户配置文件名。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "default": "default",
      "description": "ACME 账户配置文件名。",
      "format": "pve-configid",
      "format_description": "name",
      "optional": 1,
      "type": "string",
      "typetext": "<name>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "additionalProperties": 0,
  "properties": {
    "account": {
      "optional": 1,
      "renderer": "yaml",
      "type": "object"
    },
    "directory": {
      "description": "ACME CA 目录端点的 URL。",
      "optional": 1,
      "pattern": "^https?://.*",
      "type": "string"
    },
    "location": {
      "optional": 1,
      "type": "string"
    },
    "tos": {
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/acme/account/{name}`

向 CA 更新现有 ACME 账户信息。注意：不指定任何新账户信息会触发刷新。

**方法标识：** `update_account`

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
| `contact` | string | 否 | — | 联系电子邮件地址。 |
| `name` | string | 否 | "default" | ACME 账户配置文件名。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "contact": {
      "description": "联系电子邮件地址。",
      "format": "email-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "name": {
      "default": "default",
      "description": "ACME 账户配置文件名。",
      "format": "pve-configid",
      "format_description": "name",
      "optional": 1,
      "type": "string",
      "typetext": "<name>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/account/{name})。
