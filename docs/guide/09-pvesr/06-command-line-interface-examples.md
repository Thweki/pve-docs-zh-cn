# 9.6. Command-line Interface Examples <a href="#_command_line_interface_examples" id="_command_line_interface_examples"></a>

Create a replication job which runs every 5 minutes with a limited bandwidth of 10 Mbps (megabytes per second) for the guest with ID 100.

```text
# pvesr create-local-job 100-0 pve1 --schedule "*/5" --rate 10
```

Disable an active job with ID `100-0`.

```text
# pvesr disable 100-0
```

Enable a deactivated job with ID `100-0`.

```text
# pvesr enable 100-0
```

Change the schedule interval of the job with ID `100-0` to once per hour.

```text
# pvesr update 100-0 --schedule '*/00'
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
