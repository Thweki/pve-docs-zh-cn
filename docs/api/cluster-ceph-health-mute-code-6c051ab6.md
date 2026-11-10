# `/cluster/ceph/health-mute/{code}`

原始接口路径：`/cluster/ceph/health-mute/{code}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/cluster/ceph/health-mute/{code}`

静默或取消静默 Ceph 健康检查。静默的检查不再计入集群状态，但仍然可见且会继续评估。

**方法标识：** `health_mute`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `code` | string | 是 | — | 要静默的健康检查，使用 'ceph health' 报告的名称，例如 'AUTH_INSECURE_CLIENT_KEY_TYPE'。 |
| `sticky` | boolean | 否 | 0 | 即使检查情况恶化也保持静默。若不启用，则受影响条目数量一旦增加，静默便会自动解除，使该检查重新引起注意。仅在静默时使用。 |
| `ttl` | string | 否 | — | 静默持续时间，例如 '2h'、'3d' 或 '1w'。省略则静默永不过期。仅在静默时使用。 |
| `value` | boolean | 是 | — | 是静默（true）还是取消静默（false）此检查。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "code": {
      "description": "要静默的健康检查，使用 'ceph health' 报告的名称，例如 'AUTH_INSECURE_CLIENT_KEY_TYPE'。",
      "maxLength": 64,
      "pattern": "[A-Z][A-Z0-9_]+",
      "type": "string"
    },
    "sticky": {
      "default": 0,
      "description": "即使检查情况恶化也保持静默。若不启用，则受影响条目数量一旦增加，静默便会自动解除，使该检查重新引起注意。仅在静默时使用。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ttl": {
      "description": "静默持续时间，例如 '2h'、'3d' 或 '1w'。省略则静默永不过期。仅在静默时使用。",
      "optional": 1,
      "pattern": "\\d+[ \\t]*(?:s|sec|seconds?|m|min|minutes?|h|hr|hours?|d|days?|w|wk|weeks?|mo|months?|y|yr|years?)(?:[ \\t]*\\d+[ \\t]*(?:s|sec|seconds?|m|min|minutes?|h|hr|hours?|d|days?|w|wk|weeks?|mo|months?|y|yr|years?))*(?!\\n)",
      "type": "string"
    },
    "value": {
      "description": "是静默（true）还是取消静默（false）此检查。",
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ceph/health-mute/{code})。
