# 12.8. 子网 <a href="#pvesdn_config_subnet" id="pvesdn_config_subnet"></a>

子网定义由 CIDR 网络地址描述的特定 IP 范围。每个 VNet 可以具有一个或多个子网。

子网可用于：

- 限制可在特定 VNet 上定义的 IP 地址
- 在三层区域中的 VNet 上分配路由/网关
- 在三层区域中的 VNet 上启用 SNAT
- 通过 IPAM 插件为虚拟客户机（虚拟机或容器）自动分配 IP
- 通过 DNS 插件进行 DNS 注册

如果 IPAM 服务器与子网区域关联，子网前缀将自动注册到 IPAM 中。

子网配置选项：

**ID**

CIDR 网络地址，例如 10.0.0.0/8

**网关**

网络默认网关的 IP 地址。在三层区域（Simple/EVPN 插件）中，它将部署在 VNet 上。

**SNAT**

启用源 NAT，将数据包转发到节点的传出接口，使 VNet 内的虚拟机能够连接外部网络。在 EVPN 区域中，转发在 EVPN 网关节点上完成。可选。

**DNS 区域前缀**

向域名注册添加前缀，例如 \<hostname\>.prefix.\<domain\>。可选。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
