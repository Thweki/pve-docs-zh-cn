# `/nodes/{node}/version`

原始接口路径：`/nodes/{node}/version`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/version`

API version details

**方法标识：** `version`

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
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
  "properties": {
    "release": {
      "description": "The current installed Proxmox VE Release",
      "type": "string"
    },
    "repoid": {
      "description": "The short git commit hash ID from which this version was build",
      "type": "string"
    },
    "version": {
      "description": "The current installed pve-manager package version",
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/version)。
