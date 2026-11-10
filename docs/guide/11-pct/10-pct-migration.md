# 11.10. Migration <a href="#pct_migration" id="pct_migration"></a>

如果你有集群，可以使用以下命令迁移容器

```text
# pct migrate <ctid> <target>
```

只要容器处于离线状态，此方法就有效。如果定义了本地卷或挂载点，并且目标宿主机上定义了相同的存储，迁移会通过网络将内容复制到目标宿主机。

由于技术限制，正在运行的容器无法进行在线迁移。你可以执行重启迁移，即关闭容器，将其移动，然后在目标节点上重新启动。由于容器非常轻量，这通常只会造成几百毫秒的停机时间。

A restart migration can be done through the web interface or by using the `--restart` flag with the `pct migrate` command.

重启迁移会关闭容器，并在指定的超时时间（默认为 180 秒）后强制终止它。随后会像离线迁移一样迁移容器，完成后在目标节点上启动容器。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
