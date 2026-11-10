# 22.11. **pct** \- Proxmox Container Toolkit <a href="#_strong_pct_strong_proxmox_container_toolkit" id="_strong_pct_strong_proxmox_container_toolkit"></a>

<a id="cli_pct"></a>



**pct** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pct_clone"></a>



**pct clone** `<vmid> <newid>` `[OPTIONS]`

创建容器克隆/副本

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<newid>`: `<integer> (100 - 999999999)`**

克隆的 VMID。

**`--bwlimit` `<number> (0 - N)` (*default \=* `clone limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--description` `<string>`**

新 CT 的描述。

**`--full` `<boolean>`**

创建所有磁盘的完整副本。克隆普通 CT 时始终会执行此操作。对于 CT 模板，默认会尝试创建链接克隆。

**`--hostname` `<string>`**

为新 CT 设置主机名。

**`--pool` `<string>`**

将新 CT 添加到指定池。

**`--snapname` `<string>`**

快照的名称。

**`--storage` `<storage ID>`**

完整克隆的目标存储。

**`--target` `<string>`**

目标节点。仅当原始 VM 位于共享存储上时才允许。

<a id="cli_pct_config"></a>



**pct config** `<vmid>` `[OPTIONS]`

获取容器配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--current` `<boolean>` (*default \=* `0`)**

获取当前值（而非待生效值）。

**`--snapshot` `<string>`**

从指定快照获取配置值。

<a id="cli_pct_console"></a>



**pct console** `<vmid>` `[OPTIONS]`

为指定容器启动控制台。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--escape` `\^?[a-z]` (*default \=* `^a`)**

转义序列前缀。例如，要将 \<Ctrl\+b q\> 用作转义序列，请传递 *^b*。

<a id="cli_pct_cpusets"></a>



**pct cpusets**

打印已分配的 CPU 集合列表。

<a id="cli_pct_create"></a>



**pct create** `<vmid> <ostemplate>` `[OPTIONS]`

创建或恢复容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<ostemplate>`: `<string>`**

操作系统模板或备份文件。

**`--arch` `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>` (*default \=* `amd64`)**

操作系统架构类型。

**`--bwlimit` `<number> (0 - N)` (*default \=* `restore limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cmode` `<console | shell | tty>` (*default \=* `tty`)**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 *console* 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 *shell*，它只会在容器内调用一个 shell（无需登录）。

**`--console` `<boolean>` (*default \=* `1`)**

将控制台设备（/dev/console）连接到容器。

**`--cores` `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`--cpulimit` `<number> (0 - 8192)` (*default \=* `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 *2*。值 *0* 表示不限制 CPU。
{% endhint %}

**`--cpuunits` `<integer> (0 - 500000)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

容器的 CPU 权重，在 cgroup v2 中会被限制在 \[1, 10000\] 范围内。

**`--debug` `<boolean>` (*default \=* `0`)**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`--description` `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`--dev[n]` `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`--entrypoint` `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)` (*default \=* `/sbin/init`)**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`--env` `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`--features` `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`--force` `<boolean>`**

允许覆盖现有容器。

**`--ha-managed` `<boolean>` (*default \=* `0`)**

创建后，将 CT 添加为 HA 资源。

**`--hookscript` `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`--hostname` `<string>`**

为容器设置主机名。

**`--ignore-unpack-errors` `<boolean>`**

提取模板时忽略错误。

**`--lock` `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`--memory` `<integer> (16 - N)` (*default \=* `512`)**

容器的内存量，单位为 MB。

**`--mp[n]` `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`--nameserver` `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--net[n]` `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`--onboot` `<boolean>` (*default \=* `0`)**

指定容器是否在系统启动时启动。

**`--ostype` `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 *unmanaged* 跳过特定于操作系统的设置。

**`--password` `<password>`**

设置容器内的 root 密码。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>` (*default \=* `0`)**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`--restore` `<boolean>`**

将其标记为恢复任务。

**`--rootfs` `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`--searchdomain` `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--ssh-public-keys` `<filepath>`**

设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--start` `<boolean>` (*default \=* `0`)**

成功完成创建后启动 CT。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>` (*default \=* `local`)**

默认存储。

**`--swap` `<integer> (0 - N)` (*default \=* `512`)**

容器的 SWAP 大小，单位为 MB。

**`--tags` `<string>`**

容器的标签。这只是元信息。

