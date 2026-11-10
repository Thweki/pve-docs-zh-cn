# pct.conf(5)

## 名称 <a href="#_name" id="_name"></a>

pct.conf - Proxmox VE 容器配置

## 概要 <a href="#_synopsis" id="_synopsis"></a>

`/etc/pve/lxc/<CTID>.conf`

## 描述 <a href="#_description" id="_description"></a>

`/etc/pve/lxc/<CTID>.conf` 文件存储容器配置，其中 `CTID` 是给定容器的数字 ID。

{% hint style="info" %}
ID < 100 保留供内部使用。
{% endhint %}

## 文件格式 <a href="#_file_format" id="_file_format"></a>

该文件采用简单的冒号分隔键/值格式。每行的格式如下：

```text
OPTION: value
```

文件中的空白行会被忽略，以 `#` 字符开头的行会被视为注释，同样会被忽略。

可以使用 `pct` 命令生成和修改这些文件。

也可以直接添加底层 LXC 风格配置，例如：

```text
lxc.init_cmd: /sbin/my_own_init
```

或

```text
lxc.init_cmd = /sbin/my_own_init
```

这些设置会直接传递给 LXC 底层工具。

## 选项 <a href="#_options" id="_options"></a>

**`arch`: `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>` (*默认 =* `amd64`)**

操作系统架构类型。

**`cmode`: `<console | shell | tty>` (*默认 =* `tty`)**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 *console* 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 *shell*，它只会在容器内调用一个 shell（无需登录）。

**`console`: `<boolean>` (*默认 =* `1`)**

将控制台设备（/dev/console）连接到容器。

**`cores`: `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`cpulimit`: `<number> (0 - 8192)` (*默认 =* `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 *2*。值 *0* 表示不限制 CPU。
{% endhint %}

**`cpuunits`: `<integer> (0 - 500000)` (*默认 =* `cgroup v1: 1024, cgroup v2: 100`)**

容器的 CPU 权重。该参数用于内核公平调度器。数值越大，该容器获得的 CPU 时间就越多。该数值是相对于所有其他正在运行的客户机的权重而言的。

**`debug`: `<boolean>` (*默认 =* `0`)**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`description`: `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`dev[n]`: `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`deny-write`=`<boolean>` (*默认 =* `0`)**

禁止容器写入设备

**`gid`=`<integer> (0 - N)`**

要分配给设备节点的组 ID

**`mode`=`<Octal access mode>`**

要设置在设备节点上的访问模式

**`path`=`<Path>`**

要直通到容器的设备路径

**`uid`=`<integer> (0 - N)`**

要分配给设备节点的用户 ID

**`entrypoint`: `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)` (*默认 =* `/sbin/init`)**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`env`: `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`features`: `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`force_rw_sys`=`<boolean>` (*默认 =* `0`)**

在非特权容器中将 /sys 挂载为 `rw`，而不是 `mixed`。在使用较新版本（>= v245）的 systemd-network 时，这可能会破坏网络。

**`fuse`=`<boolean>` (*默认 =* `0`)**

允许在容器中使用 *fuse* 文件系统。请注意，fuse 与 freezer cgroup 之间的交互可能导致 I/O 死锁。

**`keyctl`=`<boolean>` (*默认 =* `0`)**

仅限非特权容器：允许使用 keyctl() 系统调用。这是在容器内使用 docker 所必需的。默认情况下，非特权容器会将此系统调用视为不存在。这主要是针对 systemd-networkd 的变通方法，因为当某些 keyctl() 操作因权限不足被内核拒绝时，systemd-networkd 会将其视为致命错误。本质上，你可以在运行 systemd-networkd 和 docker 之间进行选择。

**`mknod`=`<boolean>` (*默认 =* `0`)**

允许非特权容器使用 mknod() 添加某些设备节点。这需要支持 seccomp 用户空间陷阱的内核（5.3 或更新版本）。这是实验性功能。

**`mount`=`<fstype;fstype;...>`**

允许挂载特定类型的文件系统。这应是 mount 命令所使用的文件系统类型列表。请注意，这可能对容器的安全产生负面影响。例如，如果能访问 loop 设备，挂载文件可以绕过 devices cgroup 的 mknod 权限；挂载 NFS 文件系统可能完全阻塞宿主机的 I/O，并使其无法重启，等等。

**`nesting`=`<boolean>` (*默认 =* `0`)**

允许嵌套。最好与具有额外 ID 映射的非特权容器一起使用。请注意，这会向客户机暴露宿主机的 procfs 和 sysfs 内容。systemd 隔离服务也需要此功能。

**`hookscript`: `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`hostname`: `<string>`**

为容器设置主机名。

**`lock`: `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`memory`: `<integer> (16 - N)` (*默认 =* `512`)**

容器的内存量，单位为 MB。

