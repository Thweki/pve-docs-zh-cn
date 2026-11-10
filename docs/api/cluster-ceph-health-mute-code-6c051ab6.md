# `/cluster/ceph/health-mute/{code}`

原始接口路径：`/cluster/ceph/health-mute/{code}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/cluster/ceph/health-mute/{code}`

Mute or unmute a Ceph health check. A muted check no longer counts towards the cluster status, but stays visible and keeps being evaluated.

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
| `code` | string | 是 | — | The health check to mute, as reported by 'ceph health', for example 'AUTH_INSECURE_CLIENT_KEY_TYPE'. |
| `sticky` | boolean | 否 | 0 | Keep the mute even when the check gets worse. Without this a mute clears itself as soon as the number of affected items grows, which brings the check back to attention. Only used when muting. |
| `ttl` | string | 否 | — | How long the mute lasts, for example '2h', '3d' or '1w'. Without it the mute has no expiry. Only used when muting. |
| `value` | boolean | 是 | — | Whether to mute (true) or unmute (false) the check. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "code": {
      "description": "The health check to mute, as reported by 'ceph health', for example 'AUTH_INSECURE_CLIENT_KEY_TYPE'.",
      "maxLength": 64,
      "pattern": "[A-Z][A-Z0-9_]+",
      "type": "string"
    },
    "sticky": {
      "default": 0,
      "description": "Keep the mute even when the check gets worse. Without this a mute clears itself as soon as the number of affected items grows, which brings the check back to attention. Only used when muting.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ttl": {
      "description": "How long the mute lasts, for example '2h', '3d' or '1w'. Without it the mute has no expiry. Only used when muting.",
      "optional": 1,
      "pattern": "\\d+[ \\t]*(?:s|sec|seconds?|m|min|minutes?|h|hr|hours?|d|days?|w|wk|weeks?|mo|months?|y|yr|years?)(?:[ \\t]*\\d+[ \\t]*(?:s|sec|seconds?|m|min|minutes?|h|hr|hours?|d|days?|w|wk|weeks?|mo|months?|y|yr|years?))*(?!\\n)",
      "type": "string"
    },
    "value": {
      "description": "Whether to mute (true) or unmute (false) the check.",
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
