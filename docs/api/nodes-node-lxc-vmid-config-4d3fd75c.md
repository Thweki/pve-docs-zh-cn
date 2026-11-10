# `/nodes/{node}/lxc/{vmid}/config`

原始接口路径：`/nodes/{node}/lxc/{vmid}/config`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc/{vmid}/config`

获取容器配置。

**方法标识：** `vm_config`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Audit"
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
| `current` | boolean | 否 | 0 | 获取当前值（而非待应用值）。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `snapshot` | string | 否 | — | 从给定快照获取配置值。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "current": {
      "default": 0,
      "description": "获取当前值（而非待应用值）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "snapshot": {
      "description": "从给定快照获取配置值。",
      "format": "pve-configid",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "properties": {
    "arch": {
      "default": "amd64",
      "description": "操作系统架构类型。",
      "enum": [
        "amd64",
        "i386",
        "arm64",
        "armhf",
        "riscv32",
        "riscv64"
      ],
      "optional": 1,
      "type": "string"
    },
    "cmode": {
      "default": "tty",
      "description": "控制台模式。默认情况下，console 命令尝试连接到一个可用的 tty 设备。将 cmode 设为 'console' 时，会改为尝试连接到 /dev/console。如果将 cmode 设为 'shell'，则直接在容器内调用 shell（无需登录）。",
      "enum": [
        "shell",
        "console",
        "tty"
      ],
      "optional": 1,
      "type": "string"
    },
    "console": {
      "default": 1,
      "description": "将控制台设备（/dev/console）连接到容器。",
      "optional": 1,
      "type": "boolean"
    },
    "cores": {
      "description": "分配给容器的核心数。默认情况下，容器可使用所有可用核心。",
      "maximum": 8192,
      "minimum": 1,
      "optional": 1,
      "type": "integer"
    },
    "cpulimit": {
      "default": 0,
      "description": "CPU 使用量限制。\n\n注意：如果计算机有 2 个 CPU，则 CPU 时间总量为 '2'。值 '0' 表示不限制 CPU。",
      "maximum": 8192,
      "minimum": 0,
      "optional": 1,
      "type": "number"
    },
    "cpuunits": {
      "default": "cgroup v1: 1024, cgroup v2: 100",
      "description": "容器的 CPU 权重，在 cgroup v2 中会限制到 [1, 10000] 范围内。",
      "maximum": 500000,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "verbose_description": "容器的 CPU 权重。内核公平调度器使用此参数。数值越大，此容器获得的 CPU 时间越多。该数值相对于其他所有运行中客户机的权重而言。"
    },
    "debug": {
      "default": 0,
      "description": "尝试输出更详细的信息。目前仅在启动时启用 debug 日志级别。",
      "optional": 1,
      "type": "boolean"
    },
    "description": {
      "description": "容器描述。显示在 Web 界面的容器摘要中。作为注释保存在配置文件中。",
      "maxLength": 8192,
      "optional": 1,
      "type": "string"
    },
    "dev[n]": {
      "description": "要直通到容器的设备",
      "format": {
        "deny-write": {
          "default": 0,
          "description": "禁止容器写入设备",
          "optional": 1,
          "type": "boolean"
        },
        "gid": {
          "description": "要分配给设备节点的组 ID",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "mode": {
          "description": "要为设备节点设置的访问模式",
          "format_description": "Octal access mode",
          "optional": 1,
          "pattern": "0[0-7]{3}",
          "type": "string"
        },
        "path": {
          "default_key": 1,
          "description": "要直通到容器的设备",
          "format": "pve-lxc-dev-string",
          "format_description": "Path",
          "optional": 1,
          "type": "string",
          "verbose_description": "要直通到容器的设备路径"
        },
        "uid": {
          "description": "要分配给设备节点的用户 ID",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "digest": {
      "description": "配置文件的 SHA1 摘要。可用于防止并发修改。",
      "type": "string"
    },
    "entrypoint": {
      "default": "/sbin/init",
      "description": "用作 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制程序开头。",
      "optional": 1,
      "pattern": "(?^:[^\\x00-\\x08\\x0a-\\x1F\\x7F]+)",
      "type": "string"
    },
    "env": {
      "description": "容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。",
      "optional": 1,
      "pattern": "(?^:(?:\\w+=[^\\x00-\\x08\\x0a-\\x1F\\x7F]*)(?:\\0\\w+=[^\\x00-\\x08\\x0a-\\x1F\\x7F]*)*)",
      "type": "string"
    },
    "features": {
      "description": "允许容器访问高级功能。",
      "format": {
        "force_rw_sys": {
          "default": 0,
          "description": "在非特权容器中将 /sys 挂载为 `rw`，而非 `mixed`。在使用较新版本（>= v245）的 systemd-network 时，这可能破坏网络功能。",
          "optional": 1,
          "type": "boolean"
        },
        "fuse": {
          "default": 0,
          "description": "允许在容器内使用 'fuse' 文件系统。注意，fuse 与 freezer cgroup 之间的交互可能导致 I/O 死锁。",
          "optional": 1,
          "type": "boolean"
        },
        "keyctl": {
          "default": 0,
          "description": "仅适用于非特权容器：允许使用 keyctl() 系统调用。在容器内使用 docker 需要此功能。默认情况下，非特权容器会认为此系统调用不存在。这主要是针对 systemd-networkd 的变通措施，因为当内核因权限不足而拒绝某些 keyctl() 操作时，它会将其视为致命错误。实质上，您可以在运行 systemd-networkd 和 docker 之间作出选择。",
          "optional": 1,
          "type": "boolean"
        },
        "mknod": {
          "default": 0,
          "description": "允许非特权容器使用 mknod() 添加特定设备节点。这需要内核支持将 seccomp 陷阱交由用户空间处理（5.3 或更新版本）。此功能为实验性。",
          "optional": 1,
          "type": "boolean"
        },
        "mount": {
          "description": "允许挂载特定类型的文件系统。此处应为 mount 命令所用的文件系统类型列表。注意，这可能对容器安全性产生负面影响。可以访问 loop 设备时，挂载文件能够绕过 devices cgroup 的 mknod 权限；挂载 NFS 文件系统可能完全阻塞宿主机 I/O 并使其无法重启等。",
          "format_description": "fstype;fstype;...",
          "optional": 1,
          "pattern": "(?^:[a-zA-Z0-9_; ]+)",
          "type": "string"
        },
        "nesting": {
          "default": 0,
          "description": "允许嵌套。最好与具有附加 ID 映射的非特权容器一起使用。注意，这会向客户机暴露宿主机的 procfs 和 sysfs 内容。systemd 隔离服务也需要此功能。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "hookscript": {
      "description": "在容器生命周期各个阶段执行的脚本。",
      "format": "pve-volume-id",
      "optional": 1,
      "type": "string"
    },
    "hostname": {
      "description": "为容器设置主机名。",
      "format": "dns-name",
      "maxLength": 255,
      "optional": 1,
      "type": "string"
    },
    "lock": {
      "description": "锁定/解锁容器。",
      "enum": [
        "backup",
        "create",
        "destroyed",
        "disk",
        "fstrim",
        "migrate",
        "mounted",
        "rollback",
        "snapshot",
        "snapshot-delete"
      ],
      "optional": 1,
      "type": "string"
    },
    "lxc": {
      "description": "LXC 底层配置数组（[[key1, value1], [key2, value2] ...]）。",
      "items": {
        "items": {
          "type": "string"
        },
        "type": "array"
      },
      "optional": 1,
      "type": "array"
    },
    "memory": {
      "default": 512,
      "description": "容器的 RAM 容量，单位为 MB。",
      "minimum": 16,
      "optional": 1,
      "type": "integer"
    },
    "mp[n]": {
      "description": "将卷用作容器挂载点。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。",
      "format": {
        "acl": {
          "description": "显式启用或禁用 ACL 支持。",
          "optional": 1,
          "type": "boolean"
        },
        "backup": {
          "description": "是否在备份中包含挂载点。",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "是否在备份中包含挂载点（仅适用于卷挂载点）。"
        },
        "idmap": {
          "description": "将特定容器 UID/GID 映射到此挂载点底层磁盘的 UID/GID",
          "format_description": "type:container:disk:range-size[;type:container:disk:range-size;...]",
          "optional": 1,
          "pattern": "(?^:^(?:passthrough|[ug]:[0-9]+:[0-9]+:[1-9][0-9]*(?:;[ug]:[0-9]+:[0-9]+:[1-9][0-9]*)*)$)",
          "type": "string",
          "verbose_description": "自定义 UID/GID 映射，覆盖此挂载点的容器 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。\n\n`type` 对 UID 为 `u`，对 GID 为 `g`。\n\n`container` 是容器内看到的第一个 ID。\n\n`disk` 是底层文件系统上相应的第一个 ID。\n\n`range-size` 是要映射的连续 ID 数量。\n\n未映射的 ID 回退到容器的 `lxc.idmap`。\n\n示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上属于 UID 456 的文件，在容器内显示为属于 UID 123。\n\n示例 2：`g:100:50:5` 映射 5 个连续 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。\n\n示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，即容器内的 ID 与磁盘上的 ID 相同。"
        },
        "keepattrs": {
          "default": 0,
          "description": "从挂载点目录继承所有权和权限。",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "如果挂载点目录已存在，则继承其 UID、GID 和访问模式。"
        },
        "mountoptions": {
          "description": "rootfs/mps 的额外挂载选项。",
          "format_description": "opt[;opt...]",
          "optional": 1,
          "pattern": "(?^:(?^:(discard|lazytime|noatime|nodev|noexec|nosuid))(;(?^:(discard|lazytime|noatime|nodev|noexec|nosuid)))*)",
          "type": "string"
        },
        "mp": {
          "description": "从容器内部看到的挂载点路径（不得包含符号链接）。",
          "format": "pve-lxc-mp-string",
          "format_description": "Path",
          "type": "string",
          "verbose_description": "从容器内部看到的挂载点路径。\n\n注意：出于安全原因，不得包含任何符号链接。"
        },
        "quota": {
          "description": "在容器内启用用户配额（不支持 ZFS 子卷）",
          "optional": 1,
          "type": "boolean"
        },
        "replicate": {
          "default": 1,
          "description": "将此卷包含在存储复制作业中。",
          "optional": 1,
          "type": "boolean"
        },
        "ro": {
          "description": "只读挂载点",
          "optional": 1,
          "type": "boolean"
        },
        "shared": {
          "default": 0,
          "description": "将此非卷挂载点标记为在多个节点上可用（参见 'nodes'）",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此非卷挂载点标记为在所有节点上可用。\n\n警告：此选项不会自动共享挂载点，而是假定它已共享！"
        },
        "size": {
          "description": "卷大小（只读值）。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "default_key": 1,
          "description": "要挂载到容器内的卷、设备或目录。",
          "format": "pve-lxc-mp-string",
          "format_description": "volume",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "nameserver": {
      "description": "设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。",
      "format": "lxc-ip-with-ll-iface-list",
      "optional": 1,
      "type": "string"
    },
    "net[n]": {
      "description": "指定容器的网络接口。",
      "format": {
        "bridge": {
          "description": "网络设备要连接的网桥。",
          "format_description": "bridge",
          "optional": 1,
          "pattern": "[-_.\\w\\d]+",
          "type": "string"
        },
        "firewall": {
          "description": "控制是否使用此接口的防火墙规则。",
          "optional": 1,
          "type": "boolean"
        },
        "gw": {
          "description": "IPv4 流量的默认网关。",
          "format": "ipv4",
          "format_description": "GatewayIPv4",
          "optional": 1,
          "type": "string"
        },
        "gw6": {
          "description": "IPv6 流量的默认网关。",
          "format": "ipv6",
          "format_description": "GatewayIPv6",
          "optional": 1,
          "type": "string"
        },
        "host-managed": {
          "description": "此接口的 IP 配置是否由宿主机管理。启用时，由宿主机而非容器负责此接口的 IP 配置。容器不应在此接口上运行自己的 DHCP 客户端或网络管理器。适用于缺少内部网络管理栈的容器，例如许多应用容器。",
          "optional": 1,
          "type": "boolean"
        },
        "hwaddr": {
          "description": "接口 MAC 地址。默认动态分配，但可按需静态设置，例如始终使用同一链路本地 IPv6 地址。（lxc.network.hwaddr）",
          "format": "mac-addr",
          "format_description": "XX:XX:XX:XX:XX:XX",
          "optional": 1,
          "type": "string",
          "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
        },
        "ip": {
          "description": "CIDR 格式的 IPv4 地址。",
          "format": "pve-ipv4-config",
          "format_description": "(IPv4/CIDR|dhcp|manual)",
          "optional": 1,
          "type": "string"
        },
        "ip6": {
          "description": "CIDR 格式的 IPv6 地址。",
          "format": "pve-ipv6-config",
          "format_description": "(IPv6/CIDR|auto|dhcp|manual)",
          "optional": 1,
          "type": "string"
        },
        "link_down": {
          "description": "是否断开此接口的连接（如同拔掉网线）。",
          "optional": 1,
          "type": "boolean"
        },
        "mtu": {
          "description": "接口的最大传输单元。（lxc.network.mtu）",
          "maximum": 65535,
          "minimum": 64,
          "optional": 1,
          "type": "integer"
        },
        "name": {
          "description": "从容器内部看到的网络设备名称。（lxc.network.name）",
          "format_description": "string",
          "pattern": "[-_.\\w\\d]+",
          "type": "string"
        },
        "rate": {
          "description": "对接口应用速率限制",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "tag": {
          "description": "此接口的 VLAN 标签。",
          "maximum": 4094,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "trunks": {
          "description": "通过此接口的 VLAN ID",
          "format_description": "vlanid[;vlanid...]",
          "optional": 1,
          "pattern": "(?^:\\d+(?:;\\d+)*)",
          "type": "string"
        },
        "type": {
          "description": "网络接口类型。",
          "enum": [
            "veth"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "onboot": {
      "default": 0,
      "description": "指定容器是否在系统启动时启动。",
      "optional": 1,
      "type": "boolean"
    },
    "ostype": {
      "description": "操作系统类型。用于在容器内设置配置，对应 /usr/share/lxc/config/<ostype>.common.conf 中的 LXC 设置脚本。值 'unmanaged' 可用于跳过所有操作系统特定设置。",
      "enum": [
        "debian",
        "devuan",
        "ubuntu",
        "centos",
        "fedora",
        "opensuse",
        "archlinux",
        "alpine",
        "gentoo",
        "nixos",
        "unmanaged"
      ],
      "optional": 1,
      "type": "string"
    },
    "protection": {
      "default": 0,
      "description": "设置容器的保护标志。此项将阻止容器或容器磁盘的移除/更新操作。",
      "optional": 1,
      "type": "boolean"
    },
    "rootfs": {
      "description": "将卷用作容器根目录。",
      "format": {
        "acl": {
          "description": "显式启用或禁用 ACL 支持。",
          "optional": 1,
          "type": "boolean"
        },
        "idmap": {
          "description": "将特定容器 UID/GID 映射到此挂载点底层磁盘的 UID/GID",
          "format_description": "type:container:disk:range-size[;type:container:disk:range-size;...]",
          "optional": 1,
          "pattern": "(?^:^(?:passthrough|[ug]:[0-9]+:[0-9]+:[1-9][0-9]*(?:;[ug]:[0-9]+:[0-9]+:[1-9][0-9]*)*)$)",
          "type": "string",
          "verbose_description": "自定义 UID/GID 映射，覆盖此挂载点的容器 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。\n\n`type` 对 UID 为 `u`，对 GID 为 `g`。\n\n`container` 是容器内看到的第一个 ID。\n\n`disk` 是底层文件系统上相应的第一个 ID。\n\n`range-size` 是要映射的连续 ID 数量。\n\n未映射的 ID 回退到容器的 `lxc.idmap`。\n\n示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上属于 UID 456 的文件，在容器内显示为属于 UID 123。\n\n示例 2：`g:100:50:5` 映射 5 个连续 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。\n\n示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，即容器内的 ID 与磁盘上的 ID 相同。"
        },
        "mountoptions": {
          "description": "rootfs/mps 的额外挂载选项。",
          "format_description": "opt[;opt...]",
          "optional": 1,
          "pattern": "(?^:(?^:(discard|lazytime|noatime|nodev|noexec|nosuid))(;(?^:(discard|lazytime|noatime|nodev|noexec|nosuid)))*)",
          "type": "string"
        },
        "quota": {
          "description": "在容器内启用用户配额（不支持 ZFS 子卷）",
          "optional": 1,
          "type": "boolean"
        },
        "replicate": {
          "default": 1,
          "description": "将此卷包含在存储复制作业中。",
          "optional": 1,
          "type": "boolean"
        },
        "ro": {
          "description": "只读挂载点",
          "optional": 1,
          "type": "boolean"
        },
        "shared": {
          "default": 0,
          "description": "将此非卷挂载点标记为在多个节点上可用（参见 'nodes'）",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此非卷挂载点标记为在所有节点上可用。\n\n警告：此选项不会自动共享挂载点，而是假定它已共享！"
        },
        "size": {
          "description": "卷大小（只读值）。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "default_key": 1,
          "description": "要挂载到容器内的卷、设备或目录。",
          "format": "pve-lxc-mp-string",
          "format_description": "volume",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string"
    },
    "searchdomain": {
      "description": "设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。",
      "format": "dns-name-list",
      "optional": 1,
      "type": "string"
    },
    "startup": {
      "description": "启动和关闭行为。Order 是非负数，定义总体启动顺序。关闭按相反顺序执行。另外可设置以秒为单位的 'up' 或 'down' 延迟，指定启动或停止下一个虚拟机前等待的时间。",
      "format": "pve-startup-order",
      "optional": 1,
      "type": "string",
      "typetext": "[[order=]\\d+] [,up=\\d+] [,down=\\d+] "
    },
    "swap": {
      "default": 512,
      "description": "容器的 SWAP 容量，单位为 MB。",
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "tags": {
      "description": "容器标签。此项仅为元信息。",
      "format": "pve-tag-list",
      "optional": 1,
      "type": "string"
    },
    "template": {
      "default": 0,
      "description": "启用/禁用模板。",
      "optional": 1,
      "type": "boolean"
    },
    "timezone": {
      "description": "容器内使用的时区。如果未设置此选项，则不做任何操作。可设为 'host' 以匹配宿主机时区，或设为 /usr/share/zoneinfo/zone.tab 中的任意时区选项",
      "format": "pve-ct-timezone",
      "optional": 1,
      "type": "string"
    },
    "tty": {
      "default": 2,
      "description": "指定容器可用的 tty 数量",
      "maximum": 6,
      "minimum": 0,
      "optional": 1,
      "type": "integer"
    },
    "unprivileged": {
      "default": 0,
      "description": "使容器以非特权用户身份运行。创建时默认为 1。还原时默认为备份中的值。（不应手动修改。）",
      "optional": 1,
      "type": "boolean"
    },
    "unused[n]": {
      "description": "对未使用卷的引用。此项供内部使用，不应手动修改。",
      "format": {
        "volume": {
          "default_key": 1,
          "description": "当前未使用的卷。",
          "format": "pve-volume-id",
          "format_description": "volume",
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

## PUT `/nodes/{node}/lxc/{vmid}/config`

设置容器选项。

**方法标识：** `update_vm`

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Disk",
      "VM.Config.CPU",
      "VM.Config.Memory",
      "VM.Config.Network",
      "VM.Config.Options"
    ],
    "any",
    1
  ],
  "description": "rootfs 和 mp[n] 中的非卷挂载点仅限 root@pam 使用"
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
| `arch` | string | 否 | "amd64" | 操作系统架构类型。；可选值：`amd64`, `i386`, `arm64`, `armhf`, `riscv32`, `riscv64` |
| `cmode` | string | 否 | "tty" | 控制台模式。默认情况下，console 命令尝试连接到一个可用的 tty 设备。将 cmode 设为 'console' 时，会改为尝试连接到 /dev/console。如果将 cmode 设为 'shell'，则直接在容器内调用 shell（无需登录）。；可选值：`shell`, `console`, `tty` |
| `console` | boolean | 否 | 1 | 将控制台设备（/dev/console）连接到容器。 |
| `cores` | integer | 否 | — | 分配给容器的核心数。默认情况下，容器可使用所有可用核心。 |
| `cpulimit` | number | 否 | 0 | CPU 使用量限制。<br><br>注意：如果计算机有 2 个 CPU，则 CPU 时间总量为 '2'。值 '0' 表示不限制 CPU。 |
| `cpuunits` | integer | 否 | "cgroup v1: 1024, cgroup v2: 100" | 容器的 CPU 权重。内核公平调度器使用此参数。数值越大，此容器获得的 CPU 时间越多。该数值相对于其他所有运行中客户机的权重而言。 |
| `debug` | boolean | 否 | 0 | 尝试输出更详细的信息。目前仅在启动时启用 debug 日志级别。 |
| `delete` | string | 否 | — | 要删除的设置列表。 |
| `description` | string | 否 | — | 容器描述。显示在 Web 界面的容器摘要中。作为注释保存在配置文件中。 |
| `dev[n]` | string | 否 | — | 要直通到容器的设备 |
| `digest` | string | 否 | — | 如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。 |
| `entrypoint` | string | 否 | "/sbin/init" | 用作 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制程序开头。 |
| `env` | string | 否 | — | 容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。 |
| `features` | string | 否 | — | 允许容器访问高级功能。 |
| `hookscript` | string | 否 | — | 在容器生命周期各个阶段执行的脚本。 |
| `hostname` | string | 否 | — | 为容器设置主机名。 |
| `lock` | string | 否 | — | 锁定/解锁容器。；可选值：`backup`, `create`, `destroyed`, `disk`, `fstrim`, `migrate`, `mounted`, `rollback`, `snapshot`, `snapshot-delete` |
| `memory` | integer | 否 | 512 | 容器的 RAM 容量，单位为 MB。 |
| `mp[n]` | string | 否 | — | 将卷用作容器挂载点。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。 |
| `nameserver` | string | 否 | — | 设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。 |
| `net[n]` | string | 否 | — | 指定容器的网络接口。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `onboot` | boolean | 否 | 0 | 指定容器是否在系统启动时启动。 |
| `ostype` | string | 否 | — | 操作系统类型。用于在容器内设置配置，对应 /usr/share/lxc/config/&lt;ostype&gt;.common.conf 中的 LXC 设置脚本。值 'unmanaged' 可用于跳过所有操作系统特定设置。；可选值：`debian`, `devuan`, `ubuntu`, `centos`, `fedora`, `opensuse`, `archlinux`, `alpine`, `gentoo`, `nixos`, `unmanaged` |
| `protection` | boolean | 否 | 0 | 设置容器的保护标志。此项将阻止容器或容器磁盘的移除/更新操作。 |
| `revert` | string | 否 | — | 撤销待应用的更改。 |
| `rootfs` | string | 否 | — | 将卷用作容器根目录。 |
| `searchdomain` | string | 否 | — | 设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。 |
| `startup` | string | 否 | — | 启动和关闭行为。Order 是非负数，定义总体启动顺序。关闭按相反顺序执行。另外可设置以秒为单位的 'up' 或 'down' 延迟，指定启动或停止下一个虚拟机前等待的时间。 |
| `swap` | integer | 否 | 512 | 容器的 SWAP 容量，单位为 MB。 |
| `tags` | string | 否 | — | 容器标签。此项仅为元信息。 |
| `template` | boolean | 否 | 0 | 启用/禁用模板。 |
| `timezone` | string | 否 | — | 容器内使用的时区。如果未设置此选项，则不做任何操作。可设为 'host' 以匹配宿主机时区，或设为 /usr/share/zoneinfo/zone.tab 中的任意时区选项 |
| `tty` | integer | 否 | 2 | 指定容器可用的 tty 数量 |
| `unprivileged` | boolean | 否 | 0 | 使容器以非特权用户身份运行。创建时默认为 1。还原时默认为备份中的值。（不应手动修改。） |
| `unused[n]` | string | 否 | — | 对未使用卷的引用。此项供内部使用，不应手动修改。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "arch": {
      "default": "amd64",
      "description": "操作系统架构类型。",
      "enum": [
        "amd64",
        "i386",
        "arm64",
        "armhf",
        "riscv32",
        "riscv64"
      ],
      "optional": 1,
      "type": "string"
    },
    "cmode": {
      "default": "tty",
      "description": "控制台模式。默认情况下，console 命令尝试连接到一个可用的 tty 设备。将 cmode 设为 'console' 时，会改为尝试连接到 /dev/console。如果将 cmode 设为 'shell'，则直接在容器内调用 shell（无需登录）。",
      "enum": [
        "shell",
        "console",
        "tty"
      ],
      "optional": 1,
      "type": "string"
    },
    "console": {
      "default": 1,
      "description": "将控制台设备（/dev/console）连接到容器。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cores": {
      "description": "分配给容器的核心数。默认情况下，容器可使用所有可用核心。",
      "maximum": 8192,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 8192)"
    },
    "cpulimit": {
      "default": 0,
      "description": "CPU 使用量限制。\n\n注意：如果计算机有 2 个 CPU，则 CPU 时间总量为 '2'。值 '0' 表示不限制 CPU。",
      "maximum": 8192,
      "minimum": 0,
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - 8192)"
    },
    "cpuunits": {
      "default": "cgroup v1: 1024, cgroup v2: 100",
      "description": "容器的 CPU 权重，在 cgroup v2 中会限制到 [1, 10000] 范围内。",
      "maximum": 500000,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 500000)",
      "verbose_description": "容器的 CPU 权重。内核公平调度器使用此参数。数值越大，此容器获得的 CPU 时间越多。该数值相对于其他所有运行中客户机的权重而言。"
    },
    "debug": {
      "default": 0,
      "description": "尝试输出更详细的信息。目前仅在启动时启用 debug 日志级别。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "delete": {
      "description": "要删除的设置列表。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "description": {
      "description": "容器描述。显示在 Web 界面的容器摘要中。作为注释保存在配置文件中。",
      "maxLength": 8192,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dev[n]": {
      "description": "要直通到容器的设备",
      "format": {
        "deny-write": {
          "default": 0,
          "description": "禁止容器写入设备",
          "optional": 1,
          "type": "boolean"
        },
        "gid": {
          "description": "要分配给设备节点的组 ID",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "mode": {
          "description": "要为设备节点设置的访问模式",
          "format_description": "Octal access mode",
          "optional": 1,
          "pattern": "0[0-7]{3}",
          "type": "string"
        },
        "path": {
          "default_key": 1,
          "description": "要直通到容器的设备",
          "format": "pve-lxc-dev-string",
          "format_description": "Path",
          "optional": 1,
          "type": "string",
          "verbose_description": "要直通到容器的设备路径"
        },
        "uid": {
          "description": "要分配给设备节点的用户 ID",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]"
    },
    "digest": {
      "description": "如果当前配置文件的 SHA1 摘要不同，则阻止更改。可用于防止并发修改。",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "entrypoint": {
      "default": "/sbin/init",
      "description": "用作 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制程序开头。",
      "optional": 1,
      "pattern": "(?^:[^\\x00-\\x08\\x0a-\\x1F\\x7F]+)",
      "type": "string"
    },
    "env": {
      "description": "容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。",
      "optional": 1,
      "pattern": "(?^:(?:\\w+=[^\\x00-\\x08\\x0a-\\x1F\\x7F]*)(?:\\0\\w+=[^\\x00-\\x08\\x0a-\\x1F\\x7F]*)*)",
      "type": "string"
    },
    "features": {
      "description": "允许容器访问高级功能。",
      "format": {
        "force_rw_sys": {
          "default": 0,
          "description": "在非特权容器中将 /sys 挂载为 `rw`，而非 `mixed`。在使用较新版本（>= v245）的 systemd-network 时，这可能破坏网络功能。",
          "optional": 1,
          "type": "boolean"
        },
        "fuse": {
          "default": 0,
          "description": "允许在容器内使用 'fuse' 文件系统。注意，fuse 与 freezer cgroup 之间的交互可能导致 I/O 死锁。",
          "optional": 1,
          "type": "boolean"
        },
        "keyctl": {
          "default": 0,
          "description": "仅适用于非特权容器：允许使用 keyctl() 系统调用。在容器内使用 docker 需要此功能。默认情况下，非特权容器会认为此系统调用不存在。这主要是针对 systemd-networkd 的变通措施，因为当内核因权限不足而拒绝某些 keyctl() 操作时，它会将其视为致命错误。实质上，您可以在运行 systemd-networkd 和 docker 之间作出选择。",
          "optional": 1,
          "type": "boolean"
        },
        "mknod": {
          "default": 0,
          "description": "允许非特权容器使用 mknod() 添加特定设备节点。这需要内核支持将 seccomp 陷阱交由用户空间处理（5.3 或更新版本）。此功能为实验性。",
          "optional": 1,
          "type": "boolean"
        },
        "mount": {
          "description": "允许挂载特定类型的文件系统。此处应为 mount 命令所用的文件系统类型列表。注意，这可能对容器安全性产生负面影响。可以访问 loop 设备时，挂载文件能够绕过 devices cgroup 的 mknod 权限；挂载 NFS 文件系统可能完全阻塞宿主机 I/O 并使其无法重启等。",
          "format_description": "fstype;fstype;...",
          "optional": 1,
          "pattern": "(?^:[a-zA-Z0-9_; ]+)",
          "type": "string"
        },
        "nesting": {
          "default": 0,
          "description": "允许嵌套。最好与具有附加 ID 映射的非特权容器一起使用。注意，这会向客户机暴露宿主机的 procfs 和 sysfs 内容。systemd 隔离服务也需要此功能。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]"
    },
    "hookscript": {
      "description": "在容器生命周期各个阶段执行的脚本。",
      "format": "pve-volume-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "hostname": {
      "description": "为容器设置主机名。",
      "format": "dns-name",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "lock": {
      "description": "锁定/解锁容器。",
      "enum": [
        "backup",
        "create",
        "destroyed",
        "disk",
        "fstrim",
        "migrate",
        "mounted",
        "rollback",
        "snapshot",
        "snapshot-delete"
      ],
      "optional": 1,
      "type": "string"
    },
    "memory": {
      "default": 512,
      "description": "容器的 RAM 容量，单位为 MB。",
      "minimum": 16,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (16 - N)"
    },
    "mp[n]": {
      "description": "将卷用作容器挂载点。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。",
      "format": {
        "acl": {
          "description": "显式启用或禁用 ACL 支持。",
          "optional": 1,
          "type": "boolean"
        },
        "backup": {
          "description": "是否在备份中包含挂载点。",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "是否在备份中包含挂载点（仅适用于卷挂载点）。"
        },
        "idmap": {
          "description": "将特定容器 UID/GID 映射到此挂载点底层磁盘的 UID/GID",
          "format_description": "type:container:disk:range-size[;type:container:disk:range-size;...]",
          "optional": 1,
          "pattern": "(?^:^(?:passthrough|[ug]:[0-9]+:[0-9]+:[1-9][0-9]*(?:;[ug]:[0-9]+:[0-9]+:[1-9][0-9]*)*)$)",
          "type": "string",
          "verbose_description": "自定义 UID/GID 映射，覆盖此挂载点的容器 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。\n\n`type` 对 UID 为 `u`，对 GID 为 `g`。\n\n`container` 是容器内看到的第一个 ID。\n\n`disk` 是底层文件系统上相应的第一个 ID。\n\n`range-size` 是要映射的连续 ID 数量。\n\n未映射的 ID 回退到容器的 `lxc.idmap`。\n\n示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上属于 UID 456 的文件，在容器内显示为属于 UID 123。\n\n示例 2：`g:100:50:5` 映射 5 个连续 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。\n\n示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，即容器内的 ID 与磁盘上的 ID 相同。"
        },
        "keepattrs": {
          "default": 0,
          "description": "从挂载点目录继承所有权和权限。",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "如果挂载点目录已存在，则继承其 UID、GID 和访问模式。"
        },
        "mountoptions": {
          "description": "rootfs/mps 的额外挂载选项。",
          "format_description": "opt[;opt...]",
          "optional": 1,
          "pattern": "(?^:(?^:(discard|lazytime|noatime|nodev|noexec|nosuid))(;(?^:(discard|lazytime|noatime|nodev|noexec|nosuid)))*)",
          "type": "string"
        },
        "mp": {
          "description": "从容器内部看到的挂载点路径（不得包含符号链接）。",
          "format": "pve-lxc-mp-string",
          "format_description": "Path",
          "type": "string",
          "verbose_description": "从容器内部看到的挂载点路径。\n\n注意：出于安全原因，不得包含任何符号链接。"
        },
        "quota": {
          "description": "在容器内启用用户配额（不支持 ZFS 子卷）",
          "optional": 1,
          "type": "boolean"
        },
        "replicate": {
          "default": 1,
          "description": "将此卷包含在存储复制作业中。",
          "optional": 1,
          "type": "boolean"
        },
        "ro": {
          "description": "只读挂载点",
          "optional": 1,
          "type": "boolean"
        },
        "shared": {
          "default": 0,
          "description": "将此非卷挂载点标记为在多个节点上可用（参见 'nodes'）",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此非卷挂载点标记为在所有节点上可用。\n\n警告：此选项不会自动共享挂载点，而是假定它已共享！"
        },
        "size": {
          "description": "卷大小（只读值）。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "default_key": 1,
          "description": "要挂载到容器内的卷、设备或目录。",
          "format": "pve-lxc-mp-string",
          "format_description": "volume",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]"
    },
    "nameserver": {
      "description": "设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。",
      "format": "lxc-ip-with-ll-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "net[n]": {
      "description": "指定容器的网络接口。",
      "format": {
        "bridge": {
          "description": "网络设备要连接的网桥。",
          "format_description": "bridge",
          "optional": 1,
          "pattern": "[-_.\\w\\d]+",
          "type": "string"
        },
        "firewall": {
          "description": "控制是否使用此接口的防火墙规则。",
          "optional": 1,
          "type": "boolean"
        },
        "gw": {
          "description": "IPv4 流量的默认网关。",
          "format": "ipv4",
          "format_description": "GatewayIPv4",
          "optional": 1,
          "type": "string"
        },
        "gw6": {
          "description": "IPv6 流量的默认网关。",
          "format": "ipv6",
          "format_description": "GatewayIPv6",
          "optional": 1,
          "type": "string"
        },
        "host-managed": {
          "description": "此接口的 IP 配置是否由宿主机管理。启用时，由宿主机而非容器负责此接口的 IP 配置。容器不应在此接口上运行自己的 DHCP 客户端或网络管理器。适用于缺少内部网络管理栈的容器，例如许多应用容器。",
          "optional": 1,
          "type": "boolean"
        },
        "hwaddr": {
          "description": "接口 MAC 地址。默认动态分配，但可按需静态设置，例如始终使用同一链路本地 IPv6 地址。（lxc.network.hwaddr）",
          "format": "mac-addr",
          "format_description": "XX:XX:XX:XX:XX:XX",
          "optional": 1,
          "type": "string",
          "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
        },
        "ip": {
          "description": "CIDR 格式的 IPv4 地址。",
          "format": "pve-ipv4-config",
          "format_description": "(IPv4/CIDR|dhcp|manual)",
          "optional": 1,
          "type": "string"
        },
        "ip6": {
          "description": "CIDR 格式的 IPv6 地址。",
          "format": "pve-ipv6-config",
          "format_description": "(IPv6/CIDR|auto|dhcp|manual)",
          "optional": 1,
          "type": "string"
        },
        "link_down": {
          "description": "是否断开此接口的连接（如同拔掉网线）。",
          "optional": 1,
          "type": "boolean"
        },
        "mtu": {
          "description": "接口的最大传输单元。（lxc.network.mtu）",
          "maximum": 65535,
          "minimum": 64,
          "optional": 1,
          "type": "integer"
        },
        "name": {
          "description": "从容器内部看到的网络设备名称。（lxc.network.name）",
          "format_description": "string",
          "pattern": "[-_.\\w\\d]+",
          "type": "string"
        },
        "rate": {
          "description": "对接口应用速率限制",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "tag": {
          "description": "此接口的 VLAN 标签。",
          "maximum": 4094,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "trunks": {
          "description": "通过此接口的 VLAN ID",
          "format_description": "vlanid[;vlanid...]",
          "optional": 1,
          "pattern": "(?^:\\d+(?:;\\d+)*)",
          "type": "string"
        },
        "type": {
          "description": "网络接口类型。",
          "enum": [
            "veth"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "onboot": {
      "default": 0,
      "description": "指定容器是否在系统启动时启动。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ostype": {
      "description": "操作系统类型。用于在容器内设置配置，对应 /usr/share/lxc/config/<ostype>.common.conf 中的 LXC 设置脚本。值 'unmanaged' 可用于跳过所有操作系统特定设置。",
      "enum": [
        "debian",
        "devuan",
        "ubuntu",
        "centos",
        "fedora",
        "opensuse",
        "archlinux",
        "alpine",
        "gentoo",
        "nixos",
        "unmanaged"
      ],
      "optional": 1,
      "type": "string"
    },
    "protection": {
      "default": 0,
      "description": "设置容器的保护标志。此项将阻止容器或容器磁盘的移除/更新操作。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "revert": {
      "description": "撤销待应用的更改。",
      "format": "pve-configid-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "rootfs": {
      "description": "将卷用作容器根目录。",
      "format": {
        "acl": {
          "description": "显式启用或禁用 ACL 支持。",
          "optional": 1,
          "type": "boolean"
        },
        "idmap": {
          "description": "将特定容器 UID/GID 映射到此挂载点底层磁盘的 UID/GID",
          "format_description": "type:container:disk:range-size[;type:container:disk:range-size;...]",
          "optional": 1,
          "pattern": "(?^:^(?:passthrough|[ug]:[0-9]+:[0-9]+:[1-9][0-9]*(?:;[ug]:[0-9]+:[0-9]+:[1-9][0-9]*)*)$)",
          "type": "string",
          "verbose_description": "自定义 UID/GID 映射，覆盖此挂载点的容器 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。\n\n`type` 对 UID 为 `u`，对 GID 为 `g`。\n\n`container` 是容器内看到的第一个 ID。\n\n`disk` 是底层文件系统上相应的第一个 ID。\n\n`range-size` 是要映射的连续 ID 数量。\n\n未映射的 ID 回退到容器的 `lxc.idmap`。\n\n示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上属于 UID 456 的文件，在容器内显示为属于 UID 123。\n\n示例 2：`g:100:50:5` 映射 5 个连续 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。\n\n示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，即容器内的 ID 与磁盘上的 ID 相同。"
        },
        "mountoptions": {
          "description": "rootfs/mps 的额外挂载选项。",
          "format_description": "opt[;opt...]",
          "optional": 1,
          "pattern": "(?^:(?^:(discard|lazytime|noatime|nodev|noexec|nosuid))(;(?^:(discard|lazytime|noatime|nodev|noexec|nosuid)))*)",
          "type": "string"
        },
        "quota": {
          "description": "在容器内启用用户配额（不支持 ZFS 子卷）",
          "optional": 1,
          "type": "boolean"
        },
        "replicate": {
          "default": 1,
          "description": "将此卷包含在存储复制作业中。",
          "optional": 1,
          "type": "boolean"
        },
        "ro": {
          "description": "只读挂载点",
          "optional": 1,
          "type": "boolean"
        },
        "shared": {
          "default": 0,
          "description": "将此非卷挂载点标记为在多个节点上可用（参见 'nodes'）",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此非卷挂载点标记为在所有节点上可用。\n\n警告：此选项不会自动共享挂载点，而是假定它已共享！"
        },
        "size": {
          "description": "卷大小（只读值）。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "default_key": 1,
          "description": "要挂载到容器内的卷、设备或目录。",
          "format": "pve-lxc-mp-string",
          "format_description": "volume",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]"
    },
    "searchdomain": {
      "description": "设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。",
      "format": "dns-name-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "startup": {
      "description": "启动和关闭行为。Order 是非负数，定义总体启动顺序。关闭按相反顺序执行。另外可设置以秒为单位的 'up' 或 'down' 延迟，指定启动或停止下一个虚拟机前等待的时间。",
      "format": "pve-startup-order",
      "optional": 1,
      "type": "string",
      "typetext": "[[order=]\\d+] [,up=\\d+] [,down=\\d+] "
    },
    "swap": {
      "default": 512,
      "description": "容器的 SWAP 容量，单位为 MB。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "tags": {
      "description": "容器标签。此项仅为元信息。",
      "format": "pve-tag-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "template": {
      "default": 0,
      "description": "启用/禁用模板。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "timezone": {
      "description": "容器内使用的时区。如果未设置此选项，则不做任何操作。可设为 'host' 以匹配宿主机时区，或设为 /usr/share/zoneinfo/zone.tab 中的任意时区选项",
      "format": "pve-ct-timezone",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tty": {
      "default": 2,
      "description": "指定容器可用的 tty 数量",
      "maximum": 6,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 6)"
    },
    "unprivileged": {
      "default": 0,
      "description": "使容器以非特权用户身份运行。创建时默认为 1。还原时默认为备份中的值。（不应手动修改。）",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "unused[n]": {
      "description": "对未使用卷的引用。此项供内部使用，不应手动修改。",
      "format": {
        "volume": {
          "default_key": 1,
          "description": "当前未使用的卷。",
          "format": "pve-volume-id",
          "format_description": "volume",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[volume=]<volume>"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/config)。
