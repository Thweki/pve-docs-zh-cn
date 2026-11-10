# `/nodes/{node}/version`

原始接口路径：`/nodes/{node}/version`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/version`

API 版本详情

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
  "properties": {
    "release": {
      "description": "当前安装的 Proxmox VE 发行版",
      "type": "string"
    },
    "repoid": {
      "description": "构建此版本所用的简短 git 提交哈希 ID",
      "type": "string"
    },
    "version": {
      "description": "当前安装的 pve-manager 软件包版本",
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/version)。
