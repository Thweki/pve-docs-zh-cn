# `/cluster/acme/plugins/{id}`

原始接口路径：`/cluster/acme/plugins/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/acme/plugins/{id}`

Delete ACME plugin configuration.

**方法标识：** `delete_plugin`

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
| `id` | string | 是 | — | Unique identifier for ACME plugin instance. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "Unique identifier for ACME plugin instance.",
      "format": "pve-configid",
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
  "type": "null"
}
```

## GET `/cluster/acme/plugins/{id}`

Get ACME plugin configuration.

**方法标识：** `get_plugin_config`

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
| `id` | string | 是 | — | Unique identifier for ACME plugin instance. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
      "description": "Unique identifier for ACME plugin instance.",
      "format": "pve-configid",
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
  "properties": {
    "api": {
      "description": "API plugin name",
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
      "description": "DNS plugin data. (base64 encoded)",
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string"
    },
    "disable": {
      "description": "Flag to disable the config.",
      "optional": 1,
      "type": "boolean"
    },
    "nodes": {
      "description": "List of cluster node names.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string"
    },
    "plugin": {
      "description": "Unique identifier for ACME plugin instance.",
      "format": "pve-configid",
      "type": "string"
    },
    "type": {
      "description": "ACME challenge type.",
      "enum": [
        "dns",
        "standalone"
      ],
      "type": "string"
    },
    "validation-delay": {
      "default": 30,
      "description": "Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records.",
      "maximum": 172800,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    }
  },
  "type": "object"
}
```

## PUT `/cluster/acme/plugins/{id}`

Update ACME plugin configuration.

**方法标识：** `update_plugin`

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
| `api` | string | 否 | — | API plugin name；可选值：`1984hosting`, `acmedns`, `acmeproxy`, `active24`, `ad`, `ali`, `alviy`, `anx`, `artfiles`, `arvan`, `aurora`, `autodns`, `aws`, `azion`, `azure`, `beget`, `bookmyname`, `bunny`, `cf`, `clouddns`, `cloudns`, `cn`, `conoha`, `constellix`, `cpanel`, `curanet`, `cyon`, `da`, `ddnss`, `desec`, `df`, `dgon`, `dnsexit`, `dnshome`, `dnsimple`, `dnsservices`, `doapi`, `domeneshop`, `dp`, `dpi`, `dreamhost`, `duckdns`, `durabledns`, `dyn`, `dynu`, `dynv6`, `easydns`, `edgecenter`, `edgedns`, `euserv`, `exoscale`, `fornex`, `freedns`, `freemyip`, `gandi_livedns`, `gcloud`, `gcore`, `gd`, `geoscaling`, `googledomains`, `he`, `he_ddns`, `hetzner`, `hetznercloud`, `hexonet`, `hostingde`, `huaweicloud`, `infoblox`, `infomaniak`, `internetbs`, `inwx`, `ionos`, `ionos_cloud`, `ipv64`, `ispconfig`, `jd`, `joker`, `kappernet`, `kas`, `kinghost`, `knot`, `la`, `leaseweb`, `lexicon`, `limacity`, `linode`, `linode_v4`, `loopia`, `lua`, `maradns`, `me`, `miab`, `mijnhost`, `misaka`, `myapi`, `mydevil`, `mydnsjp`, `mythic_beasts`, `namecheap`, `namecom`, `namesilo`, `nanelo`, `nederhost`, `neodigit`, `netcup`, `netlify`, `nic`, `njalla`, `nm`, `nsd`, `nsone`, `nsupdate`, `nw`, `oci`, `omglol`, `one`, `online`, `openprovider`, `openprovider_rest`, `openstack`, `opnsense`, `ovh`, `pdns`, `pleskxml`, `pointhq`, `porkbun`, `rackcorp`, `rackspace`, `rage4`, `rcode0`, `regru`, `scaleway`, `schlundtech`, `selectel`, `selfhost`, `servercow`, `simply`, `spaceship`, `technitium`, `tele3`, `tencent`, `timeweb`, `transip`, `udr`, `ultra`, `unoeuro`, `variomedia`, `veesp`, `vercel`, `vscale`, `vultr`, `websupport`, `west_cn`, `world4you`, `yandex360`, `yc`, `zilore`, `zone`, `zoneedit`, `zonomi` |
| `data` | string | 否 | — | DNS plugin data. (base64 encoded) |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable` | boolean | 否 | — | Flag to disable the config. |
| `id` | string | 是 | — | ACME Plugin ID name |
| `nodes` | string | 否 | — | List of cluster node names. |
| `validation-delay` | integer | 否 | 30 | Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "api": {
      "description": "API plugin name",
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
      "description": "DNS plugin data. (base64 encoded)",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "A list of settings you want to delete.",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications.",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "Flag to disable the config.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "ACME Plugin ID name",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "nodes": {
      "description": "List of cluster node names.",
      "format": "pve-node-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "validation-delay": {
      "default": 30,
      "description": "Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/acme/plugins/{id})。
