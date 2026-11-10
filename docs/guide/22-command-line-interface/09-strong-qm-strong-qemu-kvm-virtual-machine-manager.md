# 22.9. **qm** \- QEMU/KVM 虚拟机管理器 <a href="#strong_qm_strong_qemu_kvm_virtual_machine_manager" id="strong_qm_strong_qemu_kvm_virtual_machine_manager"></a>

## **qm** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_qm" id="cli_qm"></a>

## **qm agent** <a href="#cli_qm_agent" id="cli_qm_agent"></a>

*qm guest cmd* 的别名。

## **qm cleanup** `<vmid> <clean-shutdown> <guest-requested>` <a href="#cli_qm_cleanup" id="cli_qm_cleanup"></a>

清理 tap 设备、vgpu 等资源。在虚拟机关机、崩溃等情况后调用。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<clean-shutdown>`: `<boolean>`**

表示 qemu 是否正常关闭。

**`<guest-requested>`: `<boolean>`**

表示关机是由客户机请求，还是通过 qmp 请求。

## **qm clone** `<vmid> <newid>` `[OPTIONS]` <a href="#cli_qm_clone" id="cli_qm_clone"></a>

创建虚拟机/模板的副本。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<newid>`: `<integer> (100 - 999999999)`**

克隆的 VMID。

**`--bwlimit` `<integer> (0 - N)` （*默认值 \=* `clone limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--description` `<string>`**

新虚拟机的描述。

**`--format` `<qcow2 | raw | vmdk>`**

目标磁盘格式。仅对完整克隆有效。如果目标存储不支持该格式，则改用存储的默认格式。

**`--full` `<boolean>`**

创建所有磁盘的完整副本。克隆普通虚拟机时始终执行此操作。对于虚拟机模板，默认尝试创建链接克隆。

**`--name` `<string>`**

设置新虚拟机的名称。

**`--pool` `<string>`**

将新虚拟机添加到指定资源池。

**`--snapname` `<string>`**

快照的名称。

**`--storage` `<storage ID>`**

完整克隆的目标存储。

**`--target` `<string>`**

目标节点。仅当原始 VM 位于共享存储上时才允许。

## **qm cloudinit dump** `<vmid> <type>` <a href="#cli_qm_cloudinit_dump" id="cli_qm_cloudinit_dump"></a>

获取自动生成的 cloudinit 配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<type>`: `<meta | network | user>`**

配置类型。

## **qm cloudinit pending** `<vmid>` <a href="#cli_qm_cloudinit_pending" id="cli_qm_cloudinit_pending"></a>

获取同时包含当前值和待应用值的 cloudinit 配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm cloudinit update** `<vmid>` <a href="#cli_qm_cloudinit_update" id="cli_qm_cloudinit_update"></a>

重新生成并更改 cloudinit 配置驱动器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm config** `<vmid>` `[OPTIONS]` <a href="#cli_qm_config" id="cli_qm_config"></a>

获取应用待定配置更改后的虚拟机配置。设置 *current* 参数可改为获取当前配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--current` `<boolean>`（*默认 \=* `0`）**

获取当前值（而非待生效值）。

**`--snapshot` `<string>`**

从指定快照获取配置值。

## **qm create** `<vmid>` `[OPTIONS]` <a href="#cli_qm_create" id="cli_qm_create"></a>

创建或恢复虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--acpi` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 ACPI。

**`--affinity` `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`--allow-ksm` `<boolean>` （*默认值 \=* `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`--arch` `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`--archive` `<string>`**

备份归档。可以是 .tar 或 .vma 文件的文件系统路径（使用 *\-* 从 stdin 通过管道传入数据），也可以是 proxmox 存储备份卷标识符。

**`--args` `<string>`**

传递给 kvm 的任意参数。

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`--autostart` `<boolean>` （*默认值 \=* `0`）**

崩溃后自动重启（目前被忽略）。

**`--balloon` `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`--bios` `<ovmf | seabios>` （*默认值 \=* `seabios`）**

选择 BIOS 实现。

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 *order\=* 子属性，因为不带键的用法或 *legacy\=* 已弃用。

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 *boot: order\=foo;bar*。

**`--bwlimit` `<integer> (0 - N)` （*默认值 \=* `restore limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cdrom` `<volume>`**

这是选项 -ide2 的别名

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`--cipassword` `<password>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`--citype` `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`--ciupgrade` `<boolean>` （*默认值 \=* `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`--ciuser` `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`--cores` `<integer> (1 - N)` （*默认值 \=* `1`）**

每个 CPU 插槽的核心数。

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`--cpulimit` `<number> (0 - 128)` （*默认值 \=* `0`）**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` （*默认值 \=* `cgroup v1: 1024, cgroup v2: 100`）**

虚拟机的 CPU 权重，在 cgroup v2 中限制为 \[1, 10000\]。

**`--description` `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是将默认 EFI 变量复制到该卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--force` `<boolean>`**

允许覆盖现有虚拟机。

