# `/nodes/{node}/capabilities/qemu/cpu`

原始接口路径：`/nodes/{node}/capabilities/qemu/cpu`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/capabilities/qemu/cpu`

列出所有自定义和默认 CPU 型号。

**方法标识：** `index`

**权限**

```json
{
  "description": "自定义型号会筛选为当前用户对 /mapping/cpu/<name> 具有 Mapping.{Audit,Use,Modify} 中任意权限的型号；为向后兼容，对 /nodes 的 Sys.Audit 权限仍允许查看所有自定义型号。",
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
    "properties": {
      "abstract": {
        "description": "对于 x86-64-v2、-v3、-v4 等 PVE 内部抽象配置，为 true。它们不对应 QEMU CPU 类型，不能用作自定义型号的 'reported-model'。",
        "optional": 1,
        "type": "boolean"
      },
      "custom": {
        "description": "如果这是自定义 CPU 型号，则为 true。",
        "type": "boolean"
      },
      "name": {
        "description": "CPU 型号名称。在后续 API 调用中用作标识。自定义型号带有 'custom-' 前缀。",
        "type": "string"
      },
      "vendor": {
        "description": "选择此型号时客户机可见的 CPU 供应商。对于自定义型号，为 'reported-model' 的供应商。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{name}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/capabilities/qemu/cpu)。
