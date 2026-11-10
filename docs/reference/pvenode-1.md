# pvenode(1)

## 名称 <a href="#name" id="name"></a>

pvenode \- Proxmox VE 节点管理

## 概要 <a href="#synopsis" id="synopsis"></a>

### <strong>pvenode</strong> `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvenode" id="cli_pvenode"></a>

### <strong>pvenode acme account deactivate</strong> `[<name>]` <a href="#cli_pvenode_acme_account_deactivate" id="cli_pvenode_acme_account_deactivate"></a>

在 CA 处停用现有 ACME 账户。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

### <strong>pvenode acme account info</strong> `[<name>]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_account_info" id="cli_pvenode_acme_account_info"></a>

返回现有 ACME 账户信息。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

### <strong>pvenode acme account list</strong> <a href="#cli_pvenode_acme_account_list" id="cli_pvenode_acme_account_list"></a>

ACMEAccount 索引。

### <strong>pvenode acme account register</strong> `[<name>] {<contact>}` `[OPTIONS]` <a href="#cli_pvenode_acme_account_register" id="cli_pvenode_acme_account_register"></a>

在兼容的 CA 上注册新的 ACME 账户。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

**`<contact>`: `<string>`**

联系电子邮件地址。

**`--directory` `^https?://.*`**

ACME CA 目录端点的 URL。

### <strong>pvenode acme account update</strong> `[<name>]` `[OPTIONS]` <a href="#cli_pvenode_acme_account_update" id="cli_pvenode_acme_account_update"></a>

向 CA 更新现有 ACME 账户信息。注意：不指定任何新账户信息将触发刷新。

**`<name>`: `<name>` （<em>默认值 \=</em> `default`）**

ACME 账户配置文件名。

**`--contact` `<string>`**

联系电子邮件地址。

### <strong>pvenode acme cert order</strong> `[OPTIONS]` <a href="#cli_pvenode_acme_cert_order" id="cli_pvenode_acme_cert_order"></a>

从兼容 ACME 的 CA 申请新证书。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

覆盖现有的自定义证书。

### <strong>pvenode acme cert renew</strong> `[OPTIONS]` <a href="#cli_pvenode_acme_cert_renew" id="cli_pvenode_acme_cert_renew"></a>

从 CA 续订现有证书。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

即使距离到期还有 30 天以上，也强制续订。

### <strong>pvenode acme cert revoke</strong> <a href="#cli_pvenode_acme_cert_revoke" id="cli_pvenode_acme_cert_revoke"></a>

向 CA 吊销现有证书。

### <strong>pvenode acme plugin add</strong> `<type> <id>` `[OPTIONS]` <a href="#cli_pvenode_acme_plugin_add" id="cli_pvenode_acme_plugin_add"></a>

添加 ACME 插件配置。

**`<type>`: `<dns | standalone>`**

ACME 质询类型。

**`<id>`: `<string>`**

ACME 插件 ID 名称

**`--api` `<1984hosting | acmedns | acmeproxy | active24 | ad | ali | alviy | anx | artfiles | arvan | aurora | autodns | aws | azion | azure | beget | bookmyname | bunny | cf | clouddns | cloudns | cn | conoha | constellix | cpanel | curanet | cyon | da | ddnss | desec | df | dgon | dnsexit | dnshome | dnsimple | dnsservices | doapi | domeneshop | dp | dpi | dreamhost | duckdns | durabledns | dyn | dynu | dynv6 | easydns | edgecenter | edgedns | euserv | exoscale | fornex | freedns | freemyip | gandi_livedns | gcloud | gcore | gd | geoscaling | googledomains | he | he_ddns | hetzner | hetznercloud | hexonet | hostingde | huaweicloud | infoblox | infomaniak | internetbs | inwx | ionos | ionos_cloud | ipv64 | ispconfig | jd | joker | kappernet | kas | kinghost | knot | la | leaseweb | lexicon | limacity | linode | linode_v4 | loopia | lua | maradns | me | miab | mijnhost | misaka | myapi | mydevil | mydnsjp | mythic_beasts | namecheap | namecom | namesilo | nanelo | nederhost | neodigit | netcup | netlify | nic | njalla | nm | nsd | nsone | nsupdate | nw | oci | omglol | one | online | openprovider | openprovider_rest | openstack | opnsense | ovh | pdns | pleskxml | pointhq | porkbun | rackcorp | rackspace | rage4 | rcode0 | regru | scaleway | schlundtech | selectel | selfhost | servercow | simply | spaceship | technitium | tele3 | tencent | timeweb | transip | udr | ultra | unoeuro | variomedia | veesp | vercel | vscale | vultr | websupport | west_cn | world4you | yandex360 | yc | zilore | zone | zoneedit | zonomi>`**

