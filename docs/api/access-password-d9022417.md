# `/access/password`

原始接口路径：`/access/password`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/access/password`

Change user password.

**权限**

```json
{
  "check": [
    "or",
    [
      "userid-param",
      "self"
    ],
    [
      "and",
      [
        "userid-param",
        "Realm.AllocateUser"
      ],
      [
        "userid-group",
        [
          "User.Modify"
        ]
      ]
    ]
  ],
  "description": "Each user is allowed to change their own password. A user can change the password of another user if they have 'Realm.AllocateUser' (on the realm of user <userid>) and 'User.Modify' permission on /access/groups/<group> on a group where user <userid> is member of. For the PAM realm, a password change does not take effect cluster-wide, but only applies to the local node."
}
```

**允许 API 令牌**

```json
0
```

**受保护接口**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `confirmation-password` | string | 否 | — | The current password of the user performing the change. |
| `password` | string | 是 | — | The new password. |
| `userid` | string | 是 | — | Full User ID, in the `name@realm` format. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "confirmation-password": {
      "description": "The current password of the user performing the change.",
      "maxLength": 64,
      "minLength": 5,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "The new password.",
      "maxLength": 64,
      "minLength": 8,
      "type": "string",
      "typetext": "<string>"
    },
    "userid": {
      "description": "Full User ID, in the `name@realm` format.",
      "format": "pve-userid",
      "maxLength": 64,
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/password)。
