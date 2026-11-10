# pvestatd(8)

## NAME <a href="#_name" id="_name"></a>

pvestatd \- PVE Status Daemon

## SYNOPSIS <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pvestatd"></a>



**pvestatd** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvestatd_help"></a>



**pvestatd help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvestatd_restart"></a>



**pvestatd restart**

Restart the daemon (or start if not running).

<a id="cli_pvestatd_start"></a>



**pvestatd start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>` (*default \=* `0`)**

Debug mode \- stay in foreground

<a id="cli_pvestatd_status"></a>



**pvestatd status**

Get daemon status.

<a id="cli_pvestatd_stop"></a>



**pvestatd stop**

Stop the daemon.

## DESCRIPTION <a href="#_description" id="_description"></a>

This daemon queries the status of VMs, storages and containers at regular intervals. The result is sent to all nodes in the cluster.

## Copyright and Disclaimer <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvestatd.8.html) · 版本 9.2.13 · 非官方中文翻译。
