# `/nodes/{node}/lxc/{vmid}/firewall/ipset/{name}`

原始接口路径：`/nodes/{node}/lxc/{vmid}/firewall/ipset/{name}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/nodes/{node}/lxc/{vmid}/firewall/ipset/{name}`

删除 IPSet

**方法标识：** `delete_ipset`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Network"
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
| `force` | boolean | 否 | — | 删除 IPSet 中的所有成员（如有）。 |
| `name` | string | 是 | — | IP 集合名称。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "force": {
      "description": "删除 IPSet 中的所有成员（如有）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "name": {
      "description": "IP 集合名称。",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
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
  "type": "null"
}
```

## GET `/nodes/{node}/lxc/{vmid}/firewall/ipset/{name}`

列出 IPSet 内容

**方法标识：** `get_ipset`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `name` | string | 是 | — | IP 集合名称。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "name": {
      "description": "IP 集合名称。",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
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
  "items": {
    "properties": {
      "cidr": {
        "type": "string"
      },
      "comment": {
        "optional": 1,
        "type": "string"
      },
      "digest": {
        "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
        "maxLength": 64,
        "optional": 0,
        "type": "string"
      },
      "nomatch": {
        "optional": 1,
        "type": "boolean"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{cidr}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/nodes/{node}/lxc/{vmid}/firewall/ipset/{name}`

将 IP 或网络添加到 IPSet。

**方法标识：** `create_ip`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Network"
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
| `cidr` | string | 是 | — | CIDR 格式的网络/IP 规范。 |
| `comment` | string | 否 | — |  |
| `name` | string | 是 | — | IP 集合名称。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `nomatch` | boolean | 否 | — |  |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "cidr": {
      "description": "CIDR 格式的网络/IP 规范。",
      "format": "IPorCIDRorAlias",
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "format": "pve-fw-comment-spec",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "name": {
      "description": "IP 集合名称。",
      "maxLength": 64,
      "minLength": 2,
      "pattern": "[A-Za-z][A-Za-z0-9\\-\\_]+",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "nomatch": {
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/firewall/ipset/{name})。
