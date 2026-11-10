# `/cluster/jobs/realm-sync/{id}`

原始接口路径：`/cluster/jobs/realm-sync/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/jobs/realm-sync/{id}`

删除 realm-sync 作业定义。

**方法标识：** `delete_job`

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

读取 realm-sync 作业定义。

**方法标识：** `read_job`

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

创建新的 realm-sync 作业。

**方法标识：** `create_job`

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
  "description": "需要对 '/access/realm/<realm>' 的 'Realm.AllocateUser' 权限以及对 '/access/groups/' 的 'User.Modify' 权限。"
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
| `comment` | string | 否 | — | 作业描述。 |
| `enable-new` | boolean | 否 | "1" | 立即启用新同步的用户。 |
| `enabled` | boolean | 否 | 1 | 确定是否启用作业。 |
| `id` | string | 是 | — | 作业 ID。 |
| `realm` | string | 否 | — | 认证域 ID |
| `remove-vanished` | string | 否 | "none" | 以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。 |
| `schedule` | string | 是 | — | 备份计划。格式是 `systemd` 日历事件的子集。 |
| `scope` | string | 否 | — | 选择要同步的内容。；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "作业描述。",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable-new": {
      "default": "1",
      "description": "立即启用新同步的用户。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enabled": {
      "default": 1,
      "description": "确定是否启用作业。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "作业 ID。",
      "format": "pve-configid",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "realm": {
      "description": "认证域 ID",
      "format": "pve-realm",
      "maxLength": 32,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "remove-vanished": {
      "default": "none",
      "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
      "optional": 1,
      "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
      "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "scope": {
      "description": "选择要同步的内容。",
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

更新 realm-sync 作业定义。

**方法标识：** `update_job`

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
  "description": "需要对 '/access/realm/<realm>' 的 'Realm.AllocateUser' 权限以及对 '/access/groups/' 的 'User.Modify' 权限。"
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
| `comment` | string | 否 | — | 作业描述。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `enable-new` | boolean | 否 | "1" | 立即启用新同步的用户。 |
| `enabled` | boolean | 否 | 1 | 确定是否启用作业。 |
| `id` | string | 是 | — | 作业 ID。 |
| `remove-vanished` | string | 否 | "none" | 以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。 |
| `schedule` | string | 是 | — | 备份计划。格式是 `systemd` 日历事件的子集。 |
| `scope` | string | 否 | — | 选择要同步的内容。；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "description": "作业描述。",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enable-new": {
      "default": "1",
      "description": "立即启用新同步的用户。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enabled": {
      "default": 1,
      "description": "确定是否启用作业。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "作业 ID。",
      "format": "pve-configid",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "remove-vanished": {
      "default": "none",
      "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
      "optional": 1,
      "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
      "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "schedule": {
      "description": "备份计划。格式是 `systemd` 日历事件的子集。",
      "format": "pve-calendar-event",
      "maxLength": 128,
      "type": "string",
      "typetext": "<string>"
    },
    "scope": {
      "description": "选择要同步的内容。",
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
