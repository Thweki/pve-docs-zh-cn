# 12.16. 示例 <a href="#pvesdn_setup_examples" id="pvesdn_setup_examples"></a>

本节介绍针对常见 SDN 用例的多个配置示例，旨在提供具体实现及更多细节，帮助理解可用的配置选项。

## 12.16.1. Simple 区域示例 <a href="#pvesdn_setup_example_simple" id="pvesdn_setup_example_simple"></a>

Simple 区域网络为单台宿主机上的客户机创建隔离网络，使其相互连接。

{% hint style="success" %}
如果所有客户机都位于同一宿主机上，客户机之间可以连接，但无法从其他节点访问。
{% endhint %}

- 创建名为 `simple` 的 Simple 区域。
- 添加名为 `vnet1` 的 VNet。
- 创建子网，设置网关并启用 SNAT 选项。
- 这会在节点上创建网桥 `vnet1`。将此网桥分配给要加入网络的客户机，并配置 IP 地址。

两台虚拟机的网络接口配置可以如下所示，使它们能够通过 10.0.1.0/24 网络通信。

```text
allow-hotplug ens19
iface ens19 inet static
        address 10.0.1.14/24
```

```text
allow-hotplug ens19
iface ens19 inet static
        address 10.0.1.15/24
```

## 12.16.2. 源 NAT 示例 <a href="#pvesdn_setup_example_nat" id="pvesdn_setup_example_nat"></a>

如果希望允许 Simple 网络区域中的客户机建立出站连接，Simple 区域提供源 NAT（SNAT）选项。

