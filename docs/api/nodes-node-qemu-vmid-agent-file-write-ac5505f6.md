# `/nodes/{node}/qemu/{vmid}/agent/file-write`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent/file-write`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/qemu/{vmid}/agent/file-write`

通过客户机代理写入给定文件。

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
| `content` | string | 是 | — | 要写入文件的内容。 |
| `encode` | boolean | 否 | 1 | 如果设置，内容将编码为 base64（QEMU 要求）。否则内容需要预先编码——默认为 true。 |
| `file` | string | 是 | — | 文件路径。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "content": {
      "description": "要写入文件的内容。",
      "maxLength": 61440,
      "type": "string",
      "typetext": "<string>"
    },
    "encode": {
      "default": 1,
      "description": "如果设置，内容将编码为 base64（QEMU 要求）。否则内容需要预先编码——默认为 true。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "file": {
      "description": "文件路径。",
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent/file-write)。
