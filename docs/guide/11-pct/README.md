# 11\. Proxmox 容器工具包 <a href="#chapter_pct" id="chapter_pct"></a>

容器是完全虚拟机（VM）的轻量级替代方案。它们使用所运行宿主机系统的内核，而不是模拟完整的操作系统（OS）。这意味着容器可以直接访问宿主机系统上的资源。

容器的运行时开销很低，通常可以忽略不计。但是，有一些缺点需要考虑：

- Proxmox 容器中只能运行 Linux 发行版。无法在容器内运行其他操作系统，例如 FreeBSD 或 Microsoft Windows。
- 出于安全原因，需要限制对宿主机资源的访问。因此，容器在各自独立的命名空间中运行。此外，容器内不允许使用某些系统调用（用户空间对 Linux 内核的请求）。

Proxmox VE 使用 [Linux Containers (LXC)](https://linuxcontainers.org/lxc/introduction/) 作为其底层容器技术。“Proxmox Container Toolkit”（`pct`）通过提供抽象复杂任务的接口，简化了 LXC 的使用和管理。

容器与 Proxmox VE 紧密集成。这意味着它们可以感知集群配置，并且可以使用与虚拟机相同的网络和存储资源。您还可以使用 Proxmox VE 防火墙，或通过 HA 框架管理容器。

我们的主要目标传统上一直是提供一种既能获得使用 VM 的好处、又没有额外开销的环境。这意味着 Proxmox 容器主要被归类为“系统容器”。

随着对 OCI（<strong>O</strong>pen <strong>C</strong>ontainer <strong>I</strong>nitiative）镜像支持的引入，Proxmox VE 现在还将“应用容器”作为技术预览集成进来。从 OCI 镜像创建容器时，该镜像会自动转换为 Proxmox VE 使用的 LXC 技术栈。

这种方法使用户既能受益于广泛的预打包应用生态系统，又能保留 Proxmox VE 强大的管理功能。

尽管直接运行轻量级“应用容器”相比完整 VM 具有显著优势，但对于要求最大隔离性和在线迁移能力的用例，将容器嵌套在 Proxmox QEMU VM 内仍是推荐做法。

## 11.1. 技术概述 <a href="#technology_overview" id="technology_overview"></a>

- LXC（[https://linuxcontainers.org/](https://linuxcontainers.org/)）
- 集成到 Proxmox VE 图形化 Web 用户界面（GUI）中
- 易于使用的命令行工具 `pct`
- 通过 Proxmox VE REST API 访问
- <em>lxcfs</em> 用于提供容器化的 /proc 文件系统
- 控制组（<em>cgroups</em>），用于资源隔离和限制
- <em>AppArmor</em> 和 <em>seccomp</em>，用于提高安全性
- 现代 Linux 内核
- 基于镜像的部署（[模板](#pct_supported_distributions)）
- 使用 Proxmox VE [存储库](../07-storage/README.md)
- 从宿主机配置容器（网络、DNS、存储等）

## 11.2. 支持的发行版 <a href="#pct_supported_distributions" id="pct_supported_distributions"></a>

官方支持的发行版列表如下。

以下发行版的模板可通过我们的仓库获取。您可以使用 [pveam](#pct_container_images) 工具或图形用户界面下载。

### 11.2.1. Alpine Linux <a href="#alpine_linux" id="alpine_linux"></a>

Alpine Linux 是一个注重安全的轻量级 Linux 发行版，基于 musl libc 和 busybox。

— [https://alpinelinux.org](https://alpinelinux.org)

有关当前支持的版本，请参阅：

[https://alpinelinux.org/releases/](https://alpinelinux.org/releases/)

### 11.2.2. Arch Linux <a href="#arch_linux" id="arch_linux"></a>

Arch Linux 是一个轻量级且灵活的 Linux® 发行版，力求保持简单。

— [https://archlinux.org/](https://archlinux.org/)

Arch Linux 采用滚动发布模式，更多详细信息请参阅其 wiki：

[https://wiki.archlinux.org/title/Arch\_Linux](https://wiki.archlinux.org/title/Arch_Linux)

### 11.2.3. CentOS、Almalinux、Rocky Linux <a href="#centos_almalinux_rocky_linux" id="centos_almalinux_rocky_linux"></a>

#### CentOS / CentOS Stream <a href="#centos_centos_stream" id="centos_centos_stream"></a>

CentOS Linux 发行版是一个稳定、可预测、可管理且可重现的平台，源自 Red Hat Enterprise Linux（RHEL）的源代码

— [https://centos.org](https://centos.org)

有关当前支持的版本，请参阅：

[https://en.wikipedia.org/wiki/CentOS#End-of-support\_schedule](https://en.wikipedia.org/wiki/CentOS#End-of-support_schedule)

#### Almalinux <a href="#almalinux" id="almalinux"></a>

一个开源、由社区拥有和治理、永久免费的企业级 Linux 发行版，专注于长期稳定性，提供稳健的生产级平台。AlmaLinux OS 与 RHEL® 和 CentOS Stream 之前的 CentOS 保持 1:1 二进制兼容。

— [https://almalinux.org](https://almalinux.org)

有关当前支持的版本，请参阅：

[https://en.wikipedia.org/wiki/AlmaLinux#Releases](https://en.wikipedia.org/wiki/AlmaLinux#Releases)

#### Rocky Linux <a href="#rocky_linux" id="rocky_linux"></a>

Rocky Linux 是一个社区企业级操作系统，旨在在其下游合作伙伴转变方向后，仍与美国顶级企业 Linux 发行版保持 100% 的逐缺陷兼容。

— [https://rockylinux.org](https://rockylinux.org)

有关当前支持的版本，请参阅：

[https://en.wikipedia.org/wiki/Rocky\_Linux#Releases](https://en.wikipedia.org/wiki/Rocky_Linux#Releases)

### 11.2.4. Debian <a href="#debian" id="debian"></a>

Debian 是一个自由操作系统，由 Debian 项目开发和维护。它是一个自由的 Linux 发行版，包含数千款应用程序，可满足用户的需求。

— [https://www.debian.org/intro/index#software](https://www.debian.org/intro/index#software)

有关当前支持的版本，请参阅：

[https://www.debian.org/releases/stable/releasenotes](https://www.debian.org/releases/stable/releasenotes)

### 11.2.5. Devuan <a href="#devuan" id="devuan"></a>

Devuan GNU\+Linux 是 Debian 的一个分支，不使用 systemd，使用户能够通过避免不必要的纠缠并确保初始化系统自由，重新掌控自己的系统。

— [https://www.devuan.org](https://www.devuan.org)

有关当前支持的版本，请参阅：

[https://www.devuan.org/os/releases](https://www.devuan.org/os/releases)

### 11.2.6. Fedora <a href="#fedora" id="fedora"></a>

Fedora 为硬件、云和容器创造了一个创新、自由且开源的平台，使软件开发人员和社区成员能够为其用户构建量身定制的解决方案。

— [https://getfedora.org](https://getfedora.org)

有关当前支持的版本，请参阅：

[https://fedoraproject.org/wiki/Releases](https://fedoraproject.org/wiki/Releases)

### 11.2.7. Gentoo <a href="#gentoo" id="gentoo"></a>

一个高度灵活、基于源代码的 Linux 发行版。

— [https://www.gentoo.org](https://www.gentoo.org)

Gentoo 采用滚动发布模式。

### 11.2.8. OpenSUSE <a href="#opensuse" id="opensuse"></a>

系统管理员、开发人员和桌面用户的首选。

— [https://www.opensuse.org](https://www.opensuse.org)

有关当前支持的版本，请参阅：

[https://get.opensuse.org/leap/](https://get.opensuse.org/leap/)

### 11.2.9. Ubuntu <a href="#ubuntu" id="ubuntu"></a>

Ubuntu 是面向企业服务器、桌面、云和 IoT 的现代化 Linux 开源操作系统。

— [https://ubuntu.com/](https://ubuntu.com/)

有关当前支持的版本，请参阅：

[https://wiki.ubuntu.com/Releases](https://wiki.ubuntu.com/Releases)

## 11.3. 容器镜像 <a href="#pct_container_images" id="pct_container_images"></a>

容器镜像有时也称为“模板”或“应用设备”，是包含运行容器所需一切的 `tar` 归档文件。Proxmox VE 可以使用两种主要类型的镜像：用于创建完整虚拟环境的 <strong>System Container Templates</strong>，以及基于 OCI 标准、用于运行特定应用的 <strong>Application Container Images</strong>。

### 11.3.1. 系统容器模板 <a href="#system_container_templates" id="system_container_templates"></a>

Proxmox VE 自身提供适用于 [最常见 Linux 发行版](#pct_supported_distributions) 的多种基本模板。可使用 GUI 或 `pveam`（Proxmox VE Appliance Manager 的缩写）命令行实用程序下载。此外，也可下载 [TurnKey Linux](https://www.turnkeylinux.org/) 容器模板。

可用模板列表通过 <em>pve-daily-update</em> 定时器每天更新。您也可以通过执行以下命令手动触发更新：

```text
# pveam update
```

要查看可用镜像列表，请运行：

```text
# pveam available
```

您可以通过指定感兴趣的 `section` 来缩小这个大列表的范围，例如基础 `system` 镜像：

**列出可用的系统镜像**

```text
# pveam available --section system
system          alpine-3.12-default_20200823_amd64.tar.xz
system          alpine-3.13-default_20210419_amd64.tar.xz
system          alpine-3.14-default_20210623_amd64.tar.xz
system          archlinux-base_20210420-1_amd64.tar.gz
system          centos-7-default_20190926_amd64.tar.xz
system          centos-8-default_20201210_amd64.tar.xz
system          debian-9.0-standard_9.7-1_amd64.tar.gz
system          debian-10-standard_10.7-1_amd64.tar.gz
system          devuan-3.0-standard_3.0_amd64.tar.gz
system          fedora-33-default_20201115_amd64.tar.xz
system          fedora-34-default_20210427_amd64.tar.xz
system          gentoo-current-default_20200310_amd64.tar.xz
system          opensuse-15.2-default_20200824_amd64.tar.xz
system          ubuntu-16.04-standard_16.04.5-1_amd64.tar.gz
system          ubuntu-18.04-standard_18.04.1-1_amd64.tar.gz
system          ubuntu-20.04-standard_20.04-1_amd64.tar.gz
system          ubuntu-20.10-standard_20.10-1_amd64.tar.gz
system          ubuntu-21.04-standard_21.04-1_amd64.tar.gz
```

在使用此类模板之前，您需要将其下载到您的某个存储中。如果不确定下载到哪个存储，可以直接使用名为 `local` 的存储。对于集群部署，最好使用共享存储，以便所有节点都能访问这些镜像。

```text
# pveam download local debian-10.0-standard_10.0-1_amd64.tar.gz
```

现在，您已准备好使用该镜像创建容器，并可以使用以下命令列出存储 `local` 上所有已下载的镜像：

```text
# pveam list local
local:vztmpl/debian-10.0-standard_10.0-1_amd64.tar.gz  219.95MB
```

{% hint style="success" %}
您还可以使用 Proxmox VE Web 图形用户界面（GUI）下载、列出和删除容器模板。
{% endhint %}

`pct` 使用它们创建新容器，例如：

```text
# pct create 999 local:vztmpl/debian-10.0-standard_10.0-1_amd64.tar.gz
```

上述命令会显示完整的 Proxmox VE 卷标识符。其中包含存储名称，大多数其他 Proxmox VE 命令都可以使用这些标识符。例如，您可以稍后使用以下命令删除该镜像：

```text
# pveam remove local:vztmpl/debian-10.0-standard_10.0-1_amd64.tar.gz
```

### 11.3.2. 开放容器倡议（OCI）镜像 <a href="#open_container_initiative_oci_images" id="open_container_initiative_oci_images"></a>

Proxmox VE 还可以使用 OCI 镜像创建容器，包括系统容器和应用容器。请注意，目前在 Proxmox VE 中运行应用容器仍被视为技术预览。

从 OCI 镜像创建的容器仍使用现有的 LXC 框架。

### 11.3.3. 获取 OCI 镜像 <a href="#obtaining_oci_images" id="obtaining_oci_images"></a>

在 Web 界面中，可以手动上传 OCI 镜像，也可以通过存储的容器模板视图中的 <strong>Pull from OCI registry</strong> 按钮从镜像仓库拉取镜像。

模板位于存储中后，您可以使用 `pct create` 创建容器，或使用 Web 界面中的向导。

## 11.4. 容器设置 <a href="#pct_settings" id="pct_settings"></a>

### 11.4.1. 常规设置 <a href="#pct_general" id="pct_general"></a>

[![screenshot/gui-create-ct-general.png](../../assets/screenshot-gui-create-ct-general-png-12aca10f1f54.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-ct-general.png)

容器的常规设置包括

- <strong>Node</strong>：容器将在其上运行的物理服务器
- <strong>CT ID</strong>：此 Proxmox VE 安装中用于标识容器的唯一编号
- <strong>Hostname</strong>：容器的主机名
- <strong>Resource Pool</strong>：容器和 VM 的逻辑组
- <strong>Password</strong>：容器的 root 密码
- <strong>SSH Public Key</strong>：用于通过 SSH 连接 root 账户的公钥
- <strong>Unprivileged container</strong>：此选项允许您在创建时选择要创建特权容器还是非特权容器。
- <strong>Nesting</strong>：暴露 procfs 和 sysfs 以允许嵌套容器。请注意，systemd 也使用此功能来隔离服务。

#### 非特权容器 <a href="#unprivileged_containers" id="unprivileged_containers"></a>

非特权容器使用一种称为用户命名空间的新内核功能。容器内的 root UID 0 会映射到容器外的非特权用户。这意味着，这些容器中的大多数安全问题（容器逃逸、资源滥用等）将影响某个随机的非特权用户，并且属于通用内核安全漏洞，而不是 LXC 问题。LXC 团队认为，非特权容器在设计上就是安全的。

这是创建新容器时的默认选项。

{% hint style="info" %}
如果容器使用 systemd 作为 init 系统，请注意，容器内运行的 systemd 版本应等于或高于 220。
{% endhint %}

#### 特权容器 <a href="#privileged_containers" id="privileged_containers"></a>

容器中的安全性通过使用强制访问控制 <em>AppArmor</em> 限制、<em>seccomp</em> 过滤器和 Linux 内核命名空间来实现。LXC 团队认为这种容器不安全，并且不会将新的容器逃逸漏洞视为值得分配 CVE 并快速修复的安全问题。因此，特权容器只应在受信任的环境中使用。

### 11.4.2. CPU <a href="#pct_cpu" id="pct_cpu"></a>

[![screenshot/gui-create-ct-cpu.png](../../assets/screenshot-gui-create-ct-cpu-png-e255ce428e71.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-ct-cpu.png)

可以使用 `cores` 选项限制容器内可见的 CPU 数量。这是通过 Linux <em>cpuset</em> cgroup（<strong>c</strong>ontrol <strong>group</strong>）实现的。`pvestatd` 中的一个特殊任务会定期尝试在可用 CPU 之间分配正在运行的容器。要查看分配的 CPU，请运行以下命令：

```text
# pct cpusets
 ---------------------
 102:              6 7
 105:      2 3 4 5
 108:  0 1
 ---------------------
```

容器直接使用宿主机内核。容器内的所有任务均由宿主机 CPU 调度器处理。Proxmox VE 默认使用 Linux <em>CFS</em>（<strong>C</strong>ompletely <strong>F</strong>air <strong>S</strong>cheduler）调度器，该调度器还提供额外的带宽控制选项。

<table>
<tr>
<td>
<code>cpulimit</code>: 
<br/>
</td>
<td>
<p>可以使用此选项进一步限制分配的 CPU 时间。请注意，这是一个浮点数，因此，为容器分配两个核心，同时将总体 CPU 消耗限制为半个核心，是完全有效的。</p>
<div>
<div>
<pre>cores: 2
cpulimit: 0.5</pre>
</div></div>
</td>
</tr>
<tr>
<td>
<code>cpuunits</code>: 
<br/>
</td>
<td>
<p>这是传递给内核调度器的相对权重。数值越大，此容器获得的 CPU 时间就越多。该数值是相对于所有其他正在运行的容器的权重而言的。默认值为 <code>100</code>（如果宿主机使用旧版 cgroup v1，则为 <code>1024</code>）。您可以使用此设置来确定某些容器的优先级。</p>
</td>
</tr>
</table>

### 11.4.3. 内存 <a href="#pct_memory" id="pct_memory"></a>

[![screenshot/gui-create-ct-memory.png](../../assets/screenshot-gui-create-ct-memory-png-c79b942688af.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-ct-memory.png)

容器内存通过 cgroup 内存控制器进行控制。

<table>
<tr>
<td>
<code>memory</code>: 
<br/>
</td>
<td>
<p>限制总体内存使用量。对应于 <code>memory.limit_in_bytes</code> cgroup 设置。</p>
</td>
</tr>
<tr>
<td>
<code>swap</code>: 
<br/>
</td>
<td>
<p>允许容器使用宿主机交换空间中的额外交换内存。对应于 <code>memory.memsw.limit_in_bytes</code> cgroup 设置，该设置被设为两个值之和（<code>memory + swap</code>）。</p>
</td>
</tr>
</table>

### 11.4.4. 挂载点 <a href="#pct_mount_points" id="pct_mount_points"></a>

[![screenshot/gui-create-ct-root-disk.png](../../assets/screenshot-gui-create-ct-root-disk-png-02418851db73.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-ct-root-disk.png)

根挂载点通过 `rootfs` 属性配置。您最多可以配置 256 个额外的挂载点。相应选项称为 `mp0` 至 `mp255`。它们可以包含以下设置：

**`rootfs`: `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。所有选项的详细说明见下文。

**`mp[n]`: `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`acl`\=`<boolean>`**

显式启用或禁用 ACL 支持。

**`backup`\=`<boolean>`**

是否将挂载点包含在备份中（仅用于卷挂载点）。

**`idmap`\=`<type:container:disk:range-size[;type:container:disk:range-size;...]>`**

自定义 UID/GID 映射，针对此挂载点覆盖容器的 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。

`type` 对于 UID 为 `u`，对于 GID 为 `g`。

`container` 是容器内看到的第一个 ID。

`disk` 是底层文件系统上对应的第一个 ID。

`range-size` 是要映射的连续 ID 数量。

未映射的 ID 回退到容器的 `lxc.idmap`。

示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上由 UID 456 拥有的文件在容器内将显示为由 UID 123 拥有。

示例 2：`g:100:50:5` 映射 5 个连续的 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。

示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，这意味着容器内的 ID 将与磁盘上的 ID 一致。

**`keepattrs`\=`<boolean>`（<em>默认 \=</em> `0`）**

如果挂载点目录已存在，则继承该目录的 UID、GID 和访问模式。

**`mountoptions`\=`<opt[;opt...]>`**

rootfs/mps 的额外挂载选项。

**`mp`\=`<Path>`**

从容器内部看到的挂载点路径。

{% hint style="info" %}
出于安全原因，不得包含任何符号链接。
{% endhint %}

**`quota`\=`<boolean>`**

启用容器内的用户配额（zfs 子卷不支持）

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

会将此卷包含到存储复制作业中。

**`ro`\=`<boolean>`**

只读挂载点

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

将此非卷挂载点标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享挂载点，它假定挂载点已被共享！
{% endhint %}

**`size`\=`<DiskSize>`**

卷大小（只读值）。

**`volume`\=`<volume>`**

要挂载到容器中的卷、设备或目录。

目前有三种类型的挂载点：存储支持的挂载点、绑定挂载和设备挂载。

**典型容器 `rootfs` 配置**

```text
rootfs: thin1:base-100-disk-1,size=8G
```

#### 存储支持的挂载点 <a href="#storage_backed_mount_points" id="storage_backed_mount_points"></a>

存储支持的挂载点由 Proxmox VE 存储子系统管理，并有三种不同形式：

- 基于镜像：这些是包含单个 ext4 文件系统的 raw 镜像。
- ZFS 子卷：从技术上说，这些是绑定挂载，但使用托管存储，因此允许调整大小和创建快照。
- 目录：传递 `size=0` 会触发一种特殊情况，此时将创建目录而不是 raw 镜像。

{% hint style="info" %}
存储支持的挂载点卷的特殊选项语法 `STORAGE_ID:SIZE_IN_GB` 会在指定存储上自动分配指定大小的卷。例如，调用
{% endhint %}

```text
pct set 100 -mp0 thin1:10,mp=/path/in/container
```

将在存储 `thin1` 上分配一个 10GB 的卷，用分配的卷 ID 替换卷 ID 占位符 `10`，并在容器中的 `/path/in/container` 处设置挂载点

#### 绑定挂载点 <a href="#bind_mount_points" id="bind_mount_points"></a>

绑定挂载允许您在容器内访问 Proxmox VE 宿主机上的任意目录。一些潜在的用例包括：

- 在客户机中访问您的主目录
- 在客户机中访问 USB 设备目录
- 在客户机中访问来自宿主机的 NFS 挂载

绑定挂载被视为不受存储子系统管理，因此您无法创建快照，也无法在容器内处理配额。使用非特权容器时，您可能会遇到由用户映射导致的权限问题，并且无法使用 ACL。

{% hint style="info" %}
使用 `vzdump` 时，不会备份绑定挂载点的内容。
{% endhint %}

{% hint style="warning" %}
出于安全原因，绑定挂载应仅使用专门为此目的预留的源目录，例如 `/mnt/bindmounts` 下的目录层次结构。切勿将 `/`、`/var` 或 `/etc` 等系统目录绑定挂载到容器中——这会带来巨大的安全风险。
{% endhint %}

{% hint style="info" %}
绑定挂载源路径不得包含任何符号链接。
{% endhint %}

例如，要使目录 `/mnt/bindmounts/shared` 可在 ID 为 `100` 的容器内的路径 `/shared` 下访问，请添加如下配置行：

```text
mp0: /mnt/bindmounts/shared,mp=/shared
```

添加到 `/etc/pve/lxc/100.conf`。

或者，也可以使用 `pct` 工具：

```text
pct set 100 -mp0 /mnt/bindmounts/shared,mp=/shared
```

以达到相同的结果。

#### 设备挂载点 <a href="#device_mount_points" id="device_mount_points"></a>

设备挂载点允许将宿主机的块设备直接挂载到容器中。与绑定挂载类似，设备挂载不受 Proxmox VE 存储子系统管理，但 `quota` 和 `acl` 选项会生效。

{% hint style="info" %}
设备挂载点只应在特殊情况下使用。在大多数情况下，存储支持的挂载点可以提供相同的性能和更多功能。
{% endhint %}

{% hint style="info" %}
使用 `vzdump` 时，不会备份设备挂载点的内容。
{% endhint %}

### 11.4.5. 网络 <a href="#pct_container_network" id="pct_container_network"></a>

[![screenshot/gui-create-ct-network.png](../../assets/screenshot-gui-create-ct-network-png-0b934631b465.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-create-ct-network.png)

您可以为单个容器配置多达 10 个网络接口。相应选项称为 `net0` 至 `net9`，它们可以包含以下设置：

**`net[n]`: `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`bridge`\=`<bridge>`**

网络设备要连接到的网桥。

**`firewall`\=`<boolean>`**

控制是否应使用此接口的防火墙规则。

**`gw`\=`<GatewayIPv4>`**

IPv4 流量的默认网关。

**`gw6`\=`<GatewayIPv6>`**

IPv6 流量的默认网关。

**`host-managed`\=`<boolean>`**

此接口的 IP 配置是否应由宿主机管理。启用后，由宿主机（而非容器）负责该接口的 IP 配置。容器不应在此接口上运行自己的 DHCP 客户端或网络管理器。这对于缺少内部网络管理堆栈的容器（例如许多应用程序容器）非常有用。

**`hwaddr`\=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`ip`\=`<(IPv4/CIDR|dhcp|manual)>`**

CIDR 格式的 IPv4 地址。

**`ip6`\=`<(IPv6/CIDR|auto|dhcp|manual)>`**

CIDR 格式的 IPv6 地址。

**`link_down`\=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`mtu`\=`<integer> (64 - 65535)`**

接口的最大传输单元。（lxc.network.mtu）

**`name`\=`<string>`**

从容器内部看到的网络设备名称。（lxc.network.name）

**`rate`\=`<mbps>`**

对接口应用速率限制

**`tag`\=`<integer> (1 - 4094)`**

此接口的 VLAN 标签。

**`trunks`\=`<vlanid[;vlanid...]>`**

允许通过此接口的 VLAN ID

**`type`\=`<veth>`**

网络接口类型。

### 11.4.6. 容器的自动启动和关闭 <a href="#pct_startup_and_shutdown" id="pct_startup_and_shutdown"></a>

要在宿主机系统启动时自动启动容器，请选择 <em>启动时启动</em> 选项，该选项位于 Web 界面的容器 <em>选项</em> 面板中，也可以运行以下命令：

```text
# pct set CTID -onboot 1
```

[![screenshot/gui-qemu-edit-start-order.png](../../assets/screenshot-gui-qemu-edit-start-order-png-9683f539b3b2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-edit-start-order.png)

**启动和关闭顺序**

如果您想微调容器的启动顺序，可以使用以下参数：

- <strong>启动/关闭顺序</strong>：定义启动顺序优先级。例如，如果希望 CT 最先启动，请将其设置为 1。（关闭时我们采用相反的启动顺序，因此启动顺序为 1 的容器将最后关闭）
- <strong>启动延迟</strong>：定义此容器启动与后续容器启动之间的间隔。例如，如果希望在启动其他容器之前等待 240 秒，请将其设置为 240。
- <strong>关闭超时</strong>：定义 Proxmox VE 在发出关闭命令后等待容器离线的时长（秒）。默认情况下，此值设置为 60，这意味着 Proxmox VE 将发出关闭请求，等待 60s 让机器离线；如果 60s 后机器仍在线，则会通知关闭操作失败。

请注意，未设置启动/关闭顺序参数的容器将始终在设置了该参数的容器之后启动，并且此参数仅对宿主机上本地运行的机器之间有意义，在整个集群范围内没有意义。

如果需要在宿主机启动与第一个容器启动之间设置延迟，请参阅 [Proxmox VE 节点管理](../03-system-administration/README.md#first_guest_boot_delay) 一节。

### 11.4.7. 钩子脚本 <a href="#hookscripts_2" id="hookscripts_2"></a>

您可以通过配置属性 `hookscript` 为 CT 添加钩子脚本。

```text
# pct set 100 -hookscript local:snippets/hookscript.pl
```

它将在客户机生命周期的各个阶段被调用。有关示例和文档，请参阅 `/usr/share/pve-docs/examples/guest-example-hookscript.pl` 下的示例脚本。

## 11.5. 安全注意事项 <a href="#security_considerations" id="security_considerations"></a>

容器使用宿主机系统的内核。这会为恶意用户暴露攻击面。一般来说，完整的虚拟机可以提供更好的隔离性。如果向未知或不受信任的人员提供容器，应考虑这一点。

为了减少攻击面，LXC 使用了 AppArmor、CGroups 和内核命名空间等许多安全功能。

### 11.5.1. AppArmor <a href="#apparmor" id="apparmor"></a>

AppArmor 配置文件用于限制对可能危险的操作的访问。某些系统调用（即 `mount`）会被禁止执行。

要跟踪 AppArmor 活动，请使用：

```text
# dmesg | grep apparmor
```

尽管不建议这样做，但可以为容器禁用 AppArmor。这会带来安全风险。如果系统配置不当，或者 LXC 或 Linux Kernel 存在漏洞，在容器内执行的某些系统调用可能会导致权限提升。

要为容器禁用 AppArmor，请将以下行添加到位于 `/etc/pve/lxc/CTID.conf` 的容器配置文件中：

```text
lxc.apparmor.profile = unconfined
```

{% hint style="warning" %}
请注意，不建议在生产环境中这样做。
{% endhint %}

### 11.5.2. 控制组（<em>cgroup</em>） <a href="#pct_cgroup" id="pct_cgroup"></a>

<em>cgroup</em> 是一种内核机制，用于按层次组织进程并分配系统资源。

通过 <em>cgroups</em> 控制的主要资源包括 CPU 时间、内存和交换空间限制，以及对设备节点的访问。<em>cgroups</em> 还用于在创建快照之前“冻结”容器。

<em>cgroups</em> 的当前版本是 [<em>cgroupv2</em>](https://www.kernel.org/doc/html/v6.14/admin-guide/cgroup-v2.html)。随着 Proxmox VE 7.0 的发布，cgroup 子系统的 [v1 版本](https://www.kernel.org/doc/html/v6.14/admin-guide/cgroup-v1/index.html)已被弃用，并在 Proxmox VE 9.0 中被完全移除。在 Proxmox VE 7.0 之前，默认使用“混合”模式。

#### CGroup 版本兼容性 <a href="#pct_cgroup_compat" id="pct_cgroup_compat"></a>

就 Proxmox VE 而言，纯 <em>cgroupv2</em> 与旧混合环境的主要区别在于，使用 <em>cgroupv2</em> 时，内存和交换空间现在可以独立控制。容器的内存和交换空间设置可以直接映射到这些值，而以前只能限制内存上限以及内存与交换空间<strong>总和</strong>的上限。

另一个重要区别是 <em>devices</em> 控制器的配置方式完全不同。因此，纯 <em>cgroupv2</em> 环境目前不支持文件系统配额。

容器操作系统需要支持 <em>cgroupv2</em>，才能在纯 <em>cgroupv2</em> 环境中运行。运行 <em>systemd</em> 231 或更新版本的容器支持 <em>cgroupv2</em> [\[1\]](#note-8ef5bb62-1)，不使用 <em>systemd</em> 作为 init 系统的容器也支持 [\[2\]](#note-8ef5bb62-2)。

{% hint style="info" %}
CentOS 7 和 Ubuntu 16.10 是两个知名的 Linux 发行版版本，其 <em>systemd</em> 版本太旧，无法在 <em>cgroupv2</em> 环境中运行。您可以：

- 将整个发行版升级到较新的版本。对于上述示例，可以升级到 Ubuntu 18.04 或 20.04，以及 CentOS 8（或 AlmaLinux、Rocky Linux 等 RHEL/CentOS 衍生版本）。这样做的好处是可以获得最新的缺陷修复和安全修复，通常还能获得新功能，并将 EOL 日期延后。
- 升级容器中的 systemd 版本。如果发行版提供 backports 软件仓库，这可以是一种简单快捷的临时措施。
- 将容器或其服务迁移到虚拟机。虚拟机与宿主机的交互要少得多，因此可以在其中顺利安装几十年前的操作系统版本。
{% endhint %}

#### 更改 CGroup 版本 <a href="#pct_cgroup_change_version" id="pct_cgroup_change_version"></a>

在 Proxmox VE 9.0 之前，您可以使用以下内核命令行参数切换回以前的版本：

```text
systemd.unified_cgroup_hierarchy=0
```

有关应在何处添加该参数，请参阅介绍如何编辑内核启动命令行的 [本节](../03-system-administration/README.md#sysboot_edit_kernel_cmdline)。

## 11.6. 客户机操作系统配置 <a href="#guest_operating_system_configuration" id="guest_operating_system_configuration"></a>

Proxmox VE 会尝试检测容器中的 Linux 发行版，并修改一些文件。以下是容器启动时所执行操作的简要列表：

**设置 /etc/hostname**

以设置容器名称

**修改 /etc/hosts**

以允许查询本地主机名

**网络配置**

将完整的网络配置传递给容器

**配置 DNS**

传递有关 DNS 服务器的信息

**调整 init 系统**

例如，修正生成的 getty 进程数量

**设置 root 密码**

在创建新容器时

**重写 ssh\_host\_keys**

使每个容器都有唯一的密钥

**随机化 crontab**

使 cron 不会在所有容器中同时启动

Proxmox VE 所做的更改会用注释标记括起来：

```text
# --- BEGIN PVE ---
<data>
# --- END PVE ---
```

这些标记会插入文件中的合理位置。如果这样的节已经存在，则会就地更新，不会移动。

可以通过为相应文件添加一个 `.pve-ignore.` 文件来阻止修改该文件。例如，如果存在 `/etc/.pve-ignore.hosts` 文件，则不会改动 `/etc/hosts` 文件。该文件可以是通过以下命令创建的简单空文件：

```text
# touch /etc/.pve-ignore.hosts
```

大多数修改取决于操作系统，因此会因发行版和版本而异。您可以通过手动将 `ostype` 设置为 `unmanaged` 来完全禁用这些修改。

操作系统类型检测通过测试容器内的特定文件来完成。Proxmox VE 首先检查 `/etc/os-release` 文件[\[3\]](#note-8ef5bb62-3)。如果该文件不存在，或者其中不包含清晰可辨的发行版标识符，则会检查以下发行版专用的版本文件。

**Ubuntu**

检查 /etc/lsb-release（`DISTRIB_ID=Ubuntu`）

**Debian**

检查 /etc/debian\_version

**Fedora**

检查 /etc/fedora-release

**RedHat 或 CentOS**

检查 /etc/redhat-release

**ArchLinux**

检查 /etc/arch-release

**Alpine**

检查 /etc/alpine-release

**Gentoo**

检查 /etc/gentoo-release

{% hint style="info" %}
如果配置的 `ostype` 与自动检测到的类型不同，容器将无法启动。
{% endhint %}

## 11.7. 容器存储 <a href="#pct_container_storage" id="pct_container_storage"></a>

Proxmox VE LXC 容器存储模型比传统的容器存储模型更灵活。一个容器可以有多个挂载点。这样就可以为每个应用程序使用最合适的存储。

例如，容器的根文件系统可位于速度较慢、价格较低的存储上，而数据库可以通过第二个挂载点位于快速分布式存储上。更多详情请参阅 [挂载点](#pct_mount_points) 一节。

可以使用 Proxmox VE 存储库支持的任何存储类型。这意味着容器可以存储在本地存储（例如 `lvm`、`zfs` 或目录）、共享外部存储（如 `iSCSI`、`NFS`），甚至 Ceph 等分布式存储系统上。如果底层存储支持，则可以使用快照或克隆等高级存储功能。`vzdump` 备份工具可以使用快照来提供一致的容器备份。

此外，可以使用<em>绑定挂载</em>直接挂载本地设备或本地目录。这使容器内几乎可以零开销地访问本地资源。绑定挂载可以作为在容器之间共享数据的一种简便方式。

### 11.7.1. FUSE 挂载 <a href="#fuse_mounts" id="fuse_mounts"></a>

{% hint style="warning" %}
由于 Linux 内核的 freezer 子系统存在已知问题，强烈建议不要在容器内使用 FUSE 挂载，因为在挂起或快照模式备份时需要冻结容器。
{% endhint %}

如果无法用其他挂载机制或存储技术替代 FUSE 挂载，可以在 Proxmox 宿主机上建立 FUSE 挂载，并使用绑定挂载点使其在容器内可访问。

### 11.7.2. 在容器内部使用配额 <a href="#using_quotas_inside_containers" id="using_quotas_inside_containers"></a>

配额允许在容器内为每个用户可使用的磁盘空间量设置限制。

{% hint style="info" %}
这目前需要使用旧版 <em>cgroups</em>。
{% endhint %}

{% hint style="info" %}
这仅适用于基于 ext4 镜像的存储类型，并且目前仅适用于特权容器。
{% endhint %}

启用 `quota` 选项会为挂载点使用以下挂载选项：`usrjquota=aquota.user,grpjquota=aquota.group,jqfmt=vfsv0`

这样就可以像在其他任何系统上一样使用配额。您可以通过运行以下命令来初始化 `/aquota.user` 和 `/aquota.group` 文件：

```text
# quotacheck -cmug /
# quotaon /
```

然后使用 `edquota` 命令编辑配额。有关详细信息，请参阅容器内所运行发行版的文档。

{% hint style="info" %}
您需要为每个挂载点运行上述命令，并传入挂载点的路径，而不是只传入 `/`。
{% endhint %}

### 11.7.3. 在容器内部使用 ACL <a href="#using_acls_inside_containers" id="using_acls_inside_containers"></a>

标准 Posix <strong>访问</strong><strong>控制</strong><strong>列表</strong>在容器内也可用。ACL 允许您设置比传统的用户/组/其他用户模型更细致的文件所有权。

### 11.7.4. 容器挂载点的备份 <a href="#backup_of_container_mount_points" id="backup_of_container_mount_points"></a>

要在备份中包含挂载点，请在容器配置中为其启用 `backup` 选项。对于现有挂载点 `mp0`

```text
mp0: guests:subvol-100-disk-1,mp=/root/files,size=8G
```

添加 `backup=1` 以启用该选项。

```text
mp0: guests:subvol-100-disk-1,mp=/root/files,size=8G,backup=1
```

{% hint style="info" %}
在 GUI 中创建新挂载点时，此选项默认启用。
{% endhint %}

要禁用挂载点备份，请按上述方式添加 `backup=0`，或在 GUI 中取消选中<strong>备份</strong>复选框。

### 11.7.5. 容器挂载点的复制 <a href="#replication_of_containers_mount_points" id="replication_of_containers_mount_points"></a>

默认情况下，复制根磁盘时也会复制其他挂载点。如果希望 Proxmox VE 存储复制机制跳过某个挂载点，可以为该挂载点设置<strong>跳过复制</strong>选项。自 Proxmox VE 5.0 起，复制需要类型为 `zfspool` 的存储。当容器已配置复制时，如果要将挂载点添加到其他类型的存储，则必须为该挂载点启用<strong>跳过复制</strong>。

## 11.8. 备份与恢复 <a href="#backup_and_restore" id="backup_and_restore"></a>

### 11.8.1. 容器备份 <a href="#container_backup" id="container_backup"></a>

可以使用 `vzdump` 工具进行容器备份。有关详细信息，请参阅 `vzdump` 手册页。

### 11.8.2. 恢复容器备份 <a href="#restoring_container_backups" id="restoring_container_backups"></a>

通过 `vzdump` 创建的容器备份可以使用 `pct
restore` 命令恢复。默认情况下，`pct restore` 会尽可能恢复备份的容器配置。可以通过在命令行中手动设置容器选项来覆盖备份的配置（详情参见 `pct` 手册页）。

{% hint style="info" %}
`pvesm extractconfig` 可用于查看 vzdump 归档中包含的已备份配置。
{% endhint %}

有两种基本恢复模式，它们的区别仅在于对挂载点的处理方式：

#### “简单”恢复模式 <a href="#8220_simple_8221_restore_mode" id="8220_simple_8221_restore_mode"></a>

如果既未明确设置 `rootfs` 参数，也未明确设置任何可选的 `mpX` 参数，则将通过以下步骤从备份的配置文件中恢复挂载点配置：

1. 从备份中提取挂载点及其选项
2. 在通过 `storage` 参数指定的存储上，为基于存储的挂载点创建卷（默认值：`local`）。
3. 从备份归档中提取文件
4. 将绑定挂载点和设备挂载点添加到恢复的配置中（仅限 root 用户）

{% hint style="info" %}
由于绑定挂载点和设备挂载点从不备份，最后一步不会恢复任何文件，而只会恢复配置选项。这里假定此类挂载点要么通过其他机制备份（例如，通过绑定挂载到许多容器中的 NFS 空间），要么根本不打算备份。
{% endhint %}

Web 界面中的容器恢复操作也使用这种简单模式。

#### “高级”恢复模式 <a href="#8220_advanced_8221_restore_mode" id="8220_advanced_8221_restore_mode"></a>

通过设置 `rootfs` 参数（以及可选的任意 `mpX` 参数组合），`pct restore` 命令会自动切换到高级模式。该高级模式会完全忽略备份归档中包含的 `rootfs` 和 `mpX` 配置选项，而仅使用显式作为参数提供的选项。

此模式允许在恢复时灵活配置挂载点设置，例如：

- 为每个挂载点单独设置目标存储、卷大小和其他选项
- 根据新的挂载点方案重新分配已备份的文件
- 恢复到设备和/或绑定挂载点（仅限 root 用户）

## 11.9. 使用 `pct` 管理容器 <a href="#managing_containers_with_span_class_monospaced_pct_span" id="managing_containers_with_span_class_monospaced_pct_span"></a>

“Proxmox Container Toolkit”（`pct`）是用于管理 Proxmox VE 容器的命令行工具。它可用于创建或销毁容器，以及控制容器的运行（启动、停止、重启、迁移等）。它还可用于设置容器配置文件中的参数，例如网络配置或内存限制。

### 11.9.1. CLI 用法示例 <a href="#cli_usage_examples_2" id="cli_usage_examples_2"></a>

基于 Debian 模板创建容器（前提是你已通过 Web 界面下载该模板）

```text
# pct create 100 /var/lib/vz/template/cache/debian-10.0-standard_10.0-1_amd64.tar.gz
```

启动容器 100

```text
# pct start 100
```

通过 getty 启动登录会话

```text
# pct console 100
```

进入 LXC 命名空间并以 root 用户身份运行 shell

```text
# pct enter 100
```

显示配置

```text
# pct config 100
```

在容器运行时添加名为 `eth0` 的网络接口，将其桥接到宿主机网桥 `vmbr0`，并设置地址和网关

```text
# pct set 100 -net0 name=eth0,bridge=vmbr0,ip=192.168.15.147/24,gw=192.168.15.1
```

将容器的内存减少到 512MB

```text
# pct set 100 -memory 512
```

销毁容器时，始终会将其从访问控制列表中移除，并始终会移除该容器的防火墙配置。如果还想将容器从复制任务、备份任务和 HA 资源配置中移除，则必须启用 <em>--purge</em>。

{% hint style="info" %}
启用 purge 还会从所有引用该 HA 资源的亲和性规则中移除该资源，并移除仅剩这一个资源的规则。
{% endhint %}

```text
# pct destroy 100 --purge
```

将挂载点卷移动到其他存储。

```text
# pct move-volume 100 mp0 other-storage
```

将卷重新分配给另一个 CT。这会从源 CT 中移除卷 `mp0`，并将其作为 `mp1` 附加到目标 CT。在后台，该卷会被重命名，使名称与新所有者匹配。

```text
#  pct move-volume 100 mp0 --target-vmid 200 --target-volume mp1
```

### 11.9.2. 获取调试日志 <a href="#obtaining_debugging_logs" id="obtaining_debugging_logs"></a>

如果 `pct start` 无法启动特定容器，可以通过传递 `--debug` 标志来收集调试输出（将 `CTID` 替换为容器的 CTID），这可能会有所帮助：

```text
# pct start CTID --debug
```

或者，你可以使用以下 `lxc-start` 命令，它会将调试日志保存到 `-o` 输出选项指定的文件中：

```text
# lxc-start -n CTID -F -l DEBUG -o /tmp/lxc-CTID.log
```

此命令会尝试以前台模式启动容器。要停止容器，请在另一个终端中运行 `pct shutdown CTID` 或 `pct stop CTID`。

收集到的调试日志将写入 `/tmp/lxc-CTID.log`。

{% hint style="info" %}
如果自上次使用 `pct start` 尝试启动以来，你更改了容器配置，则需要至少运行一次 `pct start`，以同时更新 `lxc-start` 使用的配置。
{% endhint %}

## 11.10. 迁移 <a href="#pct_migration" id="pct_migration"></a>

如果你有集群，可以使用以下命令迁移容器

```text
# pct migrate <ctid> <target>
```

只要容器处于离线状态，此方法就有效。如果定义了本地卷或挂载点，并且目标宿主机上定义了相同的存储，迁移会通过网络将内容复制到目标宿主机。

由于技术限制，正在运行的容器无法进行在线迁移。你可以执行重启迁移，即关闭容器，将其移动，然后在目标节点上重新启动。由于容器非常轻量，这通常只会造成几百毫秒的停机时间。

可以通过 Web 界面，或使用 `--restart` 标志配合 `pct migrate` 命令执行重启迁移。

重启迁移会关闭容器，并在指定的超时时间（默认为 180 秒）后强制终止它。随后会像离线迁移一样迁移容器，完成后在目标节点上启动容器。

## 11.11. 配置 <a href="#pct_configuration" id="pct_configuration"></a>

`/etc/pve/lxc/<CTID>.conf` 文件存储容器配置，其中 `<CTID>` 是给定容器的数字 ID。与存储在 `/etc/pve/` 中的所有其他文件一样，这些文件会自动复制到所有其他集群节点。

{% hint style="info" %}
CTID \< 100 保留供内部使用，且 CTID 必须在整个集群中唯一。
{% endhint %}

**容器配置示例**

```text
ostype: debian
arch: amd64
hostname: www
memory: 512
swap: 512
net0: bridge=vmbr0,hwaddr=66:64:66:64:64:36,ip=dhcp,name=eth0,type=veth
rootfs: local:107/vm-107-disk-1.raw,size=7G
```

配置文件是简单的文本文件。你可以使用普通文本编辑器（例如 `vi` 或 `nano`）编辑它们。这有时便于进行小幅修正，但请记住，需要重启容器才能应用此类更改。

因此，通常最好使用 `pct` 命令生成和修改这些文件，或者完全通过 GUI 操作。我们的工具包足够智能，可以将大多数更改立即应用到正在运行的容器。此功能称为“热插拔”，在这种情况下无需重启容器。

如果某项更改无法热插拔，则会被登记为待处理更改（在 GUI 中以红色显示）。只有重启容器后，这些更改才会应用。

### 11.11.1. 文件格式 <a href="#file_format_2" id="file_format_2"></a>

容器配置文件使用简单的以冒号分隔的键/值格式。每行的格式如下：

```text
# this is a comment
OPTION: value
```

这些文件中的空行会被忽略，以 `#` 字符开头的行会被视为注释，同样会被忽略。

可以直接添加底层的 LXC 风格配置，例如：

```text
lxc.init_cmd: /sbin/my_own_init
```

或

```text
lxc.init_cmd = /sbin/my_own_init
```

这些设置会直接传递给 LXC 底层工具。

### 11.11.2. 快照 <a href="#pct_snapshots" id="pct_snapshots"></a>

创建快照时，`pct` 会将快照时的配置存储在同一配置文件中单独的快照部分。例如，创建名为“testsnapshot”的快照后，配置文件将如下所示：

**带快照的容器配置**

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

有一些与快照相关的属性，例如 `parent` 和 `snaptime`。`parent` 属性用于存储快照之间的父/子关系。`snaptime` 是快照创建时间戳（Unix 纪元）。

### 11.11.3. 选项 <a href="#pct_options" id="pct_options"></a>

**`arch`: `<amd64 | arm64 | armhf | i386 | riscv32 | riscv64>` (<em>默认 \=</em> `amd64`)**

操作系统架构类型。

**`cmode`: `<console | shell | tty>` (<em>默认 \=</em> `tty`)**

控制台模式。默认情况下，console 命令会尝试连接到一个可用的 tty 设备。将 cmode 设置为 <em>console</em> 时，它会尝试改为连接到 /dev/console。如果将 cmode 设置为 <em>shell</em>，它只会在容器内调用一个 shell（无需登录）。

**`console`: `<boolean>` (<em>默认 \=</em> `1`)**

将控制台设备（/dev/console）连接到容器。

**`cores`: `<integer> (1 - 8192)`**

分配给容器的核心数。默认情况下，容器可以使用所有可用核心。

**`cpulimit`: `<number> (0 - 8192)` (<em>默认 \=</em> `0`)**

CPU 使用限制。

{% hint style="info" %}
如果计算机有 2 个 CPU，则 CPU 时间总量为 <em>2</em>。值 <em>0</em> 表示不限制 CPU。
{% endhint %}

**`cpuunits`: `<integer> (0 - 500000)` (<em>默认 \=</em> `cgroup v1: 1024, cgroup v2: 100`)**

容器的 CPU 权重。该参数用于内核公平调度器。数值越大，该容器获得的 CPU 时间就越多。该数值是相对于所有其他正在运行的客户机的权重而言的。

**`debug`: `<boolean>` (<em>默认 \=</em> `0`)**

尽量输出更详细的信息。目前仅在启动时启用调试日志级别。

**`description`: `<string>`**

容器的描述。显示在 Web 界面中 CT 的摘要里。这会作为注释保存在配置文件中。

**`dev[n]`: `[[path=]<Path>] [,deny-write=<1|0>] [,gid=<integer>] [,mode=<Octal access mode>] [,uid=<integer>]`**

要直通给容器的设备

**`deny-write`\=`<boolean>` (<em>默认 \=</em> `0`)**

禁止容器写入设备

**`gid`\=`<integer> (0 - N)`**

要分配给设备节点的组 ID

**`mode`\=`<Octal access mode>`**

要设置在设备节点上的访问模式

**`path`\=`<Path>`**

要直通到容器的设备路径

**`uid`\=`<integer> (0 - N)`**

要分配给设备节点的用户 ID

**`entrypoint`: `(?^:[^\x00-\x08\x0a-\x1F\x7F]+)` (<em>默认 \=</em> `/sbin/init`)**

作为 init 运行的命令，可带参数；可以以绝对路径、相对路径或 $PATH 中的二进制文件开头。

**`env`: `(?^:(?:\w+=[^\x00-\x08\x0a-\x1F\x7F]*)(?:\0\w+=[^\x00-\x08\x0a-\x1F\x7F]*)*)`**

容器运行时环境，以 NUL 分隔的列表表示。替换配置中的所有 lxc.environment.runtime 条目。

**`features`: `[force_rw_sys=<1|0>] [,fuse=<1|0>] [,keyctl=<1|0>] [,mknod=<1|0>] [,mount=<fstype;fstype;...>] [,nesting=<1|0>]`**

允许容器访问高级功能。

**`force_rw_sys`\=`<boolean>` (<em>默认 \=</em> `0`)**

在非特权容器中将 /sys 挂载为 `rw`，而不是 `mixed`。在使用较新版本（\>\= v245）的 systemd-network 时，这可能会破坏网络。

**`fuse`\=`<boolean>` (<em>默认 \=</em> `0`)**

允许在容器中使用 <em>fuse</em> 文件系统。请注意，fuse 与 freezer cgroup 之间的交互可能导致 I/O 死锁。

**`keyctl`\=`<boolean>` (<em>默认 \=</em> `0`)**

仅限非特权容器：允许使用 keyctl() 系统调用。这是在容器内使用 docker 所必需的。默认情况下，非特权容器会将此系统调用视为不存在。这主要是针对 systemd-networkd 的变通方法，因为当某些 keyctl() 操作因权限不足被内核拒绝时，systemd-networkd 会将其视为致命错误。本质上，你可以在运行 systemd-networkd 和 docker 之间进行选择。

**`mknod`\=`<boolean>` (<em>默认 \=</em> `0`)**

允许非特权容器使用 mknod() 添加某些设备节点。这需要支持 seccomp 用户空间陷阱的内核（5.3 或更新版本）。这是实验性功能。

**`mount`\=`<fstype;fstype;...>`**

允许挂载特定类型的文件系统。这应是 mount 命令所使用的文件系统类型列表。请注意，这可能对容器的安全产生负面影响。例如，如果能访问 loop 设备，挂载文件可以绕过 devices cgroup 的 mknod 权限；挂载 NFS 文件系统可能完全阻塞宿主机的 I/O，并使其无法重启，等等。

**`nesting`\=`<boolean>` (<em>默认 \=</em> `0`)**

允许嵌套。最好与具有额外 ID 映射的非特权容器一起使用。请注意，这会向客户机暴露宿主机的 procfs 和 sysfs 内容。systemd 隔离服务也需要此功能。

**`hookscript`: `<string>`**

在容器生命周期的各个阶段执行的脚本。

**`hostname`: `<string>`**

为容器设置主机名。

**`lock`: `<backup | create | destroyed | disk | fstrim | migrate | mounted | rollback | snapshot | snapshot-delete>`**

锁定/解锁容器。

**`memory`: `<integer> (16 - N)` (<em>默认 \=</em> `512`)**

容器的内存量，单位为 MB。

**`mp[n]`: `[volume=]<volume> ,mp=<Path> [,acl=<1|0>] [,backup=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,keepattrs=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器挂载点。使用特殊语法 STORAGE\_ID:SIZE\_IN\_GiB 可分配新卷。

**`acl`\=`<boolean>`**

显式启用或禁用 ACL 支持。

**`backup`\=`<boolean>`**

是否将挂载点包含在备份中（仅用于卷挂载点）。

**`idmap`\=`<type:container:disk:range-size[;type:container:disk:range-size;...]>`**

自定义 UID/GID 映射，针对此挂载点覆盖容器的 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。

`type` 对于 UID 为 `u`，对于 GID 为 `g`。

`container` 是容器内看到的第一个 ID。

`disk` 是底层文件系统上对应的第一个 ID。

`range-size` 是要映射的连续 ID 数量。

未映射的 ID 回退到容器的 `lxc.idmap`。

示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上由 UID 456 拥有的文件在容器内将显示为由 UID 123 拥有。

示例 2：`g:100:50:5` 映射 5 个连续的 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。

示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，这意味着容器内的 ID 将与磁盘上的 ID 一致。

**`keepattrs`\=`<boolean>`（<em>默认 \=</em> `0`）**

如果挂载点目录已存在，则继承该目录的 UID、GID 和访问模式。

**`mountoptions`\=`<opt[;opt...]>`**

rootfs/mps 的额外挂载选项。

**`mp`\=`<Path>`**

从容器内部看到的挂载点路径。

{% hint style="info" %}
出于安全原因，不得包含任何符号链接。
{% endhint %}

**`quota`\=`<boolean>`**

启用容器内的用户配额（zfs 子卷不支持）

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

会将此卷包含到存储复制作业中。

**`ro`\=`<boolean>`**

只读挂载点

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

将此非卷挂载点标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享挂载点，它假定挂载点已被共享！
{% endhint %}

**`size`\=`<DiskSize>`**

卷大小（只读值）。

**`volume`\=`<volume>`**

要挂载到容器中的卷、设备或目录。

**`nameserver`: `<string>`**

设置容器的 DNS 服务器 IP 地址。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`net[n]`: `name=<string> [,bridge=<bridge>] [,firewall=<1|0>] [,gw=<GatewayIPv4>] [,gw6=<GatewayIPv6>] [,host-managed=<1|0>] [,hwaddr=<XX:XX:XX:XX:XX:XX>] [,ip=<(IPv4/CIDR|dhcp|manual)>] [,ip6=<(IPv6/CIDR|auto|dhcp|manual)>] [,link_down=<1|0>] [,mtu=<integer>] [,rate=<mbps>] [,tag=<integer>] [,trunks=<vlanid[;vlanid...]>] [,type=<veth>]`**

指定容器的网络接口。

**`bridge`\=`<bridge>`**

网络设备要连接到的网桥。

**`firewall`\=`<boolean>`**

控制是否应使用此接口的防火墙规则。

**`gw`\=`<GatewayIPv4>`**

IPv4 流量的默认网关。

**`gw6`\=`<GatewayIPv6>`**

IPv6 流量的默认网关。

**`host-managed`\=`<boolean>`**

此接口的 IP 配置是否应由宿主机管理。启用后，由宿主机（而非容器）负责该接口的 IP 配置。容器不应在此接口上运行自己的 DHCP 客户端或网络管理器。这对于缺少内部网络管理堆栈的容器（例如许多应用程序容器）非常有用。

**`hwaddr`\=`<XX:XX:XX:XX:XX:XX>`**

I/G（Individual/Group，个体/组）位未设置的常见 MAC 地址。

**`ip`\=`<(IPv4/CIDR|dhcp|manual)>`**

CIDR 格式的 IPv4 地址。

**`ip6`\=`<(IPv6/CIDR|auto|dhcp|manual)>`**

CIDR 格式的 IPv6 地址。

**`link_down`\=`<boolean>`**

是否应断开此接口的连接（类似拔掉插头）。

**`mtu`\=`<integer> (64 - 65535)`**

接口的最大传输单元。（lxc.network.mtu）

**`name`\=`<string>`**

从容器内部看到的网络设备名称。（lxc.network.name）

**`rate`\=`<mbps>`**

对接口应用速率限制

**`tag`\=`<integer> (1 - 4094)`**

此接口的 VLAN 标签。

**`trunks`\=`<vlanid[;vlanid...]>`**

允许通过此接口的 VLAN ID

**`type`\=`<veth>`**

网络接口类型。

**`onboot`: `<boolean>` (<em>默认 \=</em> `0`)**

指定容器是否在系统启动时启动。

**`ostype`: `<alpine | archlinux | centos | debian | devuan | fedora | gentoo | nixos | opensuse | ubuntu | unmanaged>`**

操作系统类型。用于在容器内设置配置，并对应于 /usr/share/lxc/config/\<ostype\>.common.conf 中的 lxc 设置脚本。可使用值 <em>unmanaged</em> 跳过特定于操作系统的设置。

**`protection`: `<boolean>` (<em>默认 \=</em> `0`)**

设置容器的保护标志。这将阻止对 CT 或 CT 磁盘执行删除/更新操作。

**`rootfs`: `[volume=]<volume> [,acl=<1|0>] [,idmap=<type:container:disk:range-size[;type:container:disk:range-size;...]>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`**

将卷用作容器根目录。

**`acl`\=`<boolean>`**

显式启用或禁用 ACL 支持。

**`idmap`\=`<type:container:disk:range-size[;type:container:disk:range-size;...]>`**

自定义 UID/GID 映射，针对此挂载点覆盖容器的 `lxc.idmap`。接受以分号分隔的 `type:container:disk:range-size` 条目列表。

`type` 对于 UID 为 `u`，对于 GID 为 `g`。

`container` 是容器内看到的第一个 ID。

`disk` 是底层文件系统上对应的第一个 ID。

`range-size` 是要映射的连续 ID 数量。

未映射的 ID 回退到容器的 `lxc.idmap`。

示例 1：`u:123:456:1` 将容器内的 UID 123 映射到磁盘上的 UID 456。磁盘上由 UID 456 拥有的文件在容器内将显示为由 UID 123 拥有。

示例 2：`g:100:50:5` 映射 5 个连续的 GID，使容器内的 GID 100-104 映射到磁盘上的 GID 50-54。

示例 3：`passthrough` 对所有 UID 和 GID 进行恒等映射，这意味着容器内的 ID 将与磁盘上的 ID 一致。

**`mountoptions`\=`<opt[;opt...]>`**

rootfs/mps 的额外挂载选项。

**`quota`\=`<boolean>`**

启用容器内的用户配额（zfs 子卷不支持）

**`replicate`\=`<boolean>`（<em>默认 \=</em> `1`）**

会将此卷包含到存储复制作业中。

**`ro`\=`<boolean>`**

只读挂载点

**`shared`\=`<boolean>`（<em>默认 \=</em> `0`）**

将此非卷挂载点标记为在所有节点上可用。

{% hint style="warning" %}
此选项不会自动共享挂载点，它假定挂载点已被共享！
{% endhint %}

**`size`\=`<DiskSize>`**

卷大小（只读值）。

**`volume`\=`<volume>`**

要挂载到容器中的卷、设备或目录。

**`searchdomain`: `<string>`**

设置容器的 DNS 搜索域。如果既未设置 searchdomain 也未设置 nameserver，创建时将自动使用宿主机的设置。

**`startup`: \`\[\[order\=\]\\d\+\] \[,up\=\\d\+\] \[,down\=\\d\+\] \`**

启动和关闭行为。Order 是一个非负数，用于定义总体启动顺序。关闭时按相反顺序执行。此外，还可以设置以秒为单位的 <em>up</em> 或 <em>down</em> 延迟，指定在启动或停止下一个 VM 之前等待的延迟时间。

**`swap`: `<integer> (0 - N)` (<em>默认 \=</em> `512`)**

容器的 SWAP 大小，单位为 MB。

**`tags`: `<string>`**

容器的标签。这只是元信息。

**`template`: `<boolean>` (<em>默认 \=</em> `0`)**

启用/禁用模板。

**`timezone`: `<string>`**

容器中使用的时区。如果未设置此选项，则不执行任何操作。可以设置为 <em>host</em> 以与宿主机时区匹配，也可以设置为 /usr/share/zoneinfo/zone.tab 中的任意时区选项。

**`tty`: `<integer> (0 - 6)` (<em>默认 \=</em> `2`)**

指定容器可用的 tty 数量

**`unprivileged`: `<boolean>` (<em>默认 \=</em> `0`)**

使容器以非特权用户身份运行。创建时，默认值为 1。恢复时，默认值为备份中的值。（不应手动修改。）

**`unused[n]`: `[volume=]<volume>`**

对未使用卷的引用。这供内部使用，不应手动修改。

**`volume`\=`<volume>`**

当前未使用的卷。

## 11.12. 锁 <a href="#locks_2" id="locks_2"></a>

容器迁移、快照和备份（`vzdump`）会设置锁，以防止在受影响的容器上并发执行不兼容的操作。有时你需要手动删除此类锁（例如，断电后）。

```text
# pct unlock <CTID>
```

{% hint style="danger" %}
只有确定设置该锁的操作已不再运行时，才能这样做。
{% endhint %}

## 注释

### 注释 1 <a href="#note-8ef5bb62-1" id="note-8ef5bb62-1"></a>

这包括 Proxmox VE 提供的所有容器模板的最新主要版本

### 注释 2 <a href="#note-8ef5bb62-2" id="note-8ef5bb62-2"></a>

例如 Alpine Linux

### 注释 3 <a href="#note-8ef5bb62-3" id="note-8ef5bb62-3"></a>

/etc/os-release 取代了众多的各发行版专用版本文件 [https://manpages.debian.org/stable/systemd/os-release.5.en.html](https://manpages.debian.org/stable/systemd/os-release.5.en.html)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
