# `/cluster/ha/status/disarm-ha`

原始接口路径：`/cluster/ha/status/disarm-ha`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ha/status/disarm-ha`

请求解除 HA 堆栈的布防，并释放整个集群范围内的所有看门狗。

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Console"
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
| `resource-mode` | string | 是 | — | Controls how HA managed resources are handled while disarmed. The current state of resources is not affected. 'freeze': new commands and state changes are not applied. 'ignore': resources are removed from HA tracking and can be managed as if they were not HA managed.；可选值：`freeze`, `ignore` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "resource-mode": {
      "description": "Controls how HA managed resources are handled while disarmed. The current state of resources is not affected. 'freeze': new commands and state changes are not applied. 'ignore': resources are removed from HA tracking and can be managed as if they were not HA managed.",
      "enum": [
        "freeze",
        "ignore"
      ],
      "type": "string"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/ha/status/disarm-ha)。
