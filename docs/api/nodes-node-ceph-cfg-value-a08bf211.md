# `/nodes/{node}/ceph/cfg/value`

原始接口路径：`/nodes/{node}/ceph/cfg/value`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/ceph/cfg/value`

从 ceph.conf 或 mon 配置数据库获取配置值。响应中的配置节和键名中的下划线统一转换为连字符，无论其在源中如何书写。

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
| `config-keys` | string | 是 | — | 以分号、逗号或空格分隔的 &lt;section&gt;:&lt;config key&gt; 项目列表。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "config-keys": {
      "description": "以分号、逗号或空格分隔的 <section>:<config key> 项目列表。",
      "maxLength": 4096,
      "pattern": "(?^:^(?:(?^i:[0-9a-z\\-_\\.]+:[0-9a-zA-Z\\-_]+))(?:[;, ](?^i:[0-9a-z\\-_\\.]+:[0-9a-zA-Z\\-_]+))*$)",
      "type": "string",
      "typetext": "<section>:<config key>[;|,| <section>:<config key>]"
    },
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
  "description": "{section} -> {key} -> value 的两级映射。配置节和键名中的下划线统一转换为连字符。",
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/ceph/cfg/value)。
