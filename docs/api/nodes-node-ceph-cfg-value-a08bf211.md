# `/nodes/{node}/ceph/cfg/value`

原始接口路径：`/nodes/{node}/ceph/cfg/value`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/cfg/value`

Get configured values from either ceph.conf or the mon config DB. Underscores in section and key names are normalised to hyphens in the response, regardless of how they're written in the source.

**方法标识：** `value`

**权限**

```json
{
  "check": [
    "perm",
    "/",
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
| `config-keys` | string | 是 | — | List of &lt;section&gt;:&lt;config key&gt; items separated by semicolon, comma or space. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "config-keys": {
      "description": "List of <section>:<config key> items separated by semicolon, comma or space.",
      "maxLength": 4096,
      "pattern": "(?^:^(?:(?^i:[0-9a-z\\-_\\.]+:[0-9a-zA-Z\\-_]+))(?:[;, ](?^i:[0-9a-z\\-_\\.]+:[0-9a-zA-Z\\-_]+))*$)",
      "type": "string",
      "typetext": "<section>:<config key>[;|,| <section>:<config key>]"
    },
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
  "description": "Two-level map of {section} -> {key} -> value. Underscores in section and key names are normalised to hyphens.",
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/cfg/value)。
