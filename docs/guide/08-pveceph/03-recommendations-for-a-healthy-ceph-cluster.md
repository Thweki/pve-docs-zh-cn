# 8.3. 健康 Ceph 集群的建议 <a href="#recommendations_for_a_healthy_ceph_cluster" id="recommendations_for_a_healthy_ceph_cluster"></a>

要构建超融合 Proxmox \+ Ceph 集群，部署时必须至少使用三台（最好完全相同的）服务器。

另请查阅 [Ceph 网站](https://docs.ceph.com/en/tentacle/start/hardware-recommendations/)上的建议。

{% hint style="info" %}
以下建议应被视为选择硬件的粗略指南。因此，根据您的具体需求进行调整仍然至关重要。您应测试自己的部署，并持续监控其健康状况和性能。
{% endhint %}

## CPU <a href="#pve_ceph_recommendation_cpu" id="pve_ceph_recommendation_cpu"></a>

Ceph 服务可分为两类：

- CPU 使用率高，受益于较高的 CPU 基础频率和多个核心。此类服务包括：

  - 对象存储守护进程（OSD）服务
  - 用于 CephFS 的元数据服务（MDS）
- CPU 使用率适中，不需要多个 CPU 核心。这类服务包括：

  - 监视器（MON）服务
  - 管理器（MGR）服务

一个简单的经验法则是，您应为每个 Ceph 服务至少分配一个 CPU 核心（或线程），以提供维持 Ceph 稳定、持久性能所需的最低资源。

例如，如果您计划在一个节点上运行一个 Ceph 监视器、一个 Ceph 管理器和 6 个 Ceph OSD 服务，那么为了获得基本且稳定的性能，您应专门为 Ceph 预留 8 个 CPU 核心。

请注意，OSD 的 CPU 使用率主要取决于磁盘性能。磁盘可能达到的 IOPS（**IO** **O**perations per **S**econd）越高，OSD 服务可使用的 CPU 资源就越多。对于现代企业级 SSD 磁盘，例如能够持续维持超过 100’000 的高 IOPS 负载且具有亚毫秒延迟的 NVMe，每个 OSD 可以使用多个 CPU 线程；对于性能非常高的磁盘，每个由 NVMe 支持的 OSD 很可能会使用四到六个 CPU 线程。

## 内存 <a href="#pve_ceph_recommendation_memory" id="pve_ceph_recommendation_memory"></a>

尤其是在超融合部署中，需要仔细规划并监控内存消耗。除了虚拟机和容器的预计内存使用量外，您还必须确保为 Ceph 留出足够的内存，以提供出色且稳定的性能。

虽然正常情况下内存使用量可能较少，但在恢复、重新平衡或回填等关键操作期间，内存消耗会增加。这意味着您应避免在常规运行时就耗尽所有可用内存，而应留出一些余量，以应对服务中断。

目前建议[配置](08-pve-ceph-configuration.md) OSD 时至少使用 **8 GiB 内存**，以获得良好性能。OSD 守护进程默认需要 4 GiB。

{% hint style="info" %}
总内存消耗主要由 OSD 守护进程的数量决定。但是，在关键操作期间，所有 Ceph 服务都可能需要额外内存。
{% endhint %}

## 网络 <a href="#pve_ceph_recommendation_network" id="pve_ceph_recommendation_network"></a>

我们建议至少使用 10 Gbps 或更高带宽的网络，专用于 Ceph 流量。如果没有可用的 10\+ Gbps 交换机，对于三到五个节点的集群，网状网络部署 [\[1\]](#note-c8a7a90b-1) 也是一种选择。

{% hint style="warning" %}
流量，尤其是在恢复期间产生的流量，会干扰同一网络上的其他服务，尤其是对延迟敏感的 Proxmox VE corosync 集群协议栈可能会受到影响，从而可能导致集群失去仲裁。将 Ceph 流量迁移到专用的物理隔离网络可以避免此类干扰，不仅可避免对 corosync 的干扰，也可避免对任何虚拟客户机提供的网络服务的干扰。
{% endhint %}

估算带宽需求时，您需要考虑磁盘的性能。单个 HDD 或许无法跑满 1 Gb 链路，但每个节点上的多个 HDD OSD 就已经能跑满 10 Gbps。如果使用现代 NVMe 连接的 SSD，单个 SSD 就可以跑满 10 Gbps 甚至更高的带宽。对于此类高性能部署，我们建议至少使用 25 Gpbs，而要充分发挥底层磁盘的全部性能潜力，甚至可能需要 40 Gbps 或 100\+ Gbps。

如果不确定，对于高性能部署，我们建议使用三个（物理）独立的网络：

- 一个用于 Ceph（内部）集群流量的超高带宽（25\+ Gbps）网络。
- 一个用于 Ceph（公共）流量的高带宽（10\+ Gpbs）网络，即 Ceph 服务器与 Ceph 客户端之间的存储流量。根据您的需求，该网络也可用于承载虚拟客户机流量和 VM 在线迁移流量。
- 一个专用于对延迟敏感的 corosync 集群通信的中等带宽（1 Gbps）网络。

如果启用了防火墙，您必须开放 Ceph 使用的端口，最简单的方法是使用防火墙 `macro`。

## 磁盘 <a href="#pve_ceph_recommendation_disk" id="pve_ceph_recommendation_disk"></a>

规划 Ceph 集群规模时，必须考虑恢复时间。尤其是对于小型集群，恢复可能耗时很长。建议在小型部署中使用 SSD 而非 HDD，以缩短恢复时间，并最大程度降低恢复期间发生后续故障事件的可能性。

一般而言，SSD 提供的 IOPS 高于机械磁盘。考虑到这一点，尽管成本较高，但实施基于 [class](10-pve-ceph-device-classes.md) 的池分离可能仍有意义。另一种提高 OSD 速度的方法是使用更快的磁盘作为日志或 DB/**W**rite-**A**head-**L**og 设备，请参阅 [创建 Ceph OSD](07-pve-ceph-osds.md)。如果将一块更快的磁盘用于多个 OSD，必须在 OSD 与 WAL / DB（或日志）磁盘之间选择适当的平衡，否则这块更快的磁盘会成为所有关联 OSD 的瓶颈。

除磁盘类型外，各节点使用大小一致且数量均匀分布的磁盘时，Ceph 的性能最佳。例如，每个节点配备 4 x 500 GB 磁盘，优于混合配置一块 1 TB 磁盘和三块 250 GB 磁盘。

您还需要平衡 OSD 数量和单个 OSD 容量。更大的容量可以提高存储密度，但也意味着单个 OSD 发生故障时，Ceph 必须一次性恢复更多数据。

## 避免使用 RAID <a href="#pve_ceph_recommendation_raid" id="pve_ceph_recommendation_raid"></a>

由于 Ceph 自行处理数据对象冗余以及对磁盘（OSD）的多次并行写入，使用 RAID 控制器通常不会提升性能或可用性。相反，Ceph 旨在自行管理整块磁盘，中间不需要任何抽象层。RAID 控制器并非针对 Ceph 工作负载而设计，可能会使情况复杂化，有时甚至降低性能，因为其写入和缓存算法可能会干扰 Ceph 的相应算法。

{% hint style="warning" %}
避免使用 RAID 控制器，改用主机总线适配器（HBA）。
{% endhint %}

## 注释

### 注释 1 <a href="#note-c8a7a90b-1" id="note-c8a7a90b-1"></a>

Ceph 全网状网络 [https://pve.proxmox.com/wiki/Full\_Mesh\_Network\_for\_Ceph\_Server](https://pve.proxmox.com/wiki/Full_Mesh_Network_for_Ceph_Server)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
