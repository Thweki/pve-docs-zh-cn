# pvenode(1)

## 名称 <a href="#_name" id="_name"></a>

pvenode \- Proxmox VE Node Management

## 概要 <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pvenode"></a>



**pvenode** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvenode_acme_account_deactivate"></a>



**pvenode acme account deactivate** `[<name>]`

Deactivate existing ACME account at CA.

**`<name>`: `<name>` (*default \=* `default`)**

ACME account config file name.

<a id="cli_pvenode_acme_account_info"></a>



**pvenode acme account info** `[<name>]` `[FORMAT_OPTIONS]`

Return existing ACME account information.

**`<name>`: `<name>` (*default \=* `default`)**

ACME account config file name.

<a id="cli_pvenode_acme_account_list"></a>



**pvenode acme account list**

ACMEAccount index.

<a id="cli_pvenode_acme_account_register"></a>



**pvenode acme account register** `[<name>] {<contact>}` `[OPTIONS]`

Register a new ACME account with a compatible CA.

**`<name>`: `<name>` (*default \=* `default`)**

ACME account config file name.

**`<contact>`: `<string>`**

Contact email addresses.

**`--directory` `^https?://.*`**

URL of ACME CA directory endpoint.

<a id="cli_pvenode_acme_account_update"></a>



**pvenode acme account update** `[<name>]` `[OPTIONS]`

Update existing ACME account information with CA. Note: not specifying any new account information triggers a refresh.

**`<name>`: `<name>` (*default \=* `default`)**

ACME account config file name.

**`--contact` `<string>`**

Contact email addresses.

<a id="cli_pvenode_acme_cert_order"></a>



**pvenode acme cert order** `[OPTIONS]`

Order a new certificate from ACME-compatible CA.

**`--force` `<boolean>`（*默认 \=* `0`）**

Overwrite existing custom certificate.

<a id="cli_pvenode_acme_cert_renew"></a>



**pvenode acme cert renew** `[OPTIONS]`

Renew existing certificate from CA.

**`--force` `<boolean>`（*默认 \=* `0`）**

Force renewal even if expiry is more than 30 days away.

<a id="cli_pvenode_acme_cert_revoke"></a>



**pvenode acme cert revoke**

Revoke existing certificate from CA.

<a id="cli_pvenode_acme_plugin_add"></a>



**pvenode acme plugin add** `<type> <id>` `[OPTIONS]`

Add ACME plugin configuration.

**`<type>`: `<dns | standalone>`**

ACME challenge type.

**`<id>`: `<string>`**

ACME Plugin ID name

**`--api` `<1984hosting | acmedns | acmeproxy | active24 | ad | ali | alviy | anx | artfiles | arvan | aurora | autodns | aws | azion | azure | beget | bookmyname | bunny | cf | clouddns | cloudns | cn | conoha | constellix | cpanel | curanet | cyon | da | ddnss | desec | df | dgon | dnsexit | dnshome | dnsimple | dnsservices | doapi | domeneshop | dp | dpi | dreamhost | duckdns | durabledns | dyn | dynu | dynv6 | easydns | edgecenter | edgedns | euserv | exoscale | fornex | freedns | freemyip | gandi_livedns | gcloud | gcore | gd | geoscaling | googledomains | he | he_ddns | hetzner | hetznercloud | hexonet | hostingde | huaweicloud | infoblox | infomaniak | internetbs | inwx | ionos | ionos_cloud | ipv64 | ispconfig | jd | joker | kappernet | kas | kinghost | knot | la | leaseweb | lexicon | limacity | linode | linode_v4 | loopia | lua | maradns | me | miab | mijnhost | misaka | myapi | mydevil | mydnsjp | mythic_beasts | namecheap | namecom | namesilo | nanelo | nederhost | neodigit | netcup | netlify | nic | njalla | nm | nsd | nsone | nsupdate | nw | oci | omglol | one | online | openprovider | openprovider_rest | openstack | opnsense | ovh | pdns | pleskxml | pointhq | porkbun | rackcorp | rackspace | rage4 | rcode0 | regru | scaleway | schlundtech | selectel | selfhost | servercow | simply | spaceship | technitium | tele3 | tencent | timeweb | transip | udr | ultra | unoeuro | variomedia | veesp | vercel | vscale | vultr | websupport | west_cn | world4you | yandex360 | yc | zilore | zone | zoneedit | zonomi>`**

