# `/cluster/metrics/server/{id}`

原始接口路径：`/cluster/metrics/server/{id}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/cluster/metrics/server/{id}`

移除指标服务器。

**方法标识：** `delete`

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

读取指标服务器配置。

**方法标识：** `read`

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

创建新的外部指标服务器配置

**方法标识：** `create`

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
| `api-path-prefix` | string | 否 | — | 插入在 '&lt;host&gt;:&lt;port&gt;/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。 |
| `bucket` | string | 否 | — | InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。 |
| `disable` | boolean | 否 | — | 用于禁用插件的标志。 |
| `id` | string | 是 | — | 条目的 ID。 |
| `influxdbproto` | string | 否 | "udp" | ；可选值：`udp`, `http`, `https` |
| `max-body-size` | integer | 否 | 25000000 | InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。 |
| `mtu` | integer | 否 | 1500 | 通过 UDP 传输指标的 MTU |
| `organization` | string | 否 | — | InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。 |
| `otel-compression` | string | 否 | "gzip" | 请求的压缩算法；可选值：`none`, `gzip` |
| `otel-headers` | string | 否 | — | 自定义 HTTP 标头（JSON 格式，base64 编码） |
| `otel-max-body-size` | integer | 否 | 10000000 | 最大请求正文大小，单位为字节 |
| `otel-path` | string | 否 | "/v1/metrics" | OTLP 端点路径 |
| `otel-protocol` | string | 否 | "https" | HTTP 协议；可选值：`http`, `https` |
| `otel-resource-attributes` | string | 否 | — | JSON 形式的额外资源属性，采用 base64 编码 |
| `otel-timeout` | integer | 否 | 5 | HTTP 请求超时时间，单位为秒 |
| `otel-verify-ssl` | boolean | 否 | 1 | 验证 SSL 证书 |
| `path` | string | 否 | — | graphite 根路径（例如：proxmox.mycluster.mykey） |
| `port` | integer | 是 | — | 服务器网络端口 |
| `proto` | string | 否 | — | 发送 graphite 数据的协议。TCP 或 UDP（默认）；可选值：`udp`, `tcp` |
| `server` | string | 是 | — | 服务器 DNS 名称或 IP 地址 |
| `timeout` | integer | 否 | 1 | graphite TCP 套接字超时时间（默认值=1） |
| `token` | string | 否 | — | InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。 |
| `type` | string | 是 | — | 插件类型。；可选值：`graphite`, `influxdb`, `opentelemetry` |
| `verify-certificate` | boolean | 否 | 1 | 设置为 0 可禁用 https 端点的证书验证。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "api-path-prefix": {
      "description": "插入在 '<host>:<port>/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bucket": {
      "description": "InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "用于禁用插件的标志。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "条目的 ID。",
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
      "description": "InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "mtu": {
      "default": 1500,
      "description": "通过 UDP 传输指标的 MTU",
      "maximum": 65536,
      "minimum": 512,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (512 - 65536)"
    },
    "organization": {
      "description": "InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-compression": {
      "default": "gzip",
      "description": "请求的压缩算法",
      "enum": [
        "none",
        "gzip"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-headers": {
      "description": "自定义 HTTP 标头（JSON 格式，base64 编码）",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-max-body-size": {
      "default": 10000000,
      "description": "最大请求正文大小，单位为字节",
      "minimum": 1024,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1024 - N)"
    },
    "otel-path": {
      "default": "/v1/metrics",
      "description": "OTLP 端点路径",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-protocol": {
      "default": "https",
      "description": "HTTP 协议",
      "enum": [
        "http",
        "https"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-resource-attributes": {
      "description": "JSON 形式的额外资源属性，采用 base64 编码",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-timeout": {
      "default": 5,
      "description": "HTTP 请求超时时间，单位为秒",
      "maximum": 10,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 10)"
    },
    "otel-verify-ssl": {
      "default": 1,
      "description": "验证 SSL 证书",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "path": {
      "description": "graphite 根路径（例如：proxmox.mycluster.mykey）",
      "format": "graphite-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "服务器网络端口",
      "maximum": 65536,
      "minimum": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "proto": {
      "description": "发送 graphite 数据的协议。TCP 或 UDP（默认）",
      "enum": [
        "udp",
        "tcp"
      ],
      "optional": 1,
      "type": "string"
    },
    "server": {
      "description": "服务器 DNS 名称或 IP 地址",
      "format": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": 1,
      "description": "graphite TCP 套接字超时时间（默认值=1）",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "token": {
      "description": "InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "type": {
      "description": "插件类型。",
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
      "description": "设置为 0 可禁用 https 端点的证书验证。",
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

更新指标服务器配置。

**方法标识：** `update`

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
| `api-path-prefix` | string | 否 | — | 插入在 '&lt;host&gt;:&lt;port&gt;/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。 |
| `bucket` | string | 否 | — | InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `digest` | string | 否 | — | 如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。 |
| `disable` | boolean | 否 | — | 用于禁用插件的标志。 |
| `id` | string | 是 | — | 条目的 ID。 |
| `influxdbproto` | string | 否 | "udp" | ；可选值：`udp`, `http`, `https` |
| `max-body-size` | integer | 否 | 25000000 | InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。 |
| `mtu` | integer | 否 | 1500 | 通过 UDP 传输指标的 MTU |
| `organization` | string | 否 | — | InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。 |
| `otel-compression` | string | 否 | "gzip" | 请求的压缩算法；可选值：`none`, `gzip` |
| `otel-headers` | string | 否 | — | 自定义 HTTP 标头（JSON 格式，base64 编码） |
| `otel-max-body-size` | integer | 否 | 10000000 | 最大请求正文大小，单位为字节 |
| `otel-path` | string | 否 | "/v1/metrics" | OTLP 端点路径 |
| `otel-protocol` | string | 否 | "https" | HTTP 协议；可选值：`http`, `https` |
| `otel-resource-attributes` | string | 否 | — | JSON 形式的额外资源属性，采用 base64 编码 |
| `otel-timeout` | integer | 否 | 5 | HTTP 请求超时时间，单位为秒 |
| `otel-verify-ssl` | boolean | 否 | 1 | 验证 SSL 证书 |
| `path` | string | 否 | — | graphite 根路径（例如：proxmox.mycluster.mykey） |
| `port` | integer | 是 | — | 服务器网络端口 |
| `proto` | string | 否 | — | 发送 graphite 数据的协议。TCP 或 UDP（默认）；可选值：`udp`, `tcp` |
| `server` | string | 是 | — | 服务器 DNS 名称或 IP 地址 |
| `timeout` | integer | 否 | 1 | graphite TCP 套接字超时时间（默认值=1） |
| `token` | string | 否 | — | InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。 |
| `verify-certificate` | boolean | 否 | 1 | 设置为 0 可禁用 https 端点的证书验证。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "api-path-prefix": {
      "description": "插入在 '<host>:<port>/' 和 '/api2/' 之间的 API 路径前缀。如果 InfluxDB 服务运行在反向代理之后，此选项可能很有用。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "bucket": {
      "description": "InfluxDB 存储桶/数据库。仅在使用 http v2 api 时需要。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "maxLength": 4096,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "digest": {
      "description": "如果当前配置文件具有不同的摘要，则阻止更改。这可用于防止并发修改。",
      "maxLength": 64,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disable": {
      "description": "用于禁用插件的标志。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "id": {
      "description": "条目的 ID。",
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
      "description": "InfluxDB max-body-size，单位为字节。请求按批次合并，最大达到此大小。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "mtu": {
      "default": 1500,
      "description": "通过 UDP 传输指标的 MTU",
      "maximum": 65536,
      "minimum": 512,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (512 - 65536)"
    },
    "organization": {
      "description": "InfluxDB 组织。仅在使用 http v2 api 时需要。使用 v2 兼容 api 时无意义。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-compression": {
      "default": "gzip",
      "description": "请求的压缩算法",
      "enum": [
        "none",
        "gzip"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-headers": {
      "description": "自定义 HTTP 标头（JSON 格式，base64 编码）",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-max-body-size": {
      "default": 10000000,
      "description": "最大请求正文大小，单位为字节",
      "minimum": 1024,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1024 - N)"
    },
    "otel-path": {
      "default": "/v1/metrics",
      "description": "OTLP 端点路径",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-protocol": {
      "default": "https",
      "description": "HTTP 协议",
      "enum": [
        "http",
        "https"
      ],
      "optional": 1,
      "type": "string"
    },
    "otel-resource-attributes": {
      "description": "JSON 形式的额外资源属性，采用 base64 编码",
      "maxLength": 1024,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "otel-timeout": {
      "default": 5,
      "description": "HTTP 请求超时时间，单位为秒",
      "maximum": 10,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 10)"
    },
    "otel-verify-ssl": {
      "default": 1,
      "description": "验证 SSL 证书",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "path": {
      "description": "graphite 根路径（例如：proxmox.mycluster.mykey）",
      "format": "graphite-path",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "port": {
      "description": "服务器网络端口",
      "maximum": 65536,
      "minimum": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 65536)"
    },
    "proto": {
      "description": "发送 graphite 数据的协议。TCP 或 UDP（默认）",
      "enum": [
        "udp",
        "tcp"
      ],
      "optional": 1,
      "type": "string"
    },
    "server": {
      "description": "服务器 DNS 名称或 IP 地址",
      "format": "address",
      "type": "string",
      "typetext": "<string>"
    },
    "timeout": {
      "default": 1,
      "description": "graphite TCP 套接字超时时间（默认值=1）",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "token": {
      "description": "InfluxDB 访问令牌。仅在使用 http v2 api 时需要。如果使用 v2 兼容 api，则改用 'user:password'。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "verify-certificate": {
      "default": 1,
      "description": "设置为 0 可禁用 https 端点的证书验证。",
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
