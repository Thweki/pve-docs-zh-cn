# `/cluster/sdn/ipams/{ipam}/status`

原始接口路径：`/cluster/sdn/ipams/{ipam}/status`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/ipams/{ipam}/status`

List PVE IPAM Entries

**方法标识：** `ipamindex`

**权限**

```json
{
  "description": "Only list entries where you have 'SDN.Audit' or 'SDN.Allocate' permissions on '/sdn/zones/<zone>/<vnet>'",
  "user": "all"
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
| `ipam` | string | 是 | — | The SDN ipam object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "ipam": {
      "description": "The SDN ipam object identifier.",
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/ipams/{ipam}/status)。
