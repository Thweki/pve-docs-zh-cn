# 22.7. **pvenode** \- Proxmox VE 节点管理 <a href="#strong_pvenode_strong_proxmox_ve_node_management" id="strong_pvenode_strong_proxmox_ve_node_management"></a>

## **pvenode** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pvenode" id="cli_pvenode"></a>

## **pvenode acme account deactivate** `[<name>]` <a href="#cli_pvenode_acme_account_deactivate" id="cli_pvenode_acme_account_deactivate"></a>

在 CA 处停用现有 ACME 账户。

**`<name>`: `<name>` （*默认值 \=* `default`）**

ACME 账户配置文件名。

## **pvenode acme account info** `[<name>]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_account_info" id="cli_pvenode_acme_account_info"></a>

返回现有 ACME 账户信息。

**`<name>`: `<name>` （*默认值 \=* `default`）**

ACME 账户配置文件名。

## **pvenode acme account list** <a href="#cli_pvenode_acme_account_list" id="cli_pvenode_acme_account_list"></a>

ACMEAccount 索引。

## **pvenode acme account register** `[<name>] {<contact>}` `[OPTIONS]` <a href="#cli_pvenode_acme_account_register" id="cli_pvenode_acme_account_register"></a>

在兼容的 CA 上注册新的 ACME 账户。

**`<name>`: `<name>` （*默认值 \=* `default`）**

ACME 账户配置文件名。

**`<contact>`: `<string>`**

联系电子邮件地址。

**`--directory` `^https?://.*`**

ACME CA 目录端点的 URL。

## **pvenode acme account update** `[<name>]` `[OPTIONS]` <a href="#cli_pvenode_acme_account_update" id="cli_pvenode_acme_account_update"></a>

向 CA 更新现有 ACME 账户信息。注意：不指定任何新账户信息将触发刷新。

**`<name>`: `<name>` （*默认值 \=* `default`）**

ACME 账户配置文件名。

**`--contact` `<string>`**

联系电子邮件地址。

## **pvenode acme cert order** `[OPTIONS]` <a href="#cli_pvenode_acme_cert_order" id="cli_pvenode_acme_cert_order"></a>

从兼容 ACME 的 CA 申请新证书。

**`--force` `<boolean>`（*默认 \=* `0`）**

覆盖现有的自定义证书。

## **pvenode acme cert renew** `[OPTIONS]` <a href="#cli_pvenode_acme_cert_renew" id="cli_pvenode_acme_cert_renew"></a>

从 CA 续订现有证书。

**`--force` `<boolean>`（*默认 \=* `0`）**

即使距离到期还有 30 天以上，也强制续订。

## **pvenode acme cert revoke** <a href="#cli_pvenode_acme_cert_revoke" id="cli_pvenode_acme_cert_revoke"></a>

向 CA 吊销现有证书。

## **pvenode acme plugin add** `<type> <id>` `[OPTIONS]` <a href="#cli_pvenode_acme_plugin_add" id="cli_pvenode_acme_plugin_add"></a>

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

**`--validation-delay` `<integer> (0 - 172800)` （*默认值 \=* `30`）**

请求验证前额外等待的延迟，单位为秒。用于应对 DNS 记录 TTL 较长的情况。

## **pvenode acme plugin config** `<id>` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_plugin_config" id="cli_pvenode_acme_plugin_config"></a>

获取 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件实例的唯一标识符。

## **pvenode acme plugin list** `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_acme_plugin_list" id="cli_pvenode_acme_plugin_list"></a>

ACME 插件索引。

**`--type` `<dns | standalone>`**

仅列出指定类型的 ACME 插件

## **pvenode acme plugin remove** `<id>` <a href="#cli_pvenode_acme_plugin_remove" id="cli_pvenode_acme_plugin_remove"></a>

删除 ACME 插件配置。

**`<id>`: `<string>`**

ACME 插件实例的唯一标识符。

## **pvenode acme plugin set** `<id>` `[OPTIONS]` <a href="#cli_pvenode_acme_plugin_set" id="cli_pvenode_acme_plugin_set"></a>

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

**`--validation-delay` `<integer> (0 - 172800)` （*默认值 \=* `30`）**

请求验证前额外等待的延迟，单位为秒。用于应对 DNS 记录 TTL 较长的情况。

## **pvenode cert delete** `[<restart>]` <a href="#cli_pvenode_cert_delete" id="cli_pvenode_cert_delete"></a>

删除自定义证书链和密钥。

**`<restart>`: `<boolean>` （*默认值 \=* `0`）**

重启 pveproxy。

## **pvenode cert info** `[FORMAT_OPTIONS]` <a href="#cli_pvenode_cert_info" id="cli_pvenode_cert_info"></a>

获取有关节点证书的信息。

## **pvenode cert set** `<certificates> [<key>]` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_cert_set" id="cli_pvenode_cert_set"></a>

上传或更新自定义证书链和密钥。

**`<certificates>`: `<string>`**

PEM 编码的证书（链）。

**`<key>`: `<string>`**

PEM 编码的私钥。

**`--force` `<boolean>`（*默认 \=* `0`）**

覆盖现有自定义证书文件或 ACME 证书文件。

**`--restart` `<boolean>` （*默认值 \=* `0`）**

重启 pveproxy。

## **pvenode config get** `[OPTIONS]` <a href="#cli_pvenode_config_get" id="cli_pvenode_config_get"></a>

获取节点配置选项。

**`--property` `<acme | acmedomain0 | acmedomain1 | acmedomain2 | acmedomain3 | acmedomain4 | acmedomain5 | ballooning-target | description | location | startall-onboot-delay | wakeonlan>` （*默认值 \=* `all`）**

