# `/access/vncticket`

原始接口路径：`/access/vncticket`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/access/vncticket`

verify VNC authentication ticket.

**方法标识：** `verify_vnc_ticket`

**权限**

```json
{
  "description": "You need to pass valid credientials.",
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
| `authid` | string | 是 | — | UserId or token |
| `path` | string | 是 | — | Verify ticket, and check if user have access 'privs' on 'path' |
| `port` | integer | 否 | — | Verify that the ticket is valid for this port. |
| `privs` | string | 是 | — | Verify ticket, and check if user have access 'privs' on 'path' |
| `vncticket` | string | 是 | — | The VNC ticket. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "authid": {
      "description": "UserId or token",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "Verify ticket, and check if user have access 'privs' on 'path'",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "Verify that the ticket is valid for this port.",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer>"
    },
    "privs": {
      "description": "Verify ticket, and check if user have access 'privs' on 'path'",
      "format": "pve-priv-list",
      "maxLength": 64,
      "type": "string",
      "typetext": "<string>"
    },
    "vncticket": {
      "description": "The VNC ticket.",
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