API 插件名称

**`--data` `File with one key-value pair per line, will be base64url encode for storage in plugin config.`**

DNS 插件数据。（base64 编码）

**`--disable` `<boolean>`**

用于禁用配置的标志。

**`--nodes` `<string>`**

集群节点名称列表。

**`--validation-delay` `<integer> (0 - 172800)` （<em>默认值 \=</em> `30`）**

请求验证前额外等待的延迟，单位为秒。用于应对 DNS 记录 TTL 较长的情况。

### <strong>pvenode acme plugin config</strong> `<id>` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_plugin_config" id="cli_pvenode_acme_plugin_config"></a>

获取 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件实例的唯一标识符。

### <strong>pvenode acme plugin list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_plugin_list" id="cli_pvenode_acme_plugin_list"></a>

ACME 插件索引。

**`--type` `<dns | standalone>`**

仅列出指定类型的 ACME 插件

### <strong>pvenode acme plugin remove</strong> `<id>` <a href="#cli_pvenode_acme_plugin_remove" id="cli_pvenode_acme_plugin_remove"></a>

删除 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件实例的唯一标识符。

### <strong>pvenode acme plugin set</strong> `<id>` `[OPTIONS]` <a href="#cli_pvenode_acme_plugin_set" id="cli_pvenode_acme_plugin_set"></a>

更新 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件 ID 名称

**`--api` `<1984hosting | acmedns | acmeproxy | active24 | ad | ali | alviy | anx | artfiles | arvan | aurora | autodns | aws | azion | azure | beget | bookmyname | bunny | cf | clouddns | cloudns | cn | conoha | constellix | cpanel | curanet | cyon | da | ddnss | desec | df | dgon | dnsexit | dnshome | dnsimple | dnsservices | doapi | domeneshop | dp | dpi | dreamhost | duckdns | durabledns | dyn | dynu | dynv6 | easydns | edgecenter | edgedns | euserv | exoscale | fornex | freedns | freemyip | gandi_livedns | gcloud | gcore | gd | geoscaling | googledomains | he | he_ddns | hetzner | hetznercloud | hexonet | hostingde | huaweicloud | infoblox | infomaniak | internetbs | inwx | ionos | ionos_cloud | ipv64 | ispconfig | jd | joker | kappernet | kas | kinghost | knot | la | leaseweb | lexicon | limacity | linode | linode_v4 | loopia | lua | maradns | me | miab | mijnhost | misaka | myapi | mydevil | mydnsjp | mythic_beasts | namecheap | namecom | namesilo | nanelo | nederhost | neodigit | netcup | netlify | nic | njalla | nm | nsd | nsone | nsupdate | nw | oci | omglol | one | online | openprovider | openprovider_rest | openstack | opnsense | ovh | pdns | pleskxml | pointhq | porkbun | rackcorp | rackspace | rage4 | rcode0 | regru | scaleway | schlundtech | selectel | selfhost | servercow | simply | spaceship | technitium | tele3 | tencent | timeweb | transip | udr | ultra | unoeuro | variomedia | veesp | vercel | vscale | vultr | websupport | west_cn | world4you | yandex360 | yc | zilore | zone | zoneedit | zonomi>`**

API 插件名称

**`--data` `File with one key-value pair per line, will be base64url encode for storage in plugin config.`**