仅返回节点配置中的指定属性。

## **pvenode config set** `[OPTIONS]` <a href="#cli_pvenode_config_set" id="cli_pvenode_config_set"></a>

设置节点配置选项。

**`--acme` `[account=<name>] [,domains=<domain[;domain;...]>]`**

节点特定的 ACME 设置。

**`--acmedomain[n]` `[domain=]<domain> [,alias=<domain>] [,plugin=<name of the plugin configuration>]`**

ACME 域和验证插件

**`--ballooning-target` `<integer> (0 - 100)` （*默认值 \=* `80`）**

内存气球的 RAM 使用率目标（占总内存的百分比）

**`--delete` `<string>`**

要删除的设置列表。

**`--description` `<string>`**

节点描述。显示在 Web 界面的节点备注面板中。以注释形式保存在配置文件内。

**`--digest` `<string>`**

如果当前配置文件的 SHA1 摘要不同，则阻止更改。这可用于防止并发修改。

**`--location` `latitude=<number> ,longitude=<number> [,name=<name>]`**

节点的位置。覆盖数据中心配置中的默认值。

**`--startall-onboot-delay` `<integer> (0 - 300)` （*默认值 \=* `0`）**

启动所有已启用开机启动的虚拟客户机之前的初始延迟，单位为秒。

**`--wakeonlan` `[mac=]<MAC address> [,bind-interface=<bind interface>] [,broadcast-address=<IPv4 broadcast address>]`**

节点特定的网络唤醒设置。

## **pvenode help** `[OPTIONS]` <a href="#cli_pvenode_help" id="cli_pvenode_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pvenode migrateall** `<target>` `[OPTIONS]` <a href="#cli_pvenode_migrateall" id="cli_pvenode_migrateall"></a>

迁移所有虚拟机和容器。

**`<target>`: `<string>`**

目标节点。

**`--max-workers` `<integer> (1 - 64)`**

并行迁移任务的最大数量。如果未设置，则使用 max\_workers，其值来自 datacenter.cfg。两者必须至少设置一个！

**`--maxworkers` `<integer> (1 - 64)`**

并行迁移任务的最大数量。如果未设置，则使用 max\_workers，其值来自 datacenter.cfg。两者必须至少设置一个！已弃用，请改用 *max-workers*。

**`--vms` `<string>`**

仅考虑具有这些 ID 的客户机。

**`--with-local-disks` `<boolean>`**

对本地磁盘启用在线存储迁移

## **pvenode startall** `[OPTIONS]` <a href="#cli_pvenode_startall" id="cli_pvenode_startall"></a>

启动此节点上的所有虚拟机和容器（默认只启动设置了 onboot\=1 的客户机）。

**`--force` `<boolean>` （*默认值 \=* `off`）**

即使虚拟客户机未设置 *onboot* 或将其设置为 off，也发出启动命令。

**`--max-workers` `<integer> (1 - 64)`**

定义同时运行任务的最大数量。如果未设置，则使用 *max\_workers*，其值来自 datacenter.cfg；如果该值也未设置，则使用可用 CPU 线程数，但最多为 8。

**`--vms` `<string>`**

仅考虑此逗号分隔的 VMID 列表中的客户机。

## **pvenode stopall** `[OPTIONS]` <a href="#cli_pvenode_stopall" id="cli_pvenode_stopall"></a>

停止所有虚拟机和容器。

**`--force-stop` `<boolean>` （*默认值 \=* `1`）**

超时后强制停止。

**`--max-workers` `<integer> (1 - 64)`**

定义同时运行任务的最大数量。如果未设置，则使用 *max\_workers*，其值来自 datacenter.cfg；如果该值也未设置，则使用可用 CPU 线程数，但最多为 8。

**`--timeout` `<integer> (0 - 7200)` （*默认值 \=* `180`）**

每个客户机关机任务的超时时间。随后根据 `force-stop` 的设置，直接中止关机或强制停止。

**`--vms` `<string>`**

仅考虑具有这些 ID 的客户机。

## **pvenode task list** `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_task_list" id="cli_pvenode_task_list"></a>

读取某个节点的任务列表（已完成任务）。

**`--errors` `<boolean>` （*默认值 \=* `0`）**

仅列出状态为 ERROR 的任务。

**`--limit` `<integer> (0 - N)` （*默认值 \=* `50`）**

仅列出此数量的任务。

**`--since` `<integer>`**

仅列出此 UNIX 纪元时间之后的任务。

**`--source` `<active | all | archive>` （*默认值 \=* `archive`）**

列出已归档、活动或全部任务。

**`--start` `<integer> (0 - N)` （*默认值 \=* `0`）**

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

## **pvenode task log** `<upid>` `[OPTIONS]` <a href="#cli_pvenode_task_log" id="cli_pvenode_task_log"></a>

读取任务日志。

**`<upid>`: `<string>`**

任务的唯一 ID。

**`--download` `<boolean>`**

是否应下载任务日志文件。此参数不能与其他参数同时使用

**`--start` `<integer> (0 - N)` （*默认值 \=* `0`）**

读取任务日志时从此行开始

## **pvenode task status** `<upid>` `[FORMAT_OPTIONS]` <a href="#cli_pvenode_task_status" id="cli_pvenode_task_status"></a>

读取任务状态。

**`<upid>`: `<string>`**

任务的唯一 ID。

## **pvenode wakeonlan** `<node>` <a href="#cli_pvenode_wakeonlan" id="cli_pvenode_wakeonlan"></a>

尝试通过*网络唤醒*数据包唤醒节点。

**`<node>`: `<string>`**

网络唤醒数据包的目标节点

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
