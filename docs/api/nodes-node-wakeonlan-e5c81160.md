# `/nodes/{node}/wakeonlan`

原始接口路径：`/nodes/{node}/wakeonlan`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/wakeonlan`

Try to wake a node via 'wake on LAN' network packet.

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
| `node` | string | 是 | — | target node for wake on LAN packet |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "target node for wake on LAN packet",
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
  "description": "MAC address used to assemble the WoL magic packet.",
  "format": "mac-addr",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/wakeonlan)。
