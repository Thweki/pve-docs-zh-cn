# `/cluster/notifications/endpoints/smtp`

原始接口路径：`/cluster/notifications/endpoints/smtp`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/notifications/endpoints/smtp`

Returns a list of all smtp endpoints

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Audit"
      ]
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

此操作没有请求参数。

### 返回值

```json
{
  "items": {
    "properties": {
      "author": {
        "description": "Author of the mail. Defaults to 'Proxmox VE'.",
        "optional": 1,
        "type": "string"
      },
      "comment": {
        "description": "Comment",
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "default": 0,
        "description": "Disable this target",
        "optional": 1,
        "type": "boolean"
      },
      "from-address": {
        "description": "`From` address for the mail",
        "type": "string"
      },
      "mailto": {
        "description": "List of email recipients",
        "items": {
          "format": "email-or-username",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "mailto-user": {
        "description": "List of users",
        "items": {
          "format": "pve-userid",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      },
      "mode": {
        "default": "tls",
        "description": "Determine which encryption method shall be used for the connection.",
        "enum": [
          "insecure",
          "starttls",
          "tls"
        ],
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "The name of the endpoint.",
        "format": "pve-configid",
        "type": "string"
      },
      "origin": {
        "description": "Show if this entry was created by a user or was built-in",
        "enum": [
          "user-created",
          "builtin",
          "modified-builtin"
        ],
        "type": "string"
      },
      "port": {
        "description": "The port to be used. Defaults to 465 for TLS based connections, 587 for STARTTLS based connections and port 25 for insecure plain-text connections.",
        "optional": 1,
        "type": "integer"
      },
      "server": {
        "description": "The address of the SMTP server.",
        "type": "string"
      },
      "username": {
        "description": "Username for SMTP authentication",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/notifications/endpoints/smtp`

Create a new smtp endpoint

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/mapping/notifications",
      [
        "Mapping.Modify"
      ]
    ],
    [
      "or",
      [
        "perm",
        "/",
        [
          "Sys.Audit",
          "Sys.Modify"
        ]
      ],
      [
        "perm",
        "/",
        [
          "Sys.AccessNetwork"
        ]
      ]
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
| `author` | string | 否 | — | Author of the mail. Defaults to 'Proxmox VE'. |
| `comment` | string | 否 | — | Comment |
| `disable` | boolean | 否 | 0 | Disable this target |
| `from-address` | string | 是 | — | `From` address for the mail |
| `mailto` | array | 否 | — | List of email recipients |
| `mailto-user` | array | 否 | — | List of users |
| `mode` | string | 否 | "tls" | Determine which encryption method shall be used for the connection.；可选值：`insecure`, `starttls`, `tls` |
| `name` | string | 是 | — | The name of the endpoint. |
| `password` | string | 否 | — | Password for SMTP authentication |
| `port` | integer | 否 | — | The port to be used. Defaults to 465 for TLS based connections, 587 for STARTTLS based connections and port 25 for insecure plain-text connections. |
| `server` | string | 是 | — | The address of the SMTP server. |
| `username` | string | 否 | — | Username for SMTP authentication |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "author": {
      "description": "Author of the mail. Defaults to 'Proxmox VE'.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "description": "Comment",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "default": 0,
      "description": "Disable this target",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "from-address": {
      "description": "`From` address for the mail",
      "type": "string",
      "typetext": "<string>"
    },
    "mailto": {
      "description": "List of email recipients",
      "items": {
        "format": "email-or-username",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "mailto-user": {
      "description": "List of users",
      "items": {
        "format": "pve-userid",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "mode": {
      "default": "tls",
      "description": "Determine which encryption method shall be used for the connection.",
      "enum": [
        "insecure",
        "starttls",
        "tls"
      ],
      "optional": 1,
      "type": "string"
    },
    "name": {
      "description": "The name of the endpoint.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "Password for SMTP authentication",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "The port to be used. Defaults to 465 for TLS based connections, 587 for STARTTLS based connections and port 25 for insecure plain-text connections.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "server": {
      "description": "The address of the SMTP server.",
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "Username for SMTP authentication",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/notifications/endpoints/smtp)。
