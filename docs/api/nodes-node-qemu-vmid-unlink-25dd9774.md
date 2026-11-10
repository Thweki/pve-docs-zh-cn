# `/nodes/{node}/qemu/{vmid}/unlink`

原始接口路径：`/nodes/{node}/qemu/{vmid}/unlink`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/nodes/{node}/qemu/{vmid}/unlink`

解除链接/删除磁盘镜像。

**方法标识：** `unlink`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Disk"
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
| `force` | boolean | 否 | — | 强制物理移除。若不启用，则仅从配置文件中移除磁盘，并创建名为 'unused[n]' 的附加配置条目，其中包含卷 ID。解除 unused[n] 链接总会导致物理移除。 |
| `idlist` | string | 是 | — | 要删除的磁盘 ID 列表。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "description": "强制物理移除。若不启用，则仅从配置文件中移除磁盘，并创建名为 'unused[n]' 的附加配置条目，其中包含卷 ID。解除 unused[n] 链接总会导致物理移除。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "idlist": {
      "description": "要删除的磁盘 ID 列表。",
      "format": "pve-configid-list",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/unlink)。