{% hint style="info" %}
需要选项：`archive`
{% endhint %}

**`--freeze` `<boolean>`**

启动时冻结 CPU（使用 *c* 监视器命令开始执行）。

**`--ha-managed` `<boolean>`（*默认 \=* `0`）**

创建虚拟机后，将其添加为 HA 资源。

**`--hookscript` `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

**`--hotplug` `<string>` （*默认值 \=* `network,disk,usb`）**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：*network*、*disk*、*cpu*、*memory*、*usb* 和 *cloudinit*。使用 *0* 完全禁用热插拔。将 *1* 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`--hugepages` `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 *any*，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--import-working-storage` `<storage ID>`**

已启用 *images* 内容类型的文件存储，导入期间用作中间解压存储。默认为源存储。

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 *dhcp* 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 *auto* 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`--ivshmem` `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`--keephugepages` `<boolean>` （*默认值 \=* `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`--kvm` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 KVM 硬件虚拟化。

**`--live-restore` `<boolean>`**

立即启动虚拟机，同时在后台导入或恢复。

**`--localtime` `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--memory` `[current=]<integer>`**

内存属性。

**`--migrate_downtime` `<number> (0 - N)` （*默认值 \=* `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`--migrate_speed` `<integer> (0 - N)` （*默认值 \=* `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`--name` `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`--nameserver` `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`--numa` `<boolean>` （*默认值 \=* `0`）**

启用/禁用 NUMA。

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`--onboot` `<boolean>`（*默认 \=* `0`）**

指定是否在系统启动时启动虚拟机。

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` （*默认值 \=* `other`）**

指定客户机操作系统。

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>`（*默认 \=* `0`）**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`--reboot` `<boolean>` （*默认值 \=* `1`）**

允许重启。如果设为 *0*，虚拟机将在重启时退出。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` （*默认值 \=* `lsi`）**

SCSI 控制器型号

**`--searchdomain` `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--serial[n]` `(/dev/[^,]+|socket)`**

在虚拟机内创建串口设备（n 为 0 到 3）

**`--shares` `<integer> (0 - 50000)` （*默认值 \=* `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`--smp` `<integer> (1 - N)` （*默认值 \=* `1`）**

CPU 数量。请改用 -sockets 选项。

**`--sockets` `<integer> (1 - N)` （*默认值 \=* `1`）**

CPU 插槽数量。

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`--sshkeys` `<filepath>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--start` `<boolean>`（*默认 \=* `0`）**

成功创建后启动虚拟机。

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` （*默认值 \=* `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、*2006-06-17T16:01:21* 或 *2006-06-17*。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`**

默认存储。

**`--tablet` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 USB 数位板设备。

**`--tags` `<string>`**

虚拟机的标签。这只是元信息。

**`--tdf` `<boolean>` （*默认值 \=* `0`）**

启用/禁用时间漂移修正。

**`--template` `<boolean>`（*默认 \=* `0`）**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 *raw*。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是使用 4 MiB。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
需要选项：`archive`
{% endhint %}

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`--vcpus` `<integer> (1 - N)` （*默认值 \=* `0`）**

热插拔的 vcpu 数量。

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`--vmgenid` `<UUID>` （*默认值 \=* `1 (autogenerated)`）**

设置虚拟机世代 ID。使用 *1* 在创建或更新时自动生成，传入 *0* 可明确禁用。

**`--vmstatestorage` `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。

## **qm delsnapshot** `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_qm_delsnapshot" id="cli_qm_delsnapshot"></a>

删除虚拟机快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--force` `<boolean>`**

即使删除磁盘快照失败，也从配置文件中移除。

## **qm destroy** `<vmid>` `[OPTIONS]` <a href="#cli_qm_destroy" id="cli_qm_destroy"></a>

销毁虚拟机以及所有使用的/所属的卷。移除所有虚拟机特定权限和防火墙规则

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--destroy-unreferenced-disks` `<boolean>` （*默认值 \=* `0`）**

如果设置，还会从所有已启用的存储中销毁配置中未引用但 VMID 匹配的所有磁盘。

**`--purge` `<boolean>`**

从备份任务、复制任务和 HA 等配置中移除 VMID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

## **qm disk import** `<vmid> <source> <storage>` `[OPTIONS]` <a href="#cli_qm_disk_import" id="cli_qm_disk_import"></a>

将外部磁盘镜像作为虚拟机中的未使用磁盘导入。镜像格式必须受 qemu-img(1) 支持。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<source>`: `<string>`**

要导入的磁盘镜像路径

**`<storage>`: `<storage ID>`**

目标存储 ID

**`--format` `<qcow2 | raw | vmdk>`**

目标格式

**`--target-disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

卷将导入到的磁盘名称（例如 scsi1）。

## **qm disk move** `<vmid> <disk> [<storage>]` `[OPTIONS]` <a href="#cli_qm_disk_move" id="cli_qm_disk_move"></a>

将卷移动到其他存储或其他虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

