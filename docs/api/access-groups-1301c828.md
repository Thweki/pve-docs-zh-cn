# `/access/groups`

原始接口路径：`/access/groups`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/groups`

Group index.

**方法标识：** `index`

**权限**

```json
{
  "description": "The returned list is restricted to groups where you have 'User.Modify', 'Sys.Audit' or 'Group.Allocate' permissions on /access/groups/<group>.",
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
        "optional": 1,
        "type": "string"
      },
      "groupid": {
        "format": "pve-groupid",
        "type": "string"
      },
      "users": {
        "description": "list of users which form this group",
        "format": "pve-userid-list",
        "optional": 1,
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{groupid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/access/groups`

Create new group.

**方法标识：** `create_group`

**权限**

```json
{
  "check": [
    "perm",
    "/access/groups",
    [
      "Group.Allocate"
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
| `groupid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "groupid": {
      "format": "pve-groupid",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/groups)。
