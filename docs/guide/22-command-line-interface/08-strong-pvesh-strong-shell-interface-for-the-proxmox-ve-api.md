# 22.8. **pvesh** \- Proxmox VE API 的 Shell 接口 <a href="#strong_pvesh_strong_shell_interface_for_the_proxmox_ve_api" id="strong_pvesh_strong_shell_interface_for_the_proxmox_ve_api"></a>

## **pvesh** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesh" id="cli_pvesh"></a>

## **pvesh create** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_create" id="cli_pvesh_create"></a>

对 \<api\_path\> 调用 API POST。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

## **pvesh delete** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_delete" id="cli_pvesh_delete"></a>

对 \<api\_path\> 调用 API DELETE。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

## **pvesh get** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_get" id="cli_pvesh_get"></a>

对 \<api\_path\> 调用 API GET。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

## **pvesh help** `[OPTIONS]` <a href="#cli_pvesh_help" id="cli_pvesh_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvesh ls** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_ls" id="cli_pvesh_ls"></a>

列出 \<api\_path\> 下的子对象。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

## **pvesh set** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvesh_set" id="cli_pvesh_set"></a>

对 \<api\_path\> 调用 API PUT。

**`<api_path>`: `<string>`**

API 路径。

**`--noproxy` `<boolean>`**

禁用自动代理。

## **pvesh usage** `<api_path>` `[OPTIONS]` <a href="#cli_pvesh_usage" id="cli_pvesh_usage"></a>

打印 \<api\_path\> 的 API 使用信息。

**`<api_path>`: `<string>`**

API 路径。

**`--command` `<create | delete | get | set>`**

API 命令。

**`--returns` `<boolean>`**

包含返回数据的模式定义。

**`--verbose` `<boolean>`**

详细输出格式。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
