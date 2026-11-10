# `/nodes/{node}/capabilities/qemu/machines`

原始接口路径：`/nodes/{node}/capabilities/qemu/machines`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/capabilities/qemu/machines`

获取可用 QEMU/KVM 机器类型。

**方法标识：** `types`

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
| `arch` | string | 否 | — | 虚拟处理器架构。默认为宿主机架构。；可选值：`x86_64`, `aarch64` |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "arch": {
      "description": "虚拟处理器架构。默认为宿主机架构。",
      "enum": [
        "x86_64",
        "aarch64"
      ],
      "optional": 1,
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
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
        "description": "某版本的重要更改，当前仅为 +pveX 版本设置。",
        "optional": 1,
        "type": "string"
      },
      "id": {
        "description": "机器类型和版本的完整名称。",
        "type": "string"
      },
      "type": {
        "description": "机器类型。",
        "enum": [
          "q35",
          "i440fx"
        ],
        "type": "string"
      },
      "version": {
        "description": "机器版本。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/capabilities/qemu/machines)。
