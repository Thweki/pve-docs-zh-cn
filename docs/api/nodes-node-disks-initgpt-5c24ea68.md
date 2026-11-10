# `/nodes/{node}/disks/initgpt`

原始接口路径：`/nodes/{node}/disks/initgpt`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/disks/initgpt`

使用 GPT 初始化磁盘

**方法标识：** `initgpt`

**权限**

```json
{
  "check": [
    "perm",
    "/",
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
| `disk` | string | 是 | — | 块设备名称 |
| `node` | string | 是 | — | 集群节点名称。 |
| `uuid` | string | 否 | — | GPT 表的 UUID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "disk": {
      "description": "块设备名称",
      "pattern": "^/dev/[a-zA-Z0-9\\/]+$",
      "type": "string"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "uuid": {
      "description": "GPT 表的 UUID",
      "maxLength": 36,
      "optional": 1,
      "pattern": "[a-fA-F0-9\\-]+",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/disks/initgpt)。
