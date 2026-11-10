# `/nodes/{node}/apt/versions`

原始接口路径：`/nodes/{node}/apt/versions`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/apt/versions`

获取重要 Proxmox 软件包的软件包信息。

**方法标识：** `versions`

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
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
    "properties": {
      "Arch": {
        "description": "软件包架构。",
        "enum": [
          "armhf",
          "arm64",
          "amd64",
          "ppc64el",
          "risc64",
          "s390x",
          "all"
        ],
        "type": "string"
      },
      "CurrentState": {
        "description": "系统上安装的软件包的当前状态。",
        "enum": [
          "Installed",
          "NotInstalled",
          "UnPacked",
          "HalfConfigured",
          "HalfInstalled",
          "ConfigFiles"
        ],
        "type": "string"
      },
      "Description": {
        "description": "软件包描述。",
        "type": "string"
      },
      "ManagerVersion": {
        "description": "当前运行的 pve-manager API 服务器版本。",
        "optional": 1,
        "type": "string"
      },
      "NotifyStatus": {
        "description": "PVE 已为其发送更新通知的版本。",
        "optional": 1,
        "type": "string"
      },
      "OldVersion": {
        "description": "当前已安装的旧版本。",
        "optional": 1,
        "type": "string"
      },
      "Origin": {
        "description": "软件包来源，例如 'Proxmox' 或 'Debian'。",
        "type": "string"
      },
      "Package": {
        "description": "软件包名称。",
        "type": "string"
      },
      "Priority": {
        "description": "软件包优先级。",
        "type": "string"
      },
      "RunningKernel": {
        "description": "内核发行版本，仅用于 'proxmox-ve' 软件包。",
        "optional": 1,
        "type": "string"
      },
      "Section": {
        "description": "软件包分类。",
        "type": "string"
      },
      "Title": {
        "description": "软件包标题。",
        "type": "string"
      },
      "Version": {
        "description": "要更新到的新版本。",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/apt/versions)。
