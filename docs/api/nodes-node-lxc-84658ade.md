# `/nodes/{node}/lxc`

原始接口路径：`/nodes/{node}/lxc`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/lxc`

LXC 容器索引（按节点）。

**方法标识：** `vmlist`

**权限**

```json
{
  "description": "Only list CTs where you have VM.Audit permission on /vms/<vmid>.",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `node` | string | 是 | — | The cluster node name. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
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
  "items": {
    "properties": {
      "cpu": {
        "description": "Current CPU usage.",
        "optional": 1,
        "type": "number"
      },
      "cpus": {
        "description": "Maximum usable CPUs.",
        "optional": 1,
        "type": "number"
      },
      "disk": {
        "description": "Root disk image space-usage in bytes.",
        "minimum": 0,
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "diskread": {
        "description": "The amount of bytes the guest read from it's block devices since the guest was started. (Note: This info is not available for all storage types.)",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "diskwrite": {
        "description": "The amount of bytes the guest wrote from it's block devices since the guest was started. (Note: This info is not available for all storage types.)",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "lock": {
        "description": "The current config lock, if any.",
        "optional": 1,
        "type": "string"
      },
      "maxdisk": {
        "description": "Root disk image size in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "maxmem": {
        "description": "Maximum memory in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "maxswap": {
        "description": "Maximum SWAP memory in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "mem": {
        "description": "Currently used memory in bytes.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "name": {
        "description": "Container name.",
        "optional": 1,
        "type": "string"
      },
      "netin": {
        "description": "The amount of traffic in bytes that was sent to the guest over the network since it was started.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "netout": {
        "description": "The amount of traffic in bytes that was sent from the guest over the network since it was started.",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "pressurecpusome": {
        "description": "CPU Some pressure stall average over the last 10 seconds.",
        "optional": 1,
        "type": "number"
      },
      "pressureiofull": {
        "description": "IO Full pressure stall average over the last 10 seconds.",
        "optional": 1,
        "type": "number"
      },
      "pressureiosome": {
        "description": "IO Some pressure stall average over the last 10 seconds.",
        "optional": 1,
        "type": "number"
      },
      "pressurememoryfull": {
        "description": "Memory Full pressure stall average over the last 10 seconds.",
        "optional": 1,
        "type": "number"
      },
      "pressurememorysome": {
        "description": "Memory Some pressure stall average over the last 10 seconds.",
        "optional": 1,
        "type": "number"
      },
      "status": {
        "description": "LXC Container status.",
        "enum": [
          "stopped",
          "running"
        ],
        "type": "string"
      },
      "tags": {
        "description": "The current configured tags, if any.",
        "optional": 1,
        "type": "string"
      },
      "template": {
        "default": 0,
        "description": "Determines if the guest is a template.",
        "optional": 1,
        "type": "boolean"
      },
      "uptime": {
        "description": "Uptime in seconds.",
        "optional": 1,
        "renderer": "duration",
        "type": "integer"
      },
      "vmid": {
        "description": "The (unique) ID of the VM.",
        "format": "pve-vmid",
        "maximum": 999999999,
        "minimum": 100,
        "type": "integer"
      }
    },
    "type": "object"
  },
  "links": [
    {
      "href": "{vmid}",
      "rel": "child"
    }
  ],
  "type": "array"
}
```

## POST `/nodes/{node}/lxc`

创建或恢复容器。

**方法标识：** `create_vm`

**权限**

```json
{
  "description": "You need 'VM.Allocate' permission on /vms/{vmid} or on the VM pool /pool/{pool}. For restore, it is enough if the user has 'VM.Backup' permission and the VM already exists. You also need 'Datastore.AllocateSpace' permissions on the storage. For privileged containers, 'Sys.Modify' permissions on '/' are required.",
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

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `arch` | string | 否 | "amd64" | OS architecture type.；可选值：`amd64`, `i386`, `arm64`, `armhf`, `riscv32`, `riscv64` |
| `bwlimit` | number | 否 | "restore limit from datacenter or storage config" | Override I/O bandwidth limit (in KiB/s). |
| `cmode` | string | 否 | "tty" | Console mode. By default, the console command tries to open a connection to one of the available tty devices. By setting cmode to 'console' it tries to attach to /dev/console instead. If you set cmode to 'shell', it simply invokes a shell inside the container (no login).；可选值：`shell`, `console`, `tty` |
| `console` | boolean | 否 | 1 | Attach a console device (/dev/console) to the container. |
| `cores` | integer | 否 | — | The number of cores assigned to the container. A container can use all available cores by default. |
| `cpulimit` | number | 否 | 0 | Limit of CPU usage. NOTE: If the computer has 2 CPUs, it has a total of '2' CPU time. Value '0' indicates no CPU limit. |
| `cpuunits` | integer | 否 | "cgroup v1: 1024, cgroup v2: 100" | CPU weight for a container, will be clamped to [1, 10000] in cgroup v2. |
| `debug` | boolean | 否 | 0 | Try to be more verbose. For now this only enables debug log-level on start. |
| `description` | string | 否 | — | Description for the Container. Shown in the web-interface CT's summary. This is saved as comment inside the configuration file. |
| `dev[n]` | string | 否 | — | Device to pass through to the container |
| `entrypoint` | string | 否 | "/sbin/init" | Command to run as init, optionally with arguments; may start with an absolute path, relative path, or a binary in $PATH. |
| `env` | string | 否 | — | The container runtime environment as NUL-separated list. Replaces any lxc.environment.runtime entries in the config. |
| `features` | string | 否 | — | Allow containers access to advanced features. |
| `force` | boolean | 否 | — | Allow to overwrite existing container. |
| `ha-managed` | boolean | 否 | 0 | Add the CT as a HA resource after it was created. |
| `hookscript` | string | 否 | — | Script that will be executed during various steps in the containers lifetime. |
| `hostname` | string | 否 | — | Set a host name for the container. |
| `ignore-unpack-errors` | boolean | 否 | — | Ignore errors when extracting the template. |
| `lock` | string | 否 | — | Lock/unlock the container.；可选值：`backup`, `create`, `destroyed`, `disk`, `fstrim`, `migrate`, `mounted`, `rollback`, `snapshot`, `snapshot-delete` |
| `memory` | integer | 否 | 512 | Amount of RAM for the container in MB. |
| `mp[n]` | string | 否 | — | Use volume as container mount point. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume. |
| `nameserver` | string | 否 | — | Sets DNS server IP address for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver. |
| `net[n]` | string | 否 | — | Specifies network interfaces for the container. |
| `node` | string | 是 | — | The cluster node name. |
| `onboot` | boolean | 否 | 0 | Specifies whether a container will be started during system bootup. |
| `ostemplate` | string | 是 | — | The OS template or backup file. |
| `ostype` | string | 否 | — | OS type. This is used to setup configuration inside the container, and corresponds to lxc setup scripts in /usr/share/lxc/config/&lt;ostype&gt;.common.conf. Value 'unmanaged' can be used to skip and OS specific setup.；可选值：`debian`, `devuan`, `ubuntu`, `centos`, `fedora`, `opensuse`, `archlinux`, `alpine`, `gentoo`, `nixos`, `unmanaged` |
| `password` | string | 否 | — | Sets root password inside container. |
| `pool` | string | 否 | — | Add the VM to the specified pool. |
| `protection` | boolean | 否 | 0 | Sets the protection flag of the container. This will prevent the CT or CT's disk remove/update operation. |
| `restore` | boolean | 否 | — | Mark this as restore task. |
| `rootfs` | string | 否 | — | Use volume as container root. |
| `searchdomain` | string | 否 | — | Sets DNS search domains for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver. |
| `ssh-public-keys` | string | 否 | — | Setup public SSH keys (one key per line, OpenSSH format). |
| `start` | boolean | 否 | 0 | Start the CT after its creation finished successfully. |
| `startup` | string | 否 | — | Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped. |
| `storage` | string | 否 | "local" | Default Storage. |
| `swap` | integer | 否 | 512 | Amount of SWAP for the container in MB. |
| `tags` | string | 否 | — | Tags of the Container. This is only meta information. |
| `template` | boolean | 否 | 0 | Enable/disable Template. |
| `timezone` | string | 否 | — | Time zone to use in the container. If option isn't set, then nothing will be done. Can be set to 'host' to match the host time zone, or an arbitrary time zone option from /usr/share/zoneinfo/zone.tab |
| `tty` | integer | 否 | 2 | Specify the number of tty available to the container |
| `unique` | boolean | 否 | — | Assign a unique random ethernet address. |
| `unprivileged` | boolean | 否 | 0 | Makes the container run as unprivileged user. For creation, the default is 1. For restore, the default is the value from the backup. (Should not be modified manually.) |
| `unused[n]` | string | 否 | — | Reference to unused volumes. This is used internally, and should not be modified manually. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "arch": {
      "default": "amd64",
      "description": "OS architecture type.",
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
    "bwlimit": {
      "default": "restore limit from datacenter or storage config",
      "description": "Override I/O bandwidth limit (in KiB/s).",
      "minimum": "0",
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - N)"
    },
    "cmode": {
      "default": "tty",
      "description": "Console mode. By default, the console command tries to open a connection to one of the available tty devices. By setting cmode to 'console' it tries to attach to /dev/console instead. If you set cmode to 'shell', it simply invokes a shell inside the container (no login).",
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
      "description": "Attach a console device (/dev/console) to the container.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "cores": {
      "description": "The number of cores assigned to the container. A container can use all available cores by default.",
      "maximum": 8192,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 8192)"
    },
    "cpulimit": {
      "default": 0,
      "description": "Limit of CPU usage. NOTE: If the computer has 2 CPUs, it has a total of '2' CPU time. Value '0' indicates no CPU limit.",
      "maximum": 8192,
      "minimum": 0,
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - 8192)"
    },
    "cpuunits": {
      "default": "cgroup v1: 1024, cgroup v2: 100",
      "description": "CPU weight for a container, will be clamped to [1, 10000] in cgroup v2.",
      "maximum": 500000,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 500000)",
      "verbose_description": "CPU weight for a container. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this container gets. Number is relative to the weights of all the other running guests."
    },
    "debug": {
      "default": 0,
      "description": "Try to be more verbose. For now this only enables debug log-level on start.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "description": {
      "description": "Description for the Container. Shown in the web-interface CT's summary. This is saved as comment inside the configuration file.",
      "maxLength": 8192,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "dev[n]": {
      "description": "Device to pass through to the container",
      "format": {
        "deny-write": {
          "default": 0,
          "description": "Deny the container to write to the device",
          "optional": 1,
          "type": "boolean"
        },
        "gid": {
          "description": "Group ID to be assigned to the device node",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "mode": {
          "description": "Access mode to be set on the device node",
          "format_description": "Octal access mode",
          "optional": 1,
          "pattern": "0[0-7]{3}",
          "type": "string"
        },
        "path": {
          "default_key": 1,
          "description": "Device to pass through to the container",
          "format": "pve-lxc-dev-string",
          "format_description": "Path",
          "optional": 1,
          "type": "string",
          "verbose_description": "Path to the device to pass through to the container"
        },
        "uid": {
          "description": "User ID to be assigned to the device node",
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]"
    },
    "entrypoint": {
      "default": "/sbin/init",
      "description": "Command to run as init, optionally with arguments; may start with an absolute path, relative path, or a binary in $PATH.",
      "optional": 1,
      "pattern": "(?^:[^\\x00-\\x08\\x0a-\\x1F\\x7F]+)",
      "type": "string"
    },
    "env": {
      "description": "The container runtime environment as NUL-separated list. Replaces any lxc.environment.runtime entries in the config.",
      "optional": 1,
      "pattern": "(?^:(?:\\w+=[^\\x00-\\x08\\x0a-\\x1F\\x7F]*)(?:\\0\\w+=[^\\x00-\\x08\\x0a-\\x1F\\x7F]*)*)",
      "type": "string"
    },
    "features": {
      "description": "Allow containers access to advanced features.",
      "format": {
        "force_rw_sys": {
          "default": 0,
          "description": "Mount /sys in unprivileged containers as `rw` instead of `mixed`. This can break networking under newer (>= v245) systemd-network use.",
          "optional": 1,
          "type": "boolean"
        },
        "fuse": {
          "default": 0,
          "description": "Allow using 'fuse' file systems in a container. Note that interactions between fuse and the freezer cgroup can potentially cause I/O deadlocks.",
          "optional": 1,
          "type": "boolean"
        },
        "keyctl": {
          "default": 0,
          "description": "For unprivileged containers only: Allow the use of the keyctl() system call. This is required to use docker inside a container. By default unprivileged containers will see this system call as non-existent. This is mostly a workaround for systemd-networkd, as it will treat it as a fatal error when some keyctl() operations are denied by the kernel due to lacking permissions. Essentially, you can choose between running systemd-networkd or docker.",
          "optional": 1,
          "type": "boolean"
        },
        "mknod": {
          "default": 0,
          "description": "Allow unprivileged containers to use mknod() to add certain device nodes. This requires a kernel with seccomp trap to user space support (5.3 or newer). This is experimental.",
          "optional": 1,
          "type": "boolean"
        },
        "mount": {
          "description": "Allow mounting file systems of specific types. This should be a list of file system types as used with the mount command. Note that this can have negative effects on the container's security. With access to a loop device, mounting a file can circumvent the mknod permission of the devices cgroup, mounting an NFS file system can block the host's I/O completely and prevent it from rebooting, etc.",
          "format_description": "fstype;fstype;...",
          "optional": 1,
          "pattern": "(?^:[a-zA-Z0-9_; ]+)",
          "type": "string"
        },
        "nesting": {
          "default": 0,
          "description": "Allow nesting. Best used with unprivileged containers with additional id mapping. Note that this will expose procfs and sysfs contents of the host to the guest. This is also required by systemd to isolate services.",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]"
    },
    "force": {
      "description": "Allow to overwrite existing container.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ha-managed": {
      "default": 0,
      "description": "Add the CT as a HA resource after it was created.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hookscript": {
      "description": "Script that will be executed during various steps in the containers lifetime.",
      "format": "pve-volume-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "hostname": {
      "description": "Set a host name for the container.",
      "format": "dns-name",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ignore-unpack-errors": {
      "description": "Ignore errors when extracting the template.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lock": {
      "description": "Lock/unlock the container.",
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
      "description": "Amount of RAM for the container in MB.",
      "minimum": 16,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (16 - N)"
    },
    "mp[n]": {
      "description": "Use volume as container mount point. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume.",
      "format": {
        "acl": {
          "description": "Explicitly enable or disable ACL support.",
          "optional": 1,
          "type": "boolean"
        },
        "backup": {
          "description": "Whether to include the mount point in backups.",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "Whether to include the mount point in backups (only used for volume mount points)."
        },
        "idmap": {
          "description": "Map specific container UIDs/GIDs to underlying disk UIDs/GIDs for this mount point",
          "format_description": "type:container:disk:range-size[;type:container:disk:range-size;...]",
          "optional": 1,
          "pattern": "(?^:^(?:passthrough|[ug]:[0-9]+:[0-9]+:[1-9][0-9]*(?:;[ug]:[0-9]+:[0-9]+:[1-9][0-9]*)*)$)",
          "type": "string",
          "verbose_description": "Customize UID/GID mappings that override the container's `lxc.idmap` for this mount point. Accepts a semicolon-separated list of `type:container:disk:range-size` entries.\n\n`type` is `u` for UID or `g` for GID.\n\n`container` is the first ID as seen inside the container.\n\n`disk` is the first corresponding ID on the underlying filesystem.\n\n`range-size` is the number of consecutive IDs to map.\n\nUnmapped IDs fall back to the container's `lxc.idmap`.\n\nExample 1: `u:123:456:1` maps UID 123 in the container to UID 456 on the disk. Files owned by UID 456 on the disk will appear as UID 123 inside the container.\n\nExample 2: `g:100:50:5` maps 5 consecutive GIDs, such that GIDs 100-104 in the container are mapped to GIDs 50-54 on the disk.\n\nExample 3: `passthrough` identity-maps all UIDs and GIDs, meaning IDs inside the container will match the IDs on the disk."
        },
        "keepattrs": {
          "default": 0,
          "description": "Inherit ownership and permissions from the mount point directory.",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "Inherit UID, GID and access mode from the mount point directory, if it exists already."
        },
        "mountoptions": {
          "description": "Extra mount options for rootfs/mps.",
          "format_description": "opt[;opt...]",
          "optional": 1,
          "pattern": "(?^:(?^:(discard|lazytime|noatime|nodev|noexec|nosuid))(;(?^:(discard|lazytime|noatime|nodev|noexec|nosuid)))*)",
          "type": "string"
        },
        "mp": {
          "description": "Path to the mount point as seen from inside the container (must not contain symlinks).",
          "format": "pve-lxc-mp-string",
          "format_description": "Path",
          "type": "string",
          "verbose_description": "Path to the mount point as seen from inside the container.\n\nNOTE: Must not contain any symlinks for security reasons."
        },
        "quota": {
          "description": "Enable user quotas inside the container (not supported with zfs subvolumes)",
          "optional": 1,
          "type": "boolean"
        },
        "replicate": {
          "default": 1,
          "description": "Will include this volume to a storage replica job.",
          "optional": 1,
          "type": "boolean"
        },
        "ro": {
          "description": "Read-only mount point",
          "optional": 1,
          "type": "boolean"
        },
        "shared": {
          "default": 0,
          "description": "Mark this non-volume mount point as available on multiple nodes (see 'nodes')",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "Mark this non-volume mount point as available on all nodes.\n\nWARNING: This option does not share the mount point automatically, it assumes it is shared already!"
        },
        "size": {
          "description": "Volume size (read only value).",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "default_key": 1,
          "description": "Volume, device or directory to mount into the container.",
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
      "description": "Sets DNS server IP address for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver.",
      "format": "lxc-ip-with-ll-iface-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "net[n]": {
      "description": "Specifies network interfaces for the container.",
      "format": {
        "bridge": {
          "description": "Bridge to attach the network device to.",
          "format_description": "bridge",
          "optional": 1,
          "pattern": "[-_.\\w\\d]+",
          "type": "string"
        },
        "firewall": {
          "description": "Controls whether this interface's firewall rules should be used.",
          "optional": 1,
          "type": "boolean"
        },
        "gw": {
          "description": "Default gateway for IPv4 traffic.",
          "format": "ipv4",
          "format_description": "GatewayIPv4",
          "optional": 1,
          "type": "string"
        },
        "gw6": {
          "description": "Default gateway for IPv6 traffic.",
          "format": "ipv6",
          "format_description": "GatewayIPv6",
          "optional": 1,
          "type": "string"
        },
        "host-managed": {
          "description": "Whether this interface's IP configuration should be managed by the host. When enabled, the host (rather than the container) is responsible for the interface's IP configuration. The container should not run its own DHCP client or network manager on this interface. This is useful for containers that lack an internal network management stack, like many application containers.",
          "optional": 1,
          "type": "boolean"
        },
        "hwaddr": {
          "description": "The interface MAC address. This is dynamically allocated by default, but you can set that statically if needed, for example to always have the same link-local IPv6 address. (lxc.network.hwaddr)",
          "format": "mac-addr",
          "format_description": "XX:XX:XX:XX:XX:XX",
          "optional": 1,
          "type": "string",
          "verbose_description": "A common MAC address with the I/G (Individual/Group) bit not set."
        },
        "ip": {
          "description": "IPv4 address in CIDR format.",
          "format": "pve-ipv4-config",
          "format_description": "(IPv4/CIDR|dhcp|manual)",
          "optional": 1,
          "type": "string"
        },
        "ip6": {
          "description": "IPv6 address in CIDR format.",
          "format": "pve-ipv6-config",
          "format_description": "(IPv6/CIDR|auto|dhcp|manual)",
          "optional": 1,
          "type": "string"
        },
        "link_down": {
          "description": "Whether this interface should be disconnected (like pulling the plug).",
          "optional": 1,
          "type": "boolean"
        },
        "mtu": {
          "description": "Maximum transfer unit of the interface. (lxc.network.mtu)",
          "maximum": 65535,
          "minimum": 64,
          "optional": 1,
          "type": "integer"
        },
        "name": {
          "description": "Name of the network device as seen from inside the container. (lxc.network.name)",
          "format_description": "string",
          "pattern": "[-_.\\w\\d]+",
          "type": "string"
        },
        "rate": {
          "description": "Apply rate limiting to the interface",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "tag": {
          "description": "VLAN tag for this interface.",
          "maximum": 4094,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "trunks": {
          "description": "VLAN ids to pass through the interface",
          "format_description": "vlanid[;vlanid...]",
          "optional": 1,
          "pattern": "(?^:\\d+(?:;\\d+)*)",
          "type": "string"
        },
        "type": {
          "description": "Network interface type.",
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
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "onboot": {
      "default": 0,
      "description": "Specifies whether a container will be started during system bootup.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ostemplate": {
      "description": "The OS template or backup file.",
      "maxLength": 255,
      "type": "string",
      "typetext": "<string>"
    },
    "ostype": {
      "description": "OS type. This is used to setup configuration inside the container, and corresponds to lxc setup scripts in /usr/share/lxc/config/<ostype>.common.conf. Value 'unmanaged' can be used to skip and OS specific setup.",
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
    "password": {
      "description": "Sets root password inside container.",
      "minLength": 5,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "pool": {
      "description": "Add the VM to the specified pool.",
      "format": "pve-poolid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "protection": {
      "default": 0,
      "description": "Sets the protection flag of the container. This will prevent the CT or CT's disk remove/update operation.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "restore": {
      "description": "Mark this as restore task.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "rootfs": {
      "description": "Use volume as container root.",
      "format": {
        "acl": {
          "description": "Explicitly enable or disable ACL support.",
          "optional": 1,
          "type": "boolean"
        },
        "idmap": {
          "description": "Map specific container UIDs/GIDs to underlying disk UIDs/GIDs for this mount point",
          "format_description": "type:container:disk:range-size[;type:container:disk:range-size;...]",
          "optional": 1,
          "pattern": "(?^:^(?:passthrough|[ug]:[0-9]+:[0-9]+:[1-9][0-9]*(?:;[ug]:[0-9]+:[0-9]+:[1-9][0-9]*)*)$)",
          "type": "string",
          "verbose_description": "Customize UID/GID mappings that override the container's `lxc.idmap` for this mount point. Accepts a semicolon-separated list of `type:container:disk:range-size` entries.\n\n`type` is `u` for UID or `g` for GID.\n\n`container` is the first ID as seen inside the container.\n\n`disk` is the first corresponding ID on the underlying filesystem.\n\n`range-size` is the number of consecutive IDs to map.\n\nUnmapped IDs fall back to the container's `lxc.idmap`.\n\nExample 1: `u:123:456:1` maps UID 123 in the container to UID 456 on the disk. Files owned by UID 456 on the disk will appear as UID 123 inside the container.\n\nExample 2: `g:100:50:5` maps 5 consecutive GIDs, such that GIDs 100-104 in the container are mapped to GIDs 50-54 on the disk.\n\nExample 3: `passthrough` identity-maps all UIDs and GIDs, meaning IDs inside the container will match the IDs on the disk."
        },
        "mountoptions": {
          "description": "Extra mount options for rootfs/mps.",
          "format_description": "opt[;opt...]",
          "optional": 1,
          "pattern": "(?^:(?^:(discard|lazytime|noatime|nodev|noexec|nosuid))(;(?^:(discard|lazytime|noatime|nodev|noexec|nosuid)))*)",
          "type": "string"
        },
        "quota": {
          "description": "Enable user quotas inside the container (not supported with zfs subvolumes)",
          "optional": 1,
          "type": "boolean"
        },
        "replicate": {
          "default": 1,
          "description": "Will include this volume to a storage replica job.",
          "optional": 1,
          "type": "boolean"
        },
        "ro": {
          "description": "Read-only mount point",
          "optional": 1,
          "type": "boolean"
        },
        "shared": {
          "default": 0,
          "description": "Mark this non-volume mount point as available on multiple nodes (see 'nodes')",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "Mark this non-volume mount point as available on all nodes.\n\nWARNING: This option does not share the mount point automatically, it assumes it is shared already!"
        },
        "size": {
          "description": "Volume size (read only value).",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "default_key": 1,
          "description": "Volume, device or directory to mount into the container.",
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
      "description": "Sets DNS search domains for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver.",
      "format": "dns-name-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "ssh-public-keys": {
      "description": "Setup public SSH keys (one key per line, OpenSSH format).",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "start": {
      "default": 0,
      "description": "Start the CT after its creation finished successfully.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "startup": {
      "description": "Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped.",
      "format": "pve-startup-order",
      "optional": 1,
      "type": "string",
      "typetext": "[[order=]\\d+] [,up=\\d+] [,down=\\d+] "
    },
    "storage": {
      "default": "local",
      "description": "Default Storage.",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "swap": {
      "default": 512,
      "description": "Amount of SWAP for the container in MB.",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "tags": {
      "description": "Tags of the Container. This is only meta information.",
      "format": "pve-tag-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "template": {
      "default": 0,
      "description": "Enable/disable Template.",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "timezone": {
      "description": "Time zone to use in the container. If option isn't set, then nothing will be done. Can be set to 'host' to match the host time zone, or an arbitrary time zone option from /usr/share/zoneinfo/zone.tab",
      "format": "pve-ct-timezone",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tty": {
      "default": 2,
      "description": "Specify the number of tty available to the container",
      "maximum": 6,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 6)"
    },
    "unique": {
      "description": "Assign a unique random ethernet address.",
      "optional": 1,
      "requires": "restore",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "unprivileged": {
      "default": 0,
      "description": "Makes the container run as unprivileged user. For creation, the default is 1. For restore, the default is the value from the backup. (Should not be modified manually.)",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "unused[n]": {
      "description": "Reference to unused volumes. This is used internally, and should not be modified manually.",
      "format": {
        "volume": {
          "default_key": 1,
          "description": "The volume that is not used currently.",
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
      "description": "The (unique) ID of the VM.",
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
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc)。
