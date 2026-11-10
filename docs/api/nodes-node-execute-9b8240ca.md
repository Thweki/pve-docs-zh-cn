# `/nodes/{node}/execute`

原始接口路径：`/nodes/{node}/execute`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/execute`

Execute multiple commands in order, root only.

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
| `commands` | string | 是 | — | JSON encoded array of commands. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "commands": {
      "description": "JSON encoded array of commands.",
      "format": "pve-command-batch",
      "type": "string",
      "typetext": "<string>",
      "verbose_description": "JSON encoded array of commands, where each command is an object with the following properties:\n  args:      <object>\n\t     A set of parameter names and their values.\n\n  method:    (GET|POST|PUT|DELETE)\n\t     A method related to the API endpoint (GET, POST etc.).\n\n  path:      <string>\n\t     A relative path to an API endpoint on this node.\n\n"
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
  "items": {
    "properties": {},
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/execute)。
