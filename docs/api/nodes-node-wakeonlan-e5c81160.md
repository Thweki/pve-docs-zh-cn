# `/nodes/{node}/wakeonlan`

原始接口路径：`/nodes/{node}/wakeonlan`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/wakeonlan`

尝试通过“局域网唤醒”网络数据包唤醒节点。

**方法标识：** `wakeonlan`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.PowerMgmt"
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
| `node` | string | 是 | — | 局域网唤醒数据包的目标节点 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "局域网唤醒数据包的目标节点",
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
  "description": "用于构造 WoL 魔术包的 MAC 地址。",
  "format": "mac-addr",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/wakeonlan)。
