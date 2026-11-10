# `/cluster/qemu/cpu-flags`

原始接口路径：`/cluster/qemu/cpu-flags`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/qemu/cpu-flags`

List of available CPU flags. Currently only implemented for x86_64, returns an empty list for aarch64.

**方法标识：** `index`

**权限**

```json
{
  "check": [
    "or",
    [
      "perm",
      "/nodes",
      [
        "Sys.Audit"
      ]
    ],
    [
      "perm",
      "/mapping/cpu",
      [
        "Mapping.Audit",
        "Mapping.Use",
        "Mapping.Modify"
      ],
      "any",
      1
    ]
  ]
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
        "description": "List of nodes supporting the flag with the selected acceleration type (\"accel\").",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/qemu/cpu-flags)。
