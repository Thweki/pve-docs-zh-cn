# `/nodes/{node}/qemu`

原始接口路径：`/nodes/{node}/qemu`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## GET `/nodes/{node}/qemu`

虚拟机索引（每个节点）。

**方法标识：** `vmlist`

**权限**

```json
{
  "description": "仅列出您对 /vms/<vmid> 具有 VM.Audit 权限的虚拟机。",
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
| `full` | boolean | 否 | — | 确定活动虚拟机的完整状态。 |
| `node` | string | 是 | — | 集群节点名称。 |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "full": {
      "description": "确定活动虚拟机的完整状态。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "node": {
      "description": "集群节点名称。",
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
        "description": "当前 CPU 使用率。",
        "optional": 1,
        "type": "number"
      },
      "cpus": {
        "description": "最大可用 CPU 数量。",
        "optional": 1,
        "type": "number"
      },
      "diskread": {
        "description": "自客户机启动以来从其块设备读取的字节数。（注意：并非所有存储类型都提供此信息。）",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "diskwrite": {
        "description": "自客户机启动以来写入其块设备的字节数。（注意：并非所有存储类型都提供此信息。）",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "lock": {
        "description": "当前的配置锁（如有）。",
        "optional": 1,
        "type": "string"
      },
      "maxdisk": {
        "description": "根磁盘大小，单位为字节。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "maxmem": {
        "description": "最大内存，单位为字节。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "mem": {
        "description": "当前已用内存，单位为字节。不考虑内核同页合并（KSM）。如果 ballooning 信息可用，则使用该信息。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "memhost": {
        "description": "宿主机上的当前内存用量。不考虑内核同页合并（KSM）。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "name": {
        "description": "虚拟机的（主机）名称。",
        "optional": 1,
        "type": "string"
      },
      "netin": {
        "description": "自客户机启动以来通过网络向其发送的流量字节数。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "netout": {
        "description": "自客户机启动以来通过网络从其发送的流量字节数。",
        "optional": 1,
        "renderer": "bytes",
        "type": "integer"
      },
      "pid": {
        "description": "QEMU 进程的 PID（如果虚拟机正在运行）。",
        "optional": 1,
        "type": "integer"
      },
      "pressurecpufull": {
        "description": "过去 10 秒的 CPU Full 压力停滞平均值。",
        "optional": 1,
        "type": "number"
      },
      "pressurecpusome": {
        "description": "过去 10 秒的 CPU Some 压力停滞平均值。",
        "optional": 1,
        "type": "number"
      },
      "pressureiofull": {
        "description": "过去 10 秒的 IO Full 压力停滞平均值。",
        "optional": 1,
        "type": "number"
      },
      "pressureiosome": {
        "description": "过去 10 秒的 IO Some 压力停滞平均值。",
        "optional": 1,
        "type": "number"
      },
      "pressurememoryfull": {
        "description": "过去 10 秒的内存 Full 压力停滞平均值。",
        "optional": 1,
        "type": "number"
      },
      "pressurememorysome": {
        "description": "过去 10 秒的内存 Some 压力停滞平均值。",
        "optional": 1,
        "type": "number"
      },
      "qmpstatus": {
        "description": "'query-status' QMP 监视器命令报告的虚拟机运行状态。",
        "optional": 1,
        "type": "string"
      },
      "running-machine": {
        "description": "当前运行的机器类型（如果正在运行）。",
        "optional": 1,
        "type": "string"
      },
      "running-qemu": {
        "description": "虚拟机当前使用的 QEMU 版本（如果正在运行）。",
        "optional": 1,
        "type": "string"
      },
      "serial": {
        "description": "客户机配置了串行设备。",
        "optional": 1,
        "type": "boolean"
      },
      "status": {
        "description": "QEMU 进程状态。",
        "enum": [
          "stopped",
          "running"
        ],
        "type": "string"
      },
      "tags": {
        "description": "当前配置的标签（如有）",
        "optional": 1,
        "type": "string"
      },
      "template": {
        "default": 0,
        "description": "确定客户机是否为模板。",
        "optional": 1,
        "type": "boolean"
      },
      "uptime": {
        "description": "运行时间，单位为秒。",
        "optional": 1,
        "renderer": "duration",
        "type": "integer"
      },
      "vmid": {
        "description": "虚拟机的（唯一）ID。",
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

## POST `/nodes/{node}/qemu`

创建或恢复虚拟机。

**方法标识：** `create_vm`

**权限**

```json
{
  "description": "需要对 /vms/{vmid} 或虚拟机资源池 /pool/{pool}. 具有 'VM.Allocate' 权限。对于还原（'archive' 选项），如果虚拟机已经存在，则用户仅需具有 'VM.Backup' 权限。如果创建磁盘，需要对所有使用的存储具有 'Datastore.AllocateSpace' 权限。如果使用网桥/VLAN，需要对所有使用的网桥/VLAN 具有 'SDN.Use' 权限。",
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
| `acpi` | boolean | 否 | 1 | 启用/禁用 ACPI。 |
| `affinity` | string | 否 | — | 用于执行客户机进程的宿主机核心列表，例如：0,5,8-11 |
| `agent` | string | 否 | — | 启用/禁用与 QEMU Guest Agent 的通信及其属性。 |
| `allow-ksm` | boolean | 否 | 1 | 允许通过 KSM（内核同页合并）合并此客户机的内存页。 |
| `amd-sev` | string | 否 | — | AMD CPU 的安全加密虚拟化（SEV）功能 |
| `arch` | string | 否 | — | 虚拟处理器架构。默认为宿主机架构。；可选值：`x86_64`, `aarch64` |
| `archive` | string | 否 | — | 备份归档。可以是 .tar 或 .vma 文件的文件系统路径（使用 '-' 从 stdin 管道输入数据），或 Proxmox 存储备份卷标识符。 |
| `args` | string | 否 | — | 传递给 kvm 的任意参数，例如：<br><br>args: -no-reboot -smbios 'type=0,vendor=FOO'<br><br>注意：此选项仅供专家使用。<br> |
| `audio0` | string | 否 | — | 配置音频设备，与 QXL/Spice 配合使用很有用。 |
| `autostart` | boolean | 否 | 0 | 崩溃后自动重启（当前忽略）。 |
| `balloon` | integer | 否 | — | 虚拟机的目标 RAM 容量，单位为 MiB。默认启用 balloon 驱动，除非将此值显式设为零以禁用。 |
| `bios` | string | 否 | "seabios" | 选择 BIOS 实现。；可选值：`seabios`, `ovmf` |
| `boot` | string | 否 | — | 指定客户机启动顺序。请使用 'order=' 子属性，无键形式或 'legacy=' 的用法已弃用。 |
| `bootdisk` | string | 否 | — | 允许从指定磁盘启动。已弃用：请改用 'boot: order=foo;bar'。 |
| `bwlimit` | integer | 否 | "restore limit from datacenter or storage config" | 覆盖 I/O 带宽限制（KiB/s）。 |
| `cdrom` | string | 否 | — | 这是 -ide2 选项的别名 |
| `cicustom` | string | 否 | — | cloud-init：指定自定义文件，以替换启动时自动生成的文件。 |
| `cipassword` | string | 否 | — | cloud-init：要分配给用户的密码。通常不建议使用此项，请改用 SSH 密钥。另请注意，旧版 cloud-init 不支持哈希密码。 |
| `citype` | string | 否 | — | 指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。；可选值：`configdrive2`, `nocloud`, `opennebula` |
| `ciupgrade` | boolean | 否 | 1 | cloud-init：在首次启动后自动升级软件包。 |
| `ciuser` | string | 否 | — | cloud-init：要更改 SSH 密钥和密码的用户名，以替代镜像中配置的默认用户。 |
| `cores` | integer | 否 | 1 | 每个插槽的核心数。 |
| `cpu` | string | 否 | — | 模拟的 CPU 类型。 |
| `cpulimit` | number | 否 | 0 | CPU 使用量限制。<br><br>注意：如果计算机有 2 个 CPU，则 CPU 时间总量为 '2'。值 '0' 表示不限制 CPU。 |
| `cpuunits` | integer | 否 | "cgroup v1: 1024, cgroup v2: 100" | 虚拟机的 CPU 权重。内核公平调度器使用此参数。数值越大，此虚拟机获得的 CPU 时间越多。该数值相对于其他所有正在运行的虚拟机的权重而言。 |
| `description` | string | 否 | — | 虚拟机描述。显示在 Web 界面的虚拟机摘要中。作为注释保存在配置文件中。 |
| `efidisk0` | string | 否 | — | 配置用于存放 EFI 变量的磁盘。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。注意，此处忽略 SIZE_IN_GiB，转而将默认 EFI 变量复制到卷中。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。 |
| `force` | boolean | 否 | — | 允许覆盖现有虚拟机。 |
| `freeze` | boolean | 否 | — | 启动时冻结 CPU（使用监视器命令 'c' 开始执行）。 |
| `ha-managed` | boolean | 否 | 0 | 创建后将虚拟机添加为 HA 资源。 |
| `hookscript` | string | 否 | — | 在虚拟机生命周期各个阶段执行的脚本。 |
| `hostpci[n]` | string | 否 | — | 将宿主机 PCI 设备映射到客户机。<br><br>注意：此选项允许直接访问宿主机硬件。因此将不再<br>能够迁移此类虚拟机——请格外谨慎。<br><br>警告：实验性功能！有用户报告此选项存在问题。<br> |
| `hotplug` | string | 否 | "network,disk,usb" | 选择性启用热插拔功能。支持的热插拔功能以逗号分隔：'network'、'disk'、'cpu'、'memory'、'usb' 和 'cloudinit'。使用 '0' 完全禁用热插拔。值 '1' 是默认值 `network,disk,usb` 的别名。USB 热插拔适用于机器版本 &gt;= 7.1 且 ostype 为 l26 或 windows &gt; 7 的客户机。 |
| `hugepages` | string | 否 | — | 启用大页内存。<br><br>设置大页大小，单位为 MiB。如果值为 'any'，则尽可能使用 1 GiB 大页，否则回退到 2 MiB。；可选值：`any`, `2`, `1024` |
| `ide[n]` | string | 否 | — | 将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。 |
| `import-working-storage` | string | 否 | — | 启用了 'images' 内容类型的文件型存储，用作导入期间的中间解压存储。默认为源存储。 |
| `intel-tdx` | string | 否 | — | Intel CPU 的可信域扩展（TDX）功能 |
| `ipconfig[n]` | string | 否 | — | cloud-init：为相应接口指定 IP 地址和网关。<br><br>IP 地址使用 CIDR 表示法，网关可选，但需要指定相同类型的 IP 地址。<br><br>IP 地址可使用特殊字符串 'dhcp' 以启用 DHCP，此时不应显式<br>提供网关。<br>对于 IPv6，可使用特殊字符串 'auto' 启用无状态自动配置。这需要<br>cloud-init 19.4 或更新版本。<br><br>如果启用了 cloud-init，但既未指定 IPv4 地址也未指定 IPv6 地址，则默认在<br>IPv4 上使用 DHCP。<br> |
| `ivshmem` | string | 否 | — | 虚拟机间共享内存。适用于虚拟机之间或与宿主机直接通信。 |
| `keephugepages` | boolean | 否 | 0 | 与大页一同使用。如果启用，虚拟机关闭后不会删除大页，可用于后续启动。 |
| `keyboard` | string | 否 | null | VNC 服务器的键盘布局。通常不需要此选项，一般在客户机操作系统内处理更好。；可选值：`de`, `de-ch`, `da`, `en-gb`, `en-us`, `es`, `fi`, `fr`, `fr-be`, `fr-ca`, `fr-ch`, `hu`, `is`, `it`, `ja`, `lt`, `mk`, `nl`, `no`, `pl`, `pt`, `pt-br`, `sv`, `sl`, `tr` |
| `kvm` | boolean | 否 | 1 | 启用/禁用 KVM 硬件虚拟化。 |
| `live-restore` | boolean | 否 | — | 立即启动虚拟机，同时在后台导入或还原。 |
| `localtime` | boolean | 否 | — | 将实时时钟（RTC）设为本地时间。如果 `ostype` 表明操作系统为 Microsoft Windows，则默认启用。 |
| `lock` | string | 否 | — | 锁定/解锁虚拟机。；可选值：`backup`, `clone`, `create`, `migrate`, `rollback`, `snapshot`, `snapshot-delete`, `suspending`, `suspended` |
| `machine` | string | 否 | — | 指定 QEMU 机器。 |
| `memory` | string | 否 | — | 内存属性。 |
| `migrate_downtime` | number | 否 | 0.1 | 设置迁移期间可容忍的最长停机时间（秒）。如果迁移在最后阶段因为需要传输的新脏 RAM 过多而无法收敛，则会逐步自动提高此限制，直到迁移可以收敛。上限为 2000 秒（QEMU 的最大值）。 |
| `migrate_speed` | integer | 否 | 0 | 设置迁移的最大速度（MB/s）。值 0 表示不限制。 |
| `name` | string | 否 | — | 为虚拟机设置名称。仅在配置 Web 界面中使用。 |
| `nameserver` | string | 否 | — | cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 均未设置，创建时将自动使用宿主机的设置。 |
| `net[n]` | string | 否 | — | 指定网络设备。 |
| `node` | string | 是 | — | 集群节点名称。 |
| `numa` | boolean | 否 | 0 | 启用/禁用 NUMA。 |
| `numa[n]` | string | 否 | — | NUMA 拓扑。 |
| `onboot` | boolean | 否 | 0 | 指定虚拟机是否在系统启动时启动。 |
| `ostype` | string | 否 | "other" | 指定客户机操作系统。用于为特定操作系统启用专门的<br>优化/功能：<br><br>[horizontal]<br>other;; 未指定操作系统<br>wxp;; Microsoft Windows XP<br>w2k;; Microsoft Windows 2000<br>w2k3;; Microsoft Windows 2003<br>w2k8;; Microsoft Windows 2008<br>wvista;; Microsoft Windows Vista<br>win7;; Microsoft Windows 7<br>win8;; Microsoft Windows 8/2012/2012r2<br>win10;; Microsoft Windows 10/2016/2019<br>win11;; Microsoft Windows 11/2022/2025<br>l24;; Linux 2.4 内核<br>l26;; Linux 2.6 - 7.X 内核<br>solaris;; Solaris/OpenSolaris/OpenIndiania 内核<br>；可选值：`other`, `wxp`, `w2k`, `w2k3`, `w2k8`, `wvista`, `win7`, `win8`, `win10`, `win11`, `l24`, `l26`, `solaris` |
| `parallel[n]` | string | 否 | — | 映射宿主机并行设备（n 为 0 到 2）。<br><br>注意：此选项允许直接访问宿主机硬件。因此将无法再迁移此类<br>虚拟机——请格外谨慎。<br><br>警告：实验性功能！有用户报告此选项存在问题。<br> |
| `pool` | string | 否 | — | 将虚拟机添加到指定资源池。 |
| `protection` | boolean | 否 | 0 | 设置虚拟机的保护标志。这将禁用移除虚拟机和移除磁盘操作。 |
| `reboot` | boolean | 否 | 1 | 允许重启。如果设为 '0'，虚拟机将在重启时退出。 |
| `rng0` | string | 否 | — | 配置基于 VirtIO 的随机数生成器。 |
| `sata[n]` | string | 否 | — | 将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。 |
| `scsi[n]` | string | 否 | — | 将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。 |
| `scsihw` | string | 否 | "lsi" | SCSI 控制器型号；可选值：`lsi`, `lsi53c810`, `virtio-scsi-pci`, `virtio-scsi-single`, `megasas`, `pvscsi` |
| `searchdomain` | string | 否 | — | cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 均未设置，创建时将自动使用宿主机的设置。 |
| `serial[n]` | string | 否 | — | 在虚拟机内创建串行设备（n 为 0 到 3），并直通<br>宿主机串行设备（即 /dev/ttyS0），或在<br>宿主机侧创建 UNIX 套接字（使用 'qm terminal' 打开终端连接）。<br><br>注意：如果直通宿主机串行设备，将无法再迁移此类虚拟机——<br>请格外谨慎。<br><br>警告：实验性功能！有用户报告此选项存在问题。<br> |
| `shares` | integer | 否 | 1000 | 自动 ballooning 的内存份额。数值越大，此虚拟机获得的内存越多。数值相对于其他所有运行中虚拟机的权重而言。设为零可禁用自动 ballooning。自动 ballooning 由 pvestatd 执行。 |
| `smbios1` | string | 否 | — | 指定 SMBIOS type 1 字段。 |
| `smp` | integer | 否 | 1 | CPU 数量。请改用 -sockets 选项。 |
| `sockets` | integer | 否 | 1 | CPU 插槽数量。 |
| `spice_enhancements` | string | 否 | — | 配置 SPICE 的附加增强功能。 |
| `sshkeys` | string | 否 | — | cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。 |
| `start` | boolean | 否 | 0 | 成功创建后启动虚拟机。 |
| `startdate` | string | 否 | "now" | 设置实时时钟的初始日期。有效日期格式为：'now'、'2006-06-17T16:01:21' 或 '2006-06-17'。 |
| `startup` | string | 否 | — | 启动和关闭行为。Order 是非负数，定义总体启动顺序。关闭按相反顺序执行。另外可设置以秒为单位的 'up' 或 'down' 延迟，指定启动或停止下一个虚拟机前等待的时间。 |
| `storage` | string | 否 | — | 默认存储。 |
| `tablet` | boolean | 否 | 1 | 启用/禁用 USB 数位板设备。此设备通常用于在 VNC 中实现鼠标绝对定位。否则，鼠标会与普通 VNC 客户端失去同步。如果在一台宿主机上运行大量仅使用控制台的客户机，可考虑禁用此设备以减少上下文切换。如果使用 spice（`qm set &lt;vmid&gt; --vga qxl`），则默认关闭此项。 |
| `tags` | string | 否 | — | 虚拟机标签。此项仅为元信息。 |
| `tdf` | boolean | 否 | 0 | 启用/禁用时间漂移修正。 |
| `template` | boolean | 否 | 0 | 启用/禁用模板。 |
| `tpmstate0` | string | 否 | — | 配置用于存放 TPM 状态的磁盘。格式固定为 'raw'。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。注意，此处忽略 SIZE_IN_GiB，改用 4 MiB。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。 |
| `unique` | boolean | 否 | — | 分配唯一的随机以太网地址。 |
| `unused[n]` | string | 否 | — | 对未使用卷的引用。此项供内部使用，不应手动修改。 |
| `usb[n]` | string | 否 | — | 配置 USB 设备（n 为 0 到 4；对于机器版本 &gt;= 7.1 且 ostype 为 l26 或 windows &gt; 7 的客户机，n 最大可为 14）。 |
| `vcpus` | integer | 否 | 0 | 热插拔的 vcpu 数量。 |
| `vga` | string | 否 | — | 配置 VGA 硬件。如果要使用高分辨率模式（&gt;= 1280x1024x16），可能需要增大 vga 内存选项。从 QEMU 2.9 起，除使用 'cirrus' 的某些 Windows 版本（XP 及更早版本）外，所有操作系统类型的默认 VGA 显示类型均为 'std'。'qxl' 选项启用 SPICE 显示服务器。对于 win* 操作系统，可以选择所需的独立显示器数量，Linux 客户机可自行添加显示器。<br>也可以不使用任何显卡，而使用串行设备作为终端。 |
| `virtio[n]` | string | 否 | — | 将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。 |
| `virtiofs[n]` | string | 否 | — | 使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。 |
| `vmgenid` | string | 否 | "1 (autogenerated)" | 虚拟机生成 ID（vmgenid）设备向客户机操作系统提供一个 128 位整数标识符。这可在虚拟机以不同配置执行时（例如执行快照或从模板创建）通知客户机操作系统。客户机操作系统察觉变化后，即可相应地将其分布式数据库副本标记为脏、重新初始化随机数生成器等。<br>注意，只有通过 API/CLI 创建或更新方法操作时才会自动创建，手动编辑配置文件时不会。 |
| `vmid` | integer | 是 | — | 虚拟机的（唯一）ID。 |
| `vmstatestorage` | string | 否 | — | 虚拟机状态卷/文件的默认存储。 |
| `watchdog` | string | 否 | — | 创建虚拟硬件看门狗设备。一旦启用（由客户机操作），客户机内的代理必须定期轮询看门狗，否则看门狗将重置客户机（或执行指定的相应操作） |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "acpi": {
      "default": 1,
      "description": "启用/禁用 ACPI。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "affinity": {
      "description": "用于执行客户机进程的宿主机核心列表，例如：0,5,8-11",
      "format": "pve-cpuset",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "agent": {
      "description": "启用/禁用与 QEMU Guest Agent 的通信及其属性。",
      "format": {
        "enabled": {
          "default": 0,
          "default_key": 1,
          "description": "启用/禁用与虚拟机中运行的 QEMU Guest Agent（QGA）的通信。",
          "type": "boolean"
        },
        "freeze-fs": {
          "default": 1,
          "description": "通过 QGA 冻结客户机文件系统，以便在快照、备份、复制和克隆等操作中保持磁盘状态一致。",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "是否发出 guest-fsfreeze-freeze 和 guest-fsfreeze-thaw QEMU 客户机代理命令。在客户机配置中启用 QEMU Guest Agent 选项且代理在客户机内运行时，snapshot 模式备份、克隆、不含 RAM 的快照、从运行中的客户机导入磁盘以及复制操作，通常会发出 guest-fsfreeze-freeze 命令及相应的解冻命令。\n\n已弃用的 'freeze-fs-on-backup' 设置将作为此设置的别名处理。"
        },
        "freeze-fs-on-backup": {
          "alias": "freeze-fs"
        },
        "fstrim_cloned_disks": {
          "default": 0,
          "description": "移动磁盘或迁移虚拟机后运行 fstrim。",
          "optional": 1,
          "type": "boolean"
        },
        "guest-fsfreeze": {
          "alias": "freeze-fs"
        },
        "type": {
          "default": "virtio",
          "description": "选择代理类型",
          "enum": [
            "virtio",
            "isa"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]"
    },
    "allow-ksm": {
      "default": 1,
      "description": "允许通过 KSM（内核同页合并）合并此客户机的内存页。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "amd-sev": {
      "description": "AMD CPU 的安全加密虚拟化（SEV）功能",
      "format": "pve-qemu-sev-fmt",
      "optional": 1,
      "type": "string",
      "typetext": "[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]"
    },
    "arch": {
      "description": "虚拟处理器架构。默认为宿主机架构。",
      "enum": [
        "x86_64",
        "aarch64"
      ],
      "optional": 1,
      "type": "string"
    },
    "archive": {
      "description": "备份归档。可以是 .tar 或 .vma 文件的文件系统路径（使用 '-' 从 stdin 管道输入数据），或 Proxmox 存储备份卷标识符。",
      "maxLength": 255,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "args": {
      "description": "传递给 kvm 的任意参数。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>",
      "verbose_description": "传递给 kvm 的任意参数，例如：\n\nargs: -no-reboot -smbios 'type=0,vendor=FOO'\n\n注意：此选项仅供专家使用。\n"
    },
    "audio0": {
      "description": "配置音频设备，与 QXL/Spice 配合使用很有用。",
      "format": {
        "device": {
          "description": "配置音频设备。",
          "enum": [
            "ich9-intel-hda",
            "intel-hda",
            "AC97"
          ],
          "type": "string"
        },
        "driver": {
          "default": "spice",
          "description": "音频设备的驱动后端。",
          "enum": [
            "spice",
            "none"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]"
    },
    "autostart": {
      "default": 0,
      "description": "崩溃后自动重启（当前忽略）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "balloon": {
      "description": "虚拟机的目标 RAM 容量，单位为 MiB。默认启用 balloon 驱动，除非将此值显式设为零以禁用。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "bios": {
      "default": "seabios",
      "description": "选择 BIOS 实现。",
      "enum": [
        "seabios",
        "ovmf"
      ],
      "optional": 1,
      "type": "string"
    },
    "boot": {
      "description": "指定客户机启动顺序。请使用 'order=' 子属性，无键形式或 'legacy=' 的用法已弃用。",
      "format": "pve-qm-boot",
      "optional": 1,
      "type": "string",
      "typetext": "[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]"
    },
    "bootdisk": {
      "description": "允许从指定磁盘启动。已弃用：请改用 'boot: order=foo;bar'。",
      "format": "pve-qm-bootdisk",
      "optional": 1,
      "pattern": "(ide|sata|scsi|virtio)\\d+",
      "type": "string"
    },
    "bwlimit": {
      "default": "restore limit from datacenter or storage config",
      "description": "覆盖 I/O 带宽限制（KiB/s）。",
      "minimum": "0",
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "cdrom": {
      "description": "这是 -ide2 选项的别名",
      "format": "pve-qm-ide",
      "optional": 1,
      "type": "string",
      "typetext": "<volume>"
    },
    "cicustom": {
      "description": "cloud-init：指定自定义文件，以替换启动时自动生成的文件。",
      "format": "pve-qm-cicustom",
      "optional": 1,
      "type": "string",
      "typetext": "[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]"
    },
    "cipassword": {
      "description": "cloud-init：要分配给用户的密码。通常不建议使用此项，请改用 SSH 密钥。另请注意，旧版 cloud-init 不支持哈希密码。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "citype": {
      "description": "指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。",
      "enum": [
        "configdrive2",
        "nocloud",
        "opennebula"
      ],
      "optional": 1,
      "type": "string"
    },
    "ciupgrade": {
      "default": 1,
      "description": "cloud-init：在首次启动后自动升级软件包。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ciuser": {
      "description": "cloud-init：要更改 SSH 密钥和密码的用户名，以替代镜像中配置的默认用户。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "cores": {
      "default": 1,
      "description": "每个插槽的核心数。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "cpu": {
      "description": "模拟的 CPU 类型。",
      "format": "pve-vm-cpu-conf",
      "optional": 1,
      "type": "string",
      "typetext": "[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]"
    },
    "cpulimit": {
      "default": 0,
      "description": "CPU 使用量限制。",
      "maximum": 128,
      "minimum": 0,
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - 128)",
      "verbose_description": "CPU 使用量限制。\n\n注意：如果计算机有 2 个 CPU，则 CPU 时间总量为 '2'。值 '0' 表示不限制 CPU。"
    },
    "cpuunits": {
      "default": "cgroup v1: 1024, cgroup v2: 100",
      "description": "虚拟机的 CPU 权重，在 cgroup v2 中会限制到 [1, 10000] 范围内。",
      "maximum": 262144,
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - 262144)",
      "verbose_description": "虚拟机的 CPU 权重。内核公平调度器使用此参数。数值越大，此虚拟机获得的 CPU 时间越多。该数值相对于其他所有正在运行的虚拟机的权重而言。"
    },
    "description": {
      "description": "虚拟机描述。显示在 Web 界面的虚拟机摘要中。作为注释保存在配置文件中。",
      "maxLength": 8192,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "efidisk0": {
      "description": "配置用于存放 EFI 变量的磁盘。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。注意，此处忽略 SIZE_IN_GiB，转而将默认 EFI 变量复制到卷中。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。",
      "format": {
        "efitype": {
          "default": "2m",
          "description": "OVMF EFI 变量的大小和类型。'4m' 较新且推荐使用，也是 Secure Boot 所必需的。为向后兼容，未另行指定时使用 '2m'。对于 arch=aarch64（ARM）的虚拟机，此项被忽略。",
          "enum": [
            "2m",
            "4m"
          ],
          "optional": 1,
          "type": "string"
        },
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id-or-qm-path",
          "format_description": "volume",
          "type": "string"
        },
        "format": {
          "description": "驱动器底层文件的数据格式。",
          "enum": [
            "raw",
            "qcow",
            "qed",
            "qcow2",
            "vmdk",
            "cloop"
          ],
          "optional": 1,
          "type": "string"
        },
        "import-from": {
          "description": "创建新磁盘，并从此来源（卷 ID 或绝对路径）导入。指定绝对路径时，您需要自行确保导入期间没有其他进程正在使用源！",
          "format": "pve-volume-id-or-absolute-path",
          "format_description": "source volume",
          "optional": 1,
          "type": "string"
        },
        "ms-cert": {
          "default": "2011",
          "description": "信息性标记，指示 Proxmox VE 已注册的最新 Microsoft UEFI 证书版本。值 '2023k' 表示包含 'Microsoft UEFI CA 2023'、'Windows UEFI CA 2023' 和 'Microsoft Corporation KEK 2K CA 2023' 证书。值 '2023' 和 '2023w' 已弃用，仅用于兼容性。",
          "enum": [
            "2011",
            "2023",
            "2023w",
            "2023k"
          ],
          "optional": 1,
          "type": "string"
        },
        "pre-enrolled-keys": {
          "default": 0,
          "description": "与 'efitype=4m' 一同使用时，采用已注册发行版专用密钥和 Microsoft Standard 密钥的 EFI 变量模板。注意，这会默认启用 Secure Boot，但仍可在虚拟机内关闭。",
          "optional": 1,
          "type": "boolean"
        },
        "size": {
          "description": "磁盘大小。此项仅供参考，不产生实际影响。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "alias": "file"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]"
    },
    "force": {
      "description": "允许覆盖现有虚拟机。",
      "optional": 1,
      "requires": "archive",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "freeze": {
      "description": "启动时冻结 CPU（使用监视器命令 'c' 开始执行）。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ha-managed": {
      "default": 0,
      "description": "创建后将虚拟机添加为 HA 资源。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "hookscript": {
      "description": "在虚拟机生命周期各个阶段执行的脚本。",
      "format": "pve-volume-id",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "hostpci[n]": {
      "description": "将宿主机 PCI 设备映射到客户机。",
      "format": "pve-qm-hostpci",
      "optional": 1,
      "type": "string",
      "typetext": "[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]",
      "verbose_description": "将宿主机 PCI 设备映射到客户机。\n\n注意：此选项允许直接访问宿主机硬件。因此将不再\n能够迁移此类虚拟机——请格外谨慎。\n\n警告：实验性功能！有用户报告此选项存在问题。\n"
    },
    "hotplug": {
      "default": "network,disk,usb",
      "description": "选择性启用热插拔功能。支持的热插拔功能以逗号分隔：'network'、'disk'、'cpu'、'memory'、'usb' 和 'cloudinit'。使用 '0' 完全禁用热插拔。值 '1' 是默认值 `network,disk,usb` 的别名。USB 热插拔适用于机器版本 >= 7.1 且 ostype 为 l26 或 windows > 7 的客户机。",
      "format": "pve-hotplug-features",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "hugepages": {
      "description": "启用大页内存。\n\n设置大页大小，单位为 MiB。如果值为 'any'，则尽可能使用 1 GiB 大页，否则回退到 2 MiB。",
      "enum": [
        "any",
        "2",
        "1024"
      ],
      "optional": 1,
      "type": "string"
    },
    "ide[n]": {
      "description": "将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。",
      "format": {
        "aio": {
          "description": "使用的 AIO 类型。",
          "enum": [
            "native",
            "threads",
            "io_uring"
          ],
          "optional": 1,
          "type": "string"
        },
        "backup": {
          "description": "备份时是否包含此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "bps": {
          "description": "最大读/写速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_rd": {
          "description": "最大读取速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_rd_length": {
          "alias": "bps_rd_max_length"
        },
        "bps_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_wr": {
          "description": "最大写入速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_wr_length": {
          "alias": "bps_wr_max_length"
        },
        "bps_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "cache": {
          "description": "驱动器的缓存模式",
          "enum": [
            "none",
            "writethrough",
            "writeback",
            "unsafe",
            "directsync"
          ],
          "optional": 1,
          "type": "string"
        },
        "detect_zeroes": {
          "description": "控制是否检测并尝试优化零值写入。",
          "optional": 1,
          "type": "boolean"
        },
        "discard": {
          "description": "控制是否将 discard/trim 请求传递到底层存储。",
          "enum": [
            "ignore",
            "on"
          ],
          "optional": 1,
          "type": "string"
        },
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id-or-qm-path",
          "format_description": "volume",
          "type": "string"
        },
        "format": {
          "description": "驱动器底层文件的数据格式。",
          "enum": [
            "raw",
            "qcow",
            "qed",
            "qcow2",
            "vmdk",
            "cloop"
          ],
          "optional": 1,
          "type": "string"
        },
        "import-from": {
          "description": "创建新磁盘，并从此来源（卷 ID 或绝对路径）导入。指定绝对路径时，您需要自行确保导入期间没有其他进程正在使用源！",
          "format": "pve-volume-id-or-absolute-path",
          "format_description": "source volume",
          "optional": 1,
          "type": "string"
        },
        "iops": {
          "description": "最大读/写 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max": {
          "description": "最大不限速读/写 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_rd": {
          "description": "最大读取 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_length": {
          "alias": "iops_rd_max_length"
        },
        "iops_rd_max": {
          "description": "最大不限速读取 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_wr": {
          "description": "最大写入 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_length": {
          "alias": "iops_wr_max_length"
        },
        "iops_wr_max": {
          "description": "最大不限速写入 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "mbps": {
          "description": "最大读/写速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_max": {
          "description": "最大不限速读/写池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd": {
          "description": "最大读取速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd_max": {
          "description": "最大不限速读取池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr": {
          "description": "最大写入速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr_max": {
          "description": "最大不限速写入池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "media": {
          "default": "disk",
          "description": "驱动器的介质类型。",
          "enum": [
            "cdrom",
            "disk"
          ],
          "optional": 1,
          "type": "string"
        },
        "model": {
          "description": "驱动器报告的型号名称，采用 URL 编码，最长 40 字节。",
          "format": "urlencoded",
          "format_description": "model",
          "maxLength": 120,
          "optional": 1,
          "type": "string"
        },
        "replicate": {
          "default": 1,
          "description": "是否在复制任务中考虑此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "rerror": {
          "description": "读取错误时的操作。",
          "enum": [
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "serial": {
          "description": "驱动器报告的序列号，采用 URL 编码，最长 20 字节。",
          "format": "urlencoded",
          "format_description": "serial",
          "maxLength": 60,
          "optional": 1,
          "type": "string"
        },
        "shared": {
          "default": 0,
          "description": "将此本地管理的卷标记为在所有节点上可用",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此本地管理的卷标记为在所有节点上可用。\n\n警告：此选项不会自动共享该卷，而是假定它已共享！"
        },
        "size": {
          "description": "磁盘大小。此项仅供参考，不产生实际影响。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "snapshot": {
          "description": "控制 qemu 的快照模式功能。如果启用，对磁盘的更改将是临时的，并会在虚拟机关闭时丢弃。",
          "optional": 1,
          "type": "boolean"
        },
        "ssd": {
          "description": "是否将此驱动器呈现为 SSD，而非旋转式硬盘。",
          "optional": 1,
          "type": "boolean"
        },
        "volume": {
          "alias": "file"
        },
        "werror": {
          "description": "写入错误时的操作。",
          "enum": [
            "enospc",
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "wwn": {
          "description": "驱动器的全球名称，编码为带 '0x' 前缀的 16 字节十六进制字符串。",
          "format_description": "wwn",
          "optional": 1,
          "pattern": "(?^:^(0x)[0-9a-fA-F]{16})",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]"
    },
    "import-working-storage": {
      "description": "启用了 'images' 内容类型的文件型存储，用作导入期间的中间解压存储。默认为源存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "intel-tdx": {
      "description": "Intel CPU 的可信域扩展（TDX）功能",
      "format": "pve-qemu-tdx-fmt",
      "optional": 1,
      "type": "string",
      "typetext": "[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]"
    },
    "ipconfig[n]": {
      "description": "cloud-init：为相应接口指定 IP 地址和网关。\n\nIP 地址使用 CIDR 表示法，网关可选，但需要指定相同类型的 IP 地址。\n\nIP 地址可使用特殊字符串 'dhcp' 以启用 DHCP，此时不应显式\n提供网关。\n对于 IPv6，可使用特殊字符串 'auto' 启用无状态自动配置。这需要\ncloud-init 19.4 或更新版本。\n\n如果启用了 cloud-init，但既未指定 IPv4 地址也未指定 IPv6 地址，则默认在\nIPv4 上使用 DHCP。\n",
      "format": "pve-qm-ipconfig",
      "optional": 1,
      "type": "string",
      "typetext": "[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]"
    },
    "ivshmem": {
      "description": "虚拟机间共享内存。适用于虚拟机之间或与宿主机直接通信。",
      "format": {
        "name": {
          "description": "文件名。将添加 'pve-shm-' 前缀。默认为 VMID。虚拟机停止时将删除此文件。",
          "format_description": "string",
          "optional": 1,
          "pattern": "[a-zA-Z0-9\\-]+",
          "type": "string"
        },
        "size": {
          "description": "文件大小，单位为 MB。",
          "minimum": 1,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "size=<integer> [,name=<string>]"
    },
    "keephugepages": {
      "default": 0,
      "description": "与大页一同使用。如果启用，虚拟机关闭后不会删除大页，可用于后续启动。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "keyboard": {
      "default": null,
      "description": "VNC 服务器的键盘布局。通常不需要此选项，一般在客户机操作系统内处理更好。",
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
    "kvm": {
      "default": 1,
      "description": "启用/禁用 KVM 硬件虚拟化。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "live-restore": {
      "description": "立即启动虚拟机，同时在后台导入或还原。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "localtime": {
      "description": "将实时时钟（RTC）设为本地时间。如果 `ostype` 表明操作系统为 Microsoft Windows，则默认启用。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "lock": {
      "description": "锁定/解锁虚拟机。",
      "enum": [
        "backup",
        "clone",
        "create",
        "migrate",
        "rollback",
        "snapshot",
        "snapshot-delete",
        "suspending",
        "suspended"
      ],
      "optional": 1,
      "type": "string"
    },
    "machine": {
      "description": "指定 QEMU 机器。",
      "format": {
        "aw-bits": {
          "description": "指定 vIOMMU 地址空间的位宽。",
          "maximum": 64,
          "minimum": 32,
          "optional": 1,
          "type": "number",
          "verbose_description": "指定 vIOMMU 地址空间的位宽。\n\nIntel vIOMMU 支持 39 或 48 位，VirtIO vIOMMU 支持 32 到 64 位之间的任意位宽。"
        },
        "enable-s3": {
          "description": "启用 S3 电源状态。从机器类型 9.2+pve1 起默认为 false，此前为 true。",
          "optional": 1,
          "type": "boolean"
        },
        "enable-s4": {
          "description": "启用 S4 电源状态。从机器类型 9.2+pve1 起默认为 false，此前为 true。",
          "optional": 1,
          "type": "boolean"
        },
        "type": {
          "default_key": 1,
          "description": "指定 QEMU 机器类型。",
          "format_description": "machine type",
          "maxLength": 40,
          "optional": 1,
          "pattern": "(pc|pc(-i440fx)?-\\d+(\\.\\d+)+(\\+pve\\d+)?(\\.pxe)?|q35|pc-q35-\\d+(\\.\\d+)+(\\+pve\\d+)?(\\.pxe)?|virt(?:-\\d+(\\.\\d+)+)?(\\+pve\\d+)?)",
          "type": "string"
        },
        "viommu": {
          "description": "启用并设置客户机 vIOMMU 变体（Intel vIOMMU 需要将机器类型设为 q35）。",
          "enum": [
            "intel",
            "virtio"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]"
    },
    "memory": {
      "description": "内存属性。",
      "format": {
        "current": {
          "default": 512,
          "default_key": 1,
          "description": "虚拟机当前在线 RAM 容量，单位为 MiB。使用 balloon 设备时，这是最大可用内存。",
          "minimum": 16,
          "type": "integer"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[current=]<integer>"
    },
    "migrate_downtime": {
      "default": 0.1,
      "description": "设置迁移期间可容忍的最长停机时间（秒）。如果迁移在最后阶段因为需要传输的新脏 RAM 过多而无法收敛，则会逐步自动提高此限制，直到迁移可以收敛。上限为 2000 秒（QEMU 的最大值）。",
      "minimum": 0,
      "optional": 1,
      "type": "number",
      "typetext": "<number> (0 - N)"
    },
    "migrate_speed": {
      "default": 0,
      "description": "设置迁移的最大速度（MB/s）。值 0 表示不限制。",
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - N)"
    },
    "name": {
      "description": "为虚拟机设置名称。仅在配置 Web 界面中使用。",
      "format": "dns-name",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "nameserver": {
      "description": "cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 均未设置，创建时将自动使用宿主机的设置。",
      "format": "address-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "net[n]": {
      "description": "指定网络设备。",
      "format": {
        "bridge": {
          "description": "网络设备要连接的网桥。Proxmox VE 的标准网桥\n名为 'vmbr0'。\n\n如果未指定网桥，将创建一个 kvm 用户模式（NAT）网络\n设备，提供 DHCP 和 DNS 服务。使用以下地址\n：\n\n 10.0.2.2   网关\n 10.0.2.3   DNS 服务器\n 10.0.2.4   SMB 服务器\n\nDHCP 服务器从 10.0.2.15 开始向客户机分配地址。\n",
          "format": "pve-bridge-id",
          "format_description": "bridge",
          "optional": 1,
          "type": "string"
        },
        "e1000": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "e1000-82540em": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "e1000-82544gc": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "e1000-82545em": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "e1000e": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "firewall": {
          "description": "是否应通过防火墙保护此接口。",
          "optional": 1,
          "type": "boolean"
        },
        "host-tunnel": {
          "description": "启用宿主机通过 UDP 隧道卸载 GSO。（仅适用于 VirtIO）。",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "启用宿主机通过 UDP 隧道卸载 GSO（仅适用于 VirtIO）。需要 QEMU > 10.2 以及客户机和宿主机内核支持。从机器版本 11.0+pve1 起默认禁用，以规避客户机内核中 virtio-net 驱动的问题。机器版本 10.2 和 11.0 默认启用。"
        },
        "i82551": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "i82557b": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "i82559er": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "link_down": {
          "description": "是否断开此接口的连接（如同拔掉网线）。",
          "optional": 1,
          "type": "boolean"
        },
        "macaddr": {
          "description": "MAC 地址。此地址必须在网络中唯一。如果未指定，将自动生成。",
          "format": "mac-addr",
          "format_description": "XX:XX:XX:XX:XX:XX",
          "optional": 1,
          "type": "string",
          "verbose_description": "未设置 I/G（个体/组）位的普通 MAC 地址。"
        },
        "model": {
          "default_key": 1,
          "description": "网卡型号。'virtio' 型号提供最佳性能，CPU 开销很低。如果客户机不支持此驱动，通常最好使用 'e1000'。",
          "enum": [
            "e1000",
            "e1000-82540em",
            "e1000-82544gc",
            "e1000-82545em",
            "e1000e",
            "i82551",
            "i82557b",
            "i82559er",
            "ne2k_isa",
            "ne2k_pci",
            "pcnet",
            "rtl8139",
            "virtio",
            "vmxnet3"
          ],
          "type": "string"
        },
        "mtu": {
          "description": "强制指定网络设备的 MTU（仅适用于 VirtIO）。设为 '1' 或留空将使用网桥 MTU",
          "maximum": 65520,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "ne2k_isa": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "ne2k_pci": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "pcnet": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "queues": {
          "description": "设备使用的数据包队列数量。",
          "maximum": 64,
          "minimum": 0,
          "optional": 1,
          "type": "integer"
        },
        "rate": {
          "description": "速率限制，单位为 mbps（每秒兆字节），使用浮点数表示。",
          "minimum": 0,
          "optional": 1,
          "type": "number"
        },
        "rtl8139": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "tag": {
          "description": "应用到此接口数据包的 VLAN 标签。",
          "maximum": 4094,
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "trunks": {
          "description": "通过此接口的 VLAN 中继。",
          "format_description": "vlanid[;vlanid...]",
          "optional": 1,
          "pattern": "(?^:\\d+(?:-\\d+)?(?:;\\d+(?:-\\d+)?)*)",
          "type": "string"
        },
        "virtio": {
          "alias": "macaddr",
          "keyAlias": "model"
        },
        "vmxnet3": {
          "alias": "macaddr",
          "keyAlias": "model"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]"
    },
    "node": {
      "description": "集群节点名称。",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "numa": {
      "default": 0,
      "description": "启用/禁用 NUMA。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "numa[n]": {
      "description": "NUMA 拓扑。",
      "format": {
        "cpus": {
          "description": "访问此 NUMA 节点的 CPU。",
          "format_description": "id[-id];...",
          "pattern": "(?^:\\d+(?:-\\d+)?(?:;\\d+(?:-\\d+)?)*)",
          "type": "string"
        },
        "hostnodes": {
          "description": "要使用的宿主机 NUMA 节点。",
          "format_description": "id[-id];...",
          "optional": 1,
          "pattern": "(?^:\\d+(?:-\\d+)?(?:;\\d+(?:-\\d+)?)*)",
          "type": "string"
        },
        "memory": {
          "description": "此 NUMA 节点提供的内存容量。",
          "optional": 1,
          "type": "number"
        },
        "policy": {
          "description": "NUMA 分配策略。",
          "enum": [
            "preferred",
            "bind",
            "interleave"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]"
    },
    "onboot": {
      "default": 0,
      "description": "指定虚拟机是否在系统启动时启动。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "ostype": {
      "default": "other",
      "description": "指定客户机操作系统。",
      "enum": [
        "other",
        "wxp",
        "w2k",
        "w2k3",
        "w2k8",
        "wvista",
        "win7",
        "win8",
        "win10",
        "win11",
        "l24",
        "l26",
        "solaris"
      ],
      "optional": 1,
      "type": "string",
      "verbose_description": "指定客户机操作系统。用于为特定操作系统启用专门的\n优化/功能：\n\n[horizontal]\nother;; 未指定操作系统\nwxp;; Microsoft Windows XP\nw2k;; Microsoft Windows 2000\nw2k3;; Microsoft Windows 2003\nw2k8;; Microsoft Windows 2008\nwvista;; Microsoft Windows Vista\nwin7;; Microsoft Windows 7\nwin8;; Microsoft Windows 8/2012/2012r2\nwin10;; Microsoft Windows 10/2016/2019\nwin11;; Microsoft Windows 11/2022/2025\nl24;; Linux 2.4 内核\nl26;; Linux 2.6 - 7.X 内核\nsolaris;; Solaris/OpenSolaris/OpenIndiania 内核\n"
    },
    "parallel[n]": {
      "description": "映射宿主机并行设备（n 为 0 到 2）。",
      "optional": 1,
      "pattern": "/dev/parport\\d+|/dev/usb/lp\\d+",
      "type": "string",
      "verbose_description": "映射宿主机并行设备（n 为 0 到 2）。\n\n注意：此选项允许直接访问宿主机硬件。因此将无法再迁移此类\n虚拟机——请格外谨慎。\n\n警告：实验性功能！有用户报告此选项存在问题。\n"
    },
    "pool": {
      "description": "将虚拟机添加到指定资源池。",
      "format": "pve-poolid",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "protection": {
      "default": 0,
      "description": "设置虚拟机的保护标志。这将禁用移除虚拟机和移除磁盘操作。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "reboot": {
      "default": 1,
      "description": "允许重启。如果设为 '0'，虚拟机将在重启时退出。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "rng0": {
      "description": "配置基于 VirtIO 的随机数生成器。",
      "format": "pve-qm-rng",
      "optional": 1,
      "type": "string",
      "typetext": "[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]"
    },
    "sata[n]": {
      "description": "将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。",
      "format": {
        "aio": {
          "description": "使用的 AIO 类型。",
          "enum": [
            "native",
            "threads",
            "io_uring"
          ],
          "optional": 1,
          "type": "string"
        },
        "backup": {
          "description": "备份时是否包含此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "bps": {
          "description": "最大读/写速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_rd": {
          "description": "最大读取速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_rd_length": {
          "alias": "bps_rd_max_length"
        },
        "bps_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_wr": {
          "description": "最大写入速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_wr_length": {
          "alias": "bps_wr_max_length"
        },
        "bps_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "cache": {
          "description": "驱动器的缓存模式",
          "enum": [
            "none",
            "writethrough",
            "writeback",
            "unsafe",
            "directsync"
          ],
          "optional": 1,
          "type": "string"
        },
        "detect_zeroes": {
          "description": "控制是否检测并尝试优化零值写入。",
          "optional": 1,
          "type": "boolean"
        },
        "discard": {
          "description": "控制是否将 discard/trim 请求传递到底层存储。",
          "enum": [
            "ignore",
            "on"
          ],
          "optional": 1,
          "type": "string"
        },
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id-or-qm-path",
          "format_description": "volume",
          "type": "string"
        },
        "format": {
          "description": "驱动器底层文件的数据格式。",
          "enum": [
            "raw",
            "qcow",
            "qed",
            "qcow2",
            "vmdk",
            "cloop"
          ],
          "optional": 1,
          "type": "string"
        },
        "import-from": {
          "description": "创建新磁盘，并从此来源（卷 ID 或绝对路径）导入。指定绝对路径时，您需要自行确保导入期间没有其他进程正在使用源！",
          "format": "pve-volume-id-or-absolute-path",
          "format_description": "source volume",
          "optional": 1,
          "type": "string"
        },
        "iops": {
          "description": "最大读/写 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max": {
          "description": "最大不限速读/写 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_rd": {
          "description": "最大读取 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_length": {
          "alias": "iops_rd_max_length"
        },
        "iops_rd_max": {
          "description": "最大不限速读取 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_wr": {
          "description": "最大写入 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_length": {
          "alias": "iops_wr_max_length"
        },
        "iops_wr_max": {
          "description": "最大不限速写入 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "mbps": {
          "description": "最大读/写速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_max": {
          "description": "最大不限速读/写池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd": {
          "description": "最大读取速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd_max": {
          "description": "最大不限速读取池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr": {
          "description": "最大写入速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr_max": {
          "description": "最大不限速写入池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "media": {
          "default": "disk",
          "description": "驱动器的介质类型。",
          "enum": [
            "cdrom",
            "disk"
          ],
          "optional": 1,
          "type": "string"
        },
        "replicate": {
          "default": 1,
          "description": "是否在复制任务中考虑此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "rerror": {
          "description": "读取错误时的操作。",
          "enum": [
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "serial": {
          "description": "驱动器报告的序列号，采用 URL 编码，最长 20 字节。",
          "format": "urlencoded",
          "format_description": "serial",
          "maxLength": 60,
          "optional": 1,
          "type": "string"
        },
        "shared": {
          "default": 0,
          "description": "将此本地管理的卷标记为在所有节点上可用",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此本地管理的卷标记为在所有节点上可用。\n\n警告：此选项不会自动共享该卷，而是假定它已共享！"
        },
        "size": {
          "description": "磁盘大小。此项仅供参考，不产生实际影响。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "snapshot": {
          "description": "控制 qemu 的快照模式功能。如果启用，对磁盘的更改将是临时的，并会在虚拟机关闭时丢弃。",
          "optional": 1,
          "type": "boolean"
        },
        "ssd": {
          "description": "是否将此驱动器呈现为 SSD，而非旋转式硬盘。",
          "optional": 1,
          "type": "boolean"
        },
        "volume": {
          "alias": "file"
        },
        "werror": {
          "description": "写入错误时的操作。",
          "enum": [
            "enospc",
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "wwn": {
          "description": "驱动器的全球名称，编码为带 '0x' 前缀的 16 字节十六进制字符串。",
          "format_description": "wwn",
          "optional": 1,
          "pattern": "(?^:^(0x)[0-9a-fA-F]{16})",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]"
    },
    "scsi[n]": {
      "description": "将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。",
      "format": {
        "aio": {
          "description": "使用的 AIO 类型。",
          "enum": [
            "native",
            "threads",
            "io_uring"
          ],
          "optional": 1,
          "type": "string"
        },
        "backup": {
          "description": "备份时是否包含此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "bps": {
          "description": "最大读/写速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_rd": {
          "description": "最大读取速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_rd_length": {
          "alias": "bps_rd_max_length"
        },
        "bps_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_wr": {
          "description": "最大写入速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_wr_length": {
          "alias": "bps_wr_max_length"
        },
        "bps_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "cache": {
          "description": "驱动器的缓存模式",
          "enum": [
            "none",
            "writethrough",
            "writeback",
            "unsafe",
            "directsync"
          ],
          "optional": 1,
          "type": "string"
        },
        "detect_zeroes": {
          "description": "控制是否检测并尝试优化零值写入。",
          "optional": 1,
          "type": "boolean"
        },
        "discard": {
          "description": "控制是否将 discard/trim 请求传递到底层存储。",
          "enum": [
            "ignore",
            "on"
          ],
          "optional": 1,
          "type": "string"
        },
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id-or-qm-path",
          "format_description": "volume",
          "type": "string"
        },
        "format": {
          "description": "驱动器底层文件的数据格式。",
          "enum": [
            "raw",
            "qcow",
            "qed",
            "qcow2",
            "vmdk",
            "cloop"
          ],
          "optional": 1,
          "type": "string"
        },
        "import-from": {
          "description": "创建新磁盘，并从此来源（卷 ID 或绝对路径）导入。指定绝对路径时，您需要自行确保导入期间没有其他进程正在使用源！",
          "format": "pve-volume-id-or-absolute-path",
          "format_description": "source volume",
          "optional": 1,
          "type": "string"
        },
        "iops": {
          "description": "最大读/写 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max": {
          "description": "最大不限速读/写 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_rd": {
          "description": "最大读取 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_length": {
          "alias": "iops_rd_max_length"
        },
        "iops_rd_max": {
          "description": "最大不限速读取 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_wr": {
          "description": "最大写入 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_length": {
          "alias": "iops_wr_max_length"
        },
        "iops_wr_max": {
          "description": "最大不限速写入 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iothread": {
          "description": "是否为此驱动器使用 iothreads",
          "optional": 1,
          "type": "boolean"
        },
        "mbps": {
          "description": "最大读/写速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_max": {
          "description": "最大不限速读/写池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd": {
          "description": "最大读取速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd_max": {
          "description": "最大不限速读取池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr": {
          "description": "最大写入速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr_max": {
          "description": "最大不限速写入池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "media": {
          "default": "disk",
          "description": "驱动器的介质类型。",
          "enum": [
            "cdrom",
            "disk"
          ],
          "optional": 1,
          "type": "string"
        },
        "product": {
          "description": "驱动器的产品名称，最长 16 字节。",
          "format_description": "product",
          "optional": 1,
          "pattern": "[A-Za-z0-9\\-_\\s]{,16}",
          "type": "string"
        },
        "queues": {
          "description": "队列数量。",
          "minimum": 2,
          "optional": 1,
          "type": "integer"
        },
        "replicate": {
          "default": 1,
          "description": "是否在复制任务中考虑此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "rerror": {
          "description": "读取错误时的操作。",
          "enum": [
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "ro": {
          "description": "驱动器是否为只读。",
          "optional": 1,
          "type": "boolean"
        },
        "scsiblock": {
          "default": 0,
          "description": "是否使用 scsi-block 完整直通宿主机块设备\n\n警告：宿主机内存不足或内存碎片严重时，可能导致 I/O 错误",
          "optional": 1,
          "type": "boolean"
        },
        "serial": {
          "description": "驱动器报告的序列号，采用 URL 编码，最长 20 字节。",
          "format": "urlencoded",
          "format_description": "serial",
          "maxLength": 60,
          "optional": 1,
          "type": "string"
        },
        "shared": {
          "default": 0,
          "description": "将此本地管理的卷标记为在所有节点上可用",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此本地管理的卷标记为在所有节点上可用。\n\n警告：此选项不会自动共享该卷，而是假定它已共享！"
        },
        "size": {
          "description": "磁盘大小。此项仅供参考，不产生实际影响。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "snapshot": {
          "description": "控制 qemu 的快照模式功能。如果启用，对磁盘的更改将是临时的，并会在虚拟机关闭时丢弃。",
          "optional": 1,
          "type": "boolean"
        },
        "ssd": {
          "description": "是否将此驱动器呈现为 SSD，而非旋转式硬盘。",
          "optional": 1,
          "type": "boolean"
        },
        "vendor": {
          "description": "驱动器的供应商名称，最长 8 字节。",
          "format_description": "vendor",
          "optional": 1,
          "pattern": "[A-Za-z0-9\\-_\\s]{,8}",
          "type": "string"
        },
        "volume": {
          "alias": "file"
        },
        "werror": {
          "description": "写入错误时的操作。",
          "enum": [
            "enospc",
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "wwn": {
          "description": "驱动器的全球名称，编码为带 '0x' 前缀的 16 字节十六进制字符串。",
          "format_description": "wwn",
          "optional": 1,
          "pattern": "(?^:^(0x)[0-9a-fA-F]{16})",
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]"
    },
    "scsihw": {
      "default": "lsi",
      "description": "SCSI 控制器型号",
      "enum": [
        "lsi",
        "lsi53c810",
        "virtio-scsi-pci",
        "virtio-scsi-single",
        "megasas",
        "pvscsi"
      ],
      "optional": 1,
      "type": "string"
    },
    "searchdomain": {
      "description": "cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 均未设置，创建时将自动使用宿主机的设置。",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "serial[n]": {
      "description": "在虚拟机内创建串行设备（n 为 0 到 3）",
      "optional": 1,
      "pattern": "(/dev/[^,]+|socket)",
      "type": "string",
      "verbose_description": "在虚拟机内创建串行设备（n 为 0 到 3），并直通\n宿主机串行设备（即 /dev/ttyS0），或在\n宿主机侧创建 UNIX 套接字（使用 'qm terminal' 打开终端连接）。\n\n注意：如果直通宿主机串行设备，将无法再迁移此类虚拟机——\n请格外谨慎。\n\n警告：实验性功能！有用户报告此选项存在问题。\n"
    },
    "shares": {
      "default": 1000,
      "description": "自动 ballooning 的内存份额。数值越大，此虚拟机获得的内存越多。数值相对于其他所有运行中虚拟机的权重而言。设为零可禁用自动 ballooning。自动 ballooning 由 pvestatd 执行。",
      "maximum": 50000,
      "minimum": 0,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (0 - 50000)"
    },
    "smbios1": {
      "description": "指定 SMBIOS type 1 字段。",
      "format": "pve-qm-smbios1",
      "maxLength": 512,
      "optional": 1,
      "type": "string",
      "typetext": "[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]"
    },
    "smp": {
      "default": 1,
      "description": "CPU 数量。请改用 -sockets 选项。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "sockets": {
      "default": 1,
      "description": "CPU 插槽数量。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "spice_enhancements": {
      "description": "配置 SPICE 的附加增强功能。",
      "format": {
        "foldersharing": {
          "default": "0",
          "description": "通过 SPICE 启用文件夹共享。需要在虚拟机中安装 Spice-WebDAV 守护进程。",
          "optional": 1,
          "type": "boolean"
        },
        "videostreaming": {
          "default": "off",
          "description": "启用视频流。对检测到的视频流使用压缩。",
          "enum": [
            "off",
            "all",
            "filter"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]"
    },
    "sshkeys": {
      "description": "cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。",
      "format": "urlencoded",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "start": {
      "default": 0,
      "description": "成功创建后启动虚拟机。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "startdate": {
      "default": "now",
      "description": "设置实时时钟的初始日期。有效日期格式为：'now'、'2006-06-17T16:01:21' 或 '2006-06-17'。",
      "optional": 1,
      "pattern": "(now|\\d{4}-\\d{1,2}-\\d{1,2}(T\\d{1,2}:\\d{1,2}:\\d{1,2})?)",
      "type": "string",
      "typetext": "(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)"
    },
    "startup": {
      "description": "启动和关闭行为。Order 是非负数，定义总体启动顺序。关闭按相反顺序执行。另外可设置以秒为单位的 'up' 或 'down' 延迟，指定启动或停止下一个虚拟机前等待的时间。",
      "format": "pve-startup-order",
      "optional": 1,
      "type": "string",
      "typetext": "[[order=]\\d+] [,up=\\d+] [,down=\\d+] "
    },
    "storage": {
      "description": "默认存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "tablet": {
      "default": 1,
      "description": "启用/禁用 USB 数位板设备。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>",
      "verbose_description": "启用/禁用 USB 数位板设备。此设备通常用于在 VNC 中实现鼠标绝对定位。否则，鼠标会与普通 VNC 客户端失去同步。如果在一台宿主机上运行大量仅使用控制台的客户机，可考虑禁用此设备以减少上下文切换。如果使用 spice（`qm set <vmid> --vga qxl`），则默认关闭此项。"
    },
    "tags": {
      "description": "虚拟机标签。此项仅为元信息。",
      "format": "pve-tag-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "tdf": {
      "default": 0,
      "description": "启用/禁用时间漂移修正。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "template": {
      "default": 0,
      "description": "启用/禁用模板。",
      "optional": 1,
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "tpmstate0": {
      "description": "配置用于存放 TPM 状态的磁盘。格式固定为 'raw'。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。注意，此处忽略 SIZE_IN_GiB，改用 4 MiB。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。",
      "format": {
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id-or-qm-path",
          "format_description": "volume",
          "type": "string"
        },
        "format": {
          "description": "镜像格式。",
          "enum": [
            "raw",
            "qcow2",
            "vmdk"
          ],
          "optional": 1,
          "type": "string"
        },
        "import-from": {
          "description": "创建新磁盘，并从此来源（卷 ID 或绝对路径）导入。指定绝对路径时，您需要自行确保导入期间没有其他进程正在使用源！",
          "format": "pve-volume-id-or-absolute-path",
          "format_description": "source volume",
          "optional": 1,
          "type": "string"
        },
        "size": {
          "description": "磁盘大小。此项仅供参考，不产生实际影响。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "version": {
          "default": "v1.2",
          "description": "TPM 接口版本。v2.0 较新，应优先使用。注意，此项以后无法更改。",
          "enum": [
            "v1.2",
            "v2.0"
          ],
          "optional": 1,
          "type": "string"
        },
        "volume": {
          "alias": "file"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]"
    },
    "unique": {
      "description": "分配唯一的随机以太网地址。",
      "optional": 1,
      "requires": "archive",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "unused[n]": {
      "description": "对未使用卷的引用。此项供内部使用，不应手动修改。",
      "format": {
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id",
          "format_description": "volume",
          "type": "string"
        },
        "volume": {
          "alias": "file"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume>"
    },
    "usb[n]": {
      "description": "配置 USB 设备（n 为 0 到 4；对于机器版本 >= 7.1 且 ostype 为 l26 或 windows > 7 的客户机，n 最大可为 14）。",
      "format": {
        "host": {
          "default_key": 1,
          "description": "宿主机 USB 设备、端口或值 'spice'。HOSTUSBDEVICE 语法如下：\n\n 'bus-port(.port)*'（十进制数），或\n 'vendor_id:product_id'（十六进制数），或\n 'spice'\n\n可使用 'lsusb -t' 命令列出现有 USB 设备。\n\n注意：此选项允许直接访问宿主机硬件。因此将无法再迁移此类\n虚拟机——请格外谨慎。\n\n值 'spice' 可用于为 spice 添加 USB 重定向设备。\n\n必须设置此项或 'mapping' 键。\n",
          "format_description": "HOSTUSBDEVICE|spice",
          "optional": 1,
          "pattern": "(?^:(?:(?:(?^:(0x)?([0-9A-Fa-f]{4}):(0x)?([0-9A-Fa-f]{4})))|(?:(?^:(\\d+)\\-(\\d+(\\.\\d+)*)))|[Ss][Pp][Ii][Cc][Ee]))",
          "type": "string"
        },
        "mapping": {
          "description": "集群范围映射的 ID。必须设置此项或默认键 'host'。",
          "format": "pve-configid",
          "format_description": "mapping-id",
          "optional": 1,
          "type": "string"
        },
        "usb3": {
          "default": 0,
          "description": "指定给定的 host 选项是否为 USB3 设备或端口。对于现代客户机（机器版本 >= 7.1，ostype 为 l26 和 windows > 7），此标志无关紧要（所有设备均接入 xhci 控制器）。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]"
    },
    "vcpus": {
      "default": 0,
      "description": "热插拔的 vcpu 数量。",
      "minimum": 1,
      "optional": 1,
      "type": "integer",
      "typetext": "<integer> (1 - N)"
    },
    "vga": {
      "description": "配置 VGA 硬件。",
      "format": {
        "clipboard": {
          "description": "启用特定剪贴板。未设置时，将根据显示类型添加 SPICE 剪贴板。QEMU 机器版本 < 10.1 时，无法使用 VNC 剪贴板进行在线迁移。",
          "enum": [
            "vnc"
          ],
          "optional": 1,
          "type": "string"
        },
        "memory": {
          "description": "设置 VGA 内存（MiB）。使用串行显示时无效。",
          "maximum": 512,
          "minimum": 4,
          "optional": 1,
          "type": "integer"
        },
        "type": {
          "default": "std",
          "default_key": 1,
          "description": "选择 VGA 类型。不建议使用 'cirrus' 类型。",
          "enum": [
            "cirrus",
            "qxl",
            "qxl2",
            "qxl3",
            "qxl4",
            "none",
            "serial0",
            "serial1",
            "serial2",
            "serial3",
            "std",
            "virtio",
            "virtio-gl",
            "vmware"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]",
      "verbose_description": "配置 VGA 硬件。如果要使用高分辨率模式（>= 1280x1024x16），可能需要增大 vga 内存选项。从 QEMU 2.9 起，除使用 'cirrus' 的某些 Windows 版本（XP 及更早版本）外，所有操作系统类型的默认 VGA 显示类型均为 'std'。'qxl' 选项启用 SPICE 显示服务器。对于 win* 操作系统，可以选择所需的独立显示器数量，Linux 客户机可自行添加显示器。\n也可以不使用任何显卡，而使用串行设备作为终端。"
    },
    "virtio[n]": {
      "description": "将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 分配新卷。使用 STORAGE_ID:0 和 'import-from' 参数从现有卷导入。",
      "format": {
        "aio": {
          "description": "使用的 AIO 类型。",
          "enum": [
            "native",
            "threads",
            "io_uring"
          ],
          "optional": 1,
          "type": "string"
        },
        "backup": {
          "description": "备份时是否包含此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "bps": {
          "description": "最大读/写速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_rd": {
          "description": "最大读取速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_rd_length": {
          "alias": "bps_rd_max_length"
        },
        "bps_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "bps_wr": {
          "description": "最大写入速度，单位为字节/秒。",
          "format_description": "bps",
          "optional": 1,
          "type": "integer"
        },
        "bps_wr_length": {
          "alias": "bps_wr_max_length"
        },
        "bps_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "cache": {
          "description": "驱动器的缓存模式",
          "enum": [
            "none",
            "writethrough",
            "writeback",
            "unsafe",
            "directsync"
          ],
          "optional": 1,
          "type": "string"
        },
        "detect_zeroes": {
          "description": "控制是否检测并尝试优化零值写入。",
          "optional": 1,
          "type": "boolean"
        },
        "discard": {
          "description": "控制是否将 discard/trim 请求传递到底层存储。",
          "enum": [
            "ignore",
            "on"
          ],
          "optional": 1,
          "type": "string"
        },
        "file": {
          "default_key": 1,
          "description": "驱动器的底层卷。",
          "format": "pve-volume-id-or-qm-path",
          "format_description": "volume",
          "type": "string"
        },
        "format": {
          "description": "驱动器底层文件的数据格式。",
          "enum": [
            "raw",
            "qcow",
            "qed",
            "qcow2",
            "vmdk",
            "cloop"
          ],
          "optional": 1,
          "type": "string"
        },
        "import-from": {
          "description": "创建新磁盘，并从此来源（卷 ID 或绝对路径）导入。指定绝对路径时，您需要自行确保导入期间没有其他进程正在使用源！",
          "format": "pve-volume-id-or-absolute-path",
          "format_description": "source volume",
          "optional": 1,
          "type": "string"
        },
        "iops": {
          "description": "最大读/写 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max": {
          "description": "最大不限速读/写 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_max_length": {
          "description": "I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_rd": {
          "description": "最大读取 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_length": {
          "alias": "iops_rd_max_length"
        },
        "iops_rd_max": {
          "description": "最大不限速读取 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_rd_max_length": {
          "description": "读取 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iops_wr": {
          "description": "最大写入 I/O，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_length": {
          "alias": "iops_wr_max_length"
        },
        "iops_wr_max": {
          "description": "最大不限速写入 I/O 池，单位为操作数/秒。",
          "format_description": "iops",
          "optional": 1,
          "type": "integer"
        },
        "iops_wr_max_length": {
          "description": "写入 I/O 突发的最长持续时间，单位为秒。",
          "format_description": "seconds",
          "minimum": 1,
          "optional": 1,
          "type": "integer"
        },
        "iothread": {
          "description": "是否为此驱动器使用 iothreads",
          "optional": 1,
          "type": "boolean"
        },
        "mbps": {
          "description": "最大读/写速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_max": {
          "description": "最大不限速读/写池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd": {
          "description": "最大读取速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_rd_max": {
          "description": "最大不限速读取池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr": {
          "description": "最大写入速度，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "mbps_wr_max": {
          "description": "最大不限速写入池，单位为兆字节/秒。",
          "format_description": "mbps",
          "optional": 1,
          "type": "number"
        },
        "media": {
          "default": "disk",
          "description": "驱动器的介质类型。",
          "enum": [
            "cdrom",
            "disk"
          ],
          "optional": 1,
          "type": "string"
        },
        "replicate": {
          "default": 1,
          "description": "是否在复制任务中考虑此驱动器。",
          "optional": 1,
          "type": "boolean"
        },
        "rerror": {
          "description": "读取错误时的操作。",
          "enum": [
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        },
        "ro": {
          "description": "驱动器是否为只读。",
          "optional": 1,
          "type": "boolean"
        },
        "serial": {
          "description": "驱动器报告的序列号，采用 URL 编码，最长 20 字节。",
          "format": "urlencoded",
          "format_description": "serial",
          "maxLength": 60,
          "optional": 1,
          "type": "string"
        },
        "shared": {
          "default": 0,
          "description": "将此本地管理的卷标记为在所有节点上可用",
          "optional": 1,
          "type": "boolean",
          "verbose_description": "将此本地管理的卷标记为在所有节点上可用。\n\n警告：此选项不会自动共享该卷，而是假定它已共享！"
        },
        "size": {
          "description": "磁盘大小。此项仅供参考，不产生实际影响。",
          "format": "disk-size",
          "format_description": "DiskSize",
          "optional": 1,
          "type": "string"
        },
        "snapshot": {
          "description": "控制 qemu 的快照模式功能。如果启用，对磁盘的更改将是临时的，并会在虚拟机关闭时丢弃。",
          "optional": 1,
          "type": "boolean"
        },
        "volume": {
          "alias": "file"
        },
        "werror": {
          "description": "写入错误时的操作。",
          "enum": [
            "enospc",
            "ignore",
            "report",
            "stop"
          ],
          "optional": 1,
          "type": "string"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]"
    },
    "virtiofs[n]": {
      "description": "使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。",
      "format": {
        "cache": {
          "default": "auto",
          "description": "文件系统应使用的缓存策略（auto、always、metadata、never）。",
          "enum": [
            "auto",
            "always",
            "metadata",
            "never"
          ],
          "optional": 1,
          "type": "string"
        },
        "direct-io": {
          "default": 0,
          "description": "遵循客户机应用程序传下来的 O_DIRECT 标志。",
          "optional": 1,
          "type": "boolean"
        },
        "dirid": {
          "default_key": 1,
          "description": "要与客户机共享的目录映射的映射标识符。也用作虚拟机内的挂载标签。",
          "format": "pve-configid",
          "format_description": "mapping-id",
          "type": "string"
        },
        "expose-acl": {
          "default": 0,
          "description": "为此挂载启用 POSIX ACL 支持（启用 ACL 会隐含启用 xattr）。",
          "optional": 1,
          "type": "boolean"
        },
        "expose-xattr": {
          "default": 0,
          "description": "为此挂载启用扩展属性支持。",
          "optional": 1,
          "type": "boolean"
        }
      },
      "optional": 1,
      "type": "string",
      "typetext": "[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]"
    },
    "vmgenid": {
      "default": "1 (autogenerated)",
      "description": "设置虚拟机生成 ID。使用 '1' 在创建或更新时自动生成，传入 '0' 显式禁用。",
      "format_description": "UUID",
      "optional": 1,
      "pattern": "(?:[a-fA-F0-9]{8}(?:-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}|[01])",
      "type": "string",
      "verbose_description": "虚拟机生成 ID（vmgenid）设备向客户机操作系统提供一个 128 位整数标识符。这可在虚拟机以不同配置执行时（例如执行快照或从模板创建）通知客户机操作系统。客户机操作系统察觉变化后，即可相应地将其分布式数据库副本标记为脏、重新初始化随机数生成器等。\n注意，只有通过 API/CLI 创建或更新方法操作时才会自动创建，手动编辑配置文件时不会。"
    },
    "vmid": {
      "description": "虚拟机的（唯一）ID。",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    },
    "vmstatestorage": {
      "description": "虚拟机状态卷/文件的默认存储。",
      "format": "pve-storage-id",
      "format_description": "storage ID",
      "optional": 1,
      "type": "string",
      "typetext": "<storage ID>"
    },
    "watchdog": {
      "description": "创建虚拟硬件看门狗设备。",
      "format": "pve-qm-watchdog",
      "optional": 1,
      "type": "string",
      "typetext": "[[model=]<i6300esb|ib700>] [,action=<enum>]",
      "verbose_description": "创建虚拟硬件看门狗设备。一旦启用（由客户机操作），客户机内的代理必须定期轮询看门狗，否则看门狗将重置客户机（或执行指定的相应操作）"
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

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/qemu)。
