# `/cluster/acme/plugins`

原始接口路径：`/cluster/acme/plugins`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/acme/plugins`

ACME 插件索引。

**方法标识：** `index`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `type` | string | 否 | — | 仅列出特定类型的 ACME 插件；可选值：`dns`, `standalone` |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "type": {
      "description": "仅列出特定类型的 ACME 插件",
      "enum": [
        "dns",
        "standalone"
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
  "items": {
    "properties": {
      "api": {
        "description": "API 插件名称",
        "enum": [
          "1984hosting",
          "acmedns",
          "acmeproxy",
          "active24",
          "ad",
          "ali",
          "alviy",
          "anx",
          "artfiles",
          "arvan",
          "aurora",
          "autodns",
          "aws",
          "azion",
          "azure",
          "beget",
          "bookmyname",
          "bunny",
          "cf",
          "clouddns",
          "cloudns",
          "cn",
          "conoha",
          "constellix",
          "cpanel",
          "curanet",
          "cyon",
          "da",
          "ddnss",
          "desec",
          "df",
          "dgon",
          "dnsexit",
          "dnshome",
          "dnsimple",
          "dnsservices",
          "doapi",
          "domeneshop",
          "dp",
          "dpi",
          "dreamhost",
          "duckdns",
          "durabledns",
          "dyn",
          "dynu",
          "dynv6",
          "easydns",
          "edgecenter",
          "edgedns",
          "euserv",
          "exoscale",
          "fornex",
          "freedns",
          "freemyip",
          "gandi_livedns",
          "gcloud",
          "gcore",
          "gd",
          "geoscaling",
          "googledomains",
          "he",
          "he_ddns",
          "hetzner",
          "hetznercloud",
          "hexonet",
          "hostingde",
          "huaweicloud",
          "infoblox",
          "infomaniak",
          "internetbs",
          "inwx",
          "ionos",
          "ionos_cloud",
          "ipv64",
          "ispconfig",
          "jd",
          "joker",
          "kappernet",
          "kas",
          "kinghost",
          "knot",
          "la",
          "leaseweb",
          "lexicon",
          "limacity",
          "linode",
          "linode_v4",
          "loopia",
          "lua",
          "maradns",
          "me",
          "miab",
          "mijnhost",
          "misaka",
          "myapi",
          "mydevil",
          "mydnsjp",
          "mythic_beasts",
          "namecheap",
          "namecom",
          "namesilo",
          "nanelo",
          "nederhost",
          "neodigit",
          "netcup",
          "netlify",
          "nic",
          "njalla",
          "nm",
          "nsd",
          "nsone",
          "nsupdate",
          "nw",
          "oci",
          "omglol",
          "one",
          "online",
          "openprovider",
          "openprovider_rest",
          "openstack",
          "opnsense",
          "ovh",
          "pdns",
          "pleskxml",
          "pointhq",
          "porkbun",
          "rackcorp",
          "rackspace",
          "rage4",
          "rcode0",
          "regru",
          "scaleway",
          "schlundtech",
          "selectel",
          "selfhost",
          "servercow",
          "simply",
          "spaceship",
          "technitium",
          "tele3",
          "tencent",
          "timeweb",
          "transip",
          "udr",
          "ultra",
          "unoeuro",
          "variomedia",
          "veesp",
          "vercel",
          "vscale",
          "vultr",
          "websupport",
          "west_cn",
          "world4you",
          "yandex360",
          "yc",
          "zilore",
          "zone",
          "zoneedit",
          "zonomi"
        ],
        "optional": 1,
        "type": "string"
      },
      "data": {
        "description": "DNS 插件数据。（base64 编码）",
        "optional": 1,
        "type": "string"
      },
      "digest": {
        "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
        "maxLength": 64,
        "optional": 1,
        "type": "string"
      },
      "disable": {
        "description": "用于禁用此配置的标志。",
        "optional": 1,
        "type": "boolean"
      },
      "nodes": {
        "description": "集群节点名称列表。",
        "format": "pve-node-list",
        "optional": 1,
        "type": "string"
      },
      "plugin": {
        "description": "ACME 插件实例的唯一标识符。",
        "format": "pve-configid",
        "type": "string"
      },
      "type": {
        "description": "ACME 质询类型。",
        "enum": [
          "dns",
          "standalone"
        ],
        "type": "string"
      },
      "validation-delay": {
        "default": 30,
        "description": "请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。",
        "maximum": 172800,
        "minimum": 0,
        "optional": 1,
        "type": "integer"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{plugin}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/cluster/acme/plugins`

添加 ACME 插件配置。

