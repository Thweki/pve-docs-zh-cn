# 5.15. Guest Migration <a href="#_guest_migration" id="_guest_migration"></a>

将虚拟客户机迁移到其他节点是集群中一项有用的功能。可以通过一些设置来控制此类迁移的行为。可以通过配置文件 `datacenter.cfg` 完成此操作，也可以通过 API 或命令行参数针对特定迁移进行设置。

客户机处于在线还是离线状态，以及是否具有本地资源（如本地磁盘），都会有所不同。

有关虚拟机迁移的详细信息，请参阅 [QEMU/KVM 迁移一章](../10-virtual-machines/03-qm-migration.md)。

有关容器迁移的详细信息，请参阅 [容器迁移一章](../11-pct/10-pct-migration.md)。

## 5.15.1. Migration Type <a href="#_migration_type" id="_migration_type"></a>

迁移类型定义迁移数据应通过加密（`secure`）通道还是未加密（`insecure`）通道发送。将迁移类型设置为 `insecure` 意味着虚拟客户机的 RAM 内容也将以未加密方式传输，这可能导致客户机内部的关键数据（例如密码或加密密钥）泄露。

因此，如果您无法完全控制网络，并且不能保证没有人在网络上窃听，我们强烈建议使用安全通道。

{% hint style="info" %}
存储迁移不遵循此设置。目前，它始终通过安全通道发送存储内容。
{% endhint %}

加密需要大量计算能力，因此通常会将此设置更改为 `insecure` 以获得更好的性能。对现代系统的影响较小，因为它们在硬件中实现了 AES 加密。在传输速率可达到 10 Gbps 或更高的快速网络中，性能影响尤为明显。

## 5.15.2. Migration Network <a href="#pvecm_migration_network" id="pvecm_migration_network"></a>

默认情况下，Proxmox VE 使用集群通信所在的网络发送迁移流量。这并非最佳选择，因为敏感的集群流量可能受到干扰，而且该网络可能无法提供节点上可用的最佳带宽。

设置迁移网络参数允许对所有迁移流量使用专用网络。除了内存流量外，这也会影响离线迁移的存储流量。

迁移网络使用 CIDR 表示法进行设置。这样做的优点是您不必为每个节点设置单独的 IP 地址。Proxmox VE 可以根据以 CIDR 形式指定的网络，确定目标节点上的实际地址。要启用此功能，所指定的网络必须确保每个节点在相应网络中恰好有一个 IP。

### Example <a href="#_example" id="_example"></a>

假设我们有一个三节点部署，使用三个独立的网络。一个用于与互联网进行公共通信，一个用于集群通信，还有一个速度非常快的网络，我们希望将其用作迁移专用网络。

这种部署的网络配置可能如下所示：

```text
iface eno1 inet manual

# public network
auto vmbr0
iface vmbr0 inet static
    address 192.X.Y.57/24
    gateway 192.X.Y.1
    bridge-ports eno1
    bridge-stp off
    bridge-fd 0

# cluster network
auto eno2
iface eno2 inet static
    address  10.1.1.1/24

# fast network
auto eno3
iface eno3 inet static
    address  10.1.2.1/24
```

在这里，我们将使用网络 10.1.2.0/24 作为迁移网络。对于单次迁移，可以使用命令行工具的 `migration_network` 参数来完成此操作：

```text
# qm migrate 106 tre --online --migration_network 10.1.2.0/24
```

要将其配置为集群中所有迁移的默认网络，请通过 `migration` 属性在 `/etc/pve/datacenter.cfg` 文件中进行设置：

```text
# use dedicated migration network
migration: secure,network=10.1.2.0/24
```

{% hint style="info" %}
在 `/etc/pve/datacenter.cfg` 中设置迁移网络时，必须始终同时设置迁移类型。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
