# `/access/domains/{realm}/sync`

原始接口路径：`/access/domains/{realm}/sync`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/domains/{realm}/sync`

Syncs users and/or groups from the configured LDAP to user.cfg. NOTE: Synced groups will have the name 'name-$realm', so make sure those groups do not exist to prevent overwriting.

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
| `dry-run` | boolean | 否 | 0 | If set, does not write anything. |
| `enable-new` | boolean | 否 | "1" | Enable newly synced users immediately. |
| `full` | boolean | 否 | — | DEPRECATED: use 'remove-vanished' instead. If set, uses the LDAP Directory as source of truth, deleting users or groups not returned from the sync and removing all locally modified properties of synced users. If not set, only syncs information which is present in the synced data, and does not delete or modify anything else. |
| `purge` | boolean | 否 | — | DEPRECATED: use 'remove-vanished' instead. Remove ACLs for users or groups which were removed from the config during a sync. |
| `realm` | string | 是 | — | Authentication domain ID |
| `remove-vanished` | string | 否 | "none" | A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: 'entry' removes the user/group when not returned from the sync. 'properties' removes the set properties on existing user/group that do not appear in the source (even custom ones). 'acl' removes acls when the user/group is not returned from the sync. Instead of a list it also can be 'none' (the default). |
| `scope` | string | 否 | — | Select what to sync.；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {
      "default": 0,
      "description": "If set, does not write anything.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "enable-new": {
      "default": "1",
      "description": "Enable newly synced users immediately.",
      "optional": "1",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "full": {
      "description": "DEPRECATED: use 'remove-vanished' instead. If set, uses the LDAP Directory as source of truth, deleting users or groups not returned from the sync and removing all locally modified properties of synced users. If not set, only syncs information which is present in the synced data, and does not delete or modify anything else.",
      "optional": "1",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "purge": {
      "description": "DEPRECATED: use 'remove-vanished' instead. Remove ACLs for users or groups which were removed from the config during a sync.",
      "optional": "1",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "realm": {
      "description": "Authentication domain ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    },
    "remove-vanished": {
      "default": "none",
      "description": "A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: 'entry' removes the user/group when not returned from the sync. 'properties' removes the set properties on existing user/group that do not appear in the source (even custom ones). 'acl' removes acls when the user/group is not returned from the sync. Instead of a list it also can be 'none' (the default).",
      "optional": "1",
      "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none",
      "type": "string",
      "typetext": "([acl];[properties];[entry])|none"
    },
    "scope": {
      "description": "Select what to sync.",
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
  "description": "Worker Task-UPID",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains/{realm}/sync)。