从 [上述](#pvesdn_setup_example_simple) 配置开始，向 VNet `vnet1` 添加子网，设置网关 IP 并启用 SNAT 选项。

```text
Subnet: 172.16.0.0/24
Gateway: 172.16.0.1
SNAT: checked
```

在客户机中配置位于子网 IP 范围内的静态 IP 地址。

节点本身将使用网关 IP *172.16.0.1* 加入此网络，并充当子网范围内客户机的 NAT 网关。

## 12.16.3. VLAN 设置示例 <a href="#pvesdn_setup_example_vlan" id="pvesdn_setup_example_vlan"></a>

当不同节点上的虚拟机需要通过隔离网络通信时，VLAN 区域允许使用 VLAN 标签进行网络级隔离。

创建名为 `myvlanzone` 的 VLAN 区域：

```text
ID: myvlanzone
Bridge: vmbr0
```

创建名为 `myvnet1` 的 VNet，使用 VLAN 标签 10 和先前创建的 `myvlanzone`。

```text
ID: myvnet1
Zone: myvlanzone
Tag: 10
```

通过主 SDN 面板应用配置，在每个节点本地创建 VNet。

在 node1 上创建基于 Debian 的虚拟机（*vm1*），其虚拟网卡位于 `myvnet1`。

为此虚拟机使用以下网络配置：

```text
auto eth0
iface eth0 inet static
        address 10.0.3.100/24
```

在 node2 上创建第二台虚拟机（*vm2*），其虚拟网卡与 vm1 位于同一 VNet `myvnet1`。

为此虚拟机使用以下网络配置：

```text
auto eth0
iface eth0 inet static
        address 10.0.3.101/24
```

完成后，应能够通过该网络在两台虚拟机之间相互 ping 通。

## 12.16.4. QinQ 设置示例 <a href="#pvesdn_setup_example_qinq" id="pvesdn_setup_example_qinq"></a>

此示例配置两个 QinQ 区域，并向每个区域添加两台虚拟机，以演示额外的一层 VLAN 标签如何支持配置更多隔离 VLAN。

此配置的典型用例是托管服务提供商：为客户提供用于虚拟机通信的隔离网络，同时将其虚拟机与其他客户隔离。

创建名为 `qinqzone1`、服务 VLAN 为 20 的 QinQ 区域

```text
ID: qinqzone1
Bridge: vmbr0
Service VLAN: 20
```

再创建一个名为 `qinqzone2`、服务 VLAN 为 30 的 QinQ 区域

```text
ID: qinqzone2
Bridge: vmbr0
Service VLAN: 30
```

创建名为 `myvnet1`、VLAN-ID 为 100 的 VNet，位于先前创建的 `qinqzone1` 区域中。

```text
ID: qinqvnet1
Zone: qinqzone1
Tag: 100
```

创建一个 `myvnet2`，VLAN-ID 为 100，位于 `qinqzone2` 区域中。

```text
ID: qinqvnet2
Zone: qinqzone2
Tag: 100
```

在主 SDN Web 界面面板中应用配置，在每个节点本地创建 VNet。

创建四台基于 Debian 的虚拟机（vm1、vm2、vm3、vm4），为 vm1 和 vm2 添加使用网桥 `qinqvnet1` 的网络接口，为 vm3 和 vm4 添加使用网桥 `qinqvnet2` 的网络接口。

在虚拟机内部配置接口的 IP 地址，例如通过 `/etc/network/interfaces`：

```text
auto eth0
iface eth0 inet static
        address 10.0.3.101/24
```

为全部四台虚拟机配置地址，范围从 *10.0.3.101* 到 *10.0.3.104*。

现在，虚拟机 *vm1* 和 *vm2* 之间，以及 *vm3* 和 *vm4* 之间应能够相互 ping 通。但是，虚拟机 *vm1* 或 *vm2* 都无法 ping 通虚拟机 *vm3* 或 *vm4*，因为它们位于不同区域，使用不同的服务 VLAN。

## 12.16.5. VXLAN 设置示例 <a href="#pvesdn_setup_example_vxlan" id="pvesdn_setup_example_vxlan"></a>

此示例假定集群有三个节点，其节点 IP 地址分别为 192.168.0.1、192.168.0.2 和 192.168.0.3。

创建名为 `myvxlanzone` 的 VXLAN 区域，并将所有节点 IP 添加到对等方地址列表。使用默认 MTU 1450，或进行相应配置。

```text
ID: myvxlanzone
Peers Address List: 192.168.0.1,192.168.0.2,192.168.0.3
```

创建名为 `vxvnet1` 的 VNet，使用先前创建的 VXLAN 区域 `myvxlanzone`。

```text
ID: vxvnet1
Zone: myvxlanzone
Tag: 100000
```

在主 SDN Web 界面面板中应用配置，在每个节点本地创建 VNet。

在 node1 上创建基于 Debian 的虚拟机（*vm1*），其虚拟网卡位于 `vxvnet1`。

为此虚拟机使用以下网络配置（注意较低的 MTU）。

```text
auto eth0
iface eth0 inet static
        address 10.0.3.100/24
        mtu 1450
```

在 node3 上创建第二台虚拟机（*vm2*），其虚拟网卡与 vm1 位于同一 VNet `vxvnet1`。

为此虚拟机使用以下网络配置：

```text
auto eth0
iface eth0 inet static
        address 10.0.3.101/24
        mtu 1450
```

然后，*vm1* 和 *vm2* 之间应能够相互 ping 通。

## 12.16.6. EVPN 设置示例 <a href="#pvesdn_setup_example_evpn" id="pvesdn_setup_example_evpn"></a>

此示例假定集群有三个节点（node1、node2、node3），IP 地址分别为 192.168.0.1、192.168.0.2 和 192.168.0.3。

创建 EVPN 控制器，使用私有 ASN 编号，以上节点地址作为对等方。

```text
ID: myevpnctl
ASN#: 65000
Peers: 192.168.0.1,192.168.0.2,192.168.0.3
```

创建名为 `myevpnzone` 的 EVPN 区域，分配先前创建的 EVPN 控制器，并将 *node1* 和 *node2* 定义为出口节点。

```text
ID: myevpnzone
VRF VXLAN Tag: 10000
Controller: myevpnctl
MTU: 1450
VNet MAC Address: 32:F4:05:FE:6C:0A
Exit Nodes: node1,node2
```

创建第一个名为 `myvnet1` 的 VNet，使用 EVPN 区域 `myevpnzone`。

```text
ID: myvnet1
Zone: myevpnzone
Tag: 11000
```

在 `myvnet1` 上创建子网：

```text
Subnet: 10.0.1.0/24
Gateway: 10.0.1.1
```

创建第二个名为 `myvnet2` 的 VNet，使用相同的 EVPN 区域 `myevpnzone`。

```text
ID: myvnet2
Zone: myevpnzone
Tag: 12000
```

在 ``myvnet2``` 上创建不同的子网：

```text
Subnet: 10.0.2.0/24
Gateway: 10.0.2.1
```

通过主 SDN Web 界面面板应用配置，在每个节点本地创建 VNet 并生成 FRR 配置。

在 node1 上创建基于 Debian 的虚拟机（*vm1*），其虚拟网卡位于 `myvnet1`。

为 *vm1* 使用以下网络配置：

```text
auto eth0
iface eth0 inet static
        address 10.0.1.100/24
        gateway 10.0.1.1
        mtu 1450
```

在 node2 上创建第二台虚拟机（*vm2*），其虚拟网卡位于另一个 VNet `myvnet2`。

为 *vm2* 使用以下网络配置：

```text
auto eth0
iface eth0 inet static
        address 10.0.2.100/24
        gateway 10.0.2.1
        mtu 1450
```

现在应能够从 vm1 ping 通 vm2，也能从 vm2 ping 通 vm1。

如果从非网关节点 node3 上的 *vm2* ping 外部 IP，数据包会先到配置的 *myvnet2* 网关，然后路由到出口节点（*node1* 或 *node2*），再经由 node1 或 node2 上配置的默认网关离开这些节点。

{% hint style="info" %}
需要在外部网关上为 *10.0.1.0/24* 和 *10.0.2.0/24* 网络添加指向 node1 和 node2 的反向路由，以便公共网络可以返回响应。
{% endhint %}

如果配置了外部 BGP 路由器，BGP-EVPN 路由（此示例中为 10.0.1.0/24 和 10.0.2.0/24）将动态通告。

## 12.16.7. WireGuard 设置示例 <a href="#pvesdn_setup_example_wireguard" id="pvesdn_setup_example_wireguard"></a>

此示例假定有一个包含 3 个节点的 Proxmox 集群（*sdn1*、*sdn2* 和 *sdn3*），IP 地址分别为 `192.0.2.1`、`192.0.2.2` 和 `192.0.2.3`，以及外部 WireGuard 对等方（*sdn-router*），其 IP 地址为 `192.0.2.10`。

在此示例中，Proxmox 节点及外部对等方将通过 WireGuard 在 `198.51.100.0/24` 子网中进行全网状连接，此外，`203.0.113.0/24` 子网会通过外部 WireGuard 对等方 `198.51.100.10` 路由。

### 设置 WireGuard 网络结构 <a href="#set_up_wireguard_fabric" id="set_up_wireguard_fabric"></a>

[![screenshot/gui-datacenter-create-fabric-wireguard.png](../../assets/screenshot-gui-datacenter-create-fabric-wireguard-png-a9b9ae75c98b.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-fabric-wireguard.png)

点击左侧资源树中的 *数据中心*，然后导航到 *SDN* \> *网络结构*，点击 *创建* 并选择 *WireGuard*，创建新的 WireGuard 网络结构。

为网络结构选择名称，此处选择 *example*。

### 设置 WireGuard 接口 <a href="#set_up_wireguard_interfaces" id="set_up_wireguard_interfaces"></a>

[![screenshot/gui-datacenter-create-internal-node-wireguard.png](../../assets/screenshot-gui-datacenter-create-internal-node-wireguard-png-1540ed7410bf.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-internal-node-wireguard.png)

每个参与节点都需要 WireGuard 接口。为此，可向 WireGuard 网络结构添加类型为 *内部* 的新节点，选择相应节点，然后创建新的 WireGuard 接口。

节点本身可以配置两个属性：*端点* 和 *允许的 IP*。*端点* 指用于连接此节点的 IP/主机名，sdn1 的情况下为 `192.0.2.1`。由于本示例不应通过此节点路由其他子网，请将 *允许的 IP* 字段留空。

创建新的 WireGuard 接口 `wg0`，并配置应设置在该 WireGuard 接口上的 IP 地址，sdn1 的情况下为 `198.51.100.1/24`。默认监听端口为 `51820`，但可以通过 *监听端口* 字段手动更改。系统会为每个新的 WireGuard 接口自动创建公钥/私钥对。

### 设置外部节点 <a href="#set_up_external_node" id="set_up_external_node"></a>

[![screenshot/gui-datacenter-create-external-node-wireguard.png](../../assets/screenshot-gui-datacenter-create-external-node-wireguard-png-4da4203f662b.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-create-external-node-wireguard.png)

要添加外部节点，请向 WireGuard 网络结构再添加一个节点，但在创建节点对话框中选择类型 *外部*。输入外部节点接口的公钥，以及可用于访问此外部对等方的 IP/主机名 \+ 端口（本示例中为 `192.0.2.10:51820`）。将节点 IP `198.51.100.10/32` 以及 `203.0.113.0/24` 子网添加到允许的 IP 字段。

### 设置 WireGuard 对等连接 <a href="#set_up_wireguard_peerings" id="set_up_wireguard_peerings"></a>

[![screenshot/gui-datacenter-select-peers-wireguard.png](../../assets/screenshot-gui-datacenter-select-peers-wireguard-png-1c9ac309b979.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-select-peers-wireguard.png)

所有接口和外部对等方设置完成后，即可在 WireGuard 接口配置中将它们选为对等方。添加节点 *sdn2*、*sdn3* 以及 *sdn-router*，作为接口 `wg0`（位于节点 *sdn1*）的对等方：

这会生成以下 `wg0.conf` 文件，位于 `/etc/wireguard/proxmox`：

```text
root@sdn1:~# cat /etc/wireguard/proxmox/wg0.conf
[Interface]
PrivateKey = EpP9R0kqNA1UjGGeDL0/y9Ok66G44dqa2ALYJ0jTWwQ=
ListenPort = 51820

[Peer]
PublicKey = xIlHE6ZA25Qnpa+HYT1un3fbjO5/0A9YUbbRmTyLWW4=
AllowedIPs = 198.51.100.10/32, 203.0.113.0/24
Endpoint = 192.0.2.10:51820

[Peer]
PublicKey = CKClJbQ42U1pQM8MqMGCa1IpZbNcqb+OJBxVWJHIrx4=
AllowedIPs = 198.51.100.2/32
Endpoint = 192.0.2.2:51820

[Peer]
PublicKey = gCXBt+n2VNBR6RiUmUxG3+15G0qnXUzsSxEQvmwGMkw=
AllowedIPs = 198.51.100.3/32
Endpoint = 192.0.2.3:51820
```

每个选定的对等方都有一个 `[Peer]` 节。WireGuard 接口上配置的 IP 也会添加到对等方的 *允许的 IP* 中。

### 验证设置 <a href="#verifying_the_setup" id="verifying_the_setup"></a>

通过 ping 验证与 WireGuard 网络结构中其他参与方的连接：

```text
root@sdn1:~# ping -c1 198.51.100.2
PING 198.51.100.2 (198.51.100.2) 56(84) bytes of data.
64 bytes from 198.51.100.2: icmp_seq=1 ttl=64 time=2.08 ms

--- 198.51.100.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 2.083/2.083/2.083/0.000 ms


root@sdn1:~# ping -c1 198.51.100.3
PING 198.51.100.3 (198.51.100.3) 56(84) bytes of data.
64 bytes from 198.51.100.3: icmp_seq=1 ttl=64 time=2.26 ms

--- 198.51.100.3 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 2.255/2.255/2.255/0.000 ms


root@sdn1:~# ping -c1 198.51.100.10
PING 198.51.100.10 (198.51.100.10) 56(84) bytes of data.
64 bytes from 198.51.100.10: icmp_seq=1 ttl=64 time=1.29 ms

--- 198.51.100.10 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.286/1.286/1.286/0.000 ms
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
