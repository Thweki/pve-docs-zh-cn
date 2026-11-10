# `/version`

原始接口路径：`/version`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/version`

API version details, including some parts of the global datacenter config.

**方法标识：** `version`

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

此操作没有请求参数。

### 返回值

```json
{
  "properties": {
    "console": {
      "description": "The default console viewer to use.",
      "enum": [
        "applet",
        "vv",
        "html5",
        "xtermjs"
      ],
      "optional": 1,
      "type": "string"
    },
    "release": {
      "description": "The current Proxmox VE point release in `x.y` format.",
      "type": "string"
    },
    "repoid": {
      "description": "The short git revision from which this version was build.",
      "pattern": "[0-9a-fA-F]{8,64}",
      "type": "string"
    },
    "version": {
      "description": "The full pve-manager package version of this node.",
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/version)。
