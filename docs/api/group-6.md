# version API

本章包含此资源组的全部接口，按路径和 HTTP 方法在同一页展开。接口路径、方法、参数、类型、约束和默认值保持原值。

## `/version` <a href="#api-version-c77d9d7f" id="api-version-c77d9d7f"></a>

原始接口路径：`/version`。

### GET `/version` <a href="#api-version-c77d9d7f-get" id="api-version-c77d9d7f-get"></a>

API 版本详情，包括部分全局数据中心配置。

**方法标识：** `version`

**权限**

```text
{
  "user": "all"
}
```

**允许 API 令牌**

```text
1
```

#### 请求参数 <a href="#api-version-c77d9d7f-get-parameters" id="api-version-c77d9d7f-get-parameters"></a>

此操作没有请求参数。

#### 返回值 <a href="#api-version-c77d9d7f-get-returns" id="api-version-c77d9d7f-get-returns"></a>

```text
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
