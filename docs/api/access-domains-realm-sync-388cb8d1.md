# `/access/domains/{realm}/sync`

原始接口路径：`/access/domains/{realm}/sync`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/domains/{realm}/sync`

将用户和/或组从配置的 LDAP 同步到 user.cfg。注意：同步组的名称为 'name-$realm'，因此请确保这些组尚不存在，以防覆盖。

**方法标识：** `sync`

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
  "description": "需要对 '/access/realm/<realm>' 具有 'Realm.AllocateUser' 权限，以及  对 '/access/groups/' 具有 'User.Modify' 权限。"
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
| `dry-run` | boolean | 否 | 0 | 如果设置，则不写入任何内容。 |
| `enable-new` | boolean | 否 | "1" | 立即启用新同步的用户。 |
| `full` | boolean | 否 | — | 已弃用：请改用 'remove-vanished'。如果设置，则将 LDAP 目录视为权威来源，删除同步未返回的用户或组，并移除同步用户的所有本地修改属性。如果未设置，则仅同步同步数据中存在的信息，不会删除或修改其他任何内容。 |
| `purge` | boolean | 否 | — | 已弃用：请改用 'remove-vanished'。移除同步期间从配置中移除的用户或组的 ACL。 |
| `realm` | string | 是 | — | 认证域 ID |
| `remove-vanished` | string | 否 | "none" | 以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。 |
| `scope` | string | 否 | — | 选择要同步的内容。；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0,
      "description": "如果设置，则不写入任何内容。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enable-new": {
      "default": "1",
      "description": "立即启用新同步的用户。",
      "optional": "1",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "full": {
      "description": "已弃用：请改用 'remove-vanished'。如果设置，则将 LDAP 目录视为权威来源，删除同步未返回的用户或组，并移除同步用户的所有本地修改属性。如果未设置，则仅同步同步数据中存在的信息，不会删除或修改其他任何内容。",
      "optional": "1",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "purge": {
      "description": "已弃用：请改用 'remove-vanished'。移除同步期间从配置中移除的用户或组的 ACL。",
      "optional": "1",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "realm": {
      "description": "认证域 ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    },
    "remove-vanished": {
      "default": "none",
      "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
      "optional": "1",
      "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
      "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "scope": {
      "description": "选择要同步的内容。",
      "enum": [
        "users",
        "groups",
        "both"
      ],
      "optional": "1",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "工作任务 UPID",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains/{realm}/sync)。