要移动的磁盘。

**`<storage>`: `<storage ID>`**

目标存储。

**`--bwlimit` `<integer> (0 - N)` （*默认值 \=* `move limit from datacenter or storage config`）**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (*默认 \=* `0`)**

成功复制后删除原始磁盘。默认保留原始磁盘作为未使用磁盘。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--format` `<qcow2 | raw | vmdk>`**

目标磁盘格式。仅在移动到其他存储时使用。如果目标存储不支持此格式，则改用存储的默认格式。

**`--target-digest` `<string>`**

如果目标虚拟机当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于检测并发修改。

**`--target-disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

磁盘将移动到的目标虚拟机配置键（例如 ide0 或 scsi1）。默认为源磁盘键。

**`--target-vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm disk rescan** `[OPTIONS]` <a href="#cli_qm_disk_rescan" id="cli_qm_disk_rescan"></a>

重新扫描所有存储，并更新磁盘大小和未使用的磁盘映像。

**`--dryrun` `<boolean>` (*默认 \=* `0`)**

不将更改实际写入虚拟机配置。

**`--vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm disk resize** `<vmid> <disk> <size>` `[OPTIONS]` <a href="#cli_qm_disk_resize" id="cli_qm_disk_resize"></a>

扩展卷大小。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

要调整大小的磁盘。

**`<size>`: `\+?\d+(\.\d+)?[KMGT]?`**

新大小。如果带有 `+` 符号，则将此值加到卷的实际大小上；否则将此值作为绝对大小。不支持缩小磁盘大小。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

## **qm disk unlink** `<vmid> --idlist <string>` `[OPTIONS]` <a href="#cli_qm_disk_unlink" id="cli_qm_disk_unlink"></a>

解除链接/删除磁盘镜像。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--force` `<boolean>`**

强制物理删除。如果不设置此项，则只从配置文件中移除磁盘，并创建一个名为 *unused\[n\]* 的额外配置条目，其中包含卷 ID。解除 unused\[n\] 的链接始终会导致物理删除。

**`--idlist` `<string>`**

要删除的磁盘 ID 列表。

## **qm enroll-efi-keys** `<vmid>` <a href="#cli_qm_enroll-efi-keys" id="cli_qm_enroll-efi-keys"></a>

向具有 pre-enrolled-keys 的 EFI 磁盘注册重要的更新证书。目前这些证书为 Microsoft 的 UEFI 2023 证书。必须在虚拟机关机时调用。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm guest cmd** `<vmid> <command>` <a href="#cli_qm_guest_cmd" id="cli_qm_guest_cmd"></a>

执行 QEMU 客户机代理命令。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<command>`: `<fsfreeze-freeze | fsfreeze-status | fsfreeze-thaw | fstrim | get-fsinfo | get-host-name | get-memory-block-info | get-memory-blocks | get-osinfo | get-time | get-timezone | get-users | get-vcpus | info | network-get-interfaces | ping | shutdown | suspend-disk | suspend-hybrid | suspend-ram>`**

QGA 命令。

## **qm guest exec** `<vmid> [<extra-args>]` `[OPTIONS]` <a href="#cli_qm_guest_exec" id="cli_qm_guest_exec"></a>

通过客户机代理执行给定命令

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--pass-stdin` `<boolean>` （*默认值 \=* `0`）**

设置后，读取 STDIN 直到 EOF，并通过 *input-data* 转发到客户机代理（通常被视为客户机代理启动进程的 STDIN）。最大允许 1 MiB。

**`--synchronous` `<boolean>` （*默认值 \=* `1`）**

如果设置为 off，则立即返回 pid，而不等待命令完成或超时。

**`--timeout` `<integer> (0 - N)` （*默认值 \=* `30`）**

同步等待命令完成的最长时间。如果达到该时间，则返回 pid。设置为 0 可禁用

## **qm guest exec-status** `<vmid> <pid>` <a href="#cli_qm_guest_exec-status" id="cli_qm_guest_exec-status"></a>

获取客户机代理启动的给定 pid 的状态

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<pid>`: `<integer>`**

要查询的 PID

## **qm guest passwd** `<vmid> <username>` `[OPTIONS]` <a href="#cli_qm_guest_passwd" id="cli_qm_guest_passwd"></a>

将给定用户的密码设置为给定密码

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<username>`: `<string>`**

要设置密码的用户。

**`--crypted` `<boolean>` （*默认值 \=* `0`）**

如果密码已通过 crypt() 处理，则设置为 1

## **qm help** `[OPTIONS]` <a href="#cli_qm_help" id="cli_qm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **qm import** `<vmid> <source> --storage <string>` `[OPTIONS]` <a href="#cli_qm_import" id="cli_qm_import"></a>

从支持的导入源（例如 ESXi 存储）导入外部虚拟客户机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<source>`: `<string>`**

导入源的卷 ID。

**`--acpi` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 ACPI。

