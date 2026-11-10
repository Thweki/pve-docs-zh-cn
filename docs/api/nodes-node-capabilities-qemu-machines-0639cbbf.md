# `/nodes/{node}/capabilities/qemu/machines`

原始接口路径：`/nodes/{node}/capabilities/qemu/machines`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/capabilities/qemu/machines`

Get available QEMU/KVM machine types.

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

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
| `arch` | string | 否 | — | Virtual processor architecture. Defaults to the host architecture.；可选值：`x86_64`, `aarch64` |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "arch": {
      "description": "Virtual processor architecture. Defaults to the host architecture.",
      "enum": [
        "x86_64",
        "aarch64"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
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
  "items": {
    "additionalProperties": 1,
    "properties": {
      "changes": {
        "description": "Notable changes of a version, currently only set for +pveX versions.",
        "optional": 1,
        "type": "string"
      },
      "id": {
        "description": "Full name of machine type and version.",
        "type": "string"
      },
      "type": {
        "description": "The machine type.",
        "enum": [
          "q35",
          "i440fx"
        ],
        "type": "string"
      },
      "version": {
        "description": "The machine version.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/capabilities/qemu/machines)。