DNS 插件数据。（base64 编码）

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--disable` `<boolean>`**

用于禁用配置的标志。

**`--nodes` `<string>`**

集群节点名称列表。

**`--validation-delay` `<integer> (0 - 172800)` （<em>默认值 \=</em> `30`）**

请求验证前额外等待的延迟，单位为秒。用于应对 DNS 记录 TTL 较长的情况。

### <strong>pvenode cert delete</strong> `[<restart>]` <a href="#cli_pvenode_cert_delete" id="cli_pvenode_cert_delete"></a>

删除自定义证书链和密钥。

**`<restart>`: `<boolean>` （<em>默认值 \=</em> `0`）**

重启 pveproxy。

### <strong>pvenode cert info</strong> `[FORMAT_OPTIONS]` <a href="#cli_pvenode_cert_info" id="cli_pvenode_cert_info"></a>

获取有关节点证书的信息。

### <strong>pvenode cert set</strong> `<certificates> [<key>]` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_cert_set" id="cli_pvenode_cert_set"></a>

上传或更新自定义证书链和密钥。

**`<certificates>`: `<string>`**

PEM 编码的证书（链）。

**`<key>`: `<string>`**

PEM 编码的私钥。

**`--force` `<boolean>`（<em>默认 \=</em> `0`）**

覆盖现有自定义证书文件或 ACME 证书文件。

**`--restart` `<boolean>` （<em>默认值 \=</em> `0`）**

重启 pveproxy。

### <strong>pvenode config get</strong> `[OPTIONS]` <a href="#cli_pvenode_config_get" id="cli_pvenode_config_get"></a>

获取节点配置选项。

**`--property` `<acme | acmedomain0 | acmedomain1 | acmedomain2 | acmedomain3 | acmedomain4 | acmedomain5 | ballooning-target | description | location | startall-onboot-delay | wakeonlan>` （<em>默认值 \=</em> `all`）**

仅返回节点配置中的指定属性。

### <strong>pvenode config set</strong> `[OPTIONS]` <a href="#cli_pvenode_config_set" id="cli_pvenode_config_set"></a>

设置节点配置选项。

**`--acme` `[account=<name>] [,domains=<domain[;domain;...]>]`**

节点特定的 ACME 设置。

**`--acmedomain[n]` `[domain=]<domain> [,alias=<domain>] [,plugin=<name of the plugin configuration>]`**

ACME 域和验证插件

**`--ballooning-target` `<integer> (0 - 100)` （<em>默认值 \=</em> `80`）**

内存气球的 RAM 使用率目标（占总内存的百分比）

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

节点描述。显示在 Web 界面的节点备注面板中。以注释形式保存在配置文件内。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--location` `latitude=<number> ,longitude=<number> [,name=<name>]`**

节点的位置。覆盖数据中心配置中的默认值。

**`--startall-onboot-delay` `<integer> (0 - 300)` （<em>默认值 \=</em> `0`）**

启动所有已启用开机启动的虚拟客户机之前的初始延迟，单位为秒。

**`--wakeonlan` `[mac=]<MAC address> [,bind-interface=<bind interface>] [,broadcast-address=<IPv4 broadcast address>]`**

节点特定的网络唤醒设置。

### <strong>pvenode help</strong> `[OPTIONS]` <a href="#cli_pvenode_help" id="cli_pvenode_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

### <strong>pvenode migrateall</strong> `<target>` `[OPTIONS]` <a href="#cli_pvenode_migrateall" id="cli_pvenode_migrateall"></a>

迁移所有虚拟机和容器。

**`<target>`: `<string>`**

目标节点。

**`--max-workers` `<integer> (1 - 64)`**

并行迁移任务的最大数量。如果未设置，则使用 max\_workers，其值来自 datacenter.cfg。两者必须至少设置一个！

**`--maxworkers` `<integer> (1 - 64)`**

并行迁移任务的最大数量。如果未设置，则使用 max\_workers，其值来自 datacenter.cfg。两者必须至少设置一个！已弃用，请改用 <em>max-workers</em>。

**`--vms` `<string>`**

仅考虑具有这些 ID 的客户机。

**`--with-local-disks` `<boolean>`**

对本地磁盘启用在线存储迁移

### <strong>pvenode startall</strong> `[OPTIONS]` <a href="#cli_pvenode_startall" id="cli_pvenode_startall"></a>

启动此节点上的所有虚拟机和容器（默认只启动设置了 onboot\=1 的客户机）。

**`--force` `<boolean>` （<em>默认值 \=</em> `off`）**

即使虚拟客户机未设置 <em>onboot</em> 或将其设置为 off，也发出启动命令。

**`--max-workers` `<integer> (1 - 64)`**

定义同时运行任务的最大数量。如果未设置，则使用 <em>max\_workers</em>，其值来自 datacenter.cfg；如果该值也未设置，则使用可用 CPU 线程数，但最多为 8。

**`--vms` `<string>`**

仅考虑此逗号分隔的 VMID 列表中的客户机。

### <strong>pvenode stopall</strong> `[OPTIONS]` <a href="#cli_pvenode_stopall" id="cli_pvenode_stopall"></a>

停止所有虚拟机和容器。

**`--force-stop` `<boolean>` （<em>默认值 \=</em> `1`）**

超时后强制停止。

**`--max-workers` `<integer> (1 - 64)`**

