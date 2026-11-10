# 10.14. Configuration <a href="#qm_configuration" id="qm_configuration"></a>

VM configuration files are stored inside the Proxmox cluster file system, and can be accessed at `/etc/pve/qemu-server/<VMID>.conf`. Like other files stored inside `/etc/pve/`, they get automatically replicated to all other cluster nodes.

{% hint style="info" %}
VMIDs < 100 are reserved for internal purposes, and VMIDs need to be unique cluster wide.
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

## 10.14.1. File Format <a href="#_file_format" id="_file_format"></a>

VM configuration files use a simple colon separated key/value format. Each line has the following format:

```text
# this is a comment
OPTION: value
```

Blank lines in those files are ignored, and lines starting with a `#` character are treated as comments and are also ignored.

## 10.14.2. Snapshots <a href="#qm_snapshots" id="qm_snapshots"></a>

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

You can optionally save the memory of a running VM with the option `vmstate`. For details about how the target storage gets chosen for the VM state, see [State storage selection](11-qm-hibernate.md#qm_vmstatestorage) in the chapter [Hibernation](11-qm-hibernate.md#qm_hibernate).

## 10.14.3. Options <a href="#qm_options" id="qm_options"></a>

**`acpi`: `<boolean>` (*default =* `1`)**

Enable/disable ACPI.

**`affinity`: `<string>`**

List of host cores used to execute guest processes, for example: 0,5,8-11

**`agent`: `[enabled=]<1|0> [,freeze-fs=<1|0>] [,fstrim_cloned_disks=<1|0>] [,type=<virtio|isa>]`**

Enable/disable communication with the QEMU Guest Agent and its properties.

**`enabled`=`<boolean>` (*default =* `0`)**

Enable/disable communication with a QEMU Guest Agent (QGA) running in the VM.

**`freeze-fs`=`<boolean>` (*default =* `1`)**

Whether to issue the guest-fsfreeze-freeze and guest-fsfreeze-thaw QEMU guest agent commands. Backups in snapshot mode, clones, snapshots without RAM, importing disks from a running guest, and replications normally issue a guest-fsfreeze-freeze and a respective thaw command when the QEMU Guest agent option is enabled in the guest’s configuration and the agent is running inside of the guest.

The deprecated *freeze-fs-on-backup* setting is treated as an alias for this setting.

**`fstrim_cloned_disks`=`<boolean>` (*default =* `0`)**

Run fstrim after moving a disk or migrating the VM.

**`type`=`<isa | virtio>` (*default =* `virtio`)**

Select the agent type

**`allow-ksm`: `<boolean>` (*default =* `1`)**

Allow memory pages of this guest to be merged via KSM (Kernel Samepage Merging).

**`amd-sev`: `[type=]<sev-type> [,allow-smt=<1|0>] [,kernel-hashes=<1|0>] [,no-debug=<1|0>] [,no-key-sharing=<1|0>]`**

Secure Encrypted Virtualization (SEV) features by AMD CPUs

**`allow-smt`=`<boolean>` (*default =* `1`)**

Sets policy bit to allow Simultaneous Multi Threading (SMT) (Ignored unless for SEV-SNP)

**`kernel-hashes`=`<boolean>` (*default =* `0`)**

Add kernel hashes to guest firmware for measured linux kernel launch

**`no-debug`=`<boolean>` (*default =* `0`)**

Sets policy bit to disallow debugging of guest

**`no-key-sharing`=`<boolean>` (*default =* `0`)**

Sets policy bit to disallow key sharing with other guests (Ignored for SEV-SNP)

**`type`=`<sev-type>`**

Enable standard SEV with type=*std* or enable experimental SEV-ES with the *es* option or enable experimental SEV-SNP with the *snp* option.

**`arch`: `<aarch64 | x86_64>`**

Virtual processor architecture. Defaults to the host architecture.

**`args`: `<string>`**

Arbitrary arguments passed to kvm, for example:

args: -no-reboot -smbios *type=0,vendor=FOO*

{% hint style="info" %}
this option is for experts only.
{% endhint %}

**`audio0`: `device=<ich9-intel-hda|intel-hda|AC97> [,driver=<spice|none>]`**

Configure a audio device, useful in combination with QXL/Spice.

**`device`=`<AC97 | ich9-intel-hda | intel-hda>`**

Configure an audio device.

**`driver`=`<none | spice>` (*default =* `spice`)**

Driver backend for the audio device.

**`autostart`: `<boolean>` (*default =* `0`)**

Automatic restart after crash (currently ignored).

**`balloon`: `<integer> (0 - N)`**

Amount of target RAM for the VM in MiB. The balloon driver is enabled by default, unless it is explicitly disabled by setting the value to zero.

**`bios`: `<ovmf | seabios>` (*default =* `seabios`)**

Select BIOS implementation.

**`boot`: `[[legacy=]<[acdn]{1,4}>] [,order=<device[;device...]>]`**

Specify guest boot order. Use the *order=* sub-property as usage with no key or *legacy=* is deprecated.

**`legacy`=`<[acdn]{1,4}>` (*default =* `cdn`)**

Boot on floppy (a), hard disk (c), CD-ROM (d), or network (n). Deprecated, use *order=* instead.

**`order`=`<device[;device...]>`**

The guest will attempt to boot from devices in the order they appear here.

Disks, optical drives and passed-through storage USB devices will be directly booted from, NICs will load PXE, and PCIe devices will either behave like disks (e.g. NVMe) or load an option ROM (e.g. RAID controller, hardware NIC).

Note that only devices in this list will be marked as bootable and thus loaded by the guest firmware (BIOS/UEFI). If you require multiple disks for booting (e.g. software-raid), you need to specify all of them here.

Overrides the deprecated *legacy=[acdn]** value when given.

**`bootdisk`: `(ide|sata|scsi|virtio)\d+`**

Enable booting from specified disk. Deprecated: Use *boot: order=foo;bar* instead.

**`cdrom`: `<volume>`**

This is an alias for option -ide2

**`cicustom`: `[meta=<volume>] [,network=<volume>] [,user=<volume>] [,vendor=<volume>]`**

cloud-init: Specify custom files to replace the automatically generated ones at start.

**`meta`=`<volume>`**

Specify a custom file containing all meta data passed to the VM via cloud-init. This is provider specific meaning configdrive2 and nocloud differ.

**`network`=`<volume>`**

To pass a custom file containing all network data to the VM via cloud-init.

**`user`=`<volume>`**

To pass a custom file containing all user data to the VM via cloud-init.

**`vendor`=`<volume>`**

To pass a custom file containing all vendor data to the VM via cloud-init.

**`cipassword`: `<string>`**

cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords.

**`citype`: `<configdrive2 | nocloud | opennebula>`**

Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows.

**`ciupgrade`: `<boolean>` (*default =* `1`)**

cloud-init: do an automatic package upgrade after the first boot.

**`ciuser`: `<string>`**

cloud-init: User name to change ssh keys and password for instead of the image’s configured default user.

**`cores`: `<integer> (1 - N)` (*default =* `1`)**

The number of cores per socket.

**`cpu`: `[[cputype=]<string>] [,flags=<+FLAG[;-FLAG...]>] [,guest-phys-bits=<integer>] [,hidden=<1|0>] [,hv-vendor-id=<vendor-id>] [,level=<integer>] [,phys-bits=<8-64|host>] [,reported-model=<enum>]`**

Emulated CPU type.

**`cputype`=`<string>` (*default =* `kvm64`)**

Emulated CPU type. Can be default or custom name (custom model names must be prefixed with *custom-*).

**`flags`=`<+FLAG[;-FLAG...]>`**

以 *;* 分隔的附加 CPU 标志列表。使用 *+FLAG* 启用标志，使用 *-FLAG* 禁用标志。有一个特殊的 *nested-virt* 简写，用于控制当前 CPU 的嵌套虚拟化（AMD 使用 *svm*，Intel 使用 *vmx*）。自定义 CPU 模型可以指定 QEMU/KVM 支持的任何标志；出于安全原因，VM 特定标志必须来自以下集合：aes、amd-no-ssb、amd-ssbd、hv-evmcs、hv-tlbflush、ibpb、md-clear、nested-virt、pcid、pdpe1gb、spec-ctrl、ssbd、virt-ssbd

**`guest-phys-bits`=`<integer> (32 - 64)`**

客户机可用的物理地址位数。

**`hidden`=`<boolean>` (*default =* `0`)**

不要标识为 KVM 虚拟机。仅影响 x86-64 架构的 vCPU。

**`hv-vendor-id`=`<vendor-id>`**

Hyper-V 供应商 ID。Windows 客户机中的某些驱动程序或程序需要特定的 ID。

**`level`=`<integer> (0 - 4294967295)`**

客户机可查询的基本 CPUID 叶的最大输入值——即供应商（叶 0）、系列/型号/步进及功能位（叶 1）、缓存和拓扑信息（叶 4 和 B）等。编号更高的叶将被隐藏。将此项设置为 *30*，是解决在较新的 Intel 宿主机上运行的 Windows 客户机出现 Hyper-V 启动故障的常用变通方法。仅当 vCPU 架构为 x86_64 时适用。

**`phys-bits`=`<8-64|host>`**

报告给客户机操作系统的物理内存地址位数。应小于或等于宿主机的位数。设置为 *host* 可使用宿主机 CPU 的值，但请注意，这样会导致无法在线迁移到该值不同的 CPU。

**`reported-model`=`<486 | Broadwell | Broadwell-IBRS | Broadwell-noTSX | Broadwell-noTSX-IBRS | Cascadelake-Server | Cascadelake-Server-noTSX | Cascadelake-Server-v2 | Cascadelake-Server-v4 | Cascadelake-Server-v5 | ClearwaterForest | ClearwaterForest-v2 | ClearwaterForest-v3 | Conroe | Cooperlake | Cooperlake-v2 | DiamondRapids | EPYC | EPYC-Genoa | EPYC-Genoa-v2 | EPYC-IBPB | EPYC-Milan | EPYC-Milan-v2 | EPYC-Milan-v3 | EPYC-Rome | EPYC-Rome-v2 | EPYC-Rome-v3 | EPYC-Rome-v4 | EPYC-Rome-v5 | EPYC-Turin | EPYC-v3 | EPYC-v4 | EPYC-v5 | GraniteRapids | GraniteRapids-v2 | GraniteRapids-v3 | GraniteRapids-v4 | GraniteRapids-v5 | Haswell | Haswell-IBRS | Haswell-noTSX | Haswell-noTSX-IBRS | Icelake-Client | Icelake-Client-noTSX | Icelake-Server | Icelake-Server-noTSX | Icelake-Server-v3 | Icelake-Server-v4 | Icelake-Server-v5 | Icelake-Server-v6 | Icelake-Server-v7 | IvyBridge | IvyBridge-IBRS | KnightsMill | Nehalem | Nehalem-IBRS | Opteron_G1 | Opteron_G2 | Opteron_G3 | Opteron_G4 | Opteron_G5 | Penryn | SandyBridge | SandyBridge-IBRS | SapphireRapids | SapphireRapids-v2 | SapphireRapids-v3 | SapphireRapids-v4 | SapphireRapids-v5 | SapphireRapids-v6 | SierraForest | SierraForest-v2 | SierraForest-v3 | SierraForest-v4 | SierraForest-v5 | Skylake-Client | Skylake-Client-IBRS | Skylake-Client-noTSX-IBRS | Skylake-Client-v4 | Skylake-Server | Skylake-Server-IBRS | Skylake-Server-noTSX-IBRS | Skylake-Server-v4 | Skylake-Server-v5 | Westmere | Westmere-IBRS | a64fx | athlon | core2duo | coreduo | cortex-a35 | cortex-a53 | cortex-a55 | cortex-a57 | cortex-a710 | cortex-a72 | cortex-a76 | cortex-a78ae | host | kvm32 | kvm64 | max | neoverse-n1 | neoverse-n2 | neoverse-v1 | pentium | pentium2 | pentium3 | phenom | qemu32 | qemu64>` (*default =* `kvm64`)**

报告给客户机的 CPU 模型和供应商。必须是 QEMU/KVM 支持的模型。仅对自定义 CPU 模型定义有效；默认模型始终会向客户机操作系统报告其自身。

**`cpulimit`: `<number> (0 - 128)` (*default =* `0`)**

CPU 使用限制。

{% hint style="info" %}
If the computer has 2 CPUs, it has total of *2* CPU time. Value *0* indicates no CPU limit.
{% endhint %}

**`cpuunits`: `<integer> (1 - 262144)` (*default =* `cgroup v1: 1024, cgroup v2: 100`)**

CPU weight for a VM. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this VM gets. Number is relative to weights of all the other running VMs.

**`description`: `<string>`**

Description for the VM. Shown in the web-interface VM’s summary. This is saved as comment inside the configuration file.

**`efidisk0`: `[file=]<volume> [,efitype=<2m|4m>] [,format=<enum>] [,ms-cert=<enum>] [,pre-enrolled-keys=<1|0>] [,size=<DiskSize>]`**

Configure a disk for storing EFI vars.

**`efitype`=`<2m | 4m>` (*default =* `2m`)**

Size and type of the OVMF EFI vars. *4m* is newer and recommended, and required for Secure Boot. For backwards compatibility, *2m* is used if not otherwise specified. Ignored for VMs with arch=aarch64 (ARM).

**`file`=`<volume>`**

The drive’s backing volume.

**`format`=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`ms-cert`=`<2011 | 2023 | 2023k | 2023w>` (*default =* `2011`)**

Informational marker indicating the version of the latest Microsoft UEFI certificates that have been enrolled by Proxmox VE. The value *2023k* means that the *Microsoft UEFI CA 2023*, the *Windows UEFI CA 2023* and the *Microsoft Corporation KEK 2K CA 2023* certificates are included. The values *2023* and *2023w* are deprecated and for compatibility only.

**`pre-enrolled-keys`=`<boolean>` (*default =* `0`)**

Use am EFI vars template with distribution-specific and Microsoft Standard keys enrolled, if used with *efitype=4m*. Note that this will enable Secure Boot by default, though it can still be turned off from within the VM.

**`size`=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`freeze`: `<boolean>`**

Freeze CPU at startup (use *c* monitor command to start execution).

**`hookscript`: `<string>`**

Script that will be executed during various steps in the vms lifetime.

**`hostpci[n]`: `[[host=]<HOSTPCIID[;HOSTPCIID2...]>] [,device-id=<hex id>] [,driver=<vfio|keep>] [,legacy-igd=<1|0>] [,mapping=<mapping-id>] [,mdev=<string>] [,pcie=<1|0>] [,rombar=<1|0>] [,romfile=<string>] [,sub-device-id=<hex id>] [,sub-vendor-id=<hex id>] [,vendor-id=<hex id>] [,x-vga=<1|0>]`**

Map host PCI devices into guest.

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines - use with special care.
{% endhint %}

{% hint style="danger" %}
Experimental! User reported problems with this option.
{% endhint %}

**`device-id`=`<hex id>`**

Override PCI device ID visible to guest

**`driver`=`<keep | vfio>` (*default =* `vfio`)**

If set to *keep* the device will neither be reset nor bound to the *vfio-pci* driver. Useful for devices that already have the correct driver loaded.

**`host`=`<HOSTPCIID[;HOSTPCIID2...]>`**

Host PCI device pass through. The PCI ID of a host’s PCI device or a list of PCI virtual functions of the host. HOSTPCIID syntax is:

*bus:dev.func* (hexadecimal numbers)

You can use the *lspci* command to list existing PCI devices.

Either this or the *mapping* key must be set.

**`legacy-igd`=`<boolean>` (*default =* `0`)**

Pass this device in legacy IGD mode, making it the primary and exclusive graphics device in the VM. Requires *pc-i440fx* machine type and VGA set to *none*.

**`mapping`=`<mapping-id>`**

The ID of a cluster wide mapping. Either this or the default-key *host* must be set.

**`mdev`=`<string>`**

The type of mediated device to use. An instance of this type will be created on startup of the VM and will be cleaned up when the VM stops.

**`pcie`=`<boolean>` (*default =* `0`)**

Choose the PCI-express bus (needs the *q35* machine model).

**`rombar`=`<boolean>` (*default =* `1`)**

Specify whether or not the device’s ROM will be visible in the guest’s memory map.

**`romfile`=`<string>`**

Custom pci device rom filename (must be located in /usr/share/kvm/).

**`sub-device-id`=`<hex id>`**

Override PCI subsystem device ID visible to guest

**`sub-vendor-id`=`<hex id>`**

Override PCI subsystem vendor ID visible to guest

**`vendor-id`=`<hex id>`**

Override PCI vendor ID visible to guest

**`x-vga`=`<boolean>` (*default =* `0`)**

Enable vfio-vga device support.

**`hotplug`: `<string>` (*default =* `network,disk,usb`)**

Selectively enable hotplug features. This is a comma separated list of hotplug features: *network*, *disk*, *cpu*, *memory*, *usb* and *cloudinit*. Use *0* to disable hotplug completely. Using *1* as value is an alias for the default `network,disk,usb`. USB hotplugging is possible for guests with machine version >= 7.1 and ostype l26 or windows > 7.

**`hugepages`: `<1024 | 2 | any>`**

Enables hugepages memory.

Sets the size of hugepages in MiB. If the value is set to *any* then 1 GiB hugepages will be used if possible, otherwise the size will fall back to 2 MiB.

**`ide[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,model=<model>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as IDE hard disk or CD-ROM (n is 0 to 3).

**`aio`=`<io_uring | native | threads>`**

AIO type to use.

**`backup`=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`=`<volume>`**

The drive’s backing volume.

**`format`=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`mbps`=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`=`<cdrom | disk>` (*default =* `disk`)**

The drive’s media type.

**`model`=`<model>`**

The drive’s reported model name, url-encoded, up to 40 bytes long.

**`replicate`=`<boolean>`（*默认 =* `1`）**

Whether the drive should considered for replication jobs.

**`rerror`=`<ignore | report | stop>`**

Read error action.

**`serial`=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`=`<boolean>`（*默认 =* `0`）**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`ssd`=`<boolean>`**

Whether to expose this drive as an SSD, rather than a rotational hard disk.

**`werror`=`<enospc | ignore | report | stop>`**

Write error action.

**`wwn`=`<wwn>`**

The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by *0x*.

**`intel-tdx`: `[type=]<tdx-type> ,attestation=<1|0> [,vsock-cid=<integer>] [,vsock-port=<integer>]`**

Trusted Domain Extension (TDX) features by Intel CPUs

**`attestation`=`<boolean>` (*default =* `1`)**

Enable TDX attestation by including quote-generation-socket

**`type`=`<tdx-type>`**

Enable TDX

**`vsock-cid`=`<integer> (2 - N)` (*default =* `2`)**

CID for vsock of Quote Generation Service

**`vsock-port`=`<integer> (0 - N)` (*default =* `4050`)**

Port for vsock of Quote Generation Service

**`ipconfig[n]`: `[gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,ip=<IPv4Format/CIDR>] [,ip6=<IPv6Format/CIDR>]`**

cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string *dhcp* can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string *auto* can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4.

**`gw`=`<GatewayIPv4>`**

IPv4 流量的默认网关。

{% hint style="info" %}
Requires option(s): `ip`
{% endhint %}

**`gw6`=`<GatewayIPv6>`**

IPv6 流量的默认网关。

{% hint style="info" %}
Requires option(s): `ip6`
{% endhint %}

**`ip`=`<IPv4Format/CIDR>` (*default =* `dhcp`)**

CIDR 格式的 IPv4 地址。

**`ip6`=`<IPv6Format/CIDR>` (*default =* `dhcp`)**

CIDR 格式的 IPv6 地址。

**`ivshmem`: `size=<integer> [,name=<string>]`**

Inter-VM shared memory. Useful for direct communication between VMs, or to the host.

**`name`=`<string>`**

The name of the file. Will be prefixed with *pve-shm-*. Default is the VMID. Will be deleted when the VM is stopped.

**`size`=`<integer> (1 - N)`**

The size of the file in MB.

**`keephugepages`: `<boolean>` (*default =* `0`)**

Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts.

**`keyboard`: `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

Keyboard layout for VNC server. This option is generally not required and is often better handled from within the guest OS.

**`kvm`: `<boolean>` (*default =* `1`)**

Enable/disable KVM hardware virtualization.

**`localtime`: `<boolean>`**

Set the real time clock (RTC) to local time. This is enabled by default if the `ostype` indicates a Microsoft Windows OS.

**`lock`: `<backup | clone | create | migrate | rollback | snapshot | snapshot-delete | suspended | suspending>`**

Lock/unlock the VM.

**`machine`: `[[type=]<machine type>] [,aw-bits=<number>] [,enable-s3=<1|0>] [,enable-s4=<1|0>] [,viommu=<intel|virtio>]`**

Specify the QEMU machine.

**`aw-bits`=`<number> (32 - 64)`**

Specifies the vIOMMU address space bit width.

Intel vIOMMU supports a bit width of either 39 or 48 bits and VirtIO vIOMMU supports any bit width between 32 and 64 bits.

**`enable-s3`=`<boolean>`**

Enables S3 power state. Defaults to false beginning with machine types 9.2+pve1, true before.

**`enable-s4`=`<boolean>`**

Enables S4 power state. Defaults to false beginning with machine types 9.2+pve1, true before.

**`type`=`<machine type>`**

Specifies the QEMU machine type.

**`viommu`=`<intel | virtio>`**

Enable and set guest vIOMMU variant (Intel vIOMMU needs q35 to be set as machine type).

**`memory`: `[current=]<integer>`**

Memory properties.

**`current`=`<integer> (16 - N)` (*default =* `512`)**

Current amount of online RAM for the VM in MiB. This is the maximum available memory when you use the balloon device.

**`migrate_downtime`: `<number> (0 - N)` (*default =* `0.1`)**

Set maximum tolerated downtime (in seconds) for migrations. Should the migration not be able to converge in the very end, because too much newly dirtied RAM needs to be transferred, the limit will be increased automatically step-by-step until migration can converge. Will be capped to 2000 seconds (maximum in QEMU).

**`migrate_speed`: `<integer> (0 - N)` (*default =* `0`)**

Set maximum speed (in MB/s) for migrations. Value 0 is no limit.

**`name`: `<string>`**

Set a name for the VM. Only used on the configuration web interface.

**`nameserver`: `<string>`**

cloud-init: Sets DNS server IP address for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`net[n]`: `[model=]<enum> [,bridge=<bridge>] [,firewall=<1|0>] [,host-tunnel=<1|0>] [,link_down=<1|0>] [,macaddr=<XX:XX:XX:XX:XX:XX>] [,mtu=<integer>] [,queues=<integer>] [,rate=<number>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,<model>=<macaddr>]`**

Specify network devices.

**`bridge`=`<bridge>`**

Bridge to attach the network device to. The Proxmox VE standard bridge is called *vmbr0*.

If you do not specify a bridge, we create a kvm user (NATed) network device, which provides DHCP and DNS services. The following addresses are used:

```text
10.0.2.2   Gateway
10.0.2.3   DNS Server
10.0.2.4   SMB Server
```

The DHCP server assign addresses to the guest starting from 10.0.2.15.

**`firewall`=`<boolean>`**

Whether this interface should be protected by the firewall.

**`host-tunnel`=`<boolean>`**

Enable host GSO over UDP tunnel offload (VirtIO only). Requires QEMU > 10.2 and guest and host kernel support. Disabled by default starting with machine version 11.0+pve1 to work around an issue with the virtio-net driver in guest kernels. With machine versions 10.2 and 11.0, this is enabled by default.

**`link_down`=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`macaddr`=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`model`=`<e1000 | e1000-82540em | e1000-82544gc | e1000-82545em | e1000e | i82551 | i82557b | i82559er | ne2k_isa | ne2k_pci | pcnet | rtl8139 | virtio | vmxnet3>`**

Network Card Model. The *virtio* model provides the best performance with very low CPU overhead. If your guest does not support this driver, it is usually best to use *e1000*.

**`mtu`=`<integer> (1 - 65520)`**

Force MTU of network device (VirtIO only). Setting to *1* or empty will use the bridge MTU

**`queues`=`<integer> (0 - 64)`**

Number of packet queues to be used on the device.

**`rate`=`<number> (0 - N)`**

Rate limit in mbps (megabytes per second) as floating point number.

**`tag`=`<integer> (1 - 4094)`**

VLAN tag to apply to packets on this interface.

**`trunks`=`<vlanid[;vlanid...]>`**

VLAN trunks to pass through this interface.

**`numa`: `<boolean>` (*default =* `0`)**

Enable/disable NUMA.

**`numa[n]`: `cpus=<id[-id];...> [,hostnodes=<id[-id];...>] [,memory=<number>] [,policy=<preferred|bind|interleave>]`**

NUMA topology.

**`cpus`=`<id[-id];...>`**

CPUs accessing this NUMA node.

**`hostnodes`=`<id[-id];...>`**

Host NUMA nodes to use.

**`memory`=`<number>`**

Amount of memory this NUMA node provides.

**`policy`=`<bind | interleave | preferred>`**

NUMA allocation policy.

**`onboot`: `<boolean>` (*默认 =* `0`)**

Specifies whether a VM will be started during system bootup.

**`ostype`: `<l24 | l26 | other | solaris | w2k | w2k3 | w2k8 | win10 | win11 | win7 | win8 | wvista | wxp>` (*default =* `other`)**

Specify guest operating system. This is used to enable special optimization/features for specific operating systems:

<table>
<tr>
<td>other <br/></td>
<td>
<p>unspecified OS</p>
</td>
</tr>
<tr>
<td>wxp <br/></td>
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
<td>wvista <br/></td>
<td>
<p>Microsoft Windows Vista</p>
</td>
</tr>
<tr>
<td>win7 <br/></td>
<td>
<p>Microsoft Windows 7</p>
</td>
</tr>
<tr>
<td>win8 <br/></td>
<td>
<p>Microsoft Windows 8/2012/2012r2</p>
</td>
</tr>
<tr>
<td>win10 <br/></td>
<td>
<p>Microsoft Windows 10/2016/2019</p>
</td>
</tr>
<tr>
<td>win11 <br/></td>
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
<td>solaris <br/></td>
<td>
<p>Solaris/OpenSolaris/OpenIndiania kernel</p>
</td>
</tr>
</table>

**`parallel[n]`: `/dev/parport\d+|/dev/usb/lp\d+`**

Map host parallel devices (n is 0 to 2).

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines - use with special care.
{% endhint %}

{% hint style="danger" %}
Experimental! User reported problems with this option.
{% endhint %}

**`protection`: `<boolean>` (*默认 =* `0`)**

Sets the protection flag of the VM. This will disable the remove VM and remove disk operations.

**`reboot`: `<boolean>` (*default =* `1`)**

Allow reboot. If set to *0* the VM exit on reboot.

**`rng0`: `[source=]</dev/urandom|/dev/random|/dev/hwrng> [,max_bytes=<integer>] [,period=<integer>]`**

Configure a VirtIO-based Random Number Generator.

**`max_bytes`=`<integer>` (*default =* `1024`)**

Maximum bytes of entropy allowed to get injected into the guest every *period* milliseconds. Use `0` to disable limiting (potentially dangerous!).

**`period`=`<integer>` (*default =* `1000`)**

Every *period* milliseconds the entropy-injection quota is reset, allowing the guest to retrieve another *max_bytes* of entropy.

**`source`=`</dev/hwrng | /dev/random | /dev/urandom>`**

The file on the host to gather entropy from. Using urandom does **not** decrease security in any meaningful way, as it’s still seeded from real entropy, and the bytes provided will most likely be mixed with real entropy on the guest as well. */dev/hwrng* can be used to pass through a hardware RNG from the host.

**`sata[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SATA hard disk or CD-ROM (n is 0 to 5).

**`aio`=`<io_uring | native | threads>`**

AIO type to use.

**`backup`=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`=`<volume>`**

The drive’s backing volume.

**`format`=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`mbps`=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`=`<cdrom | disk>` (*default =* `disk`)**

The drive’s media type.

**`replicate`=`<boolean>`（*默认 =* `1`）**

Whether the drive should considered for replication jobs.

**`rerror`=`<ignore | report | stop>`**

Read error action.

**`serial`=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`=`<boolean>`（*默认 =* `0`）**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`ssd`=`<boolean>`**

Whether to expose this drive as an SSD, rather than a rotational hard disk.

**`werror`=`<enospc | ignore | report | stop>`**

Write error action.

**`wwn`=`<wwn>`**

The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by *0x*.

**`scsi[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,product=<product>] [,queues=<integer>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,scsiblock=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,ssd=<1|0>] [,vendor=<vendor>] [,werror=<enum>] [,wwn=<wwn>]`**

Use volume as SCSI hard disk or CD-ROM (n is 0 to 30).

**`aio`=`<io_uring | native | threads>`**

AIO type to use.

**`backup`=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`=`<volume>`**

The drive’s backing volume.

**`format`=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`iothread`=`<boolean>`**

Whether to use iothreads for this drive

**`mbps`=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`=`<cdrom | disk>` (*default =* `disk`)**

The drive’s media type.

**`product`=`<product>`**

The drive’s product name, up to 16 bytes long.

**`queues`=`<integer> (2 - N)`**

Number of queues.

**`replicate`=`<boolean>`（*默认 =* `1`）**

Whether the drive should considered for replication jobs.

**`rerror`=`<ignore | report | stop>`**

Read error action.

**`ro`=`<boolean>`**

Whether the drive is read-only.

**`scsiblock`=`<boolean>` (*default =* `0`)**

whether to use scsi-block for full passthrough of host block device

{% hint style="warning" %}
can lead to I/O errors in combination with low memory or high memory fragmentation on host
{% endhint %}

**`serial`=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`=`<boolean>`（*默认 =* `0`）**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`ssd`=`<boolean>`**

Whether to expose this drive as an SSD, rather than a rotational hard disk.

**`vendor`=`<vendor>`**

The drive’s vendor name, up to 8 bytes long.

**`werror`=`<enospc | ignore | report | stop>`**

Write error action.

**`wwn`=`<wwn>`**

The drive’s worldwide name, encoded as 16 bytes hex string, prefixed by *0x*.

**`scsihw`: `<lsi | lsi53c810 | megasas | pvscsi | virtio-scsi-pci | virtio-scsi-single>` (*default =* `lsi`)**

SCSI controller model

**`searchdomain`: `<string>`**

cloud-init: Sets DNS search domains for a container. Create will automatically use the setting from the host if neither searchdomain nor nameserver are set.

**`serial[n]`: `(/dev/[^,]+|socket)`**

Create a serial device inside the VM (n is 0 to 3), and pass through a host serial device (i.e. /dev/ttyS0), or create a unix socket on the host side (use *qm terminal* to open a terminal connection).

{% hint style="info" %}
If you pass through a host serial device, it is no longer possible to migrate such machines - use with special care.
{% endhint %}

{% hint style="danger" %}
Experimental! User reported problems with this option.
{% endhint %}

**`shares`: `<integer> (0 - 50000)` (*default =* `1000`)**

Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd.

**`smbios1`: `[base64=<1|0>] [,family=<Base64 encoded string>] [,manufacturer=<Base64 encoded string>] [,product=<Base64 encoded string>] [,serial=<Base64 encoded string>] [,sku=<Base64 encoded string>] [,uuid=<UUID>] [,version=<Base64 encoded string>]`**

Specify SMBIOS type 1 fields.

**`base64`=`<boolean>`**

Flag to indicate that the SMBIOS values are base64 encoded

**`family`=`<Base64 encoded string>`**

Set SMBIOS1 family string.

**`manufacturer`=`<Base64 encoded string>`**

Set SMBIOS1 manufacturer.

**`product`=`<Base64 encoded string>`**

Set SMBIOS1 product ID.

**`serial`=`<Base64 encoded string>`**

Set SMBIOS1 serial number.

**`sku`=`<Base64 encoded string>`**

Set SMBIOS1 SKU string.

**`uuid`=`<UUID>`**

Set SMBIOS1 UUID.

**`version`=`<Base64 encoded string>`**

Set SMBIOS1 version.

**`smp`: `<integer> (1 - N)` (*default =* `1`)**

The number of CPUs. Please use option -sockets instead.

**`sockets`: `<integer> (1 - N)` (*default =* `1`)**

The number of CPU sockets.

**`spice_enhancements`: `[foldersharing=<1|0>] [,videostreaming=<off|all|filter>]`**

Configure additional enhancements for SPICE.

**`foldersharing`=`<boolean>` (*default =* `0`)**

Enable folder sharing via SPICE. Needs Spice-WebDAV daemon installed in the VM.

**`videostreaming`=`<all | filter | off>` (*default =* `off`)**

Enable video streaming. Uses compression for detected video streams.

**`sshkeys`: `<string>`**

cloud-init: Setup public SSH keys (one key per line, OpenSSH format).

**`startdate`: `(now | YYYY-MM-DD | YYYY-MM-DDTHH:MM:SS)` (*default =* `now`)**

Set the initial date of the real time clock. Valid format for date are:'now' or *2006-06-17T16:01:21* or *2006-06-17*.

**`startup`: `[[order=]\d+] [,up=\d+] [,down=\d+] `**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 *up* 或 *down* 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`tablet`: `<boolean>` (*default =* `1`)**

Enable/disable the USB tablet device. This device is usually needed to allow absolute mouse positioning with VNC. Else the mouse runs out of sync with normal VNC clients. If you’re running lots of console-only guests on one host, you may consider disabling this to save some context switches. This is turned off by default if you use spice (`qm set <vmid> --vga qxl`).

**`tags`: `<string>`**

Tags of the VM. This is only meta information.

**`tdf`: `<boolean>` (*default =* `0`)**

Enable/disable time drift fix.

**`template`: `<boolean>` (*默认 =* `0`)**

启用/禁用模板。

**`tpmstate0`: `[file=]<volume> [,format=<raw|qcow2|vmdk>] [,size=<DiskSize>] [,version=<v1.2|v2.0>]`**

Configure a Disk for storing TPM state. The format is fixed to *raw*.

**`file`=`<volume>`**

The drive’s backing volume.

**`format`=`<qcow2 | raw | vmdk>`**

Format of the image.

**`size`=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`version`=`<v1.2 | v2.0>` (*default =* `v1.2`)**

The TPM interface version. v2.0 is newer and should be preferred. Note that this cannot be changed later on.

**`unused[n]`: `[file=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`file`=`<volume>`**

The drive’s backing volume.

**`usb[n]`: `[[host=]<HOSTUSBDEVICE|spice>] [,mapping=<mapping-id>] [,usb3=<1|0>]`**

Configure an USB device (n is 0 to 4, for machine version >= 7.1 and ostype l26 or windows > 7, n can be up to 14).

**`host`=`<HOSTUSBDEVICE|spice>`**

The Host USB device or port or the value *spice*. HOSTUSBDEVICE syntax is:

```text
'bus-port(.port)*' (decimal numbers) or
'vendor_id:product_id' (hexadecimal numbers) or
'spice'
```

You can use the *lsusb -t* command to list existing usb devices.

{% hint style="info" %}
This option allows direct access to host hardware. So it is no longer possible to migrate such machines - use with special care.
{% endhint %}

The value *spice* can be used to add a usb redirection devices for spice.

Either this or the *mapping* key must be set.

**`mapping`=`<mapping-id>`**

The ID of a cluster wide mapping. Either this or the default-key *host* must be set.

**`usb3`=`<boolean>` (*default =* `0`)**

Specifies whether if given host option is a USB3 device or port. For modern guests (machine version >= 7.1 and ostype l26 and windows > 7), this flag is irrelevant (all devices are plugged into a xhci controller).

**`vcpus`: `<integer> (1 - N)` (*default =* `0`)**

Number of hotplugged vcpus.

**`vga`: `[[type=]<enum>] [,clipboard=<vnc>] [,memory=<integer>]`**

Configure the VGA Hardware. If you want to use high resolution modes (>= 1280x1024x16) you may need to increase the vga memory option. Since QEMU 2.9 the default VGA display type is *std* for all OS types besides some Windows versions (XP and older) which use *cirrus*. The *qxl* option enables the SPICE display server. For win* OS you can select how many independent displays you want, Linux guests can add displays them self. You can also run without any graphic card, using a serial device as terminal.

**`clipboard`=`<vnc>`**

Enable a specific clipboard. If not set, depending on the display type the SPICE one will be added. Live migration with a VNC clipboard is not possible with QEMU machine version < 10.1.

**`memory`=`<integer> (4 - 512)`**

Sets the VGA memory (in MiB). Has no effect with serial display.

**`type`=`<cirrus | none | qxl | qxl2 | qxl3 | qxl4 | serial0 | serial1 | serial2 | serial3 | std | virtio | virtio-gl | vmware>` (*default =* `std`)**

Select the VGA type. Using type *cirrus* is not recommended.

**`virtio[n]`: `[file=]<volume> [,aio=<native|threads|io_uring>] [,backup=<1|0>] [,bps=<bps>] [,bps_max_length=<seconds>] [,bps_rd=<bps>] [,bps_rd_max_length=<seconds>] [,bps_wr=<bps>] [,bps_wr_max_length=<seconds>] [,cache=<enum>] [,detect_zeroes=<1|0>] [,discard=<ignore|on>] [,format=<enum>] [,iops=<iops>] [,iops_max=<iops>] [,iops_max_length=<seconds>] [,iops_rd=<iops>] [,iops_rd_max=<iops>] [,iops_rd_max_length=<seconds>] [,iops_wr=<iops>] [,iops_wr_max=<iops>] [,iops_wr_max_length=<seconds>] [,iothread=<1|0>] [,mbps=<mbps>] [,mbps_max=<mbps>] [,mbps_rd=<mbps>] [,mbps_rd_max=<mbps>] [,mbps_wr=<mbps>] [,mbps_wr_max=<mbps>] [,media=<cdrom|disk>] [,replicate=<1|0>] [,rerror=<ignore|report|stop>] [,ro=<1|0>] [,serial=<serial>] [,shared=<1|0>] [,size=<DiskSize>] [,snapshot=<1|0>] [,werror=<enum>]`**

Use volume as VIRTIO hard disk (n is 0 to 15).

**`aio`=`<io_uring | native | threads>`**

AIO type to use.

**`backup`=`<boolean>`**

Whether the drive should be included when making backups.

**`bps`=`<bps>`**

Maximum r/w speed in bytes per second.

**`bps_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`bps_rd`=`<bps>`**

Maximum read speed in bytes per second.

**`bps_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`bps_wr`=`<bps>`**

Maximum write speed in bytes per second.

**`bps_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`cache`=`<directsync | none | unsafe | writeback | writethrough>`**

The drive’s cache mode

**`detect_zeroes`=`<boolean>`**

Controls whether to detect and try to optimize writes of zeroes.

**`discard`=`<ignore | on>`**

Controls whether to pass discard/trim requests to the underlying storage.

**`file`=`<volume>`**

The drive’s backing volume.

**`format`=`<cloop | qcow | qcow2 | qed | raw | vmdk>`**

The drive’s backing file’s data format.

**`iops`=`<iops>`**

Maximum r/w I/O in operations per second.

**`iops_max`=`<iops>`**

Maximum unthrottled r/w I/O pool in operations per second.

**`iops_max_length`=`<seconds>`**

Maximum length of I/O bursts in seconds.

**`iops_rd`=`<iops>`**

Maximum read I/O in operations per second.

**`iops_rd_max`=`<iops>`**

Maximum unthrottled read I/O pool in operations per second.

**`iops_rd_max_length`=`<seconds>`**

Maximum length of read I/O bursts in seconds.

**`iops_wr`=`<iops>`**

Maximum write I/O in operations per second.

**`iops_wr_max`=`<iops>`**

Maximum unthrottled write I/O pool in operations per second.

**`iops_wr_max_length`=`<seconds>`**

Maximum length of write I/O bursts in seconds.

**`iothread`=`<boolean>`**

Whether to use iothreads for this drive

**`mbps`=`<mbps>`**

Maximum r/w speed in megabytes per second.

**`mbps_max`=`<mbps>`**

Maximum unthrottled r/w pool in megabytes per second.

**`mbps_rd`=`<mbps>`**

Maximum read speed in megabytes per second.

**`mbps_rd_max`=`<mbps>`**

Maximum unthrottled read pool in megabytes per second.

**`mbps_wr`=`<mbps>`**

Maximum write speed in megabytes per second.

**`mbps_wr_max`=`<mbps>`**

Maximum unthrottled write pool in megabytes per second.

**`media`=`<cdrom | disk>` (*default =* `disk`)**

The drive’s media type.

**`replicate`=`<boolean>`（*默认 =* `1`）**

Whether the drive should considered for replication jobs.

**`rerror`=`<ignore | report | stop>`**

Read error action.

**`ro`=`<boolean>`**

Whether the drive is read-only.

**`serial`=`<serial>`**

The drive’s reported serial number, url-encoded, up to 20 bytes long.

**`shared`=`<boolean>`（*默认 =* `0`）**

Mark this locally-managed volume as available on all nodes.

{% hint style="warning" %}
This option does not share the volume automatically, it assumes it is shared already!
{% endhint %}

**`size`=`<DiskSize>`**

Disk size. This is purely informational and has no effect.

**`snapshot`=`<boolean>`**

Controls qemu’s snapshot mode feature. If activated, changes made to the disk are temporary and will be discarded when the VM is shutdown.

**`werror`=`<enospc | ignore | report | stop>`**

Write error action.

**`virtiofs[n]`: `[dirid=]<mapping-id> [,cache=<enum>] [,direct-io=<1|0>] [,expose-acl=<1|0>] [,expose-xattr=<1|0>]`**

Configuration for sharing a directory between host and guest using Virtio-fs.

**`cache`=`<always | auto | metadata | never>` (*default =* `auto`)**

The caching policy the file system should use (auto, always, metadata, never).

**`direct-io`=`<boolean>` (*default =* `0`)**

Honor the O_DIRECT flag passed down by guest applications.

**`dirid`=`<mapping-id>`**

Mapping identifier of the directory mapping to be shared with the guest. Also used as a mount tag inside the VM.

**`expose-acl`=`<boolean>` (*default =* `0`)**

Enable support for POSIX ACLs (enabled ACL implies xattr) for this mount.

**`expose-xattr`=`<boolean>` (*default =* `0`)**

Enable support for extended attributes for this mount.

**`vmgenid`: `<UUID>` (*default =* `1 (autogenerated)`)**

The VM generation ID (vmgenid) device exposes a 128-bit integer value identifier to the guest OS. This allows to notify the guest operating system when the virtual machine is executed with a different configuration (e.g. snapshot execution or creation from a template). The guest operating system notices the change, and is then able to react as appropriate by marking its copies of distributed databases as dirty, re-initializing its random number generator, etc. Note that auto-creation only works when done through API/CLI create or update methods, but not when manually editing the config file.

**`vmstatestorage`: `<storage ID>`**

Default storage for VM state volumes/files.

**`watchdog`: `[[model=]<i6300esb|ib700>] [,action=<enum>]`**

Create a virtual hardware watchdog device. Once enabled (by a guest action), the watchdog must be periodically polled by an agent inside the guest or else the watchdog will reset the guest (or execute the respective action specified)

**`action`=`<debug | none | pause | poweroff | reset | shutdown>`**

The action to perform if after activation the guest fails to poll the watchdog in time.

**`model`=`<i6300esb | ib700>` (*default =* `i6300esb`)**

Watchdog type to emulate.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
