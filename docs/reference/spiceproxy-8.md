# spiceproxy(8)

## 名称 <a href="#name" id="name"></a>

spiceproxy \- SPICE 代理服务

## 概要 <a href="#synopsis" id="synopsis"></a>

### **spiceproxy** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_spiceproxy" id="cli_spiceproxy"></a>

### **spiceproxy help** `[OPTIONS]` <a href="#cli_spiceproxy_help" id="cli_spiceproxy_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### **spiceproxy restart** <a href="#cli_spiceproxy_restart" id="cli_spiceproxy_restart"></a>

重启守护进程（如果未运行则启动）。

### **spiceproxy start** `[OPTIONS]` <a href="#cli_spiceproxy_start" id="cli_spiceproxy_start"></a>

启动守护进程。

**`--debug` `<boolean>`（*默认 \=* `0`）**

调试模式，保持在前台运行

### **spiceproxy status** <a href="#cli_spiceproxy_status" id="cli_spiceproxy_status"></a>

获取守护进程状态。

### **spiceproxy stop** <a href="#cli_spiceproxy_stop" id="cli_spiceproxy_stop"></a>

停止守护进程。

## 描述 <a href="#description" id="description"></a>

[SPICE](http://www.spice-space.org)（独立计算环境简单协议）是一种开放的远程计算解决方案，为客户端提供对远程显示器和设备（例如键盘、鼠标、音频）的访问。主要用途是远程访问虚拟机和容器。

此守护进程监听 TCP 端口 3128，并实现 HTTP 代理，将 SPICE 客户端的 *CONNECT* 请求转发到正确的 Proxmox VE 虚拟机。它以用户 `www-data` 身份运行，权限非常有限。

## 基于宿主机的访问控制 <a href="#host_based_access_control" id="host_based_access_control"></a>

可以配置类似“apache2”的访问控制列表。各项值从文件 `/etc/default/pveproxy` 读取。详情参阅 `pveproxy` 文档。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/spiceproxy.8.html) · 版本 9.2.13 · 非官方中文翻译。