API plugin name

**`--data` `File with one key-value pair per line, will be base64url encode for storage in plugin config.`**

DNS plugin data. (base64 encoded)

**`--disable` `<boolean>`**

Flag to disable the config.

**`--nodes` `<string>`**

List of cluster node names.

**`--validation-delay` `<integer> (0 - 172800)` (*default \=* `30`)**

Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records.

<a id="cli_pvenode_acme_plugin_config"></a>



**pvenode acme plugin config** `<id>` `[FORMAT_OPTIONS]`

Get ACME plugin configuration.

**`<id>`: `<string>`**

Unique identifier for ACME plugin instance.

<a id="cli_pvenode_acme_plugin_list"></a>



**pvenode acme plugin list** `[OPTIONS]` `[FORMAT_OPTIONS]`

ACME plugin index.

**`--type` `<dns | standalone>`**

Only list ACME plugins of a specific type

<a id="cli_pvenode_acme_plugin_remove"></a>



**pvenode acme plugin remove** `<id>`

Delete ACME plugin configuration.

**`<id>`: `<string>`**

Unique identifier for ACME plugin instance.

<a id="cli_pvenode_acme_plugin_set"></a>



**pvenode acme plugin set** `<id>` `[OPTIONS]`

Update ACME plugin configuration.

**`<id>`: `<string>`**

ACME Plugin ID name

**`--api` `<1984hosting | acmedns | acmeproxy | active24 | ad | ali | alviy | anx | artfiles | arvan | aurora | autodns | aws | azion | azure | beget | bookmyname | bunny | cf | clouddns | cloudns | cn | conoha | constellix | cpanel | curanet | cyon | da | ddnss | desec | df | dgon | dnsexit | dnshome | dnsimple | dnsservices | doapi | domeneshop | dp | dpi | dreamhost | duckdns | durabledns | dyn | dynu | dynv6 | easydns | edgecenter | edgedns | euserv | exoscale | fornex | freedns | freemyip | gandi_livedns | gcloud | gcore | gd | geoscaling | googledomains | he | he_ddns | hetzner | hetznercloud | hexonet | hostingde | huaweicloud | infoblox | infomaniak | internetbs | inwx | ionos | ionos_cloud | ipv64 | ispconfig | jd | joker | kappernet | kas | kinghost | knot | la | leaseweb | lexicon | limacity | linode | linode_v4 | loopia | lua | maradns | me | miab | mijnhost | misaka | myapi | mydevil | mydnsjp | mythic_beasts | namecheap | namecom | namesilo | nanelo | nederhost | neodigit | netcup | netlify | nic | njalla | nm | nsd | nsone | nsupdate | nw | oci | omglol | one | online | openprovider | openprovider_rest | openstack | opnsense | ovh | pdns | pleskxml | pointhq | porkbun | rackcorp | rackspace | rage4 | rcode0 | regru | scaleway | schlundtech | selectel | selfhost | servercow | simply | spaceship | technitium | tele3 | tencent | timeweb | transip | udr | ultra | unoeuro | variomedia | veesp | vercel | vscale | vultr | websupport | west_cn | world4you | yandex360 | yc | zilore | zone | zoneedit | zonomi>`**

API plugin name

**`--data` `File with one key-value pair per line, will be base64url encode for storage in plugin config.`**

DNS plugin data. (base64 encoded)

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

Flag to disable the config.

**`--nodes` `<string>`**

List of cluster node names.

**`--validation-delay` `<integer> (0 - 172800)` (*default \=* `30`)**

Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records.

<a id="cli_pvenode_cert_delete"></a>



**pvenode cert delete** `[<restart>]`

DELETE custom certificate chain and key.

**`<restart>`: `<boolean>` (*default \=* `0`)**

Restart pveproxy.

<a id="cli_pvenode_cert_info"></a>



**pvenode cert info** `[FORMAT_OPTIONS]`

Get information about node’s certificates.

<a id="cli_pvenode_cert_set"></a>



**pvenode cert set** `<certificates> [<key>]` `[OPTIONS]` `[FORMAT_OPTIONS]`

Upload or update custom certificate chain and key.

**`<certificates>`: `<string>`**

