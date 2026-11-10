# `/access/vncticket`

原始接口路径：`/access/vncticket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/vncticket`

验证 VNC 身份验证票据。

**方法标识：** `verify_vnc_ticket`

**权限**

```json
{
  "description": "需要传入有效凭据。",
  "user": "world"
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
| `authid` | string | 是 | — | UserId 或令牌 |
| `path` | string | 是 | — | 验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `port` | integer | 否 | — | 验证票据对此端口是否有效。 |
| `privs` | string | 是 | — | 验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限 |
| `vncticket` | string | 是 | — | VNC 票据。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "authid": {
      "description": "UserId 或令牌",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "验证票据对此端口是否有效。",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "privs": {
      "description": "验证票据，并检查用户在 'path' 上是否具有 'privs' 访问权限",
      "format": "pve-priv-list",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "vncticket": {
      "description": "VNC 票据。",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/vncticket)。
