# `/cluster/options`

原始接口路径：`/cluster/options`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/cluster/options`

获取数据中心选项。如果对 '/' 没有 'Sys.Audit' 权限，则不会返回所有选项。

**方法标识：** `get_options`

**权限**

```json
{
  "check": [
    "perm",
    "/",
    [
      "Sys.Audit"
    ]
  ],
  "user": "all"
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
  "properties": {
    "allowed-tags": {
      "description": "当前用户可设置和查看的标签。",
      "items": {
        "description": "标签。",
        "type": "string"
      },
      "type": "array"
    },
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {
          "description": "克隆磁盘的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "default": {
          "description": "默认带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "migration": {
          "description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "move": {
          "description": "移动磁盘的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "restore": {
          "description": "从备份还原客户机的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "consent-text": {
      "description": "登录前显示的同意文本。",
      "maxLength": 65536,
      "optional": 1,
      "type": "string"
    },
    "console": {
      "description": "选择默认控制台查看器。可以使用内置 java applet（VNC；已弃用，会映射到 html5）、与外部 virt-viewer 兼容的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如虚拟机未启用 SPICE），则回退到 noVNC。",
      "enum": [
        "applet",
        "vv",
        "html5",
        "xtermjs"
      ],
      "optional": 1,
      "type": "string"
    },
    "crs": {
      "description": "集群资源调度设置。",
      "format": {
        "ha": {
          "default": "basic",
          "description": "为 HA 使用此资源调度器模式。",
          "enum": [
            "basic",
            "static",
            "dynamic"
          ],
          "optional": 1,
          "type": "string",
          "verbose_description": "配置 HA 管理器应如何选择节点以启动或恢复服务：\n\n- 'basic'：仅使用服务数量，\n- 'static'：考虑服务的静态 CPU 和内存配置，\n- 'dynamic'：考虑服务的静态和动态 CPU 及内存用量。\n"
        },
        "ha-auto-rebalance": {
          "default": 0,
          "description": "是否根据当前节点不均衡程度使用 CRS 自动均衡 HA 资源。",
          "optional": 1,
          "type": "boolean"
        },
        "ha-auto-rebalance-hold-duration": {
          "default": 3,
          "description": "集群节点不均衡程度必须连续超过阈值的 HA 轮次数，达到后触发自动资源均衡迁移。",
          "minimum": 0,
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "number"
        },
        "ha-auto-rebalance-margin": {
          "default": 10,
          "description": "执行资源均衡迁移所需的集群节点不均衡程度最小相对改善百分比。",
          "maximum": 100,
          "minimum": 0,
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "number"
        },
        "ha-auto-rebalance-method": {
          "default": "bruteforce",
          "description": "对均衡迁移进行评分所用的方法。",
          "enum": [
            "bruteforce",
            "topsis"
          ],
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "string"
        },
        "ha-auto-rebalance-threshold": {
          "default": 30,
          "description": "集群节点不均衡百分比，超过此值将触发自动资源均衡系统。",
          "maximum": 100,
          "minimum": 0,
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "number"
        },
        "ha-rebalance-on-start": {
          "default": 0,
          "description": "设置为在 HA 服务请求状态从 stop 变为 start 时使用 CRS 选择合适节点。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "description": {
      "description": "数据中心描述。显示在 Web 界面的数据中心备注面板中。作为注释保存在配置文件中。",
      "maxLength": 65536,
      "optional": 1,
      "type": "string"
    },
    "email_from": {
      "description": "指定发送通知所用的电子邮件发件地址（默认为 root@$hostname）",
      "format": "email-opt",
      "optional": 1,
      "type": "string"
    },
    "fencing": {
      "default": "watchdog",
      "description": "设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中正确配置隔离设备。both 模式同时使用这两种模式。\n\n警告：'hardware' 和 'both' 均为实验性功能，仍在开发中",
      "enum": [
        "watchdog",
        "hardware",
        "both"
      ],
      "optional": 1,
      "type": "string"
    },
    "ha": {
      "description": "集群范围的 HA 设置。",
      "format": {
        "shutdown_policy": {
          "default": "conditional",
          "description": "节点关闭时 HA 服务的策略。'freeze' 禁用自动恢复，'failover' 确保恢复，'conditional' 在关机时恢复、重启时冻结。'migrate' 在可能时将正在运行的服务迁移到其他节点。使用 'freeze' 或 'failover' 时，关闭节点始终会先停止 HA 服务。",
          "enum": [
            "freeze",
            "failover",
            "conditional",
            "migrate"
          ],
          "type": "string",
          "verbose_description": "描述节点关机或重启时处理 HA 服务的策略。Freeze 总是冻结关闭时仍在该节点上的服务，这些服务不会由 HA 管理器恢复。Failover 不会将服务标记为冻结，因此如果关闭的节点未迅速恢复上线（< 1min），服务将恢复到其他节点。'conditional' 根据关闭类型自动选择，即重启时冻结服务，关机时保留服务状态，从而在约 2 分钟后恢复。Migrate 在触发重启或关机时尝试将所有正在运行的服务移至其他节点。只有当节点上不再存在运行中的服务时，关机过程才会继续。如果节点重新上线，服务将移回先前关闭的节点，前提是期间没有发生其他迁移、重新安置或恢复。"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "http_proxy": {
      "description": "指定用于下载的外部 HTTP 代理（例如：'http://username:password@host:port/')",
      "optional": 1,
      "pattern": "http://.*",
      "type": "string"
    },
    "keyboard": {
      "description": "VNC 服务器的默认键盘布局。",
      "enum": [
        "de",
        "de-ch",
        "da",
        "en-gb",
        "en-us",
        "es",
        "fi",
        "fr",
        "fr-be",
        "fr-ca",
        "fr-ch",
        "hu",
        "is",
        "it",
        "ja",
        "lt",
        "mk",
        "nl",
        "no",
        "pl",
        "pt",
        "pt-br",
        "sv",
        "sl",
        "tr"
      ],
      "optional": 1,
      "type": "string"
    },
    "language": {
      "description": "默认 GUI 语言。",
      "enum": [
        "ar",
        "ca",
        "da",
        "de",
        "en",
        "es",
        "eu",
        "fa",
        "fr",
        "hr",
        "he",
        "it",
        "ja",
        "ka",
        "kr",
        "nb",
        "nl",
        "nn",
        "pl",
        "pt_BR",
        "ru",
        "sl",
        "sv",
        "tr",
        "ukr",
        "zh_CN",
        "zh_TW"
      ],
      "optional": 1,
      "type": "string"
    },
    "location": {
      "description": "集群位置。",
      "format": "pve-node-location",
      "optional": 1,
      "type": "string"
    },
    "mac_prefix": {
      "default": "BC:24:11",
      "description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 'BC:24:11' 是 IEEE 分配给 Proxmox Server Solutions GmbH 的 OUI，对应 24 位大型 MAC 地址块。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT 后方）。",
      "format": "mac-prefix",
      "optional": 1,
      "type": "string",
      "verbose_description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），对应大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT/地址伪装后方）。\n \n请注意，当运行多个客户机网络部分或全部共享的集群时，强烈建议扩展默认 MAC 前缀，或生成自定义的有效前缀，以减少 MAC 冲突概率。例如，为每个集群在 Proxmox OUI 后添加不同的额外十六进制位，如第一个集群使用 `BC:24:11:0`，第二个使用 `BC:24:11:1`，依此类推。\n 也可以在逻辑上分隔客户机网络，例如使用 VLAN。\n\n对于可公开访问的客户机，建议向 IEEE 注册自己的 https://standards.ieee.org/products-programs/regauth/[OUI]，或与您自身或托管服务提供商的网络管理员协调。"
    },
    "max_workers": {
      "description": "定义执行 'stopall VMs' 等操作或 HA 管理器任务时，每个节点最多启动的工作任务数  。",
      "minimum": 1,
      "optional": 1,
      "type": "integer"
    },
    "migration": {
      "description": "用于集群范围的迁移设置。",
      "format": {
        "network": {
          "description": "用于迁移的（子）网络的 CIDR。如果未设置复制网络设置，则复制任务将以此作为后备值",
          "format": "CIDR",
          "format_description": "CIDR",
          "optional": 1,
          "type": "string"
        },
        "type": {
          "default": "secure",
          "default_key": 1,
          "description": "迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": [
            "secure",
            "insecure"
          ],
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "migration_unsecure": {
      "description": "默认使用 SSH 隧道保障迁移安全。在安全的私有网络上，可禁用此功能以加快迁移。已弃用，请改用 'migration' 属性！",
      "optional": 1,
      "type": "boolean"
    },
    "next-id": {
      "description": "控制空闲 VMID 自动选择池的范围。",
      "format": {
        "lower": {
          "default": 100,
          "description": "空闲 next-id API 范围的下限，包含此值。",
          "max": 999999999,
          "min": 100,
          "optional": 1,
          "type": "integer"
        },
        "upper": {
          "default": 1000000,
          "description": "空闲 next-id API 范围的上限，不包含此值。",
          "max": 1000000000,
          "min": 100,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "notify": {
      "description": "集群范围的通知设置。",
      "format": {
        "fencing": {
          "description": "未使用——请改用数据中心通知设置。",
          "enum": [
            "always",
            "never"
          ],
          "optional": 1,
          "type": "string"
        },
        "package-updates": {
          "default": "auto",
          "description": "已弃用：请改用数据中心通知设置。控制每日更新作业何时发送通知。",
          "enum": [
            "auto",
            "always",
            "never"
          ],
          "optional": 1,
          "type": "string",
          "verbose_description": "已弃用：请改用数据中心通知设置。\n控制每日更新作业发送通知的频率：\n* 'auto' 对具有有效订阅的系统每天发送，因为假定这些系统已  用于生产环境，因此应了解待处理更新。\n* 'always' 如果有新的待处理更新，则每次更新都发送。\n* 'never' 从不发送新待处理更新的通知。\n"
        },
        "replication": {
          "description": "未使用——请改用数据中心通知设置。",
          "enum": [
            "always",
            "never"
          ],
          "optional": 1,
          "type": "string"
        },
        "target-fencing": {
          "description": "未使用——请改用数据中心通知设置。",
          "format_description": "TARGET",
          "optional": 1,
          "type": "string"
        },
        "target-package-updates": {
          "description": "未使用——请改用数据中心通知设置。",
          "format_description": "TARGET",
          "optional": 1,
          "type": "string"
        },
        "target-replication": {
          "description": "未使用——请改用数据中心通知设置。",
          "format_description": "TARGET",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "registered-tags": {
      "description": "设置和删除时需要对 '/' 具有 `Sys.Modify` 权限的标签列表。此处设置且同时位于 'user-tag-access' 中的标签也需要 `Sys.Modify`。",
      "optional": 1,
      "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*);)*(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)",
      "type": "string",
      "typetext": "<tag>[;<tag>...]"
    },
    "replication": {
      "description": "用于集群范围的复制设置。",
      "format": {
        "network": {
          "description": "用于复制任务的（子）网络的 CIDR。",
          "format": "CIDR",
          "format_description": "CIDR",
          "optional": 1,
          "type": "string"
        },
        "type": {
          "default": "secure",
          "default_key": 1,
          "description": "复制流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": [
            "secure",
            "insecure"
          ],
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "tag-style": {
      "description": "标签样式选项。",
      "format": {
        "case-sensitive": {
          "default": 0,
          "description": "控制更新时筛选唯一标签是否区分大小写。",
          "optional": 1,
          "type": "boolean"
        },
        "color-map": {
          "description": "手动标签颜色映射（以分号分隔）。",
          "optional": 1,
          "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?)(?:;(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?))*",
          "type": "string",
          "typetext": "<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]"
        },
        "ordering": {
          "default": "alphabetical",
          "description": "控制 Web 界面和 API 更新中的标签排序。",
          "enum": [
            "config",
            "alphabetical"
          ],
          "optional": 1,
          "type": "string"
        },
        "shape": {
          "default": "circle",
          "description": "Web UI 树中的标签形状。'full' 绘制完整标签。'circle' 仅绘制带背景色的圆形。'dense' 仅绘制小矩形（适用于每个客户机分配了大量标签的情况）。'none' 禁止显示标签。",
          "enum": [
            "full",
            "circle",
            "dense",
            "none"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "u2f": {
      "description": "u2f",
      "format": {
        "appid": {
          "description": "覆盖 U2F AppId URL。默认为源站。",
          "format_description": "APPID",
          "optional": 1,
          "type": "string"
        },
        "origin": {
          "description": "覆盖 U2F Origin。主要适用于只有一个 URL 的单节点。",
          "format_description": "URL",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "user-tag-access": {
      "description": "用户可设置标签的权限选项",
      "format": {
        "user-allow": {
          "default": "free",
          "description": "控制没有 `Sys.Modify` 权限（作用于 `/`）的用户的标签使用方式，允许 `none`、`list`、已 `existing` 或任意标签（`free`）。",
          "enum": [
            "none",
            "list",
            "existing",
            "free"
          ],
          "optional": 1,
          "type": "string",
          "verbose_description": "控制用户可在其控制的资源（例如客户机）上设置或删除哪些标签。具有 `Sys.Modify` 权限（作用于 `/`）的用户始终不受限制。\n* 'none' 不可使用任何标签。\n* 'list' 可使用 'user-allow-list' 中的标签。\n* 'existing' 与 list 相同，但也可使用资源上已有的标签。\n* 'free' 无标签限制。\n"
        },
        "user-allow-list": {
          "description": "当 'user-allow' 为 'list' 和 'existing' 时，用户允许设置和删除的标签列表（以分号分隔）。",
          "optional": 1,
          "pattern": "(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)(?:;(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*))*",
          "type": "string",
          "typetext": "<tag>[;<tag>...]"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "webauthn": {
      "description": "webauthn 配置",
      "format": {
        "allow-subdomains": {
          "default": 1,
          "description": "是否允许源站为子域，而不必是完全相同的 URL。",
          "optional": 1,
          "type": "boolean"
        },
        "id": {
          "description": "依赖方 ID。必须为不含协议、端口或路径的域名。更改此项必定导致现有凭据失效。",
          "format_description": "DOMAINNAME",
          "optional": 1,
          "type": "string"
        },
        "origin": {
          "description": "站点源站。必须为 `https://` URL（或 `http://localhost`）。应包含用户在浏览器中访问 Web 界面时输入的地址。更改此项可能导致现有凭据失效。",
          "format_description": "URL",
          "optional": 1,
          "type": "string"
        },
        "rp": {
          "description": "依赖方名称。任意文本标识符。更改此项可能导致现有凭据失效。",
          "format_description": "RELYING_PARTY",
          "optional": 1,
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

## PUT `/cluster/options`

设置数据中心选项。

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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `bwlimit` | string | 否 | — | 为各类操作设置 I/O 带宽限制（单位为 KiB/s）。 |
| `consent-text` | string | 否 | — | 登录前显示的同意文本。 |
| `console` | string | 否 | — | 选择默认控制台查看器。可以使用内置 java applet（VNC；已弃用，会映射到 html5）、与外部 virt-viewer 兼容的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如虚拟机未启用 SPICE），则回退到 noVNC。；可选值：`applet`, `vv`, `html5`, `xtermjs` |
| `crs` | string | 否 | — | 集群资源调度设置。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `description` | string | 否 | — | 数据中心描述。显示在 Web 界面的数据中心备注面板中。作为注释保存在配置文件中。 |
| `email_from` | string | 否 | — | 指定发送通知所用的电子邮件发件地址（默认为 root@$hostname） |
| `fencing` | string | 否 | "watchdog" | 设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中正确配置隔离设备。both 模式同时使用这两种模式。<br><br>警告：'hardware' 和 'both' 均为实验性功能，仍在开发中；可选值：`watchdog`, `hardware`, `both` |
| `ha` | string | 否 | — | 集群范围的 HA 设置。 |
| `http_proxy` | string | 否 | — | 指定用于下载的外部 HTTP 代理（例如：'http://username:password@host:port/') |
| `keyboard` | string | 否 | — | VNC 服务器的默认键盘布局。；可选值：`de`, `de-ch`, `da`, `en-gb`, `en-us`, `es`, `fi`, `fr`, `fr-be`, `fr-ca`, `fr-ch`, `hu`, `is`, `it`, `ja`, `lt`, `mk`, `nl`, `no`, `pl`, `pt`, `pt-br`, `sv`, `sl`, `tr` |
| `language` | string | 否 | — | 默认 GUI 语言。；可选值：`ar`, `ca`, `da`, `de`, `en`, `es`, `eu`, `fa`, `fr`, `hr`, `he`, `it`, `ja`, `ka`, `kr`, `nb`, `nl`, `nn`, `pl`, `pt_BR`, `ru`, `sl`, `sv`, `tr`, `ukr`, `zh_CN`, `zh_TW` |
| `location` | string | 否 | — | 集群位置。 |
| `mac_prefix` | string | 否 | "BC:24:11" | 虚拟客户机自动生成的 MAC 地址前缀。默认值 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），对应大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT/地址伪装后方）。<br> <br>请注意，当运行多个客户机网络部分或全部共享的集群时，强烈建议扩展默认 MAC 前缀，或生成自定义的有效前缀，以减少 MAC 冲突概率。例如，为每个集群在 Proxmox OUI 后添加不同的额外十六进制位，如第一个集群使用 `BC:24:11:0`，第二个使用 `BC:24:11:1`，依此类推。<br> 也可以在逻辑上分隔客户机网络，例如使用 VLAN。<br><br>对于可公开访问的客户机，建议向 IEEE 注册自己的 https://standards.ieee.org/products-programs/regauth/[OUI]，或与您自身或托管服务提供商的网络管理员协调。 |
| `max_workers` | integer | 否 | — | 定义执行 'stopall VMs' 等操作或 HA 管理器任务时，每个节点最多启动的工作任务数  。 |
| `migration` | string | 否 | — | 用于集群范围的迁移设置。 |
| `migration_unsecure` | boolean | 否 | — | 默认使用 SSH 隧道保障迁移安全。在安全的私有网络上，可禁用此功能以加快迁移。已弃用，请改用 'migration' 属性！ |
| `next-id` | string | 否 | — | 控制空闲 VMID 自动选择池的范围。 |
| `notify` | string | 否 | — | 集群范围的通知设置。 |
| `registered-tags` | string | 否 | — | 设置和删除时需要对 '/' 具有 `Sys.Modify` 权限的标签列表。此处设置且同时位于 'user-tag-access' 中的标签也需要 `Sys.Modify`。 |
| `replication` | string | 否 | — | 用于集群范围的复制设置。 |
| `tag-style` | string | 否 | — | 标签样式选项。 |
| `u2f` | string | 否 | — | u2f |
| `user-tag-access` | string | 否 | — | 用户可设置标签的权限选项 |
| `webauthn` | string | 否 | — | webauthn 配置 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "bwlimit": {
      "description": "为各类操作设置 I/O 带宽限制（单位为 KiB/s）。",
      "format": {
        "clone": {
          "description": "克隆磁盘的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "default": {
          "description": "默认带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "migration": {
          "description": "迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "move": {
          "description": "移动磁盘的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        },
        "restore": {
          "description": "从备份还原客户机的带宽限制，单位为 KiB/s",
          "format_description": "LIMIT",
          "minimum": "0",
          "optional": 1,
          "type": "number"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]"
    },
    "consent-text": {
      "description": "登录前显示的同意文本。",
      "maxLength": 65536,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "console": {
      "description": "选择默认控制台查看器。可以使用内置 java applet（VNC；已弃用，会映射到 html5）、与外部 virt-viewer 兼容的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如虚拟机未启用 SPICE），则回退到 noVNC。",
      "enum": [
        "applet",
        "vv",
        "html5",
        "xtermjs"
      ],
      "optional": 1,
      "type": "string"
    },
    "crs": {
      "description": "集群资源调度设置。",
      "format": {
        "ha": {
          "default": "basic",
          "description": "为 HA 使用此资源调度器模式。",
          "enum": [
            "basic",
            "static",
            "dynamic"
          ],
          "optional": 1,
          "type": "string",
          "verbose_description": "配置 HA 管理器应如何选择节点以启动或恢复服务：\n\n- 'basic'：仅使用服务数量，\n- 'static'：考虑服务的静态 CPU 和内存配置，\n- 'dynamic'：考虑服务的静态和动态 CPU 及内存用量。\n"
        },
        "ha-auto-rebalance": {
          "default": 0,
          "description": "是否根据当前节点不均衡程度使用 CRS 自动均衡 HA 资源。",
          "optional": 1,
          "type": "boolean"
        },
        "ha-auto-rebalance-hold-duration": {
          "default": 3,
          "description": "集群节点不均衡程度必须连续超过阈值的 HA 轮次数，达到后触发自动资源均衡迁移。",
          "minimum": 0,
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "number"
        },
        "ha-auto-rebalance-margin": {
          "default": 10,
          "description": "执行资源均衡迁移所需的集群节点不均衡程度最小相对改善百分比。",
          "maximum": 100,
          "minimum": 0,
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "number"
        },
        "ha-auto-rebalance-method": {
          "default": "bruteforce",
          "description": "对均衡迁移进行评分所用的方法。",
          "enum": [
            "bruteforce",
            "topsis"
          ],
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "string"
        },
        "ha-auto-rebalance-threshold": {
          "default": 30,
          "description": "集群节点不均衡百分比，超过此值将触发自动资源均衡系统。",
          "maximum": 100,
          "minimum": 0,
          "optional": 1,
          "requires": "ha-auto-rebalance",
          "type": "number"
        },
        "ha-rebalance-on-start": {
          "default": 0,
          "description": "设置为在 HA 服务请求状态从 stop 变为 start 时使用 CRS 选择合适节点。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[ha=<basic|static|dynamic>] [,ha-auto-rebalance=<1|0>] [,ha-auto-rebalance-hold-duration=<number>] [,ha-auto-rebalance-margin=<number>] [,ha-auto-rebalance-method=<bruteforce|topsis>] [,ha-auto-rebalance-threshold=<number>] [,ha-rebalance-on-start=<1|0>]"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "数据中心描述。显示在 Web 界面的数据中心备注面板中。作为注释保存在配置文件中。",
      "maxLength": 65536,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "email_from": {
      "description": "指定发送通知所用的电子邮件发件地址（默认为 root@$hostname）",
      "format": "email-opt",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "fencing": {
      "default": "watchdog",
      "description": "设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中正确配置隔离设备。both 模式同时使用这两种模式。\n\n警告：'hardware' 和 'both' 均为实验性功能，仍在开发中",
      "enum": [
        "watchdog",
        "hardware",
        "both"
      ],
      "optional": 1,
      "type": "string"
    },
    "ha": {
      "description": "集群范围的 HA 设置。",
      "format": {
        "shutdown_policy": {
          "default": "conditional",
          "description": "节点关闭时 HA 服务的策略。'freeze' 禁用自动恢复，'failover' 确保恢复，'conditional' 在关机时恢复、重启时冻结。'migrate' 在可能时将正在运行的服务迁移到其他节点。使用 'freeze' 或 'failover' 时，关闭节点始终会先停止 HA 服务。",
          "enum": [
            "freeze",
            "failover",
            "conditional",
            "migrate"
          ],
          "type": "string",
          "verbose_description": "描述节点关机或重启时处理 HA 服务的策略。Freeze 总是冻结关闭时仍在该节点上的服务，这些服务不会由 HA 管理器恢复。Failover 不会将服务标记为冻结，因此如果关闭的节点未迅速恢复上线（< 1min），服务将恢复到其他节点。'conditional' 根据关闭类型自动选择，即重启时冻结服务，关机时保留服务状态，从而在约 2 分钟后恢复。Migrate 在触发重启或关机时尝试将所有正在运行的服务移至其他节点。只有当节点上不再存在运行中的服务时，关机过程才会继续。如果节点重新上线，服务将移回先前关闭的节点，前提是期间没有发生其他迁移、重新安置或恢复。"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "shutdown_policy=<enum>"
    },
    "http_proxy": {
      "description": "指定用于下载的外部 HTTP 代理（例如：'http://username:password@host:port/')",
      "optional": 1,
      "pattern": "http://.*",
      "type": "string"
    },
    "keyboard": {
      "description": "VNC 服务器的默认键盘布局。",
      "enum": [
        "de",
        "de-ch",
        "da",
        "en-gb",
        "en-us",
        "es",
        "fi",
        "fr",
        "fr-be",
        "fr-ca",
        "fr-ch",
        "hu",
        "is",
        "it",
        "ja",
        "lt",
        "mk",
        "nl",
        "no",
        "pl",
        "pt",
        "pt-br",
        "sv",
        "sl",
        "tr"
      ],
      "optional": 1,
      "type": "string"
    },
    "language": {
      "description": "默认 GUI 语言。",
      "enum": [
        "ar",
        "ca",
        "da",
        "de",
        "en",
        "es",
        "eu",
        "fa",
        "fr",
        "hr",
        "he",
        "it",
        "ja",
        "ka",
        "kr",
        "nb",
        "nl",
        "nn",
        "pl",
        "pt_BR",
        "ru",
        "sl",
        "sv",
        "tr",
        "ukr",
        "zh_CN",
        "zh_TW"
      ],
      "optional": 1,
      "type": "string"
    },
    "location": {
      "description": "集群位置。",
      "format": "pve-node-location",
      "optional": 1,
      "type": "string",
      "typetext": "latitude=<number> ,longitude=<number> [,name=<name>]"
    },
    "mac_prefix": {
      "default": "BC:24:11",
      "description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 'BC:24:11' 是 IEEE 分配给 Proxmox Server Solutions GmbH 的 OUI，对应 24 位大型 MAC 地址块。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT 后方）。",
      "format": "mac-prefix",
      "optional": 1,
      "type": "string",
      "typetext": "<string>",
      "verbose_description": "虚拟客户机自动生成的 MAC 地址前缀。默认值 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），对应大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 内或 NAT/地址伪装后方）。\n \n请注意，当运行多个客户机网络部分或全部共享的集群时，强烈建议扩展默认 MAC 前缀，或生成自定义的有效前缀，以减少 MAC 冲突概率。例如，为每个集群在 Proxmox OUI 后添加不同的额外十六进制位，如第一个集群使用 `BC:24:11:0`，第二个使用 `BC:24:11:1`，依此类推。\n 也可以在逻辑上分隔客户机网络，例如使用 VLAN。\n\n对于可公开访问的客户机，建议向 IEEE 注册自己的 https://standards.ieee.org/products-programs/regauth/[OUI]，或与您自身或托管服务提供商的网络管理员协调。"
    },
    "max_workers": {
      "description": "定义执行 'stopall VMs' 等操作或 HA 管理器任务时，每个节点最多启动的工作任务数  。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "migration": {
      "description": "用于集群范围的迁移设置。",
      "format": {
        "network": {
          "description": "用于迁移的（子）网络的 CIDR。如果未设置复制网络设置，则复制任务将以此作为后备值",
          "format": "CIDR",
          "format_description": "CIDR",
          "optional": 1,
          "type": "string"
        },
        "type": {
          "default": "secure",
          "default_key": 1,
          "description": "迁移流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": [
            "secure",
            "insecure"
          ],
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[type=]<secure|insecure> [,network=<CIDR>]"
    },
    "migration_unsecure": {
      "description": "默认使用 SSH 隧道保障迁移安全。在安全的私有网络上，可禁用此功能以加快迁移。已弃用，请改用 'migration' 属性！",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "next-id": {
      "description": "控制空闲 VMID 自动选择池的范围。",
      "format": {
        "lower": {
          "default": 100,
          "description": "空闲 next-id API 范围的下限，包含此值。",
          "max": 999999999,
          "min": 100,
          "optional": 1,
          "type": "integer"
        },
        "upper": {
          "default": 1000000,
          "description": "空闲 next-id API 范围的上限，不包含此值。",
          "max": 1000000000,
          "min": 100,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[lower=<integer>] [,upper=<integer>]"
    },
    "notify": {
      "description": "集群范围的通知设置。",
      "format": {
        "fencing": {
          "description": "未使用——请改用数据中心通知设置。",
          "enum": [
            "always",
            "never"
          ],
          "optional": 1,
          "type": "string"
        },
        "package-updates": {
          "default": "auto",
          "description": "已弃用：请改用数据中心通知设置。控制每日更新作业何时发送通知。",
          "enum": [
            "auto",
            "always",
            "never"
          ],
          "optional": 1,
          "type": "string",
          "verbose_description": "已弃用：请改用数据中心通知设置。\n控制每日更新作业发送通知的频率：\n* 'auto' 对具有有效订阅的系统每天发送，因为假定这些系统已  用于生产环境，因此应了解待处理更新。\n* 'always' 如果有新的待处理更新，则每次更新都发送。\n* 'never' 从不发送新待处理更新的通知。\n"
        },
        "replication": {
          "description": "未使用——请改用数据中心通知设置。",
          "enum": [
            "always",
            "never"
          ],
          "optional": 1,
          "type": "string"
        },
        "target-fencing": {
          "description": "未使用——请改用数据中心通知设置。",
          "format_description": "TARGET",
          "optional": 1,
          "type": "string"
        },
        "target-package-updates": {
          "description": "未使用——请改用数据中心通知设置。",
          "format_description": "TARGET",
          "optional": 1,
          "type": "string"
        },
        "target-replication": {
          "description": "未使用——请改用数据中心通知设置。",
          "format_description": "TARGET",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[fencing=<always|never>] [,package-updates=<auto|always|never>] [,replication=<always|never>] [,target-fencing=<TARGET>] [,target-package-updates=<TARGET>] [,target-replication=<TARGET>]"
    },
    "registered-tags": {
      "description": "设置和删除时需要对 '/' 具有 `Sys.Modify` 权限的标签列表。此处设置且同时位于 'user-tag-access' 中的标签也需要 `Sys.Modify`。",
      "optional": 1,
      "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*);)*(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)",
      "type": "string",
      "typetext": "<tag>[;<tag>...]"
    },
    "replication": {
      "description": "用于集群范围的复制设置。",
      "format": {
        "network": {
          "description": "用于复制任务的（子）网络的 CIDR。",
          "format": "CIDR",
          "format_description": "CIDR",
          "optional": 1,
          "type": "string"
        },
        "type": {
          "default": "secure",
          "default_key": 1,
          "description": "复制流量默认通过 SSH 隧道加密。在安全且完全私有的网络上，可禁用此功能以提高性能。",
          "enum": [
            "secure",
            "insecure"
          ],
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[type=]<secure|insecure> [,network=<CIDR>]"
    },
    "tag-style": {
      "description": "标签样式选项。",
      "format": {
        "case-sensitive": {
          "default": 0,
          "description": "控制更新时筛选唯一标签是否区分大小写。",
          "optional": 1,
          "type": "boolean"
        },
        "color-map": {
          "description": "手动标签颜色映射（以分号分隔）。",
          "optional": 1,
          "pattern": "(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?)(?:;(?:(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*):[0-9a-fA-F]{6}(?::[0-9a-fA-F]{6})?))*",
          "type": "string",
          "typetext": "<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]"
        },
        "ordering": {
          "default": "alphabetical",
          "description": "控制 Web 界面和 API 更新中的标签排序。",
          "enum": [
            "config",
            "alphabetical"
          ],
          "optional": 1,
          "type": "string"
        },
        "shape": {
          "default": "circle",
          "description": "Web UI 树中的标签形状。'full' 绘制完整标签。'circle' 仅绘制带背景色的圆形。'dense' 仅绘制小矩形（适用于每个客户机分配了大量标签的情况）。'none' 禁止显示标签。",
          "enum": [
            "full",
            "circle",
            "dense",
            "none"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[case-sensitive=<1|0>] [,color-map=<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]] [,ordering=<config|alphabetical>] [,shape=<enum>]"
    },
    "u2f": {
      "description": "u2f",
      "format": {
        "appid": {
          "description": "覆盖 U2F AppId URL。默认为源站。",
          "format_description": "APPID",
          "optional": 1,
          "type": "string"
        },
        "origin": {
          "description": "覆盖 U2F Origin。主要适用于只有一个 URL 的单节点。",
          "format_description": "URL",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[appid=<APPID>] [,origin=<URL>]"
    },
    "user-tag-access": {
      "description": "用户可设置标签的权限选项",
      "format": {
        "user-allow": {
          "default": "free",
          "description": "控制没有 `Sys.Modify` 权限（作用于 `/`）的用户的标签使用方式，允许 `none`、`list`、已 `existing` 或任意标签（`free`）。",
          "enum": [
            "none",
            "list",
            "existing",
            "free"
          ],
          "optional": 1,
          "type": "string",
          "verbose_description": "控制用户可在其控制的资源（例如客户机）上设置或删除哪些标签。具有 `Sys.Modify` 权限（作用于 `/`）的用户始终不受限制。\n* 'none' 不可使用任何标签。\n* 'list' 可使用 'user-allow-list' 中的标签。\n* 'existing' 与 list 相同，但也可使用资源上已有的标签。\n* 'free' 无标签限制。\n"
        },
        "user-allow-list": {
          "description": "当 'user-allow' 为 'list' 和 'existing' 时，用户允许设置和删除的标签列表（以分号分隔）。",
          "optional": 1,
          "pattern": "(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*)(?:;(?^i:[a-z0-9_][a-z0-9_\\-\\+\\.]*))*",
          "type": "string",
          "typetext": "<tag>[;<tag>...]"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[user-allow=<enum>] [,user-allow-list=<tag>[;<tag>...]]"
    },
    "webauthn": {
      "description": "webauthn 配置",
      "format": {
        "allow-subdomains": {
          "default": 1,
          "description": "是否允许源站为子域，而不必是完全相同的 URL。",
          "optional": 1,
          "type": "boolean"
        },
        "id": {
          "description": "依赖方 ID。必须为不含协议、端口或路径的域名。更改此项必定导致现有凭据失效。",
          "format_description": "DOMAINNAME",
          "optional": 1,
          "type": "string"
        },
        "origin": {
          "description": "站点源站。必须为 `https://` URL（或 `http://localhost`）。应包含用户在浏览器中访问 Web 界面时输入的地址。更改此项可能导致现有凭据失效。",
          "format_description": "URL",
          "optional": 1,
          "type": "string"
        },
        "rp": {
          "description": "依赖方名称。任意文本标识符。更改此项可能导致现有凭据失效。",
          "format_description": "RELYING_PARTY",
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[allow-subdomains=<1|0>] [,id=<DOMAINNAME>] [,origin=<URL>] [,rp=<RELYING_PARTY>]"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/cluster/options)。
