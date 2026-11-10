# `/nodes/{node}/qemu/{vmid}/agent`

原始接口路径：`/nodes/{node}/qemu/{vmid}/agent`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu/{vmid}/agent`

QEMU Guest Agent 命令索引。

**方法标识：** `index`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 1,
  "properties": {
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
  "description": "返回 QEMU Guest Agent 命令列表",
  "items": {
    "properties": {},
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

## POST `/nodes/{node}/qemu/{vmid}/agent`

执行 QEMU 客户机代理命令。

**方法标识：** `agent`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.GuestAgent.Unrestricted",
      "VM.GuestAgent.Unrestricted"
    ],
    "any",
    1
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
| `command` | string | 是 | — | QGA 命令。；可选值：`fsfreeze-freeze`, `fsfreeze-status`, `fsfreeze-thaw`, `fstrim`, `get-fsinfo`, `get-host-name`, `get-memory-block-info`, `get-memory-blocks`, `get-osinfo`, `get-time`, `get-timezone`, `get-users`, `get-vcpus`, `info`, `network-get-interfaces`, `ping`, `shutdown`, `suspend-disk`, `suspend-hybrid`, `suspend-ram` |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "command": {
      "description": "QGA 命令。",
      "enum": [
        "fsfreeze-freeze",
        "fsfreeze-status",
        "fsfreeze-thaw",
        "fstrim",
        "get-fsinfo",
        "get-host-name",
        "get-memory-block-info",
        "get-memory-blocks",
        "get-osinfo",
        "get-time",
        "get-timezone",
        "get-users",
        "get-vcpus",
        "info",
        "network-get-interfaces",
        "ping",
        "shutdown",
        "suspend-disk",
        "suspend-hybrid",
        "suspend-ram"
      ],
      "type": "string"
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
  "description": "返回仅含一个 `result` 属性的对象。",
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu/{vmid}/agent)。
