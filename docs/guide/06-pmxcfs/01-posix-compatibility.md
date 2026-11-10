# 6.1. POSIX Compatibility <a href="#_posix_compatibility" id="_posix_compatibility"></a>

该文件系统基于 FUSE，因此其行为类似于 POSIX。但有些功能并未实现，因为我们不需要它们：

- 只能创建普通文件和目录，不能创建符号链接，……
- 不能重命名非空目录（因为这样可以更容易地保证 VMID 的唯一性）。
- 不能更改文件权限（权限基于路径）
- `O_EXCL` 创建操作不是原子的（与旧版 NFS 类似）
- `O_TRUNC` 创建操作不是原子的（FUSE 限制）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
