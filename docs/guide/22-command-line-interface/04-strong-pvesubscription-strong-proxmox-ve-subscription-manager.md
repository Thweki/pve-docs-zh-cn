# 22.4. **pvesubscription** \- Proxmox VE Subscription Manager <a href="#_strong_pvesubscription_strong_proxmox_ve_subscription_manager" id="_strong_pvesubscription_strong_proxmox_ve_subscription_manager"></a>

<a id="cli_pvesubscription"></a>



**pvesubscription** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvesubscription_delete"></a>



**pvesubscription delete**

Delete subscription key of this node.

<a id="cli_pvesubscription_get"></a>



**pvesubscription get**

Read subscription info.

<a id="cli_pvesubscription_help"></a>



**pvesubscription help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvesubscription_set"></a>



**pvesubscription set** `<key>`

Set subscription key.

**`<key>`: `\s*pve([1248])([cbsp])-(arm-)?[0-9a-f]{10}\s*`**

Proxmox VE subscription key

<a id="cli_pvesubscription_set-offline-key"></a>



**pvesubscription set-offline-key** `<data>`

Internal use only! To set an offline key, use the package proxmox-offline-mirror-helper instead.

**`<data>`: `<string>`**

A signed subscription info blob

<a id="cli_pvesubscription_update"></a>



**pvesubscription update** `[OPTIONS]`

Update subscription info.

**`--force` `<boolean>` (*default \=* `0`)**

Always connect to server, even if local cache is still valid.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
