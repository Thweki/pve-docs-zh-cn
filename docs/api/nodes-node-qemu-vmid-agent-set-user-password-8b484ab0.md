# `/nodes/{node}/qemu/{vmid}/agent/set-user-password`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/set-user-password`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/agent/set-user-password`

将给定用户的密码设置为给定密码

**方法标识：** `set-user-password`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.GuestAgent.Unrestricted"
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `crypted` | boolean | 否 | 0 | 如果密码已经过 crypt() 处理，则设为 1 |
| `node` | string | 是 | — | 集群节点名称。 |
| `password` | string | 是 | — | 新密码。 |
| `username` | string | 是 | — | 要设置密码的用户。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "crypted": {
      "default": 0,
      "description": "如果密码已经过 crypt() 处理，则设为 1",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "password": {
      "description": "新密码。",
      "maxLength": 1024,
      "minLength": 5,
      "type": "string",
      "typetext": "<string>"
    },
    "username": {
      "description": "要设置密码的用户。",
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "返回仅含一个 `result` 属性的对象。",
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/set-user-password)。
