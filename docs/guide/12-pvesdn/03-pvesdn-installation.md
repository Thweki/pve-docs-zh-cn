# 12.3. 安装 <a href="#pvesdn_installation" id="pvesdn_installation"></a>

## 12.3.1. SDN 核心 <a href="#sdn_core" id="sdn_core"></a>

从 Proxmox VE 8.1 开始，默认安装核心软件定义网络（SDN）软件包。

如果从较早版本升级，需要在每个节点上安装 `libpve-network-perl` 软件包：

```text
apt update
apt install libpve-network-perl
```

{% hint style="info" %}
Proxmox VE 7.0 及以上版本默认安装 `ifupdown2` 软件包。如果系统最初安装的是较早版本，需要显式安装 `ifupdown2` 软件包。
{% endhint %}

安装后，需要确保所有节点的 `/etc/network/interfaces` 配置文件末尾都包含以下行，以便包含并激活 SDN 配置。

```text
source /etc/network/interfaces.d/*
```

## 12.3.2. DHCP IPAM <a href="#pvesdn_install_dhcp_ipam" id="pvesdn_install_dhcp_ipam"></a>

内置 *PVE* IP 地址管理栈的 DHCP 集成目前使用 `dnsmasq` 发放 DHCP 租约。目前需要选择启用此功能。

要使用此功能，需要在每个节点上安装 `dnsmasq` 软件包：

```text
apt update
apt install dnsmasq
# disable default instance
systemctl disable --now dnsmasq
```

## 12.3.3. FRRouting <a href="#pvesdn_install_frrouting" id="pvesdn_install_frrouting"></a>

Proxmox VE SDN 协议栈使用 [FRRouting](https://frrouting.org/) 项目实现高级设置。目前需要选择启用此功能。

要使用 SDN 路由集成，需要在所有节点上安装 `frr-pythontools` 软件包：

```text
apt update
apt install frr-pythontools
```

然后在所有节点上启用 frr 服务：

```text
systemctl enable frr.service
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
