# 12.3. Installation <a href="#pvesdn_installation" id="pvesdn_installation"></a>

## 12.3.1. SDN Core <a href="#_sdn_core" id="_sdn_core"></a>

Since Proxmox VE 8.1 the core Software-Defined Network (SDN) packages are installed by default.

If you upgrade from an older version, you need to install the `libpve-network-perl` package on every node:

```text
apt update
apt install libpve-network-perl
```

{% hint style="info" %}
Proxmox VE version 7.0 and above have the `ifupdown2` package installed by default. If you originally installed your system with an older version, you need to explicitly install the `ifupdown2` package.
{% endhint %}

After installation, you need to ensure that the following line is present at the end of the `/etc/network/interfaces` configuration file on all nodes, so that the SDN configuration gets included and activated.

```text
source /etc/network/interfaces.d/*
```

## 12.3.2. DHCP IPAM <a href="#pvesdn_install_dhcp_ipam" id="pvesdn_install_dhcp_ipam"></a>

The DHCP integration into the built-in *PVE* IP Address Management stack currently uses `dnsmasq` for giving out DHCP leases. This is currently opt-in.

To use that feature you need to install the `dnsmasq` package on every node:

```text
apt update
apt install dnsmasq
# disable default instance
systemctl disable --now dnsmasq
```

## 12.3.3. FRRouting <a href="#pvesdn_install_frrouting" id="pvesdn_install_frrouting"></a>

The Proxmox VE SDN stack uses the [FRRouting](https://frrouting.org/) project for advanced setups. This is currently opt-in.

To use the SDN routing integration you need to install the `frr-pythontools` package on all nodes:

```text
apt update
apt install frr-pythontools
```

Then enable the frr service on all nodes:

```text
systemctl enable frr.service
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
