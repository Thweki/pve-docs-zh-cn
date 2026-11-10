# `/cluster/ha/resources/{sid}/relocate`

原始接口路径：`/cluster/ha/resources/{sid}/relocate`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ha/resources/{sid}/relocate`

Request resource relocation to another node. This stops the service on the old node, and restarts it on the target node.

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
| `node` | string | 是 | — | Target node. |
| `sid` | string | 是 | — | HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100). |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "Target node.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "sid": {
      "description": "HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100).",
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
      "description": "HA resources, which are blocking the given HA resource from being relocated to the requested target node.",
      "items": {
        "description": "A blocking HA resource",
        "properties": {
          "cause": {
            "description": "The reason why the HA resource is blocking the relocation.",
            "enum": [
              "node-affinity",
              "resource-affinity"
            ],
            "type": "string"
          },
          "sid": {
            "description": "The blocking HA resource id",
            "type": "string"
          }
        },
        "type": "object"
      },
      "optional": 1,
      "type": "array"
    },
    "comigrated-resources": {
      "description": "HA resources, which are relocated to the same requested target node as the given HA resource, because these are in positive affinity with the HA resource.",
      "items": {
        "description": "A comigrated HA resource",
        "type": "string"
      },
      "optional": 1,
      "type": "array"
    },
    "requested-node": {
      "description": "Node, which was requested to be relocated to.",
      "optional": 0,
      "type": "string"
    },
    "sid": {
      "description": "HA resource, which is requested to be relocated.",
      "optional": 0,
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/resources/{sid}/relocate)。
