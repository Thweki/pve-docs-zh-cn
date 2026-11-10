# 12.13. DNS <a href="#pvesdn_config_dns" id="pvesdn_config_dns"></a>

Proxmox VE SDN 中的 DNS 插件用于定义 DNS API 服务器，以注册主机名和 IP 地址。DNS 配置关联一个或多个区域，为某个区域配置的所有子网 IP 提供 DNS 注册。

## 12.13.1. PowerDNS 插件 <a href="#pvesdn_dns_plugin_powerdns" id="pvesdn_dns_plugin_powerdns"></a>

[https://doc.powerdns.com/authoritative/http-api/index.html](https://doc.powerdns.com/authoritative/http-api/index.html)

需要在 PowerDNS 配置中启用 Web 服务器和 API：

```text
api=yes
api-key=arandomgeneratedstring
webserver=yes
webserver-port=8081
```

PowerDNS 配置选项为：

**url**

REST API 端点：[http://yourpowerdnserver.domain.com:8081/api/v1/servers/localhost](http://yourpowerdnserver.domain.com:8081/api/v1/servers/localhost)

**key**

API 访问密钥

**ttl**

记录的默认 TTL

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
