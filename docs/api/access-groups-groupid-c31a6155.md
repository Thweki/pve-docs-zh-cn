# `/access/groups/{groupid}`

原始接口路径：`/access/groups/{groupid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/groups/{groupid}`

Delete group.

**方法标识：** `delete_group`

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
| `groupid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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

## GET `/access/groups/{groupid}`

Get group configuration.

**方法标识：** `read_group`

**权限**

```json
{
  "check": [
    "perm",
    "/access/groups",
    [
      "Sys.Audit",
      "Group.Allocate"
    ],
    "any",
    1
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
| `groupid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
  "additionalProperties": 0,
  "properties": {
    "comment": {
      "optional": 1,
      "type": "string"
    },
    "members": {
      "items": {
        "description": "Full User ID, in the `name@realm` format.",
        "format": "pve-userid",
        "maxLength": 64,
        "type": "string"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

## PUT `/access/groups/{groupid}`

Update group data.

**方法标识：** `update_group`

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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/groups/{groupid})。
