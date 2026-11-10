# qm(1)

## NAME <a href="#chapter_virtual_machines" id="chapter_virtual_machines"></a>

qm \- QEMU/KVM Virtual Machine Manager

## SYNOPSIS <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_qm"></a>



**qm** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_qm_agent"></a>



**qm agent**

An alias for *qm guest cmd*.

<a id="cli_qm_cleanup"></a>



**qm cleanup** `<vmid> <clean-shutdown> <guest-requested>`

Cleans up resources like tap devices, vgpus, etc. Called after a vm shuts down, crashes, etc.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<clean-shutdown>`: `<boolean>`**

Indicates if qemu shutdown cleanly.

**`<guest-requested>`: `<boolean>`**

Indicates if the shutdown was requested by the guest or via qmp.

<a id="cli_qm_clone"></a>



**qm clone** `<vmid> <newid>` `[OPTIONS]`

Create a copy of virtual machine/template.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<newid>`: `<integer> (100 - 999999999)`**

克隆的 VMID。

**`--bwlimit` `<integer> (0 - N)` (*default \=* `clone limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--description` `<string>`**

Description for the new VM.

**`--format` `<qcow2 | raw | vmdk>`**

Target disk format. Only valid for full clone. If the target storage does not support the format, the storage’s default format is used instead.

**`--full` `<boolean>`**

Create a full copy of all disks. This is always done when you clone a normal VM. For VM templates, we try to create a linked clone by default.

**`--name` `<string>`**

Set a name for the new VM.

**`--pool` `<string>`**

Add the new VM to the specified pool.

**`--snapname` `<string>`**

快照的名称。

**`--storage` `<storage ID>`**

完整克隆的目标存储。

**`--target` `<string>`**

目标节点。仅当原始 VM 位于共享存储上时才允许。

<a id="cli_qm_cloudinit_dump"></a>



**qm cloudinit dump** `<vmid> <type>`

Get automatically generated cloudinit config.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<type>`: `<meta | network | user>`**

Config type.

<a id="cli_qm_cloudinit_pending"></a>



**qm cloudinit pending** `<vmid>`

Get the cloudinit configuration with both current and pending values.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_cloudinit_update"></a>



**qm cloudinit update** `<vmid>`

Regenerate and change cloudinit config drive.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_config"></a>



**qm config** `<vmid>` `[OPTIONS]`

Get the virtual machine configuration with pending configuration changes applied. Set the *current* parameter to get the current configuration instead.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--current` `<boolean>` (*default \=* `0`)**

获取当前值（而非待生效值）。

**`--snapshot` `<string>`**

从指定快照获取配置值。

<a id="cli_qm_create"></a>



**qm create** `<vmid>` `[OPTIONS]`

Create or restore a virtual machine.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--acpi` `<boolean>` (*default \=* `1`)**

Enable/disable ACPI.

**`--affinity` `<string>`**

List of host cores used to execute guest processes, for example: 0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

Enable/disable communication with the QEMU Guest Agent and its properties.

**`--allow-ksm` `<boolean>` (*default \=* `1`)**

Allow memory pages of this guest to be merged via KSM (Kernel Samepage Merging).

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

Secure Encrypted Virtualization (SEV) features by AMD CPUs

**`--arch` `<aarch64 | x86_64>`**

Virtual processor architecture. Defaults to the host architecture.

**`--archive` `<string>`**

The backup archive. Either the file system path to a .tar or .vma file (use *\-* to pipe data from stdin) or a proxmox storage backup volume identifier.

**`--args` `<string>`**

Arbitrary arguments passed to kvm.

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

Configure a audio device, useful in combination with QXL/Spice.

**`--autostart` `<boolean>` (*default \=* `0`)**

Automatic restart after crash (currently ignored).

**`--balloon` `<integer> (0 - N)`**

Amount of target RAM for the VM in MiB. The balloon driver is enabled by default, unless it is explicitly disabled by setting the value to zero.

**`--bios` `<ovmf | seabios>` (*default \=* `seabios`)**

Select BIOS implementation.

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

Specify guest boot order. Use the *order\=* sub-property as usage with no key or *legacy\=* is deprecated.

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

Enable booting from specified disk. Deprecated: Use *boot: order\=foo;bar* instead.

**`--bwlimit` `<integer> (0 - N)` (*default \=* `restore limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--cdrom` `<volume>`**

This is an alias for option -ide2

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init: Specify custom files to replace the automatically generated ones at start.

**`--cipassword` `<password>`**

cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords.

**`--citype` `<configdrive2 | nocloud | opennebula>`**

Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows.

**`--ciupgrade` `<boolean>` (*default \=* `1`)**

cloud-init: do an automatic package upgrade after the first boot.

**`--ciuser` `<string>`**

cloud-init: User name to change ssh keys and password for instead of the image’s configured default user.

**`--cores` `<integer> (1 - N)` (*default \=* `1`)**

The number of cores per socket.

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

Emulated CPU type.

**`--cpulimit` `<number> (0 - 128)` (*default \=* `0`)**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

CPU weight for a VM, will be clamped to \[1, 10000\] in cgroup v2.

**`--description` `<string>`**

Description for the VM. Shown in the web-interface VM’s summary. This is saved as comment inside the configuration file.

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

Configure a disk for storing EFI vars. Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Note that SIZE\_IN\_GiB is ignored here and that the default EFI vars are copied to the volume instead. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--force` `<boolean>`**

Allow to overwrite existing VM.

{% hint style="info" %}
Requires option(s): `archive`
{% endhint %}

**`--freeze` `<boolean>`**

Freeze CPU at startup (use *c* monitor command to start execution).

**`--ha-managed` `<boolean>` (*default \=* `0`)**

Add the VM as a HA resource after it was created.

**`--hookscript` `<string>`**

Script that will be executed during various steps in the vms lifetime.

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

Map host PCI devices into guest.

**`--hotplug` `<string>` (*default \=* `network,disk,usb`)**

Selectively enable hotplug features. This is a comma separated list of hotplug features: *network*, *disk*, *cpu*, *memory*, *usb* and *cloudinit*. Use *0* to disable hotplug completely. Using *1* as value is an alias for the default `network,disk,usb`. USB hotplugging is possible for guests with machine version \>\= 7.1 and ostype l26 or windows \> 7\.

**`--hugepages` `<1024 | 2 | any>`**

Enables hugepages memory.

Sets the size of hugepages in MiB. If the value is set to *any* then 1 GiB hugepages will be used if possible, otherwise the size will fall back to 2 MiB.

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--import-working-storage` `<storage ID>`**

A file-based storage with *images* content-type enabled, which is used as an intermediary extraction storage during import. Defaults to the source storage.

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Trusted Domain Extension (TDX) features by Intel CPUs

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string *dhcp* can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string *auto* can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4.

**`--ivshmem` `size=<integer> [,name=<string>]`**

Inter-VM shared memory. Useful for direct communication between VMs, or to the host.

**`--keephugepages` `<boolean>` (*default \=* `0`)**

Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts.

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

Keyboard layout for VNC server. This option is generally not required and is often better handled from within the guest OS.

**`--kvm` `<boolean>` (*default \=* `1`)**

Enable/disable KVM hardware virtualization.

**`--live-restore` `<boolean>`**

Start the VM immediately while importing or restoring in the background.

**`--localtime` `<boolean>`**

Set the real time clock (RTC) to local time. This is enabled by default if the `ostype` indicates a Microsoft Windows OS.

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

Lock/unlock the VM.

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`--memory` `[current=]<integer>`**

Memory properties.

**`--migrate_downtime` `<number> (0 - N)` (*default \=* `0.1`)**

Set maximum tolerated downtime (in seconds) for migrations. Should the migration not be able to converge in the very end, because too much newly dirtied RAM needs to be transferred, the limit will be increased automatically step-by-step until migration can converge. Will be capped to 2000 seconds (maximum in QEMU).

**`--migrate_speed` `<integer> (0 - N)` (*default \=* `0`)**

Set maximum speed (in MB/s) for migrations. Value 0 is no limit.

**`--name` `<string>`**

Set a name for the VM. Only used on the configuration web interface.

**`--nameserver` `<string>`**

cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

Specify network devices.

**`--numa` `<boolean>` (*default \=* `0`)**

Enable/disable NUMA.

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA topology.

**`--onboot` `<boolean>` (*default \=* `0`)**

Specifies whether a VM will be started during system bootup.

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` (*default \=* `other`)**

Specify guest operating system.

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

Map host parallel devices (n is 0 to 2).

**`--pool` `<string>`**

将 VM 添加到指定池。

**`--protection` `<boolean>` (*default \=* `0`)**

Sets the protection flag of the VM. This will disable the remove VM and remove disk operations.

**`--reboot` `<boolean>` (*default \=* `1`)**

Allow reboot. If set to *0* the VM exit on reboot.

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

Configure a VirtIO-based Random Number Generator.

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` (*default \=* `lsi`)**

SCSI controller model

**`--searchdomain` `<string>`**

cloud-init: Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`--serial[n]` `(/dev/[^,]+|socket)`**

Create a serial device inside the VM (n is 0 to 3\)

**`--shares` `<integer> (0 - 50000)` (*default \=* `1000`)**

Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd.

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

Specify SMBIOS type 1 fields.

**`--smp` `<integer> (1 - N)` (*default \=* `1`)**

The number of CPUs. Please use option -sockets instead.

**`--sockets` `<integer> (1 - N)` (*default \=* `1`)**

The number of CPU sockets.

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

Configure additional enhancements for SPICE.

**`--sshkeys` `<filepath>`**

cloud-init: Setup public SSH keys (one key per line, OpenSSH format).

**`--start` `<boolean>` (*default \=* `0`)**

Start VM after it was created successfully.

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` (*default \=* `now`)**

Set the initial date of the real time clock. Valid format for date are:'now' or *2006-06-17T16:01:21* or *2006-06-17*.

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`**

Default storage.

**`--tablet` `<boolean>` (*default \=* `1`)**

Enable/disable the USB tablet device.

**`--tags` `<string>`**

Tags of the VM. This is only meta information.

**`--tdf` `<boolean>` (*default \=* `0`)**

Enable/disable time drift fix.

**`--template` `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

Configure a Disk for storing TPM state. The format is fixed to *raw*. Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Note that SIZE\_IN\_GiB is ignored here and 4 MiB will be used instead. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--unique` `<boolean>`**

分配唯一的随机以太网地址。

{% hint style="info" %}
Requires option(s): `archive`
{% endhint %}

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

Configure an USB device (n is 0 to 4, for machine version \>\= 7.1 and ostype l26 or windows \> 7, n can be up to 14).

**`--vcpus` `<integer> (1 - N)` (*default \=* `0`)**

Number of hotplugged vcpus.

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

Configure the VGA hardware.

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

Configuration for sharing a directory between host and guest using Virtio-fs.

**`--vmgenid` `<UUID>` (*default \=* `1 (autogenerated)`)**

Set VM Generation ID. Use *1* to autogenerate on create or update, pass *0* to disable explicitly.

**`--vmstatestorage` `<storage ID>`**

Default storage for VM state volumes/files.

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

Create a virtual hardware watchdog device.

<a id="cli_qm_delsnapshot"></a>



**qm delsnapshot** `<vmid> <snapname>` `[OPTIONS]`

Delete a VM snapshot.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--force` `<boolean>`**

即使删除磁盘快照失败，也从配置文件中移除。

<a id="cli_qm_destroy"></a>



**qm destroy** `<vmid>` `[OPTIONS]`

Destroy the VM and all used/owned volumes. Removes any VM specific permissions and firewall rules

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--destroy-unreferenced-disks` `<boolean>` (*default \=* `0`)**

If set, destroy additionally all disks not referenced in the config but with a matching VMID from all enabled storages.

**`--purge` `<boolean>`**

Remove VMID from configurations, like backup \& replication jobs and HA.

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_qm_disk_import"></a>



**qm disk import** `<vmid> <source> <storage>` `[OPTIONS]`

Import an external disk image as an unused disk in a VM. The image format has to be supported by qemu-img(1).

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<source>`: `<string>`**

Path to the disk image to import

**`<storage>`: `<storage ID>`**

Target storage ID

**`--format` `<qcow2 | raw | vmdk>`**

Target format

**`--target-disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

The disk name where the volume will be imported to (e.g. scsi1).

<a id="cli_qm_disk_move"></a>



**qm disk move** `<vmid> <disk> [<storage>]` `[OPTIONS]`

Move volume to different storage or to a different VM.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

The disk you want to move.

**`<storage>`: `<storage ID>`**

Target storage.

**`--bwlimit` `<integer> (0 - N)` (*default \=* `move limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (*default \=* `0`)**

Delete the original disk after successful copy. By default the original disk is kept as unused disk.

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--format` `<qcow2 | raw | vmdk>`**

Target disk format. Only used when moving to a different storage. If the target storage does not support the format, the storage’s default format is used instead.

**`--target-digest` `<string>`**

Prevent changes if the current config file of the target VM has a different SHA1 digest. This can be used to detect concurrent modifications.

**`--target-disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | unused0 | unused1 | unused10 | unused100 | unused101 | unused102 | unused103 | unused104 | unused105 | unused106 | unused107 | unused108 | unused109 | unused11 | unused110 | unused111 | unused112 | unused113 | unused114 | unused115 | unused116 | unused117 | unused118 | unused119 | unused12 | unused120 | unused121 | unused122 | unused123 | unused124 | unused125 | unused126 | unused127 | unused128 | unused129 | unused13 | unused130 | unused131 | unused132 | unused133 | unused134 | unused135 | unused136 | unused137 | unused138 | unused139 | unused14 | unused140 | unused141 | unused142 | unused143 | unused144 | unused145 | unused146 | unused147 | unused148 | unused149 | unused15 | unused150 | unused151 | unused152 | unused153 | unused154 | unused155 | unused156 | unused157 | unused158 | unused159 | unused16 | unused160 | unused161 | unused162 | unused163 | unused164 | unused165 | unused166 | unused167 | unused168 | unused169 | unused17 | unused170 | unused171 | unused172 | unused173 | unused174 | unused175 | unused176 | unused177 | unused178 | unused179 | unused18 | unused180 | unused181 | unused182 | unused183 | unused184 | unused185 | unused186 | unused187 | unused188 | unused189 | unused19 | unused190 | unused191 | unused192 | unused193 | unused194 | unused195 | unused196 | unused197 | unused198 | unused199 | unused2 | unused20 | unused200 | unused201 | unused202 | unused203 | unused204 | unused205 | unused206 | unused207 | unused208 | unused209 | unused21 | unused210 | unused211 | unused212 | unused213 | unused214 | unused215 | unused216 | unused217 | unused218 | unused219 | unused22 | unused220 | unused221 | unused222 | unused223 | unused224 | unused225 | unused226 | unused227 | unused228 | unused229 | unused23 | unused230 | unused231 | unused232 | unused233 | unused234 | unused235 | unused236 | unused237 | unused238 | unused239 | unused24 | unused240 | unused241 | unused242 | unused243 | unused244 | unused245 | unused246 | unused247 | unused248 | unused249 | unused25 | unused250 | unused251 | unused252 | unused253 | unused254 | unused255 | unused26 | unused27 | unused28 | unused29 | unused3 | unused30 | unused31 | unused32 | unused33 | unused34 | unused35 | unused36 | unused37 | unused38 | unused39 | unused4 | unused40 | unused41 | unused42 | unused43 | unused44 | unused45 | unused46 | unused47 | unused48 | unused49 | unused5 | unused50 | unused51 | unused52 | unused53 | unused54 | unused55 | unused56 | unused57 | unused58 | unused59 | unused6 | unused60 | unused61 | unused62 | unused63 | unused64 | unused65 | unused66 | unused67 | unused68 | unused69 | unused7 | unused70 | unused71 | unused72 | unused73 | unused74 | unused75 | unused76 | unused77 | unused78 | unused79 | unused8 | unused80 | unused81 | unused82 | unused83 | unused84 | unused85 | unused86 | unused87 | unused88 | unused89 | unused9 | unused90 | unused91 | unused92 | unused93 | unused94 | unused95 | unused96 | unused97 | unused98 | unused99 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

The config key the disk will be moved to on the target VM (for example, ide0 or scsi1). Default is the source disk key.

**`--target-vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_disk_rescan"></a>



**qm disk rescan** `[OPTIONS]`

重新扫描所有存储，并更新磁盘大小和未使用的磁盘映像。

**`--dryrun` `<boolean>` (*default \=* `0`)**

Do not actually write changes out to VM config(s).

**`--vmid` `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_disk_resize"></a>



**qm disk resize** `<vmid> <disk> <size>` `[OPTIONS]`

Extend volume size.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<disk>`: `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

要调整大小的磁盘。

**`<size>`: `\+?\d+(\.\d+)?[KMGT]?`**

The new size. With the `+` sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported.

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_qm_disk_unlink"></a>



**qm disk unlink** `<vmid> --idlist <string>` `[OPTIONS]`

Unlink/delete disk images.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--force` `<boolean>`**

Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called *unused\[n\]*, which contains the volume ID. Unlink of unused\[n\] always cause physical removal.

**`--idlist` `<string>`**

A list of disk IDs you want to delete.

<a id="cli_qm_enroll-efi-keys"></a>



**qm enroll-efi-keys** `<vmid>`

Enroll important updated certificates to the EFI disk with pre-enrolled-keys. Currently, these are UEFI 2023 certificates from Microsoft. Must be called while the VM is shut down.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_guest_cmd"></a>



**qm guest cmd** `<vmid> <command>`

Execute QEMU Guest Agent commands.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<command>`: `<fsfreeze-freeze | fsfreeze-status | fsfreeze-thaw | fstrim | get-fsinfo | get-host-name | get-memory-block-info | get-memory-blocks | get-osinfo | get-time | get-timezone | get-users | get-vcpus | info | network-get-interfaces | ping | shutdown | suspend-disk | suspend-hybrid | suspend-ram>`**

The QGA command.

<a id="cli_qm_guest_exec"></a>



**qm guest exec** `<vmid> [<extra-args>]` `[OPTIONS]`

Executes the given command via the guest agent

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--pass-stdin` `<boolean>` (*default \=* `0`)**

When set, read STDIN until EOF and forward to guest agent via *input-data* (usually treated as STDIN to process launched by guest agent). Allows maximal 1 MiB.

**`--synchronous` `<boolean>` (*default \=* `1`)**

If set to off, returns the pid immediately instead of waiting for the command to finish or the timeout.

**`--timeout` `<integer> (0 - N)` (*default \=* `30`)**

The maximum time to wait synchronously for the command to finish. If reached, the pid gets returned. Set to 0 to deactivate

<a id="cli_qm_guest_exec-status"></a>



**qm guest exec-status** `<vmid> <pid>`

Gets the status of the given pid started by the guest-agent

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<pid>`: `<integer>`**

The PID to query

<a id="cli_qm_guest_passwd"></a>



**qm guest passwd** `<vmid> <username>` `[OPTIONS]`

Sets the password for the given user to the given password

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<username>`: `<string>`**

The user to set the password for.

**`--crypted` `<boolean>` (*default \=* `0`)**

set to 1 if the password has already been passed through crypt()

<a id="cli_qm_help"></a>



**qm help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_qm_import"></a>



**qm import** `<vmid> <source> --storage <string>` `[OPTIONS]`

Import a foreign virtual guest from a supported import source, such as an ESXi storage.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<source>`: `<string>`**

The import source volume id.

**`--acpi` `<boolean>` (*default \=* `1`)**

Enable/disable ACPI.

**`--affinity` `<string>`**

List of host cores used to execute guest processes, for example: 0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

Enable/disable communication with the QEMU Guest Agent and its properties.

**`--allow-ksm` `<boolean>` (*default \=* `1`)**

Allow memory pages of this guest to be merged via KSM (Kernel Samepage Merging).

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

Secure Encrypted Virtualization (SEV) features by AMD CPUs

**`--arch` `<aarch64 | x86_64>`**

Virtual processor architecture. Defaults to the host architecture.

**`--args` `<string>`**

Arbitrary arguments passed to kvm.

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

Configure a audio device, useful in combination with QXL/Spice.

**`--autostart` `<boolean>` (*default \=* `0`)**

Automatic restart after crash (currently ignored).

**`--balloon` `<integer> (0 - N)`**

Amount of target RAM for the VM in MiB. The balloon driver is enabled by default, unless it is explicitly disabled by setting the value to zero.

**`--bios` `<ovmf | seabios>` (*default \=* `seabios`)**

Select BIOS implementation.

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

Specify guest boot order. Use the *order\=* sub-property as usage with no key or *legacy\=* is deprecated.

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

Enable booting from specified disk. Deprecated: Use *boot: order\=foo;bar* instead.

**`--cdrom` `<volume>`**

This is an alias for option -ide2

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init: Specify custom files to replace the automatically generated ones at start.

**`--cipassword` `<string>`**

cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords.

**`--citype` `<configdrive2 | nocloud | opennebula>`**

Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows.

**`--ciupgrade` `<boolean>` (*default \=* `1`)**

cloud-init: do an automatic package upgrade after the first boot.

**`--ciuser` `<string>`**

cloud-init: User name to change ssh keys and password for instead of the image’s configured default user.

**`--cores` `<integer> (1 - N)` (*default \=* `1`)**

The number of cores per socket.

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

Emulated CPU type.

**`--cpulimit` `<number> (0 - 128)` (*default \=* `0`)**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

CPU weight for a VM, will be clamped to \[1, 10000\] in cgroup v2.

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

Description for the VM. Shown in the web-interface VM’s summary. This is saved as comment inside the configuration file.

**`--dryrun` `<boolean>` (*default \=* `0`)**

Show the create command and exit without doing anything.

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

Configure a disk for storing EFI vars. Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Note that SIZE\_IN\_GiB is ignored here and that the default EFI vars are copied to the volume instead. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--format` `<qcow2 | raw | vmdk>`**

Target format

**`--freeze` `<boolean>`**

Freeze CPU at startup (use *c* monitor command to start execution).

**`--hookscript` `<string>`**

Script that will be executed during various steps in the vms lifetime.

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

Map host PCI devices into guest.

**`--hotplug` `<string>` (*default \=* `network,disk,usb`)**

Selectively enable hotplug features. This is a comma separated list of hotplug features: *network*, *disk*, *cpu*, *memory*, *usb* and *cloudinit*. Use *0* to disable hotplug completely. Using *1* as value is an alias for the default `network,disk,usb`. USB hotplugging is possible for guests with machine version \>\= 7.1 and ostype l26 or windows \> 7\.

**`--hugepages` `<1024 | 2 | any>`**

Enables hugepages memory.

Sets the size of hugepages in MiB. If the value is set to *any* then 1 GiB hugepages will be used if possible, otherwise the size will fall back to 2 MiB.

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Trusted Domain Extension (TDX) features by Intel CPUs

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string *dhcp* can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string *auto* can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4.

**`--ivshmem` `size=<integer> [,name=<string>]`**

Inter-VM shared memory. Useful for direct communication between VMs, or to the host.

**`--keephugepages` `<boolean>` (*default \=* `0`)**

Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts.

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

Keyboard layout for VNC server. This option is generally not required and is often better handled from within the guest OS.

**`--kvm` `<boolean>` (*default \=* `1`)**

Enable/disable KVM hardware virtualization.

**`--live-import` `<boolean>` (*default \=* `0`)**

Immediately start the VM and copy the data in the background.

**`--localtime` `<boolean>`**

Set the real time clock (RTC) to local time. This is enabled by default if the `ostype` indicates a Microsoft Windows OS.

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

Lock/unlock the VM.

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`--memory` `[current=]<integer>`**

Memory properties.

**`--migrate_downtime` `<number> (0 - N)` (*default \=* `0.1`)**

Set maximum tolerated downtime (in seconds) for migrations. Should the migration not be able to converge in the very end, because too much newly dirtied RAM needs to be transferred, the limit will be increased automatically step-by-step until migration can converge. Will be capped to 2000 seconds (maximum in QEMU).

**`--migrate_speed` `<integer> (0 - N)` (*default \=* `0`)**

Set maximum speed (in MB/s) for migrations. Value 0 is no limit.

**`--name` `<string>`**

Set a name for the VM. Only used on the configuration web interface.

**`--nameserver` `<string>`**

cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

Specify network devices.

**`--numa` `<boolean>` (*default \=* `0`)**

Enable/disable NUMA.

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA topology.

**`--onboot` `<boolean>` (*default \=* `0`)**

Specifies whether a VM will be started during system bootup.

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` (*default \=* `other`)**

Specify guest operating system.

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

Map host parallel devices (n is 0 to 2).

**`--protection` `<boolean>` (*default \=* `0`)**

Sets the protection flag of the VM. This will disable the remove VM and remove disk operations.

**`--reboot` `<boolean>` (*default \=* `1`)**

Allow reboot. If set to *0* the VM exit on reboot.

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

Configure a VirtIO-based Random Number Generator.

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` (*default \=* `lsi`)**

SCSI controller model

**`--searchdomain` `<string>`**

cloud-init: Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`--serial[n]` `(/dev/[^,]+|socket)`**

Create a serial device inside the VM (n is 0 to 3\)

**`--shares` `<integer> (0 - 50000)` (*default \=* `1000`)**

Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd.

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

Specify SMBIOS type 1 fields.

**`--smp` `<integer> (1 - N)` (*default \=* `1`)**

The number of CPUs. Please use option -sockets instead.

**`--sockets` `<integer> (1 - N)` (*default \=* `1`)**

The number of CPU sockets.

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

Configure additional enhancements for SPICE.

**`--sshkeys` `<string>`**

cloud-init: Setup public SSH keys (one key per line, OpenSSH format).

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` (*default \=* `now`)**

Set the initial date of the real time clock. Valid format for date are:'now' or *2006-06-17T16:01:21* or *2006-06-17*.

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--storage` `<storage ID>`**

Default storage.

**`--tablet` `<boolean>` (*default \=* `1`)**

Enable/disable the USB tablet device.

**`--tags` `<string>`**

Tags of the VM. This is only meta information.

**`--tdf` `<boolean>` (*default \=* `0`)**

Enable/disable time drift fix.

**`--template` `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

Configure a Disk for storing TPM state. The format is fixed to *raw*. Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Note that SIZE\_IN\_GiB is ignored here and 4 MiB will be used instead. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

Configure an USB device (n is 0 to 4, for machine version \>\= 7.1 and ostype l26 or windows \> 7, n can be up to 14).

**`--vcpus` `<integer> (1 - N)` (*default \=* `0`)**

Number of hotplugged vcpus.

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

Configure the VGA hardware.

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

Configuration for sharing a directory between host and guest using Virtio-fs.

**`--vmgenid` `<UUID>` (*default \=* `1 (autogenerated)`)**

Set VM Generation ID. Use *1* to autogenerate on create or update, pass *0* to disable explicitly.

**`--vmstatestorage` `<storage ID>`**

Default storage for VM state volumes/files.

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

Create a virtual hardware watchdog device.

<a id="cli_qm_importdisk"></a>



**qm importdisk**

An alias for *qm disk import*.

<a id="cli_qm_importovf"></a>



**qm importovf** `<vmid> <manifest> <storage>` `[OPTIONS]`

Create a new VM using parameters read from an OVF manifest

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<manifest>`: `<string>`**

path to the ovf file

**`<storage>`: `<storage ID>`**

Target storage ID

**`--dryrun` `<boolean>`**

Print a parsed representation of the extracted OVF parameters, but do not create a VM

**`--format` `<qcow2 | raw | vmdk>`**

Target format

<a id="cli_qm_list"></a>



**qm list** `[OPTIONS]`

Virtual machine index (per node).

**`--full` `<boolean>`**

Determine the full status of active VMs.

<a id="cli_qm_listsnapshot"></a>



**qm listsnapshot** `<vmid>`

列出所有快照。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_migrate"></a>



**qm migrate** `<vmid> <target>` `[OPTIONS]`

Migrate virtual machine. Creates a new migration task.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target>`: `<string>`**

目标节点。

**`--bwlimit` `<integer> (0 - N)` (*default \=* `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--force` `<boolean>`**

Allow to migrate VMs which use local devices. Only root may use this option.

**`--migration_network` `<string>`**

CIDR of the (sub) network that is used for migration.

**`--migration_type` `<insecure | secure>`**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`--online` `<boolean>`**

Use online/live migration if VM is running. Ignored if VM is stopped.

**`--targetstorage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

**`--with-conntrack-state` `<boolean>` (*default \=* `0`)**

Whether to migrate conntrack entries for running VMs.

**`--with-local-disks` `<boolean>`**

Enable live storage migration for local disk

<a id="cli_qm_monitor"></a>



**qm monitor** `<vmid>`

Enter QEMU Monitor interface.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_move-disk"></a>



**qm move-disk**

An alias for *qm disk move*.

<a id="cli_qm_move_disk"></a>



**qm move\_disk**

An alias for *qm disk move*.

<a id="cli_qm_mtunnel"></a>



**qm mtunnel**

Used by qmigrate \- do not use manually.

<a id="cli_qm_nbdstop"></a>



**qm nbdstop** `<vmid>`

Stop embedded nbd server.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_pending"></a>



**qm pending** `<vmid>`

Get the virtual machine configuration with both current and pending values.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_reboot"></a>



**qm reboot** `<vmid>` `[OPTIONS]`

Reboot the VM by shutting it down, and starting it again. Applies pending changes.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒以完成关机。

<a id="cli_qm_remote-migrate"></a>



**qm remote-migrate** `<vmid> [<target-vmid>] <target-endpoint> --target-bridge <string> --target-storage <string>` `[OPTIONS]`

Migrate virtual machine to a remote cluster. Creates a new migration task. EXPERIMENTAL feature!

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<target-endpoint>`: `apitoken=<PVEAPIToken=user@realm!token=SECRET> ,host=<ADDRESS> [,fingerprint=<FINGERPRINT>] [,port=<PORT>]`**

远程目标端点

**`--bwlimit` `<integer> (0 - N)` (*default \=* `migrate limit from datacenter or storage config`)**

覆盖 I/O 带宽限制（单位为 KiB/s）。

**`--delete` `<boolean>` (*default \=* `0`)**

Delete the original VM and related data after successful migration. By default the original VM is kept on the source cluster in a stopped state.

**`--online` `<boolean>`**

Use online/live migration if VM is running. Ignored if VM is stopped.

**`--target-bridge` `<string>`**

从源网桥到目标网桥的映射。仅提供一个网桥 ID 会将所有源网桥映射到该网桥。提供特殊值 *1* 会将每个源网桥映射到其自身。

**`--target-storage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

<a id="cli_qm_rescan"></a>



**qm rescan**

An alias for *qm disk rescan*.

<a id="cli_qm_reset"></a>



**qm reset** `<vmid>` `[OPTIONS]`

Reset virtual machine.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_qm_resize"></a>



**qm resize**

An alias for *qm disk resize*.

<a id="cli_qm_resume"></a>



**qm resume** `<vmid>` `[OPTIONS]`

Resume virtual machine.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--nocheck` `<boolean>`**

Do not check whether the VM is running, used internally during migration. Only root may use this option.

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_qm_rollback"></a>



**qm rollback** `<vmid> <snapname>` `[OPTIONS]`

Rollback VM state to specified snapshot.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--start` `<boolean>` (*default \=* `0`)**

Whether the VM should get started after rolling back successfully. (Note: VMs will be automatically started if the snapshot includes RAM.)

<a id="cli_qm_sendkey"></a>



**qm sendkey** `<vmid> <key>` `[OPTIONS]`

Send key event to virtual machine.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<key>`: `<string>`**

The key (qemu monitor encoding).

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

<a id="cli_qm_set"></a>



**qm set** `<vmid>` `[OPTIONS]`

Set virtual machine options (synchronous API) \- You should consider using the POST method instead for any actions involving hotplug or storage allocation.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--acpi` `<boolean>` (*default \=* `1`)**

Enable/disable ACPI.

**`--affinity` `<string>`**

List of host cores used to execute guest processes, for example: 0,5,8-11

**`--agent` `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

Enable/disable communication with the QEMU Guest Agent and its properties.

**`--allow-ksm` `<boolean>` (*default \=* `1`)**

Allow memory pages of this guest to be merged via KSM (Kernel Samepage Merging).

**`--amd-sev` `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

Secure Encrypted Virtualization (SEV) features by AMD CPUs

**`--arch` `<aarch64 | x86_64>`**

Virtual processor architecture. Defaults to the host architecture.

**`--args` `<string>`**

Arbitrary arguments passed to kvm.

**`--audio0` `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

Configure a audio device, useful in combination with QXL/Spice.

**`--autostart` `<boolean>` (*default \=* `0`)**

Automatic restart after crash (currently ignored).

**`--balloon` `<integer> (0 - N)`**

Amount of target RAM for the VM in MiB. The balloon driver is enabled by default, unless it is explicitly disabled by setting the value to zero.

**`--bios` `<ovmf | seabios>` (*default \=* `seabios`)**

Select BIOS implementation.

**`--boot` `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

Specify guest boot order. Use the *order\=* sub-property as usage with no key or *legacy\=* is deprecated.

**`--bootdisk` `(ide|sata|scsi|virtio)\d+`**

Enable booting from specified disk. Deprecated: Use *boot: order\=foo;bar* instead.

**`--cdrom` `<volume>`**

This is an alias for option -ide2

**`--cicustom` `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init: Specify custom files to replace the automatically generated ones at start.

**`--cipassword` `<password>`**

cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords.

**`--citype` `<configdrive2 | nocloud | opennebula>`**

Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows.

**`--ciupgrade` `<boolean>` (*default \=* `1`)**

cloud-init: do an automatic package upgrade after the first boot.

**`--ciuser` `<string>`**

cloud-init: User name to change ssh keys and password for instead of the image’s configured default user.

**`--cores` `<integer> (1 - N)` (*default \=* `1`)**

The number of cores per socket.

**`--cpu` `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

Emulated CPU type.

**`--cpulimit` `<number> (0 - 128)` (*default \=* `0`)**

CPU 使用限制。

**`--cpuunits` `<integer> (1 - 262144)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

CPU weight for a VM, will be clamped to \[1, 10000\] in cgroup v2.

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

Description for the VM. Shown in the web-interface VM’s summary. This is saved as comment inside the configuration file.

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--efidisk0` `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,import-from=<source volume>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

Configure a disk for storing EFI vars. Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Note that SIZE\_IN\_GiB is ignored here and that the default EFI vars are copied to the volume instead. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--force` `<boolean>`**

Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called *unused\[n\]*, which contains the volume ID. Unlink of unused\[n\] always cause physical removal.

{% hint style="info" %}
Requires option(s): `delete`
{% endhint %}

**`--freeze` `<boolean>`**

Freeze CPU at startup (use *c* monitor command to start execution).

**`--hookscript` `<string>`**

Script that will be executed during various steps in the vms lifetime.

**`--hostpci[n]` `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

Map host PCI devices into guest.

**`--hotplug` `<string>` (*default \=* `network,disk,usb`)**

Selectively enable hotplug features. This is a comma separated list of hotplug features: *network*, *disk*, *cpu*, *memory*, *usb* and *cloudinit*. Use *0* to disable hotplug completely. Using *1* as value is an alias for the default `network,disk,usb`. USB hotplugging is possible for guests with machine version \>\= 7.1 and ostype l26 or windows \> 7\.

**`--hugepages` `<1024 | 2 | any>`**

Enables hugepages memory.

Sets the size of hugepages in MiB. If the value is set to *any* then 1 GiB hugepages will be used if possible, otherwise the size will fall back to 2 MiB.

**`--ide[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--intel-tdx` `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Trusted Domain Extension (TDX) features by Intel CPUs

**`--ipconfig[n]` `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string *dhcp* can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string *auto* can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4.

**`--ivshmem` `size=<integer> [,name=<string>]`**

Inter-VM shared memory. Useful for direct communication between VMs, or to the host.

**`--keephugepages` `<boolean>` (*default \=* `0`)**

Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts.

**`--keyboard` `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

Keyboard layout for VNC server. This option is generally not required and is often better handled from within the guest OS.

**`--kvm` `<boolean>` (*default \=* `1`)**

Enable/disable KVM hardware virtualization.

**`--localtime` `<boolean>`**

Set the real time clock (RTC) to local time. This is enabled by default if the `ostype` indicates a Microsoft Windows OS.

**`--lock` `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

Lock/unlock the VM.

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`--memory` `[current=]<integer>`**

Memory properties.

**`--migrate_downtime` `<number> (0 - N)` (*default \=* `0.1`)**

Set maximum tolerated downtime (in seconds) for migrations. Should the migration not be able to converge in the very end, because too much newly dirtied RAM needs to be transferred, the limit will be increased automatically step-by-step until migration can converge. Will be capped to 2000 seconds (maximum in QEMU).

**`--migrate_speed` `<integer> (0 - N)` (*default \=* `0`)**

Set maximum speed (in MB/s) for migrations. Value 0 is no limit.

**`--name` `<string>`**

Set a name for the VM. Only used on the configuration web interface.

**`--nameserver` `<string>`**

cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`--net[n]` `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

Specify network devices.

**`--numa` `<boolean>` (*default \=* `0`)**

Enable/disable NUMA.

**`--numa[n]` `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA topology.

**`--onboot` `<boolean>` (*default \=* `0`)**

Specifies whether a VM will be started during system bootup.

**`--ostype` `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` (*default \=* `other`)**

Specify guest operating system.

**`--parallel[n]` `/dev/parport\d+|/dev/usb/lp\d+`**

Map host parallel devices (n is 0 to 2).

**`--protection` `<boolean>` (*default \=* `0`)**

Sets the protection flag of the VM. This will disable the remove VM and remove disk operations.

**`--reboot` `<boolean>` (*default \=* `1`)**

Allow reboot. If set to *0* the VM exit on reboot.

**`--revert` `<string>`**

撤销待处理的更改。

**`--rng0` `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

Configure a VirtIO-based Random Number Generator.

**`--sata[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--scsi[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--scsihw` `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` (*default \=* `lsi`)**

SCSI controller model

**`--searchdomain` `<string>`**

cloud-init: Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`--serial[n]` `(/dev/[^,]+|socket)`**

Create a serial device inside the VM (n is 0 to 3\)

**`--shares` `<integer> (0 - 50000)` (*default \=* `1000`)**

Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd.

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--smbios1` `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

Specify SMBIOS type 1 fields.

**`--smp` `<integer> (1 - N)` (*default \=* `1`)**

The number of CPUs. Please use option -sockets instead.

**`--sockets` `<integer> (1 - N)` (*default \=* `1`)**

The number of CPU sockets.

**`--spice_enhancements` `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

Configure additional enhancements for SPICE.

**`--sshkeys` `<filepath>`**

cloud-init: Setup public SSH keys (one key per line, OpenSSH format).

**`--startdate` `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` (*default \=* `now`)**

Set the initial date of the real time clock. Valid format for date are:'now' or *2006-06-17T16:01:21* or *2006-06-17*.

**`--startup` \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`--tablet` `<boolean>` (*default \=* `1`)**

Enable/disable the USB tablet device.

**`--tags` `<string>`**

Tags of the VM. This is only meta information.

**`--tdf` `<boolean>` (*default \=* `0`)**

Enable/disable time drift fix.

**`--template` `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`--tpmstate0` `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,import-from=<source volume>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

Configure a Disk for storing TPM state. The format is fixed to *raw*. Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Note that SIZE\_IN\_GiB is ignored here and 4 MiB will be used instead. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--unused[n]` `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`--usb[n]` `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

Configure an USB device (n is 0 to 4, for machine version \>\= 7.1 and ostype l26 or windows \> 7, n can be up to 14).

**`--vcpus` `<integer> (1 - N)` (*default \=* `0`)**

Number of hotplugged vcpus.

**`--vga` `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

Configure the VGA hardware.

**`--virtio[n]` `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,import-from=<source volume>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE\_ID:SIZE\_IN\_GiB to allocate a new volume. Use STORAGE\_ID:0 and the *import-from* parameter to import from an existing volume.

**`--virtiofs[n]` `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

Configuration for sharing a directory between host and guest using Virtio-fs.

**`--vmgenid` `<UUID>` (*default \=* `1 (autogenerated)`)**

Set VM Generation ID. Use *1* to autogenerate on create or update, pass *0* to disable explicitly.

**`--vmstatestorage` `<storage ID>`**

Default storage for VM state volumes/files.

**`--watchdog` `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

Create a virtual hardware watchdog device.

<a id="cli_qm_showcmd"></a>



**qm showcmd** `<vmid>` `[OPTIONS]`

Show command line which is used to start the VM (debug info).

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--pretty` `<boolean>` (*default \=* `0`)**

Puts each option on a new line to enhance human readability

**`--snapshot` `<string>`**

从指定快照获取配置值。

<a id="cli_qm_shutdown"></a>



**qm shutdown** `<vmid>` `[OPTIONS]`

Shutdown virtual machine. This is similar to pressing the power button on a physical machine. This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--forceStop` `<boolean>` (*default \=* `0`)**

Make sure the VM stops.

**`--keepActive` `<boolean>` (*default \=* `0`)**

Do not deactivate storage volumes.

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒。

<a id="cli_qm_snapshot"></a>



**qm snapshot** `<vmid> <snapname>` `[OPTIONS]`

Snapshot a VM.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`<snapname>`: `<string>`**

快照的名称。

**`--description` `<string>`**

文本描述或注释。

**`--vmstate` `<boolean>`**

Save the vmstate

<a id="cli_qm_start"></a>



**qm start** `<vmid>` `[OPTIONS]`

Start virtual machine.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--force-cpu` `<string>`**

Override QEMU’s -cpu argument with the given string.

**`--machine` `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`--migratedfrom` `<string>`**

集群节点名称。

**`--migration_network` `<string>`**

CIDR of the (sub) network that is used for migration.

**`--migration_type` `<insecure | secure>`**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`--nets-host-mtu` `net\d+=\d+(,net\d+=\d+)*`**

Used for migration compat. List of VirtIO network devices and their effective host\_mtu setting according to the QEMU object model on the source side of the migration. A value of 0 means that the host\_mtu parameter is to be avoided for the corresponding device.

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--stateuri` `<string>`**

Some command save/restore state from this location.

**`--targetstorage` `<string>`**

从源存储到目标存储的映射。仅提供一个存储 ID 会将所有源存储映射到该存储。提供特殊值 *1* 会将每个源存储映射到其自身。

**`--timeout` `<integer> (0 - N)` (*default \=* `max(30, vm memory in GiB)`)**

最多等待 timeout 秒。

**`--with-conntrack-state` `<boolean>` (*default \=* `0`)**

Whether to migrate conntrack entries for running VMs.

<a id="cli_qm_status"></a>



**qm status** `<vmid>` `[OPTIONS]`

Show VM status.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--verbose` `<boolean>`**

详细输出格式

<a id="cli_qm_stop"></a>



**qm stop** `<vmid>` `[OPTIONS]`

Stop virtual machine. The qemu process will exit immediately. This is akin to pulling the power plug of a running computer and may damage the VM data.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--keepActive` `<boolean>` (*default \=* `0`)**

Do not deactivate storage volumes.

**`--migratedfrom` `<string>`**

集群节点名称。

**`--overrule-shutdown` `<boolean>` (*default \=* `0`)**

Try to abort active *qmshutdown* tasks before stopping.

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--timeout` `<integer> (0 - N)`**

最多等待 timeout 秒。

<a id="cli_qm_suspend"></a>



**qm suspend** `<vmid>` `[OPTIONS]`

Suspend virtual machine.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--skiplock` `<boolean>`**

忽略锁——仅允许 root 使用此选项。

**`--statestorage` `<storage ID>`**

The storage for the VM state

{% hint style="info" %}
Requires option(s): `todisk`
{% endhint %}

**`--todisk` `<boolean>` (*default \=* `0`)**

If set, suspends the VM to disk. Will be resumed on next VM start.

<a id="cli_qm_template"></a>



**qm template** `<vmid>` `[OPTIONS]`

创建模板。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--disk` `<efidisk0 | ide0 | ide1 | ide2 | ide3 | sata0 | sata1 | sata2 | sata3 | sata4 | sata5 | scsi0 | scsi1 | scsi10 | scsi11 | scsi12 | scsi13 | scsi14 | scsi15 | scsi16 | scsi17 | scsi18 | scsi19 | scsi2 | scsi20 | scsi21 | scsi22 | scsi23 | scsi24 | scsi25 | scsi26 | scsi27 | scsi28 | scsi29 | scsi3 | scsi30 | scsi4 | scsi5 | scsi6 | scsi7 | scsi8 | scsi9 | tpmstate0 | virtio0 | virtio1 | virtio10 | virtio11 | virtio12 | virtio13 | virtio14 | virtio15 | virtio2 | virtio3 | virtio4 | virtio5 | virtio6 | virtio7 | virtio8 | virtio9>`**

If you want to convert only 1 disk to base image.

<a id="cli_qm_terminal"></a>



**qm terminal** `<vmid>` `[OPTIONS]`

Open a terminal using a serial device (The VM need to have a serial device configured, for example *serial0: socket*)

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--escape` `<string>` (*default \=* `^O`)**

Escape character.

**`--iface` `<serial0 | serial1 | serial2 | serial3>`**

Select the serial device. By default we simply use the first suitable device.

<a id="cli_qm_unlink"></a>



**qm unlink**

An alias for *qm disk unlink*.

<a id="cli_qm_unlock"></a>



**qm unlock** `<vmid>`

解锁 VM。

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_vncproxy"></a>



**qm vncproxy** `<vmid>`

Proxy VM VNC traffic to stdin/stdout

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

<a id="cli_qm_wait"></a>



**qm wait** `<vmid>` `[OPTIONS]`

Wait until the VM is stopped.

**`<vmid>`: `<integer> (100 - 999999999)`**

VM 的唯一 ID。

**`--timeout` `<integer> (1 - N)`**

Timeout in seconds. Default is to wait forever.

## DESCRIPTION <a href="#_description" id="_description"></a>

QEMU（Quick Emulator 的缩写）是一种开源虚拟机监控程序，用于模拟物理计算机。从运行 QEMU 的宿主系统的角度来看，QEMU 是一个用户程序，可以访问分区、文件、网卡等多种本地资源，然后将这些资源传递给模拟计算机，后者将它们视为真实设备。

在模拟计算机中运行的客户机操作系统会访问这些设备，并像在真实硬件上运行一样工作。例如，可以将 ISO 镜像作为参数传递给 QEMU，在模拟计算机中运行的操作系统就会看到 CD 驱动器中插入了一张真实的 CD-ROM。

QEMU 可以模拟从 ARM 到 Sparc 的多种硬件。在 x86 宿主机上，Proxmox VE 关注 32 位和 64 位 PC 兼容机模拟，因为它们代表了绝大多数服务器硬件。在 arm64 宿主机上，Proxmox VE 则模拟 64 位 ARM（aarch64）机器。模拟与宿主机相同的架构也是最快的选项之一，因为当模拟架构与宿主机架构匹配时，可用的处理器扩展可以大幅加速 QEMU。

{% hint style="info" %}
有时您会遇到术语 *KVM*（Kernel-based Virtual Machine，基于内核的虚拟机）。它表示 QEMU 通过 Linux KVM 模块，在处理器虚拟化扩展的支持下运行。在 Proxmox VE 的语境中，*QEMU* 和 *KVM* 可以互换使用，因为 Proxmox VE 中的 QEMU 始终会尝试加载 KVM 模块。
{% endhint %}

Proxmox VE 内部的 QEMU 以 root 进程运行，因为访问块设备和 PCI 设备需要这样做。

## Emulated devices and paravirtualized devices <a href="#_emulated_devices_and_paravirtualized_devices" id="_emulated_devices_and_paravirtualized_devices"></a>

QEMU 模拟的 PC 硬件包括主板、网络控制器、SCSI、IDE 和 SATA 控制器、串口（完整列表见 `kvm(1)` 手册页），所有这些都由软件模拟。所有这些设备都是现有硬件设备的精确软件等效物，如果客户机中运行的操作系统具有适当的驱动程序，就会像在真实硬件上运行一样使用这些设备。这使 QEMU 能够运行*未经修改的*操作系统。

然而，这会带来性能开销，因为让原本应由硬件执行的功能通过软件运行，会给宿主机 CPU 带来大量额外工作。为缓解这一问题，QEMU 可以向客户机操作系统提供*半虚拟化设备*，此时客户机操作系统会识别出自己正在 QEMU 内运行，并与虚拟机监控程序协作。

QEMU 依赖 virtio 虚拟化标准，因此能够提供半虚拟化 virtio 设备，包括半虚拟化通用磁盘控制器、半虚拟化网卡、半虚拟化串口、半虚拟化 SCSI 控制器等……

{% hint style="success" %}
**强烈建议**尽可能使用 virtio 设备，因为它们可以显著提升性能，而且通常维护得更好。根据 `bonnie++(8)` 的测量结果，与模拟 IDE 控制器相比，使用 virtio 通用磁盘控制器可使顺序写入吞吐量翻倍。根据 `iperf(1)` 的测量结果，使用 virtio 网络接口可提供最高达模拟 Intel E1000 网卡三倍的吞吐量。[\[1\]](#note-0cdd31f9-1)
{% endhint %}

## Virtual Machines Settings <a href="#qm_virtual_machines_settings" id="qm_virtual_machines_settings"></a>

一般来说，Proxmox VE 会尝试为虚拟机（VM）选择合理的默认设置。请确保理解所更改设置的含义，因为这可能会导致性能下降，或使数据面临风险。

### General Settings <a href="#qm_general_settings" id="qm_general_settings"></a>

[![screenshot/gui-create-vm-general.png](../assets/screenshot-gui-create-vm-general-png-60617f9d68b1.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-general.png)

虚拟机的常规设置包括

- **节点**：虚拟机将运行的物理服务器
- **VM ID**：此 Proxmox VE 安装中用于标识虚拟机的唯一编号
- **Name**: a free form text string you can use to describe the VM
- **Resource Pool**: a logical group of VMs

### OS Settings <a href="#qm_os_settings" id="qm_os_settings"></a>

[![screenshot/gui-create-vm-os.png](../assets/screenshot-gui-create-vm-os-png-2f840c53a6ca.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-os.png)

创建虚拟机（VM）时，设置正确的操作系统（OS）可让 Proxmox VE 优化某些底层参数。例如，Windows 操作系统期望 BIOS 时钟使用本地时间，而基于 Unix 的操作系统期望 BIOS 时钟使用 UTC 时间。

### System Settings <a href="#qm_system_settings" id="qm_system_settings"></a>

On VM creation you can change some basic system components of the new VM. You can specify which [display type](#qm_display) you want to use.

[![screenshot/gui-create-vm-system.png](../assets/screenshot-gui-create-vm-system-png-511b121389af.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-system.png)

Additionally, the [SCSI controller](#qm_hard_disk) can be changed. If you plan to install the QEMU Guest Agent, or if your selected ISO image already ships and installs it automatically, you may want to tick the *QEMU Agent* box, which lets Proxmox VE know that it can use its features to show some more information, and complete some actions (for example, shutdown or snapshots) more intelligently.

Proxmox VE allows to boot VMs with different firmware and machine types, namely [SeaBIOS and OVMF](#qm_bios_and_uefi). In most cases you want to switch from the default SeaBIOS to OVMF only if you plan to use [PCIe passthrough](#qm_pci_passthrough). On arm64 hosts OVMF is the default and only option, as SeaBIOS is x86-only.

#### Machine Type <a href="#qm_machine_type" id="qm_machine_type"></a>

A VM’s *Machine Type* defines the hardware layout of the VM’s virtual motherboard. You can choose between the default [Intel 440FX](https://en.wikipedia.org/wiki/Intel_440FX) or the [Q35](https://ark.intel.com/content/www/us/en/ark/products/31918/intel-82q35-graphics-and-memory-controller.html) chipset, which also provides a virtual PCIe bus, and thus may be desired if you want to pass through PCIe hardware. Additionally, you can select a [vIOMMU](#qm_pci_viommu) implementation.

{% hint style="info" %}
Intel 440FX 和 Q35 芯片组专用于 x86 客户机。在 arm64 宿主机上，虚拟机使用`virt`机器类型，该类型模拟一种通用的、基于 UEFI 的 ARM 机器。
{% endhint %}

##### Machine Version <a href="#_machine_version" id="_machine_version"></a>

每种机器类型在 QEMU 中都有版本，并且给定的 QEMU 二进制文件支持多种机器版本。新版本可能带来对新功能的支持、修复或一般性改进。但是，它们也会更改虚拟硬件的属性。为避免从客户机角度来看发生突然变化，并确保虚拟机状态、在线迁移和包含 RAM 的快照的兼容性，新的 QEMU 实例将继续使用相同的机器版本。

对于 Windows 客户机，机器版本会在创建时固定，因为 Windows 对虚拟硬件的更改很敏感，即使是在冷启动之间也是如此。例如，不同的机器版本可能会导致网络设备的枚举不同。Linux 等其他操作系统通常可以很好地应对此类更改。对于这些操作系统，默认使用*最新*机器版本。这意味着在全新启动后，将使用 QEMU 二进制文件支持的最新机器版本（例如，QEMU 8.1 支持的每种机器类型的最新机器版本均为 8.1 版）。

在实现会更改硬件布局的新功能或修复时，机器版本还用作确保向后兼容的保障措施。对于正在运行的虚拟机上的操作（例如在线迁移），会保存正在运行的机器版本，以确保虚拟机能够完全按原样恢复，这不仅涉及 QEMU 虚拟化层面，还涉及 Proxmox VE 创建 QEMU 虚拟机实例的方式。

**PVE 机器修订版本**

有时，Proxmox VE 需要更改硬件布局或修改选项，而不能等待新的 QEMU 版本发布。为此，Proxmox VE 以`+pveX`的形式添加了额外的下游修订版本。在这些修订版本中，每个新 QEMU 机器版本的`X`均为 0，并且在这种情况下会省略，例如机器版本`pc-q35-9.2`与机器版本`pc-q35-9.2+pve0`相同。

如果 Proxmox VE 需要更改硬件布局或默认选项，则会递增修订版本，并将其用于新创建的客户机，或在始终使用最新机器版本的虚拟机重启时使用。

##### QEMU Machine Version Deprecation <a href="#_qemu_machine_version_deprecation" id="_qemu_machine_version_deprecation"></a>

从 QEMU 10.1 开始，机器版本在上游 QEMU 中保留 6 年后会被移除。Proxmox VE 大约每 2 年发布一个主要版本，因此一个 Proxmox VE 主要版本将支持来自大约前两个 Proxmox VE 主要版本的机器版本。

Before upgrading to a new major Proxmox VE release, you should update VM configurations to avoid all machine versions that will be dropped during the next major Proxmox VE release. This ensures that the guests can still be used throughout that release. See the section [Update to a Newer Machine Version](#qm_machine_update).

移除策略尚未在 Proxmox VE 8 中生效，因此受支持机器版本的基线为 2.4。为 Proxmox VE 9 发布的最后一个 QEMU 二进制版本预计将是 QEMU 11.2。此 QEMU 二进制文件将移除对低于 6.0 的机器版本的支持，因此 6.0 是 Proxmox VE 9 发布生命周期的基线。预计每次 Proxmox VE 主版本发布时，基线都会提高两个主版本，例如 Proxmox VE 10 的基线为 8.0。

##### Update to a Newer Machine Version <a href="#qm_machine_update" id="qm_machine_update"></a>

如果看到弃用警告，应将机器版本更改为较新的版本。请务必先准备好可用的备份，并做好客户机识别硬件的方式可能发生变化的准备。在某些情况下，可能需要重新安装特定驱动程序。还应检查使用这些机器版本创建的含内存快照（即 `runningmachine` 配置项）。遗憾的是，无法更改快照的机器版本，因此需要加载该快照以挽救其中的任何数据。

### Hard Disk <a href="#qm_hard_disk" id="qm_hard_disk"></a>

#### Bus/Controller <a href="#qm_hard_disk_bus" id="qm_hard_disk_bus"></a>

QEMU 可以模拟多种存储控制器：

{% hint style="success" %}
出于性能考虑，并且由于它们得到了更好的维护，强烈建议使用 **VirtIO SCSI** 或 **VirtIO Block** 控制器。
{% endhint %}

- **IDE** 控制器的设计可追溯至 1984 年的 PC/AT 磁盘控制器。尽管这种控制器已被较新的设计所取代，但您能想到的每一种操作系统都支持它，因此，如果要运行 2003 年之前发布的操作系统，它是一个很好的选择。此控制器最多可连接 4 个设备。
- **SATA**（Serial ATA）控制器诞生于 2003 年，采用更现代的设计，可实现更高的吞吐量并连接更多设备。此控制器最多可连接 6 个设备。
- **SCSI** 控制器设计于 1985 年，常见于服务器级硬件，最多可连接 14 个存储设备。Proxmox VE 默认模拟 LSI 53C895A 控制器。

  A SCSI controller of type *VirtIO SCSI single* and enabling the [IO Thread](#qm_hard_disk_iothread) setting for the attached disks is recommended if you aim for performance. This is the default for newly created Linux VMs since Proxmox VE 7.3. Each disk will have its own *VirtIO SCSI* controller, and QEMU will handle the disks IO in a dedicated thread. Linux distributions have support for this controller since 2012, and FreeBSD since 2014\. For Windows OSes, you need to provide an extra ISO containing the drivers during the installation.
- **VirtIO Block** 控制器通常简称为 VirtIO 或 virtio-blk，是一种较旧的半虚拟化控制器。在功能方面，它已被 VirtIO SCSI 控制器取代。

#### Image Format <a href="#qm_hard_disk_formats" id="qm_hard_disk_formats"></a>

每个控制器上都连接有若干模拟硬盘，这些硬盘由所配置存储中的文件或块设备提供后端支持。存储类型的选择将决定硬盘镜像的格式。提供块设备的存储（LVM、ZFS、Ceph）需要使用 **raw disk image format**，而基于文件的存储（如 Ext4、XFS、NFS 或 CIFS）则允许选择 **raw disk image format** 或 **QEMU image format**。

- **QEMU image format** 是一种写时复制格式，支持快照和磁盘镜像的精简置备。
- the **raw disk image** is a bit-to-bit image of a hard disk, similar to what you would get when executing the `dd` command on a block device in Linux. This format does not support thin provisioning or snapshots by itself, requiring cooperation from the storage layer for these tasks. It may, however, be up to 10% faster than the **QEMU image format**. [\[2\]](#note-0cdd31f9-2)
- 只有打算将磁盘镜像导入或导出到其他虚拟机管理程序时，**VMware image format** 才有意义。

#### Cache Mode <a href="#qm_hard_disk_cache" id="qm_hard_disk_cache"></a>

设置硬盘的 **Cache** 模式会影响宿主机系统如何向客户机系统通知块写入完成。默认的 **No cache** 表示当每个块到达物理存储写入队列时，客户机系统就会收到写入完成通知，并忽略宿主机页缓存。这在安全性和速度之间提供了良好的平衡。

如果希望 Proxmox VE 备份管理器在备份 VM 时跳过某个磁盘，可以在该磁盘上设置 **No backup** 选项。

如果希望 Proxmox VE 存储复制机制在启动复制任务时跳过某个磁盘，可以在该磁盘上设置 **Skip replication** 选项。自 Proxmox VE 5.0 起，复制要求磁盘镜像位于类型为 `zfspool` 的存储上，因此，当 VM 配置了复制时，如果将磁盘镜像添加到其他存储，则必须跳过此磁盘镜像的复制。

#### Trim/Discard <a href="#qm_hard_disk_discard" id="qm_hard_disk_discard"></a>

If your storage supports *thin provisioning* (see the storage chapter in the Proxmox VE guide), you can activate the **Discard** option on a drive. With **Discard** set and a *TRIM*-enabled guest OS [\[3\]](#note-0cdd31f9-3), when the VM’s filesystem marks blocks as unused after deleting files, the controller will relay this information to the storage, which will then shrink the disk image accordingly. For the guest to be able to issue *TRIM* commands, you must enable the **Discard** option on the drive. Some guest operating systems may also require the **SSD Emulation** flag to be set. Note that **Discard** on **VirtIO Block** drives is only supported on guests using Linux Kernel 5.0 or higher.

If you would like a drive to be presented to the guest as a solid-state drive rather than a rotational hard disk, you can set the **SSD emulation** option on that drive. There is no requirement that the underlying storage actually be backed by SSDs; this feature can be used with physical media of any type. Note that **SSD emulation** is not supported on **VirtIO Block** drives.

#### IO Thread <a href="#qm_hard_disk_iothread" id="qm_hard_disk_iothread"></a>

**IO thread** 选项只能用于采用以下总线/设备控制器之一的磁盘：

- **SCSI**, if the emulated SCSI controller type is **VirtIO SCSI single**, or
- **VirtIO Block**

启用 **IO thread** 后，QEMU 会为每个存储控制器创建一个 I/O 线程，而不是在主事件循环或 vCPU 线程中处理所有 I/O。其好处之一是能够更好地分配工作并利用底层存储。另一个好处是，当宿主机工作负载的 I/O 非常密集时，可降低客户机中的延迟（卡顿），因为主线程和 vCPU 线程都不会被磁盘 I/O 阻塞。

### CPU <a href="#qm_cpu" id="qm_cpu"></a>

[![screenshot/gui-create-vm-cpu.png](../assets/screenshot-gui-create-vm-cpu-png-cf8772d20d7e.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-cpu.png)

**CPU socket** 是 PC 主板上用于插入 CPU 的物理插槽。该 CPU 可以包含一个或多个 **cores**，它们是独立的处理单元。从性能角度看，使用一个 4 核 CPU 插槽还是两个双核 CPU 插槽基本没有区别。但是，某些软件许可证取决于机器拥有的插槽数量，在这种情况下，将插槽数量设置为许可证允许的数量是合理的。

增加虚拟 CPU（核心和插槽）的数量通常会提升性能，但这在很大程度上取决于 VM 的用途。多线程应用程序当然会从大量虚拟 CPU 中受益，因为每添加一个虚拟 CPU，QEMU 都会在宿主机系统上创建一个新的执行线程。如果不确定 VM 的工作负载，将 **Total cores** 的数量设置为 2 通常比较稳妥。

{% hint style="info" %}
所有 VM 的核心*总数*大于服务器上的核心数量是完全安全的（例如，在只有 8 个核心的机器上运行 4 个各有 4 个核心的 VM，总计 16 个核心）。在这种情况下，宿主机系统会在服务器核心之间平衡 QEMU 执行线程，就像运行标准的多线程应用程序一样。但是，Proxmox VE 会阻止您启动虚拟 CPU 核心数超过物理可用核心数的 VM，因为这只会因上下文切换的开销而降低性能。
{% endhint %}

#### Resource Limits <a href="#qm_cpu_resource_limits" id="qm_cpu_resource_limits"></a>

**cpulimit**

除了虚拟核心数量外，还可以使用 **cpulimit** 选项设置 VM 可用的“宿主机 CPU 时间”总量。它是一个浮点值，以百分比表示 CPU 时间，因此 `1.0` 等于 `100%`，`2.5` 等于 `250%`，依此类推。如果单个进程完全占用一个核心，其 CPU 时间使用率将为 `100%`。如果一个四核 VM 完全利用其所有核心，理论上将使用 `400%`。实际使用率可能还会稍高一些，因为除了 vCPU 核心线程之外，QEMU 还可以为 VM 外围设备运行额外的线程。

当 VM 因并行运行某些进程而需要多个 vCPU，但又不希望整个 VM 能够同时以 100% 的利用率运行所有 vCPU 时，此设置会很有用。

例如，假设有一台虚拟机可从 8 个虚拟 CPU 中受益，但您不希望该 VM 能够让所有 8 个核心都满载运行，因为这会使服务器过载，导致其他虚拟机和容器获得的 CPU 时间过少。要解决此问题，可以将 **cpulimit** 设置为 `4.0`（\=400%）。这意味着，如果 VM 通过同时运行 8 个进程来充分利用所有 8 个虚拟 CPU，则每个 vCPU 最多能从物理核心获得 50% 的 CPU 时间。但是，如果 VM 工作负载仅充分利用 4 个虚拟 CPU，则每个虚拟 CPU 仍可从物理核心获得最多 100% 的 CPU 时间，总计为 400%。

{% hint style="info" %}
根据配置，VM 可以使用额外的线程，例如用于网络或 I/O 操作的线程，以及用于在线迁移的线程。因此，VM 显示的 CPU 时间用量可能超过其虚拟 CPU 本身所能使用的量。要确保 VM 使用的 CPU 时间永远不会超过所分配的 vCPU 可使用的量，请将 **cpulimit** 设置为与核心总数相同的值。
{% endhint %}

**cpuunits**

通过 **cpuunits** 选项（如今通常称为 CPU 份额或 CPU 权重），可以控制 VM 与其他正在运行的 VM 相比能获得多少 CPU 时间。它是一个相对权重，默认值为 `100`（如果宿主机使用旧版 cgroup v1，则为 `1024`）。如果提高某个 VM 的此值，与权重较低的其他 VM 相比，调度器会优先调度该 VM。

例如，如果 VM 100 使用默认值 `100`，而 VM 200 被更改为 `200`，则后一个 VM 200 获得的 CPU 带宽将是前一个 VM 100 的两倍。

有关更多信息，请参阅 `man systemd.resource-control`，其中 `CPUQuota` 对应于 `cpulimit`，`CPUWeight` 对应于我们的 `cpuunits` 设置。请访问其 Notes 部分，查看参考资料和实现细节。

**affinity**

通过 **affinity** 选项，可以指定用于运行 VM vCPU 的物理 CPU 核心。I/O 等外围 VM 进程不受此设置影响。请注意，**CPU 亲和性不是一项安全功能**。

强制设置 CPU **affinity** 在某些情况下可能很有意义，但也会增加复杂性和维护工作量。例如，以后需要添加更多 VM，或将 VM 迁移到 CPU 核心数较少的节点时。如果某些 CPU 已得到充分利用，而其他 CPU 几乎处于空闲状态，还很容易造成 CPU 使用不均衡，进而导致系统性能受限。

The **affinity** is set through the `taskset` CLI tool. It accepts the host CPU numbers (see `lscpu`) in the `List Format` from `man cpuset`. This ASCII decimal list can contain numbers but also number ranges. For example, the **affinity**
`0-1,8-11` (expanded `0, 1, 8, 9, 10, 11`) would allow the VM to run on only these six specific host cores.

#### CPU Type <a href="#_cpu_type" id="_cpu_type"></a>

QEMU can emulate a number different of **CPU types** from 486 to the latest Xeon processors. Each new processor generation adds new features, like hardware assisted 3d rendering, random number generation, memory protection, etc. Also, a current generation can be upgraded through microcode update with bug or security fixes.

通常，应为 VM 选择与宿主机系统 CPU 尽量接近的处理器类型，这样宿主机 CPU 功能（也称为 *CPU 标志*）将在 VM 中可用。如果需要完全匹配，可以将 CPU 类型设置为 **host**，此时 VM 将具有与宿主机系统完全相同的 CPU 标志。

不过，这有一个缺点。如果要在不同宿主机之间在线迁移 VM，VM 最终可能会运行在一个 CPU 类型或微代码版本不同的新系统上。如果传递给客户机的 CPU 标志缺失，QEMU 进程将停止。为解决这一问题，QEMU 还提供了自己的虚拟 CPU 类型，Proxmox VE 默认使用这些类型。

后端默认值为 *kvm64*，它基本上适用于所有 x86\_64 宿主机 CPU；而在 UI 中创建新 VM 时，默认值为 *x86-64-v2-AES*，后者要求 Intel 宿主机 CPU 至少为 Westmere，AMD 宿主机 CPU 至少为第四代 Opteron。

{% hint style="info" %}
这里介绍的 *kvm64* 和 *x86-64-v\** CPU 模型仅适用于 x86。在 arm64 宿主机上，客户机使用 ARM CPU 模型：*host* 用于暴露物理 CPU（在受支持的硬件上建议使用），或使用 *max* 等通用模型，并搭配 `virt` 机器类型。
{% endhint %}

简而言之：

如果不关心在线迁移，或者集群是同构的，即所有节点都具有相同的 CPU 和相同的微代码版本，请将 CPU 类型设置为 host，因为理论上这将使客户机获得最大性能。

如果关心在线迁移和安全性，并且只有 Intel CPU 或只有 AMD CPU，请选择集群中最低代次的 CPU 模型。

如果关心在线迁移但不关心安全性，或者集群混用了 Intel/AMD CPU，请选择兼容的最低级别 QEMU 虚拟 CPU 类型。

{% hint style="info" %}
Intel 和 AMD 宿主机 CPU 之间的在线迁移不保证能够正常工作。
{% endhint %}

See also List of AMD and Intel CPU Types as Defined in QEMU.

#### QEMU CPU Types <a href="#_qemu_cpu_types" id="_qemu_cpu_types"></a>

QEMU 还提供与 Intel 和 AMD 宿主机 CPU 均兼容的虚拟 CPU 类型。

{% hint style="info" %}
To mitigate the Spectre vulnerability for virtual CPU types, you need to add the relevant CPU flags, see [Meltdown / Spectre related CPU flags](#qm_meltdown_spectre).
{% endhint %}

历史上，Proxmox VE 使用 *kvm64* CPU 模型，其启用的 CPU 标志处于 Pentium 4 水平，因此对于某些工作负载，性能并不理想。

2020 年夏，AMD、Intel、Red Hat 和 SUSE 合作在 x86-64 基线之上定义了三个 x86-64 微架构级别，并启用了现代标志。详情请参阅 [x86-64-ABI 规范](https://gitlab.com/x86-psABIs/x86-64-ABI)。

{% hint style="info" %}
一些较新的发行版（如 CentOS 9）现在构建时将 *x86-64-v2* 标志作为最低要求。
{% endhint %}

- *kvm64 (x86-64-v1)*: Compatible with Intel CPU \>\= Pentium 4, AMD CPU \>\= Phenom.
- *x86-64-v2*: Compatible with Intel CPU \>\= Nehalem, AMD CPU \>\= Opteron\_G3. Added CPU flags compared to *x86-64-v1*: *\+cx16*, *\+lahf-lm*, *\+popcnt*, *\+pni*, *\+sse4.1*, *\+sse4.2*, *\+ssse3*.
- *x86-64-v2-AES*: Compatible with Intel CPU \>\= Westmere, AMD CPU \>\= Opteron\_G4. Added CPU flags compared to *x86-64-v2*: *\+aes*.
- *x86-64-v3*: Compatible with Intel CPU \>\= Haswell, AMD CPU \>\= EPYC. Added CPU flags compared to *x86-64-v2-AES*: *\+avx*, *\+avx2*, *\+bmi1*, *\+bmi2*, *\+f16c*, *\+fma*, *\+movbe*, *\+xsave*.
- *x86-64-v4*: Compatible with Intel CPU \>\= Skylake, AMD CPU \>\= EPYC v4 Genoa. Added CPU flags compared to *x86-64-v3*: *\+avx512f*, *\+avx512bw*, *\+avx512cd*, *\+avx512dq*, *\+avx512vl*.

#### Custom CPU Types <a href="#_custom_cpu_types" id="_custom_cpu_types"></a>

可以定义自定义 CPU 类型，配置其基础模型、厂商、物理地址位数以及各标志的开关，然后像内置类型一样将其分配给 VM。在 VM 配置中，自定义类型以 `custom-<name>` 的形式引用。

在 Web UI 中的 `Datacenter -> Custom CPU Models` 下管理这些类型。模型对话框内嵌一个标志编辑器网格，支持按标志名称和描述进行自由文本搜索，提供加速器（kvm/tcg）选择器，并提供按节点选择的多选框；该多选框会突出显示每个所选集群节点当前报告为受支持的标志，有助于在确定模型之前，识别哪些标志在目标宿主机上实际可用。同一网格还用于每个 VM 的 `Processor` 编辑对话框，但在该对话框中仅限显示可为单个 VM 设置的标志；如果配置的标志不被 API 识别或不受所选加速器支持，则会在顶部显示警告。

自定义 CPU 类型仍由配置文件 `/etc/pve/virtual-guest/cpu-models.conf` 提供支持，也可以通过 CLI 维护，格式请参阅 `man cpu-models.conf`。

对自定义模型的访问通过 ACL 路径 `/mapping/cpu/<name>` 按模型分别控制。`Mapping.Audit` 允许用户在列表中查看模型，`Mapping.Modify` 控制是否可在面板中创建、更新和删除模型，`Mapping.Use` 则是将模型分配给 VM 所必需的权限。后者会在创建 VM、更新 VM 和克隆 VM 时强制执行，因此，即使用户可以克隆使用自定义模型的 VM，仍需要在该模型的 ACL 路径上拥有 `Mapping.Use` 权限。

#### Meltdown / Spectre related CPU flags <a href="#qm_meltdown_spectre" id="qm_meltdown_spectre"></a>

有多个与 Meltdown 和 Spectre 漏洞相关的 CPU 标志 [\[4\]](#note-0cdd31f9-4)，除非为 VM 选择的 CPU 类型默认已启用这些标志，否则需要手动设置。

要使用这些 CPU 标志，必须满足以下两个要求：

- 宿主机 CPU 必须支持该功能，并将其传递给客户机的虚拟 CPU
- 客户机操作系统必须更新到能够缓解这些攻击并能够利用该 CPU 功能的版本

否则，需要设置虚拟 CPU 所需的 CPU 标志，即设置 *flags* 属性（VM 配置文件中 *cpu* 选项的属性），或者在 Web UI 中编辑 CPU 选项。

For Spectre v1,v2,v4 fixes, your CPU or system vendor also needs to provide a so-called “microcode update” for your CPU, see chapter Firmware Updates. Note that not all affected CPUs can be updated to support spec-ctrl.

要检查 Proxmox VE 宿主机是否存在漏洞，请以 root 身份执行以下命令：

```text
for f in /sys/devices/system/cpu/vulnerabilities/*; do echo "${f##*/} -" $(cat "$f"); done
```

还有一个社区脚本可用于检测宿主机是否仍存在漏洞。[\[5\]](#note-0cdd31f9-5)

#### Intel processors <a href="#_intel_processors" id="_intel_processors"></a>

- *pcid*

  这可降低称为 *内核页表隔离（KPTI）* 的 Meltdown（CVE-2017-5754）缓解措施对性能的影响；KPTI 可有效地向用户空间隐藏内核内存。如果没有 PCID，KPTI 是一种开销相当大的机制 [\[6\]](#note-0cdd31f9-6)。

  要检查 Proxmox VE 宿主机是否支持 PCID，请以 root 身份执行以下命令：

  ```text
  # grep ' pcid ' /proc/cpuinfo
  ```

  如果返回结果不为空，则表示宿主机的 CPU 支持 *pcid*。
- *spec-ctrl*

  在 retpoline 不足以解决问题的情况下，需要此标志来启用 Spectre v1（CVE-2017-5753）和 Spectre v2（CVE-2017-5715）修复。默认包含在带有 -IBRS 后缀的 Intel CPU 模型中。对于不带 -IBRS 后缀的 Intel CPU 模型，必须显式启用。需要更新宿主机 CPU 微代码（intel-microcode \>\= 20180425）。
- *ssbd*

  需要此标志来启用 Spectre V4（CVE-2018-3639）修复。默认不包含在任何 Intel CPU 模型中。对于所有 Intel CPU 模型，都必须显式启用。需要更新宿主机 CPU 微代码（intel-microcode \>\= 20180703）。

#### AMD processors <a href="#_amd_processors" id="_amd_processors"></a>

- *ibpb*

  在 retpoline 不足以解决问题的情况下，需要此标志来启用 Spectre v1（CVE-2017-5753）和 Spectre v2（CVE-2017-5715）修复。默认包含在带有 -IBPB 后缀的 AMD CPU 模型中。对于不带 -IBPB 后缀的 AMD CPU 模型，必须显式启用。宿主机 CPU 微代码必须先支持此功能，才能将其用于客户机 CPU。
- *virt-ssbd*

  需要此标志来启用 Spectre v4（CVE-2018-3639）修复。默认不包含在任何 AMD CPU 模型中。对于所有 AMD CPU 模型，都必须显式启用。即使也提供了 amd-ssbd，也应向客户机提供此标志，以最大限度地提高客户机兼容性。请注意，使用 "host" CPU 模型时必须显式启用此标志，因为这是一项物理 CPU 中不存在的虚拟功能。
- *amd-ssbd*

  需要此标志来启用 Spectre v4（CVE-2018-3639）修复。默认不包含在任何 AMD CPU 模型中。对于所有 AMD CPU 模型，都必须显式启用。此标志提供比 virt-ssbd 更高的性能，因此，如果可能，支持此功能的宿主机应始终将其暴露给客户机。尽管如此，仍应同时暴露 virt-ssbd，以最大限度地提高客户机兼容性，因为某些内核只识别 virt-ssbd。
- *amd-no-ssb*

  建议用于指示宿主机不受 Spectre V4（CVE-2018-3639）影响。默认不包含在任何 AMD CPU 模型中。未来的 CPU 硬件代次将不受 CVE-2018-3639 影响，因此应通过暴露 amd-no-ssb 告知客户机不要启用其缓解措施。此标志与 virt-ssbd 和 amd-ssbd 互斥。

#### Windows-related CPU settings <a href="#qm_cpu_windows_tweaks" id="qm_cpu_windows_tweaks"></a>

一些 CPU 默认设置和属性专门针对近期 Intel 硬件上的 Windows 客户机进行了调整：

- `cet-ibt` and `cet-ss` (Control-flow Enforcement Technology: indirect branch tracking and shadow stack) are disabled by default for Windows 11 machine types, as they currently break boot for Windows guests with virtualization-based security enabled. Workloads that explicitly rely on the flags can re-enable them per VM via the `Processor` flag editor.
- The QEMU `level` CPU property is exposed so it can be set per VM (or in a custom CPU model) without resorting to custom `args`. Setting `level=30` is a known workaround for Hyper-V boot failures of Windows guests on recent Intel hosts when the CPU type is `host` or `max`. The property only applies for x86\_64 vCPUs; it is silently ignored on other architectures.

#### NUMA <a href="#_numa" id="_numa"></a>

You can also optionally emulate a **NUMA**
[\[7\]](#note-0cdd31f9-7) architecture in your VMs. The basics of the NUMA architecture mean that instead of having a global memory pool available to all your cores, the memory is spread into local banks close to each socket. This can bring speed improvements as the memory bus is not a bottleneck anymore. If your system has a NUMA architecture [\[8\]](#note-0cdd31f9-8) we recommend to activate the option, as this will allow proper distribution of the VM resources on the host system. This option is also required to hot-plug cores or RAM in a VM.

如果使用 NUMA 选项，建议将插槽数设置为宿主机系统的节点数。

#### vCPU hot-plug <a href="#_vcpu_hot_plug" id="_vcpu_hot_plug"></a>

Modern operating systems introduced the capability to hot-plug and, to a certain extent, hot-unplug CPUs in a running system. Virtualization allows us to avoid a lot of the (physical) problems real hardware can cause in such scenarios. Still, this is a rather new and complicated feature, so its use should be restricted to cases where its absolutely needed. Most of the functionality can be replicated with other, well tested and less complicated, features, see [Resource Limits](#qm_cpu_resource_limits).

在 Proxmox VE 中，可插入的 CPU 最大数量始终为 `cores * sockets`。若要在启动虚拟机时使用少于该总核心数的 CPU，可以使用 **vcpus** 设置，它表示虚拟机启动时应插入多少个 vCPU。

目前，此功能仅在 Linux 上受支持，需要高于 3.10 版本的内核，建议使用高于 4.7 版本的内核。

您可以使用如下 udev 规则，自动将客户机中的新 CPU 设置为在线状态：

```text
SUBSYSTEM=="cpu", ACTION=="add", TEST=="online", ATTR{online}=="0", ATTR{online}="1"
```

Save this under /etc/udev/rules.d/ as a file ending in `.rules`.

注意：CPU 热移除取决于机器类型，并且需要客户机配合。删除命令并不保证 CPU 移除会实际发生；通常，它只是通过目标相关机制（例如 x86/amd64 上的 ACPI）转发给客户机操作系统的请求。

### Memory <a href="#qm_memory" id="qm_memory"></a>

对于每台虚拟机，您可以选择设置固定大小的内存，也可以让 Proxmox VE 根据宿主机的当前 RAM 使用情况动态分配内存。

[![screenshot/gui-create-vm-memory.png](../assets/screenshot-gui-create-vm-memory-png-3dded0eeb67d.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-memory.png)

**固定内存分配**

当将内存和最小内存设置为相同数值时，Proxmox VE 将直接按照您指定的数量为虚拟机分配内存。

即使使用固定内存大小，仍会为虚拟机添加气球设备，因为它能提供有用信息，例如客户机实际使用了多少内存。通常，您应保持启用 **ballooning**，但如果您想禁用它（例如出于调试目的），只需取消选中 **气球设备** 或进行如下设置

```text
balloon: 0
```

在配置中。

<a id="qm_ballooning"></a>



**自动内存分配**

When setting the minimum memory lower than memory, Proxmox VE will make sure that the minimum amount you specified is always available to the VM, and if RAM usage on the host is below a certain target percentage, will dynamically add memory to the guest up to the maximum memory specified. The target percentage defaults to 80% and can be configured in the node options.

当宿主机 RAM 不足时，虚拟机随后会将部分内存释放回宿主机，必要时换出正在运行的进程，并在万不得已时启动 oom killer。宿主机和客户机之间的内存传递通过运行在客户机内部的特殊 `balloon` 内核驱动程序完成，该驱动程序会从宿主机获取或向宿主机释放内存页。[\[9\]](#note-0cdd31f9-9)

当多台虚拟机使用自动分配功能时，可以设置 **Shares** 系数，该系数表示每台虚拟机应占用的宿主机空闲内存相对比例。例如，假设您有四台虚拟机，其中三台运行 HTTP 服务器，最后一台是数据库服务器。宿主机配置的目标 RAM 使用率为 80%。为了在数据库服务器的 RAM 中缓存更多数据库块，您希望在有闲置 RAM 时优先考虑数据库虚拟机。为此，将数据库虚拟机的 Shares 属性设置为 3000，其他虚拟机则保留 Shares 的默认设置 1000。该宿主机具有 32GB RAM，当前已使用 16GB，因此在虚拟机各自配置的最小内存量之外，还有 32 \* 80/100 \- 16 \= 9GB RAM 可分配给虚拟机。数据库虚拟机将额外获得 9 \* 3000 / (3000 \+ 1000 \+ 1000 \+ 1000\) \= 4.5 GB RAM，每台 HTTP 服务器虚拟机则可额外获得 1.5 GB。

2010 年之后发布的所有 Linux 发行版都包含气球内核驱动程序。对于 Windows 操作系统，需要手动添加气球驱动程序，这可能会导致客户机速度变慢，因此我们不建议在关键系统上使用它。

为虚拟机分配 RAM 时，一个很好的经验法则是始终为宿主机保留 1GB 可用 RAM。

### Memory Encryption <a href="#qm_memory_encryption" id="qm_memory_encryption"></a>

#### AMD SEV <a href="#qm_memory_encryption_sev" id="qm_memory_encryption_sev"></a>

SEV（安全加密虚拟化）使用 AES-128 加密和 AMD Secure Processor，为每台虚拟机启用内存加密。

SEV-ES（安全加密虚拟化 \- 加密状态）还会加密所有 CPU 寄存器内容，以防止信息泄露给虚拟机监视器。

SEV-SNP（安全加密虚拟化 \- 安全嵌套分页）还试图防止基于软件的完整性攻击。有关更多信息，请参阅 [AMD SEV SNP 白皮书](https://www.amd.com/content/dam/amd/en/documents/epyc-business-docs/white-papers/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf)。

**宿主机要求：**

- AMD EPYC CPU
- SEV-ES 仅在 AMD EPYC 7002 系列及更新的 EPYC CPU 上受支持
- SEV-SNP 仅在 AMD EPYC 7003 系列及更新的 EPYC CPU 上受支持
- SEV-SNP 要求宿主机内核版本为 6.11 或更高。
- 在宿主机的 BIOS 设置中配置 AMD 内存加密
- 如果默认未启用，请将 "kvm\_amd.sev\=1" 添加到内核参数
- add "mem\_encrypt\=on" to kernel parameters if you want to encrypt memory on the host (SME) see [https://www.kernel.org/doc/Documentation/x86/amd-memory-encryption.txt](https://www.kernel.org/doc/Documentation/x86/amd-memory-encryption.txt)
- maybe increase SWIOTLB see [https://github.com/AMDESE/AMDSEV#faq-4](https://github.com/AMDESE/AMDSEV#faq-4)

要检查宿主机上是否启用了 SEV，请在 dmesg 中搜索 `sev`，并打印 kvm\_amd 的 SEV 内核参数：

```text
# dmesg | grep -i sev
[...] ccp 0000:45:00.1: sev enabled
[...] ccp 0000:45:00.1: SEV API: <buildversion>
[...] SEV supported: <number> ASIDs
[...] SEV-ES supported: <number> ASIDs
# cat /sys/module/kvm_amd/parameters/sev
Y
```

**客户机要求：**

- edk2-OVMF
- 建议使用 Q35
- 客户机操作系统必须支持 SEV。

**限制：**

- 由于内存已加密，宿主机上显示的内存使用情况始终不准确。
- 涉及保存或恢复内存的操作（如快照和在线迁移）尚无法正常工作，或者[容易受到攻击](https://github.com/PSPReverse/amd-sev-migration-attack)。
- 不支持 PCI 直通。
- SEV-ES 和 SEV-SNP 仍处于高度实验性阶段。
- SEV-SNP 不支持 EFI 磁盘。
- 使用 SEV-SNP 时，虚拟机内的 `reboot` 命令只会让虚拟机关机。

**配置示例（SEV）：**

```text
# qm set <vmid> -amd-sev type=std,no-debug=1,no-key-sharing=1,kernel-hashes=1
```

**type** 定义加密技术（不需要 "type\="）。可用选项为 std、es 和 snp。

QEMU 的 **policy** 参数根据 **no-debug** 和 **no-key-sharing** 参数计算得出。这些参数分别对应 policy-bit 0 和 1。如果 **type** 为 **es**，则将 policy-bit 2 设置为 1，以启用 SEV-ES。policy-bit 3（nosend）始终设置为 1，以防止迁移攻击。有关如何计算 policy 的更多信息，请参阅：[AMD SEV API 规范第 3 章](https://www.amd.com/system/files/TechDocs/55766_SEV-KM_API_Specification.pdf)

为了向后兼容较旧的 OVMF 镜像以及不度量 kernel/initrd 的客户机，**kernel-hashes** 选项默认关闭。请参阅 [https://lists.gnu.org/archive/html/qemu-devel/2021-11/msg02598.html](https://lists.gnu.org/archive/html/qemu-devel/2021-11/msg02598.html)

**检查 SEV 是否在虚拟机中正常工作**

方法 1 \- dmesg：

输出应如下所示。

```text
# dmesg | grep -i sev
AMD Memory Encryption Features active: SEV
```

方法 2 \- MSR 0xc0010131（MSR\_AMD64\_SEV）：

输出应为 1。

```text
# apt install msr-tools
# modprobe msr
# rdmsr -a 0xc0010131
1
```

**配置示例（SEV-SNP）：**

```text
# qm set <vmid> -amd-sev type=snp,allow-smt=1,no-debug=1,kernel-hashes=1
```

默认会设置 `allow-smt` policy-bit。如果通过将 `allow-smt` 设置为 `0` 来禁用它，则必须在宿主机上禁用 SMT，虚拟机才能运行。

**检查 SEV-SNP 是否在虚拟机中正常工作**

```text
# dmesg | grep -i snp
Memory Encryption Features active: AMD SEV SEV-ES SEV-SNP
SEV: Using SNP CPUID table, 29 entries present.
SEV: SNP guest platform device initialized.
```

链接：

- [https://developer.amd.com/sev/](https://developer.amd.com/sev/)
- [https://github.com/AMDESE/AMDSEV](https://github.com/AMDESE/AMDSEV)
- [https://www.qemu.org/docs/master/system/i386/amd-memory-encryption.html](https://www.qemu.org/docs/master/system/i386/amd-memory-encryption.html)
- [https://www.amd.com/system/files/TechDocs/55766\_SEV-KM\_API\_Specification.pdf](https://www.amd.com/system/files/TechDocs/55766_SEV-KM_API_Specification.pdf)
- [https://documentation.suse.com/sles/15-SP1/html/SLES-amd-sev/index.html](https://documentation.suse.com/sles/15-SP1/html/SLES-amd-sev/index.html)
- [SEV Secure Nested Paging Firmware ABI Specification](https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/specifications/56860.pdf)

### Network Device <a href="#qm_network_device" id="qm_network_device"></a>

[![screenshot/gui-create-vm-network.png](../assets/screenshot-gui-create-vm-network-png-52dc7176c8f4.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-vm-network.png)

每台虚拟机都可以有多个 *网络接口控制器*（NIC），分为四种不同类型：

- **Intel E1000** is the default, and emulates an Intel Gigabit network card.
- 如果追求最高性能，应使用 **VirtIO** 半虚拟化 NIC。与所有 VirtIO 设备一样，客户机操作系统应安装适当的驱动程序。
- **Realtek 8139** 模拟较旧的 100 MB/s 网卡，只应在模拟较旧的操作系统（2002 年之前发布）时使用
- **vmxnet3** 是另一种半虚拟化设备，只应在从其他虚拟机监视器导入虚拟机时使用。

Proxmox VE 会为每个 NIC 生成一个随机 **MAC 地址**，从而使虚拟机能够在以太网网络中被寻址。

您添加到虚拟机的 NIC 可以采用以下两种不同模式之一：

- 在默认的 **桥接模式**下，每个虚拟 NIC 在宿主机上都有一个 *tap 设备* 作为后端（一种模拟以太网 NIC 的软件环回设备）。此 tap 设备会添加到一个网桥，在 Proxmox VE 中默认为 vmbr0。在此模式下，虚拟机可以直接访问宿主机所在的以太网 LAN。
- 在备选的 **NAT 模式**下，每个虚拟 NIC 只与 QEMU 用户网络协议栈通信，其中内置的路由器和 DHCP 服务器可以提供网络访问。此内置 DHCP 将在私有 10.0.2.0/24 范围内提供地址。NAT 模式比桥接模式慢得多，只应用于测试。此模式只能通过 CLI 或 API 使用，不能通过 Web UI 使用。

您还可以在创建虚拟机时选择 **无网络设备**，以跳过添加网络设备。

您可以手动覆盖每个虚拟机网络设备的 **MTU** 设置。将该字段留空或设置为 `mtu=1` 将从底层网桥继承 MTU。此选项仅适用于 **VirtIO** 网络设备。

**多队列**

如果您使用 VirtIO 驱动程序，可以选择启用 **Multiqueue** 选项。此选项允许客户机操作系统使用多个虚拟 CPU 处理网络数据包，从而提高传输的数据包总数。

在 Proxmox VE 中使用 VirtIO 驱动程序时，每个 NIC 网络队列都会传递给宿主机内核，队列将在该内核中由 vhost 驱动程序创建的内核线程处理。启用此选项后，可以为每个 NIC 将*多个*网络队列传递给宿主机内核。

使用 Multiqueue 时，建议将其设置为等于客户机 vCPU 数量的值。请记住，vCPU 数量是为虚拟机配置的插槽数乘以核心数。您还需要使用以下 ethtool 命令，设置虚拟机中每个 VirtIO NIC 的多用途通道数量：

`ethtool -L ens1 combined X`

其中 X 是虚拟机的 vCPU 数量。

要为 Windows 客户机配置 Multiqueue，请安装 [Redhat VirtIO Ethernet Adapter 驱动程序](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers)，然后按如下方式调整 NIC 的配置。打开设备管理器，右键单击“网络适配器”下的 NIC，然后选择“属性”。接着打开“高级”选项卡，并从左侧列表中选择“Receive Side Scaling”。确保其设置为“Enabled”。接下来，在列表中找到“Maximum number of RSS Queues”，并将其设置为 VM 的 vCPU 数量。确认设置正确后，单击“确定”以确认这些设置。

您应该注意，将 Multiqueue 参数设置为大于 1 的值时，随着流量增加，宿主机和客户机系统的 CPU 负载都会增加。我们建议仅在 VM 必须处理大量传入连接时才设置此选项，例如 VM 作为路由器、反向代理或执行长轮询的繁忙 HTTP 服务器运行时。

### Display <a href="#qm_display" id="qm_display"></a>

QEMU 可以虚拟化几种类型的 VGA 硬件。例如：

- **std**, the default, emulates a card with Bochs VBE extensions.
- **cirrus**, this was once the default, it emulates a very old hardware module with all its problems. This display type should only be used if really necessary [\[10\]](#note-0cdd31f9-10), for example, if using Windows XP or earlier
- **vmware**, is a VMWare SVGA-II compatible adapter.
- **qxl**, is the QXL paravirtualized graphics card. Selecting this also enables [SPICE](https://www.spice-space.org/) (a remote viewer protocol) for the VM.
- **virtio-gl**, often named VirGL is a virtual 3D GPU for use inside VMs that can offload workloads to the host GPU without requiring special (expensive) models and drivers and neither binding the host GPU completely, allowing reuse between multiple guests and or the host.

  {% hint style="info" %}
  VirGL 支持需要一些额外的库，这些库由于体积相对较大，而且并非适用于所有 GPU 型号/供应商的开源版本，因此默认不会安装。对于大多数设置，您只需执行：`apt install libgl1 libegl1`
  {% endhint %}

您可以通过设置 *memory* 选项来编辑分配给虚拟 GPU 的内存量。这可以在 VM 内启用更高的分辨率，尤其是在使用 SPICE/QXL 时。

由于内存由显示设备保留，为 SPICE 选择多显示器模式（例如 `qxl2` 表示双显示器）会产生一些影响：

- Windows 需要每台显示器对应一个设备，因此，如果您的 *ostype* 是某个 Windows 版本，Proxmox VE 会为 VM 的每台显示器额外提供一个设备。每个设备都会获得指定数量的内存。
- Linux VM 始终可以启用更多虚拟显示器，但选择多显示器模式会将分配给设备的内存乘以显示器数量。

选择 `serialX` 作为显示 *type* 会禁用 VGA 输出，并将 Web 控制台重定向到所选的串行端口。在这种情况下，配置的显示 *memory* 设置将被忽略。

**VNC 剪贴板**

您可以通过将 `clipboard` 设置为 `vnc` 来启用 VNC 剪贴板。

```text
# qm set <vmid> -vga <displaytype>,clipboard=vnc
```

要使用剪贴板功能，必须先安装 SPICE 客户机工具。在基于 Debian 的发行版上，可以通过安装 `spice-vdagent` 来实现。对于其他操作系统，请在官方软件仓库中搜索，或参阅：[https://www.spice-space.org/download.html](https://www.spice-space.org/download.html)

Once you have installed the spice guest tools, you can use the VNC clipboard function (e.g. in the noVNC console panel). However, if you’re using SPICE, virtio or virgl, you’ll need to choose which clipboard to use. This is because the default **SPICE** clipboard will be replaced by the **VNC** clipboard, if `clipboard` is set to `vnc`.

{% hint style="info" %}
为了启用 VNC 剪贴板，QEMU 会被配置为使用 qemu-vdagent 设备。QEMU 10.1 版本增加了对该设备在线迁移的支持。运行在低于 10.1 的 QEMU 或机器版本上且已启用 VNC 剪贴板的 VM 无法在线迁移。
{% endhint %}

### USB Passthrough <a href="#qm_usb_passthrough" id="qm_usb_passthrough"></a>

USB 直通设备有两种不同的类型：

- 宿主机 USB 直通
- SPICE USB 直通

宿主机 USB 直通通过将宿主机的一个 USB 设备提供给 VM 来工作。这可以通过供应商 ID 和产品 ID 完成，也可以通过宿主机总线和端口完成。

供应商/产品 ID 的格式如下：**0123:abcd**，其中 **0123** 是供应商 ID，**abcd** 是产品 ID，这意味着同一型号 USB 设备的两个实例具有相同的 ID。

总线/端口的格式如下：**1-2.3.4**，其中 **1** 是总线，**2.3.4** 是端口路径。这表示宿主机的物理端口（取决于 USB 控制器的内部顺序）。

如果 VM 启动时其配置中存在某个设备，但该设备并不存在于宿主机上，VM 仍可正常启动。一旦该设备/端口在宿主机上可用，就会被直通给 VM。

{% hint style="warning" %}
使用这种 USB 直通意味着您无法将 VM 在线迁移到另一台宿主机，因为该硬件仅在 VM 当前所在的宿主机上可用。
{% endhint %}

第二种直通类型是 SPICE USB 直通。如果为 VM 添加一个或多个 SPICE USB 端口，就可以将 SPICE 客户端上的本地 USB 设备动态直通到 VM。这对于临时重定向输入设备或硬件加密狗非常有用。

It is also possible to map devices on a cluster level, so that they can be properly used with HA and hardware changes are detected and non root users can configure them. See [Resource Mapping](#resource_mapping) for details on that.

### BIOS and UEFI <a href="#qm_bios_and_uefi" id="qm_bios_and_uefi"></a>

为了正确模拟计算机，QEMU 需要使用固件。在普通 PC 上通常称为 BIOS 或 (U)EFI 的固件，是 VM 启动时最早执行的步骤之一。它负责执行基本硬件初始化，并为操作系统提供固件和硬件接口。默认情况下，QEMU 使用 **SeaBIOS**，这是一种开源的 x86 BIOS 实现。对于大多数标准设置，SeaBIOS 是一个不错的选择。

{% hint style="info" %}
SeaBIOS 以及 `bios=seabios` 仅适用于 x86 客户机。在 arm64 宿主机上，虚拟机始终通过 UEFI 启动，使用 OVMF 的 ARM 构建版本（AAVMF），因此 `bios=ovmf` 是那里唯一受支持的设置。
{% endhint %}

某些操作系统（例如 Windows 11）可能要求使用兼容 UEFI 的实现。在这种情况下，必须改用 **OVMF**，它是一种开源的 UEFI 实现。[\[11\]](#note-0cdd31f9-11)

在其他一些场景中，SeaBIOS 可能不是理想的启动固件，例如当您想要进行 VGA 直通时。[\[12\]](#note-0cdd31f9-12)

如果您想使用 OVMF，需要考虑以下几点：

为了保存**启动顺序**之类的设置，需要有一个 EFI 磁盘。该磁盘将包含在备份和快照中，并且只能有一个。

您可以使用以下命令创建这样的磁盘：

```text
# qm set <vmid> -efidisk0 <storage>:1,format=<format>,efitype=4m,pre-enrolled-keys=1
```

其中 **\<storage\>** 是您希望存放该磁盘的存储，**\<format\>** 是该存储支持的格式。或者，您也可以通过 Web 界面，在 VM 的硬件部分使用 *Add* → *EFI Disk* 创建这样的磁盘。

**efitype** 选项指定应使用哪个版本的 OVMF 固件。对于新 VM，应始终使用 *4m*，因为它支持安全启动，并分配了更多空间以支持未来的开发（这是 GUI 中的默认值）。

**pre-enroll-keys** specifies if the efidisk should come pre-loaded with distribution-specific and Microsoft Standard Secure Boot keys. It also enables Secure Boot by default (though it can still be disabled in the OVMF menu within the VM). See also [Secure Boot Certificate Expiration](#qm_secure_boot_ca_expiration).

{% hint style="info" %}
如果您想在现有 VM（仍使用 *2m* efidisk）中开始使用安全启动，则需要重新创建 efidisk。为此，请删除旧磁盘（`qm set <vmid> -delete efidisk0`），然后按上述说明添加新磁盘。这将重置您在 OVMF 菜单中所做的任何自定义配置！
{% endhint %}

将 OVMF 与虚拟显示器一起使用时（不进行 VGA 直通），您需要在 OVMF 菜单中设置客户端分辨率（启动期间按 ESC 键即可进入该菜单），或者必须选择 SPICE 作为显示类型。

When using OVMF with PXE boot, you have to add an [RNG device](#qm_virtio_rng) to the VM. For security reasons, the OVMF firmware disables PXE boot for guests without a random number generator.

#### Secure Boot Certificate Expiration <a href="#qm_secure_boot_ca_expiration" id="qm_secure_boot_ca_expiration"></a>

The original set of Microsoft certificates from 2011, which Windows and common Linux distributions use for secure boot, expires in June 2026\. Microsoft created replacement certificates in 2023 [\[13\]](#note-0cdd31f9-13).

固件只允许使用 EFI 磁盘上存在的证书所签名的引导加载程序。特别是，仅包含 2011 年证书的 EFI 磁盘将拒绝使用 2023 年证书签名的引导加载程序。VM 配置中 EFI 磁盘的 `ms-cert=2023k` 标记表示新证书已注册。

如果 `pve-edk2-firmware` 软件包版本至少为 `4.2025.05-1`，则新创建的 EFI 磁盘会同时包含 2011 年和 2023 年的证书，并带有 `ms-cert=2023k` 标记。对于此前创建的 EFI 磁盘，您需要注册这些证书：

对于使用 BitLocker 的 Windows，请在 PowerShell 中运行以下命令：

```text
manage-bde -protectors -disable <drive>
```

例如，`<drive>` 可以是 `C:`。在继续操作之前，每个使用 BitLocker 的驱动器都必须执行此操作。否则，下次启动时系统将提示您输入 BitLocker 恢复密钥！

在 UI 的 *Hardware* 视图中选择 EFI 磁盘，然后使用 *Disk Action \> Enroll Updated Certificates*。或者，通过 `/nodes/{node}/qemu/{vmid}/config` API 端点注册证书。注册将在 VM 下次启动时生效。该

```text
qm enroll-efi-keys <vmid>
```

CLI 命令可以实现相同的效果，但要求 VM 处于关机状态。

有关在 Windows 中更新安全启动以及使用新的 2023 年证书为引导加载程序签名的后续步骤，请参阅 Microsoft 关于[enterprise deployment guidance for CVE-2023-24932](https://support.microsoft.com/en-us/topic/enterprise-deployment-guidance-for-cve-2023-24932-88b8f034-20b7-4a45-80cb-c6049b0f9967)的支持文章，以及需要首先安装的[related security update](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-24932)。

{% hint style="info" %}
标记 `ms-cert=2023` 和 `ms-cert=2023w` 可能表示部分注册。VM 启动任务日志会对此发出警告。您也应对这类 EFI 磁盘执行注册过程。
{% endhint %}

### Trusted Platform Module (TPM) <a href="#qm_tpm" id="qm_tpm"></a>

**可信平台模块**是一种安全存储机密数据（例如加密密钥）的设备，并提供用于验证系统启动的防篡改功能。

某些操作系统（例如 Windows 11）要求将此类设备连接到机器（无论是物理机还是虚拟机）。

通过指定 **tpmstate** 卷来添加 TPM。其工作方式与 efidisk 类似，即创建后无法更改（只能删除）。您可以通过以下命令添加一个：

```text
# qm set <vmid> -tpmstate0 <storage>:1,version=<version>
```

其中 **\<storage\>** 是您希望存放状态的存储，**\<version\>** 可以是 *v1.2* 或 *v2.0*。您也可以通过 Web 界面，在 VM 的硬件部分选择 *Add* → *TPM State* 来添加一个。

*v2.0* TPM 规范较新且支持更好，因此除非您的特定实现需要 *v1.2* TPM，否则应优先使用它。

{% hint style="info" %}
与物理 TPM 相比，模拟 TPM **并不**能提供任何真正的安全优势。TPM 的意义在于，除非通过 TPM 规范中规定的命令，否则其中的数据无法被轻易修改。由于模拟设备的数据存储在常规卷上，因此任何有权访问该卷的人都有可能编辑这些数据。
{% endhint %}

### Inter-VM shared memory <a href="#qm_ivshmem" id="qm_ivshmem"></a>

您可以添加虚拟机间共享内存设备（`ivshmem`），它允许在宿主机与客户机之间共享内存，也允许在多个客户机之间共享内存。

要添加此类设备，可以使用 `qm`：

```text
# qm set <vmid> -ivshmem size=32,name=foo
```

其中大小以 MiB 为单位。文件将位于 `/dev/shm/pve-shm-$name` 下（默认名称为 vmid）。

{% hint style="info" %}
目前，一旦任何使用该设备的 VM 关机或停止，该设备就会被删除。现有连接仍会保持，但无法再与同一设备建立新连接。
{% endhint %}

此类设备的一个用例是 Looking Glass [\[14\]](#note-0cdd31f9-14) 项目，它可在宿主机与客户机之间实现高性能、低延迟的显示镜像。

### Audio Device <a href="#qm_audio_device" id="qm_audio_device"></a>

要添加音频设备，请运行以下命令：

```text
qm set <vmid> -audio0 device=<device>
```

支持的音频设备有：

- `ich9-intel-hda`: Intel HD Audio Controller, emulates ICH9
- `intel-hda`: Intel HD Audio Controller, emulates ICH6
- `AC97`: Audio Codec '97, useful for older operating systems like Windows XP

有两种可用的后端：

- *spice*
- *none*

The *spice* backend can be used in combination with [SPICE](#qm_display) while the *none* backend can be useful if an audio device is needed in the VM for some software to work. To use the physical audio device of the host use device passthrough (see [PCI Passthrough](#qm_pci_passthrough) and [USB Passthrough](#qm_usb_passthrough)). Remote protocols like Microsoft’s RDP have options to play sound.

### VirtIO RNG <a href="#qm_virtio_rng" id="qm_virtio_rng"></a>

RNG（随机数生成器）是一种为系统提供熵（*随机性*）的设备。虚拟硬件 RNG 可用于将宿主机系统的这种熵提供给客户机 VM。这有助于避免客户机出现熵不足问题（即没有足够可用的熵，系统可能变慢或出现问题的情况），尤其是在客户机启动过程中。

要添加基于 VirtIO 的模拟 RNG，请运行以下命令：

```text
qm set <vmid> -rng0 source=<source>[,max_bytes=X,period=Y]
```

`source` 指定在宿主机上从何处读取熵，其值必须是以下之一：

- `/dev/urandom`: Non-blocking kernel entropy pool (preferred)
- `/dev/random`: Blocking kernel pool (not recommended, can lead to entropy starvation on the host system)
- `/dev/hwrng`: To pass through a hardware RNG attached to the host (if multiple are available, the one selected in `/sys/devices/virtual/misc/hw_random/rng_current` will be used)

A limit can be specified via the `max_bytes` and `period` parameters, they are read as `max_bytes` per `period` in milliseconds. However, it does not represent a linear relationship: 1024B/1000ms would mean that up to 1 KiB of data becomes available on a 1 second timer, not that 1 KiB is streamed to the guest over the course of one second. Reducing the `period` can thus be used to inject entropy into the guest at a faster rate.

默认情况下，限制设置为每 1000 ms 1024 字节（1 KiB/s）。建议始终使用限制器，以避免客户机占用过多宿主机资源。如果需要，可将 *0* 用作 `max_bytes` 的值，以禁用所有限制。

### Virtiofs <a href="#qm_virtiofs" id="qm_virtiofs"></a>

Virtiofs 是一种为虚拟环境设计的共享文件系统。它允许通过在 VM 内挂载宿主机上可用的目录树来共享该目录树。它不使用网络协议栈，并致力于提供与源文件系统类似的性能和语义。

要使用 virtiofs，[virtiofsd](https://gitlab.com/virtio-fs/virtiofsd) 守护进程需要在后台运行。在 Proxmox VE 中，启动使用 virtiofs 挂载的 VM 时会自动完成此操作。

内核版本 \>\=5.4 的 Linux VM 默认支持 virtiofs（[virtiofs 内核模块](https://www.kernelconfig.io/CONFIG_VIRTIO_FS)），但某些功能需要更新的内核。

要使用 virtiofs，请确保 Proxmox VE 宿主机上已安装 virtiofsd：

```text
apt install virtiofsd
```

有一篇[指南](https://github.com/virtio-win/kvm-guest-drivers-windows/wiki/Virtiofs:-Shared-file-system)介绍如何在 Windows VM 中使用 virtiofs。

#### Known Limitations <a href="#_known_limitations" id="_known_limitations"></a>

- 如果 virtiofsd 崩溃，其挂载点将在 VM 中一直处于无响应状态，直到 VM 完全停止。
- virtiofsd 无响应可能会导致 VM 中的挂载卡住，类似于无法访问 NFS 的情况。
- 内存热插拔在与 virtiofs 一起使用时不起作用（也会导致访问卡住）。
- 在线迁移、快照和休眠等内存相关功能在 virtiofs 设备上不可用。
- Windows 无法理解 virtiofs 上下文中的 ACL。因此，不要向 Windows VM 暴露 ACL，否则 virtiofs 设备将在 VM 内不可见。

#### Add Mapping for Shared Directories <a href="#_add_mapping_for_shared_directories" id="_add_mapping_for_shared_directories"></a>

To add a mapping for a shared directory, you can use the API directly with `pvesh` as described in the [Resource Mapping](#resource_mapping) section:

```text
pvesh create /cluster/mapping/dir --id dir1 \
    --map node=node1,path=/path/to/share1 \
    --map node=node2,path=/path/to/share2 \
```

#### Add virtiofs to a VM <a href="#_add_virtiofs_to_a_vm" id="_add_virtiofs_to_a_vm"></a>

要使用 virtiofs 共享目录，请将参数 `virtiofs<N>`（N 可以是 0 到 9 之间的任意值）添加到 VM 配置中，并使用已在资源映射中配置的目录 ID（dirid）。此外，可以根据需求将 `cache` 选项设置为 `always`、`never`、`metadata` 或 `auto`（默认值：`auto`）。有关不同缓存模式行为的信息，请参阅[此处的“缓存模式”一节](https://lwn.net/Articles/774495/)。

`virtiofsd` 支持 ACL 和 xattr 直通（可通过 `expose-acl` 和 `expose-xattr` 选项启用），如果底层宿主机文件系统支持 ACL 和 xattr，则允许客户机访问它们，但它们还必须与客户机文件系统兼容（例如，大多数 Linux 文件系统支持 ACL，而 Windows 文件系统不支持）。

`expose-acl` 选项会自动隐含 `expose-xattr`，也就是说，将 `expose-xattr` 设置为 `0` 时，如果 `expose-acl` 已设置为 `1`，结果不会有所不同。

如果希望 virtiofs 遵循 `O_DIRECT` 标志，可以将 `direct-io` 参数设置为 `1`（默认值：`0`）。这会降低性能，但在应用程序自行进行缓存时很有用。

```text
qm set <vmid> -virtiofs0 dirid=<dirid>,cache=always,direct-io=1
qm set <vmid> -virtiofs1 <dirid>,cache=never,expose-xattr=1
qm set <vmid> -virtiofs2 <dirid>,expose-acl=1
```

要在使用 Linux 内核 virtiofs 驱动程序的客户机 VM 中临时挂载 virtiofs，请在客户机内运行以下命令：

```text
mount -t virtiofs <dirid> <mount point>
```

要持久挂载 virtiofs，可以创建一个 fstab 条目：

```text
<dirid> <mount point> virtiofs rw,relatime 0 0
```

与当前节点上的路径关联的 dirid 也会用作挂载标签（在客户机上挂载设备时使用的名称）。

有关可用 virtiofsd 参数的更多信息，请参阅[GitLab virtiofsd 项目页面](https://gitlab.com/virtio-fs/virtiofsd)。

### Device Boot Order <a href="#qm_bootorder" id="qm_bootorder"></a>

QEMU 可以告知客户机应从哪些设备启动以及启动顺序。可以通过配置中的 `boot` 属性指定，例如：

```text
boot: order=scsi0;net0;hostpci0
```

[![screenshot/gui-qemu-edit-bootorder.png](../assets/screenshot-gui-qemu-edit-bootorder-png-e24815e584de.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-edit-bootorder.png)

这样，客户机会首先尝试从磁盘 `scsi0` 启动；如果失败，则会继续尝试从 `net0` 进行网络启动；如果仍然失败，最后会尝试从直通 PCIe 设备启动（对于 NVMe，该设备会被视为磁盘，否则会尝试从 option ROM 启动）。

在 GUI 中，您可以使用拖放编辑器指定启动顺序，并通过复选框启用或禁用某些设备的启动。

{% hint style="info" %}
如果您的客户机使用多个磁盘来启动操作系统或加载引导加载程序，则必须将所有这些磁盘标记为*可启动*（即必须启用相应复选框，或使其出现在配置中的列表里），客户机才能启动。这是因为较新的 SeaBIOS 和 OVMF 版本只会初始化标记为*可启动*的磁盘。
{% endhint %}

无论如何，即使设备未出现在列表中或未选中其复选框，一旦客户机的操作系统启动并初始化这些设备，它们仍可供客户机使用。*可启动*标志仅影响客户机 BIOS 和引导加载程序。

### Automatic Start and Shutdown of Virtual Machines <a href="#qm_startup_and_shutdown" id="qm_startup_and_shutdown"></a>

创建 VM 后，您可能希望它们在宿主机系统启动时自动启动。为此，您需要在 Web 界面中选择 VM 的*开机启动*选项，该选项位于*选项*选项卡中，或者使用以下命令进行设置：

```text
# qm set <vmid> -onboot 1
```

[![screenshot/gui-qemu-edit-start-order.png](../assets/screenshot-gui-qemu-edit-start-order-png-9683f539b3b2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-edit-start-order.png)

**启动和关闭顺序**

在某些情况下，您可能希望能够微调 VM 的启动顺序，例如，当您的某个 VM 为其他客户机系统提供防火墙或 DHCP 服务时。为此，可以使用以下参数：

- **Start/Shutdown order**: Defines the start order priority. For example, set it to 1 if you want the VM to be the first to be started. (We use the reverse startup order for shutdown, so a machine with a start order of 1 would be the last to be shut down). If multiple VMs have the same order defined on a host, they will additionally be ordered by *VMID* in ascending order.
- **Startup delay**: Defines the interval between this VM start and subsequent VMs starts. For example, set it to 240 if you want to wait 240 seconds before starting other VMs.
- **Shutdown timeout**: Defines the duration in seconds Proxmox VE should wait for the VM to be offline after issuing a shutdown command. By default this value is set to 180, which means that Proxmox VE will issue a shutdown request and wait 180 seconds for the machine to be offline. If the machine is still online after the timeout it will be stopped forcefully.

{% hint style="info" %}
目前，由 HA 堆栈管理的 VM 不遵循*开机启动*和*启动顺序*选项。这些 VM 将被启动和关闭算法跳过，因为 HA 管理器本身会确保 VM 得到启动和停止。
{% endhint %}

请注意，未设置启动/关闭顺序参数的机器始终会在设置了该参数的机器之后启动。此外，该参数只能在同一宿主机上运行的虚拟机之间强制执行，无法在整个集群范围内生效。

If you require a delay between the host boot and the booting of the first VM, see the section on Proxmox VE Node Management.

### QEMU Guest Agent <a href="#qm_qemu_agent" id="qm_qemu_agent"></a>

QEMU Guest Agent 是一项在 VM 内运行的服务，它在宿主机与客户机之间提供通信通道。它用于交换信息，并允许宿主机向客户机发出命令。

例如，VM 摘要面板中的 IP 地址就是通过客户机代理获取的。

或者，在开始备份时，会通过客户机代理指示客户机通过 `guest-fsfreeze-freeze` 和 `guest-fsfreeze-thaw` 命令同步未完成的写入。

要使客户机代理正常工作，必须执行以下步骤：

- 在客户机中安装代理并确保其正在运行
- 在 Proxmox VE 中启用通过代理进行的通信

#### Install Guest Agent <a href="#_install_guest_agent" id="_install_guest_agent"></a>

大多数 Linux 发行版都提供客户机代理。该软件包通常名为 `qemu-guest-agent`。

对于 Windows，请参阅我们的[Windows VirtIO 驱动程序](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers)文章，了解有关如何获取和安装驱动程序的更多信息。

#### Enable Guest Agent Communication <a href="#qm_qga_enable" id="qm_qga_enable"></a>

可以在 VM 的**选项**面板中启用 Proxmox VE 与客户机代理之间的通信。需要重新启动 VM 才能使更改生效。

#### Automatic TRIM Using QGA <a href="#qm_qga_auto_trim" id="qm_qga_auto_trim"></a>

可以启用*运行 guest-trim*选项。启用后，Proxmox VE 会在以下可能将零写入存储的操作完成后，向客户机发出 trim 命令：

- 将磁盘移动到另一个存储
- live migrating a VM to another node with local storage

On a thin provisioned storage, this can help to free up unused space.

{% hint style="info" %}
There is a caveat with ext4 on Linux, because it uses an in-memory optimization to avoid issuing duplicate TRIM requests. Since the guest doesn’t know about the change in the underlying storage, only the first guest-trim will run as expected. Subsequent ones, until the next reboot, will only consider parts of the filesystem that changed since then.
{% endhint %}

#### Filesystem Freeze \& Thaw <a href="#qm_qga_fsfreeze" id="qm_qga_fsfreeze"></a>

By default, if the QEMU Guest Agent is enabled in the guest’s config and if the agent is available inside of the guest, then the virtual machine’s filesystems are synced via the `guest-fsfreeze-freeze` QEMU Guest Agent command when certain operations are performed. This is done to provide data consistency.

See the [QEMU Guest Agent Protocol Reference](https://www.qemu.org/docs/master/interop/qemu-ga-ref.html) for more details.

A freeze will be issued for any of the following operations on a VM:

- Performing a backup in snapshot mode
- Creating a clone of a VM while it is running
- Replicating a VM while it is running
- Taking a snapshot without RAM of a running VM
- Importing a disk image from a running guest will issue a freeze for that running guest

On Windows guests, some applications might handle consistent backups themselves by hooking into the Windows VSS (Volume Shadow Copy Service) layer, a freeze then might interfere with that. For example, it has been observed that calling `guest-fsfreeze-freeze` with some SQL Servers triggers VSS to call the SQL Writer VSS module in a mode that breaks the SQL Server backup chain for differential backups.

There are two options on how to handle such a situation.

1. Configure the QEMU Guest Agent to use a different VSS variant that does not interfere with other VSS users. The [Proxmox VE wiki](https://pve.proxmox.com/wiki/VM_Backup_Consistency) has more details.
2. Alternatively, you can configure Proxmox VE to not issue a freeze-and-thaw cycle by disabling the `freeze-fs` guest agent option. This can also be done in the GUI: open the *Options* panel of the virtual machine, then the *QEMU Guest Agent* dialog, and disable the *Freeze/thaw guest filesystems during certain operations for consistency* option.

   {% hint style="warning" %}
   Disabling this option can potentially lead to backups with inconsistent filesystems. Therefore, adapting the QEMU Guest Agent configuration in the guest is the preferred option.
   {% endhint %}

#### Troubleshooting <a href="#_troubleshooting" id="_troubleshooting"></a>

**VM does not shut down**

Make sure the guest agent is installed and running.

Once the guest agent is enabled, Proxmox VE will send power commands like *shutdown* via the guest agent. If the guest agent is not running, commands cannot get executed properly and the shutdown command will run into a timeout.

### SPICE Enhancements <a href="#qm_spice_enhancements" id="qm_spice_enhancements"></a>

SPICE Enhancements are optional features that can improve the remote viewer experience.

To enable them via the GUI go to the **Options** panel of the virtual machine. Run the following command to enable them via the CLI:

```text
qm set <vmid> -spice_enhancements foldersharing=1,videostreaming=all
```

{% hint style="info" %}
To use these features the [**Display**](#qm_display) of the virtual machine must be set to SPICE (qxl).
{% endhint %}

#### Folder Sharing <a href="#_folder_sharing" id="_folder_sharing"></a>

Share a local folder with the guest. The `spice-webdavd` daemon needs to be installed in the guest. It makes the shared folder available through a local WebDAV server located at [http://localhost:9843](http://localhost:9843).

For Windows guests the installer for the *Spice WebDAV daemon* can be downloaded from the [official SPICE website](https://www.spice-space.org/download.html#windows-binaries).

Most Linux distributions have a package called `spice-webdavd` that can be installed.

To share a folder in Virt-Viewer (Remote Viewer) go to *File → Preferences*. Select the folder to share and then enable the checkbox.

{% hint style="info" %}
Folder sharing currently only works in the Linux version of Virt-Viewer.
{% endhint %}

{% hint style="danger" %}
Experimental! Currently this feature does not work reliably.
{% endhint %}

#### Video Streaming <a href="#_video_streaming" id="_video_streaming"></a>

Fast refreshing areas are encoded into a video stream. Two options exist:

- **all**: Any fast refreshing area will be encoded into a video stream.
- **filter**: Additional filters are used to decide if video streaming should be used (currently only small window surfaces are skipped).

A general recommendation if video streaming should be enabled and which option to choose from cannot be given. Your mileage may vary depending on the specific circumstances.

#### Troubleshooting <a href="#_troubleshooting_2" id="_troubleshooting_2"></a>

**Shared folder does not show up**

Make sure the WebDAV service is enabled and running in the guest. On Windows it is called *Spice webdav proxy*. In Linux the name is *spice-webdavd* but can be different depending on the distribution.

If the service is running, check the WebDAV server by opening [http://localhost:9843](http://localhost:9843) in a browser in the guest.

It can help to restart the SPICE session.

## Migration <a href="#qm_migration" id="qm_migration"></a>

[![screenshot/gui-qemu-migrate.png](../assets/screenshot-gui-qemu-migrate-png-75844014c4d2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-migrate.png)

If you have a cluster, you can migrate your VM to another host with

```text
# qm migrate <vmid> <target>
```

There are generally two mechanisms for this

- Online Migration (aka Live Migration)
- Offline Migration

### Online Migration <a href="#_online_migration" id="_online_migration"></a>

If your VM is running and no locally bound resources are configured (such as devices that are passed through), you can initiate a live migration with the `--online` flag in the `qm migration` command evocation. The web interface defaults to live migration when the VM is running.

{% hint style="info" %}
Live migration is only possible between hosts of the same CPU architecture. A running guest’s CPU state cannot be transferred between an x86 and an arm64 host.
{% endhint %}

#### How it works <a href="#_how_it_works" id="_how_it_works"></a>

Online migration first starts a new QEMU process on the target host with the *incoming* flag, which performs only basic initialization with the guest vCPUs still paused and then waits for the guest memory and device state data streams of the source Virtual Machine. All other resources, such as disks, are either shared or got already sent before runtime state migration of the VMs begins; so only the memory content and device state remain to be transferred.

Once this connection is established, the source begins asynchronously sending the memory content to the target. If the guest memory on the source changes, those sections are marked dirty and another pass is made to send the guest memory data. This loop is repeated until the data difference between running source VM and incoming target VM is small enough to be sent in a few milliseconds, because then the source VM can be paused completely, without a user or program noticing the pause, so that the remaining data can be sent to the target, and then unpause the targets VM’s CPU to make it the new running VM in well under a second.

#### Requirements <a href="#_requirements" id="_requirements"></a>

For Live Migration to work, there are some things required:

- The VM has no local resources that cannot be migrated. For example, PCI or USB devices that are passed through currently block live-migration. Local Disks, on the other hand, can be migrated by sending them to the target just fine.
- The hosts are located in the same Proxmox VE cluster.
- The hosts have a working (and reliable) network connection between them.
- The target host must have the same, or higher versions of the Proxmox VE packages. Although it can sometimes work the other way around, this cannot be guaranteed.
- The hosts have CPUs from the same vendor with similar capabilities. Different vendor **might** work depending on the actual models and VMs CPU type configured, but it cannot be guaranteed \- so please test before deploying such a setup in production.

#### Conntrack State Migration <a href="#_conntrack_state_migration" id="_conntrack_state_migration"></a>

{% hint style="info" %}
Conntrack state migration is considered best-effort only and might not work, as it heavily depends on the network setup. For example, setups using source address masquerading (SNAT) on the host will most likely **not** work.
{% endhint %}

Conntrack is a Linux kernel mechanism to enable a stateful firewall by tracking individual connection. When live migrating running VMs, active in- and/or outbound connections **might** get interrupted as soon as the VM starts running on the target host, as the new host node does not have the same conntrack entries and thus the firewall can drop packets.

Conntrack state migration copies all conntrack entries on the host for the live-migrated VM to the target node and afterwards flushes the migrated entries from the conntrack table on the source node.

### Offline Migration <a href="#_offline_migration" id="_offline_migration"></a>

If you have local resources, you can still migrate your VMs offline as long as all disk are on storage defined on both hosts. Migration then copies the disks to the target host over the network, as with online migration. Note that any hardware passthrough configuration may need to be adapted to the device location on the target host.

## Copies and Clones <a href="#qm_copy_and_clone" id="qm_copy_and_clone"></a>

[![screenshot/gui-qemu-full-clone.png](../assets/screenshot-gui-qemu-full-clone-png-cd406793042e.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-full-clone.png)

VM installation is usually done using an installation media (CD-ROM) from the operating system vendor. Depending on the OS, this can be a time consuming task one might want to avoid.

An easy way to deploy many VMs of the same type is to copy an existing VM. We use the term *clone* for such copies, and distinguish between *linked* and *full* clones.

**Full Clone**

The result of such copy is an independent VM. The new VM does not share any storage resources with the original.

It is possible to select a **Target Storage**, so one can use this to migrate a VM to a totally different storage. You can also change the disk image **Format** if the storage driver supports several formats.

{% hint style="info" %}
A full clone needs to read and copy all VM image data. This is usually much slower than creating a linked clone.
{% endhint %}

Some storage types allows to copy a specific **Snapshot**, which defaults to the *current* VM data. This also means that the final copy never includes any additional snapshots from the original VM.

**Linked Clone**

Modern storage drivers support a way to generate fast linked clones. Such a clone is a writable copy whose initial contents are the same as the original data. Creating a linked clone is nearly instantaneous, and initially consumes no additional space.

They are called *linked* because the new image still refers to the original. Unmodified data blocks are read from the original image, but modification are written (and afterwards read) from a new location. This technique is called *Copy-on-write*.

This requires that the original volume is read-only. With Proxmox VE one can convert any VM into a read-only  [Template](#qm_templates)). Such templates can later be used to create linked clones efficiently.

{% hint style="info" %}
You cannot delete an original template while linked clones exist.
{% endhint %}

It is not possible to change the **Target storage** for linked clones, because this is a storage internal feature.

The **Target node** option allows you to create the new VM on a different node. The only restriction is that the VM is on shared storage, and that storage is also available on the target node.

To avoid resource conflicts, all network interface MAC addresses get randomized, and we generate a new *UUID* for the VM BIOS (smbios1) setting.

## Virtual Machine Templates <a href="#qm_templates" id="qm_templates"></a>

One can convert a VM into a Template. Such templates are read-only, and you can use them to create linked clones.

{% hint style="info" %}
It is not possible to start templates, because this would modify the disk images. If you want to change the template, create a linked clone and modify that.
{% endhint %}

## VM Generation ID <a href="#_vm_generation_id" id="_vm_generation_id"></a>

Proxmox VE supports Virtual Machine Generation ID (*vmgenid*) [\[15\]](#note-0cdd31f9-15) for virtual machines. This can be used by the guest operating system to detect any event resulting in a time shift event, for example, restoring a backup or a snapshot rollback.

When creating new VMs, a *vmgenid* will be automatically generated and saved in its configuration file.

To create and add a *vmgenid* to an already existing VM one can pass the special value ‘1’ to let Proxmox VE autogenerate one or manually set the *UUID*
[\[16\]](#note-0cdd31f9-16) by using it as value, for example:

```text
# qm set VMID -vmgenid 1
# qm set VMID -vmgenid 00000000-0000-0000-0000-000000000000
```

{% hint style="info" %}
The initial addition of a *vmgenid* device to an existing VM, may result in the same effects as a change on snapshot rollback, backup restore, etc., has as the VM can interpret this as generation change.
{% endhint %}

In the rare case the *vmgenid* mechanism is not wanted one can pass ‘0’ for its value on VM creation, or retroactively delete the property in the configuration with:

```text
# qm set VMID -delete vmgenid
```

The most prominent use case for *vmgenid* are newer Microsoft Windows operating systems, which use it to avoid problems in time sensitive or replicate services (such as databases or domain controller [\[17\]](#note-0cdd31f9-17)) on snapshot rollback, backup restore or a whole VM clone operation.

## Importing Virtual Machines <a href="#qm_import_virtual_machines" id="qm_import_virtual_machines"></a>

Importing existing virtual machines from foreign hypervisors or other Proxmox VE clusters can be achieved through various methods, the most common ones are:

- Using the native import wizard, which utilizes the *import* content type, such as provided by the ESXi special storage.
- Performing a backup on the source and then restoring on the target. This method works best when migrating from another Proxmox VE instance.
- using the OVF-specific import command of the `qm` command-line tool.

If you import VMs to Proxmox VE from other hypervisors, it’s recommended to familiarize yourself with the [concepts of Proxmox VE](https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE#Concepts).

### Import Wizard <a href="#_import_wizard" id="_import_wizard"></a>

[![screenshot/gui-import-wizard-general.png](../assets/screenshot-gui-import-wizard-general-png-988ac134e0fc.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-import-wizard-general.png)

Proxmox VE provides an integrated VM importer using the storage plugin system for native integration into the API and web-based user interface. You can use this to import the VM as a whole, with most of its config mapped to Proxmox VE’s config model and reduced downtime.

{% hint style="info" %}
The import wizard was added during the Proxmox VE 8.2 development cycle and is in tech preview state. While it’s already promising and working stable, it’s still under active development.
{% endhint %}

To use the import wizard you have to first set up a new storage for an import source, you can do so on the web-interface under *Datacenter → Storage → Add*.

Then you can select the new storage in the resource tree and use the *Virtual Guests* content tab to see all available guests that can be imported.

[![screenshot/gui-import-wizard-advanced.png](../assets/screenshot-gui-import-wizard-advanced-png-6fe679ff204b.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-import-wizard-advanced.png)

Select one and use the *Import* button (or double-click) to open the import wizard. You can modify a subset of the available options here and then start the import. Please note that you can do more advanced modifications after the import finished.

{% hint style="success" %}
The ESXi import wizard has been tested with ESXi versions 6.5 through 8.0. Note that guests using vSAN storage cannot be directly imported directly; their disks must first be moved to another storage. While it is possible to use a vCenter as the import source, performance is dramatically degraded (5 to 10 times slower).
{% endhint %}

For a step-by-step guide and tips for how to adapt the virtual guest to the new hyper-visor see our [migrate to Proxmox VE wiki article](https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE#Migration).

#### OVA/OVF Import <a href="#_ova_ovf_import" id="_ova_ovf_import"></a>

To import OVA/OVF files, you first need a File-based storage with the *import* content type. On this storage, there will be an *import* folder where you can put OVA files or OVF files with the corresponding images in a flat structure. Alternatively you can use the web UI to upload or download OVA files directly. You can then use the web UI to select those and use the import wizard to import the guests.

For OVA files, there is additional space needed to temporarily extract the image. This needs a file-based storage that has the *images* content type configured. By default the source storage is selected for this, but you can specify a *Import Working Storage* on which the images will be extracted before importing to the actual target storage.

{% hint style="info" %}
Since OVA/OVF file structure and content are not always well maintained or defined, it might be necessary to adapt some guest settings manually. For example the SCSI controller type is almost never defined in OVA/OVF files, but the default is unbootable with OVMF (UEFI), so you should select *Virtio SCSI* or *VMware PVSCSI* for these cases.
{% endhint %}

### Import OVF/OVA Through CLI <a href="#_import_ovf_ova_through_cli" id="_import_ovf_ova_through_cli"></a>

A VM export from a foreign hypervisor takes usually the form of one or more disk images, with a configuration file describing the settings of the VM (RAM, number of cores).  
 The disk images can be in the vmdk format, if the disks come from VMware or VirtualBox, or qcow2 if the disks come from a KVM hypervisor. The most popular configuration format for VM exports is the OVF standard, but in practice interoperation is limited because many settings are not implemented in the standard itself, and hypervisors export the supplementary information in non-standard extensions.

Besides the problem of format, importing disk images from other hypervisors may fail if the emulated hardware changes too much from one hypervisor to another. Windows VMs are particularly concerned by this, as the OS is very picky about any changes of hardware. This problem may be solved by installing the MergeIDE.zip utility available from the Internet before exporting and choosing a hard disk type of **IDE** before booting the imported Windows VM.

Finally there is the question of paravirtualized drivers, which improve the speed of the emulated system and are specific to the hypervisor. GNU/Linux and other free Unix OSes have all the necessary drivers installed by default and you can switch to the paravirtualized drivers right after importing the VM. For Windows VMs, you need to install the Windows paravirtualized drivers by yourself.

GNU/Linux and other free Unix can usually be imported without hassle. Note that we cannot guarantee a successful import/export of Windows VMs in all cases due to the problems above.

#### Step-by-step example of a Windows OVF import <a href="#_step_by_step_example_of_a_windows_ovf_import" id="_step_by_step_example_of_a_windows_ovf_import"></a>

Microsoft provides [Virtual Machines downloads](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/) to get started with Windows development.We are going to use one of these to demonstrate the OVF import feature.

##### Download the Virtual Machine zip <a href="#_download_the_virtual_machine_zip" id="_download_the_virtual_machine_zip"></a>

After getting informed about the user agreement, choose the *Windows 10 Enterprise (Evaluation \- Build)* for the VMware platform, and download the zip.

##### Extract the disk image from the zip <a href="#_extract_the_disk_image_from_the_zip" id="_extract_the_disk_image_from_the_zip"></a>

Using the `unzip` utility or any archiver of your choice, unpack the zip, and copy via ssh/scp the ovf and vmdk files to your Proxmox VE host.

##### Import the Virtual Machine <a href="#_import_the_virtual_machine" id="_import_the_virtual_machine"></a>

This will create a new virtual machine, using cores, memory and VM name as read from the OVF manifest, and import the disks to the `local-lvm` storage. You have to configure the network manually.

```text
# qm importovf 999 WinDev1709Eval.ovf local-lvm
```

The VM is ready to be started.

##### Adding an external disk image to a Virtual Machine <a href="#_adding_an_external_disk_image_to_a_virtual_machine" id="_adding_an_external_disk_image_to_a_virtual_machine"></a>

You can also add an existing disk image to a VM, either coming from a foreign hypervisor, or one that you created yourself.

Suppose you created a Debian/Ubuntu disk image with the *vmdebootstrap* tool:

```text
vmdebootstrap --verbose \
 --size 10GiB --serial-console \
 --grub --no-extlinux \
 --package openssh-server \
 --package avahi-daemon \
 --package qemu-guest-agent \
 --hostname vm600 --enable-dhcp \
 --customize=./copy_pub_ssh.sh \
 --sparse --image vm600.raw
```

You can now create a new target VM, importing the image to the storage `pvedir` and attaching it to the VM’s SCSI controller:

```text
# qm create 600 --net0 virtio,bridge=vmbr0 --name vm600 --serial0 socket \
   --boot order=scsi0 --scsihw virtio-scsi-pci --ostype l26 \
   --scsi0 pvedir:0,import-from=/path/to/dir/vm600.raw
```

The VM is ready to be started.

## Cloud-Init Support <a href="#qm_cloud_init" id="qm_cloud_init"></a>

[Cloud-Init](https://cloudinit.readthedocs.io) is the de facto multi-distribution package that handles early initialization of a virtual machine instance. Using Cloud-Init, configuration of network devices and ssh keys on the hypervisor side is possible. When the VM starts for the first time, the Cloud-Init software inside the VM will apply those settings.

Many Linux distributions provide ready-to-use Cloud-Init images, mostly designed for *OpenStack*. These images will also work with Proxmox VE. While it may seem convenient to get such ready-to-use images, we usually recommended to prepare the images by yourself. The advantage is that you will know exactly what you have installed, and this helps you later to easily customize the image for your needs.

Once you have created such a Cloud-Init image we recommend to convert it into a VM template. From a VM template you can quickly create linked clones, so this is a fast method to roll out new VM instances. You just need to configure the network (and maybe the ssh keys) before you start the new VM.

We recommend using SSH key-based authentication to login to the VMs provisioned by Cloud-Init. It is also possible to set a password, but this is not as safe as using SSH key-based authentication because Proxmox VE needs to store an encrypted version of that password inside the Cloud-Init data.

Proxmox VE generates an ISO image to pass the Cloud-Init data to the VM. For that purpose, all Cloud-Init VMs need to have an assigned CD-ROM drive. Usually, a serial console should be added and used as a display. Many Cloud-Init images rely on this, it is a requirement for OpenStack. However, other images might have problems with this configuration. Switch back to the default display configuration if using a serial console doesn’t work.

### Preparing Cloud-Init Templates <a href="#_preparing_cloud_init_templates" id="_preparing_cloud_init_templates"></a>

The first step is to prepare your VM. Basically you can use any VM. Simply install the Cloud-Init packages **inside the VM** that you want to prepare. On Debian/Ubuntu based systems this is as simple as:

```text
apt-get install cloud-init
```

{% hint style="warning" %}
This command is **not** intended to be executed on the Proxmox VE host, but only inside the VM.
{% endhint %}

Already many distributions provide ready-to-use Cloud-Init images (provided as `.qcow2` files), so alternatively you can simply download and import such images. For the following example, we will use the cloud image provided by Ubuntu at [https://cloud-images.ubuntu.com](https://cloud-images.ubuntu.com).

```text
# download the image
wget https://cloud-images.ubuntu.com/bionic/current/bionic-server-cloudimg-amd64.img

# create a new VM with VirtIO SCSI controller
qm create 9000 --memory 2048 --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-pci

# import the downloaded disk to the local-lvm storage, attaching it as a SCSI drive
qm set 9000 --scsi0 local-lvm:0,import-from=/path/to/bionic-server-cloudimg-amd64.img
```

{% hint style="info" %}
Ubuntu Cloud-Init images require the `virtio-scsi-pci` controller type for SCSI drives.
{% endhint %}

[![screenshot/gui-cloudinit-hardware.png](../assets/screenshot-gui-cloudinit-hardware-png-a02f91a43c57.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cloudinit-hardware.png)

**Add Cloud-Init CD-ROM drive**

The next step is to configure a CD-ROM drive, which will be used to pass the Cloud-Init data to the VM.

```text
qm set 9000 --ide2 local-lvm:cloudinit
```

To be able to boot directly from the Cloud-Init image, set the `boot` parameter to `order=scsi0` to restrict BIOS to boot from this disk only. This will speed up booting, because VM BIOS skips the testing for a bootable CD-ROM.

```text
qm set 9000 --boot order=scsi0
```

For many Cloud-Init images, it is required to configure a serial console and use it as a display. If the configuration doesn’t work for a given image however, switch back to the default display instead.

```text
qm set 9000 --serial0 socket --vga serial0
```

In a last step, it is helpful to convert the VM into a template. From this template you can then quickly create linked clones. The deployment from VM templates is much faster than creating a full clone (copy).

```text
qm template 9000
```

### Deploying Cloud-Init Templates <a href="#_deploying_cloud_init_templates" id="_deploying_cloud_init_templates"></a>

[![screenshot/gui-cloudinit-config.png](../assets/screenshot-gui-cloudinit-config-png-19f801d9de33.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-cloudinit-config.png)

You can easily deploy such a template by cloning:

```text
qm clone 9000 123 --name ubuntu2
```

Then configure the SSH public key used for authentication, and configure the IP setup:

```text
qm set 123 --sshkey ~/.ssh/id_rsa.pub
qm set 123 --ipconfig0 ip=10.0.10.123/24,gw=10.0.10.1
```

You can also configure all the Cloud-Init options using a single command only. We have simply split the above example to separate the commands for reducing the line length. Also make sure to adopt the IP setup for your specific environment.

### Custom Cloud-Init Configuration <a href="#_custom_cloud_init_configuration" id="_custom_cloud_init_configuration"></a>

The Cloud-Init integration also allows custom config files to be used instead of the automatically generated configs. This is done via the `cicustom` option on the command line:

```text
qm set 9000 --cicustom "user=<volume>,network=<volume>,meta=<volume>"
```

The custom config files have to be on a storage that supports snippets and have to be available on all nodes the VM is going to be migrated to. Otherwise the VM won’t be able to start. For example:

```text
qm set 9000 --cicustom "user=local:snippets/userconfig.yaml"
```

There are three kinds of configs for Cloud-Init. The first one is the `user` config as seen in the example above. The second is the `network` config and the third the `meta` config. They can all be specified together or mixed and matched however needed. The automatically generated config will be used for any that don’t have a custom config file specified.

The generated config can be dumped to serve as a base for custom configs:

```text
qm cloudinit dump 9000 user
```

The same command exists for `network` and `meta`.

### Cloud-Init on Windows <a href="#_cloud_init_on_windows" id="_cloud_init_on_windows"></a>

There is a reimplementation of Cloud-Init available for Windows called [cloudbase-init](https://cloudbase.it/). Not every feature of Cloud-Init is available with Cloudbase-Init, and some features differ compared to Cloud-Init.

Cloudbase-Init requires both `ostype` set to any Windows version and the `citype` set to `configdrive2`, which is the default with any Windows `ostype`.

There are no ready-made cloud images for Windows available for free. Using Cloudbase-Init requires manually installing and configuring a Windows guest.

### Preparing Cloudbase-Init Templates <a href="#_preparing_cloudbase_init_templates" id="_preparing_cloudbase_init_templates"></a>

The first step is to install Windows in a VM. Download and install Cloudbase-Init in the guest. It may be necessary to install the Beta version. Don’t run Sysprep at the end of the installation. Instead configure Cloudbase-Init first.

A few common options to set would be:

- *username*: This sets the username of the administrator
- *groups*: This allows one to add the user to the `Administrators` group
- *inject\_user\_password*: Set this to `true` to allow setting the password in the VM config
- *first\_logon\_behaviour*: Set this to `no` to not require a new password on login
- *rename\_admin\_user*: Set this to `true` to allow renaming the default `Administrator` user to the username specified with `username`
- *metadata\_services*: Set this to `cloudbaseinit.metadata.services.configdrive.ConfigDriveService` for Cloudbase-Init to first check this service. Otherwise it may take a few minutes for Cloudbase-Init to configure the system after boot.

Some plugins, for example the SetHostnamePlugin, require reboots and will do so automatically. To disable automatic reboots by Cloudbase-Init, you can set `allow_reboot` to `false`.

A full set of configuration options can be found in the [official cloudbase-init documentation](https://cloudbase-init.readthedocs.io/en/latest/config.html).

It can make sense to make a snapshot after configuring in case some parts of the config still need adjustments. After configuring Cloudbase-Init you can start creating the template. Shutdown the Windows guest, add a Cloud-Init disk and make it into a template.

```text
qm set 9000 --ide2 local-lvm:cloudinit
qm template 9000
```

Clone the template into a new VM:

```text
qm clone 9000 123 --name windows123
```

Then set the password, network config and SSH key:

```text
qm set 123 --cipassword <password>
qm set 123 --ipconfig0 ip=10.0.10.123/24,gw=10.0.10.1
qm set 123 --sshkey ~/.ssh/id_rsa.pub
```

Make sure that the `ostype` is set to any Windows version before setting the password. Otherwise the password will be encrypted and Cloudbase-Init will use the encrypted password as plaintext password.

When everything is set, start the cloned guest. On the first boot the login won’t work and it will reboot automatically for the changed hostname. After the reboot the new password should be set and login should work.

### Cloudbase-Init and Sysprep <a href="#_cloudbase_init_and_sysprep" id="_cloudbase_init_and_sysprep"></a>

Sysprep is a feature to reset the configuration of Windows and provide a `new` system. This can be used in conjunction with Cloudbase-Init to create a clean template.

When using Sysprep there are 2 configuration files that need to be adapted. The first one is the normal configuration file, the second one is the one ending in `-unattend.conf`.

Cloudbase-Init runs in 2 steps, first the Sysprep step using the `-unattend.conf` and then the regular step using the primary config file.

For `Windows Server` running Sysprep with the provided `Unattend.xml` file should work out of the box. Normal Windows versions however require additional steps:

1. Open a PowerShell instance
2. Enable the Administrator user:

   ```text
   net user Administrator /active:yes`
   ```
3. Install Cloudbase-Init using the Administrator user
4. Modify `Unattend.xml` to include the command to enable the Administrator user on the first boot after sysprepping:

   ```text
   <RunSynchronousCommand wcm:action="add">
     <Path>net user administrator /active:yes</Path>
     <Order>1</Order>
     <Description>Enable Administrator User</Description>
   </RunSynchronousCommand>
   ```

   Make sure the `<Order>` does not conflict with other synchronous commands. Modify `<Order>` of the Cloudbase-Init command to run after this one by increasing the number to a higher value: `<Order>2</Order>`
5. (Windows 11 only) Remove the conflicting Microsoft.OneDriveSync package:

   ```text
   Get-AppxPackage -AllUsers Microsoft.OneDriveSync | Remove-AppxPackage -AllUsers
   ```
6. `cd` into the Cloudbase-Init config directory:

   ```text
   cd 'C:\Program Files\Cloudbase Solutions\Cloudbase-Init\conf'
   ```
7. (optional) Create a snapshot of the VM before Sysprep in case of a misconfiguration
8. Run Sysprep:

   ```text
   C:\Windows\System32\Sysprep\sysprep.exe /generalize /oobe /unattend:Unattend.xml
   ```

After following the above steps the VM should be in shut down state due to the Sysprep. Now you can make it into a template, clone it and configure it as needed.

### Cloud-Init specific Options <a href="#_cloud_init_specific_options" id="_cloud_init_specific_options"></a>

**`cicustom`: `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

Specify custom files to replace the automatically generated ones at start.

**`meta`\=`<volume>`**

Specify a custom file containing all meta data passed to the VM via cloud-init. This is provider specific meaning configdrive2 and nocloud differ.

**`network`\=`<volume>`**

To pass a custom file containing all network data to the VM via cloud-init.

**`user`\=`<volume>`**

To pass a custom file containing all user data to the VM via cloud-init.

**`vendor`\=`<volume>`**

To pass a custom file containing all vendor data to the VM via cloud-init.

**`cipassword`: `<string>`**

Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords.

**`citype`: `<configdrive2 | nocloud | opennebula>`**

Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows.

**`ciupgrade`: `<boolean>` (*default \=* `1`)**

do an automatic package upgrade after the first boot.

**`ciuser`: `<string>`**

User name to change ssh keys and password for instead of the image’s configured default user.

**`ipconfig[n]`: `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string *dhcp* can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string *auto* can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4.

**`gw`\=`<GatewayIPv4>`**

IPv4 流量的默认网关。

{% hint style="info" %}
Requires option(s): `ip`
{% endhint %}

**`gw6`\=`<GatewayIPv6>`**

IPv6 流量的默认网关。

{% hint style="info" %}
Requires option(s): `ip6`
{% endhint %}

**`ip`\=`<IPv4Format/CIDR>` (*default \=* `dhcp`)**

CIDR 格式的 IPv4 地址。

**`ip6`\=`<IPv6Format/CIDR>` (*default \=* `dhcp`)**

CIDR 格式的 IPv6 地址。

**`nameserver`: `<string>`**

Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`searchdomain`: `<string>`**

Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`sshkeys`: `<string>`**

设置 SSH 公钥（每行一个密钥，OpenSSH 格式）。

## PCI(e) Passthrough <a href="#qm_pci_passthrough" id="qm_pci_passthrough"></a>

PCI(e) passthrough is a mechanism to give a virtual machine control over a PCI device from the host. This can have some advantages over using virtualized hardware, for example lower latency, higher performance, or more features (e.g., offloading).

But, if you pass through a device to a virtual machine, you cannot use that device anymore on the host or in any other VM.

Note that, while PCI passthrough is available for i440fx and q35 machines, PCIe passthrough is only available on q35 machines. This does not mean that PCIe-capable devices that are passed through as PCI devices will only run at PCI speeds. Passing through devices as PCIe just sets a flag for the guest to tell it that the device is a PCIe device instead of a "really fast legacy PCI device". Some guest applications benefit from this.

### General Requirements <a href="#_general_requirements" id="_general_requirements"></a>

Since passthrough is performed on real hardware, it needs to fulfill some requirements. A brief overview of these requirements is given below, for more information on specific devices, see [PCI Passthrough Examples](https://pve.proxmox.com/wiki/PCI_Passthrough).

#### Hardware <a href="#_hardware" id="_hardware"></a>

Your hardware needs to support `IOMMU` (**I**/**O** **M**emory **M**anagement **U**nit) interrupt remapping, this includes the CPU and the motherboard.

Generally, Intel systems with VT-d and AMD systems with AMD-Vi support this. On arm64, the equivalent is the System Memory Management Unit (SMMU), provided by supported platforms. It is not guaranteed that everything will work out of the box, due to bad hardware implementation and missing or low quality drivers.

Further, server grade hardware has often better support than consumer grade hardware, but even then, many modern systems can support this.

Please refer to your hardware vendor to check if they support this feature under Linux for your specific setup.

#### Determining PCI Card Address <a href="#_determining_pci_card_address" id="_determining_pci_card_address"></a>

The easiest way is to use the GUI to add a device of type "Host PCI" in the VM’s hardware tab. Alternatively, you can use the command line.

You can locate your card using

```text
 lspci
```

#### Configuration <a href="#_configuration" id="_configuration"></a>

Once you ensured that your hardware supports passthrough, you will need to do some configuration to enable PCI(e) passthrough.

**IOMMU**

You will have to enable IOMMU support in your BIOS/UEFI. Usually the corresponding setting is called `IOMMU` or `VT-d`, but you should find the exact option name in the manual of your motherboard.

With AMD CPUs IOMMU is enabled by default. With recent kernels (6.8 or newer), this is also true for Intel CPUs. On older kernels, it is necessary to enable it on Intel CPUs via the kernel command line by adding:

```text
 intel_iommu=on
```

{% hint style="info" %}
The `intel_iommu=on` parameter applies to x86 hosts. On arm64, the SMMU is enabled through firmware and ACPI, so no such kernel command line parameter is needed.
{% endhint %}

**IOMMU Passthrough Mode**

If your hardware supports IOMMU passthrough mode, enabling this mode might increase performance. This is because VMs then bypass the (default) DMA translation normally performed by the hypervisor and instead pass DMA requests directly to the hardware IOMMU. To enable these options, add:

```text
 iommu=pt
```

to the kernel commandline.

**Kernel Modules**

Make sure the following modules are loaded by adding them to a file under `'/etc/modules-load.d/'`, for example `'/etc/modules-load.d/vfio.conf'`:

{% hint style="info" %}
**Mediated devices passthrough**

If passing through mediated devices (e.g. vGPUs), the following is not needed. In these cases, the device will be owned by the appropriate host driver directly.
{% endhint %}

```text
 vfio
 vfio_iommu_type1
 vfio_pci
```

<a id="qm_pci_passthrough_update_initramfs"></a>



After changing anything modules related, you need to refresh your `initramfs`. On Proxmox VE this can be done by executing:

```text
# update-initramfs -u -k all
```

To check if the modules are being loaded, the output of

```text
# lsmod | grep vfio
```

should include the three modules from above.

**Finish Configuration**

Finally, reboot to bring the changes into effect and check that IOMMU is indeed enabled.

```text
# dmesg | grep -e DMAR -e IOMMU -e AMD-Vi
```

should display that `IOMMU`, `Directed I/O` or `Interrupt Remapping` is enabled, depending on hardware and kernel the exact message can vary.

For notes on how to troubleshoot or verify if IOMMU is working as intended, please see the [Verifying IOMMU Parameters](https://pve.proxmox.com/wiki/PCI_Passthrough#Verifying_IOMMU_parameters) section in our wiki.

It is also important that the device(s) you want to pass through are in a **separate** `IOMMU` group. This can be checked with a call to the Proxmox VE API:

```text
# pvesh get /nodes/{nodename}/hardware/pci --pci-class-blacklist ""
```

It is okay if the device is in an `IOMMU` group together with its functions (e.g. a GPU with the HDMI Audio device) or with its root port or PCI(e) bridge.

{% hint style="info" %}
**PCI(e) slots**

Some platforms handle their physical PCI(e) slots differently. Sometimes it can help to put the card in another PCI(e) slot, if you do not get the desired `IOMMU` group separation.
{% endhint %}

{% hint style="info" %}
**Unsafe interrupts**

For some platforms, it may be necessary to allow unsafe interrupts. To do so, add the following line to a file ending in `.conf` under **/etc/modprobe.d/**:

```text
 options vfio_iommu_type1 allow_unsafe_interrupts=1
```

Please be aware that this option can make your system unstable.
{% endhint %}

#### GPU Passthrough Notes <a href="#_gpu_passthrough_notes" id="_gpu_passthrough_notes"></a>

It is not possible to display the frame buffer of the GPU via NoVNC or SPICE on the Proxmox VE web interface.

When passing through a whole GPU or a vGPU and graphic output is wanted, one has to either physically connect a monitor to the card, or configure a remote desktop software (for example, VNC or RDP) inside the guest.

If you only want to use the GPU as a hardware accelerator — for example, with programs using OpenCL or CUDA — this isn’t necessary.

### Host Device Passthrough <a href="#_host_device_passthrough" id="_host_device_passthrough"></a>

The most used variant of PCI(e) passthrough is to pass through a whole PCI(e) card, for example a GPU or a network card.

#### Host Configuration <a href="#_host_configuration" id="_host_configuration"></a>

Proxmox VE tries to automatically make the PCI(e) device unavailable for the host. However, if this doesn’t work, there are two things that can be done:

- pass the device IDs to the options of the *vfio-pci* modules by adding

  ```text
   options vfio-pci ids=1234:5678,4321:8765
  ```

  to a `.conf` file in **/etc/modprobe.d/** where `1234:5678` and `4321:8765` are the vendor and device IDs obtained by:

  ```text
  # lspci -nn
  ```
- blacklist the driver on the host completely, ensuring it is free to bind for passthrough instead, by adding

  ```text
   blacklist DRIVERNAME
  ```

  to a `.conf` file in **/etc/modprobe.d/**.

  To find the driver name, execute

  ```text
  # lspci -k
  ```

  for example:

  ```text
  # lspci -k | grep -A 3 "VGA"
  ```

  will output something similar to

  ```text
  01:00.0 VGA compatible controller: NVIDIA Corporation GP108 [GeForce GT 1030] (rev a1)
          Subsystem: Micro-Star International Co., Ltd. [MSI] GP108 [GeForce GT 1030]
          Kernel driver in use: <some-module>
          Kernel modules: <some-module>
  ```

  Now we can blacklist the drivers by writing them into a `.conf` file:

  ```text
  echo "blacklist <some-module>" >> /etc/modprobe.d/blacklist.conf
  ```

For both methods you need to [update the `initramfs`](#qm_pci_passthrough_update_initramfs) and reboot after that.

Should this not work, you might need to set a soft dependency to load *vfio-pci* before loading the GPU modules. This can be done with the *softdep* flag, see also the manpages on *modprobe.d* for more information.

For example, if you are using drivers named \<some-module\>:

```text
# echo "softdep <some-module> pre: vfio-pci" >> /etc/modprobe.d/<some-module>.conf
```

**Verify Configuration**

To check if your changes were successful, you can use

```text
# lspci -nnk
```

and check your device entry. If it says

```text
Kernel driver in use: vfio-pci
```

or the *in use* line is missing entirely, the device is ready to be used for passthrough.

{% hint style="info" %}
**Mediated devices**

For mediated devices this line will differ as the device will be owned by the host driver directly, not *vfio-pci*.
{% endhint %}

#### VM Configuration <a href="#qm_pci_passthrough_vm_config" id="qm_pci_passthrough_vm_config"></a>

When passing through a GPU, the best compatibility is reached when using *q35* as machine type, *OVMF* (*UEFI* for VMs) instead of SeaBIOS and PCIe instead of PCI. Note that if you want to use *OVMF* for GPU passthrough, the GPU needs to have a UEFI-capable ROM, otherwise use SeaBIOS instead. To check if the ROM is UEFI capable, see the [PCI Passthrough Examples](https://pve.proxmox.com/wiki/PCI_Passthrough#How_to_know_if_a_graphics_card_is_UEFI_.28OVMF.29_compatible) wiki.

Furthermore, when using OVMF, VGA arbitration can potentially be disabled, which reduces the amount of legacy code that needs to run at boot. To disable VGA arbitration:

```text
 echo "options vfio-pci ids=<vendor-id>,<device-id> disable_vga=1" > /etc/modprobe.d/vfio.conf
```

replacing the \<vendor-id\> and \<device-id\> with the ones obtained from:

```text
# lspci -nn
```

PCI devices can be added in the web interface in the hardware section of the VM. Alternatively, you can use the command line; set the **hostpciX** option in the VM configuration, for example by executing:

```text
# qm set VMID -hostpci0 00:02.0
```

or by adding a line to the VM configuration file:

```text
 hostpci0: 00:02.0
```

If your device has multiple functions (e.g., ‘`00:02.0`’ and ‘`00:02.1`’ ), you can pass them through all together with the shortened syntax \`\`00:02\`*. This is equivalent to checking the \`\`All Functions\`* checkbox in the web interface.

There are some options which may be necessary, depending on the device and guest OS:

- **x-vga\=on\|off** marks the PCI(e) device as the primary GPU of the VM. With this enabled the **vga** configuration option will be ignored.
- **pcie\=on\|off** tells Proxmox VE to use a PCIe or PCI port. Some guests/device combinations require PCIe rather than PCI. PCIe is only available for *q35* machine types.
- **rombar\=on\|off** makes the firmware ROM visible for the guest. Default is on. Some PCI(e) devices need this disabled.
- **romfile\=\<path\>**, is an optional path to a ROM file for the device to use. This is a relative path under **/usr/share/kvm/**.

**Example**

An example of PCIe passthrough with a GPU set to primary:

```text
# qm set VMID -hostpci0 02:00,pcie=on,x-vga=on
```

**PCI ID overrides**

You can override the PCI vendor ID, device ID, and subsystem IDs that will be seen by the guest. This is useful if your device is a variant with an ID that your guest’s drivers don’t recognize, but you want to force those drivers to be loaded anyway (e.g. if you know your device shares the same chipset as a supported variant).

The available options are `vendor-id`, `device-id`, `sub-vendor-id`, and `sub-device-id`. You can set any or all of these to override your device’s default IDs.

例如：

```text
# qm set VMID -hostpci0 02:00,device-id=0x10f6,sub-vendor-id=0x0000
```

### SR-IOV <a href="#_sr_iov" id="_sr_iov"></a>

Another variant for passing through PCI(e) devices is to use the hardware virtualization features of your devices, if available.

{% hint style="info" %}
**Enabling SR-IOV**

To use SR-IOV, platform support is especially important. It may be necessary to enable this feature in the BIOS/UEFI first, or to use a specific PCI(e) port for it to work. If in doubt, consult the manual of the platform or contact its vendor.
{% endhint %}

*SR-IOV* (**S**ingle-**R**oot **I**nput/**O**utput **V**irtualization) enables a single device to provide multiple *VFs* (**V**irtual **F**unctions) to the system. Each of those *VFs* can be used in a different VM, with full hardware features and also better performance and lower latency than software-virtualized devices.

Currently, the most common use case for this is with NICs (**N**etwork **I**nterface **C**ard) with SR-IOV support, which can provide multiple VFs per physical port. This allows features such as checksum offloading to be used inside a VM, reducing the (host) CPU overhead.

#### Host Configuration <a href="#_host_configuration_2" id="_host_configuration_2"></a>

Generally, there are two methods for enabling virtual functions on a device.

- sometimes there is an option for the driver module e.g. for some Intel drivers

  ```text
   max_vfs=4
  ```

  which can be placed in a file with a *.conf* ending under **/etc/modprobe.d/**. (Do not forget to update your initramfs after that)

  Please refer to your driver module documentation for the exact parameters and options.
- The second, more generic, approach is using the `sysfs`. If a device and driver support this, you can change the number of VFs on the fly. For example, to set up 4 VFs on device 0000:01:00.0 execute:

  ```text
  # echo 4 > /sys/bus/pci/devices/0000:01:00.0/sriov_numvfs
  ```

  To make this change persistent, you can use the ‘sysfsutils\` Debian package. After installation, configure it via **/etc/sysfs.conf** or a \`FILE.conf’ in **/etc/sysfs.d/**.

#### VM Configuration <a href="#_vm_configuration" id="_vm_configuration"></a>

After creating VFs, you should see them as separate PCI(e) devices when outputting them with `lspci`. Get their ID and pass them through like a [normal PCI(e) device](#qm_pci_passthrough_vm_config).

### Mediated Devices (vGPU, GVT-g) <a href="#_mediated_devices_vgpu_gvt_g" id="_mediated_devices_vgpu_gvt_g"></a>

Mediated devices are another method to reuse features and performance from physical hardware for virtualized hardware. These are most commonly found in virtualized GPU setups such as Intel’s GVT-g and NVIDIA’s vGPUs used in their GRID technology.

With this, a physical card is able to create virtual cards, similar to SR-IOV. The difference is that mediated devices do not appear as PCI(e) devices on the host, and are thus only suited for use in virtual machines.

#### Host Configuration <a href="#_host_configuration_3" id="_host_configuration_3"></a>

In general, your card’s driver must support that feature, otherwise it will not work. So please refer to your vendor for compatible drivers and how to configure them.

Intel’s drivers for GVT-g are integrated in the kernel and should work with 5th, 6th and 7th generation Intel Core Processors, as well as E3 v4, E3 v5 and E3 v6 Xeon Processors.

To enable it for Intel Graphics, you have to make sure to load the module *kvmgt* (for example via `/etc/modules-load.d/`) and to enable it on the kernel commandline and add the following parameter:

```text
 i915.enable_gvt=1
```

After that remember to [update the `initramfs`](#qm_pci_passthrough_update_initramfs), and reboot your host.

#### VM Configuration <a href="#_vm_configuration_2" id="_vm_configuration_2"></a>

To use a mediated device, simply specify the `mdev` property on a `hostpciX` VM configuration option.

You can get the supported devices via the *sysfs*. For example, to list the supported types for the device *0000:00:02.0* you would simply execute:

```text
# ls /sys/bus/pci/devices/0000:00:02.0/mdev_supported_types
```

Each entry is a directory which contains the following important files:

- *available\_instances* contains the amount of still available instances of this type; each *mdev* used in a VM reduces this.
- *description* contains a short description about the capabilities of the type
- *create* is the endpoint to create such a device — Proxmox VE does this automatically for you if a *hostpciX* option with `mdev` is configured.

Example configuration with an `Intel GVT-g vGPU` (`Intel Skylake 6700k`):

```text
# qm set VMID -hostpci0 00:02.0,mdev=i915-GVTg_V5_4
```

With this set, Proxmox VE automatically creates such a device on VM start, and cleans it up again when the VM stops.

### Usage in Clusters <a href="#_use_in_clusters" id="_use_in_clusters"></a>

It is also possible to map devices at a cluster level, so that they can be properly used with HA and hardware changes are detected and non-root users can configure them. See [Resource Mapping](#resource_mapping) for details on that.

### vIOMMU (emulated IOMMU) <a href="#qm_pci_viommu" id="qm_pci_viommu"></a>

vIOMMU is the emulation of a hardware IOMMU within a virtual machine, providing improved memory access control and security for virtualized I/O devices. Using the vIOMMU option also allows you to pass through PCI(e) devices to level-2 VMs in level-1 VMs via [Nested Virtualization](https://pve.proxmox.com/wiki/Nested_Virtualization). To pass through physical PCI(e) devices from the host to nested VMs, follow the PCI(e) passthrough instructions.

There are currently two vIOMMU implementations available: Intel and VirtIO.

#### Intel vIOMMU <a href="#_intel_viommu" id="_intel_viommu"></a>

Intel vIOMMU-specific VM requirements:

- Whether you are using an Intel or AMD CPU on your host, it is important to set `intel_iommu=on` in the VM’s kernel parameters.
- To use Intel vIOMMU you need to set **q35** as the machine type.

If all requirements are met, you can add `viommu=intel` to the machine parameter in the configuration of the VM that should be able to pass through PCI devices.

```text
# qm set VMID -machine q35,viommu=intel
```

[QEMU documentation for VT-d](https://wiki.qemu.org/Features/VT-d)

#### VirtIO vIOMMU <a href="#_virtio_viommu" id="_virtio_viommu"></a>

This vIOMMU implementation is more recent and does not have as many limitations as Intel vIOMMU but is currently less used in production and less documented.

With VirtIO vIOMMU there is **no** need to set any kernel parameters. It is also **not** necessary to use q35 as the machine type, but it is advisable if you want to use PCIe.

```text
# qm set VMID -machine q35,viommu=virtio
```

[Blog-Post by Michael Zhao explaining virtio-iommu](https://web.archive.org/web/20230804075844/https://michael2012z.medium.com/virtio-iommu-789369049443)

## Hookscripts <a href="#_hookscripts" id="_hookscripts"></a>

You can add a hook script to VMs with the config property `hookscript`.

```text
# qm set 100 --hookscript local:snippets/hookscript.pl
```

It will be called during various phases of the guests lifetime. For an example and documentation see the example script under `/usr/share/pve-docs/examples/guest-example-hookscript.pl`.

## Hibernation <a href="#qm_hibernate" id="qm_hibernate"></a>

You can suspend a VM to disk with the GUI option `Hibernate` or with

```text
# qm suspend ID --todisk
```

That means that the current content of the memory will be saved onto disk and the VM gets stopped. On the next start, the memory content will be loaded and the VM can continue where it was left off.

<a id="qm_vmstatestorage"></a>



**State storage selection**

If no target storage for the memory is given, it will be automatically chosen, the first of:

1. The storage `vmstatestorage` from the VM config.
2. The first shared storage from any VM disk.
3. The first non-shared storage from any VM disk.
4. The storage `local` as a fallback.

## Resource Mapping <a href="#resource_mapping" id="resource_mapping"></a>

[![screenshot/gui-datacenter-resource-mappings.png](../assets/screenshot-gui-datacenter-resource-mappings-png-da2a9a26150d.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-resource-mappings.png)

When using or referencing local resources (e.g. address of a pci device), using the raw address or id is sometimes problematic, for example:

- when using HA, a different device with the same id or path may exist on the target node, and if one is not careful when assigning such guests to HA groups, the wrong device could be used, breaking configurations.
- changing hardware can change ids and paths, so one would have to check all assigned devices and see if the path or id is still correct.

To handle this better, one can define cluster wide resource mappings, such that a resource has a cluster unique, user selected identifier which can correspond to different devices on different hosts. With this, HA won’t start a guest with a wrong device, and hardware changes can be detected.

Creating such a mapping can be done with the Proxmox VE web GUI under `Datacenter` in the relevant tab in the `Resource Mappings` category, or on the cli with

```text
# pvesh create /cluster/mapping/<type> <options>
```

[![screenshot/gui-datacenter-mapping-pci-edit.png](../assets/screenshot-gui-datacenter-mapping-pci-edit-png-96b3f049d8df.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-mapping-pci-edit.png)

Where `<type>` is the hardware type (currently either `pci`, `usb` or [dir](#qm_virtiofs)) and `<options>` are the device mappings and other configuration parameters.

Note that the options must include a map property with all identifying properties of that hardware, so that it’s possible to verify the hardware did not change and the correct device is passed through.

For example to add a PCI device as `device1` with the path `0000:01:00.0` that has the device id `0001` and the vendor id `0002` on the node `node1`, and `0000:02:00.0` on `node2` you can add it with:

```text
# pvesh create /cluster/mapping/pci --id device1 \
 --map node=node1,path=0000:01:00.0,id=0002:0001 \
 --map node=node2,path=0000:02:00.0,id=0002:0001
```

You must repeat the `map` parameter for each node where that device should have a mapping (note that you can currently only map one USB device per node per mapping).

Using the GUI makes this much easier, as the correct properties are automatically picked up and sent to the API.

[![screenshot/gui-datacenter-mapping-usb-edit.png](../assets/screenshot-gui-datacenter-mapping-usb-edit-png-e01c9f9453d3.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-mapping-usb-edit.png)

It’s also possible for PCI devices to provide multiple devices per node with multiple map properties for the nodes. If such a device is assigned to a guest, the first free one will be used when the guest is started. The order of the paths given is also the order in which they are tried, so arbitrary allocation policies can be implemented.

This is useful for devices with SR-IOV, since some times it is not important which exact virtual function is passed through.

You can assign such a device to a guest either with the GUI or with

```text
# qm set ID -hostpci0 <name>
```

for PCI devices, or

```text
# qm set <vmid> -usb0 <name>
```

for USB devices.

Where `<vmid>` is the guests id and `<name>` is the chosen name for the created mapping. All usual options for passing through the devices are allowed, such as `mdev`.

To create mappings `Mapping.Modify` on `/mapping/<type>/<name>` is necessary (where `<type>` is the device type and `<name>` is the name of the mapping).

To use these mappings, `Mapping.Use` on `/mapping/<type>/<name>` is necessary (in addition to the normal guest privileges to edit the configuration).

**Additional Options**

There are additional options when defining a cluster wide resource mapping. Currently there are the following options:

- `mdev` (PCI): This marks the PCI device as being capable of providing `mediated devices`. When this is enabled, you can select a type when configuring it on the guest. If multiple PCI devices are selected for the mapping, the mediated device will be created on the first one where there are any available instances of the selected type.
- `live-migration-capable` (PCI): This marks the PCI device as being capable of being live migrated between nodes. This requires driver and hardware support. Only NVIDIA GPUs with recent kernel are known to support this. Note that live migrating passed through devices is an experimental feature and may not work or cause issues.

## Managing Virtual Machines with `qm` <a href="#_managing_virtual_machines_with_span_class_monospaced_qm_span" id="_managing_virtual_machines_with_span_class_monospaced_qm_span"></a>

qm is the tool to manage QEMU/KVM virtual machines on Proxmox VE. You can create and destroy virtual machines, and control execution (start/stop/suspend/resume). Besides that, you can use qm to set parameters in the associated config file. It is also possible to create and delete virtual disks.

### CLI Usage Examples <a href="#_cli_usage_examples" id="_cli_usage_examples"></a>

Using an iso file uploaded on the *local* storage, create a VM with a 4 GB IDE disk on the *local-lvm* storage

```text
# qm create 300 -ide0 local-lvm:4 -net0 e1000 -cdrom local:iso/proxmox-mailgateway_2.1.iso
```

Start the new VM

```text
# qm start 300
```

Send a shutdown request, then wait until the VM is stopped.

```text
# qm shutdown 300 && qm wait 300
```

Same as above, but only wait for 40 seconds.

```text
# qm shutdown 300 && qm wait 300 -timeout 40
```

If the VM does not shut down, force-stop it and overrule any running shutdown tasks. As stopping VMs may incur data loss, use it with caution.

```text
# qm stop 300 -overrule-shutdown 1
```

Destroying a VM always removes it from Access Control Lists and it always removes the firewall configuration of the VM. You have to activate *--purge*, if you want to additionally remove the VM from replication jobs, backup jobs and HA resource configurations.

{% hint style="info" %}
启用 purge 还会从所有引用该 HA 资源的亲和性规则中移除该资源，并移除仅剩这一个资源的规则。
{% endhint %}

```text
# qm destroy 300 --purge
```

Move a disk image to a different storage.

```text
# qm move-disk 300 scsi0 other-storage
```

Reassign a disk image to a different VM. This will remove the disk `scsi1` from the source VM and attaches it as `scsi3` to the target VM. In the background the disk image is being renamed so that the name matches the new owner.

```text
# qm move-disk 300 scsi1 --target-vmid 400 --target-disk scsi3
```

## Configuration <a href="#qm_configuration" id="qm_configuration"></a>

VM configuration files are stored inside the Proxmox cluster file system, and can be accessed at `/etc/pve/qemu-server/<VMID>.conf`. Like other files stored inside `/etc/pve/`, they get automatically replicated to all other cluster nodes.

{% hint style="info" %}
VMIDs \< 100 are reserved for internal purposes, and VMIDs need to be unique cluster wide.
{% endhint %}

**Example VM Configuration**

```text
boot: order=virtio0;net0
cores: 1
sockets: 1
memory: 512
name: webmail
ostype: l26
net0: e1000=EE:D2:28:5F:B6:3E,bridge=vmbr0
virtio0: local:vm-100-disk-1,size=32G
```

Those configuration files are simple text files, and you can edit them using a normal text editor (`vi`, `nano`, …). This is sometimes useful to do small corrections, but keep in mind that you need to restart the VM to apply such changes.

For that reason, it is usually better to use the `qm` command to generate and modify those files, or do the whole thing using the GUI. Our toolkit is smart enough to instantaneously apply most changes to running VM. This feature is called "hot plug", and there is no need to restart the VM in that case.

### File Format <a href="#_file_format" id="_file_format"></a>

VM configuration files use a simple colon separated key/value format. Each line has the following format:

```text
# this is a comment
OPTION: value
```

Blank lines in those files are ignored, and lines starting with a `#` character are treated as comments and are also ignored.

### Snapshots <a href="#qm_snapshots" id="qm_snapshots"></a>

When you create a snapshot, `qm` stores the configuration at snapshot time into a separate snapshot section within the same configuration file. For example, after creating a snapshot called “testsnapshot”, your configuration file will look like this:

**VM configuration with snapshot**

```text
memory: 512
swap: 512
parent: testsnaphot
...

[testsnaphot]
memory: 512
swap: 512
snaptime: 1457170803
...
```

There are a few snapshot related properties like `parent` and `snaptime`. The `parent` property is used to store the parent/child relationship between snapshots. `snaptime` is the snapshot creation time stamp (Unix epoch).

You can optionally save the memory of a running VM with the option `vmstate`. For details about how the target storage gets chosen for the VM state, see [State storage selection](#qm_vmstatestorage) in the chapter [Hibernation](#qm_hibernate).

### Options <a href="#qm_options" id="qm_options"></a>

**`acpi`: `<boolean>` (*default \=* `1`)**

Enable/disable ACPI.

**`affinity`: `<string>`**

List of host cores used to execute guest processes, for example: 0,5,8-11

**`agent`: `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

Enable/disable communication with the QEMU Guest Agent and its properties.

**`enabled`\=`<boolean>` (*default \=* `0`)**

Enable/disable communication with a QEMU Guest Agent (QGA) running in the VM.

**`freeze-fs`\=`<boolean>` (*default \=* `1`)**

Whether to issue the guest-fsfreeze-freeze and guest-fsfreeze-thaw QEMU guest agent commands. Backups in snapshot mode, clones, snapshots without RAM, importing disks from a running guest, and replications normally issue a guest-fsfreeze-freeze and a respective thaw command when the QEMU Guest agent option is enabled in the guest’s configuration and the agent is running inside of the guest.

The deprecated *freeze-fs-on-backup* setting is treated as an alias for this setting.

**`fstrim_cloned_disks`\=`<boolean>` (*default \=* `0`)**

Run fstrim after moving a disk or migrating the VM.

**`type`\=`<isa | virtio>` (*default \=* `virtio`)**

Select the agent type

**`allow-ksm`: `<boolean>` (*default \=* `1`)**

Allow memory pages of this guest to be merged via KSM (Kernel Samepage Merging).

**`amd-sev`: `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

Secure Encrypted Virtualization (SEV) features by AMD CPUs

**`allow-smt`\=`<boolean>` (*default \=* `1`)**

Sets policy bit to allow Simultaneous Multi Threading (SMT) (Ignored unless for SEV-SNP)

**`kernel-hashes`\=`<boolean>` (*default \=* `0`)**

Add kernel hashes to guest firmware for measured linux kernel launch

**`no-debug`\=`<boolean>` (*default \=* `0`)**

Sets policy bit to disallow debugging of guest

**`no-key-sharing`\=`<boolean>` (*default \=* `0`)**

Sets policy bit to disallow key sharing with other guests (Ignored for SEV-SNP)

**`type`\=`<sev-type>`**

Enable standard SEV with type\=*std* or enable experimental SEV-ES with the *es* option or enable experimental SEV-SNP with the *snp* option.

**`arch`: `<aarch64 | x86_64>`**

Virtual processor architecture. Defaults to the host architecture.

**`args`: `<string>`**

Arbitrary arguments passed to kvm, for example:

args: -no-reboot -smbios *type\=0,vendor\=FOO*

{% hint style="info" %}
this option is for experts only.
{% endhint %}

**`audio0`: `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

Configure a audio device, useful in combination with QXL/Spice.

**`device`\=`<AC97 | ich9-intel-hda | intel-hda>`**

Configure an audio device.

**`driver`\=`<none | spice>` (*default \=* `spice`)**

Driver backend for the audio device.

**`autostart`: `<boolean>` (*default \=* `0`)**

Automatic restart after crash (currently ignored).

**`balloon`: `<integer> (0 - N)`**

Amount of target RAM for the VM in MiB. The balloon driver is enabled by default, unless it is explicitly disabled by setting the value to zero.

**`bios`: `<ovmf | seabios>` (*default \=* `seabios`)**

Select BIOS implementation.

**`boot`: `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

Specify guest boot order. Use the *order\=* sub-property as usage with no key or *legacy\=* is deprecated.

**`legacy`\=`<[acdn]{1,4}>` (*default \=* `cdn`)**

Boot on floppy (a), hard disk (c), CD-ROM (d), or network (n). Deprecated, use *order\=* instead.

**`order`\=`<device[;device...]>`**

The guest will attempt to boot from devices in the order they appear here.

Disks, optical drives and passed-through storage USB devices will be directly booted from, NICs will load PXE, and PCIe devices will either behave like disks (e.g. NVMe) or load an option ROM (e.g. RAID controller, hardware NIC).

Note that only devices in this list will be marked as bootable and thus loaded by the guest firmware (BIOS/UEFI). If you require multiple disks for booting (e.g. software-raid), you need to specify all of them here.

Overrides the deprecated *legacy\=\[acdn\]\** value when given.

**`bootdisk`: `(ide|sata|scsi|virtio)\d+`**

Enable booting from specified disk. Deprecated: Use *boot: order\=foo;bar* instead.

**`cdrom`: `<volume>`**

This is an alias for option -ide2

**`cicustom`: `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init: Specify custom files to replace the automatically generated ones at start.

**`meta`\=`<volume>`**

Specify a custom file containing all meta data passed to the VM via cloud-init. This is provider specific meaning configdrive2 and nocloud differ.

**`network`\=`<volume>`**

To pass a custom file containing all network data to the VM via cloud-init.

**`user`\=`<volume>`**

To pass a custom file containing all user data to the VM via cloud-init.

**`vendor`\=`<volume>`**

To pass a custom file containing all vendor data to the VM via cloud-init.

**`cipassword`: `<string>`**

cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords.

**`citype`: `<configdrive2 | nocloud | opennebula>`**

Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows.

**`ciupgrade`: `<boolean>` (*default \=* `1`)**

cloud-init: do an automatic package upgrade after the first boot.

**`ciuser`: `<string>`**

cloud-init: User name to change ssh keys and password for instead of the image’s configured default user.

**`cores`: `<integer> (1 - N)` (*default \=* `1`)**

The number of cores per socket.

**`cpu`: `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

Emulated CPU type.

**`cputype`\=`<string>` (*default \=* `kvm64`)**

Emulated CPU type. Can be default or custom name (custom model names must be prefixed with *custom-*).

**`flags`\=`<+FLAG[;-FLAG...]>`**

以 *;* 分隔的附加 CPU 标志列表。使用 *\+FLAG* 启用标志，使用 *-FLAG* 禁用标志。有一个特殊的 *nested-virt* 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 使用 *svm*，Intel 使用 *vmx*）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，VM 特定标志必须来自以下集合：aes、amd-no-ssb、amd-ssbd、hv-evmcs、hv-tlbflush、ibpb、md-clear、nested-virt、pcid、pdpe1gb、spec-ctrl、ssbd、virt-ssbd

**`guest-phys-bits`\=`<integer> (32 - 64)`**

客户机可用的物理地址位数。

**`hidden`\=`<boolean>` (*default \=* `0`)**

不要标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。

**`hv-vendor-id`\=`<vendor-id>`**

Hyper-V 供应商 ID。Windows 客户机中的某些驱动程序或程序需要特定的 ID。

**`level`\=`<integer> (0 - 4294967295)`**

客户机可查询的基本 CPUID 叶的最大输入值——即供应商（叶 0）、系列/型号/步进及功能位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶将被隐藏。将此项设置为 *30*，是解决在较新的 Intel 宿主机上运行的 Windows 客户机出现 Hyper-V 启动故障的常用变通方法。仅当 vCPU 架构为 x86\_64 时适用。

**`phys-bits`\=`<8-64|host>`**

报告给客户机操作系统的物理内存地址位数。应小于或等于宿主机的位数。设置为 *host* 可使用宿主机 CPU 的值，但请注意，这样会导致无法在线迁移到该值不同的 CPU。

**`reported-model`\=`<486 | Broadwell | Broadwell-IBRS | Broadwell-noTSX | Broadwell-noTSX-IBRS | Cascadelake-Server | Cascadelake-Server-noTSX | Cascadelake-Server-v2 | Cascadelake-Server-v4 | Cascadelake-Server-v5 | ClearwaterForest | ClearwaterForest-v2 | ClearwaterForest-v3 | Conroe | Cooperlake | Cooperlake-v2 | DiamondRapids | EPYC | EPYC-Genoa | EPYC-Genoa-v2 | EPYC-IBPB | EPYC-Milan | EPYC-Milan-v2 | EPYC-Milan-v3 | EPYC-Rome | EPYC-Rome-v2 | EPYC-Rome-v3 | EPYC-Rome-v4 | EPYC-Rome-v5 | EPYC-Turin | EPYC-v3 | EPYC-v4 | EPYC-v5 | GraniteRapids | GraniteRapids-v2 | GraniteRapids-v3 | GraniteRapids-v4 | GraniteRapids-v5 | Haswell | Haswell-IBRS | Haswell-noTSX | Haswell-noTSX-IBRS | Icelake-Client | Icelake-Client-noTSX | Icelake-Server | Icelake-Server-noTSX | Icelake-Server-v3 | Icelake-Server-v4 | Icelake-Server-v5 | Icelake-Server-v6 | Icelake-Server-v7 | IvyBridge | IvyBridge-IBRS | KnightsMill | Nehalem | Nehalem-IBRS | Opteron_G1 | Opteron_G2 | Opteron_G3 | Opteron_G4 | Opteron_G5 | Penryn | SandyBridge | SandyBridge-IBRS | SapphireRapids | SapphireRapids-v2 | SapphireRapids-v3 | SapphireRapids-v4 | SapphireRapids-v5 | SapphireRapids-v6 | SierraForest | SierraForest-v2 | SierraForest-v3 | SierraForest-v4 | SierraForest-v5 | Skylake-Client | Skylake-Client-IBRS | Skylake-Client-noTSX-IBRS | Skylake-Client-v4 | Skylake-Server | Skylake-Server-IBRS | Skylake-Server-noTSX-IBRS | Skylake-Server-v4 | Skylake-Server-v5 | Westmere | Westmere-IBRS | a64fx | athlon | core2duo | coreduo | cortex-a35 | cortex-a53 | cortex-a55 | cortex-a57 | cortex-a710 | cortex-a72 | cortex-a76 | cortex-a78ae | host | kvm32 | kvm64 | max | neoverse-n1 | neoverse-n2 | neoverse-v1 | pentium | pentium2 | pentium3 | phenom | qemu32 | qemu64>` (*default \=* `kvm64`)**

报告给客户机的 CPU 模型和供应商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效；默认模型始终会向客户机操作系统报告其自身。

**`cpulimit`: `<number> (0 - 128)` (*default \=* `0`)**

CPU 使用限制。

{% hint style="info" %}
If the computer has 2 CPUs, it has total of *2* CPU time. Value *0* indicates no CPU limit.
{% endhint %}

**`cpuunits`: `<integer> (1 - 262144)` (*default \=* `cgroup v1: 1024, cgroup v2: 100`)**

CPU weight for a VM. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this VM gets. Number is relative to weights of all the other running VMs.

**`description`: `<string>`**

Description for the VM. Shown in the web-interface VM’s summary. This is saved as comment inside the configuration file.

**`efidisk0`: `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

Configure a disk for storing EFI vars.

**`efitype`\=`<2m | 4m>` (*default \=* `2m`)**

Size and type of the OVMF EFI vars. *4m* is newer and recommended, and required for Secure Boot. For backwards compatibility, *2m* is used if not otherwise specified. Ignored for VMs with arch\=aarch64 (ARM).

**`file`\=`<volume>`**

The drive’s backing volume.

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`ms-cert`\=`<2011 | 2023 | 2023k | 2023w>` (*default \=* `2011`)**

Informational marker indicating the version of the latest Microsoft UEFI certificates that have been enrolled by Proxmox VE. The value *2023k* means that the *Microsoft UEFI CA 2023*, the *Windows UEFI CA 2023* and the *Microsoft Corporation KEK 2K CA 2023* certificates are included. The values *2023* and *2023w* are deprecated and for compatibility only.

**`pre-enrolled-keys`\=`<boolean>` (*default \=* `0`)**

Use am EFI vars template with distribution-specific and Microsoft Standard keys enrolled, if used with *efitype\=4m*. Note that this will enable Secure Boot by default, though it can still be turned off from within the VM.

**`size`\=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`freeze`: `<boolean>`**

Freeze CPU at startup (use *c* monitor command to start execution).

**`hookscript`: `<string>`**

Script that will be executed during various steps in the vms lifetime.

**`hostpci[n]`: `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

Map host PCI devices into guest.

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

{% hint style="danger" %}
Experimental! User reported problems with this option.
{% endhint %}

**`device-id`\=`<hex id>`**

Override PCI device ID visible to guest

**`driver`\=`<keep | vfio>` (*default \=* `vfio`)**

If set to *keep* the device will neither be reset nor bound to the *vfio-pci* driver. Useful for devices that already have the correct driver loaded.

**`host`\=`<HOSTPCIID[;HOSTPCIID2...]>`**

Host PCI device pass through. The PCI ID of a host’s PCI device or a list of PCI virtual functions of the host. HOSTPCIID syntax is:

*bus:dev.func* (hexadecimal numbers)

You can use the *lspci* command to list existing PCI devices.

Either this or the *mapping* key must be set.

**`legacy-igd`\=`<boolean>` (*default \=* `0`)**

Pass this device in legacy IGD mode, making it the primary and exclusive graphics device in the VM. Requires *pc-i440fx* machine type and VGA set to *none*.

**`mapping`\=`<mapping-id>`**

The ID of a cluster wide mapping. Either this or the default-key *host* must be set.

**`mdev`\=`<string>`**

The type of mediated device to use. An instance of this type will be created on startup of the VM and will be cleaned up when the VM stops.

**`pcie`\=`<boolean>` (*default \=* `0`)**

Choose the PCI-express bus (needs the *q35* machine model).

**`rombar`\=`<boolean>` (*default \=* `1`)**

Specify whether or not the device’s ROM will be visible in the guest’s memory map.

**`romfile`\=`<string>`**

Custom pci device rom filename (must be located in /usr/share/kvm/).

**`sub-device-id`\=`<hex id>`**

Override PCI subsystem device ID visible to guest

**`sub-vendor-id`\=`<hex id>`**

Override PCI subsystem vendor ID visible to guest

**`vendor-id`\=`<hex id>`**

Override PCI vendor ID visible to guest

**`x-vga`\=`<boolean>` (*default \=* `0`)**

Enable vfio-vga device support.

**`hotplug`: `<string>` (*default \=* `network,disk,usb`)**

Selectively enable hotplug features. This is a comma separated list of hotplug features: *network*, *disk*, *cpu*, *memory*, *usb* and *cloudinit*. Use *0* to disable hotplug completely. Using *1* as value is an alias for the default `network,disk,usb`. USB hotplugging is possible for guests with machine version \>\= 7.1 and ostype l26 or windows \> 7\.

**`hugepages`: `<1024 | 2 | any>`**

Enables hugepages memory.

Sets the size of hugepages in MiB. If the value is set to *any* then 1 GiB hugepages will be used if possible, otherwise the size will fall back to 2 MiB.

**`ide[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as IDE hard disk or CD-ROM (n is 0 to 3).

**`aio`\=`<io_uring | native | threads>`**

AIO type to use.

**`backup`\=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`\=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`\=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`\=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`\=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`\=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`\=`<volume>`**

The drive’s backing volume.

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`\=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`\=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`\=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`\=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`\=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`\=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`mbps`\=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`\=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`\=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`\=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`\=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`\=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`\=`<cdrom | disk>` (*default \=* `disk`)**

The drive’s media type.

**`model`\=`<model>`**

The drive’s reported model name, url-encoded, up to 40 bytes long.

**`replicate`\=`<boolean>` (*default \=* `1`)**

Whether the drive should considered for replication jobs.

**`rerror`\=`<ignore | report | stop>`**

Read error action.

**`serial`\=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`\=`<boolean>` (*default \=* `0`)**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`\=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`\=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`ssd`\=`<boolean>`**

Whether to expose this drive as an SSD, rather than a rotational hard disk.

**`werror`\=`<enospc | ignore | report | stop>`**

Write error action.

**`wwn`\=`<wwn>`**

The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by *0x*.

**`intel-tdx`: `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Trusted Domain Extension (TDX) features by Intel CPUs

**`attestation`\=`<boolean>` (*default \=* `1`)**

Enable TDX attestation by including quote-generation-socket

**`type`\=`<tdx-type>`**

Enable TDX

**`vsock-cid`\=`<integer> (2 - N)` (*default \=* `2`)**

CID for vsock of Quote Generation Service

**`vsock-port`\=`<integer> (0 - N)` (*default \=* `4050`)**

Port for vsock of Quote Generation Service

**`ipconfig[n]`: `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string *dhcp* can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string *auto* can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4.

**`gw`\=`<GatewayIPv4>`**

IPv4 流量的默认网关。

{% hint style="info" %}
Requires option(s): `ip`
{% endhint %}

**`gw6`\=`<GatewayIPv6>`**

IPv6 流量的默认网关。

{% hint style="info" %}
Requires option(s): `ip6`
{% endhint %}

**`ip`\=`<IPv4Format/CIDR>` (*default \=* `dhcp`)**

CIDR 格式的 IPv4 地址。

**`ip6`\=`<IPv6Format/CIDR>` (*default \=* `dhcp`)**

CIDR 格式的 IPv6 地址。

**`ivshmem`: `size=<integer> [,name=<string>]`**

Inter-VM shared memory. Useful for direct communication between VMs, or to the host.

**`name`\=`<string>`**

The name of the file. Will be prefixed with *pve-shm-*. Default is the VMID. Will be deleted when the VM is stopped.

**`size`\=`<integer> (1 - N)`**

The size of the file in MB.

**`keephugepages`: `<boolean>` (*default \=* `0`)**

Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts.

**`keyboard`: `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

Keyboard layout for VNC server. This option is generally not required and is often better handled from within the guest OS.

**`kvm`: `<boolean>` (*default \=* `1`)**

Enable/disable KVM hardware virtualization.

**`localtime`: `<boolean>`**

Set the real time clock (RTC) to local time. This is enabled by default if the `ostype` indicates a Microsoft Windows OS.

**`lock`: `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

Lock/unlock the VM.

**`machine`: `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`aw-bits`\=`<number> (32 - 64)`**

Specifies the vIOMMU address space bit width.

Intel vIOMMU supports a bit width of either 39 or 48 bits and VirtIO vIOMMU supports any bit width between 32 and 64 bits.

**`enable-s3`\=`<boolean>`**

Enables S3 power state. Defaults to false beginning with machine types 9.2\+pve1, true before.

**`enable-s4`\=`<boolean>`**

Enables S4 power state. Defaults to false beginning with machine types 9.2\+pve1, true before.

**`type`\=`<machine type>`**

Specifies the QEMU machine type.

**`viommu`\=`<intel | virtio>`**

Enable and set guest vIOMMU variant (Intel vIOMMU needs q35 to be set as machine type).

**`memory`: `[current=]<integer>`**

Memory properties.

**`current`\=`<integer> (16 - N)` (*default \=* `512`)**

Current amount of online RAM for the VM in MiB. This is the maximum available memory when you use the balloon device.

**`migrate_downtime`: `<number> (0 - N)` (*default \=* `0.1`)**

Set maximum tolerated downtime (in seconds) for migrations. Should the migration not be able to converge in the very end, because too much newly dirtied RAM needs to be transferred, the limit will be increased automatically step-by-step until migration can converge. Will be capped to 2000 seconds (maximum in QEMU).

**`migrate_speed`: `<integer> (0 - N)` (*default \=* `0`)**

Set maximum speed (in MB/s) for migrations. Value 0 is no limit.

**`name`: `<string>`**

Set a name for the VM. Only used on the configuration web interface.

**`nameserver`: `<string>`**

cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`net[n]`: `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

Specify network devices.

**`bridge`\=`<bridge>`**

Bridge to attach the network device to. The Proxmox VE standard bridge is called *vmbr0*.

If you do not specify a bridge, we create a kvm user (NATed) network device, which provides DHCP and DNS services. The following addresses are used:

```text
10.0.2.2   Gateway
10.0.2.3   DNS Server
10.0.2.4   SMB Server
```

The DHCP server assign addresses to the guest starting from 10.0.2.15.

**`firewall`\=`<boolean>`**

Whether this interface should be protected by the firewall.

**`host-tunnel`\=`<boolean>`**

Enable host GSO over UDP tunnel offload (VirtIO only). Requires QEMU \> 10.2 and guest and host kernel support. Disabled by default starting with machine version 11.0\+pve1 to work around an issue with the virtio-net driver in guest kernels. With machine versions 10.2 and 11.0, this is enabled by default.

**`link_down`\=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`macaddr`\=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`model`\=`<e1000 | e1000-82540em | e1000-82544gc | e1000-82545em | e1000e | i82551 | i82557b | i82559er | ne2k_isa | ne2k_pci | pcnet | rtl8139 | virtio | vmxnet3>`**

Network Card Model. The *virtio* model provides the best performance with very low CPU overhead. If your guest does not support this driver, it is usually best to use *e1000*.

**`mtu`\=`<integer> (1 - 65520)`**

Force MTU of network device (VirtIO only). Setting to *1* or empty will use the bridge MTU

**`queues`\=`<integer> (0 - 64)`**

Number of packet queues to be used on the device.

**`rate`\=`<number> (0 - N)`**

Rate limit in mbps (megabytes per second) as floating point number.

**`tag`\=`<integer> (1 - 4094)`**

VLAN tag to apply to packets on this interface.

**`trunks`\=`<vlanid[;vlanid...]>`**

VLAN trunks to pass through this interface.

**`numa`: `<boolean>` (*default \=* `0`)**

Enable/disable NUMA.

**`numa[n]`: `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA topology.

**`cpus`\=`<id[-id];...>`**

CPUs accessing this NUMA node.

**`hostnodes`\=`<id[-id];...>`**

Host NUMA nodes to use.

**`memory`\=`<number>`**

Amount of memory this NUMA node provides.

**`policy`\=`<bind | interleave | preferred>`**

NUMA allocation policy.

**`onboot`: `<boolean>` (*default \=* `0`)**

Specifies whether a VM will be started during system bootup.

**`ostype`: `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` (*default \=* `other`)**

Specify guest operating system. This is used to enable special optimization/features for specific operating systems:

<table>
<tr>
<td>other <br/>
</td>
<td>
<p>unspecified OS</p>
</td>
</tr>
<tr>
<td>wxp <br/>
</td>
<td>
<p>Microsoft Windows XP</p>
</td>
</tr>
<tr>
<td>
w2k
<br/>
</td>
<td>
<p>Microsoft Windows 2000</p>
</td>
</tr>
<tr>
<td>
w2k3
<br/>
</td>
<td>
<p>Microsoft Windows 2003</p>
</td>
</tr>
<tr>
<td>
w2k8
<br/>
</td>
<td>
<p>Microsoft Windows 2008</p>
</td>
</tr>
<tr>
<td>wvista <br/>
</td>
<td>
<p>Microsoft Windows Vista</p>
</td>
</tr>
<tr>
<td>win7 <br/>
</td>
<td>
<p>Microsoft Windows 7</p>
</td>
</tr>
<tr>
<td>win8 <br/>
</td>
<td>
<p>Microsoft Windows 8/2012/2012r2</p>
</td>
</tr>
<tr>
<td>win10 <br/>
</td>
<td>
<p>Microsoft Windows 10/2016/2019</p>
</td>
</tr>
<tr>
<td>win11 <br/>
</td>
<td>
<p>Microsoft Windows 11/2022/2025</p>
</td>
</tr>
<tr>
<td>
l24
<br/>
</td>
<td>
<p>Linux 2.4 Kernel</p>
</td>
</tr>
<tr>
<td>
l26
<br/>
</td>
<td>
<p>Linux 2.6 - 7.X Kernel</p>
</td>
</tr>
<tr>
<td>solaris <br/>
</td>
<td>
<p>Solaris/OpenSolaris/OpenIndiania kernel</p>
</td>
</tr>
</table>

**`parallel[n]`: `/dev/parport\d+|/dev/usb/lp\d+`**

Map host parallel devices (n is 0 to 2).

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

{% hint style="danger" %}
Experimental! User reported problems with this option.
{% endhint %}

**`protection`: `<boolean>` (*default \=* `0`)**

Sets the protection flag of the VM. This will disable the remove VM and remove disk operations.

**`reboot`: `<boolean>` (*default \=* `1`)**

Allow reboot. If set to *0* the VM exit on reboot.

**`rng0`: `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

Configure a VirtIO-based Random Number Generator.

**`max_bytes`\=`<integer>` (*default \=* `1024`)**

Maximum bytes of entropy allowed to get injected into the guest every *period* milliseconds. Use `0` to disable limiting (potentially dangerous!).

**`period`\=`<integer>` (*default \=* `1000`)**

Every *period* milliseconds the entropy-injection quota is reset, allowing the guest to retrieve another *max\_bytes* of entropy.

**`source`\=`</dev/hwrng | /dev/random | /dev/urandom>`**

The file on the host to gather entropy from. Using urandom does **not** decrease security in any meaningful way, as it’s still seeded from real entropy, and the bytes provided will most likely be mixed with real entropy on the guest as well. */dev/hwrng* can be used to pass through a hardware RNG from the host.

**`sata[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SATA hard disk or CD-ROM (n is 0 to 5).

**`aio`\=`<io_uring | native | threads>`**

AIO type to use.

**`backup`\=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`\=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`\=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`\=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`\=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`\=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`\=`<volume>`**

The drive’s backing volume.

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`\=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`\=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`\=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`\=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`\=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`\=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`mbps`\=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`\=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`\=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`\=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`\=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`\=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`\=`<cdrom | disk>` (*default \=* `disk`)**

The drive’s media type.

**`replicate`\=`<boolean>` (*default \=* `1`)**

Whether the drive should considered for replication jobs.

**`rerror`\=`<ignore | report | stop>`**

Read error action.

**`serial`\=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`\=`<boolean>` (*default \=* `0`)**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`\=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`\=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`ssd`\=`<boolean>`**

Whether to expose this drive as an SSD, rather than a rotational hard disk.

**`werror`\=`<enospc | ignore | report | stop>`**

Write error action.

**`wwn`\=`<wwn>`**

The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by *0x*.

**`scsi[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SCSI hard disk or CD-ROM (n is 0 to 30).

**`aio`\=`<io_uring | native | threads>`**

AIO type to use.

**`backup`\=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`\=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`\=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`\=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`\=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`\=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`\=`<volume>`**

The drive’s backing volume.

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`\=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`\=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`\=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`\=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`\=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`\=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`iothread`\=`<boolean>`**

Whether to use iothreads for this drive

**`mbps`\=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`\=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`\=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`\=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`\=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`\=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`\=`<cdrom | disk>` (*default \=* `disk`)**

The drive’s media type.

**`product`\=`<product>`**

The drive’s product name, up to 16 bytes long.

**`queues`\=`<integer> (2 - N)`**

Number of queues.

**`replicate`\=`<boolean>` (*default \=* `1`)**

Whether the drive should considered for replication jobs.

**`rerror`\=`<ignore | report | stop>`**

Read error action.

**`ro`\=`<boolean>`**

Whether the drive is read-only.

**`scsiblock`\=`<boolean>` (*default \=* `0`)**

whether to use scsi-block for full passthrough of host block device

{% hint style="warning" %}
can lead to I/O errors in combination with low memory or high memory fragmentation on host
{% endhint %}

**`serial`\=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`\=`<boolean>` (*default \=* `0`)**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`\=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`\=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`ssd`\=`<boolean>`**

Whether to expose this drive as an SSD, rather than a rotational hard disk.

**`vendor`\=`<vendor>`**

The drive’s vendor name, up to 8 bytes long.

**`werror`\=`<enospc | ignore | report | stop>`**

Write error action.

**`wwn`\=`<wwn>`**

The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by *0x*.

**`scsihw`: `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` (*default \=* `lsi`)**

SCSI controller model

**`searchdomain`: `<string>`**

cloud-init: Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`serial[n]`: `(/dev/[^,]+|socket)`**

Create a serial device inside the VM (n is 0 to 3), and pass through a host serial device (i.e. /dev/ttyS0), or create a unix socket on the host side (use *qm terminal* to open a terminal connection).

{% hint style="info" %}
If you pass through a host serial device, it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

{% hint style="danger" %}
Experimental! User reported problems with this option.
{% endhint %}

**`shares`: `<integer> (0 - 50000)` (*default \=* `1000`)**

Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd.

**`smbios1`: `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

Specify SMBIOS type 1 fields.

**`base64`\=`<boolean>`**

Flag to indicate that the SMBIOS values are base64 encoded

**`family`\=`<Base64 encoded string>`**

Set SMBIOS1 family string.

**`manufacturer`\=`<Base64 encoded string>`**

Set SMBIOS1 manufacturer.

**`product`\=`<Base64 encoded string>`**

Set SMBIOS1 product ID.

**`serial`\=`<Base64 encoded string>`**

Set SMBIOS1 serial number.

**`sku`\=`<Base64 encoded string>`**

Set SMBIOS1 SKU string.

**`uuid`\=`<UUID>`**

Set SMBIOS1 UUID.

**`version`\=`<Base64 encoded string>`**

Set SMBIOS1 version.

**`smp`: `<integer> (1 - N)` (*default \=* `1`)**

The number of CPUs. Please use option -sockets instead.

**`sockets`: `<integer> (1 - N)` (*default \=* `1`)**

The number of CPU sockets.

**`spice_enhancements`: `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

Configure additional enhancements for SPICE.

**`foldersharing`\=`<boolean>` (*default \=* `0`)**

Enable folder sharing via SPICE. Needs Spice-WebDAV daemon installed in the VM.

**`videostreaming`\=`<all | filter | off>` (*default \=* `off`)**

Enable video streaming. Uses compression for detected video streams.

**`sshkeys`: `<string>`**

cloud-init: Setup public SSH keys (one key per line, OpenSSH format).

**`startdate`: `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` (*default \=* `now`)**

Set the initial date of the real time clock. Valid format for date are:'now' or *2006-06-17T16:01:21* or *2006-06-17*.

**`startup`: \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`tablet`: `<boolean>` (*default \=* `1`)**

Enable/disable the USB tablet device. This device is usually needed to allow absolute mouse positioning with VNC. Else the mouse runs out of sync with normal VNC clients. If you’re running lots of console-only guests on one host, you may consider disabling this to save some context switches. This is turned off by default if you use spice (`qm set <vmid> --vga qxl`).

**`tags`: `<string>`**

Tags of the VM. This is only meta information.

**`tdf`: `<boolean>` (*default \=* `0`)**

Enable/disable time drift fix.

**`template`: `<boolean>` (*default \=* `0`)**

启用/禁用模板。

**`tpmstate0`: `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

Configure a Disk for storing TPM state. The format is fixed to *raw*.

**`file`\=`<volume>`**

The drive’s backing volume.

**`format`\=`<qcow2 | raw | vmdk>`**

Format of the image.

**`size`\=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`version`\=`<v1.2 | v2.0>` (*default \=* `v1.2`)**

The TPM interface version. v2.0 is newer and should be preferred. Note that this cannot be changed later on.

**`unused[n]`: `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`file`\=`<volume>`**

The drive’s backing volume.

**`usb[n]`: `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

Configure an USB device (n is 0 to 4, for machine version \>\= 7.1 and ostype l26 or windows \> 7, n can be up to 14).

**`host`\=`<HOSTUSBDEVICE|spice>`**

The Host USB device or port or the value *spice*. HOSTUSBDEVICE syntax is:

```text
'bus-port(.port)*' (decimal numbers) or
'vendor_id:product_id' (hexadecimal numbers) or
'spice'
```

You can use the *lsusb -t* command to list existing usb devices.

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines \- use with special care.
{% endhint %}

The value *spice* can be used to add a usb redirection devices for spice.

Either this or the *mapping* key must be set.

**`mapping`\=`<mapping-id>`**

The ID of a cluster wide mapping. Either this or the default-key *host* must be set.

**`usb3`\=`<boolean>` (*default \=* `0`)**

Specifies whether if given host option is a USB3 device or port. For modern guests (machine version \>\= 7.1 and ostype l26 and windows \> 7), this flag is irrelevant (all devices are plugged into a xhci controller).

**`vcpus`: `<integer> (1 - N)` (*default \=* `0`)**

Number of hotplugged vcpus.

**`vga`: `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

Configure the VGA Hardware. If you want to use high resolution modes (\>\= 1280x1024x16) you may need to increase the vga memory option. Since QEMU 2.9 the default VGA display type is *std* for all OS types besides some Windows versions (XP and older) which use *cirrus*. The *qxl* option enables the SPICE display server. For win\* OS you can select how many independent displays you want, Linux guests can add displays them self. You can also run without any graphic card, using a serial device as terminal.

**`clipboard`\=`<vnc>`**

Enable a specific clipboard. If not set, depending on the display type the SPICE one will be added. Live migration with a VNC clipboard is not possible with QEMU machine version \< 10.1.

**`memory`\=`<integer> (4 - 512)`**

Sets the VGA memory (in MiB). Has no effect with serial display.

**`type`\=`<cirrus | none | qxl | qxl2 | qxl3 | qxl4 | serial0 | serial1 | serial2 | serial3 | std | virtio | virtio-gl | vmware>` (*default \=* `std`)**

Select the VGA type. Using type *cirrus* is not recommended.

**`virtio[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

Use volume as VIRTIO hard disk (n is 0 to 15).

**`aio`\=`<io_uring | native | threads>`**

AIO type to use.

**`backup`\=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`\=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`\=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`\=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`\=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`\=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`\=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`\=`<volume>`**

The drive’s backing volume.

**`format`\=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`\=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`\=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`\=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`\=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`\=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`\=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`\=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`\=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`\=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`iothread`\=`<boolean>`**

Whether to use iothreads for this drive

**`mbps`\=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`\=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`\=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`\=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`\=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`\=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`\=`<cdrom | disk>` (*default \=* `disk`)**

The drive’s media type.

**`replicate`\=`<boolean>` (*default \=* `1`)**

Whether the drive should considered for replication jobs.

**`rerror`\=`<ignore | report | stop>`**

Read error action.

**`ro`\=`<boolean>`**

Whether the drive is read-only.

**`serial`\=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`\=`<boolean>` (*default \=* `0`)**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`\=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`\=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`werror`\=`<enospc | ignore | report | stop>`**

Write error action.

**`virtiofs[n]`: `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

Configuration for sharing a directory between host and guest using Virtio-fs.

**`cache`\=`<always | auto | metadata | never>` (*default \=* `auto`)**

The caching policy the file system should use (auto, always, metadata, never).

**`direct-io`\=`<boolean>` (*default \=* `0`)**

Honor the O\_DIRECT flag passed down by guest applications.

**`dirid`\=`<mapping-id>`**

Mapping identifier of the directory mapping to be shared with the guest. Also used as a mount tag inside the VM.

**`expose-acl`\=`<boolean>` (*default \=* `0`)**

Enable support for POSIX ACLs (enabled ACL implies xattr) for this mount.

**`expose-xattr`\=`<boolean>` (*default \=* `0`)**

Enable support for extended attributes for this mount.

**`vmgenid`: `<UUID>` (*default \=* `1 (autogenerated)`)**

The VM generation ID (vmgenid) device exposes a 128-bit integer value identifier to the guest OS. This allows to notify the guest operating system when the virtual machine is executed with a different configuration (e.g. snapshot execution or creation from a template). The guest operating system notices the change, and is then able to react as appropriate by marking its copies of distributed databases as dirty, re-initializing its random number generator, etc. Note that auto-creation only works when done through API/CLI create or update methods, but not when manually editing the config file.

**`vmstatestorage`: `<storage ID>`**

Default storage for VM state volumes/files.

**`watchdog`: `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the watchdog will reset the guest (or execute the respective action specified)

**`action`\=`<debug | none | pause | poweroff | reset | shutdown>`**

The action to perform if after activation the guest fails to poll the watchdog in time.

**`model`\=`<i6300esb | ib700>` (*default \=* `i6300esb`)**

Watchdog type to emulate.

## Locks <a href="#_locks" id="_locks"></a>

Online migrations, snapshots and backups (`vzdump`) set a lock to prevent incompatible concurrent actions on the affected VMs. Sometimes you need to remove such a lock manually (for example after a power failure).

```text
# qm unlock <vmid>
```

{% hint style="danger" %}
Only do that if you are sure the action which set the lock is no longer running.
{% endhint %}

## Files <a href="#_files" id="_files"></a>

**`/etc/pve/qemu-server/<VMID>.conf`**

Configuration file for the VM *\<VMID\>*.

## Copyright and Disclaimer <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

## 注释

### 注释 1 <a href="#note-0cdd31f9-1" id="note-0cdd31f9-1"></a>

请参阅 KVM wiki 上的此基准测试 [https://www.linux-kvm.org/page/Using\_VirtIO\_NIC](https://www.linux-kvm.org/page/Using_VirtIO_NIC)

### 注释 2 <a href="#note-0cdd31f9-2" id="note-0cdd31f9-2"></a>

See this benchmark for details [https://events.static.linuxfound.org/sites/events/files/slides/CloudOpen2013\_Khoa\_Huynh\_v3.pdf](https://events.static.linuxfound.org/sites/events/files/slides/CloudOpen2013_Khoa_Huynh_v3.pdf)

### 注释 3 <a href="#note-0cdd31f9-3" id="note-0cdd31f9-3"></a>

TRIM, UNMAP, and discard [https://en.wikipedia.org/wiki/Trim\_%28computing%29](https://en.wikipedia.org/wiki/Trim_%28computing%29)

### 注释 4 <a href="#note-0cdd31f9-4" id="note-0cdd31f9-4"></a>

Meltdown 攻击 [https://meltdownattack.com/](https://meltdownattack.com/)

### 注释 5 <a href="#note-0cdd31f9-5" id="note-0cdd31f9-5"></a>

spectre-meltdown-checker [https://meltdown.ovh/](https://meltdown.ovh/)

### 注释 6 <a href="#note-0cdd31f9-6" id="note-0cdd31f9-6"></a>

PCID 现已成为 x86 上一项关键的性能/安全功能 [https://groups.google.com/forum/m/#!topic/mechanical-sympathy/L9mHTbeQLNU](https://groups.google.com/forum/m/#!topic/mechanical-sympathy/L9mHTbeQLNU)

### 注释 7 <a href="#note-0cdd31f9-7" id="note-0cdd31f9-7"></a>

[https://en.wikipedia.org/wiki/Non-uniform\_memory\_access](https://en.wikipedia.org/wiki/Non-uniform_memory_access)

### 注释 8 <a href="#note-0cdd31f9-8" id="note-0cdd31f9-8"></a>

if the command `numactl --hardware | grep available` returns more than one node, then your host system has a NUMA architecture

### 注释 9 <a href="#note-0cdd31f9-9" id="note-0cdd31f9-9"></a>

可以在此处找到对气球驱动程序内部工作原理的详细说明 [https://rwmj.wordpress.com/2010/07/17/virtio-balloon/](https://rwmj.wordpress.com/2010/07/17/virtio-balloon/)

### 注释 10 <a href="#note-0cdd31f9-10" id="note-0cdd31f9-10"></a>

[https://www.kraxel.org/blog/2014/10/qemu-using-cirrus-considered-harmful/](https://www.kraxel.org/blog/2014/10/qemu-using-cirrus-considered-harmful/) qemu: using cirrus considered harmful

### 注释 11 <a href="#note-0cdd31f9-11" id="note-0cdd31f9-11"></a>

See the OVMF Project [https://github.com/tianocore/tianocore.github.io/wiki/OVMF](https://github.com/tianocore/tianocore.github.io/wiki/OVMF)

### 注释 12 <a href="#note-0cdd31f9-12" id="note-0cdd31f9-12"></a>

Alex Williamson has a good blog entry about this [https://vfio.blogspot.co.at/2014/08/primary-graphics-assignment-without-vga.html](https://vfio.blogspot.co.at/2014/08/primary-graphics-assignment-without-vga.html)

### 注释 13 <a href="#note-0cdd31f9-13" id="note-0cdd31f9-13"></a>

Microsoft support article about the issue [https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e](https://support.microsoft.com/en-us/topic/windows-secure-boot-certificate-expiration-and-ca-updates-7ff40d33-95dc-4c3c-8725-a9b95457578e)

### 注释 14 <a href="#note-0cdd31f9-14" id="note-0cdd31f9-14"></a>

Looking Glass: [https://looking-glass.io/](https://looking-glass.io/)

### 注释 15 <a href="#note-0cdd31f9-15" id="note-0cdd31f9-15"></a>

Official *vmgenid* Specification [https://docs.microsoft.com/en-us/windows/desktop/hyperv\_v2/virtual-machine-generation-identifier](https://docs.microsoft.com/en-us/windows/desktop/hyperv_v2/virtual-machine-generation-identifier)

### 注释 16 <a href="#note-0cdd31f9-16" id="note-0cdd31f9-16"></a>

Online GUID generator [http://guid.one/](http://guid.one/)

### 注释 17 <a href="#note-0cdd31f9-17" id="note-0cdd31f9-17"></a>

[https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/virtualized-domain-controller-architecture)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/qm.1.html) · 版本 9.2.13 · 非官方中文翻译。
