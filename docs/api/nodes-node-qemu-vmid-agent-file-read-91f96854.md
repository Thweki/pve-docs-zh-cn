# `/nodes/{node}/qemu/{vmid}/agent/file-read`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/file-read`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/agent/file-read`

通过客户机代理读取给定文件。限制为 16777216 字节。

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
| `count` | integer | 否 | "16777216" | 要读取的字节数。 |
| `decode` | boolean | 否 | 1 | 从 QEMU Guest-Agent 接收的数据采用 base64 编码。如果设为 true，则解码数据。否则以 base64 编码转发内容。默认为 true。 |
| `file` | string | 是 | — | 文件路径 |
| `node` | string | 是 | — | 集群节点名称。 |
| `offset` | integer | 否 | 0 | 开始读取的偏移量 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "count": {
      "default": "16777216",
      "description": "要读取的字节数。",
      "maximum": "16777216",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 16777216)"
    },
    "decode": {
      "default": 1,
      "description": "从 QEMU Guest-Agent 接收的数据采用 base64 编码。如果设为 true，则解码数据。否则以 base64 编码转发内容。默认为 true。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "file": {
      "description": "文件路径",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "offset": {
      "default": 0,
      "description": "开始读取的偏移量",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
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
  "description": "返回带有 `content` 属性的对象。",
  "properties": {
    "content": {
      "description": "文件内容，最大 16777216",
      "type": "string"
    },
    "truncated": {
      "description": "如果设为 1，表示读取未到达文件末尾。",
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/file-read)。
