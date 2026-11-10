# 22.12. **pveam** \- Proxmox VE Appliance Manager <a href="#_strong_pveam_strong_proxmox_ve_appliance_manager" id="_strong_pveam_strong_proxmox_ve_appliance_manager"></a>

<a id="cli_pveam"></a>



**pveam** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pveam_available"></a>



**pveam available** `[OPTIONS]`

List available templates.

**`--section` `<mail | system | turnkeylinux>`**

Restrict list to specified section.

<a id="cli_pveam_download"></a>



**pveam download** `<storage> <template>`

Download appliance templates.

**`<storage>`: `<storage ID>`**

The storage where the template will be stored

**`<template>`: `<string>`**

The template which will downloaded

<a id="cli_pveam_help"></a>



**pveam help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pveam_list"></a>



**pveam list** `<storage>`

Get list of all templates on storage

**`<storage>`: `<storage ID>`**

Only list templates on specified storage

<a id="cli_pveam_remove"></a>



**pveam remove** `<template_path>`

Remove a template.

**`<template_path>`: `<string>`**

The template to remove.

<a id="cli_pveam_update"></a>



**pveam update**

Update Container Template Database.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
