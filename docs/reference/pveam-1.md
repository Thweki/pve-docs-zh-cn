# pveam(1)

## 名称 <a href="#name" id="name"></a>

pveam \- Proxmox VE 设备模板管理器

## 概要 <a href="#synopsis" id="synopsis"></a>

### **pveam** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveam" id="cli_pveam"></a>

### **pveam available** `[OPTIONS]` <a href="#cli_pveam_available" id="cli_pveam_available"></a>

列出可用模板。

**`--section` `<mail | system | turnkeylinux>`**

将列表限制为指定部分。

### **pveam download** `<storage> <template>` <a href="#cli_pveam_download" id="cli_pveam_download"></a>

下载设备模板。

**`<storage>`: `<storage ID>`**

用于保存模板的存储

**`<template>`: `<string>`**

要下载的模板

### **pveam help** `[OPTIONS]` <a href="#cli_pveam_help" id="cli_pveam_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### **pveam list** `<storage>` <a href="#cli_pveam_list" id="cli_pveam_list"></a>

获取存储上的所有模板列表

**`<storage>`: `<storage ID>`**

仅列出指定存储上的模板

### **pveam remove** `<template_path>` <a href="#cli_pveam_remove" id="cli_pveam_remove"></a>

移除模板。

**`<template_path>`: `<string>`**

要移除的模板。

### **pveam update** <a href="#cli_pveam_update" id="cli_pveam_update"></a>

更新容器模板数据库。

## 描述 <a href="#description" id="description"></a>

管理容器镜像的命令行工具。使用示例请参阅 `man pct`。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pveam.1.html) · 版本 9.2.13 · 非官方中文翻译。
