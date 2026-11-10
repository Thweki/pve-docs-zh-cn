# 22.13. **pvecm** \- Proxmox VE 集群管理器 <a href="#strong_pvecm_strong_proxmox_ve_cluster_manager" id="strong_pvecm_strong_proxmox_ve_cluster_manager"></a>

## **pvecm** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvecm" id="cli_pvecm"></a>

## **pvecm add** `<hostname>` `[OPTIONS]` <a href="#cli_pvecm_add" id="cli_pvecm_add"></a>

将当前节点加入现有集群。

**`<hostname>`: `<string>`**

现有集群成员的主机名（或 IP）。

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

证书 SHA 256 指纹。

**`--force` `<boolean>`**

如果节点已存在，则不抛出错误。

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

单个 corosync 链路的地址和优先级信息。（最多支持 8 个链路；link0..link7）

**`--nodeid` `<integer> (1 - N)`**

此节点的节点 ID。

**`--use_ssh` `<boolean>`**

始终使用 SSH 加入，即使对端可以通过 API 完成。

**`--votes` `<integer> (0 - N)`**

此节点的票数

## **pvecm addnode** `<node>` `[OPTIONS]` <a href="#cli_pvecm_addnode" id="cli_pvecm_addnode"></a>

将节点添加到集群配置。此调用供内部使用。

**`<node>`: `<string>`**

集群节点名称。

**`--apiversion` `<integer>`**

新节点的 JOIN\_API\_VERSION。

**`--force` `<boolean>`**

如果节点已存在，则不抛出错误。

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

单个 corosync 链路的地址和优先级信息。（最多支持 8 个链路；link0..link7）

**`--new_node_ip` `<string>`**

要添加节点的 IP 地址。未提供链路时用作回退值。

**`--nodeid` `<integer> (1 - N)`**

此节点的节点 ID。

**`--votes` `<integer> (0 - N)`**

此节点的票数

## **pvecm apiver** <a href="#cli_pvecm_apiver" id="cli_pvecm_apiver"></a>

返回此节点上可用的集群加入 API 版本。

## **pvecm create** `<clustername>` `[OPTIONS]` <a href="#cli_pvecm_create" id="cli_pvecm_create"></a>

生成新的集群配置。如果未提供链路，则默认将本地 IP 地址用作 link0。

**`<clustername>`: `<string>`**

集群名称。

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

单个 corosync 链路的地址和优先级信息。（最多支持 8 个链路；link0..link7）

**`--nodeid` `<integer> (1 - N)`**

此节点的节点 ID。

**`--token-coefficient` `<integer> (0 - N)` （*默认值 \=* `125`）**

用于确定 Corosync 令牌超时时间的系数。详情请参阅 corosync.conf(5) 手册。

**`--votes` `<integer> (1 - N)`**

此节点的票数。

## **pvecm delnode** `<node>` <a href="#cli_pvecm_delnode" id="cli_pvecm_delnode"></a>

从集群配置中移除节点。

**`<node>`: `<string>`**

集群节点名称。

## **pvecm expected** `<expected>` <a href="#cli_pvecm_expected" id="cli_pvecm_expected"></a>

告知 corosync 新的预期票数值。

**`<expected>`: `<integer> (1 - N)`**

预期票数

## **pvecm help** `[OPTIONS]` <a href="#cli_pvecm_help" id="cli_pvecm_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvecm keygen** `<filename>` <a href="#cli_pvecm_keygen" id="cli_pvecm_keygen"></a>

为 corosync 生成新的加密密钥。

**`<filename>`: `<string>`**

输出文件名

## **pvecm mtunnel** `[<extra-args>]` `[OPTIONS]` <a href="#cli_pvecm_mtunnel" id="cli_pvecm_mtunnel"></a>

由虚拟机/容器迁移使用，请勿手动使用。

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--get_migration_ip` `<boolean>` （*默认值 \=* `0`）**

如果配置了迁移 IP，则返回该 IP

**`--migration_network` `<string>`**

用于检测本地迁移 IP 的迁移网络

**`--run-command` `<boolean>`**

运行命令，并使用 tcp 套接字作为标准输入。首先通过此命令的标准输出打印 IP 地址和端口，各占一行。

## **pvecm nodes** <a href="#cli_pvecm_nodes" id="cli_pvecm_nodes"></a>

显示本地所见的集群节点。

## **pvecm qdevice remove** <a href="#cli_pvecm_qdevice_remove" id="cli_pvecm_qdevice_remove"></a>

移除已配置的 QDevice

## **pvecm qdevice setup** `<address>` `[OPTIONS]` <a href="#cli_pvecm_qdevice_setup" id="cli_pvecm_qdevice_setup"></a>

设置 QDevice 的使用

**`<address>`: `<string>`**

指定外部 corosync QDevice 的网络地址

**`--force` `<boolean>`**

遇到可能危险的操作时不抛出错误。

**`--network` `<string>`**

应使用哪个网络连接外部 qdevice

## **pvecm status** <a href="#cli_pvecm_status" id="cli_pvecm_status"></a>

显示本地所见的集群状态。

## **pvecm updatecerts** `[OPTIONS]` <a href="#cli_pvecm_updatecerts" id="cli_pvecm_updatecerts"></a>

更新节点证书（并生成所有所需文件/目录）。

**`--force` `<boolean>`**

强制生成新的 SSL 证书。

**`--silent` `<boolean>`**

忽略错误（例如集群没有仲裁时）。

**`--unmerge-known-hosts` `<boolean>` （*默认值 \=* `0`）**

取消合并旧版 SSH 已知主机记录。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
