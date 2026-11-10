# `/nodes/{node}/capabilities/qemu/migration`

原始接口路径：`/nodes/{node}/capabilities/qemu/migration`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/capabilities/qemu/migration`

获取节点特有的 QEMU 迁移能力。需要对 '/nodes/&lt;node&gt;' 具有 'Sys.Audit' 权限。

**方法标识：** `capabilities`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Audit"
    ]
  ]
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
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
  "additionalProperties": 0,
  "properties": {
    "has-dbus-vmstate": {
      "description": "宿主机是否支持通过 dbus-vmstate 辅助程序在线迁移附加虚拟机状态。",
      "type": "boolean"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/capabilities/qemu/migration)。