**方法标识：** `add_plugin`

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `api` | string | 否 | — | API 插件名称；可选值：`1984hosting`, `acmedns`, `acmeproxy`, `active24`, `ad`, `ali`, `alviy`, `anx`, `artfiles`, `arvan`, `aurora`, `autodns`, `aws`, `azion`, `azure`, `beget`, `bookmyname`, `bunny`, `cf`, `clouddns`, `cloudns`, `cn`, `conoha`, `constellix`, `cpanel`, `curanet`, `cyon`, `da`, `ddnss`, `desec`, `df`, `dgon`, `dnsexit`, `dnshome`, `dnsimple`, `dnsservices`, `doapi`, `domeneshop`, `dp`, `dpi`, `dreamhost`, `duckdns`, `durabledns`, `dyn`, `dynu`, `dynv6`, `easydns`, `edgecenter`, `edgedns`, `euserv`, `exoscale`, `fornex`, `freedns`, `freemyip`, `gandi_livedns`, `gcloud`, `gcore`, `gd`, `geoscaling`, `googledomains`, `he`, `he_ddns`, `hetzner`, `hetznercloud`, `hexonet`, `hostingde`, `huaweicloud`, `infoblox`, `infomaniak`, `internetbs`, `inwx`, `ionos`, `ionos_cloud`, `ipv64`, `ispconfig`, `jd`, `joker`, `kappernet`, `kas`, `kinghost`, `knot`, `la`, `leaseweb`, `lexicon`, `limacity`, `linode`, `linode_v4`, `loopia`, `lua`, `maradns`, `me`, `miab`, `mijnhost`, `misaka`, `myapi`, `mydevil`, `mydnsjp`, `mythic_beasts`, `namecheap`, `namecom`, `namesilo`, `nanelo`, `nederhost`, `neodigit`, `netcup`, `netlify`, `nic`, `njalla`, `nm`, `nsd`, `nsone`, `nsupdate`, `nw`, `oci`, `omglol`, `one`, `online`, `openprovider`, `openprovider_rest`, `openstack`, `opnsense`, `ovh`, `pdns`, `pleskxml`, `pointhq`, `porkbun`, `rackcorp`, `rackspace`, `rage4`, `rcode0`, `regru`, `scaleway`, `schlundtech`, `selectel`, `selfhost`, `servercow`, `simply`, `spaceship`, `technitium`, `tele3`, `tencent`, `timeweb`, `transip`, `udr`, `ultra`, `unoeuro`, `variomedia`, `veesp`, `vercel`, `vscale`, `vultr`, `websupport`, `west_cn`, `world4you`, `yandex360`, `yc`, `zilore`, `zone`, `zoneedit`, `zonomi` |
| `data` | string | 否 | — | DNS 插件数据。（base64 编码） |
| `disable` | boolean | 否 | — | 用于禁用此配置的标志。 |
| `id` | string | 是 | — | ACME 插件 ID 名称 |
| `nodes` | string | 否 | — | 集群节点名称列表。 |
| `type` | string | 是 | — | ACME 质询类型。；可选值：`dns`, `standalone` |
| `validation-delay` | integer | 否 | 30 | 请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "api": {
      "description": "API 插件名称",
      "enum": [
        "1984hosting",
        "acmedns",
        "acmeproxy",
        "active24",
        "ad",
        "ali",
        "alviy",
        "anx",
        "artfiles",
        "arvan",
        "aurora",
        "autodns",
        "aws",
        "azion",
        "azure",
        "beget",
        "bookmyname",
        "bunny",
        "cf",
        "clouddns",
        "cloudns",
        "cn",
        "conoha",
        "constellix",
        "cpanel",
        "curanet",
        "cyon",
        "da",
        "ddnss",
        "desec",
        "df",
        "dgon",
        "dnsexit",
        "dnshome",
        "dnsimple",
        "dnsservices",
        "doapi",
        "domeneshop",
        "dp",
        "dpi",
        "dreamhost",
        "duckdns",
        "durabledns",
        "dyn",
        "dynu",
        "dynv6",
        "easydns",
        "edgecenter",
        "edgedns",
        "euserv",
        "exoscale",
        "fornex",
        "freedns",
        "freemyip",
        "gandi_livedns",
        "gcloud",
        "gcore",
        "gd",
        "geoscaling",
        "googledomains",
        "he",
        "he_ddns",
        "hetzner",
        "hetznercloud",
        "hexonet",
        "hostingde",
        "huaweicloud",
        "infoblox",
        "infomaniak",
        "internetbs",
        "inwx",
        "ionos",
        "ionos_cloud",
        "ipv64",
        "ispconfig",
        "jd",
        "joker",
        "kappernet",
        "kas",
        "kinghost",
        "knot",
        "la",
        "leaseweb",
        "lexicon",
        "limacity",
        "linode",
        "linode_v4",
        "loopia",
        "lua",
        "maradns",
        "me",
        "miab",
        "mijnhost",
        "misaka",
        "myapi",
        "mydevil",
        "mydnsjp",
        "mythic_beasts",
        "namecheap",
        "namecom",
        "namesilo",
        "nanelo",
        "nederhost",
        "neodigit",
        "netcup",
        "netlify",
        "nic",
        "njalla",
        "nm",
        "nsd",
        "nsone",
        "nsupdate",
        "nw",
        "oci",
        "omglol",
        "one",
        "online",
        "openprovider",
        "openprovider_rest",
        "openstack",
        "opnsense",
        "ovh",
        "pdns",
        "pleskxml",
        "pointhq",
        "porkbun",
        "rackcorp",
        "rackspace",
        "rage4",
        "rcode0",
        "regru",
        "scaleway",
        "schlundtech",
        "selectel",
        "selfhost",
        "servercow",
        "simply",
        "spaceship",
        "technitium",
        "tele3",
        "tencent",
        "timeweb",
        "transip",
        "udr",
        "ultra",
        "unoeuro",
        "variomedia",
        "veesp",
        "vercel",
        "vscale",
        "vultr",
        "websupport",
        "west_cn",
        "world4you",
        "yandex360",
        "yc",
        "zilore",
        "zone",
        "zoneedit",
        "zonomi"
      ],
      "optional": 1,
      "type": "string"
    },
    "data": {
      "description": "DNS 插件数据。（base64 编码）",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "用于禁用此配置的标志。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "ACME 插件 ID 名称",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "nodes": {
      "description": "集群节点名称列表。",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "ACME 质询类型。",
      "enum": [
        "dns",
        "standalone"
      ],
      "type": "string"
    },
    "validation-delay": {
      "default": 30,
      "description": "请求验证前额外等待的秒数。用于应对 DNS 记录 TTL 较长的情况。",
      "maximum": 172800,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 172800)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/plugins)。
