# `/nodes/{node}/capabilities/qemu/cpu-flags`

原始接口路径：`/nodes/{node}/capabilities/qemu/cpu-flags`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/capabilities/qemu/cpu-flags`

List of available VM-specific CPU flags. Returns an empty list for 'aarch64' as no VM-specific flags are defined for it yet.

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `accel` | string | 否 | "kvm" | Acceleration type to check node compatibility for.；可选值：`kvm`, `tcg` |
| `arch` | string | 否 | — | Virtual processor architecture. Defaults to the host architecture.；可选值：`x86_64`, `aarch64` |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "accel": {
      "default": "kvm",
      "description": "Acceleration type to check node compatibility for.",
      "enum": [
        "kvm",
        "tcg"
      ],
      "optional": 1,
      "type": "string"
    },
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
    "properties": {
      "description": {
        "description": "Description of the CPU flag.",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "Name of the CPU flag.",
        "type": "string"
      },
      "supported-on": {
        "description": "List of nodes supporting the CPU flag with the selected acceleration type (\"accel\").",
        "items": {
          "description": "The cluster node name.",
          "format": "pve-node",
          "type": "string"
        },
        "optional": 1,
        "type": "array"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/capabilities/qemu/cpu-flags)。
