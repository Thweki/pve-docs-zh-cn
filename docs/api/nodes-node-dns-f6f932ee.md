# `/nodes/{node}/dns`

原始接口路径：`/nodes/{node}/dns`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/dns`

读取 DNS 设置。

**方法标识：** `dns`

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
    "dns1": {
      "description": "第一个名称服务器 IP 地址。",
      "optional": 1,
      "type": "string"
    },
    "dns2": {
      "description": "第二个名称服务器 IP 地址。",
      "optional": 1,
      "type": "string"
    },
    "dns3": {
      "description": "第三个名称服务器 IP 地址。",
      "optional": 1,
      "type": "string"
    },
    "search": {
      "description": "主机名查找的搜索域。",
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/dns`

写入 DNS 设置。

**方法标识：** `update_dns`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.Modify"
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
| `dns1` | string | 否 | — | 第一个名称服务器 IP 地址。 |
| `dns2` | string | 否 | — | 第二个名称服务器 IP 地址。 |
| `dns3` | string | 否 | — | 第三个名称服务器 IP 地址。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `search` | string | 是 | — | 主机名查找的搜索域。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dns1": {
      "description": "第一个名称服务器 IP 地址。",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dns2": {
      "description": "第二个名称服务器 IP 地址。",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dns3": {
      "description": "第三个名称服务器 IP 地址。",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "search": {
      "description": "主机名查找的搜索域。",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/dns)。
