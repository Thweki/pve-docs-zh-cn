# `/cluster/sdn/vnets/{vnet}/subnets`

原始接口路径：`/cluster/sdn/vnets/{vnet}/subnets`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/sdn/vnets/{vnet}/subnets`

SDN subnets index.

**方法标识：** `index`

**权限**

```json
{
  "description": "Only list entries where you have 'SDN.Audit' or 'SDN.Allocate' permissions on '/sdn/zones/<zone>/<vnet>'",
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
| `pending` | boolean | 否 | — | Display pending config. |
| `running` | boolean | 否 | — | Display running config. |
| `vnet` | string | 是 | — | The SDN vnet object identifier. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "pending": {
      "description": "Display pending config.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "running": {
      "description": "Display running config.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "vnet": {
      "description": "The SDN vnet object identifier.",
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

Create a new sdn subnet object.

**方法标识：** `create`

**权限**

```json
{
  "description": "Require 'SDN.Allocate' permission on '/sdn/zones/<zone>/<vnet>'",
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
| `dhcp-dns-server` | string | 否 | — | IP address for the DNS server |
| `dhcp-range` | array | 否 | — | A list of DHCP ranges for this subnet |
| `dnszoneprefix` | string | 否 | — | dns domain zone prefix ex: 'adm' -&gt; &lt;hostname&gt;.adm.mydomain.com |
| `gateway` | string | 否 | — | Subnet Gateway: Will be assign on vnet for layer3 zones |
| `lock-token` | string | 否 | — | the token for unlocking the global SDN configuration |
| `snat` | boolean | 否 | — | enable masquerade for this subnet if pve-firewall |
| `subnet` | string | 是 | — | The SDN subnet object identifier. |
| `type` | string | 是 | — | ；可选值：`subnet` |
| `vnet` | string | 是 | — | associated vnet |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "dhcp-dns-server": {
      "description": "IP address for the DNS server",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dhcp-range": {
      "description": "A list of DHCP ranges for this subnet",
      "items": {
        "format": "pve-sdn-dhcp-range",
        "type": "string"
      },
      "optional": 1,
      "type": "array",
      "typetext": "<array>"
    },
    "dnszoneprefix": {
      "description": "dns domain zone prefix ex: 'adm' -> <hostname>.adm.mydomain.com",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "gateway": {
      "description": "Subnet Gateway: Will be assign on vnet for layer3 zones",
      "format": "ip",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "lock-token": {
      "description": "the token for unlocking the global SDN configuration",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "snat": {
      "description": "enable masquerade for this subnet if pve-firewall",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "subnet": {
      "description": "The SDN subnet object identifier.",
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
      "description": "associated vnet",
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
