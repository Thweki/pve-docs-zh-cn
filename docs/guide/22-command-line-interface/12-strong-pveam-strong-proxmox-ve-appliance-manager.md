# 22.12. **pveam** \- Proxmox VE 设备模板管理器 <a href="#strong_pveam_strong_proxmox_ve_appliance_manager" id="strong_pveam_strong_proxmox_ve_appliance_manager"></a>

## **pveam** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveam" id="cli_pveam"></a>

## **pveam available** `[OPTIONS]` <a href="#cli_pveam_available" id="cli_pveam_available"></a>

列出可用模板。

**`--section` `<mail | system | turnkeylinux>`**

将列表限制为指定部分。

## **pveam download** `<storage> <template>` <a href="#cli_pveam_download" id="cli_pveam_download"></a>

下载设备模板。

**`<storage>`: `<storage ID>`**

用于保存模板的存储

**`<template>`: `<string>`**

要下载的模板

## **pveam help** `[OPTIONS]` <a href="#cli_pveam_help" id="cli_pveam_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pveam list** `<storage>` <a href="#cli_pveam_list" id="cli_pveam_list"></a>

获取存储上的所有模板列表

**`<storage>`: `<storage ID>`**

仅列出指定存储上的模板

## **pveam remove** `<template_path>` <a href="#cli_pveam_remove" id="cli_pveam_remove"></a>

移除模板。

**`<template_path>`: `<string>`**

要移除的模板。

## **pveam update** <a href="#cli_pveam_update" id="cli_pveam_update"></a>

更新容器模板数据库。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