PEM encoded certificate (chain).

**`<key>`: `<string>`**

PEM encoded private key.

**`--force` `<boolean>`（*默认 \=* `0`）**

Overwrite existing custom or ACME certificate files.

**`--restart` `<boolean>` (*default \=* `0`)**

Restart pveproxy.

<a id="cli_pvenode_config_get"></a>



**pvenode config get** `[OPTIONS]`

Get node configuration options.

**`--property` `<acme | acmedomain0 | acmedomain1 | acmedomain2 | acmedomain3 | acmedomain4 | acmedomain5 | ballooning-target | description | location | startall-onboot-delay | wakeonlan>` (*default \=* `all`)**

Return only a specific property from the node configuration.

<a id="cli_pvenode_config_set"></a>



**pvenode config set** `[OPTIONS]`

Set node configuration options.

**`--acme` `[account=<name>] [,domains=<domain[;domain;...]>]`**

Node specific ACME settings.

**`--acmedomain[n]` `[domain=]<domain> [,alias=<domain>] [,plugin=<name of the plugin configuration>]`**

ACME domain and validation plugin

**`--ballooning-target` `<integer> (0 - 100)` (*default \=* `80`)**

RAM usage target for ballooning (in percent of total memory)

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

Description for the Node. Shown in the web-interface node notes panel. This is saved as comment inside the configuration file.

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--location` `latitude=<number> ,longitude=<number> [,name=<name>]`**

The location of the node. Overrides the default from the datacenter config.

**`--startall-onboot-delay` `<integer> (0 - 300)` (*default \=* `0`)**

Initial delay in seconds, before starting all the Virtual Guests with on-boot enabled.

**`--wakeonlan` `[mac=]<MAC address> [,bind-interface=<bind interface>] [,broadcast-address=<IPv4 broadcast address>]`**

Node specific wake on LAN settings.

<a id="cli_pvenode_help"></a>



**pvenode help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvenode_migrateall"></a>



**pvenode migrateall** `<target>` `[OPTIONS]`

Migrate all VMs and Containers.

**`<target>`: `<string>`**

目标节点。

**`--max-workers` `<integer> (1 - 64)`**

Maximal number of parallel migration job. If not set, uses’max\_workers' from datacenter.cfg. One of both must be set!

**`--maxworkers` `<integer> (1 - 64)`**

Maximal number of parallel migration job. If not set, uses’max\_workers' from datacenter.cfg. One of both must be set!Deprecated, use *max-workers* instead.

**`--vms` `<string>`**

Only consider Guests with these IDs.

**`--with-local-disks` `<boolean>`**

Enable live storage migration for local disk

<a id="cli_pvenode_startall"></a>



**pvenode startall** `[OPTIONS]`

Start all VMs and containers located on this node (by default only those with onboot\=1).

**`--force` `<boolean>` (*default \=* `off`)**

Issue start command even if virtual guest have *onboot* not set or set to off.

**`--max-workers` `<integer> (1 - 64)`**

Defines the maximum number of tasks running concurrently. If not set, uses *max\_workers* from datacenter.cfg, and if that’s not set, the available CPU threads, clamped to a maximum of 8, are used.

**`--vms` `<string>`**

Only consider guests from this comma separated list of VMIDs.

<a id="cli_pvenode_stopall"></a>



**pvenode stopall** `[OPTIONS]`

Stop all VMs and Containers.

**`--force-stop` `<boolean>` (*default \=* `1`)**

Force a hard-stop after the timeout.

**`--max-workers` `<integer> (1 - 64)`**

Defines the maximum number of tasks running concurrently. If not set, uses *max\_workers* from datacenter.cfg, and if that’s not set, the available CPU threads, clamped to a maximum of 8, are used.

**`--timeout` `<integer> (0 - 7200)` (*default \=* `180`)**

Timeout for each guest shutdown task. Depending on `force-stop`, the shutdown gets then simply aborted or a hard-stop is forced.

**`--vms` `<string>`**

Only consider Guests with these IDs.

<a id="cli_pvenode_task_list"></a>



**pvenode task list** `[OPTIONS]` `[FORMAT_OPTIONS]`

Read task list for one node (finished tasks).

**`--errors` `<boolean>` (*default \=* `0`)**

Only list tasks with a status of ERROR.

**`--limit` `<integer> (0 - N)` (*default \=* `50`)**

Only list this number of tasks.

**`--since` `<integer>`**

Only list tasks since this UNIX epoch.

**`--source` `<active | all | archive>` (*default \=* `archive`)**

List archived, active or all tasks.

**`--start` `<integer> (0 - N)` (*default \=* `0`)**

List tasks beginning from this offset.

**`--statusfilter` `<string>`**

List of Task States that should be returned.

**`--typefilter` `<string>`**

Only list tasks of this type (e.g., vzstart, vzdump).

**`--until` `<integer>`**

Only list tasks until this UNIX epoch.

**`--userfilter` `<string>`**

Only list tasks from this user.

**`--vmid` `<integer> (100 - 999999999)`**

Only list tasks for this VM.

<a id="cli_pvenode_task_log"></a>



**pvenode task log** `<upid>` `[OPTIONS]`

Read task log.

**`<upid>`: `<string>`**

The task’s unique ID.

**`--download` `<boolean>`**

Whether the tasklog file should be downloaded. This parameter can’t be used in conjunction with other parameters

**`--start` `<integer> (0 - N)` (*default \=* `0`)**

Start at this line when reading the tasklog

<a id="cli_pvenode_task_status"></a>



**pvenode task status** `<upid>` `[FORMAT_OPTIONS]`

Read task status.

**`<upid>`: `<string>`**

The task’s unique ID.

<a id="cli_pvenode_wakeonlan"></a>



**pvenode wakeonlan** `<node>`

Try to wake a node via *wake on LAN* network packet.

**`<node>`: `<string>`**

target node for wake on LAN packet

## 描述 <a href="#_description" id="_description"></a>

Proxmox VE 节点管理工具（`pvenode`）允许你控制节点特定的设置和资源。

目前，`pvenode` 允许你设置节点描述、对节点上的客户机执行各种批量操作、查看节点的任务历史记录，以及管理节点的 SSL 证书；这些证书由 `pveproxy` 用于 API 和 Web GUI。

## FORMAT\_OPTIONS <a href="#_format_options" id="_format_options"></a>

It is possible to specify the output format using the `--output-format` parameter. The default format *text* uses ASCII-art to draw nice borders around tables. It additionally transforms some values into human-readable text, for example:

- Unix epoch is displayed as ISO 8601 date string.
- Durations are displayed as week/day/hour/minute/second count, i.e `1d 5h`.
- Byte sizes value include units (`B`, `KiB`, `MiB`, `GiB`, `TiB`, `PiB`).
- Fractions are display as percentage, i.e. 1.0 is displayed as 100%.

You can also completely suppress output using option `--quiet`.

**`--human-readable` `<boolean>` (*default \=* `1`)**

Call output rendering functions to produce human readable text.

**`--noborder` `<boolean>` (*default \=* `0`)**

Do not draw borders (for *text* format).

**`--noheader` `<boolean>` (*default \=* `0`)**

Do not show column headers (for *text* format).

**`--output-format` `<json | json-pretty | text | yaml>` (*default \=* `text`)**

Output format.

**`--quiet` `<boolean>`**

Suppress printing results.

### Examples <a href="#_examples" id="_examples"></a>

**Install an externally provided certificate**

`pvenode cert set certificate.crt certificate.key -force`

Both files need to be PEM encoded. `certificate.key` contains the private key and `certificate.crt` contains the whole certificate chain.

**Setup ACME account and order a certificate for the local node.**

```text
pvenode acme account register default mail@example.invalid
pvenode config set --acme domains=example.invalid
pvenode acme cert order
systemctl restart pveproxy
```

### Wake-on-LAN <a href="#_wake_on_lan" id="_wake_on_lan"></a>

Wake-on-LAN（WoL）允许你通过发送魔术包来唤醒网络中处于睡眠状态的计算机。至少有一个 NIC 必须支持此功能，并且需要在计算机的固件（BIOS/UEFI）配置中启用相应选项。选项名称可能从*启用 Wake-on-Lan*到*通过 PCIE 设备开机*不等；如果不确定，请查阅主板厂商手册。可以运行以下命令，使用 `ethtool` 检查 `<interface>` 的 WoL 配置：

```text
ethtool <interface> | grep Wake-on
```

`pvenode` 允许你通过 WoL 唤醒集群中处于睡眠状态的成员，命令为：

```text
pvenode wakeonlan <node>
```

This broadcasts the WoL magic packet on UDP port 9, containing the MAC address of `<node>` obtained from the `wakeonlan` property. The node-specific `wakeonlan` property can be set using the following command:

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX
```

