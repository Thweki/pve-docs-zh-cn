# `/cluster/jobs/realm-sync/{id}`

原始接口路径：`/cluster/jobs/realm-sync/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/jobs/realm-sync/{id}`

Delete realm-sync job definition.

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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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

## GET `/cluster/jobs/realm-sync/{id}`

Read realm-sync job definition.

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

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "format": "pve-configid",
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
  "type": "object"
}
```

## POST `/cluster/jobs/realm-sync/{id}`

Create new realm-sync job.

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/access/realm/{realm}",
      [
        "Realm.AllocateUser"
      ]
    ],
    [
      "perm",
      "/access/groups",
      [
        "User.Modify"
      ]
    ]
  ],
  "description": "'Realm.AllocateUser' on '/access/realm/<realm>' and 'User.Modify' permissions to '/access/groups/'."
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
| `comment` | string | 否 | — | Description for the Job. |
| `enable-new` | boolean | 否 | "1" | Enable newly synced users immediately. |
| `enabled` | boolean | 否 | 1 | Determines if the job is enabled. |
| `id` | string | 是 | — | The ID of the job. |
| `realm` | string | 否 | — | Authentication domain ID |
| `remove-vanished` | string | 否 | "none" | A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: 'entry' removes the user/group when not returned from the sync. 'properties' removes the set properties on existing user/group that do not appear in the source (even custom ones). 'acl' removes acls when the user/group is not returned from the sync. Instead of a list it also can be 'none' (the default). |
| `schedule` | string | 是 | — | Backup schedule. The format is a subset of `systemd` calendar events. |
| `scope` | string | 否 | — | Select what to sync.；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "Description for the Job.",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable-new": {
      "default": "1",
      "description": "Enable newly synced users immediately.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enabled": {
      "default": 1,
      "description": "Determines if the job is enabled.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "The ID of the job.",
      "format": "pve-configid",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "realm": {
      "description": "Authentication domain ID",
      "format": "pve-realm",
      "maxLength": 32,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "remove-vanished": {
      "default": "none",
      "description": "A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: 'entry' removes the user/group when not returned from the sync. 'properties' removes the set properties on existing user/group that do not appear in the source (even custom ones). 'acl' removes acls when the user/group is not returned from the sync. Instead of a list it also can be 'none' (the default).",
      "optional": 1,
      "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
      "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "schedule": {
      "description": "Backup schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "scope": {
      "description": "Select what to sync.",
      "enum": [
        "users",
        "groups",
        "both"
      ],
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## PUT `/cluster/jobs/realm-sync/{id}`

Update realm-sync job definition.

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/access/realm/{realm}",
      [
        "Realm.AllocateUser"
      ]
    ],
    [
      "perm",
      "/access/groups",
      [
        "User.Modify"
      ]
    ]
  ],
  "description": "'Realm.AllocateUser' on '/access/realm/<realm>' and 'User.Modify' permissions to '/access/groups/'."
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
| `comment` | string | 否 | — | Description for the Job. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `enable-new` | boolean | 否 | "1" | Enable newly synced users immediately. |
| `enabled` | boolean | 否 | 1 | Determines if the job is enabled. |
| `id` | string | 是 | — | The ID of the job. |
| `remove-vanished` | string | 否 | "none" | A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: 'entry' removes the user/group when not returned from the sync. 'properties' removes the set properties on existing user/group that do not appear in the source (even custom ones). 'acl' removes acls when the user/group is not returned from the sync. Instead of a list it also can be 'none' (the default). |
| `schedule` | string | 是 | — | Backup schedule. The format is a subset of `systemd` calendar events. |
| `scope` | string | 否 | — | Select what to sync.；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "Description for the Job.",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable-new": {
      "default": "1",
      "description": "Enable newly synced users immediately.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enabled": {
      "default": 1,
      "description": "Determines if the job is enabled.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "The ID of the job.",
      "format": "pve-configid",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "remove-vanished": {
      "default": "none",
      "description": "A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: 'entry' removes the user/group when not returned from the sync. 'properties' removes the set properties on existing user/group that do not appear in the source (even custom ones). 'acl' removes acls when the user/group is not returned from the sync. Instead of a list it also can be 'none' (the default).",
      "optional": 1,
      "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
      "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "schedule": {
      "description": "Backup schedule. The format is a subset of `systemd` calendar events.",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "scope": {
      "description": "Select what to sync.",
      "enum": [
        "users",
        "groups",
        "both"
      ],
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/jobs/realm-sync/{id})。