定义同时运行任务的最大数量。如果未设置，则使用 <em>max\_workers</em>，其值来自 datacenter.cfg；如果该值也未设置，则使用可用 CPU 线程数，但最多为 8。

**`--timeout` `<integer> (0 - 7200)` （<em>默认值 \=</em> `180`）**

每个客户机关机任务的超时时间。随后根据 `force-stop` 的设置，直接中止关机或强制停止。

**`--vms` `<string>`**

仅考虑具有这些 ID 的客户机。

### <strong>pvenode task list</strong> `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_task_list" id="cli_pvenode_task_list"></a>

读取某个节点的任务列表（已完成任务）。

**`--errors` `<boolean>` （<em>默认值 \=</em> `0`）**

仅列出状态为 ERROR 的任务。

**`--limit` `<integer> (0 - N)` （<em>默认值 \=</em> `50`）**

仅列出此数量的任务。

**`--since` `<integer>`**

仅列出此 UNIX 纪元时间之后的任务。

**`--source` `<active | all | archive>` （<em>默认值 \=</em> `archive`）**

列出已归档、活动或全部任务。

**`--start` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

从此偏移量开始列出任务。

**`--statusfilter` `<string>`**

应返回的任务状态列表。

**`--typefilter` `<string>`**

仅列出此类型的任务（例如 vzstart、vzdump）。

**`--until` `<integer>`**

仅列出此 UNIX 纪元时间之前的任务。

**`--userfilter` `<string>`**

仅列出此用户的任务。

**`--vmid` `<integer> (100 - 999999999)`**

仅列出此虚拟机的任务。

### <strong>pvenode task log</strong> `<upid>` `[OPTIONS]` <a href="#cli_pvenode_task_log" id="cli_pvenode_task_log"></a>

读取任务日志。

**`<upid>`: `<string>`**

任务的唯一 ID。

**`--download` `<boolean>`**

是否应下载任务日志文件。此参数不能与其他参数同时使用

**`--start` `<integer> (0 - N)` （<em>默认值 \=</em> `0`）**

读取任务日志时从此行开始

### <strong>pvenode task status</strong> `<upid>` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_task_status" id="cli_pvenode_task_status"></a>

读取任务状态。

**`<upid>`: `<string>`**

任务的唯一 ID。

### <strong>pvenode wakeonlan</strong> `<node>` <a href="#cli_pvenode_wakeonlan" id="cli_pvenode_wakeonlan"></a>

尝试通过<em>网络唤醒</em>数据包唤醒节点。

**`<node>`: `<string>`**

网络唤醒数据包的目标节点

## 描述 <a href="#description" id="description"></a>

Proxmox VE 节点管理工具（`pvenode`）允许你控制节点特定的设置和资源。

目前，`pvenode` 允许你设置节点描述、对节点上的客户机执行各种批量操作、查看节点的任务历史记录，以及管理节点的 SSL 证书；这些证书由 `pveproxy` 用于 API 和 Web GUI。

## FORMAT\_OPTIONS <a href="#format_options" id="format_options"></a>

可以使用 `--output-format` 参数指定输出格式。默认格式 <em>text</em> 使用 ASCII 字符画为表格绘制美观的边框。此外，还会将某些值转换为易于阅读的文本，例如：

- Unix 纪元时间显示为 ISO 8601 日期字符串。
- 时长显示为周/天/小时/分钟/秒的数量，即 `1d 5h`。
- 字节大小值包含单位（`B`、`KiB`、`MiB`、`GiB`、`TiB`、`PiB`）。
- 小数显示为百分比，即 1.0 显示为 100%。

还可以使用选项 `--quiet` 完全禁止输出。

**`--human-readable` `<boolean>`（<em>默认值 \=</em> `1`）**

调用输出渲染函数，生成易于阅读的文本。

**`--noborder` `<boolean>`（<em>默认值 \=</em> `0`）**

不绘制边框（适用于 <em>text</em> 格式）。

**`--noheader` `<boolean>`（<em>默认值 \=</em> `0`）**

不显示列标题（适用于 <em>text</em> 格式）。

**`--output-format` `<json | json-pretty | text | yaml>`（<em>默认值 \=</em> `text`）**

输出格式。

**`--quiet` `<boolean>`**

禁止打印结果。

### 示例 <a href="#examples" id="examples"></a>

**安装外部提供的证书**

`pvenode cert set certificate.crt certificate.key -force`

