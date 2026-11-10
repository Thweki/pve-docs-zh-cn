# 22.8. **pvesh** \- Shell interface for the Proxmox VE API <a href="#_strong_pvesh_strong_shell_interface_for_the_proxmox_ve_api" id="_strong_pvesh_strong_shell_interface_for_the_proxmox_ve_api"></a>

<a id="cli_pvesh"></a>



**pvesh** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvesh_create"></a>



**pvesh create** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API POST on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_delete"></a>



**pvesh delete** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API DELETE on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_get"></a>



**pvesh get** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API GET on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_help"></a>



**pvesh help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvesh_ls"></a>



**pvesh ls** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

List child objects on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_set"></a>



**pvesh set** `<api_path>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Call API PUT on \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--noproxy` `<boolean>`**

Disable automatic proxying.

<a id="cli_pvesh_usage"></a>



**pvesh usage** `<api_path>` `[OPTIONS]`

print API usage information for \<api\_path\>.

**`<api_path>`: `<string>`**

API path.

**`--command` `<create | delete | get | set>`**

API command.

**`--returns` `<boolean>`**

Including schema for returned data.

**`--verbose` `<boolean>`**

详细输出格式。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
