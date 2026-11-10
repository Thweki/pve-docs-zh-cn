# `/cluster/firewall/groups`

原始接口路径：`/cluster/firewall/groups`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/firewall/groups`

List security groups.

**权限**

```json
{
  "user": "all"
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
  "items": {
    "properties": {
      "comment": {
        "description": "Optional comment or description.",
        "optional": 1,
        "type": "string"
      },
      "digest": {
        "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
        "maxLength": 64,
        "optional": 0,
        "type": "string"
      },
      "group": {
        "description": "Security Group name.",
        "maxLength": 18,
        "minLength": 2,
        "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{group}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/firewall/groups`

Create new security group.

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
| `comment` | string | 否 | — |  |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `group` | string | 是 | — | Security Group name. |
| `rename` | string | 否 | — | Rename/update an existing security group. You can set 'rename' to the same value as 'name' to update the 'comment' of an existing group. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "format": "pve-fw-comment-spec",
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
    "group": {
      "description": "Security Group name.",
      "maxLength": 18,
      "minLength": 2,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
      "type": "string"
    },
    "rename": {
      "description": "Rename/update an existing security group. You can set 'rename' to the same value as 'name' to update the 'comment' of an existing group.",
      "maxLength": 18,
      "minLength": 2,
      "optional": 1,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/firewall/groups)。
