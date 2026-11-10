# `/cluster/metrics/server/{id}`

原始接口路径：`/cluster/metrics/server/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/metrics/server/{id}`

Remove Metric server.

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
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
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

## GET `/cluster/metrics/server/{id}`

Read metric server configuration.

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `id` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "id": {
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
  "type": "object"
}
```

## POST `/cluster/metrics/server/{id}`

Create a new external metric server config

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
| `api-path-prefix` | string | 否 | — | An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy. |
| `bucket` | string | 否 | — | The InfluxDB bucket/db. Only necessary when using the http v2 api. |
| `disable` | boolean | 否 | — | Flag to disable the plugin. |
| `id` | string | 是 | — | The ID of the entry. |
| `influxdbproto` | string | 否 | "udp" | ；可选值：`udp`, `http`, `https` |
| `max-body-size` | integer | 否 | 25000000 | InfluxDB max-body-size in bytes. Requests are batched up to this size. |
| `mtu` | integer | 否 | 1500 | MTU for metrics transmission over UDP |
| `organization` | string | 否 | — | The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api. |
| `otel-compression` | string | 否 | "gzip" | Compression algorithm for requests；可选值：`none`, `gzip` |
| `otel-headers` | string | 否 | — | Custom HTTP headers (JSON format, base64 encoded) |
| `otel-max-body-size` | integer | 否 | 10000000 | Maximum request body size in bytes |
| `otel-path` | string | 否 | "/v1/metrics" | OTLP endpoint path |
| `otel-protocol` | string | 否 | "https" | HTTP protocol；可选值：`http`, `https` |
| `otel-resource-attributes` | string | 否 | — | Additional resource attributes as JSON, base64 encoded |
| `otel-timeout` | integer | 否 | 5 | HTTP request timeout in seconds |
| `otel-verify-ssl` | boolean | 否 | 1 | Verify SSL certificates |
| `path` | string | 否 | — | root graphite path (ex: proxmox.mycluster.mykey) |
| `port` | integer | 是 | — | server network port |
| `proto` | string | 否 | — | Protocol to send graphite data. TCP or UDP (default)；可选值：`udp`, `tcp` |
| `server` | string | 是 | — | server dns name or IP address |
| `timeout` | integer | 否 | 1 | graphite TCP socket timeout (default=1) |
| `token` | string | 否 | — | The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead. |
| `type` | string | 是 | — | Plugin type.；可选值：`graphite`, `influxdb`, `opentelemetry` |
| `verify-certificate` | boolean | 否 | 1 | Set to 0 to disable certificate verification for https endpoints. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "api-path-prefix": {
      "description": "An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bucket": {
      "description": "The InfluxDB bucket/db. Only necessary when using the http v2 api.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "Flag to disable the plugin.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "The ID of the entry.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "influxdbproto": {
      "default": "udp",
      "enum": [
        "udp",
        "http",
        "https"
      ],
      "optional": 1,
      "type": "string"
    },
    "max-body-size": {
      "default": 25000000,
      "description": "InfluxDB max-body-size in bytes. Requests are batched up to this size.",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "mtu": {
      "default": 1500,
      "description": "MTU for metrics transmission over UDP",
      "maximum": 65536,
      "minimum": 512,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (512 - 65536)"
    },
    "organization": {
      "description": "The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-compression": {
      "default": "gzip",
      "description": "Compression algorithm for requests",
      "enum": [
        "none",
        "gzip"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-headers": {
      "description": "Custom HTTP headers (JSON format, base64 encoded)",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-max-body-size": {
      "default": 10000000,
      "description": "Maximum request body size in bytes",
      "minimum": 1024,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1024 - N)"
    },
    "otel-path": {
      "default": "/v1/metrics",
      "description": "OTLP endpoint path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-protocol": {
      "default": "https",
      "description": "HTTP protocol",
      "enum": [
        "http",
        "https"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-resource-attributes": {
      "description": "Additional resource attributes as JSON, base64 encoded",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-timeout": {
      "default": 5,
      "description": "HTTP request timeout in seconds",
      "maximum": 10,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 10)"
    },
    "otel-verify-ssl": {
      "default": 1,
      "description": "Verify SSL certificates",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "path": {
      "description": "root graphite path (ex: proxmox.mycluster.mykey)",
      "format": "graphite-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "server network port",
      "maximum": 65536,
      "minimum": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "proto": {
      "description": "Protocol to send graphite data. TCP or UDP (default)",
      "enum": [
        "udp",
        "tcp"
      ],
      "optional": 1,
      "type": "string"
    },
    "server": {
      "description": "server dns name or IP address",
      "format": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": 1,
      "description": "graphite TCP socket timeout (default=1)",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "token": {
      "description": "The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "Plugin type.",
      "enum": [
        "graphite",
        "influxdb",
        "opentelemetry"
      ],
      "format": "pve-configid",
      "type": "string"
    },
    "verify-certificate": {
      "default": 1,
      "description": "Set to 0 to disable certificate verification for https endpoints.",
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

## PUT `/cluster/metrics/server/{id}`

Update metric server configuration.

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
| `api-path-prefix` | string | 否 | — | An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy. |
| `bucket` | string | 否 | — | The InfluxDB bucket/db. Only necessary when using the http v2 api. |
| `delete` | string | 否 | — | A list of settings you want to delete. |
| `digest` | string | 否 | — | Prevent changes if current configuration file has a different digest. This can be used to prevent concurrent modifications. |
| `disable` | boolean | 否 | — | Flag to disable the plugin. |
| `id` | string | 是 | — | The ID of the entry. |
| `influxdbproto` | string | 否 | "udp" | ；可选值：`udp`, `http`, `https` |
| `max-body-size` | integer | 否 | 25000000 | InfluxDB max-body-size in bytes. Requests are batched up to this size. |
| `mtu` | integer | 否 | 1500 | MTU for metrics transmission over UDP |
| `organization` | string | 否 | — | The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api. |
| `otel-compression` | string | 否 | "gzip" | Compression algorithm for requests；可选值：`none`, `gzip` |
| `otel-headers` | string | 否 | — | Custom HTTP headers (JSON format, base64 encoded) |
| `otel-max-body-size` | integer | 否 | 10000000 | Maximum request body size in bytes |
| `otel-path` | string | 否 | "/v1/metrics" | OTLP endpoint path |
| `otel-protocol` | string | 否 | "https" | HTTP protocol；可选值：`http`, `https` |
| `otel-resource-attributes` | string | 否 | — | Additional resource attributes as JSON, base64 encoded |
| `otel-timeout` | integer | 否 | 5 | HTTP request timeout in seconds |
| `otel-verify-ssl` | boolean | 否 | 1 | Verify SSL certificates |
| `path` | string | 否 | — | root graphite path (ex: proxmox.mycluster.mykey) |
| `port` | integer | 是 | — | server network port |
| `proto` | string | 否 | — | Protocol to send graphite data. TCP or UDP (default)；可选值：`udp`, `tcp` |
| `server` | string | 是 | — | server dns name or IP address |
| `timeout` | integer | 否 | 1 | graphite TCP socket timeout (default=1) |
| `token` | string | 否 | — | The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead. |
| `verify-certificate` | boolean | 否 | 1 | Set to 0 to disable certificate verification for https endpoints. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "api-path-prefix": {
      "description": "An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bucket": {
      "description": "The InfluxDB bucket/db. Only necessary when using the http v2 api.",
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
      "description": "Flag to disable the plugin.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "The ID of the entry.",
      "format": "pve-configid",
      "type": "string",
      "typetext": "<string>"
    },
    "influxdbproto": {
      "default": "udp",
      "enum": [
        "udp",
        "http",
        "https"
      ],
      "optional": 1,
      "type": "string"
    },
    "max-body-size": {
      "default": 25000000,
      "description": "InfluxDB max-body-size in bytes. Requests are batched up to this size.",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "mtu": {
      "default": 1500,
      "description": "MTU for metrics transmission over UDP",
      "maximum": 65536,
      "minimum": 512,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (512 - 65536)"
    },
    "organization": {
      "description": "The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-compression": {
      "default": "gzip",
      "description": "Compression algorithm for requests",
      "enum": [
        "none",
        "gzip"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-headers": {
      "description": "Custom HTTP headers (JSON format, base64 encoded)",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-max-body-size": {
      "default": 10000000,
      "description": "Maximum request body size in bytes",
      "minimum": 1024,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1024 - N)"
    },
    "otel-path": {
      "default": "/v1/metrics",
      "description": "OTLP endpoint path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-protocol": {
      "default": "https",
      "description": "HTTP protocol",
      "enum": [
        "http",
        "https"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-resource-attributes": {
      "description": "Additional resource attributes as JSON, base64 encoded",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-timeout": {
      "default": 5,
      "description": "HTTP request timeout in seconds",
      "maximum": 10,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 10)"
    },
    "otel-verify-ssl": {
      "default": 1,
      "description": "Verify SSL certificates",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "path": {
      "description": "root graphite path (ex: proxmox.mycluster.mykey)",
      "format": "graphite-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "server network port",
      "maximum": 65536,
      "minimum": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "proto": {
      "description": "Protocol to send graphite data. TCP or UDP (default)",
      "enum": [
        "udp",
        "tcp"
      ],
      "optional": 1,
      "type": "string"
    },
    "server": {
      "description": "server dns name or IP address",
      "format": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": 1,
      "description": "graphite TCP socket timeout (default=1)",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "token": {
      "description": "The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead.",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "verify-certificate": {
      "default": 1,
      "description": "Set to 0 to disable certificate verification for https endpoints.",
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/metrics/server/{id})。
