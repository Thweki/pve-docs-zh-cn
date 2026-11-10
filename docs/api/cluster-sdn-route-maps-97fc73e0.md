# `/cluster/sdn/route-maps`

原始接口路径：`/cluster/sdn/route-maps`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/route-maps`

List Route Maps

**方法标识：** `list_route_maps`

**权限**

```json
{
  "description": "Only returns route maps where you have 'SDN.Audit' or 'SDN.Allocate' permissions.",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `running` | boolean | 否 | — | Display running config. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "properties": {
    "running": {
      "description": "Display running config.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
      "id": {
        "description": "The SDN route map identifier",
        "format": "pve-sdn-route-map-id",
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "entries/{id}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/route-maps)。
