# 6.1. POSIX Compatibility <a href="#_posix_compatibility" id="_posix_compatibility"></a>

The file system is based on FUSE, so the behavior is POSIX like. But some feature are simply not implemented, because we do not need them:

- You can just generate normal files and directories, but no symbolic links, …
- You can’t rename non-empty directories (because this makes it easier to guarantee that VMIDs are unique).
- You can’t change file permissions (permissions are based on paths)
- `O_EXCL` creates were not atomic (like old NFS)
- `O_TRUNC` creates are not atomic (FUSE restriction)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
