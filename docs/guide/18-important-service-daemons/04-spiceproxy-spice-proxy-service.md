# 18.4. spiceproxy - SPICE Proxy Service <a href="#_spiceproxy_spice_proxy_service" id="_spiceproxy_spice_proxy_service"></a>

[SPICE](http://www.spice-space.org) (the Simple Protocol for Independent Computing Environments) is an open remote computing solution, providing client access to remote displays and devices (e.g. keyboard, mouse, audio). The main use case is to get remote access to virtual machines and container.

This daemon listens on TCP port 3128, and implements an HTTP proxy to forward *CONNECT* request from the SPICE client to the correct Proxmox VE VM. It runs as user `www-data` and has very limited permissions.

## 18.4.1. Host based Access Control <a href="#_host_based_access_control" id="_host_based_access_control"></a>

It is possible to configure "apache2" like access control lists. Values are read from file `/etc/default/pveproxy`. See `pveproxy` documentation for details.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
