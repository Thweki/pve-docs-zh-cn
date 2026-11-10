# `/access/domains/{realm}`

原始接口路径：`/access/domains/{realm}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/domains/{realm}`

Delete an authentication server.

**方法标识：** `delete`

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
| `realm` | string | 是 | — | Authentication domain ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "realm": {
      "description": "Authentication domain ID",
      "format": "pve-realm",
      "maxLength": 32,
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

## GET `/access/domains/{realm}`

Get auth server configuration.

**方法标识：** `read`

**权限**

```json
{
  "check": [
    "perm",
    "/access/realm",
    [
      "Realm.Allocate",
      "Sys.Audit"
    ],
    "any",
    1
  ]
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `realm` | string | 是 | — | Authentication domain ID |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "realm": {
      "description": "Authentication domain ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{}
```

## PUT `/access/domains/{realm}`

Update authentication server settings.

**方法标识：** `update`

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
| `acr-values` | string | 否 | — | Specifies the Authentication Context Class Reference values that theAuthorization Server is being requested to use for the Auth Request. |
| `audiences` | string | 否 | — | A list of audiences that the OpenID Issuer may include that are accepted in addition to 'client-id'. |
| `autocreate` | boolean | 否 | 0 | Automatically create users if they do not exist. |
| `base_dn` | string | 否 | — | LDAP base domain name |
| `bind_dn` | string | 否 | — | LDAP bind domain name |
| `capath` | string | 否 | "/etc/ssl/certs" | Path to the CA certificate store |
| `case-sensitive` | boolean | 否 | 1 | username is case-sensitive |
| `cert` | string | 否 | — | Path to the client certificate |
| `certkey` | string | 否 | — | Path to the client certificate key |
| `check-connection` | boolean | 否 | 0 | Check bind connection to the server. |
| `client-id` | string | 否 | — | OpenID Client ID |
| `client-key` | string | 否 | — | OpenID Client Key |
| `comment` | string | 否 | — | Description. |
| `default` | boolean | 否 | — | Use this as default realm |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `domain` | string | 否 | — | AD domain name |
| `filter` | string | 否 | — | LDAP filter for user sync. |
| `group_classes` | string | 否 | "groupOfNames, group, univentionGroup, ipausergroup" | The objectclasses for groups. |
| `group_dn` | string | 否 | — | LDAP base domain name for group sync. If not set, the base_dn will be used. |
| `group_filter` | string | 否 | — | LDAP filter for group sync. |
| `group_name_attr` | string | 否 | — | LDAP attribute representing a groups name. If not set or found, the first value of the DN will be used as name. |
| `groups-autocreate` | boolean | 否 | 0 | Automatically create groups if they do not exist. |
| `groups-claim` | string | 否 | — | OpenID claim used to retrieve groups with. |
| `groups-overwrite` | boolean | 否 | 0 | All groups will be overwritten for the user on login. |
| `issuer-url` | string | 否 | — | OpenID Issuer Url |
| `mode` | string | 否 | "ldap" | LDAP protocol mode.；可选值：`ldap`, `ldaps`, `ldap+starttls` |
| `password` | string | 否 | — | LDAP bind password. Will be stored in '/etc/pve/priv/realm/&lt;REALM&gt;.pw'. |
| `port` | integer | 否 | — | Server port. |
| `prompt` | string | 否 | — | Specifies whether the Authorization Server prompts the End-User for reauthentication and consent. |
| `query-userinfo` | boolean | 否 | 1 | Enables querying the userinfo endpoint for claims values. |
| `realm` | string | 是 | — | Authentication domain ID |
| `scopes` | string | 否 | "email profile" | Specifies the scopes (user details) that should be authorized and returned, for example 'email' or 'profile'. |
| `secure` | boolean | 否 | — | Use secure LDAPS protocol. DEPRECATED: use 'mode' instead. |
| `server1` | string | 否 | — | Server IP address (or DNS name) |
| `server2` | string | 否 | — | Fallback Server IP address (or DNS name) |
| `sslversion` | string | 否 | — | LDAPS TLS/SSL version. It's not recommended to use version older than 1.2!；可选值：`tlsv1`, `tlsv1_1`, `tlsv1_2`, `tlsv1_3` |
| `sync-defaults-options` | string | 否 | — | The default options for behavior of synchronizations. |
| `sync_attributes` | string | 否 | — | Comma separated list of key=value pairs for specifying which LDAP attributes map to which PVE user field. For example, to map the LDAP attribute 'mail' to PVEs 'email', write  'email=mail'. By default, each PVE user field is represented  by an LDAP attribute of the same name. |
| `tfa` | string | 否 | — | Use Two-factor authentication. |
| `user_attr` | string | 否 | — | LDAP user attribute name |
| `user_classes` | string | 否 | "inetorgperson, posixaccount, person, user" | The objectclasses for users. |
| `verify` | boolean | 否 | 0 | Verify the server's SSL certificate |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "acr-values": {
      "description": "Specifies the Authentication Context Class Reference values that theAuthorization Server is being requested to use for the Auth Request.",
      "optional": 1,
      "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$",
      "type": "string"
    },
    "audiences": {
      "description": "A list of audiences that the OpenID Issuer may include that are accepted in addition to 'client-id'.",
      "optional": 1,
      "pattern": "^[^\\x00-\\x1F\\x7F <>#\"]*$",
      "type": "string"
    },
    "autocreate": {
      "default": 0,
      "description": "Automatically create users if they do not exist.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "base_dn": {
      "description": "LDAP base domain name",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bind_dn": {
      "description": "LDAP bind domain name",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "capath": {
      "default": "/etc/ssl/certs",
      "description": "Path to the CA certificate store",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "case-sensitive": {
      "default": 1,
      "description": "username is case-sensitive",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cert": {
      "description": "Path to the client certificate",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "certkey": {
      "description": "Path to the client certificate key",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "check-connection": {
      "default": 0,
      "description": "Check bind connection to the server.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "client-id": {
      "description": "OpenID Client ID",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "client-key": {
      "description": "OpenID Client Key",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "comment": {
      "description": "Description.",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "default": {
      "description": "Use this as default realm",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
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
    "domain": {
      "description": "AD domain name",
      "maxLength": 256,
      "optional": 1,
      "pattern": "\\S+",
      "type": "string"
    },
    "filter": {
      "description": "LDAP filter for user sync.",
      "maxLength": 2048,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_classes": {
      "default": "groupOfNames, group, univentionGroup, ipausergroup",
      "description": "The objectclasses for groups.",
      "format": "ldap-simple-attr-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_dn": {
      "description": "LDAP base domain name for group sync. If not set, the base_dn will be used.",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_filter": {
      "description": "LDAP filter for group sync.",
      "maxLength": 2048,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "group_name_attr": {
      "description": "LDAP attribute representing a groups name. If not set or found, the first value of the DN will be used as name.",
      "format": "ldap-simple-attr",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "groups-autocreate": {
      "default": 0,
      "description": "Automatically create groups if they do not exist.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "groups-claim": {
      "description": "OpenID claim used to retrieve groups with.",
      "maxLength": 256,
      "optional": 1,
      "pattern": "(?^:[A-Za-z0-9\\.\\-_]+)",
      "type": "string"
    },
    "groups-overwrite": {
      "default": 0,
      "description": "All groups will be overwritten for the user on login.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "issuer-url": {
      "description": "OpenID Issuer Url",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "mode": {
      "default": "ldap",
      "description": "LDAP protocol mode.",
      "enum": [
        "ldap",
        "ldaps",
        "ldap+starttls"
      ],
      "optional": 1,
      "type": "string"
    },
    "password": {
      "description": "LDAP bind password. Will be stored in '/etc/pve/priv/realm/<REALM>.pw'.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "Server port.",
      "maximum": 65535,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65535)"
    },
    "prompt": {
      "description": "Specifies whether the Authorization Server prompts the End-User for reauthentication and consent.",
      "optional": 1,
      "pattern": "(?:none|login|consent|select_account|\\S+)",
      "type": "string"
    },
    "query-userinfo": {
      "default": 1,
      "description": "Enables querying the userinfo endpoint for claims values.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "realm": {
      "description": "Authentication domain ID",
      "format": "pve-realm",
      "maxLength": 32,
      "type": "string",
      "typetext": "<string>"
    },
    "scopes": {
      "default": "email profile",
      "description": "Specifies the scopes (user details) that should be authorized and returned, for example 'email' or 'profile'.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "secure": {
      "description": "Use secure LDAPS protocol. DEPRECATED: use 'mode' instead.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "server1": {
      "description": "Server IP address (or DNS name)",
      "format": "address",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "server2": {
      "description": "Fallback Server IP address (or DNS name)",
      "format": "address",
      "maxLength": 256,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "sslversion": {
      "description": "LDAPS TLS/SSL version. It's not recommended to use version older than 1.2!",
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
      "description": "The default options for behavior of synchronizations.",
      "format": "realm-sync-options",
      "optional": 1,
      "type": "string",
      "typetext": "[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]"
    },
    "sync_attributes": {
      "description": "Comma separated list of key=value pairs for specifying which LDAP attributes map to which PVE user field. For example, to map the LDAP attribute 'mail' to PVEs 'email', write  'email=mail'. By default, each PVE user field is represented  by an LDAP attribute of the same name.",
      "optional": 1,
      "pattern": "\\w+=[^,]+(,\\s*\\w+=[^,]+)*",
      "type": "string"
    },
    "tfa": {
      "description": "Use Two-factor authentication.",
      "format": "pve-tfa-config",
      "maxLength": 128,
      "optional": 1,
      "type": "string",
      "typetext": "type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]"
    },
    "user_attr": {
      "description": "LDAP user attribute name",
      "maxLength": 256,
      "optional": 1,
      "pattern": "\\S{2,}",
      "type": "string"
    },
    "user_classes": {
      "default": "inetorgperson, posixaccount, person, user",
      "description": "The objectclasses for users.",
      "format": "ldap-simple-attr-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "verify": {
      "default": 0,
      "description": "Verify the server's SSL certificate",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/domains/{realm})。
