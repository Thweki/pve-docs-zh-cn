# `/nodes/{node}/config`

原始接口路径：`/nodes/{node}/config`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/config`

获取节点配置选项。

**方法标识：** `get_config`

**权限**

```json
{
  "check": [
    "perm",
    "/",
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
| `property` | string | 否 | "all" | 仅返回节点配置中的特定属性。；可选值：`acme`, `acmedomain0`, `acmedomain1`, `acmedomain2`, `acmedomain3`, `acmedomain4`, `acmedomain5`, `ballooning-target`, `description`, `location`, `startall-onboot-delay`, `wakeonlan` |

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
    "property": {
      "default": "all",
      "description": "仅返回节点配置中的特定属性。",
      "enum": [
        "acme",
        "acmedomain0",
        "acmedomain1",
        "acmedomain2",
        "acmedomain3",
        "acmedomain4",
        "acmedomain5",
        "ballooning-target",
        "description",
        "location",
        "startall-onboot-delay",
        "wakeonlan"
      ],
      "optional": 1,
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "acme": {
      "description": "节点特定 ACME 设置。",
      "format": {
        "account": {
          "default": "default",
          "description": "ACME 账户配置文件名。",
          "format": "pve-configid",
          "format_description": "name",
          "optional": 1,
          "type": "string"
        },
        "domains": {
          "description": "此节点 ACME 证书的域名列表",
          "format": "pve-acme-domain-list",
          "format_description": "domain[;domain;...]",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "acmedomain[n]": {
      "description": "ACME 域名和验证插件",
      "format": {
        "alias": {
          "description": "用于通过 DNS 验证 ACME 质询的域名别名",
          "format": "pve-acme-alias",
          "format_description": "domain",
          "optional": 1,
          "type": "string"
        },
        "domain": {
          "default_key": 1,
          "description": "此节点 ACME 证书的域名",
          "format": "pve-acme-domain",
          "format_description": "domain",
          "type": "string"
        },
        "plugin": {
          "default": "standalone",
          "description": "ACME 插件 ID",
          "format": "pve-configid",
          "format_description": "name of the plugin configuration",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "ballooning-target": {
      "default": 80,
      "description": "ballooning 的 RAM 使用目标（占总内存的百分比）",
      "maximum": 100,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "description": {
      "description": "节点描述。显示在 Web 界面的节点备注面板中。作为注释保存在配置文件中。",
      "maxLength": 65536,
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。",
      "maxLength": 40,
      "optional": 1,
      "type": "string"
    },
    "location": {
      "description": "节点位置。覆盖数据中心配置中的默认值。",
      "format": "pve-node-location",
      "optional": 1,
      "type": "string"
    },
    "startall-onboot-delay": {
      "default": 0,
      "description": "启动所有启用了 on-boot 的虚拟客户机前的初始延迟，单位为秒。",
      "maximum": 300,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "wakeonlan": {
      "description": "节点特定的局域网唤醒设置。",
      "format": {
        "bind-interface": {
          "default": "The interface carrying the default route",
          "description": "发送局域网唤醒数据包时绑定到此接口",
          "format": "pve-iface",
          "format_description": "bind interface",
          "optional": 1,
          "type": "string"
        },
        "broadcast-address": {
          "default": "255.255.255.255",
          "description": "发送局域网唤醒数据包时使用的 IPv4 广播地址",
          "format": "ipv4",
          "format_description": "IPv4 broadcast address",
          "optional": 1,
          "type": "string"
        },
        "mac": {
          "default_key": 1,
          "description": "用于局域网唤醒的 MAC 地址",
          "format": "mac-addr",
          "format_description": "MAC address",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    }
  },
  "type": "object"
}
```

## PUT `/nodes/{node}/config`

设置节点配置选项。

**方法标识：** `set_options`

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
| `acme` | string | 否 | — | 节点特定 ACME 设置。 |
| `acmedomain[n]` | string | 否 | — | ACME 域名和验证插件 |
| `ballooning-target` | integer | 否 | 80 | ballooning 的 RAM 使用目标（占总内存的百分比） |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `description` | string | 否 | — | 节点描述。显示在 Web 界面的节点备注面板中。作为注释保存在配置文件中。 |
| `digest` | string | 否 | — | 如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。 |
| `location` | string | 否 | — | 节点位置。覆盖数据中心配置中的默认值。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `startall-onboot-delay` | integer | 否 | 0 | 启动所有启用了 on-boot 的虚拟客户机前的初始延迟，单位为秒。 |
| `wakeonlan` | string | 否 | — | 节点特定的局域网唤醒设置。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "acme": {
      "description": "节点特定 ACME 设置。",
      "format": {
        "account": {
          "default": "default",
          "description": "ACME 账户配置文件名。",
          "format": "pve-configid",
          "format_description": "name",
          "optional": 1,
          "type": "string"
        },
        "domains": {
          "description": "此节点 ACME 证书的域名列表",
          "format": "pve-acme-domain-list",
          "format_description": "domain[;domain;...]",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[account=<name>] [,domains=<domain[;domain;...]>]"
    },
    "acmedomain[n]": {
      "description": "ACME 域名和验证插件",
      "format": {
        "alias": {
          "description": "用于通过 DNS 验证 ACME 质询的域名别名",
          "format": "pve-acme-alias",
          "format_description": "domain",
          "optional": 1,
          "type": "string"
        },
        "domain": {
          "default_key": 1,
          "description": "此节点 ACME 证书的域名",
          "format": "pve-acme-domain",
          "format_description": "domain",
          "type": "string"
        },
        "plugin": {
          "default": "standalone",
          "description": "ACME 插件 ID",
          "format": "pve-configid",
          "format_description": "name of the plugin configuration",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[domain=]<domain> [,alias=<domain>] [,plugin=<name of the plugin configuration>]"
    },
    "ballooning-target": {
      "default": 80,
      "description": "ballooning 的 RAM 使用目标（占总内存的百分比）",
      "maximum": 100,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 100)"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "节点描述。显示在 Web 界面的节点备注面板中。作为注释保存在配置文件中。",
      "maxLength": 65536,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "location": {
      "description": "节点位置。覆盖数据中心配置中的默认值。",
      "format": "pve-node-location",
      "optional": 1,
      "type": "string",
      "typetext": "latitude=<number> ,longitude=<number> [,name=<name>]"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "startall-onboot-delay": {
      "default": 0,
      "description": "启动所有启用了 on-boot 的虚拟客户机前的初始延迟，单位为秒。",
      "maximum": 300,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 300)"
    },
    "wakeonlan": {
      "description": "节点特定的局域网唤醒设置。",
      "format": {
        "bind-interface": {
          "default": "The interface carrying the default route",
          "description": "发送局域网唤醒数据包时绑定到此接口",
          "format": "pve-iface",
          "format_description": "bind interface",
          "optional": 1,
          "type": "string"
        },
        "broadcast-address": {
          "default": "255.255.255.255",
          "description": "发送局域网唤醒数据包时使用的 IPv4 广播地址",
          "format": "ipv4",
          "format_description": "IPv4 broadcast address",
          "optional": 1,
          "type": "string"
        },
        "mac": {
          "default_key": 1,
          "description": "用于局域网唤醒的 MAC 地址",
          "format": "mac-addr",
          "format_description": "MAC address",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[mac=]<MAC address> [,bind-interface=<bind interface>] [,broadcast-address=<IPv4 broadcast address>]"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/config)。
