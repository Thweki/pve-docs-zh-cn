# 22.7. **pvenode** \- Proxmox VE Node Management <a href="#_strong_pvenode_strong_proxmox_ve_node_management" id="_strong_pvenode_strong_proxmox_ve_node_management"></a>

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

**`--force` `<boolean>` (*default \=* `0`)**

Overwrite existing custom certificate.

<a id="cli_pvenode_acme_cert_renew"></a>



**pvenode acme cert renew** `[OPTIONS]`

Renew existing certificate from CA.

**`--force` `<boolean>` (*default \=* `0`)**

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

**`--force` `<boolean>` (*default \=* `0`)**

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

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
