# 14.8. 命令行工具 <a href="#command_line_tool" id="command_line_tool"></a>

大多数用户只需使用 GUI 管理用户。不过也有一个功能完整的命令行工具，名为 `pveum`（“**P**roxmox **VE** **U**ser **M**anager”的缩写，即 Proxmox VE 用户管理器）。请注意，所有 Proxmox VE 命令行工具都是 API 的封装，因此也可以通过 REST API 访问这些功能。

以下是一些简单用法示例。要显示帮助，输入：

```text
 pveum
```

或（显示特定命令的详细帮助）

```text
 pveum help user add
```

创建新用户：

```text
 pveum user add testuser@pve -comment "Just a test"
```

设置或更改密码（并非所有认证域都支持）：

```text
 pveum passwd testuser@pve
```

禁用用户：

```text
 pveum user modify testuser@pve -enable 0
```

创建新组：

```text
 pveum group add testgroup
```

创建新角色：

```text
 pveum role add PVE_Power-only -privs "VM.PowerMgmt VM.Console"
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