**`--template` `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`--timezone` `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 *host* 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`--tty` `<integer> (0 - 6)` (*default \=* `2`)**

指定容器可用的 tty 数量

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
需要选项：`restore`
{% endhint %}

**`--unprivileged` `<boolean>` (*default \=* `0`)**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`--unused[n]` `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

<a id="cli_pct_delsnapshot"></a>



**pct delsnapshot** `<vmid> <snapname>` `[OPTIONS]`

删除 LXC 快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--force` `<boolean>`**

即使删除磁盘快照失败，也从配置文件中移除。

<a id="cli_pct_destroy"></a>



**pct destroy** `<vmid>` `[OPTIONS]`

销毁容器（同时删除所有相关文件）。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--destroy-unreferenced-disks` `<boolean>`**

如果设置，还会从所有已启用的存储中销毁具有该 VMID 但未在配置中引用的所有磁盘。

**`--force` `<boolean>` (*default \=* `0`)**

强制销毁，即使正在运行。

**`--purge` `<boolean>` (*default \=* `0`)**

从所有相关配置中移除容器。例如，备份任务、复制任务或 HA。相关 ACL 和防火墙条目**始终**会被移除。

<a id="cli_pct_df"></a>



**pct df** `<vmid>`

获取容器当前的磁盘使用情况。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_enter"></a>



**pct enter** `<vmid>` `[OPTIONS]`

为指定的容器启动 shell。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--keep-env` `<boolean>` (*default \=* `1`)**

保留当前环境。在 PVE 9 中，此选项将默认禁用。如果您依赖保留的环境，请使用此选项，以确保与未来版本兼容。

<a id="cli_pct_exec"></a>



**pct exec** `<vmid> [<extra-args>]` `[OPTIONS]`

在指定的容器内启动命令。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--keep-env` `<boolean>` (*default \=* `1`)**

保留当前环境。在 PVE 9 中，此选项将默认禁用。如果您依赖保留的环境，请使用此选项，以确保与未来版本兼容。

<a id="cli_pct_fsck"></a>



**pct fsck** `<vmid>` `[OPTIONS]`

对容器卷运行文件系统检查（fsck）。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--device` `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs>`**

要对其运行文件系统检查的卷

**`--force` `<boolean>` (*default \=* `0`)**

即使文件系统看起来干净，也强制检查

<a id="cli_pct_fstrim"></a>



**pct fstrim** `<vmid>` `[OPTIONS]`

对选定的容器及其挂载点运行 fstrim，绑定挂载点或只读挂载点除外。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--ignore-mountpoints` `<boolean>`**

跳过所有挂载点，仅对容器根目录执行 fstrim。

<a id="cli_pct_help"></a>



**pct help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pct_list"></a>



**pct list**

LXC 容器索引（按节点）。

<a id="cli_pct_listsnapshot"></a>



**pct listsnapshot** `<vmid>`

列出所有快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_migrate"></a>



**pct migrate** `<vmid> <target>` `[OPTIONS]`

将容器迁移到另一个节点。创建新的迁移任务。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target>`: `<string>`**

目标节点。

