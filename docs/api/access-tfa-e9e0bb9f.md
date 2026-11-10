# `/access/tfa`

原始接口路径：`/access/tfa`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/tfa`

List TFA configurations of users.

**方法标识：** `list_tfa`

**权限**

```json
{
  "description": "Returns all or just the logged-in user, depending on privileges.",
  "user": "all"
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
  "description": "The list tuples of user and TFA entries.",
  "items": {
    "properties": {
      "entries": {
        "items": {
          "description": "TFA Entry.",
          "properties": {
            "created": {
              "description": "Creation time of this entry as unix epoch.",
              "type": "integer"
            },
            "description": {
              "description": "User chosen description for this entry.",
              "type": "string"
            },
            "enable": {
              "default": 1,
              "description": "Whether this TFA entry is currently enabled.",
              "optional": 1,
              "type": "boolean"
            },
            "id": {
              "description": "The id used to reference this entry.",
              "type": "string"
            },
            "type": {
              "description": "TFA Entry Type.",
              "enum": [
                "totp",
                "u2f",
                "webauthn",
                "recovery",
                "yubico"
              ],
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "tfa-locked-until": {
        "description": "Contains a timestamp until when a user is locked out of 2nd factors.",
        "optional": 1,
        "type": "integer"
      },
      "totp-locked": {
        "description": "True if the user is currently locked out of TOTP factors.",
        "optional": 1,
        "type": "boolean"
      },
      "userid": {
        "description": "User this entry belongs to.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{userid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/tfa)。
