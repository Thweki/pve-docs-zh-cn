# 15.9. Error Recovery <a href="#ha_manager_error_recovery" id="ha_manager_error_recovery"></a>

如果在所有尝试之后仍无法恢复服务状态，服务将被置于错误状态。在此状态下，HA 堆栈将不再对该服务执行任何操作。唯一的退出方法是禁用该服务：

```text
# ha-manager set vm:100 --state disabled
```

这也可以在 Web 界面中完成。

要从错误状态中恢复，应执行以下操作：

- 使资源恢复到安全且一致的状态（例如：如果无法停止服务，则终止其进程）
- 禁用资源以清除错误标志
- 修复导致这些故障的错误
- **在**修复所有错误后，可以请求重新启动该服务

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
