# `/nodes/{node}/apt/repositories`

原始接口路径：`/nodes/{node}/apt/repositories`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/apt/repositories`

获取 APT 仓库信息。

**方法标识：** `repositories`

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
  "description": "解析 /etc/apt/. 中 APT 仓库文件的结果",
  "properties": {
    "digest": {
      "description": "所有文件的共同摘要。",
      "type": "string"
    },
    "errors": {
      "description": "存在问题的仓库文件列表。",
      "items": {
        "properties": {
          "error": {
            "description": "错误消息",
            "type": "string"
          },
          "path": {
            "description": "存在问题的文件路径。",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "files": {
      "description": "已解析的仓库文件列表。",
      "items": {
        "properties": {
          "digest": {
            "description": "文件摘要，以字节形式表示。",
            "items": {
              "type": "integer"
            },
            "type": "array"
          },
          "file-type": {
            "description": "文件格式。",
            "enum": [
              "list",
              "sources"
            ],
            "type": "string"
          },
          "path": {
            "description": "存在问题的文件路径。",
            "type": "string"
          },
          "repositories": {
            "description": "已解析的仓库。",
            "items": {
              "properties": {
                "Comment": {
                  "description": "关联注释",
                  "optional": 1,
                  "type": "string"
                },
                "Components": {
                  "description": "仓库组件列表",
                  "items": {
                    "type": "string"
                  },
                  "optional": 1,
                  "type": "array"
                },
                "Enabled": {
                  "description": "仓库是否已启用",
                  "type": "boolean"
                },
                "FileType": {
                  "description": "定义文件的格式。",
                  "enum": [
                    "list",
                    "sources"
                  ],
                  "type": "string"
                },
                "Options": {
                  "description": "附加选项",
                  "items": {
                    "properties": {
                      "Key": {
                        "type": "string"
                      },
                      "Values": {
                        "items": {
                          "type": "string"
                        },
                        "type": "array"
                      }
                    },
                    "type": "object"
                  },
                  "optional": 1,
                  "type": "array"
                },
                "Suites": {
                  "description": "软件包发行版列表",
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "Types": {
                  "description": "软件包类型列表。",
                  "items": {
                    "enum": [
                      "deb",
                      "deb-src"
                    ],
                    "type": "string"
                  },
                  "type": "array"
                },
                "URIs": {
                  "description": "仓库 URI 列表。",
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                }
              },
              "type": "object"
            },
            "type": "array"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "infos": {
      "description": "APT 仓库的附加信息/警告。",
      "items": {
        "properties": {
          "index": {
            "description": "关联仓库在文件内的索引。",
            "type": "string"
          },
          "kind": {
            "description": "信息种类（例如警告）。",
            "type": "string"
          },
          "message": {
            "description": "信息消息。",
            "type": "string"
          },
          "path": {
            "description": "关联文件的路径。",
            "type": "string"
          },
          "property": {
            "description": "信息来源的属性。",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "standard-repos": {
      "description": "标准仓库及其配置状态列表",
      "items": {
        "properties": {
          "handle": {
            "description": "用于标识仓库的句柄。",
            "type": "string"
          },
          "name": {
            "description": "仓库完整名称。",
            "type": "string"
          },
          "status": {
            "description": "如果仓库已配置，表示启用/禁用状态。",
            "optional": 1,
            "type": "boolean"
          }
        },
        "type": "object"
      },
      "type": "array"
    }
  },
  "type": "object"
}
```

## POST `/nodes/{node}/apt/repositories`

更改仓库属性。目前仅允许启用/禁用。

**方法标识：** `change_repository`

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
| `digest` | string | 否 | — | 用于检测修改的摘要。 |
| `enabled` | boolean | 否 | — | 是否应启用仓库。 |
| `index` | integer | 是 | — | 文件内的索引（从 0 开始）。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `path` | string | 是 | — | 所在文件的路径。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "用于检测修改的摘要。",
      "maxLength": 80,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enabled": {
      "description": "是否应启用仓库。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "index": {
      "description": "文件内的索引（从 0 开始）。",
      "type": "integer",
      "typetext": "<integer>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "所在文件的路径。",
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
  "type": "null"
}
```

## PUT `/nodes/{node}/apt/repositories`

将标准仓库添加到配置

**方法标识：** `add_repository`

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
| `digest` | string | 否 | — | 用于检测修改的摘要。 |
| `handle` | string | 是 | — | 标识仓库的句柄。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "用于检测修改的摘要。",
      "maxLength": 80,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "handle": {
      "description": "标识仓库的句柄。",
      "type": "string",
      "typetext": "<string>"
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/apt/repositories)。
