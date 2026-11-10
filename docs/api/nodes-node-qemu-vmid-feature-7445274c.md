# `/nodes/{node}/qemu/{vmid}/feature`

原始接口路径：`/nodes/{node}/qemu/{vmid}/feature`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/feature`

Check if feature for virtual machine is available.

**方法标识：** `vm_feature`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
    ]
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
| `feature` | string | 是 | — | Feature to check.；可选值：`snapshot`, `clone`, `copy` |
| `node` | string | 是 | — | The cluster node name. |
| `snapname` | string | 否 | — | The name of the snapshot. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "feature": {
      "description": "Feature to check.",
      "enum": [
        "snapshot",
        "clone",
        "copy"
      ],
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "snapname": {
      "description": "The name of the snapshot.",
      "format": "pve-configid",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
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
  "properties": {
    "hasFeature": {
      "type": "boolean"
    },
    "nodes": {
      "items": {
        "type": "string"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/feature)。
