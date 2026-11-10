# `/nodes/{node}/hardware/usb`

原始接口路径：`/nodes/{node}/hardware/usb`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/hardware/usb`

List local USB devices.

**方法标识：** `usbscan`

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
      "busnum": {
        "type": "integer"
      },
      "class": {
        "type": "integer"
      },
      "devnum": {
        "type": "integer"
      },
      "level": {
        "type": "integer"
      },
      "manufacturer": {
        "optional": 1,
        "type": "string"
      },
      "port": {
        "type": "integer"
      },
      "prodid": {
        "type": "string"
      },
      "product": {
        "optional": 1,
        "type": "string"
      },
      "serial": {
        "optional": 1,
        "type": "string"
      },
      "speed": {
        "type": "string"
      },
      "usbpath": {
        "optional": 1,
        "type": "string"
      },
      "vendid": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/hardware/usb)。
