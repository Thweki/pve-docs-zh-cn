# `/version`

原始接口路径：`/version`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/version`

API 版本详情，包括部分全局数据中心配置。

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
      "description": "默认使用的控制台查看器。",
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
      "description": "当前 Proxmox VE 小版本，采用 `x.y` 格式。",
      "type": "string"
    },
    "repoid": {
      "description": "构建此版本所用的简短 git 修订号。",
      "pattern": "[0-9a-fA-F]{8,64}",
      "type": "string"
    },
    "version": {
      "description": "此节点的完整 pve-manager 软件包版本。",
      "type": "string"
    }
  },
  "type": "object"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/version)。