**`--affinity` `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`--allow-ksm` `<boolean>` （*默认值 \=* `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`--arch` `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`--args` `<string>`**

传递给 kvm 的任意参数。

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`--autostart` `<boolean>` （*默认值 \=* `0`）**

崩溃后自动重启（目前被忽略）。

**`--balloon` `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`--bios` `<ovmf | seabios>` （*默认值 \=* `seabios`）**

选择 BIOS 实现。

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 *order\=* 子属性，因为不带键的用法或 *legacy\=* 已弃用。

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 *boot: order\=foo;bar*。

**`--cdrom` `<volume>`**

这是选项 -ide2 的别名

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`--cipassword` `<string>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`--citype` `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`--ciupgrade` `<boolean>` （*默认值 \=* `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`--ciuser` `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`--cores` `<integer> (1 - N)` （*默认值 \=* `1`）**

每个 CPU 插槽的核心数。

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`--cpulimit` `<number> (0 - 128)` （*默认值 \=* `0`）**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` （*默认值 \=* `cgroup v1: 1024, cgroup v2: 100`）**

虚拟机的 CPU 权重，在 cgroup v2 中限制为 \[1, 10000\]。

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`--dryrun` `<boolean>` (*默认 \=* `0`)**

显示创建命令后退出，不执行任何操作。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是将默认 EFI 变量复制到该卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--format` `<qcow2 | raw | vmdk>`**

目标格式

**`--freeze` `<boolean>`**

启动时冻结 CPU（使用 *c* 监视器命令开始执行）。

**`--hookscript` `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

**`--hotplug` `<string>` （*默认值 \=* `network,disk,usb`）**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：*network*、*disk*、*cpu*、*memory*、*usb* 和 *cloudinit*。使用 *0* 完全禁用热插拔。将 *1* 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`--hugepages` `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 *any*，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 *dhcp* 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 *auto* 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`--ivshmem` `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`--keephugepages` `<boolean>` （*默认值 \=* `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`--kvm` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 KVM 硬件虚拟化。

**`--live-import` `<boolean>` （*默认值 \=* `0`）**

立即启动虚拟机，并在后台复制数据。

**`--localtime` `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--memory` `[current=]<integer>`**

内存属性。

**`--migrate_downtime` `<number> (0 - N)` （*默认值 \=* `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`--migrate_speed` `<integer> (0 - N)` （*默认值 \=* `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`--name` `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`--nameserver` `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`--numa` `<boolean>` （*默认值 \=* `0`）**

启用/禁用 NUMA。

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`--onboot` `<boolean>`（*默认 \=* `0`）**

指定是否在系统启动时启动虚拟机。

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` （*默认值 \=* `other`）**

指定客户机操作系统。

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

**`--protection` `<boolean>`（*默认 \=* `0`）**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`--reboot` `<boolean>` （*默认值 \=* `1`）**

允许重启。如果设为 *0*，虚拟机将在重启时退出。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` （*默认值 \=* `lsi`）**

SCSI 控制器型号

**`--searchdomain` `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--serial[n]` `(/dev/[^,]+|socket)`**

在虚拟机内创建串口设备（n 为 0 到 3）

**`--shares` `<integer> (0 - 50000)` （*默认值 \=* `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`--smp` `<integer> (1 - N)` （*默认值 \=* `1`）**

CPU 数量。请改用 -sockets 选项。

**`--sockets` `<integer> (1 - N)` （*默认值 \=* `1`）**

CPU 插槽数量。

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`--sshkeys` `<string>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` （*默认值 \=* `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、*2006-06-17T16:01:21* 或 *2006-06-17*。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`**

默认存储。

**`--tablet` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 USB 数位板设备。

**`--tags` `<string>`**

虚拟机的标签。这只是元信息。

**`--tdf` `<boolean>` （*默认值 \=* `0`）**

启用/禁用时间漂移修正。

**`--template` `<boolean>`（*默认 \=* `0`）**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 *raw*。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是使用 4 MiB。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`--vcpus` `<integer> (1 - N)` （*默认值 \=* `0`）**

热插拔的 vcpu 数量。

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`--vmgenid` `<UUID>` （*默认值 \=* `1 (autogenerated)`）**

设置虚拟机世代 ID。使用 *1* 在创建或更新时自动生成，传入 *0* 可明确禁用。

**`--vmstatestorage` `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。

## **qm importdisk** <a href="#cli_qm_importdisk" id="cli_qm_importdisk"></a>

*qm disk import* 的别名。

## **qm importovf** `<vmid> <manifest> <storage>` `[OPTIONS]` <a href="#cli_qm_importovf" id="cli_qm_importovf"></a>

