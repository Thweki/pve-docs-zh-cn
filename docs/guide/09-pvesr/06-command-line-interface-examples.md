# 9.6. 命令行界面示例 <a href="#_command_line_interface_examples" id="_command_line_interface_examples"></a>

为 ID 为 100 的客户机创建一个每 5 分钟运行一次、带宽限制为 10 Mbps（兆字节每秒）的复制作业。

```text
# pvesr create-local-job 100-0 pve1 --schedule "*/5" --rate 10
```

禁用 ID 为 `100-0` 的活动作业。

```text
# pvesr disable 100-0
```

启用 ID 为 `100-0` 的已停用作业。

```text
# pvesr enable 100-0
```

将 ID 为 `100-0` 的作业的计划间隔更改为每小时一次。

```text
# pvesr update 100-0 --schedule '*/00'
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
