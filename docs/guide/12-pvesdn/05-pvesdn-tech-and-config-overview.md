# 12.5. 技术与配置 <a href="#pvesdn_tech_and_config_overview" id="pvesdn_tech_and_config_overview"></a>

Proxmox VE 软件定义网络实现尽可能使用标准 Linux 网络功能。这是因为现代 Linux 网络功能几乎能够满足功能完整的 SDN 实现的全部需求，同时避免添加外部依赖，并减少可能发生故障的组件总数。

Proxmox VE SDN 配置位于 `/etc/pve/sdn`，通过 Proxmox VE [配置文件系统](../06-pmxcfs/README.md) 与所有其他集群节点共享。这些配置会转换为管理底层网络协议栈的工具（例如 `ifupdown2` 或 `frr`）各自所需的配置格式。

新更改不会立即应用，而是先记录为待处理状态。然后可以在 Web 界面的主 *SDN* 概览面板中一次性应用一组不同的更改。此系统允许将多项更改作为单个原子更改推出。

SDN 通过 *.running-config* 和 *.version* 文件跟踪已推出的状态，这些文件位于 */etc/pve/sdn*。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
