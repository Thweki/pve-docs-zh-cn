# `/nodes/{node}/storage/{storage}/oci-registry-pull`

原始接口路径：`/nodes/{node}/storage/{storage}/oci-registry-pull`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## POST `/nodes/{node}/storage/{storage}/oci-registry-pull`

从镜像仓库拉取 OCI 镜像。

**方法标识：** `oci_registry_pull`

**权限**

```json
{
  "check": [
    "and",
    [
      "perm",
      "/storage/{storage}",
      [
        "Datastore.AllocateTemplate"
      ]
    ],
    [
      "perm",
      "/nodes/{node}",
      [
        "Sys.AccessNetwork"
      ]
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
| `filename` | string | 否 | — | OCI 镜像的自定义目标文件名。注意：此名称将被规范化！ |
| `node` | string | 是 | — | 集群节点名称。 |
| `reference` | string | 是 | — | 要下载的 OCI 镜像的引用。 |
| `storage` | string | 是 | — | 存储标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "filename": {
      "description": "OCI 镜像的自定义目标文件名。注意：此名称将被规范化！",
      "maxLength": 255,
      "minLength": 1,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "reference": {
      "description": "要下载的 OCI 镜像的引用。",
      "pattern": "^(?:(?:[a-zA-Z\\d]|[a-zA-Z\\d][a-zA-Z\\d-]*[a-zA-Z\\d])(?:\\.(?:[a-zA-Z\\d]|[a-zA-Z\\d][a-zA-Z\\d-]*[a-zA-Z\\d]))*(?::\\d+)?/)?[a-z\\d]+(?:(?:[._]|__|[-]*)[a-z\\d]+)*(?:/[a-z\\d]+(?:(?:[._]|__|[-]*)[a-z\\d]+)*)*:\\w[\\w.-]{0,127}$",
      "type": "string"
    },
    "storage": {
      "description": "存储标识符。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "type": "string",
      "typetext": "<storage ID>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/storage/{storage}/oci-registry-pull)。
