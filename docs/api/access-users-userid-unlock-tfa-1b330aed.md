# `/access/users/{userid}/unlock-tfa`

原始接口路径：`/access/users/{userid}/unlock-tfa`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/access/users/{userid}/unlock-tfa`

解除用户 TFA 身份验证锁定。

**方法标识：** `unlock_tfa`

**权限**

```json
{
  "check": [
    "userid-group",
    [
      "User.Modify"
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
| `userid` | string | 是 | — | 完整用户 ID，采用 `name@realm` 格式。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
  "type": "boolean"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/users/{userid}/unlock-tfa)。