使用从 OVF 清单读取的参数创建新虚拟机

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<manifest>`: `<string>`**

ovf 文件的路径

**`<storage>`: `<storage ID>`**

目标存储 ID

**`--dryrun` `<boolean>`**

打印所提取 OVF 参数的解析后表示，但不创建虚拟机

**`--format` `<qcow2 | raw | vmdk>`**

目标格式

## **qm list** `[OPTIONS]` <a href="#cli_qm_list" id="cli_qm_list"></a>

虚拟机索引（每个节点）。

**`--full` `<boolean>`**

确定活动虚拟机的完整状态。

## **qm listsnapshot** `<vmid>` <a href="#cli_qm_listsnapshot" id="cli_qm_listsnapshot"></a>

列出所有快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm migrate** `<vmid> <target>` `[OPTIONS]` <a href="#cli_qm_migrate" id="cli_qm_migrate"></a>

迁移虚拟机。创建新的迁移任务。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target>`: `<string>`**

目标节点。

**`--bwlimit` `<integer> (0 - N)` (*默认 \=* `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--force` `<boolean>`**

允许迁移使用本地设备的虚拟机。只有 root 可以使用此选项。

**`--migration_network` `<string>`**

用于迁移的网络（或子网）的 CIDR。

**`--migration_type` `<insecure | secure>`**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`--online` `<boolean>`**

如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。

**`--targetstorage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

**`--with-conntrack-state` `<boolean>` （*默认值 \=* `0`）**

是否迁移运行中虚拟机的 conntrack 条目。

**`--with-local-disks` `<boolean>`**

对本地磁盘启用在线存储迁移

## **qm monitor** `<vmid>` <a href="#cli_qm_monitor" id="cli_qm_monitor"></a>

进入 QEMU 监视器界面。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm move-disk** <a href="#cli_qm_move-disk" id="cli_qm_move-disk"></a>

*qm disk move* 的别名。

## **qm move\_disk** <a href="#cli_qm_move_disk" id="cli_qm_move_disk"></a>

*qm disk move* 的别名。

## **qm mtunnel** <a href="#cli_qm_mtunnel" id="cli_qm_mtunnel"></a>

由 qmigrate 使用，请勿手动使用。

## **qm nbdstop** `<vmid>` <a href="#cli_qm_nbdstop" id="cli_qm_nbdstop"></a>

停止内嵌 nbd 服务器。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm pending** `<vmid>` <a href="#cli_qm_pending" id="cli_qm_pending"></a>

获取同时包含当前值和待应用值的虚拟机配置。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm reboot** `<vmid>` `[OPTIONS]` <a href="#cli_qm_reboot" id="cli_qm_reboot"></a>

通过关闭虚拟机后重新启动来重启虚拟机。应用待定更改。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒以完成关机。

## **qm remote-migrate** `<vmid> [<target-vmid>] <target-endpoint> --target-bridge <string> --target-storage <string>` `[OPTIONS]` <a href="#cli_qm_remote-migrate" id="cli_qm_remote-migrate"></a>

将虚拟机迁移到远程集群。创建新的迁移任务。实验性功能！

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-endpoint>`: `apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]`**

远程目标端点

**`--bwlimit` `<integer> (0 - N)` (*默认 \=* `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (*默认 \=* `0`)**

成功迁移后删除原始虚拟机及相关数据。默认情况下，原始虚拟机保留在源集群中，处于停止状态。

**`--online` `<boolean>`**

如果虚拟机正在运行，则使用在线迁移。如果虚拟机已停止，则忽略。

**`--target-bridge` `<string>`**

从源网桥到目标网桥的映射。仅提供一个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 *1* 会将每个源网桥映射到其自身。

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

## **qm rescan** <a href="#cli_qm_rescan" id="cli_qm_rescan"></a>

*qm disk rescan* 的别名。

## **qm reset** `<vmid>` `[OPTIONS]` <a href="#cli_qm_reset" id="cli_qm_reset"></a>

重置虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

## **qm resize** <a href="#cli_qm_resize" id="cli_qm_resize"></a>

*qm disk resize* 的别名。

## **qm resume** `<vmid>` `[OPTIONS]` <a href="#cli_qm_resume" id="cli_qm_resume"></a>

恢复虚拟机运行。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--nocheck` `<boolean>`**

不检查虚拟机是否正在运行，内部用于迁移期间。只有 root 可以使用此选项。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

## **qm rollback** `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_qm_rollback" id="cli_qm_rollback"></a>

将虚拟机状态回滚到指定快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--start` `<boolean>`（*默认 \=* `0`）**

成功回滚后是否启动虚拟机。（注意：如果快照包含 RAM，虚拟机将自动启动。）

## **qm sendkey** `<vmid> <key>` `[OPTIONS]` <a href="#cli_qm_sendkey" id="cli_qm_sendkey"></a>

向虚拟机发送按键事件。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<key>`: `<string>`**

按键（qemu 监视器编码）。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

## **qm set** `<vmid>` `[OPTIONS]` <a href="#cli_qm_set" id="cli_qm_set"></a>

设置虚拟机选项（同步 API）。对于任何涉及热插拔或存储分配的操作，应考虑改用 POST 方法。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--acpi` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 ACPI。

**`--affinity` `<string>`**

用于执行客户机进程的宿主机核心列表，例如：0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

启用/禁用与 QEMU Guest Agent 的通信及其属性。

**`--allow-ksm` `<boolean>` （*默认值 \=* `1`）**

允许通过 KSM（内核同页合并）合并此客户机的内存页。

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

AMD CPU 的安全加密虚拟化（SEV）功能

**`--arch` `<aarch64 | x86_64>`**

虚拟处理器架构。默认为宿主机架构。

**`--args` `<string>`**

传递给 kvm 的任意参数。

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

配置音频设备，与 QXL/Spice 结合使用时很有用。

**`--autostart` `<boolean>` （*默认值 \=* `0`）**

崩溃后自动重启（目前被忽略）。

**`--balloon` `<integer> (0 - N)`**

VM 的目标 RAM 大小，单位为 MiB。默认启用 balloon 驱动程序，除非通过将值设置为零明确禁用它。

**`--bios` `<ovmf | seabios>` （*默认值 \=* `seabios`）**

选择 BIOS 实现。

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

指定客户机启动顺序。请使用 *order\=* 子属性，因为不带键的用法或 *legacy\=* 已弃用。

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

启用从指定磁盘启动。已弃用：请改用 *boot: order\=foo;bar*。

**`--cdrom` `<volume>`**

这是选项 -ide2 的别名

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init：指定自定义文件，以在启动时替换自动生成的文件。

**`--cipassword` `<password>`**

cloud-init：分配给用户的密码。通常不建议使用此选项，请改用 ssh 密钥。另请注意，较旧版本的 cloud-init 不支持哈希密码。

**`--citype` `<configdrive2 | nocloud | opennebula>`**

指定 cloud-init 配置格式。默认值取决于配置的操作系统类型（`ostype`。Linux 使用 `nocloud` 格式，Windows 使用 `configdrive2`。

**`--ciupgrade` `<boolean>` （*默认值 \=* `1`）**

cloud-init：首次启动后自动执行软件包升级。

**`--ciuser` `<string>`**

cloud-init：指定要更改 ssh 密钥和密码的用户名，以代替映像中配置的默认用户。

**`--cores` `<integer> (1 - N)` （*默认值 \=* `1`）**

每个 CPU 插槽的核心数。

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

模拟的 CPU 类型。

**`--cpulimit` `<number> (0 - 128)` （*默认值 \=* `0`）**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` （*默认值 \=* `cgroup v1: 1024, cgroup v2: 100`）**

虚拟机的 CPU 权重，在 cgroup v2 中限制为 \[1, 10000\]。

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

虚拟机的描述。显示在 Web 界面的虚拟机摘要中。此描述会作为注释保存在配置文件内。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

配置用于存储 EFI 变量的磁盘。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是将默认 EFI 变量复制到该卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--force` `<boolean>`**

强制物理删除。如果不设置此项，则只从配置文件中移除磁盘，并创建一个名为 *unused\[n\]* 的额外配置条目，其中包含卷 ID。解除 unused\[n\] 的链接始终会导致物理删除。

{% hint style="info" %}
需要选项：`delete`
{% endhint %}

**`--freeze` `<boolean>`**

启动时冻结 CPU（使用 *c* 监视器命令开始执行）。

**`--hookscript` `<string>`**

在虚拟机生命周期的各个阶段执行的脚本。

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

将宿主机 PCI 设备映射到客户机中。

**`--hotplug` `<string>` （*默认值 \=* `network,disk,usb`）**

选择性启用热插拔功能。这是以逗号分隔的热插拔功能列表：*network*、*disk*、*cpu*、*memory*、*usb* 和 *cloudinit*。使用 *0* 完全禁用热插拔。将 *1* 用作值是默认值 `network,disk,usb` 的别名。机器版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的客户机支持 USB 热插拔。

**`--hugepages` `<1024 | 2 | any>`**

启用大页内存。

设置大页的大小，单位为 MiB。如果值设置为 *any*，则尽可能使用 1 GiB 大页，否则大小将回退到 2 MiB。

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 IDE 硬盘或 CD-ROM（n 为 0 到 3）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Intel CPU 的信任域扩展（TDX）功能

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init：为相应接口指定 IP 地址和网关。

IP 地址使用 CIDR 表示法，网关是可选的，但需要指定相同类型的 IP 地址。

IP 地址可以使用特殊字符串 *dhcp* 来表示使用 DHCP，在这种情况下不应提供显式网关。对于 IPv6，可以使用特殊字符串 *auto* 来表示使用无状态自动配置。这需要 cloud-init 19.4 或更高版本。

如果启用了 cloud-init，且既未指定 IPv4 地址也未指定 IPv6 地址，则默认在 IPv4 上使用 dhcp。

**`--ivshmem` `size=<integer> [,name=<string>]`**

虚拟机间共享内存。适用于虚拟机之间的直接通信，或与宿主机的直接通信。

**`--keephugepages` `<boolean>` （*默认值 \=* `0`）**

与大页配合使用。如果启用，虚拟机关机后不会删除大页，可供后续启动使用。

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的键盘布局。通常不需要此选项，在客户机操作系统内部处理通常更合适。

**`--kvm` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 KVM 硬件虚拟化。

**`--localtime` `<boolean>`**

将实时时钟（RTC）设为本地时间。如果 `ostype` 表明是 Microsoft Windows 操作系统，则默认启用。

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

锁定/解锁虚拟机。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--memory` `[current=]<integer>`**

内存属性。

**`--migrate_downtime` `<number> (0 - N)` （*默认值 \=* `0.1`）**

设置迁移可容忍的最长停机时间（秒）。如果迁移在最后阶段因需要传输过多新写脏的 RAM 而无法收敛，将自动逐步增加此限制，直至迁移能够收敛。上限为 2000 秒（QEMU 中的最大值）。

**`--migrate_speed` `<integer> (0 - N)` （*默认值 \=* `0`）**

设置迁移的最大速度（MB/s）。值为 0 表示不限制。

**`--name` `<string>`**

设置虚拟机名称。仅用于配置 Web 界面。

**`--nameserver` `<string>`**

cloud-init：设置容器的 DNS 服务器 IP 地址。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

指定网络设备。

**`--numa` `<boolean>` （*默认值 \=* `0`）**

启用/禁用 NUMA。

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA 拓扑。

**`--onboot` `<boolean>`（*默认 \=* `0`）**

指定是否在系统启动时启动虚拟机。

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` （*默认值 \=* `other`）**

指定客户机操作系统。

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

映射宿主机并口设备（n 为 0 到 2）。

**`--protection` `<boolean>`（*默认 \=* `0`）**

设置虚拟机的保护标志。这将禁用删除虚拟机和删除磁盘操作。

**`--reboot` `<boolean>` （*默认值 \=* `1`）**

允许重启。如果设为 *0*，虚拟机将在重启时退出。

**`--revert` `<string>`**

撤销待处理的更改。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

配置基于 VirtIO 的随机数生成器。

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SATA 硬盘或 CD-ROM（n 为 0 到 5）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

将卷用作 SCSI 硬盘或 CD-ROM（n 为 0 到 30）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` （*默认值 \=* `lsi`）**

SCSI 控制器型号

**`--searchdomain` `<string>`**

cloud-init：设置容器的 DNS 搜索域。如果 searchdomain 和 nameserver 都未设置，创建时将自动采用宿主机的设置。

**`--serial[n]` `(/dev/[^,]+|socket)`**

在虚拟机内创建串口设备（n 为 0 到 3）

**`--shares` `<integer> (0 - 50000)` （*默认值 \=* `1000`）**

自动气球调整的内存份额。数值越大，该虚拟机获得的内存越多。该数值相对于所有其他运行中虚拟机的权重。使用零可禁用自动气球调整。自动气球调整由 pvestatd 完成。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

指定 SMBIOS 类型 1 的字段。

**`--smp` `<integer> (1 - N)` （*默认值 \=* `1`）**

CPU 数量。请改用 -sockets 选项。

**`--sockets` `<integer> (1 - N)` （*默认值 \=* `1`）**

CPU 插槽数量。

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

配置 SPICE 的额外增强功能。

**`--sshkeys` `<filepath>`**

cloud-init：设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` （*默认值 \=* `now`）**

设置实时时钟的初始日期。有效的日期格式为：'now'、*2006-06-17T16:01:21* 或 *2006-06-17*。

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--tablet` `<boolean>` （*默认值 \=* `1`）**

启用/禁用 USB 数位板设备。

**`--tags` `<string>`**

虚拟机的标签。这只是元信息。

**`--tdf` `<boolean>` （*默认值 \=* `0`）**

启用/禁用时间漂移修正。

**`--template` `<boolean>`（*默认 \=* `0`）**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

配置用于存储 TPM 状态的磁盘。格式固定为 *raw*。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。请注意，此处会忽略 SIZE\_IN\_GiB，而是使用 4 MiB。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

配置 USB 设备（n 为 0 到 4；对于机型版本 \>\= 7.1 且 ostype 为 l26 或 windows \> 7 的情况，n 最大可为 14）。

**`--vcpus` `<integer> (1 - N)` （*默认值 \=* `0`）**

热插拔的 vcpu 数量。

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

配置 VGA 硬件。

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

将卷用作 VIRTIO 硬盘（n 为 0 到 15）。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 分配新卷。使用 STORAGE\_ID:0 和 *import-from* 参数从现有卷导入。

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

使用 Virtio-fs 在宿主机与客户机之间共享目录的配置。

**`--vmgenid` `<UUID>` （*默认值 \=* `1 (autogenerated)`）**

设置虚拟机世代 ID。使用 *1* 在创建或更新时自动生成，传入 *0* 可明确禁用。

**`--vmstatestorage` `<storage ID>`**

虚拟机状态卷/文件的默认存储。

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

创建虚拟硬件看门狗设备。

## **qm showcmd** `<vmid>` `[OPTIONS]` <a href="#cli_qm_showcmd" id="cli_qm_showcmd"></a>

显示用于启动虚拟机的命令行（调试信息）。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--pretty` `<boolean>` （*默认值 \=* `0`）**

将每个选项放在单独一行，以提高可读性

**`--snapshot` `<string>`**

从指定快照获取配置值。

## **qm shutdown** `<vmid>` `[OPTIONS]` <a href="#cli_qm_shutdown" id="cli_qm_shutdown"></a>

关闭虚拟机。这类似于按下物理机器的电源按钮。此操作会向客户机操作系统发送 ACPI 事件，随后客户机应执行正常关机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--forceStop` `<boolean>` (*默认 \=* `0`)**

确保虚拟机停止。

**`--keepActive` `<boolean>` （*默认值 \=* `0`）**

不停用存储卷。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒。

## **qm snapshot** `<vmid> <snapname>` `[OPTIONS]` <a href="#cli_qm_snapshot" id="cli_qm_snapshot"></a>

为虚拟机创建快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--description` `<string>`**

文本描述或注释。

**`--vmstate` `<boolean>`**

保存 vmstate

## **qm start** `<vmid>` `[OPTIONS]` <a href="#cli_qm_start" id="cli_qm_start"></a>

启动虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--force-cpu` `<string>`**

使用给定字符串覆盖 QEMU 的 -cpu 参数。

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

指定 QEMU 机型。

**`--migratedfrom` `<string>`**

集群节点名称。

**`--migration_network` `<string>`**

用于迁移的网络（或子网）的 CIDR。

**`--migration_type` `<insecure | secure>`**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`--nets-host-mtu` `net\d+=\d+(,net\d+=\d+)*`**

用于迁移兼容性。根据迁移源端的 QEMU 对象模型列出 VirtIO 网络设备及其有效的 host\_mtu 设置。值为 0 表示对应设备应避免使用 host\_mtu 参数。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--stateuri` `<string>`**

某些命令从此位置保存/恢复状态。

**`--targetstorage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

**`--timeout` `<integer> (0 - N)` （*默认值 \=* `max(30, vm memory in GiB)`）**

最多等待 timeout 秒。

**`--with-conntrack-state` `<boolean>` （*默认值 \=* `0`）**

是否迁移运行中虚拟机的 conntrack 条目。

## **qm status** `<vmid>` `[OPTIONS]` <a href="#cli_qm_status" id="cli_qm_status"></a>

显示虚拟机状态。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--verbose` `<boolean>`**

详细输出格式

## **qm stop** `<vmid>` `[OPTIONS]` <a href="#cli_qm_stop" id="cli_qm_stop"></a>

停止虚拟机。qemu 进程将立即退出。这相当于拔掉正在运行的计算机的电源插头，可能损坏虚拟机数据。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--keepActive` `<boolean>` （*默认值 \=* `0`）**

不停用存储卷。

**`--migratedfrom` `<string>`**

集群节点名称。

**`--overrule-shutdown` `<boolean>`（*默认值 \=* `0`）**

停止前尝试中止活动的 *qmshutdown* 任务。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒。

## **qm suspend** `<vmid>` `[OPTIONS]` <a href="#cli_qm_suspend" id="cli_qm_suspend"></a>

挂起虚拟机。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--statestorage` `<storage ID>`**

存放虚拟机状态的存储

{% hint style="info" %}
需要选项：`todisk`
{% endhint %}

**`--todisk` `<boolean>` （*默认值 \=* `0`）**

如果设置，则将虚拟机挂起到磁盘。下次启动虚拟机时将恢复运行。

## **qm template** `<vmid>` `[OPTIONS]` <a href="#cli_qm_template" id="cli_qm_template"></a>

创建模板。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

如果只想将 1 个磁盘转换为基础镜像。

## **qm terminal** `<vmid>` `[OPTIONS]` <a href="#cli_qm_terminal" id="cli_qm_terminal"></a>

使用串口设备打开终端（虚拟机需要配置串口设备，例如 *serial0: socket*）

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--escape` `<string>` （*默认值 \=* `^O`）**

转义字符。

**`--iface` `<serial0 | serial1 | serial2 | serial3>`**

选择串口设备。默认使用首个合适的设备。

## **qm unlink** <a href="#cli_qm_unlink" id="cli_qm_unlink"></a>

*qm disk unlink* 的别名。

## **qm unlock** `<vmid>` <a href="#cli_qm_unlock" id="cli_qm_unlock"></a>

解锁 VM。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm vncproxy** `<vmid>` <a href="#cli_qm_vncproxy" id="cli_qm_vncproxy"></a>

将虚拟机 VNC 流量代理到 stdin/stdout

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

## **qm wait** `<vmid>` `[OPTIONS]` <a href="#cli_qm_wait" id="cli_qm_wait"></a>

等待虚拟机停止。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (1 - N)`**

超时时间，单位为秒。默认无限等待。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
