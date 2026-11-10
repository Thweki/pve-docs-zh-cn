# access API

本章包含此资源组的全部接口，按路径和 HTTP 方法在同一页展开。接口路径、方法、参数、类型、约束和默认值保持原值。

## `/access` <a href="#api-access-ef531503" id="api-access-ef531503"></a>

原始接口路径：`/access`。

### GET `/access` <a href="#api-access-ef531503-get" id="api-access-ef531503-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-ef531503-get-parameters" id="api-access-ef531503-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-ef531503-get-returns" id="api-access-ef531503-get-returns"></a>

```text
{"items": {"properties": {"subdir": {"type": "string"}}, "type": "object"}, "links": [{"href": "{subdir}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access)。

## `/access/users` <a href="#api-access-users-ff4a891d" id="api-access-users-ff4a891d"></a>

原始接口路径：`/access/users`。

### GET `/access/users` <a href="#api-access-users-ff4a891d-get" id="api-access-users-ff4a891d-get"></a>

用户索引。

**方法标识：** `index`

**权限**

```text
{"description": "返回列表仅限于您对 '/access/groups' 或用户所属的组具有 'User.Modify' 或 'Sys.Audit' 权限的用户。但始终包含当前（已通过身份验证的）用户。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-ff4a891d-get-parameters" id="api-access-users-ff4a891d-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `enabled` | 类型：boolean；必填：否；默认值：—<br>enable 属性的可选过滤条件。 |
| `full` | 类型：boolean；必填：否；默认值：0<br>包含组和令牌信息。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"enabled": {"description": "enable 属性的可选过滤条件。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "full": {"default": 0, "description": "包含组和令牌信息。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-ff4a891d-get-returns" id="api-access-users-ff4a891d-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"maxLength": 2048, "optional": 1, "type": "string"}, "email": {"format": "email-opt", "maxLength": 254, "optional": 1, "type": "string"}, "enable": {"default": 1, "description": "启用账户（默认）。可设为 '0' 以禁用账户", "optional": 1, "type": "boolean"},
      "expire": {"description": "账户到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"}, "firstname": {"maxLength": 1024, "optional": 1, "type": "string"}, "groups": {"format": "pve-groupid-list", "optional": 1, "type": "string"},
      "keys": {"description": "双因素身份验证密钥（yubico）。", "optional": 1, "pattern": "[0-9a-zA-Z!=]{0,4096}", "type": "string"}, "lastname": {"maxLength": 1024, "optional": 1, "type": "string"}, "realm-type": {"description": "用户所属认证域的类型", "format": "pve-realm", "optional": 1, "type": "string"},
      "tfa-locked-until": {"description": "包含用户第二因素锁定截止时间的时间戳。", "optional": 1, "type": "integer"},
      "tokens": {
        "items": {
          "properties": {
            "comment": {"optional": 1, "type": "string"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"},
            "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean"}, "tokenid": {"description": "用户特定的令牌标识符。", "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)", "type": "string"}
          },
          "type": "object"
        },
        "optional": 1, "type": "array"
      },
      "totp-locked": {"description": "如果用户当前被锁定而无法使用 TOTP 因素，则为 true。", "optional": 1, "type": "boolean"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{userid}", "rel": "child"}], "type": "array"
}
```

### POST `/access/users` <a href="#api-access-users-ff4a891d-post" id="api-access-users-ff4a891d-post"></a>

创建新用户。

**方法标识：** `create_user`

**权限**

```text
{
  "check": ["and", ["userid-param", "Realm.AllocateUser"], ["userid-group", ["User.Modify"], "groups_param", "create"]],
  "description": "需要对用户 <userid> 所属认证域的 '/access/realm/<realm>' 具有 'Realm.AllocateUser' 权限，并且对任何指定组的 '/access/groups/<group>' 具有 'User.Modify' 权限（如果未传入任何组，则需要对 '/access/groups' 具有 'User.Modify' 权限。"
}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-ff4a891d-post-parameters" id="api-access-users-ff4a891d-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `email` | 类型：string；必填：否；默认值：—<br> |
| `enable` | 类型：boolean；必填：否；默认值：1<br>启用账户（默认）。可设为 '0' 以禁用账户 |
| `expire` | 类型：integer；必填：否；默认值：—<br>账户到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `firstname` | 类型：string；必填：否；默认值：—<br> |
| `groups` | 类型：string；必填：否；默认值：—<br> |
| `keys` | 类型：string；必填：否；默认值：—<br>双因素身份验证密钥（yubico）。 |
| `lastname` | 类型：string；必填：否；默认值：—<br> |
| `password` | 类型：string；必填：否；默认值：—<br>初始密码。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"maxLength": 2048, "optional": 1, "type": "string", "typetext": "<string>"}, "email": {"format": "email-opt", "maxLength": 254, "optional": 1, "type": "string", "typetext": "<string>"},
    "enable": {"default": 1, "description": "启用账户（默认）。可设为 '0' 以禁用账户", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "expire": {"description": "账户到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "firstname": {"maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"}, "groups": {"format": "pve-groupid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "keys": {"description": "双因素身份验证密钥（yubico）。", "optional": 1, "pattern": "[0-9a-zA-Z!=]{0,4096}", "type": "string"}, "lastname": {"maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"},
    "password": {"description": "初始密码。", "maxLength": 64, "minLength": 8, "optional": 1, "type": "string", "typetext": "<string>"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-users-ff4a891d-post-returns" id="api-access-users-ff4a891d-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users)。

## `/access/users/{userid}` <a href="#api-access-users-userid-aad17cce" id="api-access-users-userid-aad17cce"></a>

原始接口路径：`/access/users/{userid}`。

### DELETE `/access/users/{userid}` <a href="#api-access-users-userid-aad17cce-delete" id="api-access-users-userid-aad17cce-delete"></a>

删除用户。

**方法标识：** `delete_user`

**权限**

```text
{"check": ["and", ["userid-param", "Realm.AllocateUser"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-aad17cce-delete-parameters" id="api-access-users-userid-aad17cce-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-userid-aad17cce-delete-returns" id="api-access-users-userid-aad17cce-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/access/users/{userid}` <a href="#api-access-users-userid-aad17cce-get" id="api-access-users-userid-aad17cce-get"></a>

获取用户配置。

**方法标识：** `read_user`

**权限**

```text
{"check": ["userid-group", ["User.Modify", "Sys.Audit"]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-users-userid-aad17cce-get-parameters" id="api-access-users-userid-aad17cce-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-userid-aad17cce-get-returns" id="api-access-users-userid-aad17cce-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"maxLength": 2048, "optional": 1, "type": "string"}, "email": {"format": "email-opt", "maxLength": 254, "optional": 1, "type": "string"}, "enable": {"default": 1, "description": "启用账户（默认）。可设为 '0' 以禁用账户", "optional": 1, "type": "boolean"},
    "expire": {"description": "账户到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"}, "firstname": {"maxLength": 1024, "optional": 1, "type": "string"}, "groups": {"items": {"format": "pve-groupid", "type": "string"}, "optional": 1, "type": "array"},
    "keys": {"description": "双因素身份验证密钥（yubico）。", "optional": 1, "pattern": "[0-9a-zA-Z!=]{0,4096}", "type": "string"}, "lastname": {"maxLength": 1024, "optional": 1, "type": "string"},
    "tokens": {
      "additionalProperties": {
        "properties": {
          "comment": {"optional": 1, "type": "string"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"},
          "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean"}
        },
        "type": "object"
      },
      "optional": 1, "type": "object"
    }
  },
  "type": "object"
}
```

### PUT `/access/users/{userid}` <a href="#api-access-users-userid-aad17cce-put" id="api-access-users-userid-aad17cce-put"></a>

更新用户配置。

**方法标识：** `update_user`

**权限**

```text
{"check": ["userid-group", ["User.Modify"], "groups_param", "update"]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-aad17cce-put-parameters" id="api-access-users-userid-aad17cce-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `append` | 类型：boolean；必填：否；默认值：—<br> |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `email` | 类型：string；必填：否；默认值：—<br> |
| `enable` | 类型：boolean；必填：否；默认值：1<br>启用账户（默认）。可设为 '0' 以禁用账户 |
| `expire` | 类型：integer；必填：否；默认值：—<br>账户到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `firstname` | 类型：string；必填：否；默认值：—<br> |
| `groups` | 类型：string；必填：否；默认值：—<br> |
| `keys` | 类型：string；必填：否；默认值：—<br>双因素身份验证密钥（yubico）。 |
| `lastname` | 类型：string；必填：否；默认值：—<br> |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "append": {"optional": 1, "requires": "groups", "type": "boolean", "typetext": "<boolean>"}, "comment": {"maxLength": 2048, "optional": 1, "type": "string", "typetext": "<string>"}, "email": {"format": "email-opt", "maxLength": 254, "optional": 1, "type": "string", "typetext": "<string>"},
    "enable": {"default": 1, "description": "启用账户（默认）。可设为 '0' 以禁用账户", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "expire": {"description": "账户到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "firstname": {"maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"}, "groups": {"format": "pve-groupid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "keys": {"description": "双因素身份验证密钥（yubico）。", "optional": 1, "pattern": "[0-9a-zA-Z!=]{0,4096}", "type": "string"}, "lastname": {"maxLength": 1024, "optional": 1, "type": "string", "typetext": "<string>"},
    "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-users-userid-aad17cce-put-returns" id="api-access-users-userid-aad17cce-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid})。

## `/access/users/{userid}/tfa` <a href="#api-access-users-userid-tfa-9dcb2591" id="api-access-users-userid-tfa-9dcb2591"></a>

原始接口路径：`/access/users/{userid}/tfa`。

### GET `/access/users/{userid}/tfa` <a href="#api-access-users-userid-tfa-9dcb2591-get" id="api-access-users-userid-tfa-9dcb2591-get"></a>

获取用户 TFA 类型（个人及认证域）。

**方法标识：** `read_user_tfa_type`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify", "Sys.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-tfa-9dcb2591-get-parameters" id="api-access-users-userid-tfa-9dcb2591-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `multiple` | 类型：boolean；必填：否；默认值：0<br>将所有条目作为数组请求。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"multiple": {"default": 0, "description": "将所有条目作为数组请求。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}
}
```

</details>

#### 返回值 <a href="#api-access-users-userid-tfa-9dcb2591-get-returns" id="api-access-users-userid-tfa-9dcb2591-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "realm": {"description": "用户所属认证域设置的 TFA 类型（如有）。", "enum": ["oath", "yubico"], "optional": 1, "type": "string"},
    "types": {"description": "用户配置的 TFA 类型数组（如有）。仅在未传入 'multiple' 时可用。", "items": {"description": "TFA 类型。", "enum": ["totp", "u2f", "yubico", "webauthn", "recovedry"], "type": "string"}, "optional": 1, "type": "array"},
    "user": {"description": "用户设置的 TFA 类型（如有）。仅在未传入 'multiple' 时设置。", "enum": ["oath", "u2f"], "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/tfa)。

## `/access/users/{userid}/unlock-tfa` <a href="#api-access-users-userid-unlock-tfa-1b330aed" id="api-access-users-userid-unlock-tfa-1b330aed"></a>

原始接口路径：`/access/users/{userid}/unlock-tfa`。

### PUT `/access/users/{userid}/unlock-tfa` <a href="#api-access-users-userid-unlock-tfa-1b330aed-put" id="api-access-users-userid-unlock-tfa-1b330aed-put"></a>

解除用户 TFA 身份验证锁定。

**方法标识：** `unlock_tfa`

**权限**

```text
{"check": ["userid-group", ["User.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-unlock-tfa-1b330aed-put-parameters" id="api-access-users-userid-unlock-tfa-1b330aed-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-userid-unlock-tfa-1b330aed-put-returns" id="api-access-users-userid-unlock-tfa-1b330aed-put-returns"></a>

```text
{"type": "boolean"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/unlock-tfa)。

## `/access/users/{userid}/token` <a href="#api-access-users-userid-token-ad96dab5" id="api-access-users-userid-token-ad96dab5"></a>

原始接口路径：`/access/users/{userid}/token`。

### GET `/access/users/{userid}/token` <a href="#api-access-users-userid-token-ad96dab5-get" id="api-access-users-userid-token-ad96dab5-get"></a>

获取用户 API 令牌。

**方法标识：** `token_index`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-users-userid-token-ad96dab5-get-parameters" id="api-access-users-userid-token-ad96dab5-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-userid-token-ad96dab5-get-returns" id="api-access-users-userid-token-ad96dab5-get-returns"></a>

```text
{
  "items": {
    "properties": {
      "comment": {"optional": 1, "type": "string"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"},
      "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean"}, "tokenid": {"description": "用户特定的令牌标识符。", "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{tokenid}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/token)。

## `/access/users/{userid}/token/{tokenid}` <a href="#api-access-users-userid-token-tokenid-29a42318" id="api-access-users-userid-token-tokenid-29a42318"></a>

原始接口路径：`/access/users/{userid}/token/{tokenid}`。

### DELETE `/access/users/{userid}/token/{tokenid}` <a href="#api-access-users-userid-token-tokenid-29a42318-delete" id="api-access-users-userid-token-tokenid-29a42318-delete"></a>

移除特定用户的 API 令牌。

**方法标识：** `remove_token`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-token-tokenid-29a42318-delete-parameters" id="api-access-users-userid-token-tokenid-29a42318-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `tokenid` | 类型：string；必填：是；默认值：—<br>用户特定的令牌标识符。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"tokenid": {"description": "用户特定的令牌标识符。", "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)", "type": "string"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-userid-token-tokenid-29a42318-delete-returns" id="api-access-users-userid-token-tokenid-29a42318-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/access/users/{userid}/token/{tokenid}` <a href="#api-access-users-userid-token-tokenid-29a42318-get" id="api-access-users-userid-token-tokenid-29a42318-get"></a>

获取特定 API 令牌信息。

**方法标识：** `read_token`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-users-userid-token-tokenid-29a42318-get-parameters" id="api-access-users-userid-token-tokenid-29a42318-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `tokenid` | 类型：string；必填：是；默认值：—<br>用户特定的令牌标识符。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"tokenid": {"description": "用户特定的令牌标识符。", "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)", "type": "string"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-users-userid-token-tokenid-29a42318-get-returns" id="api-access-users-userid-token-tokenid-29a42318-get-returns"></a>

```text
{
  "properties": {
    "comment": {"optional": 1, "type": "string"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"},
    "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean"}
  },
  "type": "object"
}
```

### POST `/access/users/{userid}/token/{tokenid}` <a href="#api-access-users-userid-token-tokenid-29a42318-post" id="api-access-users-userid-token-tokenid-29a42318-post"></a>

为特定用户生成新的 API 令牌。注意：返回 API 令牌值，必须保存，因为之后无法再次获取！

**方法标识：** `generate_token`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-token-tokenid-29a42318-post-parameters" id="api-access-users-userid-token-tokenid-29a42318-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `expire` | 类型：integer；必填：否；默认值："same as user"<br>API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `privsep` | 类型：boolean；必填：否；默认值：1<br>使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。 |
| `tokenid` | 类型：string；必填：是；默认值：—<br>用户特定的令牌标识符。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"optional": 1, "type": "string", "typetext": "<string>"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "tokenid": {"description": "用户特定的令牌标识符。", "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)", "type": "string"},
    "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-users-userid-token-tokenid-29a42318-post-returns" id="api-access-users-userid-token-tokenid-29a42318-post-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "full-tokenid": {"description": "完整令牌 ID。", "format_description": "<userid>!<tokenid>", "type": "string"},
    "info": {
      "properties": {
        "comment": {"optional": 1, "type": "string"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"},
        "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean"}
      },
      "type": "object"
    },
    "value": {"description": "用于身份验证的 API 令牌值。", "type": "string"}
  },
  "type": "object"
}
```

### PUT `/access/users/{userid}/token/{tokenid}` <a href="#api-access-users-userid-token-tokenid-29a42318-put" id="api-access-users-userid-token-tokenid-29a42318-put"></a>

更新特定用户的 API 令牌。注意：设置 'regenerate' 时，必须保存返回的令牌值，因为之后无法再次获取！

**方法标识：** `update_token_info`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-users-userid-token-tokenid-29a42318-put-parameters" id="api-access-users-userid-token-tokenid-29a42318-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `expire` | 类型：integer；必填：否；默认值："same as user"<br>API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。 |
| `privsep` | 类型：boolean；必填：否；默认值：1<br>使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。 |
| `regenerate` | 类型：boolean；必填：否；默认值：0<br>重新生成令牌的密钥值。此操作后，所有使用旧密钥的使用方都将失去访问权限。 |
| `tokenid` | 类型：string；必填：是；默认值：—<br>用户特定的令牌标识符。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "comment": {"optional": 1, "type": "string", "typetext": "<string>"}, "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer", "typetext": "<integer> (0 - N)"},
    "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "regenerate": {"default": 0, "description": "重新生成令牌的密钥值。此操作后，所有使用旧密钥的使用方都将失去访问权限。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "tokenid": {"description": "用户特定的令牌标识符。", "pattern": "(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)", "type": "string"},
    "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-users-userid-token-tokenid-29a42318-put-returns" id="api-access-users-userid-token-tokenid-29a42318-put-returns"></a>

```text
{
  "properties": {
    "comment": {"optional": 1, "type": "string"}, "expire": {"default": "same as user", "description": "API 令牌到期日期（自纪元起的秒数）。'0' 表示永不过期。", "minimum": 0, "optional": 1, "type": "integer"},
    "full-tokenid": {"description": "完整令牌 ID。仅在设置了 'regenerate' 时设置。", "format_description": "<userid>!<tokenid>", "optional": 1, "type": "string"}, "privsep": {"default": 1, "description": "使用单独的 ACL 限制 API 令牌权限（默认），或授予相应用户的全部权限。", "optional": 1, "type": "boolean"},
    "value": {"description": "用于身份验证的 API 令牌值。仅在设置了 'regenerate' 时设置。", "optional": 1, "type": "string"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/token/{tokenid})。

## `/access/groups` <a href="#api-access-groups-1301c828" id="api-access-groups-1301c828"></a>

原始接口路径：`/access/groups`。

### GET `/access/groups` <a href="#api-access-groups-1301c828-get" id="api-access-groups-1301c828-get"></a>

组索引。

**方法标识：** `index`

**权限**

```text
{"description": "返回列表仅限于您具有 'User.Modify'、'Sys.Audit'  或 'Group.Allocate' 权限（作用于 /access/groups/<group>）的组。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-groups-1301c828-get-parameters" id="api-access-groups-1301c828-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-groups-1301c828-get-returns" id="api-access-groups-1301c828-get-returns"></a>

```text
{
  "items": {"properties": {"comment": {"optional": 1, "type": "string"}, "groupid": {"format": "pve-groupid", "type": "string"}, "users": {"description": "组成此组的用户列表", "format": "pve-userid-list", "optional": 1, "type": "string"}}, "type": "object"}, "links": [{"href": "{groupid}", "rel": "child"}],
  "type": "array"
}
```

### POST `/access/groups` <a href="#api-access-groups-1301c828-post" id="api-access-groups-1301c828-post"></a>

创建新组。

**方法标识：** `create_group`

**权限**

```text
{"check": ["perm", "/access/groups", ["Group.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-groups-1301c828-post-parameters" id="api-access-groups-1301c828-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `groupid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"comment": {"optional": 1, "type": "string", "typetext": "<string>"}, "groupid": {"format": "pve-groupid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-groups-1301c828-post-returns" id="api-access-groups-1301c828-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/groups)。

## `/access/groups/{groupid}` <a href="#api-access-groups-groupid-c31a6155" id="api-access-groups-groupid-c31a6155"></a>

原始接口路径：`/access/groups/{groupid}`。

### DELETE `/access/groups/{groupid}` <a href="#api-access-groups-groupid-c31a6155-delete" id="api-access-groups-groupid-c31a6155-delete"></a>

删除组。

**方法标识：** `delete_group`

**权限**

```text
{"check": ["perm", "/access/groups", ["Group.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-groups-groupid-c31a6155-delete-parameters" id="api-access-groups-groupid-c31a6155-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `groupid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"groupid": {"format": "pve-groupid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-groups-groupid-c31a6155-delete-returns" id="api-access-groups-groupid-c31a6155-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/access/groups/{groupid}` <a href="#api-access-groups-groupid-c31a6155-get" id="api-access-groups-groupid-c31a6155-get"></a>

获取组配置。

**方法标识：** `read_group`

**权限**

```text
{"check": ["perm", "/access/groups", ["Sys.Audit", "Group.Allocate"], "any", 1]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-groups-groupid-c31a6155-get-parameters" id="api-access-groups-groupid-c31a6155-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `groupid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"groupid": {"format": "pve-groupid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-groups-groupid-c31a6155-get-returns" id="api-access-groups-groupid-c31a6155-get-returns"></a>

```text
{"additionalProperties": 0, "properties": {"comment": {"optional": 1, "type": "string"}, "members": {"items": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string"}, "type": "array"}}, "type": "object"}
```

### PUT `/access/groups/{groupid}` <a href="#api-access-groups-groupid-c31a6155-put" id="api-access-groups-groupid-c31a6155-put"></a>

更新组数据。

**方法标识：** `update_group`

**权限**

```text
{"check": ["perm", "/access/groups", ["Group.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-groups-groupid-c31a6155-put-parameters" id="api-access-groups-groupid-c31a6155-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `comment` | 类型：string；必填：否；默认值：—<br> |
| `groupid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"comment": {"optional": 1, "type": "string", "typetext": "<string>"}, "groupid": {"format": "pve-groupid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-groups-groupid-c31a6155-put-returns" id="api-access-groups-groupid-c31a6155-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/groups/{groupid})。

## `/access/roles` <a href="#api-access-roles-664f9b93" id="api-access-roles-664f9b93"></a>

原始接口路径：`/access/roles`。

### GET `/access/roles` <a href="#api-access-roles-664f9b93-get" id="api-access-roles-664f9b93-get"></a>

角色索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-roles-664f9b93-get-parameters" id="api-access-roles-664f9b93-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-roles-664f9b93-get-returns" id="api-access-roles-664f9b93-get-returns"></a>

```text
{"items": {"properties": {"privs": {"format": "pve-priv-list", "optional": 1, "type": "string"}, "roleid": {"format": "pve-roleid", "type": "string"}, "special": {"default": 0, "optional": 1, "type": "boolean"}}, "type": "object"}, "links": [{"href": "{roleid}", "rel": "child"}], "type": "array"}
```

### POST `/access/roles` <a href="#api-access-roles-664f9b93-post" id="api-access-roles-664f9b93-post"></a>

创建新角色。

**方法标识：** `create_role`

**权限**

```text
{"check": ["perm", "/access", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-roles-664f9b93-post-parameters" id="api-access-roles-664f9b93-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `privs` | 类型：string；必填：否；默认值：—<br> |
| `roleid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"privs": {"format": "pve-priv-list", "optional": 1, "type": "string", "typetext": "<string>"}, "roleid": {"format": "pve-roleid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-roles-664f9b93-post-returns" id="api-access-roles-664f9b93-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/roles)。

## `/access/roles/{roleid}` <a href="#api-access-roles-roleid-d4beb42c" id="api-access-roles-roleid-d4beb42c"></a>

原始接口路径：`/access/roles/{roleid}`。

### DELETE `/access/roles/{roleid}` <a href="#api-access-roles-roleid-d4beb42c-delete" id="api-access-roles-roleid-d4beb42c-delete"></a>

删除角色。

**方法标识：** `delete_role`

**权限**

```text
{"check": ["perm", "/access", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-roles-roleid-d4beb42c-delete-parameters" id="api-access-roles-roleid-d4beb42c-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `roleid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"roleid": {"format": "pve-roleid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-roles-roleid-d4beb42c-delete-returns" id="api-access-roles-roleid-d4beb42c-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/access/roles/{roleid}` <a href="#api-access-roles-roleid-d4beb42c-get" id="api-access-roles-roleid-d4beb42c-get"></a>

获取角色配置。

**方法标识：** `read_role`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-roles-roleid-d4beb42c-get-parameters" id="api-access-roles-roleid-d4beb42c-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `roleid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"roleid": {"format": "pve-roleid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-roles-roleid-d4beb42c-get-returns" id="api-access-roles-roleid-d4beb42c-get-returns"></a>

```text
{
  "additionalProperties": 0,
  "properties": {
    "Datastore.Allocate": {"optional": 1, "type": "boolean"}, "Datastore.AllocateSpace": {"optional": 1, "type": "boolean"}, "Datastore.AllocateTemplate": {"optional": 1, "type": "boolean"}, "Datastore.Audit": {"optional": 1, "type": "boolean"}, "Group.Allocate": {"optional": 1, "type": "boolean"},
    "Mapping.Audit": {"optional": 1, "type": "boolean"}, "Mapping.Modify": {"optional": 1, "type": "boolean"}, "Mapping.Use": {"optional": 1, "type": "boolean"}, "Permissions.Modify": {"optional": 1, "type": "boolean"}, "Pool.Allocate": {"optional": 1, "type": "boolean"},
    "Pool.Audit": {"optional": 1, "type": "boolean"}, "Realm.Allocate": {"optional": 1, "type": "boolean"}, "Realm.AllocateUser": {"optional": 1, "type": "boolean"}, "SDN.Allocate": {"optional": 1, "type": "boolean"}, "SDN.Audit": {"optional": 1, "type": "boolean"}, "SDN.Use": {"optional": 1, "type": "boolean"},
    "Sys.AccessNetwork": {"optional": 1, "type": "boolean"}, "Sys.Audit": {"optional": 1, "type": "boolean"}, "Sys.Console": {"optional": 1, "type": "boolean"}, "Sys.Incoming": {"optional": 1, "type": "boolean"}, "Sys.Modify": {"optional": 1, "type": "boolean"}, "Sys.PowerMgmt": {"optional": 1, "type": "boolean"},
    "Sys.Syslog": {"optional": 1, "type": "boolean"}, "User.Modify": {"optional": 1, "type": "boolean"}, "VM.Allocate": {"optional": 1, "type": "boolean"}, "VM.Audit": {"optional": 1, "type": "boolean"}, "VM.Backup": {"optional": 1, "type": "boolean"}, "VM.Clone": {"optional": 1, "type": "boolean"},
    "VM.Config.CDROM": {"optional": 1, "type": "boolean"}, "VM.Config.CPU": {"optional": 1, "type": "boolean"}, "VM.Config.Cloudinit": {"optional": 1, "type": "boolean"}, "VM.Config.Disk": {"optional": 1, "type": "boolean"}, "VM.Config.HWType": {"optional": 1, "type": "boolean"},
    "VM.Config.Memory": {"optional": 1, "type": "boolean"}, "VM.Config.Network": {"optional": 1, "type": "boolean"}, "VM.Config.Options": {"optional": 1, "type": "boolean"}, "VM.Console": {"optional": 1, "type": "boolean"}, "VM.GuestAgent.Audit": {"optional": 1, "type": "boolean"},
    "VM.GuestAgent.FileRead": {"optional": 1, "type": "boolean"}, "VM.GuestAgent.FileSystemMgmt": {"optional": 1, "type": "boolean"}, "VM.GuestAgent.FileWrite": {"optional": 1, "type": "boolean"}, "VM.GuestAgent.Unrestricted": {"optional": 1, "type": "boolean"}, "VM.Migrate": {"optional": 1, "type": "boolean"},
    "VM.PowerMgmt": {"optional": 1, "type": "boolean"}, "VM.Replicate": {"optional": 1, "type": "boolean"}, "VM.Snapshot": {"optional": 1, "type": "boolean"}, "VM.Snapshot.Rollback": {"optional": 1, "type": "boolean"}
  },
  "type": "object"
}
```

### PUT `/access/roles/{roleid}` <a href="#api-access-roles-roleid-d4beb42c-put" id="api-access-roles-roleid-d4beb42c-put"></a>

更新现有角色。

**方法标识：** `update_role`

**权限**

```text
{"check": ["perm", "/access", ["Sys.Modify"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-roles-roleid-d4beb42c-put-parameters" id="api-access-roles-roleid-d4beb42c-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `append` | 类型：boolean；必填：否；默认值：—<br> |
| `privs` | 类型：string；必填：否；默认值：—<br> |
| `roleid` | 类型：string；必填：是；默认值：—<br> |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"append": {"optional": 1, "requires": "privs", "type": "boolean", "typetext": "<boolean>"}, "privs": {"format": "pve-priv-list", "optional": 1, "type": "string", "typetext": "<string>"}, "roleid": {"format": "pve-roleid", "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-roles-roleid-d4beb42c-put-returns" id="api-access-roles-roleid-d4beb42c-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/roles/{roleid})。

## `/access/acl` <a href="#api-access-acl-26eff873" id="api-access-acl-26eff873"></a>

原始接口路径：`/access/acl`。

### GET `/access/acl` <a href="#api-access-acl-26eff873-get" id="api-access-acl-26eff873-get"></a>

获取访问控制列表（ACL）。

**方法标识：** `read_acl`

**权限**

```text
{"description": "返回列表仅限于您有权修改其权限的对象。", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-acl-26eff873-get-parameters" id="api-access-acl-26eff873-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-acl-26eff873-get-returns" id="api-access-acl-26eff873-get-returns"></a>

```text
{
  "items": {
    "additionalProperties": 0,
    "properties": {"path": {"description": "访问控制路径", "type": "string"}, "propagate": {"default": 1, "description": "允许传播（继承）权限。", "optional": 1, "type": "boolean"}, "roleid": {"type": "string"}, "type": {"enum": ["user", "group", "token"], "type": "string"}, "ugid": {"type": "string"}},
    "type": "object"
  },
  "type": "array"
}
```

### PUT `/access/acl` <a href="#api-access-acl-26eff873-put" id="api-access-acl-26eff873-put"></a>

更新访问控制列表（添加或移除权限）。

**方法标识：** `update_acl`

**权限**

```text
{"check": ["perm-modify", "{path}"]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-acl-26eff873-put-parameters" id="api-access-acl-26eff873-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `delete` | 类型：boolean；必填：否；默认值：—<br>移除权限（而非添加）。 |
| `groups` | 类型：string；必填：否；默认值：—<br>组列表。 |
| `path` | 类型：string；必填：是；默认值：—<br>访问控制路径 |
| `propagate` | 类型：boolean；必填：否；默认值：1<br>允许传播（继承）权限。 |
| `roles` | 类型：string；必填：是；默认值：—<br>角色列表。 |
| `tokens` | 类型：string；必填：否；默认值：—<br>API 令牌列表。 |
| `users` | 类型：string；必填：否；默认值：—<br>用户列表。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "delete": {"description": "移除权限（而非添加）。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "groups": {"description": "组列表。", "format": "pve-groupid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "path": {"description": "访问控制路径", "type": "string", "typetext": "<string>"}, "propagate": {"default": 1, "description": "允许传播（继承）权限。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "roles": {"description": "角色列表。", "format": "pve-roleid-list", "type": "string", "typetext": "<string>"}, "tokens": {"description": "API 令牌列表。", "format": "pve-tokenid-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "users": {"description": "用户列表。", "format": "pve-userid-list", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-acl-26eff873-put-returns" id="api-access-acl-26eff873-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/acl)。

## `/access/domains` <a href="#api-access-domains-bb4462c8" id="api-access-domains-bb4462c8"></a>

原始接口路径：`/access/domains`。

### GET `/access/domains` <a href="#api-access-domains-bb4462c8-get" id="api-access-domains-bb4462c8-get"></a>

认证域索引。

**方法标识：** `index`

**权限**

```text
{"description": "任何人均可访问，因为登录框在用户通过身份验证之前就需要此列表。", "user": "world"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-domains-bb4462c8-get-parameters" id="api-access-domains-bb4462c8-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-domains-bb4462c8-get-returns" id="api-access-domains-bb4462c8-get-returns"></a>

```text
{
  "items": {
    "properties": {"comment": {"description": "注释。在登录窗口中选择域（认证域）时，GUI 使用此文本。", "optional": 1, "type": "string"}, "realm": {"type": "string"}, "tfa": {"description": "双因素身份验证提供程序。", "enum": ["yubico", "oath"], "optional": 1, "type": "string"}, "type": {"type": "string"}},
    "type": "object"
  },
  "links": [{"href": "{realm}", "rel": "child"}], "type": "array"
}
```

### POST `/access/domains` <a href="#api-access-domains-bb4462c8-post" id="api-access-domains-bb4462c8-post"></a>

添加认证服务器。

**方法标识：** `create`

**权限**

```text
{"check": ["perm", "/access/realm", ["Realm.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-domains-bb4462c8-post-parameters" id="api-access-domains-bb4462c8-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `acr-values` | 类型：string；必填：否；默认值：—<br>指定请求授权服务器在身份验证请求中使用的身份验证上下文类引用值。 |
| `audiences` | 类型：string；必填：否；默认值：—<br>除 'client-id' 外，也接受 OpenID 颁发者可能包含的受众列表。 |
| `autocreate` | 类型：boolean；必填：否；默认值：0<br>如果用户不存在，则自动创建。 |
| `base_dn` | 类型：string；必填：否；默认值：—<br>LDAP 基础域名 |
| `bind_dn` | 类型：string；必填：否；默认值：—<br>LDAP 绑定域名 |
| `capath` | 类型：string；必填：否；默认值："/etc/ssl/certs"<br>CA 证书存储路径 |
| `case-sensitive` | 类型：boolean；必填：否；默认值：1<br>用户名区分大小写 |
| `cert` | 类型：string；必填：否；默认值：—<br>客户端证书路径 |
| `certkey` | 类型：string；必填：否；默认值：—<br>客户端证书密钥路径 |
| `check-connection` | 类型：boolean；必填：否；默认值：0<br>检查到服务器的绑定连接。 |
| `client-id` | 类型：string；必填：否；默认值：—<br>OpenID 客户端 ID |
| `client-key` | 类型：string；必填：否；默认值：—<br>OpenID 客户端密钥 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `default` | 类型：boolean；必填：否；默认值：—<br>将此认证域用作默认认证域 |
| `domain` | 类型：string；必填：否；默认值：—<br>AD 域名 |
| `filter` | 类型：string；必填：否；默认值：—<br>用户同步的 LDAP 过滤器。 |
| `group_classes` | 类型：string；必填：否；默认值："groupOfNames, group, univentionGroup, ipausergroup"<br>组的 objectclass。 |
| `group_dn` | 类型：string；必填：否；默认值：—<br>组同步的 LDAP 基础域名。如果未设置，将使用 base_dn。 |
| `group_filter` | 类型：string；必填：否；默认值：—<br>组同步的 LDAP 过滤器。 |
| `group_name_attr` | 类型：string；必填：否；默认值：—<br>表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。 |
| `groups-autocreate` | 类型：boolean；必填：否；默认值：0<br>如果组不存在，则自动创建。 |
| `groups-claim` | 类型：string；必填：否；默认值：—<br>用于获取组的 OpenID 声明。 |
| `groups-overwrite` | 类型：boolean；必填：否；默认值：0<br>用户登录时将覆盖其所有组。 |
| `issuer-url` | 类型：string；必填：否；默认值：—<br>OpenID 颁发者 URL |
| `mode` | 类型：string；必填：否；默认值："ldap"<br>LDAP 协议模式。；可选值：`ldap`, `ldaps`, `ldap+starttls` |
| `password` | 类型：string；必填：否；默认值：—<br>LDAP 绑定密码。将保存于 '/etc/pve/priv/realm/&lt;REALM&gt;.pw'。 |
| `port` | 类型：integer；必填：否；默认值：—<br>服务器端口。 |
| `prompt` | 类型：string；必填：否；默认值：—<br>指定授权服务器是否提示最终用户重新身份验证并表示同意。 |
| `query-userinfo` | 类型：boolean；必填：否；默认值：1<br>启用查询 userinfo 端点以获取声明值。 |
| `realm` | 类型：string；必填：是；默认值：—<br>认证域 ID |
| `scopes` | 类型：string；必填：否；默认值："email profile"<br>指定应授权并返回的作用域（用户详细信息），例如 'email' 或 'profile'。 |
| `secure` | 类型：boolean；必填：否；默认值：—<br>使用安全的 LDAPS 协议。已弃用：请改用 'mode'。 |
| `server1` | 类型：string；必填：否；默认值：—<br>服务器 IP 地址（或 DNS 名称） |
| `server2` | 类型：string；必填：否；默认值：—<br>后备服务器 IP 地址（或 DNS 名称） |
| `sslversion` | 类型：string；必填：否；默认值：—<br>LDAPS TLS/SSL 版本。不建议使用早于 1.2 的版本！；可选值：`tlsv1`, `tlsv1_1`, `tlsv1_2`, `tlsv1_3` |
| `sync-defaults-options` | 类型：string；必填：否；默认值：—<br>同步行为的默认选项。 |
| `sync_attributes` | 类型：string；必填：否；默认值：—<br>以逗号分隔的 key=value 对列表，指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 'mail' 映射到 PVE 的 'email'，请填写  'email=mail'。默认情况下，每个 PVE 用户字段均由  同名 LDAP 属性表示。 |
| `tfa` | 类型：string；必填：否；默认值：—<br>使用双因素身份验证。 |
| `type` | 类型：string；必填：是；默认值：—<br>认证域类型。；可选值：`ad`, `ldap`, `openid`, `pam`, `pve` |
| `user_attr` | 类型：string；必填：否；默认值：—<br>LDAP 用户属性名称 |
| `user_classes` | 类型：string；必填：否；默认值："inetorgperson, posixaccount, person, user"<br>用户的 objectclass。 |
| `username-claim` | 类型：string；必填：否；默认值：—<br>用于生成唯一用户名的 OpenID 声明。 |
| `verify` | 类型：boolean；必填：否；默认值：0<br>验证服务器的 SSL 证书 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "acr-values": {"description": "指定请求授权服务器在身份验证请求中使用的身份验证上下文类引用值。", "optional": 1, "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$", "type": "string"},
    "audiences": {"description": "除 'client-id' 外，也接受 OpenID 颁发者可能包含的受众列表。", "optional": 1, "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$", "type": "string"}, "autocreate": {"default": 0, "description": "如果用户不存在，则自动创建。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "base_dn": {"description": "LDAP 基础域名", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "bind_dn": {"description": "LDAP 绑定域名", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "capath": {"default": "/etc/ssl/certs", "description": "CA 证书存储路径", "optional": 1, "type": "string", "typetext": "<string>"}, "case-sensitive": {"default": 1, "description": "用户名区分大小写", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "cert": {"description": "客户端证书路径", "optional": 1, "type": "string", "typetext": "<string>"}, "certkey": {"description": "客户端证书密钥路径", "optional": 1, "type": "string", "typetext": "<string>"},
    "check-connection": {"default": 0, "description": "检查到服务器的绑定连接。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "client-id": {"description": "OpenID 客户端 ID", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "client-key": {"description": "OpenID 客户端密钥", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "default": {"description": "将此认证域用作默认认证域", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "domain": {"description": "AD 域名", "maxLength": 256, "optional": 1, "pattern": "\\S+", "type": "string"},
    "filter": {"description": "用户同步的 LDAP 过滤器。", "maxLength": 2048, "optional": 1, "type": "string", "typetext": "<string>"},
    "group_classes": {"default": "groupOfNames, group, univentionGroup, ipausergroup", "description": "组的 objectclass。", "format": "ldap-simple-attr-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "group_dn": {"description": "组同步的 LDAP 基础域名。如果未设置，将使用 base_dn。", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "group_filter": {"description": "组同步的 LDAP 过滤器。", "maxLength": 2048, "optional": 1, "type": "string", "typetext": "<string>"},
    "group_name_attr": {"description": "表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。", "format": "ldap-simple-attr", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "groups-autocreate": {"default": 0, "description": "如果组不存在，则自动创建。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "groups-claim": {"description": "用于获取组的 OpenID 声明。", "maxLength": 256, "optional": 1, "pattern": "(?^:[A-Za-z0-9\\.\\-_]+)", "type": "string"},
    "groups-overwrite": {"default": 0, "description": "用户登录时将覆盖其所有组。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "issuer-url": {"description": "OpenID 颁发者 URL", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "mode": {"default": "ldap", "description": "LDAP 协议模式。", "enum": ["ldap", "ldaps", "ldap+starttls"], "optional": 1, "type": "string"}, "password": {"description": "LDAP 绑定密码。将保存于 '/etc/pve/priv/realm/<REALM>.pw'。", "optional": 1, "type": "string", "typetext": "<string>"},
    "port": {"description": "服务器端口。", "maximum": 65535, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 65535)"},
    "prompt": {"description": "指定授权服务器是否提示最终用户重新身份验证并表示同意。", "optional": 1, "pattern": "(?:none|login|consent|select_account|\\S+)", "type": "string"},
    "query-userinfo": {"default": 1, "description": "启用查询 userinfo 端点以获取声明值。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string", "typetext": "<string>"},
    "scopes": {"default": "email profile", "description": "指定应授权并返回的作用域（用户详细信息），例如 'email' 或 'profile'。", "optional": 1, "type": "string", "typetext": "<string>"},
    "secure": {"description": "使用安全的 LDAPS 协议。已弃用：请改用 'mode'。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "server1": {"description": "服务器 IP 地址（或 DNS 名称）", "format": "address", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "server2": {"description": "后备服务器 IP 地址（或 DNS 名称）", "format": "address", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "sslversion": {"description": "LDAPS TLS/SSL 版本。不建议使用早于 1.2 的版本！", "enum": ["tlsv1", "tlsv1_1", "tlsv1_2", "tlsv1_3"], "optional": 1, "type": "string"},
    "sync-defaults-options": {"description": "同步行为的默认选项。", "format": "realm-sync-options", "optional": 1, "type": "string", "typetext": "[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]"},
    "sync_attributes": {
      "description": "以逗号分隔的 key=value 对列表，指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 'mail' 映射到 PVE 的 'email'，请填写  'email=mail'。默认情况下，每个 PVE 用户字段均由  同名 LDAP 属性表示。", "optional": 1, "pattern": "\\w+=[^,]+(,\\s*\\w+=[^,]+)*", "type": "string"
    },
    "tfa": {"description": "使用双因素身份验证。", "format": "pve-tfa-config", "maxLength": 128, "optional": 1, "type": "string", "typetext": "type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]"},
    "type": {"description": "认证域类型。", "enum": ["ad", "ldap", "openid", "pam", "pve"], "type": "string"}, "user_attr": {"description": "LDAP 用户属性名称", "maxLength": 256, "optional": 1, "pattern": "\\S{2,}", "type": "string"},
    "user_classes": {"default": "inetorgperson, posixaccount, person, user", "description": "用户的 objectclass。", "format": "ldap-simple-attr-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "username-claim": {"description": "用于生成唯一用户名的 OpenID 声明。", "optional": 1, "type": "string", "typetext": "<string>"}, "verify": {"default": 0, "description": "验证服务器的 SSL 证书", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-access-domains-bb4462c8-post-returns" id="api-access-domains-bb4462c8-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains)。

## `/access/domains/{realm}` <a href="#api-access-domains-realm-0f82ea36" id="api-access-domains-realm-0f82ea36"></a>

原始接口路径：`/access/domains/{realm}`。

### DELETE `/access/domains/{realm}` <a href="#api-access-domains-realm-0f82ea36-delete" id="api-access-domains-realm-0f82ea36-delete"></a>

删除认证服务器。

**方法标识：** `delete`

**权限**

```text
{"check": ["perm", "/access/realm", ["Realm.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-domains-realm-0f82ea36-delete-parameters" id="api-access-domains-realm-0f82ea36-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `realm` | 类型：string；必填：是；默认值：—<br>认证域 ID |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-domains-realm-0f82ea36-delete-returns" id="api-access-domains-realm-0f82ea36-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/access/domains/{realm}` <a href="#api-access-domains-realm-0f82ea36-get" id="api-access-domains-realm-0f82ea36-get"></a>

获取身份验证服务器配置。

**方法标识：** `read`

**权限**

```text
{"check": ["perm", "/access/realm", ["Realm.Allocate", "Sys.Audit"], "any", 1]}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-domains-realm-0f82ea36-get-parameters" id="api-access-domains-realm-0f82ea36-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `realm` | 类型：string；必填：是；默认值：—<br>认证域 ID |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-domains-realm-0f82ea36-get-returns" id="api-access-domains-realm-0f82ea36-get-returns"></a>

```text
{}
```

### PUT `/access/domains/{realm}` <a href="#api-access-domains-realm-0f82ea36-put" id="api-access-domains-realm-0f82ea36-put"></a>

更新认证服务器设置。

**方法标识：** `update`

**权限**

```text
{"check": ["perm", "/access/realm", ["Realm.Allocate"]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-domains-realm-0f82ea36-put-parameters" id="api-access-domains-realm-0f82ea36-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `acr-values` | 类型：string；必填：否；默认值：—<br>指定请求授权服务器在身份验证请求中使用的身份验证上下文类引用值。 |
| `audiences` | 类型：string；必填：否；默认值：—<br>除 'client-id' 外，也接受 OpenID 颁发者可能包含的受众列表。 |
| `autocreate` | 类型：boolean；必填：否；默认值：0<br>如果用户不存在，则自动创建。 |
| `base_dn` | 类型：string；必填：否；默认值：—<br>LDAP 基础域名 |
| `bind_dn` | 类型：string；必填：否；默认值：—<br>LDAP 绑定域名 |
| `capath` | 类型：string；必填：否；默认值："/etc/ssl/certs"<br>CA 证书存储路径 |
| `case-sensitive` | 类型：boolean；必填：否；默认值：1<br>用户名区分大小写 |
| `cert` | 类型：string；必填：否；默认值：—<br>客户端证书路径 |
| `certkey` | 类型：string；必填：否；默认值：—<br>客户端证书密钥路径 |
| `check-connection` | 类型：boolean；必填：否；默认值：0<br>检查到服务器的绑定连接。 |
| `client-id` | 类型：string；必填：否；默认值：—<br>OpenID 客户端 ID |
| `client-key` | 类型：string；必填：否；默认值：—<br>OpenID 客户端密钥 |
| `comment` | 类型：string；必填：否；默认值：—<br>描述。 |
| `default` | 类型：boolean；必填：否；默认值：—<br>将此认证域用作默认认证域 |
| `delete` | 类型：string；必填：否；默认值：—<br>要删除的设置列表。 |
| `digest` | 类型：string；必填：否；默认值：—<br>如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `domain` | 类型：string；必填：否；默认值：—<br>AD 域名 |
| `filter` | 类型：string；必填：否；默认值：—<br>用户同步的 LDAP 过滤器。 |
| `group_classes` | 类型：string；必填：否；默认值："groupOfNames, group, univentionGroup, ipausergroup"<br>组的 objectclass。 |
| `group_dn` | 类型：string；必填：否；默认值：—<br>组同步的 LDAP 基础域名。如果未设置，将使用 base_dn。 |
| `group_filter` | 类型：string；必填：否；默认值：—<br>组同步的 LDAP 过滤器。 |
| `group_name_attr` | 类型：string；必填：否；默认值：—<br>表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。 |
| `groups-autocreate` | 类型：boolean；必填：否；默认值：0<br>如果组不存在，则自动创建。 |
| `groups-claim` | 类型：string；必填：否；默认值：—<br>用于获取组的 OpenID 声明。 |
| `groups-overwrite` | 类型：boolean；必填：否；默认值：0<br>用户登录时将覆盖其所有组。 |
| `issuer-url` | 类型：string；必填：否；默认值：—<br>OpenID 颁发者 URL |
| `mode` | 类型：string；必填：否；默认值："ldap"<br>LDAP 协议模式。；可选值：`ldap`, `ldaps`, `ldap+starttls` |
| `password` | 类型：string；必填：否；默认值：—<br>LDAP 绑定密码。将保存于 '/etc/pve/priv/realm/&lt;REALM&gt;.pw'。 |
| `port` | 类型：integer；必填：否；默认值：—<br>服务器端口。 |
| `prompt` | 类型：string；必填：否；默认值：—<br>指定授权服务器是否提示最终用户重新身份验证并表示同意。 |
| `query-userinfo` | 类型：boolean；必填：否；默认值：1<br>启用查询 userinfo 端点以获取声明值。 |
| `realm` | 类型：string；必填：是；默认值：—<br>认证域 ID |
| `scopes` | 类型：string；必填：否；默认值："email profile"<br>指定应授权并返回的作用域（用户详细信息），例如 'email' 或 'profile'。 |
| `secure` | 类型：boolean；必填：否；默认值：—<br>使用安全的 LDAPS 协议。已弃用：请改用 'mode'。 |
| `server1` | 类型：string；必填：否；默认值：—<br>服务器 IP 地址（或 DNS 名称） |
| `server2` | 类型：string；必填：否；默认值：—<br>后备服务器 IP 地址（或 DNS 名称） |
| `sslversion` | 类型：string；必填：否；默认值：—<br>LDAPS TLS/SSL 版本。不建议使用早于 1.2 的版本！；可选值：`tlsv1`, `tlsv1_1`, `tlsv1_2`, `tlsv1_3` |
| `sync-defaults-options` | 类型：string；必填：否；默认值：—<br>同步行为的默认选项。 |
| `sync_attributes` | 类型：string；必填：否；默认值：—<br>以逗号分隔的 key=value 对列表，指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 'mail' 映射到 PVE 的 'email'，请填写  'email=mail'。默认情况下，每个 PVE 用户字段均由  同名 LDAP 属性表示。 |
| `tfa` | 类型：string；必填：否；默认值：—<br>使用双因素身份验证。 |
| `user_attr` | 类型：string；必填：否；默认值：—<br>LDAP 用户属性名称 |
| `user_classes` | 类型：string；必填：否；默认值："inetorgperson, posixaccount, person, user"<br>用户的 objectclass。 |
| `verify` | 类型：boolean；必填：否；默认值：0<br>验证服务器的 SSL 证书 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "acr-values": {"description": "指定请求授权服务器在身份验证请求中使用的身份验证上下文类引用值。", "optional": 1, "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$", "type": "string"},
    "audiences": {"description": "除 'client-id' 外，也接受 OpenID 颁发者可能包含的受众列表。", "optional": 1, "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$", "type": "string"}, "autocreate": {"default": 0, "description": "如果用户不存在，则自动创建。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "base_dn": {"description": "LDAP 基础域名", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "bind_dn": {"description": "LDAP 绑定域名", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "capath": {"default": "/etc/ssl/certs", "description": "CA 证书存储路径", "optional": 1, "type": "string", "typetext": "<string>"}, "case-sensitive": {"default": 1, "description": "用户名区分大小写", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "cert": {"description": "客户端证书路径", "optional": 1, "type": "string", "typetext": "<string>"}, "certkey": {"description": "客户端证书密钥路径", "optional": 1, "type": "string", "typetext": "<string>"},
    "check-connection": {"default": 0, "description": "检查到服务器的绑定连接。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "client-id": {"description": "OpenID 客户端 ID", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "client-key": {"description": "OpenID 客户端密钥", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "comment": {"description": "描述。", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "default": {"description": "将此认证域用作默认认证域", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "delete": {"description": "要删除的设置列表。", "format": "pve-configid-list", "maxLength": 4096, "optional": 1, "type": "string", "typetext": "<string>"},
    "digest": {"description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。", "maxLength": 64, "optional": 1, "type": "string", "typetext": "<string>"}, "domain": {"description": "AD 域名", "maxLength": 256, "optional": 1, "pattern": "\\S+", "type": "string"},
    "filter": {"description": "用户同步的 LDAP 过滤器。", "maxLength": 2048, "optional": 1, "type": "string", "typetext": "<string>"},
    "group_classes": {"default": "groupOfNames, group, univentionGroup, ipausergroup", "description": "组的 objectclass。", "format": "ldap-simple-attr-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "group_dn": {"description": "组同步的 LDAP 基础域名。如果未设置，将使用 base_dn。", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"}, "group_filter": {"description": "组同步的 LDAP 过滤器。", "maxLength": 2048, "optional": 1, "type": "string", "typetext": "<string>"},
    "group_name_attr": {"description": "表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。", "format": "ldap-simple-attr", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "groups-autocreate": {"default": 0, "description": "如果组不存在，则自动创建。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "groups-claim": {"description": "用于获取组的 OpenID 声明。", "maxLength": 256, "optional": 1, "pattern": "(?^:[A-Za-z0-9\\.\\-_]+)", "type": "string"},
    "groups-overwrite": {"default": 0, "description": "用户登录时将覆盖其所有组。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "issuer-url": {"description": "OpenID 颁发者 URL", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "mode": {"default": "ldap", "description": "LDAP 协议模式。", "enum": ["ldap", "ldaps", "ldap+starttls"], "optional": 1, "type": "string"}, "password": {"description": "LDAP 绑定密码。将保存于 '/etc/pve/priv/realm/<REALM>.pw'。", "optional": 1, "type": "string", "typetext": "<string>"},
    "port": {"description": "服务器端口。", "maximum": 65535, "minimum": 1, "optional": 1, "type": "integer", "typetext": "<integer> (1 - 65535)"},
    "prompt": {"description": "指定授权服务器是否提示最终用户重新身份验证并表示同意。", "optional": 1, "pattern": "(?:none|login|consent|select_account|\\S+)", "type": "string"},
    "query-userinfo": {"default": 1, "description": "启用查询 userinfo 端点以获取声明值。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string", "typetext": "<string>"},
    "scopes": {"default": "email profile", "description": "指定应授权并返回的作用域（用户详细信息），例如 'email' 或 'profile'。", "optional": 1, "type": "string", "typetext": "<string>"},
    "secure": {"description": "使用安全的 LDAPS 协议。已弃用：请改用 'mode'。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "server1": {"description": "服务器 IP 地址（或 DNS 名称）", "format": "address", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "server2": {"description": "后备服务器 IP 地址（或 DNS 名称）", "format": "address", "maxLength": 256, "optional": 1, "type": "string", "typetext": "<string>"},
    "sslversion": {"description": "LDAPS TLS/SSL 版本。不建议使用早于 1.2 的版本！", "enum": ["tlsv1", "tlsv1_1", "tlsv1_2", "tlsv1_3"], "optional": 1, "type": "string"},
    "sync-defaults-options": {"description": "同步行为的默认选项。", "format": "realm-sync-options", "optional": 1, "type": "string", "typetext": "[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]"},
    "sync_attributes": {
      "description": "以逗号分隔的 key=value 对列表，指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 'mail' 映射到 PVE 的 'email'，请填写  'email=mail'。默认情况下，每个 PVE 用户字段均由  同名 LDAP 属性表示。", "optional": 1, "pattern": "\\w+=[^,]+(,\\s*\\w+=[^,]+)*", "type": "string"
    },
    "tfa": {"description": "使用双因素身份验证。", "format": "pve-tfa-config", "maxLength": 128, "optional": 1, "type": "string", "typetext": "type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]"},
    "user_attr": {"description": "LDAP 用户属性名称", "maxLength": 256, "optional": 1, "pattern": "\\S{2,}", "type": "string"},
    "user_classes": {"default": "inetorgperson, posixaccount, person, user", "description": "用户的 objectclass。", "format": "ldap-simple-attr-list", "optional": 1, "type": "string", "typetext": "<string>"},
    "verify": {"default": 0, "description": "验证服务器的 SSL 证书", "optional": 1, "type": "boolean", "typetext": "<boolean>"}
  },
  "type": "object"
}
```

</details>

#### 返回值 <a href="#api-access-domains-realm-0f82ea36-put-returns" id="api-access-domains-realm-0f82ea36-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains/{realm})。

## `/access/domains/{realm}/sync` <a href="#api-access-domains-realm-sync-388cb8d1" id="api-access-domains-realm-sync-388cb8d1"></a>

原始接口路径：`/access/domains/{realm}/sync`。

### POST `/access/domains/{realm}/sync` <a href="#api-access-domains-realm-sync-388cb8d1-post" id="api-access-domains-realm-sync-388cb8d1-post"></a>

将用户和/或组从配置的 LDAP 同步到 user.cfg。注意：同步组的名称为 'name-$realm'，因此请确保这些组尚不存在，以防覆盖。

**方法标识：** `sync`

**权限**

```text
{"check": ["and", ["perm", "/access/realm/{realm}", ["Realm.AllocateUser"]], ["perm", "/access/groups", ["User.Modify"]]], "description": "需要对 '/access/realm/<realm>' 具有 'Realm.AllocateUser' 权限，以及  对 '/access/groups/' 具有 'User.Modify' 权限。"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-domains-realm-sync-388cb8d1-post-parameters" id="api-access-domains-realm-sync-388cb8d1-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `dry-run` | 类型：boolean；必填：否；默认值：0<br>如果设置，则不写入任何内容。 |
| `enable-new` | 类型：boolean；必填：否；默认值："1"<br>立即启用新同步的用户。 |
| `full` | 类型：boolean；必填：否；默认值：—<br>已弃用：请改用 'remove-vanished'。如果设置，则将 LDAP 目录视为权威来源，删除同步未返回的用户或组，并移除同步用户的所有本地修改属性。如果未设置，则仅同步同步数据中存在的信息，不会删除或修改其他任何内容。 |
| `purge` | 类型：boolean；必填：否；默认值：—<br>已弃用：请改用 'remove-vanished'。移除同步期间从配置中移除的用户或组的 ACL。 |
| `realm` | 类型：string；必填：是；默认值：—<br>认证域 ID |
| `remove-vanished` | 类型：string；必填：否；默认值："none"<br>以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。 |
| `scope` | 类型：string；必填：否；默认值：—<br>选择要同步的内容。；可选值：`users`, `groups`, `both` |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "dry-run": {"default": 0, "description": "如果设置，则不写入任何内容。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "enable-new": {"default": "1", "description": "立即启用新同步的用户。", "optional": "1", "type": "boolean", "typetext": "<boolean>"},
    "full": {"description": "已弃用：请改用 'remove-vanished'。如果设置，则将 LDAP 目录视为权威来源，删除同步未返回的用户或组，并移除同步用户的所有本地修改属性。如果未设置，则仅同步同步数据中存在的信息，不会删除或修改其他任何内容。", "optional": "1", "type": "boolean", "typetext": "<boolean>"},
    "purge": {"description": "已弃用：请改用 'remove-vanished'。移除同步期间从配置中移除的用户或组的 ACL。", "optional": "1", "type": "boolean", "typetext": "<boolean>"}, "realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string", "typetext": "<string>"},
    "remove-vanished": {
      "default": "none",
      "description": "以分号分隔的移除项目列表，指定当项目本身或用户在同步期间消失时移除哪些内容。可用值如下：'entry' 在同步未返回用户/组时移除该用户/组。'properties' 移除现有用户/组中已设置但源中不存在的属性（包括自定义属性）。'acl' 在同步未返回用户/组时移除 acl。也可以使用 'none'（默认值）代替列表。",
      "optional": "1", "pattern": "(?:(?:(?:acl|properties|entry);)*(?:acl|properties|entry))|none", "type": "string", "typetext": "([acl];[properties];[entry])|none"
    },
    "scope": {"description": "选择要同步的内容。", "enum": ["users", "groups", "both"], "optional": "1", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-domains-realm-sync-388cb8d1-post-returns" id="api-access-domains-realm-sync-388cb8d1-post-returns"></a>

```text
{"description": "工作任务 UPID", "type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains/{realm}/sync)。

## `/access/openid` <a href="#api-access-openid-12c1d0b0" id="api-access-openid-12c1d0b0"></a>

原始接口路径：`/access/openid`。

### GET `/access/openid` <a href="#api-access-openid-12c1d0b0-get" id="api-access-openid-12c1d0b0-get"></a>

目录索引。

**方法标识：** `index`

**权限**

```text
{"user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-openid-12c1d0b0-get-parameters" id="api-access-openid-12c1d0b0-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-openid-12c1d0b0-get-returns" id="api-access-openid-12c1d0b0-get-returns"></a>

```text
{"items": {"properties": {"subdir": {"type": "string"}}, "type": "object"}, "links": [{"href": "{subdir}", "rel": "child"}], "type": "array"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/openid)。

## `/access/openid/auth-url` <a href="#api-access-openid-auth-url-ec28351f" id="api-access-openid-auth-url-ec28351f"></a>

原始接口路径：`/access/openid/auth-url`。

### POST `/access/openid/auth-url` <a href="#api-access-openid-auth-url-ec28351f-post" id="api-access-openid-auth-url-ec28351f-post"></a>

获取指定认证域的 OpenID 授权 URL。

**方法标识：** `auth_url`

**权限**

```text
{"user": "world"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-openid-auth-url-ec28351f-post-parameters" id="api-access-openid-auth-url-ec28351f-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `realm` | 类型：string；必填：是；默认值：—<br>认证域 ID |
| `redirect-url` | 类型：string；必填：是；默认值：—<br>重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {"realm": {"description": "认证域 ID", "format": "pve-realm", "maxLength": 32, "type": "string", "typetext": "<string>"}, "redirect-url": {"description": "重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。", "maxLength": 255, "type": "string", "typetext": "<string>"}}
}
```

</details>

#### 返回值 <a href="#api-access-openid-auth-url-ec28351f-post-returns" id="api-access-openid-auth-url-ec28351f-post-returns"></a>

```text
{"description": "重定向 URL。", "type": "string"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/openid/auth-url)。

## `/access/openid/login` <a href="#api-access-openid-login-b04e60dc" id="api-access-openid-login-b04e60dc"></a>

原始接口路径：`/access/openid/login`。

### POST `/access/openid/login` <a href="#api-access-openid-login-b04e60dc-post" id="api-access-openid-login-b04e60dc-post"></a>

验证 OpenID 授权码并创建票据。

**方法标识：** `login`

**权限**

```text
{"user": "world"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-openid-login-b04e60dc-post-parameters" id="api-access-openid-login-b04e60dc-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `code` | 类型：string；必填：是；默认值：—<br>OpenID 授权码。 |
| `redirect-url` | 类型：string；必填：是；默认值：—<br>重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。 |
| `state` | 类型：string；必填：是；默认值：—<br>OpenID 状态。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "code": {"description": "OpenID 授权码。", "maxLength": 4096, "type": "string", "typetext": "<string>"}, "redirect-url": {"description": "重定向 URL。客户端应将其设为所用服务器的 URL（location.origin）。", "maxLength": 255, "type": "string", "typetext": "<string>"},
    "state": {"description": "OpenID 状态。", "maxLength": 1024, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-openid-login-b04e60dc-post-returns" id="api-access-openid-login-b04e60dc-post-returns"></a>

```text
{"properties": {"CSRFPreventionToken": {"type": "string"}, "cap": {"type": "object"}, "clustername": {"optional": 1, "type": "string"}, "ticket": {"type": "string"}, "username": {"type": "string"}}}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/openid/login)。

## `/access/tfa` <a href="#api-access-tfa-e9e0bb9f" id="api-access-tfa-e9e0bb9f"></a>

原始接口路径：`/access/tfa`。

### GET `/access/tfa` <a href="#api-access-tfa-e9e0bb9f-get" id="api-access-tfa-e9e0bb9f-get"></a>

列出用户的 TFA 配置。

**方法标识：** `list_tfa`

**权限**

```text
{"description": "根据权限返回所有用户或仅已登录用户。", "user": "all"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-tfa-e9e0bb9f-get-parameters" id="api-access-tfa-e9e0bb9f-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-tfa-e9e0bb9f-get-returns" id="api-access-tfa-e9e0bb9f-get-returns"></a>

```text
{
  "description": "用户与 TFA 条目的元组列表。",
  "items": {
    "properties": {
      "entries": {
        "items": {
          "description": "TFA 条目。",
          "properties": {
            "created": {"description": "此条目的创建时间，以 UNIX 纪元时间表示。", "type": "integer"}, "description": {"description": "用户为此条目选择的描述。", "type": "string"}, "enable": {"default": 1, "description": "此 TFA 条目当前是否已启用。", "optional": 1, "type": "boolean"},
            "id": {"description": "用于引用此条目的 ID。", "type": "string"}, "type": {"description": "TFA 条目类型。", "enum": ["totp", "u2f", "webauthn", "recovery", "yubico"], "type": "string"}
          },
          "type": "object"
        },
        "type": "array"
      },
      "tfa-locked-until": {"description": "包含用户第二因素锁定截止时间的时间戳。", "optional": 1, "type": "integer"}, "totp-locked": {"description": "如果用户当前被锁定而无法使用 TOTP 因素，则为 true。", "optional": 1, "type": "boolean"}, "userid": {"description": "此条目所属的用户。", "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{userid}", "rel": "child"}], "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa)。

## `/access/tfa/{userid}` <a href="#api-access-tfa-userid-4f95baa5" id="api-access-tfa-userid-4f95baa5"></a>

原始接口路径：`/access/tfa/{userid}`。

### GET `/access/tfa/{userid}` <a href="#api-access-tfa-userid-4f95baa5-get" id="api-access-tfa-userid-4f95baa5-get"></a>

列出用户的 TFA 配置。

**方法标识：** `list_user_tfa`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify", "Sys.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-tfa-userid-4f95baa5-get-parameters" id="api-access-tfa-userid-4f95baa5-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-tfa-userid-4f95baa5-get-returns" id="api-access-tfa-userid-4f95baa5-get-returns"></a>

```text
{
  "description": "用户的 TFA 条目列表。",
  "items": {
    "description": "TFA 条目。",
    "properties": {
      "created": {"description": "此条目的创建时间，以 UNIX 纪元时间表示。", "type": "integer"}, "description": {"description": "用户为此条目选择的描述。", "type": "string"}, "enable": {"default": 1, "description": "此 TFA 条目当前是否已启用。", "optional": 1, "type": "boolean"},
      "id": {"description": "用于引用此条目的 ID。", "type": "string"}, "type": {"description": "TFA 条目类型。", "enum": ["totp", "u2f", "webauthn", "recovery", "yubico"], "type": "string"}
    },
    "type": "object"
  },
  "links": [{"href": "{id}", "rel": "child"}], "type": "array"
}
```

### POST `/access/tfa/{userid}` <a href="#api-access-tfa-userid-4f95baa5-post" id="api-access-tfa-userid-4f95baa5-post"></a>

为用户添加 TFA 条目。

**方法标识：** `add_tfa_entry`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `0`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-tfa-userid-4f95baa5-post-parameters" id="api-access-tfa-userid-4f95baa5-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `challenge` | 类型：string；必填：否；默认值：—<br>响应 U2F 质询时：原始质询字符串 |
| `description` | 类型：string；必填：否；默认值：—<br>用于区分多个条目的描述 |
| `password` | 类型：string；必填：否；默认值：—<br>执行更改的用户的当前密码。 |
| `totp` | 类型：string；必填：否；默认值：—<br>TOTP URI。 |
| `type` | 类型：string；必填：是；默认值：—<br>TFA 条目类型。；可选值：`totp`, `u2f`, `webauthn`, `recovery`, `yubico` |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |
| `value` | 类型：string；必填：否；默认值：—<br>提供的 TOTP URI 的当前值，或 Webauthn/U2F 质询响应 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "challenge": {"description": "响应 U2F 质询时：原始质询字符串", "optional": 1, "type": "string", "typetext": "<string>"}, "description": {"description": "用于区分多个条目的描述", "maxLength": 255, "optional": 1, "type": "string", "typetext": "<string>"},
    "password": {"description": "执行更改的用户的当前密码。", "maxLength": 64, "minLength": 5, "optional": 1, "type": "string", "typetext": "<string>"}, "totp": {"description": "TOTP URI。", "optional": 1, "type": "string", "typetext": "<string>"},
    "type": {"description": "TFA 条目类型。", "enum": ["totp", "u2f", "webauthn", "recovery", "yubico"], "type": "string"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"},
    "value": {"description": "提供的 TOTP URI 的当前值，或 Webauthn/U2F 质询响应", "optional": 1, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-tfa-userid-4f95baa5-post-returns" id="api-access-tfa-userid-4f95baa5-post-returns"></a>

```text
{
  "properties": {
    "challenge": {"description": "添加 U2F 条目时，此项包含用户必须响应以完成注册的质询。", "optional": 1, "type": "string"}, "id": {"description": "新添加的 TFA 条目的 ID。", "type": "string"},
    "recovery": {"description": "添加恢复码时，此项包含要向用户显示的恢复码列表", "items": {"description": "恢复条目。", "type": "string"}, "optional": 1, "type": "array"}
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa/{userid})。

## `/access/tfa/{userid}/{id}` <a href="#api-access-tfa-userid-id-2f4086eb" id="api-access-tfa-userid-id-2f4086eb"></a>

原始接口路径：`/access/tfa/{userid}/{id}`。

### DELETE `/access/tfa/{userid}/{id}` <a href="#api-access-tfa-userid-id-2f4086eb-delete" id="api-access-tfa-userid-id-2f4086eb-delete"></a>

按 ID 删除 TFA 条目。

**方法标识：** `delete_tfa`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `0`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-tfa-userid-id-2f4086eb-delete-parameters" id="api-access-tfa-userid-id-2f4086eb-delete-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>TFA 条目 ID。 |
| `password` | 类型：string；必填：否；默认值：—<br>执行更改的用户的当前密码。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "id": {"description": "TFA 条目 ID。", "type": "string", "typetext": "<string>"}, "password": {"description": "执行更改的用户的当前密码。", "maxLength": 64, "minLength": 5, "optional": 1, "type": "string", "typetext": "<string>"},
    "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-tfa-userid-id-2f4086eb-delete-returns" id="api-access-tfa-userid-id-2f4086eb-delete-returns"></a>

```text
{"type": "null"}
```

### GET `/access/tfa/{userid}/{id}` <a href="#api-access-tfa-userid-id-2f4086eb-get" id="api-access-tfa-userid-id-2f4086eb-get"></a>

获取请求的 TFA 条目（如存在）。

**方法标识：** `get_tfa_entry`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify", "Sys.Audit"]]]}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-tfa-userid-id-2f4086eb-get-parameters" id="api-access-tfa-userid-id-2f4086eb-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `id` | 类型：string；必填：是；默认值：—<br>TFA 条目 ID。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{"additionalProperties": 0, "properties": {"id": {"description": "TFA 条目 ID。", "type": "string", "typetext": "<string>"}, "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}}}
```

</details>

#### 返回值 <a href="#api-access-tfa-userid-id-2f4086eb-get-returns" id="api-access-tfa-userid-id-2f4086eb-get-returns"></a>

```text
{
  "description": "TFA 条目。",
  "properties": {
    "created": {"description": "此条目的创建时间，以 UNIX 纪元时间表示。", "type": "integer"}, "description": {"description": "用户为此条目选择的描述。", "type": "string"}, "enable": {"default": 1, "description": "此 TFA 条目当前是否已启用。", "optional": 1, "type": "boolean"},
    "id": {"description": "用于引用此条目的 ID。", "type": "string"}, "type": {"description": "TFA 条目类型。", "enum": ["totp", "u2f", "webauthn", "recovery", "yubico"], "type": "string"}
  },
  "type": "object"
}
```

### PUT `/access/tfa/{userid}/{id}` <a href="#api-access-tfa-userid-id-2f4086eb-put" id="api-access-tfa-userid-id-2f4086eb-put"></a>

为用户添加 TFA 条目。

**方法标识：** `update_tfa_entry`

**权限**

```text
{"check": ["or", ["userid-param", "self"], ["userid-group", ["User.Modify"]]]}
```

**允许 API 令牌：** `0`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-tfa-userid-id-2f4086eb-put-parameters" id="api-access-tfa-userid-id-2f4086eb-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `description` | 类型：string；必填：否；默认值：—<br>用于区分多个条目的描述 |
| `enable` | 类型：boolean；必填：否；默认值：—<br>是否应启用此条目用于登录。 |
| `id` | 类型：string；必填：是；默认值：—<br>TFA 条目 ID。 |
| `password` | 类型：string；必填：否；默认值：—<br>执行更改的用户的当前密码。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "description": {"description": "用于区分多个条目的描述", "maxLength": 255, "optional": 1, "type": "string", "typetext": "<string>"}, "enable": {"description": "是否应启用此条目用于登录。", "optional": 1, "type": "boolean", "typetext": "<boolean>"},
    "id": {"description": "TFA 条目 ID。", "type": "string", "typetext": "<string>"}, "password": {"description": "执行更改的用户的当前密码。", "maxLength": 64, "minLength": 5, "optional": 1, "type": "string", "typetext": "<string>"},
    "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-tfa-userid-id-2f4086eb-put-returns" id="api-access-tfa-userid-id-2f4086eb-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa/{userid}/{id})。

## `/access/ticket` <a href="#api-access-ticket-bbd93e48" id="api-access-ticket-bbd93e48"></a>

原始接口路径：`/access/ticket`。

### GET `/access/ticket` <a href="#api-access-ticket-bbd93e48-get" id="api-access-ticket-bbd93e48-get"></a>

占位项。适用于希望提供登录页面的格式化程序。

**方法标识：** `get_ticket`

**权限**

```text
{"user": "world"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-ticket-bbd93e48-get-parameters" id="api-access-ticket-bbd93e48-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-access-ticket-bbd93e48-get-returns" id="api-access-ticket-bbd93e48-get-returns"></a>

```text
{"type": "null"}
```

### POST `/access/ticket` <a href="#api-access-ticket-bbd93e48-post" id="api-access-ticket-bbd93e48-post"></a>

创建或验证认证票据。

**方法标识：** `create_ticket`

**权限**

```text
{"description": "需要传入有效凭据。", "user": "world"}
```

**允许 API 令牌：** `0`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-ticket-bbd93e48-post-parameters" id="api-access-ticket-bbd93e48-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `new-format` | 类型：boolean；必填：否；默认值：1<br>此参数现在被忽略，并假定为 1。 |
| `otp` | 类型：string；必填：否；默认值：—<br>双因素身份验证的一次性密码。 |
| `password` | 类型：string；必填：是；默认值：—<br>秘密密码。也可以是有效票据。 |
| `path` | 类型：string；必填：否；默认值：—<br>验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `privs` | 类型：string；必填：否；默认值：—<br>验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `realm` | 类型：string；必填：否；默认值：—<br>可以选择使用此参数传入认证域。通常只需将认证域添加到用户名后，形式为 &lt;username&gt;@&lt;realm&gt;。 |
| `tfa-challenge` | 类型：string；必填：否；默认值：—<br>用户要响应的已签名 TFA 质询字符串。 |
| `username` | 类型：string；必填：是；默认值：—<br>用户名 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "new-format": {"default": 1, "description": "此参数现在被忽略，并假定为 1。", "optional": 1, "type": "boolean", "typetext": "<boolean>"}, "otp": {"description": "双因素身份验证的一次性密码。", "optional": 1, "type": "string", "typetext": "<string>"},
    "password": {"description": "秘密密码。也可以是有效票据。", "type": "string", "typetext": "<string>"}, "path": {"description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限", "maxLength": 64, "optional": 1, "requires": "privs", "type": "string", "typetext": "<string>"},
    "privs": {"description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限", "format": "pve-priv-list", "maxLength": 64, "optional": 1, "requires": "path", "type": "string", "typetext": "<string>"},
    "realm": {"description": "可以选择使用此参数传入认证域。通常只需将认证域添加到用户名后，形式为 <username>@<realm>。", "format": "pve-realm", "maxLength": 32, "optional": 1, "type": "string", "typetext": "<string>"},
    "tfa-challenge": {"description": "用户要响应的已签名 TFA 质询字符串。", "optional": 1, "type": "string", "typetext": "<string>"}, "username": {"description": "用户名", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-ticket-bbd93e48-post-returns" id="api-access-ticket-bbd93e48-post-returns"></a>

```text
{"properties": {"CSRFPreventionToken": {"optional": 1, "type": "string"}, "clustername": {"optional": 1, "type": "string"}, "ticket": {"optional": 1, "type": "string"}, "username": {"type": "string"}}, "type": "object"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/ticket)。

## `/access/vncticket` <a href="#api-access-vncticket-d992db8d" id="api-access-vncticket-d992db8d"></a>

原始接口路径：`/access/vncticket`。

### POST `/access/vncticket` <a href="#api-access-vncticket-d992db8d-post" id="api-access-vncticket-d992db8d-post"></a>

验证 VNC 身份验证票据。

**方法标识：** `verify_vnc_ticket`

**权限**

```text
{"description": "需要传入有效凭据。", "user": "world"}
```

**允许 API 令牌：** `1`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-vncticket-d992db8d-post-parameters" id="api-access-vncticket-d992db8d-post-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `authid` | 类型：string；必填：是；默认值：—<br>UserId 或令牌 |
| `path` | 类型：string；必填：是；默认值：—<br>验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `port` | 类型：integer；必填：否；默认值：—<br>验证票据对此端口是否有效。 |
| `privs` | 类型：string；必填：是；默认值：—<br>验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `vncticket` | 类型：string；必填：是；默认值：—<br>VNC 票据。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "authid": {"description": "UserId 或令牌", "maxLength": 64, "type": "string", "typetext": "<string>"}, "path": {"description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限", "maxLength": 64, "type": "string", "typetext": "<string>"},
    "port": {"description": "验证票据对此端口是否有效。", "optional": 1, "type": "integer", "typetext": "<integer>"}, "privs": {"description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限", "format": "pve-priv-list", "maxLength": 64, "type": "string", "typetext": "<string>"},
    "vncticket": {"description": "VNC 票据。", "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-vncticket-d992db8d-post-returns" id="api-access-vncticket-d992db8d-post-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/vncticket)。

## `/access/password` <a href="#api-access-password-d9022417" id="api-access-password-d9022417"></a>

原始接口路径：`/access/password`。

### PUT `/access/password` <a href="#api-access-password-d9022417-put" id="api-access-password-d9022417-put"></a>

更改用户密码。

**方法标识：** `change_password`

**权限**

```text
{
  "check": ["or", ["userid-param", "self"], ["and", ["userid-param", "Realm.AllocateUser"], ["userid-group", ["User.Modify"]]]],
  "description": "每个用户都可以更改自己的密码。如果用户具有 'Realm.AllocateUser' 权限（作用于用户 <userid> 所属认证域），且对用户 <userid> 所属的某组的 /access/groups/<group> 具有 'User.Modify' 权限，则可以更改该用户的密码。对于 PAM 认证域，密码更改不会在  整个集群生效，仅适用于本地节点。"
}
```

**允许 API 令牌：** `0`

**受保护接口：** `1`

#### 请求参数 <a href="#api-access-password-d9022417-put-parameters" id="api-access-password-d9022417-put-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `confirmation-password` | 类型：string；必填：否；默认值：—<br>执行更改的用户的当前密码。 |
| `password` | 类型：string；必填：是；默认值：—<br>新密码。 |
| `userid` | 类型：string；必填：是；默认值：—<br>完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "confirmation-password": {"description": "执行更改的用户的当前密码。", "maxLength": 64, "minLength": 5, "optional": 1, "type": "string", "typetext": "<string>"}, "password": {"description": "新密码。", "maxLength": 64, "minLength": 8, "type": "string", "typetext": "<string>"},
    "userid": {"description": "完整用户 ID，采用 `name@realm` 格式。", "format": "pve-userid", "maxLength": 64, "type": "string", "typetext": "<string>"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-password-d9022417-put-returns" id="api-access-password-d9022417-put-returns"></a>

```text
{"type": "null"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/password)。

## `/access/permissions` <a href="#api-access-permissions-f180524f" id="api-access-permissions-f180524f"></a>

原始接口路径：`/access/permissions`。

### GET `/access/permissions` <a href="#api-access-permissions-f180524f-get" id="api-access-permissions-f180524f-get"></a>

获取给定用户/令牌的有效权限。

**方法标识：** `permissions`

**权限**

```text
{"description": "每个用户/令牌都可以导出自己的权限（或所拥有令牌的权限）。如果用户对 /access. 具有 'Sys.Audit' 权限，则可以导出其他用户或其令牌的权限", "user": "all"}
```

**允许 API 令牌：** `1`

#### 请求参数 <a href="#api-access-permissions-f180524f-get-parameters" id="api-access-permissions-f180524f-get-parameters"></a>

| 参数 | 定义与说明 |
| --- | --- |
| `path` | 类型：string；必填：否；默认值：—<br>仅导出此特定路径，而非整棵树。 |
| `userid` | 类型：string；必填：否；默认值：—<br>用户 ID 或完整 API 令牌 ID |

<details>
<summary>完整请求参数结构</summary>

```text
{
  "additionalProperties": 0,
  "properties": {
    "path": {"description": "仅导出此特定路径，而非整棵树。", "optional": 1, "type": "string", "typetext": "<string>"}, "userid": {"description": "用户 ID 或完整 API 令牌 ID", "optional": 1, "pattern": "(?^:^(?^:[^\\s:/]+)\\@(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+)(?:!(?^:[A-Za-z][A-Za-z0-9\\.\\-_]+))?$)", "type": "string"}
  }
}
```

</details>

#### 返回值 <a href="#api-access-permissions-f180524f-get-returns" id="api-access-permissions-f180524f-get-returns"></a>

```text
{"description": "\"path\" =>（\"privilege\" => \"propagate boolean\" 的映射）的映射。", "type": "object"}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/permissions)。
