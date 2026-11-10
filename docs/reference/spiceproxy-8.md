# spiceproxy(8)

## 名称 <a href="#_name" id="_name"></a>

spiceproxy \- SPICE Proxy Service

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_spiceproxy"></a>



**spiceproxy** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_spiceproxy_help"></a>



**spiceproxy help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_spiceproxy_restart"></a>



**spiceproxy restart**

Restart the daemon (or start if not running).

<a id="cli_spiceproxy_start"></a>



**spiceproxy start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>`（*默认 \=* `0`）**

Debug mode \- stay in foreground

<a id="cli_spiceproxy_status"></a>



**spiceproxy status**

Get daemon status.

<a id="cli_spiceproxy_stop"></a>



**spiceproxy stop**

Stop the daemon.

## 描述 <a href="#_description" id="_description"></a>

[SPICE](http://www.spice-space.org) (the Simple Protocol for Independent Computing Environments) is an open remote computing solution, providing client access to remote displays and devices (e.g. keyboard, mouse, audio). The main use case is to get remote access to virtual machines and container.

This daemon listens on TCP port 3128, and implements an HTTP proxy to forward *CONNECT* request from the SPICE client to the correct Proxmox VE VM. It runs as user `www-data` and has very limited permissions.

## Host based Access Control <a href="#_host_based_access_control" id="_host_based_access_control"></a>

It is possible to configure "apache2" like access control lists. Values are read from file `/etc/default/pveproxy`. See `pveproxy` documentation for details.

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/spiceproxy.8.html) · 版本 9.2.13 · 非官方中文翻译。
