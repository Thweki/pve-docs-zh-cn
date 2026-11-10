# `/access/password`

原始接口路径：`/access/password`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/access/password`

更改用户密码。

**方法标识：** `change_password`

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
  "description": "每个用户都可以更改自己的密码。如果用户具有 'Realm.AllocateUser' 权限（作用于用户 <userid> 所属认证域），且对用户 <userid> 所属的某组的 /access/groups/<group> 具有 'User.Modify' 权限，则可以更改该用户的密码。对于 PAM 认证域，密码更改不会在  整个集群生效，仅适用于本地节点。"
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
| `confirmation-password` | string | 否 | — | 执行更改的用户的当前密码。 |
| `password` | string | 是 | — | 新密码。 |
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "confirmation-password": {
      "description": "执行更改的用户的当前密码。",
      "maxLength": 64,
      "minLength": 5,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "新密码。",
      "maxLength": 64,
      "minLength": 8,
      "type": "string",
      "typetext": "<string>"
    },
    "userid": {
      "description": "完整用户 ID，采用 `name@realm` 格式。",
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
