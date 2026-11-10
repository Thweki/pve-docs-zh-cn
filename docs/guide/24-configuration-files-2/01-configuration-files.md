# 24.1. 常规 <a href="#configuration_files" id="configuration_files"></a>

Proxmox VE 中的大多数配置文件位于[共享集群文件系统](../06-pmxcfs/README.md)中，该文件系统挂载在 `/etc/pve`。也存在例外，例如 `/etc/vzdump.conf` 中节点特定的备份配置文件。

通常，配置文件中的属性派生自 JSON Schema，相关 API 端点也使用同一模式。

## 24.1.1. 属性名称的大小写 <a href="#configuration_files_casing" id="configuration_files_casing"></a>

历史上，较长的属性（及子属性）通常使用 `snake_case`，或连写为一个单词。这很可能是因为 Proxmox VE 软件栈主要使用 Perl 编程语言开发，在 Perl 中访问使用 `kebab-case` 的属性时需要额外的引号；同时，早期开发时对风格的约束较少，因此不同开发者使用不同的约定。

对于新属性，首选方式为 `kebab-case`，并计划为现有的 `snake_case` 属性引入别名。从长远来看，计划将 API、CLI 和使用中的配置文件切换为 `kebab-case`，同时在恢复配置时保持向后兼容。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
