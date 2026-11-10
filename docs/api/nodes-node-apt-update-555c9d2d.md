# `/nodes/{node}/apt/update`

原始接口路径：`/nodes/{node}/apt/update`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/apt/update`

List available updates.

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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
      "Description": {
        "description": "Package description.",
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

## POST `/nodes/{node}/apt/update`

This is used to resynchronize the package index files from their sources (apt-get update).

**权限**

```json
{
  "check": [
    "perm",
    "/nodes/{node}",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |
| `notify` | boolean | 否 | 0 | Send notification about new packages. |
| `quiet` | boolean | 否 | 0 | Only produces output suitable for logging, omitting progress indicators. |

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
    },
    "notify": {
      "default": 0,
      "description": "Send notification about new packages.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "quiet": {
      "default": 0,
      "description": "Only produces output suitable for logging, omitting progress indicators.",
      "optional": 1,
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/apt/update)。
