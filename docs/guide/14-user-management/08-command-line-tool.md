# 14.8. Command-line Tool <a href="#_command_line_tool" id="_command_line_tool"></a>

Most users will simply use the GUI to manage users. But there is also a fully featured command-line tool called `pveum` (short for “**P**roxmox **VE** **U**ser **M**anager”). Please note that all Proxmox VE command-line tools are wrappers around the API, so you can also access those functions through the REST API.

Here are some simple usage examples. To show help, type:

```text
 pveum
```

or (to show detailed help about a specific command)

```text
 pveum help user add
```

Create a new user:

```text
 pveum user add testuser@pve -comment "Just a test"
```

Set or change the password (not all realms support this):

```text
 pveum passwd testuser@pve
```

Disable a user:

```text
 pveum user modify testuser@pve -enable 0
```

Create a new group:

```text
 pveum group add testgroup
```

Create a new role:

```text
 pveum role add PVE_Power-only -privs "VM.PowerMgmt VM.Console"
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
