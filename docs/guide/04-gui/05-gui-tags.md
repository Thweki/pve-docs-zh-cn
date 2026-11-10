# 4.5. Tags <a href="#gui_tags" id="gui_tags"></a>

[![screenshot/gui-qemu-summary-tags-edit.png](../../assets/screenshot-gui-qemu-summary-tags-edit-png-c6e85f4f644b.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-qemu-summary-tags-edit.png)

出于组织管理的目的，可以为客户机设置 `tags`。目前，它们仅用于向用户提供信息。标签在 Web 界面的两个位置显示：在 `Resource Tree` 中，以及选中客户机时的状态行中。

点击客户机状态行中的 `pencil` 图标，即可添加、编辑和移除标签。按 `+` 按钮可添加多个标签，按 `-` 按钮可将其移除。要保存或取消更改，可分别使用 `✓` 和 `x` 按钮。

也可以通过 CLI 设置标签，多个标签之间用分号分隔。例如：

```text
# qm set ID --tags 'myfirsttag;mysecondtag'
```

## 4.5.1. Style Configuration <a href="#_style_configuration" id="_style_configuration"></a>

[![screenshot/gui-datacenter-tag-style.png](../../assets/screenshot-gui-datacenter-tag-style-png-f3ff2cf9dfd8.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-tag-style.png)

默认情况下，标签颜色通过确定性方式根据其文本生成。可以自定义颜色、在资源树中的形状和大小写敏感性，以及标签的排序方式。可在 Web 界面的 *数据中心 → 选项 → 标签样式覆盖* 下进行配置。也可以通过 CLI 完成。例如：

```text
# pvesh set /cluster/options --tag-style color-map=example:000000:FFFFFF
```

将标签 `example` 的背景颜色设置为黑色（#000000），文本颜色设置为白色（#FFFFFF）。

## 4.5.2. Permissions <a href="#_permissions" id="_permissions"></a>

[![screenshot/gui-datacenter-options.png](../../assets/screenshot-gui-datacenter-options-png-535789a52e69.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-options.png)

By default, users with the privilege `VM.Config.Options` on a guest (`/vms/ID`) can set any tags they want (see [Permission Management](../14-user-management/07-pveum-permission-management.md)). If you want to restrict this behavior, appropriate permissions can be set under *Datacenter → Options → User Tag Access*:

- `free`: users are not restricted in setting tags (Default)
- `list`: users can set tags based on a predefined list of tags
- `existing`: like list but users can also use already existing tags
- `none`: users are restricted from using tags

同样也可以通过 CLI 完成此操作。

Note that a user with the `Sys.Modify` privileges on `/` is always able to set or delete any tags, regardless of the settings here. Additionally, there is a configurable list of `registered tags` which can only be added and removed by users with the privilege `Sys.Modify` on `/`. The list of registered tags can be edited under *Datacenter → Options → Registered Tags* or via the CLI.

有关确切选项以及如何在 CLI 中调用它们的更多详细信息，请参见[数据中心配置](../24-configuration-files-2/02-datacenter-configuration-file.md)。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
