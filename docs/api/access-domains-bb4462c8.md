# `/access/domains`

原始接口路径：`/access/domains`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/access/domains`

认证域索引。

**方法标识：** `index`

**权限**

```json
{
  "description": "任何人均可访问，因为登录框在用户通过身份验证之前就需要此列表。",
  "user": "world"
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
  "items": {
    "properties": {
      "comment": {
        "description": "注释。在登录窗口中选择域（认证域）时，GUI 使用此文本。",
        "optional": 1,
        "type": "string"
      },
      "realm": {
        "type": "string"
      },
      "tfa": {
        "description": "双因素身份验证提供程序。",
        "enum": [
          "yubico",
          "oath"
        ],
        "optional": 1,
        "type": "string"
      },
      "type": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{realm}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/access/domains`

添加认证服务器。

**方法标识：** `create`

**权限**

```json
{
  "check": [
    "perm",
    "/access/realm",
    [
      "Realm.Allocate"
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
| `acr-values` | string | 否 | — | 指定请求授权服务器在身份验证请求中使用的身份验证上下文类引用值。 |
| `audiences` | string | 否 | — | 除 'client-id' 外，也接受 OpenID 颁发者可能包含的受众列表。 |
| `autocreate` | boolean | 否 | 0 | 如果用户不存在，则自动创建。 |
| `base_dn` | string | 否 | — | LDAP 基础域名 |
| `bind_dn` | string | 否 | — | LDAP 绑定域名 |
| `capath` | string | 否 | "/etc/ssl/certs" | CA 证书存储路径 |
| `case-sensitive` | boolean | 否 | 1 | 用户名区分大小写 |
| `cert` | string | 否 | — | 客户端证书路径 |
| `certkey` | string | 否 | — | 客户端证书密钥路径 |
| `check-connection` | boolean | 否 | 0 | 检查到服务器的绑定连接。 |
| `client-id` | string | 否 | — | OpenID 客户端 ID |
| `client-key` | string | 否 | — | OpenID 客户端密钥 |
| `comment` | string | 否 | — | 描述。 |
| `default` | boolean | 否 | — | 将此认证域用作默认认证域 |
| `domain` | string | 否 | — | AD 域名 |
| `filter` | string | 否 | — | 用户同步的 LDAP 过滤器。 |
| `group_classes` | string | 否 | "groupOfNames, group, univentionGroup, ipausergroup" | 组的 objectclass。 |
| `group_dn` | string | 否 | — | 组同步的 LDAP 基础域名。如果未设置，将使用 base_dn。 |
| `group_filter` | string | 否 | — | 组同步的 LDAP 过滤器。 |
| `group_name_attr` | string | 否 | — | 表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。 |
| `groups-autocreate` | boolean | 否 | 0 | 如果组不存在，则自动创建。 |
| `groups-claim` | string | 否 | — | 用于获取组的 OpenID 声明。 |
| `groups-overwrite` | boolean | 否 | 0 | 用户登录时将覆盖其所有组。 |
| `issuer-url` | string | 否 | — | OpenID 颁发者 URL |
| `mode` | string | 否 | "ldap" | LDAP 协议模式。；可选值：`ldap`, `ldaps`, `ldap+starttls` |
| `password` | string | 否 | — | LDAP 绑定密码。将保存于 '/etc/pve/priv/realm/&lt;REALM&gt;.pw'。 |
| `port` | integer | 否 | — | 服务器端口。 |
| `prompt` | string | 否 | — | 指定授权服务器是否提示最终用户重新身份验证并表示同意。 |
| `query-userinfo` | boolean | 否 | 1 | 启用查询 userinfo 端点以获取声明值。 |
| `realm` | string | 是 | — | 认证域 ID |
| `scopes` | string | 否 | "email profile" | 指定应授权并返回的作用域（用户详细信息），例如 'email' 或 'profile'。 |
| `secure` | boolean | 否 | — | 使用安全的 LDAPS 协议。已弃用：请改用 'mode'。 |
| `server1` | string | 否 | — | 服务器 IP 地址（或 DNS 名称） |
| `server2` | string | 否 | — | 后备服务器 IP 地址（或 DNS 名称） |
| `sslversion` | string | 否 | — | LDAPS TLS/SSL 版本。不建议使用早于 1.2 的版本！；可选值：`tlsv1`, `tlsv1_1`, `tlsv1_2`, `tlsv1_3` |
| `sync-defaults-options` | string | 否 | — | 同步行为的默认选项。 |
| `sync_attributes` | string | 否 | — | 以逗号分隔的 key=value 对列表，指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 'mail' 映射到 PVE 的 'email'，请填写  'email=mail'。默认情况下，每个 PVE 用户字段均由  同名 LDAP 属性表示。 |
| `tfa` | string | 否 | — | 使用双因素身份验证。 |
| `type` | string | 是 | — | 认证域类型。；可选值：`ad`, `ldap`, `openid`, `pam`, `pve` |
| `user_attr` | string | 否 | — | LDAP 用户属性名称 |
| `user_classes` | string | 否 | "inetorgperson, posixaccount, person, user" | 用户的 objectclass。 |
| `username-claim` | string | 否 | — | 用于生成唯一用户名的 OpenID 声明。 |
| `verify` | boolean | 否 | 0 | 验证服务器的 SSL 证书 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "acr-values": {
      "description": "指定请求授权服务器在身份验证请求中使用的身份验证上下文类引用值。",
      "optional": 1,
      "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$",
      "type": "string"
    },
    "audiences": {
      "description": "除 'client-id' 外，也接受 OpenID 颁发者可能包含的受众列表。",
      "optional": 1,
      "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$",
      "type": "string"
    },
    "autocreate": {
      "default": 0,
      "description": "如果用户不存在，则自动创建。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "base_dn": {
      "description": "LDAP 基础域名",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bind_dn": {
      "description": "LDAP 绑定域名",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "capath": {
      "default": "/etc/ssl/certs",
      "description": "CA 证书存储路径",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "case-sensitive": {
      "default": 1,
      "description": "用户名区分大小写",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cert": {
      "description": "客户端证书路径",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "certkey": {
      "description": "客户端证书密钥路径",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "check-connection": {
      "default": 0,
      "description": "检查到服务器的绑定连接。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "client-id": {
      "description": "OpenID 客户端 ID",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "client-key": {
      "description": "OpenID 客户端密钥",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "description": "描述。",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "default": {
      "description": "将此认证域用作默认认证域",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "domain": {
      "description": "AD 域名",
      "maxLength": 256,
      "optional": 1,
      "pattern": "\\S+",
      "type": "string"
    },
    "filter": {
      "description": "用户同步的 LDAP 过滤器。",
      "maxLength": 2048,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_classes": {
      "default": "groupOfNames, group, univentionGroup, ipausergroup",
      "description": "组的 objectclass。",
      "format": "ldap-simple-attr-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_dn": {
      "description": "组同步的 LDAP 基础域名。如果未设置，将使用 base_dn。",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_filter": {
      "description": "组同步的 LDAP 过滤器。",
      "maxLength": 2048,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_name_attr": {
      "description": "表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。",
      "format": "ldap-simple-attr",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "groups-autocreate": {
      "default": 0,
      "description": "如果组不存在，则自动创建。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "groups-claim": {
      "description": "用于获取组的 OpenID 声明。",
      "maxLength": 256,
      "optional": 1,
      "pattern": "(?^:[A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "groups-overwrite": {
      "default": 0,
      "description": "用户登录时将覆盖其所有组。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "issuer-url": {
      "description": "OpenID 颁发者 URL",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mode": {
      "default": "ldap",
      "description": "LDAP 协议模式。",
      "enum": [
        "ldap",
        "ldaps",
        "ldap+starttls"
      ],
      "optional": 1,
      "type": "string"
    },
    "password": {
      "description": "LDAP 绑定密码。将保存于 '/etc/pve/priv/realm/<REALM>.pw'。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "服务器端口。",
      "maximum": 65535,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65535)"
    },
    "prompt": {
      "description": "指定授权服务器是否提示最终用户重新身份验证并表示同意。",
      "optional": 1,
      "pattern": "(?:none|login|consent|select_account|\\S+)",
      "type": "string"
    },
    "query-userinfo": {
      "default": 1,
      "description": "启用查询 userinfo 端点以获取声明值。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "realm": {
      "description": "认证域 ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    },
    "scopes": {
      "default": "email profile",
      "description": "指定应授权并返回的作用域（用户详细信息），例如 'email' 或 'profile'。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "secure": {
      "description": "使用安全的 LDAPS 协议。已弃用：请改用 'mode'。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "server1": {
      "description": "服务器 IP 地址（或 DNS 名称）",
      "format": "address",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "server2": {
      "description": "后备服务器 IP 地址（或 DNS 名称）",
      "format": "address",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "sslversion": {
      "description": "LDAPS TLS/SSL 版本。不建议使用早于 1.2 的版本！",
      "enum": [
        "tlsv1",
        "tlsv1_1",
        "tlsv1_2",
        "tlsv1_3"
      ],
      "optional": 1,
      "type": "string"
    },
    "sync-defaults-options": {
      "description": "同步行为的默认选项。",
      "format": "realm-sync-options",
      "optional": 1,
      "type": "string",
      "typetext": "[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]"
    },
    "sync_attributes": {
      "description": "以逗号分隔的 key=value 对列表，指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 'mail' 映射到 PVE 的 'email'，请填写  'email=mail'。默认情况下，每个 PVE 用户字段均由  同名 LDAP 属性表示。",
      "optional": 1,
      "pattern": "\\w+=[^,]+(,\\s*\\w+=[^,]+)*",
      "type": "string"
    },
    "tfa": {
      "description": "使用双因素身份验证。",
      "format": "pve-tfa-config",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]"
    },
    "type": {
      "description": "认证域类型。",
      "enum": [
        "ad",
        "ldap",
        "openid",
        "pam",
        "pve"
      ],
      "type": "string"
    },
    "user_attr": {
      "description": "LDAP 用户属性名称",
      "maxLength": 256,
      "optional": 1,
      "pattern": "\\S{2,}",
      "type": "string"
    },
    "user_classes": {
      "default": "inetorgperson, posixaccount, person, user",
      "description": "用户的 objectclass。",
      "format": "ldap-simple-attr-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "username-claim": {
      "description": "用于生成唯一用户名的 OpenID 声明。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "verify": {
      "default": 0,
      "description": "验证服务器的 SSL 证书",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains)。
