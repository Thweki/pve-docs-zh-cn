# `/nodes/{node}/qemu/{vmid}/agent/file-write`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/file-write`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/agent/file-write`

Writes the given file via guest agent.

**方法标识：** `file-write`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.GuestAgent.FileWrite",
      "VM.GuestAgent.Unrestricted"
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
| `content` | string | 是 | — | The content to write into the file. |
| `encode` | boolean | 否 | 1 | If set, the content will be encoded as base64 (required by QEMU).Otherwise the content needs to be encoded beforehand - defaults to true. |
| `file` | string | 是 | — | The path to the file. |
| `node` | string | 是 | — | The cluster node name. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "content": {
      "description": "The content to write into the file.",
      "maxLength": 61440,
      "type": "string",
      "typetext": "<string>"
    },
    "encode": {
      "default": 1,
      "description": "If set, the content will be encoded as base64 (required by QEMU).Otherwise the content needs to be encoded beforehand - defaults to true.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "file": {
      "description": "The path to the file.",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/file-write)。
