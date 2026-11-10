# `/access/tfa`

原始接口路径：`/access/tfa`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/tfa`

列出用户的 TFA 配置。

**方法标识：** `list_tfa`

**权限**

```json
{
  "description": "根据权限返回所有用户或仅已登录用户。",
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
  "description": "用户与 TFA 条目的元组列表。",
  "items": {
    "properties": {
      "entries": {
        "items": {
          "description": "TFA 条目。",
          "properties": {
            "created": {
              "description": "此条目的创建时间，以 UNIX 纪元时间表示。",
              "type": "integer"
            },
            "description": {
              "description": "用户为此条目选择的描述。",
              "type": "string"
            },
            "enable": {
              "default": 1,
              "description": "此 TFA 条目当前是否已启用。",
              "optional": 1,
              "type": "boolean"
            },
            "id": {
              "description": "用于引用此条目的 ID。",
              "type": "string"
            },
            "type": {
              "description": "TFA 条目类型。",
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
        "description": "包含用户第二因素锁定截止时间的时间戳。",
        "optional": 1,
        "type": "integer"
      },
      "totp-locked": {
        "description": "如果用户当前被锁定而无法使用 TOTP 因素，则为 true。",
        "optional": 1,
        "type": "boolean"
      },
      "userid": {
        "description": "此条目所属的用户。",
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
