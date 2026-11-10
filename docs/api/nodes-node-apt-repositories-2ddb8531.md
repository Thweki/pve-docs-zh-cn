# `/nodes/{node}/apt/repositories`

原始接口路径：`/nodes/{node}/apt/repositories`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/apt/repositories`

Get APT repository information.

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
  "description": "Result from parsing the APT repository files in /etc/apt/.",
  "properties": {
    "digest": {
      "description": "Common digest of all files.",
      "type": "string"
    },
    "errors": {
      "description": "List of problematic repository files.",
      "items": {
        "properties": {
          "error": {
            "description": "The error message",
            "type": "string"
          },
          "path": {
            "description": "Path to the problematic file.",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "files": {
      "description": "List of parsed repository files.",
      "items": {
        "properties": {
          "digest": {
            "description": "Digest of the file as bytes.",
            "items": {
              "type": "integer"
            },
            "type": "array"
          },
          "file-type": {
            "description": "Format of the file.",
            "enum": [
              "list",
              "sources"
            ],
            "type": "string"
          },
          "path": {
            "description": "Path to the problematic file.",
            "type": "string"
          },
          "repositories": {
            "description": "The parsed repositories.",
            "items": {
              "properties": {
                "Comment": {
                  "description": "Associated comment",
                  "optional": 1,
                  "type": "string"
                },
                "Components": {
                  "description": "List of repository components",
                  "items": {
                    "type": "string"
                  },
                  "optional": 1,
                  "type": "array"
                },
                "Enabled": {
                  "description": "Whether the repository is enabled or not",
                  "type": "boolean"
                },
                "FileType": {
                  "description": "Format of the defining file.",
                  "enum": [
                    "list",
                    "sources"
                  ],
                  "type": "string"
                },
                "Options": {
                  "description": "Additional options",
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
                  "description": "List of package distribuitions",
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "Types": {
                  "description": "List of package types.",
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
                  "description": "List of repository URIs.",
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
      "description": "Additional information/warnings for APT repositories.",
      "items": {
        "properties": {
          "index": {
            "description": "Index of the associated repository within the file.",
            "type": "string"
          },
          "kind": {
            "description": "Kind of the information (e.g. warning).",
            "type": "string"
          },
          "message": {
            "description": "Information message.",
            "type": "string"
          },
          "path": {
            "description": "Path to the associated file.",
            "type": "string"
          },
          "property": {
            "description": "Property from which the info originates.",
            "optional": 1,
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "standard-repos": {
      "description": "List of standard repositories and their configuration status",
      "items": {
        "properties": {
          "handle": {
            "description": "Handle to identify the repository.",
            "type": "string"
          },
          "name": {
            "description": "Full name of the repository.",
            "type": "string"
          },
          "status": {
            "description": "Indicating enabled/disabled status, if the repository is configured.",
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

Change the properties of a repository. Currently only allows enabling/disabling.

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
| `digest` | string | 否 | — | Digest to detect modifications. |
| `enabled` | boolean | 否 | — | Whether the repository should be enabled or not. |
| `index` | integer | 是 | — | Index within the file (starting from 0). |
| `node` | string | 是 | — | The cluster node name. |
| `path` | string | 是 | — | Path to the containing file. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "Digest to detect modifications.",
      "maxLength": 80,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "enabled": {
      "description": "Whether the repository should be enabled or not.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "index": {
      "description": "Index within the file (starting from 0).",
      "type": "integer",
      "typetext": "<integer>"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "path": {
      "description": "Path to the containing file.",
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

Add a standard repository to the configuration

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
| `digest` | string | 否 | — | Digest to detect modifications. |
| `handle` | string | 是 | — | Handle that identifies a repository. |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "Digest to detect modifications.",
      "maxLength": 80,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "handle": {
      "description": "Handle that identifies a repository.",
      "type": "string",
      "typetext": "<string>"
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
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/apt/repositories)。
