# 22.4. **pvesubscription** \- Proxmox VE 订阅管理器 <a href="#strong_pvesubscription_strong_proxmox_ve_subscription_manager" id="strong_pvesubscription_strong_proxmox_ve_subscription_manager"></a>

## **pvesubscription** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvesubscription" id="cli_pvesubscription"></a>

## **pvesubscription delete** <a href="#cli_pvesubscription_delete" id="cli_pvesubscription_delete"></a>

删除此节点的订阅密钥。

## **pvesubscription get** <a href="#cli_pvesubscription_get" id="cli_pvesubscription_get"></a>

读取订阅信息。

## **pvesubscription help** `[OPTIONS]` <a href="#cli_pvesubscription_help" id="cli_pvesubscription_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvesubscription set** `<key>` <a href="#cli_pvesubscription_set" id="cli_pvesubscription_set"></a>

设置订阅密钥。

**`<key>`: `\s*pve([1248])([cbsp])-(arm-)?[0-9a-f]{10}\s*`**

Proxmox VE 订阅密钥

## **pvesubscription set-offline-key** `<data>` <a href="#cli_pvesubscription_set-offline-key" id="cli_pvesubscription_set-offline-key"></a>

仅供内部使用！要设置离线密钥，请改用 proxmox-offline-mirror-helper 软件包。

**`<data>`: `<string>`**

已签名的订阅信息数据块

## **pvesubscription update** `[OPTIONS]` <a href="#cli_pvesubscription_update" id="cli_pvesubscription_update"></a>

更新订阅信息。

**`--force` `<boolean>`（*默认 \=* `0`）**

始终连接服务器，即使本地缓存仍有效。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
