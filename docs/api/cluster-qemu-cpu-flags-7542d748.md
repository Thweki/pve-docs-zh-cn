# `/cluster/qemu/cpu-flags`

原始接口路径：`/cluster/qemu/cpu-flags`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/qemu/cpu-flags`

可用 CPU 标志列表。目前仅针对 x86_64 实现，对于 aarch64 返回空列表。

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
| `accel` | string | 否 | "kvm" | 要检查节点兼容性的加速类型。；可选值：`kvm`, `tcg` |
| `arch` | string | 否 | — | 虚拟处理器架构。默认为宿主机架构。；可选值：`x86_64`, `aarch64` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "accel": {
      "default": "kvm",
      "description": "要检查节点兼容性的加速类型。",
      "enum": [
        "kvm",
        "tcg"
      ],
      "optional": 1,
      "type": "string"
    },
    "arch": {
      "description": "虚拟处理器架构。默认为宿主机架构。",
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
        "description": "CPU 标志描述。",
        "optional": 1,
        "type": "string"
      },
      "name": {
        "description": "CPU 标志名称。",
        "type": "string"
      },
      "supported-on": {
        "description": "使用所选加速类型（“accel”）时支持此标志的节点列表。",
        "items": {
          "description": "集群节点名称。",
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
