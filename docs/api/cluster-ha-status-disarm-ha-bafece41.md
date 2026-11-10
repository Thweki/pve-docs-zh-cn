# `/cluster/ha/status/disarm-ha`

原始接口路径：`/cluster/ha/status/disarm-ha`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/cluster/ha/status/disarm-ha`

请求解除 HA 堆栈的布防，并释放整个集群范围内的所有看门狗。

**方法标识：** `disarm-ha`

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
| `resource-mode` | string | 是 | — | 控制解除后如何处理 HA 管理的资源。资源的当前状态不受影响。'freeze'：不应用新命令和状态更改。'ignore'：将资源移出 HA 跟踪，此后可按未受 HA 管理的资源进行管理。；可选值：`freeze`, `ignore` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "resource-mode": {
      "description": "控制解除后如何处理 HA 管理的资源。资源的当前状态不受影响。'freeze'：不应用新命令和状态更改。'ignore'：将资源移出 HA 跟踪，此后可按未受 HA 管理的资源进行管理。",
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
