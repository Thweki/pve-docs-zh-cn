# `/nodes/{node}/qemu/{vmid}/agent/file-read`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/file-read`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/agent/file-read`

Reads the given file via guest agent. Is limited to 16777216 bytes.

**方法标识：** `file-read`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.GuestAgent.FileRead",
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
| `count` | integer | 否 | "16777216" | Number of bytes to read. |
| `decode` | boolean | 否 | 1 | Data received from the QEMU Guest-Agent is base64 encoded. If this is set to true, the data is decoded. Otherwise the content is forwarded with base64 encoding. Defaults to true. |
| `file` | string | 是 | — | The path to the file |
| `node` | string | 是 | — | The cluster node name. |
| `offset` | integer | 否 | 0 | Offset to start reading at |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "count": {
      "default": "16777216",
      "description": "Number of bytes to read.",
      "maximum": "16777216",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 16777216)"
    },
    "decode": {
      "default": 1,
      "description": "Data received from the QEMU Guest-Agent is base64 encoded. If this is set to true, the data is decoded. Otherwise the content is forwarded with base64 encoding. Defaults to true.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "file": {
      "description": "The path to the file",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "offset": {
      "default": 0,
      "description": "Offset to start reading at",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
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
  "description": "Returns an object with a `content` property.",
  "properties": {
    "content": {
      "description": "The content of the file, maximum 16777216",
      "type": "string"
    },
    "truncated": {
      "description": "If set to 1, the read did not reach the end of the file.",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/file-read)。
