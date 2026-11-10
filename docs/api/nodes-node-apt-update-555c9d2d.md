# `/nodes/{node}/apt/update`

原始接口路径：`/nodes/{node}/apt/update`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/apt/update`

列出可用更新。

**方法标识：** `list_updates`

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
      "Description": {
        "description": "软件包描述。",
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

## POST `/nodes/{node}/apt/update`

用于从源重新同步软件包索引文件（apt-get update）。

**方法标识：** `update_database`

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
| `node` | string | 是 | — | 集群节点名称。 |
| `notify` | boolean | 否 | 0 | 发送新软件包通知。 |
| `quiet` | boolean | 否 | 0 | 仅生成适合日志记录的输出，省略进度指示器。 |

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
    },
    "notify": {
      "default": 0,
      "description": "发送新软件包通知。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "quiet": {
      "default": 0,
      "description": "仅生成适合日志记录的输出，省略进度指示器。",
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