**`mp[n]`: `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE_ID:SIZE_IN_GiB 可分配新卷。

**`acl`=`<boolean>`**

显式启用或禁用 ACL 支持。

**`backup`=`<boolean>`**

是否将挂载点包含在备份中（仅用于卷挂载点）。

**`idmap`=`<type:container:disk:range-size[;type:container:disk:range-size;...]>`**

自定义 UID/GID 映射，针对此挂载点覆盖容器的 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。

`type` 对于 UID 为 `u`，对于 GID 为 `g`。

`container` 是容器内看到的第一个 ID。

`disk` 是底层文件系统上对应的第一个 ID。

`range-size` 是要映射的连续 ID 数量。

未映射的 ID 回退到容器的 `lxc.idmap`。

示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上由 UID 456 拥有的文件在容器内将显示为由 UID 123 拥有。

示例 2：`g:100:50:5` 映射 5 个连续的 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。

示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，这意味着容器内的 ID 将与磁盘上的 ID 一致。

**`keepattrs`=`<boolean>`（*默认 =* `0`）**

如果挂载点目录已存在，则继承该目录的 UID、GID 和访问模式。

**`mountoptions`=`<opt[;opt...]>`**

rootfs/mps 的额外挂载选项。

**`mp`=`<Path>`**

从容器内部看到的挂载点路径。

{% hint style="info" %}
出于安全原因，不得包含任何符号链接。
{% endhint %}

**`quota`=`<boolean>`**

启用容器内的用户配额（zfs 子卷不支持）

**`replicate`=`<boolean>`（*默认 =* `1`）**

会将此卷包含到存储复制作业中。

**`ro`=`<boolean>`**

只读挂载点

**`shared`=`<boolean>`（*默认 =* `0`）**

将此非卷挂载点标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享挂载点，它假定挂载点已被共享！
{% endhint %}

**`size`=`<DiskSize>`**

卷大小（只读值）。

**`volume`=`<volume>`**

要挂载到容器中的卷、设备或目录。

**`nameserver`: `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`net[n]`: `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`bridge`=`<bridge>`**

网络设备要连接到的网桥。

**`firewall`=`<boolean>`**

控制是否应使用此接口的防火墙规则。

**`gw`=`<GatewayIPv4>`**

IPv4 流量的默认网关。

**`gw6`=`<GatewayIPv6>`**

IPv6 流量的默认网关。

**`host-managed`=`<boolean>`**

此接口的 IP 配置是否应由宿主机管理。启用后，由宿主机（而非容器）负责该接口的 IP 配置。容器不应在此接口上运行自己的 DHCP 客户端或网络管理器。这对于缺少内部网络管理堆栈的容器（例如许多应用程序容器）非常有用。

**`hwaddr`=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`ip`=`<(IPv4/CIDR|dhcp|manual)>`**

CIDR 格式的 IPv4 地址。

**`ip6`=`<(IPv6/CIDR|auto|dhcp|manual)>`**

CIDR 格式的 IPv6 地址。

**`link_down`=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`mtu`=`<integer> (64 - 65535)`**

接口的最大传输单元。（lxc.network.mtu）

**`name`=`<string>`**

从容器内部看到的网络设备名称。（lxc.network.name）

**`rate`=`<mbps>`**

对接口应用速率限制

**`tag`=`<integer> (1 - 4094)`**

此接口的 VLAN 标签。

**`trunks`=`<vlanid[;vlanid...]>`**

允许通过此接口的 VLAN ID

**`type`=`<veth>`**

网络接口类型。

**`onboot`: `<boolean>` (*默认 =* `0`)**

指定容器是否在系统启动时启动。

**`ostype`: `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/<ostype>.common.conf 中的 lxc 设置脚本。可使用值 *unmanaged* 跳过特定于操作系统的设置。

**`protection`: `<boolean>` (*默认 =* `0`)**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`rootfs`: `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`acl`=`<boolean>`**

显式启用或禁用 ACL 支持。

**`idmap`=`<type:container:disk:range-size[;type:container:disk:range-size;...]>`**

自定义 UID/GID 映射，针对此挂载点覆盖容器的 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。

`type` 对于 UID 为 `u`，对于 GID 为 `g`。

`container` 是容器内看到的第一个 ID。

`disk` 是底层文件系统上对应的第一个 ID。

`range-size` 是要映射的连续 ID 数量。

未映射的 ID 回退到容器的 `lxc.idmap`。

示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上由 UID 456 拥有的文件在容器内将显示为由 UID 123 拥有。

示例 2：`g:100:50:5` 映射 5 个连续的 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。

示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，这意味着容器内的 ID 将与磁盘上的 ID 一致。

**`mountoptions`=`<opt[;opt...]>`**

rootfs/mps 的额外挂载选项。

**`quota`=`<boolean>`**

启用容器内的用户配额（zfs 子卷不支持）

**`replicate`=`<boolean>`（*默认 =* `1`）**

会将此卷包含到存储复制作业中。

**`ro`=`<boolean>`**

只读挂载点

**`shared`=`<boolean>`（*默认 =* `0`）**

将此非卷挂载点标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享挂载点，它假定挂载点已被共享！
{% endhint %}

**`size`=`<DiskSize>`**

卷大小（只读值）。

**`volume`=`<volume>`**

要挂载到容器中的卷、设备或目录。

**`searchdomain`: `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`startup`: `[[order=]\d+] [,up=\d+] [,down=\d+] `**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`swap`: `<integer> (0 - N)` (*默认 =* `512`)**

容器的 SWAP 大小，单位为 MB。

**`tags`: `<string>`**

容器的标签。这只是元信息。

**`template`: `<boolean>` (*默认 =* `0`)**

启用/禁用模板。

**`timezone`: `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 *host* 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`tty`: `<integer> (0 - 6)` (*默认 =* `2`)**

指定容器可用的 tty 数量

**`unprivileged`: `<boolean>` (*默认 =* `0`)**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`unused[n]`: `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`volume`=`<volume>`**

当前未使用的卷。

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pct.conf.5.html) · 版本 9.2.13 · 非官方中文翻译。