两个文件都必须采用 PEM 编码。`certificate.key` 包含私钥，`certificate.crt` 包含完整证书链。

**设置 ACME 账户，并为本地节点申请证书。**

```text
pvenode acme account register default mail@example.invalid
pvenode config set --acme domains=example.invalid
pvenode acme cert order
systemctl restart pveproxy
```

### 网络唤醒 <a href="#wake_on_lan" id="wake_on_lan"></a>

Wake-on-LAN（WoL）允许你通过发送魔术包来唤醒网络中处于睡眠状态的计算机。至少有一个 NIC 必须支持此功能，并且需要在计算机的固件（BIOS/UEFI）配置中启用相应选项。选项名称可能从<em>启用 Wake-on-Lan</em>到<em>通过 PCIE 设备开机</em>不等；如果不确定，请查阅主板厂商手册。可以运行以下命令，使用 `ethtool` 检查 `<interface>` 的 WoL 配置：

```text
ethtool <interface> | grep Wake-on
```

`pvenode` 允许你通过 WoL 唤醒集群中处于睡眠状态的成员，命令为：

```text
pvenode wakeonlan <node>
```

这会在 UDP 端口 9 上广播 WoL 魔术包，其中包含 `<node>` 的 MAC 地址，该地址从 `wakeonlan` 属性获取。可以使用以下命令设置节点特定的 `wakeonlan` 属性：

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

### 任务历史 <a href="#task_history" id="task_history"></a>

排查服务器问题（例如备份作业失败）时，查看先前运行任务的日志通常会很有帮助。在 Proxmox VE 中，可以通过 `pvenode task` 命令访问节点的任务历史记录。

可以使用 `list` 子命令获取节点已完成任务的筛选列表。例如，要获取与 VM <em>100</em> 相关且以错误结束的任务列表，命令如下：

```text
pvenode task list --errors --vmid 100
```

随后可以使用任务的 UPID 打印其日志：

```text
pvenode task log UPID:pve1:00010D94:001CA6EA:6124E1B9:vzdump:100:root@pam:
```

### 客户机批量电源管理 <a href="#bulk_guest_power_management" id="bulk_guest_power_management"></a>

如果有许多虚拟机/容器，可以通过 `startall` 和 `stopall` 子命令批量启动和停止客户机，这些子命令属于 `pvenode`。默认情况下，`pvenode startall` 只启动已设置为开机自动启动的虚拟机/容器（参见[虚拟机的自动启动和关闭](qm-1.md#qm_startup_and_shutdown)），但可以使用 `--force` 标志覆盖此行为。两个命令也都有 `--vms` 选项，将停止/启动的客户机限制为指定的 VMID。

例如，要启动 VM <em>100</em>、<em>101</em> 和 <em>102</em>，无论它们是否设置了 `onboot`，都可以使用：

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

### 首个客户机启动延迟 <a href="#first_guest_boot_delay" id="first_guest_boot_delay"></a>

如果虚拟机/容器依赖启动缓慢的外部资源，例如 NFS 服务器，还可以按节点设置从 Proxmox VE 启动到首个配置为自动启动的虚拟机/容器启动之间的延迟（参见[虚拟机的自动启动和关闭](qm-1.md#qm_startup_and_shutdown)）。

可通过以下设置实现（其中 `10` 表示以秒为单位的延迟）：

```text
pvenode config set --startall-onboot-delay 10
```

### 客户机批量迁移 <a href="#bulk_guest_migration" id="bulk_guest_migration"></a>

如果升级时需要将所有客户机从一个节点迁移到另一个节点，`pvenode` 还提供用于批量迁移的 `migrateall` 子命令。默认情况下，此命令会将系统上的每个客户机迁移到目标节点，但也可以设置为仅迁移一组客户机。

例如，要将 VM <em>100</em>、<em>101</em> 和 <em>102</em> 迁移到节点 <em>pve2</em>，并启用本地磁盘的在线迁移，可以运行：

```text
pvenode migrateall pve2 --vms 100,101,102 --with-local-disks
```

### 内存气球的 RAM 使用率目标 <a href="#ballooning-target" id="ballooning-target"></a>

[自动内存分配](qm-1.md#qm_ballooning)的目标百分比默认为 80%。可以通过设置 `ballooning-target` 属性，为每个节点自定义此目标。例如，要改为以 90% 的宿主机内存使用率为目标：

```text
pvenode config set --ballooning-target 90
```

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pvenode.1.html) · 版本 9.2.13 · 非官方中文翻译。