发送 WoL 数据包的接口由默认路由确定。可以通过以下命令设置 `bind-interface` 来覆盖该接口：

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX,bind-interface=<iface-name>
```

发送 WoL 数据包时使用的广播地址（默认为 `255.255.255.255`）也可以通过以下命令显式设置 `broadcast-address` 来更改：

```text
pvenode config set -wakeonlan XX:XX:XX:XX:XX:XX,broadcast-address=<broadcast-address>
```

### Task History <a href="#_task_history" id="_task_history"></a>

排查服务器问题（例如备份作业失败）时，查看先前运行任务的日志通常会很有帮助。在 Proxmox VE 中，可以通过 `pvenode task` 命令访问节点的任务历史记录。

可以使用 `list` 子命令获取节点已完成任务的筛选列表。例如，要获取与 VM *100* 相关且以错误结束的任务列表，命令如下：

```text
pvenode task list --errors --vmid 100
```

随后可以使用任务的 UPID 打印其日志：

```text
pvenode task log UPID:pve1:00010D94:001CA6EA:6124E1B9:vzdump:100:root@pam:
```

### Bulk Guest Power Management <a href="#_bulk_guest_power_management" id="_bulk_guest_power_management"></a>

In case you have many VMs/containers, starting and stopping guests can be carried out in bulk operations with the `startall` and `stopall` subcommands of `pvenode`. By default, `pvenode startall` will only start VMs/containers which have been set to automatically start on boot (see [Automatic Start and Shutdown of Virtual Machines](qm-1.md#qm_startup_and_shutdown)), however, you can override this behavior with the `--force` flag. Both commands also have a `--vms` option, which limits the stopped/started guests to the specified VMIDs.

例如，要启动 VM *100*、*101* 和 *102*，无论它们是否设置了 `onboot`，都可以使用：

```text
pvenode startall --vms 100,101,102 --force
```

要停止这些客户机（以及可能正在运行的任何其他客户机），请使用以下命令：

```text
pvenode stopall
```

{% hint style="info" %}
stopall 命令首先尝试执行正常关闭，然后等待，直到所有客户机均成功关闭，或可覆盖的超时时间（默认为 3 分钟）到期。此后，如果 force-stop 参数未显式设置为 0（false），则所有仍在运行的虚拟客户机都会被强制停止。
{% endhint %}

### First Guest Boot Delay <a href="#first_guest_boot_delay" id="first_guest_boot_delay"></a>

In case your VMs/containers rely on slow-to-start external resources, for example an NFS server, you can also set a per-node delay between the time Proxmox VE boots and the time the first VM/container that is configured to autostart boots (see [Automatic Start and Shutdown of Virtual Machines](qm-1.md#qm_startup_and_shutdown)).

可通过以下设置实现（其中 `10` 表示以秒为单位的延迟）：

```text
pvenode config set --startall-onboot-delay 10
```

### Bulk Guest Migration <a href="#_bulk_guest_migration" id="_bulk_guest_migration"></a>

如果升级时需要将所有客户机从一个节点迁移到另一个节点，`pvenode` 还提供用于批量迁移的 `migrateall` 子命令。默认情况下，此命令会将系统上的每个客户机迁移到目标节点，但也可以设置为仅迁移一组客户机。

例如，要将 VM *100*、*101* 和 *102* 迁移到节点 *pve2*，并启用本地磁盘的在线迁移，可以运行：

```text
pvenode migrateall pve2 --vms 100,101,102 --with-local-disks
```

### RAM Usage Target for Ballooning <a href="#ballooning-target" id="ballooning-target"></a>

The target percentage for [automatic memory allocation](qm-1.md#qm_ballooning) defaults to 80%. You can customize this target per node by setting the `ballooning-target` property. For example, to target 90% host memory usage instead:

```text
pvenode config set --ballooning-target 90
```

## 版权与免责声明 <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvenode.1.html) · 版本 9.2.13 · 非官方中文翻译。
