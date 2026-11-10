# `/nodes/{node}/config`

原始接口路径：`/nodes/{node}/config`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/config`

Get node configuration options.

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
| `node` | string | 是 | — | The cluster node name. |
| `property` | string | 否 | "all" | Return only a specific property from the node configuration.；可选值：`acme`, `acmedomain0`, `acmedomain1`, `acmedomain2`, `acmedomain3`, `acmedomain4`, `acmedomain5`, `ballooning-target`, `description`, `location`, `startall-onboot-delay`, `wakeonlan` |

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
    "property": {
      "default": "all",
      "description": "Return only a specific property from the node configuration.",
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
      "description": "Node specific ACME settings.",
      "format": {
        "account": {
          "default": "default",
          "description": "ACME account config file name.",
          "format": "pve-configid",
          "format_description": "name",
          "optional": 1,
          "type": "string"
        },
        "domains": {
          "description": "List of domains for this node's ACME certificate",
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
      "description": "ACME domain and validation plugin",
      "format": {
        "alias": {
          "description": "Alias for the Domain to verify ACME Challenge over DNS",
          "format": "pve-acme-alias",
          "format_description": "domain",
          "optional": 1,
          "type": "string"
        },
        "domain": {
          "default_key": 1,
          "description": "domain for this node's ACME certificate",
          "format": "pve-acme-domain",
          "format_description": "domain",
          "type": "string"
        },
        "plugin": {
          "default": "standalone",
          "description": "The ACME plugin ID",
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
      "description": "RAM usage target for ballooning (in percent of total memory)",
      "maximum": 100,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "description": {
      "description": "Description for the Node. Shown in the web-interface node notes panel. This is saved as comment inside the configuration file.",
      "maxLength": 65536,
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications.",
      "maxLength": 40,
      "optional": 1,
      "type": "string"
    },
    "location": {
      "description": "The location of the node. Overrides the default from the datacenter config.",
      "format": "pve-node-location",
      "optional": 1,
      "type": "string"
    },
    "startall-onboot-delay": {
      "default": 0,
      "description": "Initial delay in seconds, before starting all the Virtual Guests with on-boot enabled.",
      "maximum": 300,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "wakeonlan": {
      "description": "Node specific wake on LAN settings.",
      "format": {
        "bind-interface": {
          "default": "The interface carrying the default route",
          "description": "Bind to this interface when sending wake on LAN packet",
          "format": "pve-iface",
          "format_description": "bind interface",
          "optional": 1,
          "type": "string"
        },
        "broadcast-address": {
          "default": "255.255.255.255",
          "description": "IPv4 broadcast address to use when sending wake on LAN packet",
          "format": "ipv4",
          "format_description": "IPv4 broadcast address",
          "optional": 1,
          "type": "string"
        },
        "mac": {
          "default_key": 1,
          "description": "MAC address for wake on LAN",
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

Set node configuration options.

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
| `acme` | string | 否 | — | Node specific ACME settings. |
| `acmedomain[n]` | string | 否 | — | ACME domain and validation plugin |
| `ballooning-target` | integer | 否 | 80 | RAM usage target for ballooning (in percent of total memory) |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `description` | string | 否 | — | Description for the Node. Shown in the web-interface node notes panel. This is saved as comment inside the configuration file. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications. |
| `location` | string | 否 | — | The location of the node. Overrides the default from the datacenter config. |
| `node` | string | 是 | — | The cluster node name. |
| `startall-onboot-delay` | integer | 否 | 0 | Initial delay in seconds, before starting all the Virtual Guests with on-boot enabled. |
| `wakeonlan` | string | 否 | — | Node specific wake on LAN settings. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "acme": {
      "description": "Node specific ACME settings.",
      "format": {
        "account": {
          "default": "default",
          "description": "ACME account config file name.",
          "format": "pve-configid",
          "format_description": "name",
          "optional": 1,
          "type": "string"
        },
        "domains": {
          "description": "List of domains for this node's ACME certificate",
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
      "description": "ACME domain and validation plugin",
      "format": {
        "alias": {
          "description": "Alias for the Domain to verify ACME Challenge over DNS",
          "format": "pve-acme-alias",
          "format_description": "domain",
          "optional": 1,
          "type": "string"
        },
        "domain": {
          "default_key": 1,
          "description": "domain for this node's ACME certificate",
          "format": "pve-acme-domain",
          "format_description": "domain",
          "type": "string"
        },
        "plugin": {
          "default": "standalone",
          "description": "The ACME plugin ID",
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
      "description": "RAM usage target for ballooning (in percent of total memory)",
      "maximum": 100,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 100)"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "Description for the Node. Shown in the web-interface node notes panel. This is saved as comment inside the configuration file.",
      "maxLength": 65536,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications.",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "location": {
      "description": "The location of the node. Overrides the default from the datacenter config.",
      "format": "pve-node-location",
      "optional": 1,
      "type": "string",
      "typetext": "latitude=<number> ,longitude=<number> [,name=<name>]"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "startall-onboot-delay": {
      "default": 0,
      "description": "Initial delay in seconds, before starting all the Virtual Guests with on-boot enabled.",
      "maximum": 300,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 300)"
    },
    "wakeonlan": {
      "description": "Node specific wake on LAN settings.",
      "format": {
        "bind-interface": {
          "default": "The interface carrying the default route",
          "description": "Bind to this interface when sending wake on LAN packet",
          "format": "pve-iface",
          "format_description": "bind interface",
          "optional": 1,
          "type": "string"
        },
        "broadcast-address": {
          "default": "255.255.255.255",
          "description": "IPv4 broadcast address to use when sending wake on LAN packet",
          "format": "ipv4",
          "format_description": "IPv4 broadcast address",
          "optional": 1,
          "type": "string"
        },
        "mac": {
          "default_key": 1,
          "description": "MAC address for wake on LAN",
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
