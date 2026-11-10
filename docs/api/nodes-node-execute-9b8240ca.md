# `/nodes/{node}/execute`

原始接口路径：`/nodes/{node}/execute`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/execute`

按顺序执行多个命令，仅限 root。

**方法标识：** `execute`

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
| `commands` | string | 是 | — | JSON 编码的命令数组，其中每条命令都是具有以下属性的对象：<br>  args:      &lt;object&gt;<br>	     参数名称及其值的集合。<br><br>  method:    (GET\|POST\|PUT\|DELETE)<br>	     与 API 端点相关的方法（GET、POST 等）。<br><br>  path:      &lt;string&gt;<br>	     此节点上 API 端点的相对路径。<br><br> |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "commands": {
      "description": "JSON 编码的命令数组。",
      "format": "pve-command-batch",
      "type": "string",
      "typetext": "<string>",
      "verbose_description": "JSON 编码的命令数组，其中每条命令都是具有以下属性的对象：\n  args:      <object>\n\t     参数名称及其值的集合。\n\n  method:    (GET|POST|PUT|DELETE)\n\t     与 API 端点相关的方法（GET、POST 等）。\n\n  path:      <string>\n\t     此节点上 API 端点的相对路径。\n\n"
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
  "items": {
    "properties": {},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/execute)。
