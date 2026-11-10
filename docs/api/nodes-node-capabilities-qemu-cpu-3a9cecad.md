# `/nodes/{node}/capabilities/qemu/cpu`

原始接口路径：`/nodes/{node}/capabilities/qemu/cpu`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/capabilities/qemu/cpu`

List all custom and default CPU models.

**方法标识：** `index`

**权限**

```json
{
  "description": "Custom models are filtered to those the current user has any of Mapping.{Audit,Use,Modify} on /mapping/cpu/<name>; Sys.Audit on /nodes continues to grant visibility of all custom models for back-compat.",
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
    "properties": {
      "abstract": {
        "description": "True for PVE-internal abstract profiles like x86-64-v2, -v3, -v4. These do not correspond to a QEMU CPU type and cannot be used as a custom model's 'reported-model'.",
        "optional": 1,
        "type": "boolean"
      },
      "custom": {
        "description": "True if this is a custom CPU model.",
        "type": "boolean"
      },
      "name": {
        "description": "Name of the CPU model. Identifies it for subsequent API calls. Prefixed with 'custom-' for custom models.",
        "type": "string"
      },
      "vendor": {
        "description": "CPU vendor visible to the guest when this model is selected. Vendor of 'reported-model' in case of custom models.",
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
