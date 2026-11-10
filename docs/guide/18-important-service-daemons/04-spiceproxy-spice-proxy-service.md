# 18.4. spiceproxy \- SPICE 代理服务 <a href="#spiceproxy_spice_proxy_service" id="spiceproxy_spice_proxy_service"></a>

[SPICE](http://www.spice-space.org)（独立计算环境简单协议）是一种开放的远程计算解决方案，为客户端提供对远程显示器和设备（例如键盘、鼠标、音频）的访问。主要用途是远程访问虚拟机和容器。

此守护进程监听 TCP 端口 3128，并实现 HTTP 代理，将 SPICE 客户端的 *CONNECT* 请求转发到正确的 Proxmox VE 虚拟机。它以用户 `www-data` 身份运行，权限非常有限。

## 18.4.1. 基于宿主机的访问控制 <a href="#host_based_access_control" id="host_based_access_control"></a>

可以配置类似“apache2”的访问控制列表。各项值从文件 `/etc/default/pveproxy` 读取。详情参阅 `pveproxy` 文档。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
