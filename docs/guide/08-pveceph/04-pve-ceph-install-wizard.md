# 8.4. Initial Ceph Installation \& Configuration <a href="#pve_ceph_install_wizard" id="pve_ceph_install_wizard"></a>

## 8.4.1. Using the Web-based Wizard <a href="#_using_the_web_based_wizard" id="_using_the_web_based_wizard"></a>

[![screenshot/gui-node-ceph-install.png](../../assets/screenshot-gui-node-ceph-install-png-146fee5f8339.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-install.png)

使用 Proxmox VE 的好处是，它提供了易于使用的 Ceph 安装向导。点击一个集群节点，然后在菜单树中导航到 Ceph 部分。如果尚未安装 Ceph，您会看到提示您进行安装的信息。

该向导分为多个部分，每个部分都必须成功完成，才能使用 Ceph。

首先，您需要选择要安装的 Ceph 版本。优先选择其他节点使用的版本；如果这是您第一个安装 Ceph 的节点，则选择最新版本。

开始安装后，向导将从 Proxmox VE 的 Ceph 软件仓库下载并安装所有必需的软件包。

[![screenshot/gui-node-ceph-install-wizard-step0.png](../../assets/screenshot-gui-node-ceph-install-wizard-step0-png-41f18d5b8097.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-install-wizard-step0.png)

完成安装步骤后，您需要创建配置。每个集群只需执行一次此步骤，因为该配置会通过 Proxmox VE 的集群 [配置文件系统（pmxcfs）](../06-pmxcfs/README.md) 自动分发到所有其余集群成员。

配置步骤包括以下设置：

<a id="pve_ceph_wizard_networks"></a>



- **Public Network:** This network will be used for public storage communication (e.g., for virtual machines using a Ceph RBD backed disk, or a CephFS mount), and communication between the different Ceph services. This setting is required.   
   Separating your Ceph traffic from the Proxmox VE cluster communication (corosync), and possibly the front-facing (public) networks of your virtual guests, is highly recommended. Otherwise, Ceph’s high-bandwidth IO-traffic could cause interference with other low-latency dependent services.
- **Cluster Network:** Specify to separate the [OSD](07-pve-ceph-osds.md) replication and heartbeat traffic as well. This setting is optional.   
   Using a physically separated network is recommended, as it will relieve the Ceph public and the virtual guests network, while also providing a significant Ceph performance improvements.   
   The Ceph cluster network can be configured and moved to another physically separated network at a later time.

[![screenshot/gui-node-ceph-install-wizard-step2.png](../../assets/screenshot-gui-node-ceph-install-wizard-step2-png-8fdd1bc317bd.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-ceph-install-wizard-step2.png)

另外两个选项属于高级选项，因此只有在您清楚自己的操作时才应更改。

- **Number of replicas**: Defines how often an object is replicated.
- **Minimum replicas**: Defines the minimum number of required replicas for I/O to be marked as complete.

此外，您需要选择第一个监视器节点。此步骤为必需步骤。

就是这样。现在，最后一步应显示成功页面，其中包含后续操作说明。您的系统现在已准备好开始使用 Ceph。要开始使用，您需要创建一些额外的 [监视器](05-pve-ceph-monitors.md)、[OSD](07-pve-ceph-osds.md) 和至少一个 [池](09-pve-ceph-pools.md)。

本章其余部分将指导您充分利用基于 Proxmox VE 的 Ceph 部署。这包括上述提示及更多内容，例如 [CephFS](13-pveceph-fs.md)，它是新 Ceph 集群的有用补充。

## 8.4.2. CLI Installation of Ceph Packages <a href="#pve_ceph_install" id="pve_ceph_install"></a>

除了使用 Web 界面中推荐的 Proxmox VE Ceph 安装向导外，您还可以在每个节点上使用以下 CLI 命令：

```text
pveceph install
```

This sets up an `apt` package repository in `/etc/apt/sources.list.d/ceph.sources` and installs the required software.

## 8.4.3. Initial Ceph configuration via CLI <a href="#_initial_ceph_configuration_via_cli" id="_initial_ceph_configuration_via_cli"></a>

使用 Proxmox VE Ceph 安装向导（推荐），或在其中一个节点上运行以下命令：

```text
pveceph init --network 10.10.10.0/24
```

这会在 `/etc/pve/ceph.conf` 处创建一个初始配置，并为 Ceph 配置专用网络。该文件会通过 [pmxcfs](../06-pmxcfs/README.md) 自动分发到所有 Proxmox VE 节点。该命令还会在 `/etc/ceph/ceph.conf` 处创建一个指向该文件的符号链接。因此，您可以直接运行 Ceph 命令，而无需指定配置文件。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
