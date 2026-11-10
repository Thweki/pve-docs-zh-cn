# 12.12. IPAM <a href="#pvesdn_config_ipam" id="pvesdn_config_ipam"></a>

IP 地址管理（IPAM）工具管理网络上客户端的 IP 地址。Proxmox VE 中的 SDN 使用 IPAM，例如为新客户机查找空闲 IP 地址。

单个 IPAM 实例可关联一个或多个区域。

## 12.12.1. PVE IPAM 插件 <a href="#pvesdn_ipam_plugin_pveipam" id="pvesdn_ipam_plugin_pveipam"></a>

Proxmox VE 集群的默认内置 IPAM。

可以通过数据中心配置的 SDN 部分中的 IPAM 面板查看 PVE IPAM 插件的当前状态。此 UI 可用于创建、更新和删除 IP 映射。与 [DHCP 功能](14-pvesdn-config-dhcp.md) 结合使用时尤其方便。

如果使用 DHCP，可以通过 IPAM 面板为特定虚拟机创建或编辑租约，从而更改通过 DHCP 分配的 IP。编辑使用 DHCP 的虚拟机的 IP 时，必须确保强制客户机获取新的 DHCP 租约。通常可以通过重新加载客户机的网络协议栈或重启客户机来实现。

## 12.12.2. NetBox IPAM 插件 <a href="#pvesdn_ipam_plugin_netbox" id="pvesdn_ipam_plugin_netbox"></a>

[NetBox](https://github.com/netbox-community/netbox) 是开源的 IP 地址管理（IPAM）和数据中心基础设施管理（DCIM）工具。

要将 NetBox 与 Proxmox VE SDN 集成，请按照此处说明在 NetBox 中创建 API 令牌：[https://docs.netbox.dev/en/stable/integrations/rest-api/#tokens](https://docs.netbox.dev/en/stable/integrations/rest-api/#tokens)

NetBox 配置属性为：

**URL**

NetBox REST API 端点：`http://yournetbox.domain.com/api`

**令牌**

API 访问令牌

**指纹**

NetBox API 的 SHA-256 指纹。使用默认证书时可通过 `openssl x509 -in /etc/ssl/certs/netbox.crt -noout -fingerprint -sha256` 获取。

## 12.12.3. phpIPAM 插件 <a href="#pvesdn_ipam_plugin_phpipam" id="pvesdn_ipam_plugin_phpipam"></a>

在 [phpIPAM](https://phpipam.net/) 中，需要创建一个“应用程序”，并向该应用程序添加具有管理员权限的 API 令牌。

phpIPAM 配置属性为：

**URL**

REST-API 端点：`http://phpipam.domain.com/api/<appname>/`

**令牌**

API 访问令牌

**分区**

整数 ID。在 phpIPAM 中，分区是一组子网。默认安装为客户使用 `sectionid=1`。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
