# `/cluster/sdn/vnets/{vnet}/subnets`

原始接口路径：`/cluster/sdn/vnets/{vnet}/subnets`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets/{vnet}/subnets`

SDN 子网索引。

**方法标识：** `index`

**权限**

```json
{
  "description": "仅列出您对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Audit' 或 'SDN.Allocate' 权限的条目",
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `pending` | boolean | 否 | — | 显示待应用的配置。 |
| `running` | boolean | 否 | — | 显示运行中的配置。 |
| `vnet` | string | 是 | — | SDN vnet 对象标识符。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "pending": {
      "description": "显示待应用的配置。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "running": {
      "description": "显示运行中的配置。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vnet": {
      "description": "SDN vnet 对象标识符。",
      "maxLength": 8,
      "minLength": 2,
      "pattern": "[a-zA-Z][a-zA-Z0-9]*[a-zA-Z0-9]",
      "type": "string"
    }
  }
}
```

</details>

### 返回值

```json
{
  "items": {
    "properties": {},
    "type": "object"
  },
  "links": [
    {
      "href": "{subnet}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/sdn/vnets/{vnet}/subnets`

创建新的 SDN 子网对象。

**方法标识：** `create`

**权限**

```json
{
  "description": "需要对 '/sdn/zones/<zone>/<vnet>' 具有 'SDN.Allocate' 权限",
  "user": "all"
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `dhcp-dns-server` | string | 否 | — | DNS 服务器的 IP 地址 |
| `dhcp-range` | array | 否 | — | 此子网的 DHCP 地址范围列表 |
| `dnszoneprefix` | string | 否 | — | DNS 域区域前缀  例如：'adm' -&gt; &lt;hostname&gt;.adm.mydomain.com |
| `gateway` | string | 否 | — | 子网网关：对于 layer3 区域，将分配在 vnet 上 |
| `lock-token` | string | 否 | — | 用于解锁全局 SDN 配置的令牌 |
| `snat` | boolean | 否 | — | 使用 pve-firewall 时为此子网启用地址伪装 |
| `subnet` | string | 是 | — | SDN 子网对象标识符。 |
| `type` | string | 是 | — | ；可选值：`subnet` |
| `vnet` | string | 是 | — | 关联的 vnet |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dhcp-dns-server": {
      "description": "DNS 服务器的 IP 地址",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dhcp-range": {
      "description": "此子网的 DHCP 地址范围列表",
      "items": {
        "format": "pve-sdn-dhcp-range",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "dnszoneprefix": {
      "description": "DNS 域区域前缀  例如：'adm' -> <hostname>.adm.mydomain.com",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway": {
      "description": "子网网关：对于 layer3 区域，将分配在 vnet 上",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "用于解锁全局 SDN 配置的令牌",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "snat": {
      "description": "使用 pve-firewall 时为此子网启用地址伪装",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "subnet": {
      "description": "SDN 子网对象标识符。",
      "format": "pve-sdn-subnet-id",
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "enum": [
        "subnet"
      ],
      "type": "string"
    },
    "vnet": {
      "description": "关联的 vnet",
      "optional": 0,
      "type": "string",
      "typetext": "<string>"
    }
  },
  "type": "object"
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/sdn/vnets/{vnet}/subnets)。
