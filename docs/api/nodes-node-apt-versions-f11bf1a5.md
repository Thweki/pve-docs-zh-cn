# `/nodes/{node}/apt/versions`

原始接口路径：`/nodes/{node}/apt/versions`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/apt/versions`

Get package information for important Proxmox packages.

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
| `node` | string | 是 | — | The cluster node name. |

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
        "description": "Package Architecture.",
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
        "description": "Current state of the package installed on the system.",
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
        "description": "Package description.",
        "type": "string"
      },
      "ManagerVersion": {
        "description": "Version of the currently running pve-manager API server.",
        "optional": 1,
        "type": "string"
      },
      "NotifyStatus": {
        "description": "Version for which PVE has already sent an update notification for.",
        "optional": 1,
        "type": "string"
      },
      "OldVersion": {
        "description": "Old version currently installed.",
        "optional": 1,
        "type": "string"
      },
      "Origin": {
        "description": "Package origin, e.g., 'Proxmox' or 'Debian'.",
        "type": "string"
      },
      "Package": {
        "description": "Package name.",
        "type": "string"
      },
      "Priority": {
        "description": "Package priority.",
        "type": "string"
      },
      "RunningKernel": {
        "description": "Kernel release, only for package 'proxmox-ve'.",
        "optional": 1,
        "type": "string"
      },
      "Section": {
        "description": "Package section.",
        "type": "string"
      },
      "Title": {
        "description": "Package title.",
        "type": "string"
      },
      "Version": {
        "description": "New version to be updated to.",
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/apt/versions)。
