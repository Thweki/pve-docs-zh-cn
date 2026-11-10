# 12.13. DNS <a href="#pvesdn_config_dns" id="pvesdn_config_dns"></a>

The DNS plugin in Proxmox VE SDN is used to define a DNS API server for registration of your hostname and IP address. A DNS configuration is associated with one or more zones, to provide DNS registration for all the subnet IPs configured for a zone.

## 12.13.1. PowerDNS Plugin <a href="#pvesdn_dns_plugin_powerdns" id="pvesdn_dns_plugin_powerdns"></a>

[https://doc.powerdns.com/authoritative/http-api/index.html](https://doc.powerdns.com/authoritative/http-api/index.html)

You need to enable the web server and the API in your PowerDNS config:

```text
api=yes
api-key=arandomgeneratedstring
webserver=yes
webserver-port=8081
```

The PowerDNS configuration options are:

**url**

The REST API endpoint: [http://yourpowerdnserver.domain.com:8081/api/v1/servers/localhost](http://yourpowerdnserver.domain.com:8081/api/v1/servers/localhost)

**key**

An API access key

**ttl**

The default TTL for records

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
