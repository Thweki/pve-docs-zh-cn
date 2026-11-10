# 16.12. 文件排除 <a href="#file_exclusions" id="file_exclusions"></a>

{% hint style="info" %}
此选项仅适用于容器备份。
{% endhint %}

`vzdump` 默认跳过以下文件（使用选项 `--stdexcludes 0` 禁用）

```text
/tmp/?*
/var/tmp/?*
/var/run/?*pid
```

也可以手动指定（额外的）排除路径，例如：

```text
# vzdump 777 --exclude-path /tmp/ --exclude-path '/var/foo*'
```

排除目录 `/tmp/` 以及名为 `/var/foo`、`/var/foobar` 等的任何文件或目录。

{% hint style="warning" %}
对于备份到 Proxmox Backup Server（PBS）的备份和 `suspend` 模式备份，以斜杠结尾的模式会匹配目录，但不匹配文件。另一方面，对于非 PBS 的 `snapshot` 模式和 `stop` 模式备份，以斜杠结尾的模式目前完全不会匹配，因为 `tar` 命令不支持这种模式。
{% endhint %}

不以 `/` 开头的路径不会锚定到容器的根目录，而是相对于任意子目录进行匹配。例如：

```text
# vzdump 777 --exclude-path bar
```

排除名为 `/bar`、`/var/bar`、`/var/foo/bar` 等的任何文件或目录，但不排除 `/bar2`。

配置文件也保存在备份归档中（位于 `./etc/vzdump/`），并会得到正确恢复。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
