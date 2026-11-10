# 4.4. 内容面板 <a href="#_content_panels" id="_content_panels"></a>

当你从资源树中选择一个项目时，相应对象会在内容面板中显示配置和状态信息。以下各节简要介绍此功能。更多详细信息，请参阅参考文档中的相应章节。

## 4.4.1. 数据中心 <a href="#_datacenter" id="_datacenter"></a>

[![screenshot/gui-datacenter-search.png](../../assets/screenshot-gui-datacenter-search-png-0d4035c472d2.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-search.png)

在数据中心级别，你可以访问集群范围的设置和信息。

- **搜索：** 在整个集群范围内搜索节点、虚拟机、容器、存储设备和池。
- **摘要：** 简要概述集群的运行状况和资源使用情况。
- **集群：** 提供创建或加入集群所需的功能和信息。
- **选项：** 查看和管理集群范围的默认设置。
- **存储：** 提供用于管理集群存储的接口。
- **备份：** 安排备份任务。此功能在整个集群范围内运行，因此在安排备份任务时，无需考虑虚拟机/容器位于集群中的哪个位置。
- **复制：** 查看和管理复制作业。
- **权限：** 管理用户、组和 API 令牌的权限，以及 LDAP、MS-AD 和双因素认证。
- **HA：** 管理 Proxmox VE 高可用性。
- **ACME：** 为服务器节点设置 ACME（Let’s Encrypt）证书。
- **防火墙：** 在整个集群范围内配置 Proxmox Firewall 并制作模板。
- **指标服务器：** 为 Proxmox VE 定义外部指标服务器。
- **通知：** 配置 Proxmox VE 的通知行为和通知目标。
- **支持：** 显示有关你的支持订阅的信息。

## 4.4.2. 节点 <a href="#_nodes" id="_nodes"></a>

[![screenshot/gui-node-summary.png](../../assets/screenshot-gui-node-summary-png-fa9649a32134.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-summary.png)

可以在此级别单独管理集群中的节点。

顶部标题栏提供了一些实用按钮，例如 *重启*、*关机*、*Shell*、*批量操作*和 *帮助*。*Shell* 提供 *noVNC*、*SPICE* 和 *xterm.js* 选项。*批量操作* 提供 *批量启动*、*批量关机* 和 *批量迁移* 选项。

- **搜索：** 在节点中搜索虚拟机、容器、存储设备和池。
- **摘要：** 简要显示节点资源使用情况的概览。
- **备注：** 使用 [Markdown 语法](../28-markdown-primer/01-markdown-basics.md) 编写自定义注释。
- **Shell：** 访问节点的 Shell 接口。
- **系统：** 配置网络、DNS 和时间设置，并访问 syslog。
- **更新：** 升级系统并查看可用的新软件包。
- **防火墙：** 管理特定节点的 Proxmox Firewall。
- **磁盘：** 概览已连接的磁盘，并管理它们的使用方式。
- **Ceph：** 仅在宿主机上安装了 Ceph 服务器时使用。在这种情况下，你可以在此处管理 Ceph 集群并查看其状态。
- **复制：** 查看和管理复制作业。
- **任务历史：** 查看以往任务的列表。
- **订阅：** 上传订阅密钥，并生成供支持案例使用的系统报告。

## 4.4.3. 客户机 <a href="#_guests" id="_guests"></a>

[![screenshot/gui-qemu-summary.png](../../assets/screenshot-gui-qemu-summary-png-58b9f19bf02c.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-summary.png)

客户机有两种不同的类型，且均可转换为模板。其中一种是基于内核的虚拟机（KVM），另一种是 Linux 容器（LXC）。它们的导航方式基本相同，只有部分选项不同。

要访问各种客户机管理接口，请从左侧菜单中选择一个虚拟机或容器。

标题栏包含电源管理、迁移、控制台访问及类型、克隆、HA 和帮助等项目的命令。其中一些按钮包含下拉菜单，例如，*关机* 还包含其他电源选项，而 *控制台* 包含不同的控制台类型：*SPICE*、*noVNC* 和 *xterm.js*。

右侧面板包含与左侧菜单中所选项目对应的接口。

可用的接口如下。

- **Summary:** provides a brief overview of the VM’s activity and a `Notes` field for [Markdown syntax](../28-markdown-primer/01-markdown-basics.md) comments.
- **控制台：** 访问虚拟机/容器的交互式控制台。
- **(KVM) 硬件：** 定义 KVM 虚拟机可用的硬件。
- **(LXC) 资源：** 定义 LXC 可用的系统资源。
- **(LXC) 网络：** 配置容器的网络设置。
- **(LXC) DNS：** 配置容器的 DNS 设置。
- **选项：** 管理客户机选项。
- **任务历史：** 查看与所选客户机相关的所有以往任务。
- **(KVM) 监视器：** 与 KVM 进程进行交互式通信的接口。
- **备份：** 创建和恢复系统备份。
- **复制：** 查看和管理所选客户机的复制作业。
- **快照：** 创建和恢复虚拟机快照。
- **防火墙：** 在虚拟机级别配置防火墙。
- **权限：** 管理所选客户机的权限。

## 4.4.4. 存储 <a href="#_storage" id="_storage"></a>

[![screenshot/gui-storage-summary-local.png](../../assets/screenshot-gui-storage-summary-local-png-bed0feb5e875.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-storage-summary-local.png)

与客户机接口一样，存储接口由左侧用于特定存储元素的菜单和右侧用于管理这些元素的接口组成。

此视图采用由两个分区组成的拆分视图。左侧是存储选项，右侧显示所选选项的内容。

- **摘要：** 显示有关存储的重要信息，例如其类型、使用情况以及其中存储的内容。
- **内容：** 存储所保存的每种内容类型各有一个菜单项，例如备份、ISO 镜像、CT 模板。
- **权限：** 管理存储的权限。

## 4.4.5. 池 <a href="#_pools" id="_pools"></a>

[![screenshot/gui-pool-summary-development.png](../../assets/screenshot-gui-pool-summary-development-png-00f1481ce5db.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-pool-summary-development.png)

同样，池视图也包含两个分区：左侧的菜单，以及右侧与每个菜单项对应的接口。

- **摘要：** 显示池的描述。
- **成员：** 显示和管理池成员（客户机和存储）。
- **权限：** 管理池的权限。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
