# `/nodes/{node}/query-oci-repo-tags`

原始接口路径：`/nodes/{node}/query-oci-repo-tags`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/query-oci-repo-tags`

List all tags for an OCI repository reference.

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
    [
      "Sys.AccessNetwork"
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
| `node` | string | 是 | — | The cluster node name. |
| `reference` | string | 是 | — | The reference to the repository to query tags from. |

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
    },
    "reference": {
      "description": "The reference to the repository to query tags from.",
      "pattern": "^(?:(?:[a-zA-Z\\d]|[a-zA-Z\\d][a-zA-Z\\d-]*[a-zA-Z\\d])(?:\\.(?:[a-zA-Z\\d]|[a-zA-Z\\d][a-zA-Z\\d-]*[a-zA-Z\\d]))*(?::\\d+)?/)?[a-z\\d]+(?:(?:[._]|__|[-]*)[a-z\\d]+)*(?:/[a-z\\d]+(?:(?:[._]|__|[-]*)[a-z\\d]+)*)*$",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "type": "string"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/query-oci-repo-tags)。