**`--bwlimit` `<number> (0 - N)` (*default \=* `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--online` `<boolean>`**

使用在线迁移。

**`--restart` `<boolean>`**

使用重启迁移

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

**`--timeout` `<integer>` (*default \=* `180`)**

重启迁移时等待关机的超时时间（秒）

<a id="cli_pct_mount"></a>



**pct mount** `<vmid>`

将容器的文件系统挂载到宿主机。这会锁定容器，仅用于紧急维护，因为除了启动和停止之外，它将阻止对容器执行其他操作。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_move-volume"></a>



**pct move-volume** `<vmid> <volume> [<storage>] [<target-vmid>] [<target-volume>]` `[OPTIONS]`

将 rootfs-/mp-volume 移动到其他存储或其他容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<volume>`: `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99>`**

将被移动的卷。

**`<storage>`: `<storage ID>`**

目标存储。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-volume>`: `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99>`**

卷将移动到的配置键。默认为源卷的配置键。

**`--bwlimit` `<number> (0 - N)` (*default \=* `clone limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (*default \=* `0`)**

成功复制后删除原始卷。默认情况下，原始卷会作为未使用的卷条目保留。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--target-digest` `<string>`**

如果目标容器的当前配置文件具有不同的 SHA1 摘要，则阻止更改。这可用于防止并发修改。

<a id="cli_pct_move_volume"></a>



**pct move\_volume**

*pct move-volume* 的别名。

<a id="cli_pct_pending"></a>



**pct pending** `<vmid>`

获取容器配置，包括待处理的更改。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_pull"></a>



**pct pull** `<vmid> <path> <destination>` `[OPTIONS]`

将文件从容器复制到本地系统。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<path>`: `<string>`**

要提取的容器内文件的路径。

**`<destination>`: `<string>`**

目标位置

**`--group` `<string>`**

属组名称或 ID。

**`--perms` `<string>`**

要使用的文件权限（默认为八进制，使用十六进制时以 *0x* 为前缀）。

**`--user` `<string>`**

属主用户名或 ID。

<a id="cli_pct_push"></a>



**pct push** `<vmid> <file> <destination>` `[OPTIONS]`

将本地文件复制到容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<file>`: `<string>`**

本地文件的路径。

**`<destination>`: `<string>`**

要写入的容器内目标位置。

**`--group` `<string>`**

属组名称或 ID。使用名称时，该名称必须存在于容器内。

**`--perms` `<string>`**

要使用的文件权限（默认为八进制，使用十六进制时以 *0x* 为前缀）。

**`--user` `<string>`**

属主用户名或 ID。使用名称时，该名称必须存在于容器内。

<a id="cli_pct_reboot"></a>



**pct reboot** `<vmid>` `[OPTIONS]`

通过关机并重新启动来重启容器。应用待处理的更改。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒以完成关机。

<a id="cli_pct_remote-migrate"></a>



**pct remote-migrate** `<vmid> [<target-vmid>] <target-endpoint> --target-bridge <string> --target-storage <string>` `[OPTIONS]`

将容器迁移到远程集群。创建新的迁移任务。实验性功能！

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-endpoint>`: `apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]`**

远程目标端点

**`--bwlimit` `<integer> (0 - N)` (*default \=* `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (*default \=* `0`)**

成功迁移后删除原始 CT 及相关数据。默认情况下，原始 CT 会以停止状态保留在源集群上。

**`--online` `<boolean>`**

使用在线迁移。

**`--restart` `<boolean>`**

使用重启迁移

**`--target-bridge` `<string>`**

从源网桥到目标网桥的映射。仅提供一个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 *1* 会将每个源网桥映射到其自身。

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

**`--timeout` `<integer>` (*default \=* `180`)**

重启迁移时等待关机的超时时间（秒）

<a id="cli_pct_rescan"></a>



**pct rescan** `[OPTIONS]`

重新扫描所有存储，并更新磁盘大小和未使用的磁盘映像。

**`--dryrun` `<boolean>` (*default \=* `0`)**

不实际将更改写入配置。

**`--vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_resize"></a>



**pct resize** `<vmid> <disk> <size>` `[OPTIONS]`

调整容器挂载点的大小。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<mp0 | mp1 | mp10 | mp100 | mp101 | mp102 | mp103 | mp104 | mp105 | mp106 | mp107 | mp108 | mp109 | mp11 | mp110 | mp111 | mp112 | mp113 | mp114 | mp115 | mp116 | mp117 | mp118 | mp119 | mp12 | mp120 | mp121 | mp122 | mp123 | mp124 | mp125 | mp126 | mp127 | mp128 | mp129 | mp13 | mp130 | mp131 | mp132 | mp133 | mp134 | mp135 | mp136 | mp137 | mp138 | mp139 | mp14 | mp140 | mp141 | mp142 | mp143 | mp144 | mp145 | mp146 | mp147 | mp148 | mp149 | mp15 | mp150 | mp151 | mp152 | mp153 | mp154 | mp155 | mp156 | mp157 | mp158 | mp159 | mp16 | mp160 | mp161 | mp162 | mp163 | mp164 | mp165 | mp166 | mp167 | mp168 | mp169 | mp17 | mp170 | mp171 | mp172 | mp173 | mp174 | mp175 | mp176 | mp177 | mp178 | mp179 | mp18 | mp180 | mp181 | mp182 | mp183 | mp184 | mp185 | mp186 | mp187 | mp188 | mp189 | mp19 | mp190 | mp191 | mp192 | mp193 | mp194 | mp195 | mp196 | mp197 | mp198 | mp199 | mp2 | mp20 | mp200 | mp201 | mp202 | mp203 | mp204 | mp205 | mp206 | mp207 | mp208 | mp209 | mp21 | mp210 | mp211 | mp212 | mp213 | mp214 | mp215 | mp216 | mp217 | mp218 | mp219 | mp22 | mp220 | mp221 | mp222 | mp223 | mp224 | mp225 | mp226 | mp227 | mp228 | mp229 | mp23 | mp230 | mp231 | mp232 | mp233 | mp234 | mp235 | mp236 | mp237 | mp238 | mp239 | mp24 | mp240 | mp241 | mp242 | mp243 | mp244 | mp245 | mp246 | mp247 | mp248 | mp249 | mp25 | mp250 | mp251 | mp252 | mp253 | mp254 | mp255 | mp26 | mp27 | mp28 | mp29 | mp3 | mp30 | mp31 | mp32 | mp33 | mp34 | mp35 | mp36 | mp37 | mp38 | mp39 | mp4 | mp40 | mp41 | mp42 | mp43 | mp44 | mp45 | mp46 | mp47 | mp48 | mp49 | mp5 | mp50 | mp51 | mp52 | mp53 | mp54 | mp55 | mp56 | mp57 | mp58 | mp59 | mp6 | mp60 | mp61 | mp62 | mp63 | mp64 | mp65 | mp66 | mp67 | mp68 | mp69 | mp7 | mp70 | mp71 | mp72 | mp73 | mp74 | mp75 | mp76 | mp77 | mp78 | mp79 | mp8 | mp80 | mp81 | mp82 | mp83 | mp84 | mp85 | mp86 | mp87 | mp88 | mp89 | mp9 | mp90 | mp91 | mp92 | mp93 | mp94 | mp95 | mp96 | mp97 | mp98 | mp99 | rootfs>`**

要调整大小的磁盘。

**`<size>`: `\+?\d+(\.\d+)?[KMGT]?`**

新大小。带有 *\+* 符号时，该值会加到卷的实际大小上；不带该符号时，该值将被视为绝对大小。不支持缩小磁盘。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

<a id="cli_pct_restore"></a>



**pct restore** `<vmid> <ostemplate>` `[OPTIONS]`

创建或恢复容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<ostemplate>`: `<string>`**

操作系统模板或备份文件。

**`--arch` `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>` (*default \=* `amd64`)**

操作系统架构类型。

**`--bwlimit` `<number> (0 - N)` (*default \=* `restore limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cmode` `<console | shell | tty>` (*default \=* `tty`)**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 *console* 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 *shell*，它只会在容器内调用一个 shell（无需登录）。

**`--console` `<boolean>` (*default \=* `1`)**

将控制台设备（/dev/console）连接到容器。

**`--cores` `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`--cpulimit` `<number> (0 - 8192)` (*default \=* `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 *2*。值 *0* 表示不限制 CPU。
{% endhint %}

**`--cpuunits` `<integer> (0 - 500000)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

容器的 CPU 权重，在 cgroup v2 中会被限制在 \[1, 10000\] 范围内。

**`--debug` `<boolean>` (*default \=* `0`)**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`--description` `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`--dev[n]` `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`--entrypoint` `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)` (*default \=* `/sbin/init`)**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`--env` `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`--features` `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`--force` `<boolean>`**

允许覆盖现有容器。

**`--ha-managed` `<boolean>` (*default \=* `0`)**

创建后，将 CT 添加为 HA 资源。

**`--hookscript` `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`--hostname` `<string>`**

为容器设置主机名。

**`--ignore-unpack-errors` `<boolean>`**

提取模板时忽略错误。

**`--lock` `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`--memory` `<integer> (16 - N)` (*default \=* `512`)**

容器的内存量，单位为 MB。

**`--mp[n]` `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`--nameserver` `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--net[n]` `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`--onboot` `<boolean>` (*default \=* `0`)**

指定容器是否在系统启动时启动。

**`--ostype` `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 *unmanaged* 跳过特定于操作系统的设置。

**`--password` `<password>`**

设置容器内的 root 密码。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>` (*default \=* `0`)**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`--rootfs` `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`--searchdomain` `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--ssh-public-keys` `<filepath>`**

设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--start` `<boolean>` (*default \=* `0`)**

成功完成创建后启动 CT。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>` (*default \=* `local`)**

默认存储。

**`--swap` `<integer> (0 - N)` (*default \=* `512`)**

容器的 SWAP 大小，单位为 MB。

**`--tags` `<string>`**

容器的标签。这只是元信息。

**`--template` `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`--timezone` `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 *host* 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`--tty` `<integer> (0 - 6)` (*default \=* `2`)**

指定容器可用的 tty 数量

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
需要选项：`restore`
{% endhint %}

**`--unprivileged` `<boolean>` (*default \=* `0`)**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`--unused[n]` `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

<a id="cli_pct_resume"></a>



**pct resume** `<vmid>`

恢复容器运行。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_rollback"></a>



**pct rollback** `<vmid> <snapname>` `[OPTIONS]`

将 LXC 状态回滚到指定快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--start` `<boolean>` (*default \=* `0`)**

成功回滚后是否应启动容器

<a id="cli_pct_set"></a>



**pct set** `<vmid>` `[OPTIONS]`

设置容器选项。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--arch` `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>` (*default \=* `amd64`)**

操作系统架构类型。

**`--cmode` `<console | shell | tty>` (*default \=* `tty`)**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 *console* 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 *shell*，它只会在容器内调用一个 shell（无需登录）。

**`--console` `<boolean>` (*default \=* `1`)**

将控制台设备（/dev/console）连接到容器。

**`--cores` `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`--cpulimit` `<number> (0 - 8192)` (*default \=* `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 *2*。值 *0* 表示不限制 CPU。
{% endhint %}

**`--cpuunits` `<integer> (0 - 500000)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

容器的 CPU 权重，在 cgroup v2 中会被限制在 \[1, 10000\] 范围内。

**`--debug` `<boolean>` (*default \=* `0`)**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`--dev[n]` `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--entrypoint` `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)` (*default \=* `/sbin/init`)**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`--env` `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`--features` `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`--hookscript` `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`--hostname` `<string>`**

为容器设置主机名。

**`--lock` `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`--memory` `<integer> (16 - N)` (*default \=* `512`)**

容器的内存量，单位为 MB。

**`--mp[n]` `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`--nameserver` `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--net[n]` `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`--onboot` `<boolean>` (*default \=* `0`)**

指定容器是否在系统启动时启动。

**`--ostype` `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 *unmanaged* 跳过特定于操作系统的设置。

**`--protection` `<boolean>` (*default \=* `0`)**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`--revert` `<string>`**

撤销待处理的更改。

**`--rootfs` `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`--searchdomain` `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--swap` `<integer> (0 - N)` (*default \=* `512`)**

容器的 SWAP 大小，单位为 MB。

**`--tags` `<string>`**

容器的标签。这只是元信息。

**`--template` `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`--timezone` `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 *host* 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`--tty` `<integer> (0 - 6)` (*default \=* `2`)**

指定容器可用的 tty 数量

**`--unprivileged` `<boolean>` (*default \=* `0`)**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`--unused[n]` `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

<a id="cli_pct_shutdown"></a>



**pct shutdown** `<vmid>` `[OPTIONS]`

关闭容器。这会触发容器正常关机，详情请参阅 lxc-stop(1)。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--forceStop` `<boolean>` (*default \=* `0`)**

确保容器停止。

**`--timeout` `<integer> (0 - N)` (*default \=* `60`)**

最多等待 timeout 秒。

<a id="cli_pct_snapshot"></a>



**pct snapshot** `<vmid> <snapname>` `[OPTIONS]`

为容器创建快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--description` `<string>`**

文本描述或注释。

<a id="cli_pct_start"></a>



**pct start** `<vmid>` `[OPTIONS]`

启动容器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--debug` `<boolean>` (*default \=* `0`)**

如果设置，启动时会启用非常详细的调试日志级别。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_pct_status"></a>



**pct status** `<vmid>` `[OPTIONS]`

显示 CT 状态。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--verbose` `<boolean>`**

详细输出格式

<a id="cli_pct_stop"></a>



**pct stop** `<vmid>` `[OPTIONS]`

停止容器。这将突然终止容器中运行的所有进程。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--overrule-shutdown` `<boolean>` (*default \=* `0`)**

停止前尝试中止正在运行的 *vzshutdown* 任务。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_pct_suspend"></a>



**pct suspend** `<vmid>`

挂起容器。此功能处于实验阶段。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_template"></a>



**pct template** `<vmid>`

创建模板。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_unlock"></a>



**pct unlock** `<vmid>`

解锁 VM。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_pct_unmount"></a>



**pct unmount** `<vmid>`

卸载容器的文件系统。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
