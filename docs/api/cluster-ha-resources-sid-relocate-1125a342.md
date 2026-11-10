# `/cluster/ha/resources/{sid}/relocate`

原始接口路径：`/cluster/ha/resources/{sid}/relocate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ha/resources/{sid}/relocate`

请求将资源重新安置到另一节点。此操作会停止旧节点上的服务，并在目标节点上重新启动。

**方法标识：** `relocate`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Console"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 目标节点。 |
| `sid` | string | 是 | — | HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "目标节点。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "sid": {
      "description": "HA 资源 ID。由资源类型和资源特定名称组成，以冒号分隔（例如 vm:100 / ct:100）。对于虚拟机和容器，可直接使用 VM 或 CT ID 作为简写（例如 100）。",
      "format": "pve-ha-resource-or-vm-id",
      "type": "string",
      "typetext": "<type>:<name>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "blocking-resources": {
      "description": "阻止将给定 HA 资源重新安置到请求的目标节点的 HA 资源。",
      "items": {
        "description": "阻塞迁移的 HA 资源",
        "properties": {
          "cause": {
            "description": "此 HA 资源阻塞重新安置的原因。",
            "enum": [
              "node-affinity",
              "resource-affinity"
            ],
            "type": "string"
          },
          "sid": {
            "description": "阻塞迁移的 HA 资源 ID",
            "type": "string"
          }
        },
        "type": "object"
      },
      "optional": 1,
      "type": "array"
    },
    "comigrated-resources": {
      "description": "由于与给定 HA 资源具有正向亲和性，而重新安置到相同请求目标节点的 HA 资源。",
      "items": {
        "description": "一同迁移的 HA 资源",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "requested-node": {
      "description": "请求重新安置到的节点。",
      "optional": 0,
      "type": "string"
    },
    "sid": {
      "description": "请求重新安置的 HA 资源。",
      "optional": 0,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources/{sid}/relocate)。
