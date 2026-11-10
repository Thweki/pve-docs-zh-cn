# 22.13. **pvecm** - Proxmox VE Cluster Manager <a href="#_strong_pvecm_strong_proxmox_ve_cluster_manager" id="_strong_pvecm_strong_proxmox_ve_cluster_manager"></a>

<a id="cli_pvecm"></a>



**pvecm** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pvecm_add"></a>



**pvecm add** `<hostname>` `[OPTIONS]`

Adds the current node to an existing cluster.

**`<hostname>`: `<string>`**

Hostname (or IP) of an existing cluster member.

**`--fingerprint` `([A-Fa-f0-9]{2}:){31}[A-Fa-f0-9]{2}`**

Certificate SHA 256 fingerprint.

**`--force` `<boolean>`**

Do not throw error if node already exists.

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)

**`--nodeid` `<integer> (1 - N)`**

Node id for this node.

**`--use_ssh` `<boolean>`**

Always use SSH to join, even if peer may do it over API.

**`--votes` `<integer> (0 - N)`**

Number of votes for this node

<a id="cli_pvecm_addnode"></a>



**pvecm addnode** `<node>` `[OPTIONS]`

Adds a node to the cluster configuration. This call is for internal use.

**`<node>`: `<string>`**

集群节点名称。

**`--apiversion` `<integer>`**

The JOIN_API_VERSION of the new node.

**`--force` `<boolean>`**

Do not throw error if node already exists.

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)

**`--new_node_ip` `<string>`**

IP Address of node to add. Used as fallback if no links are given.

**`--nodeid` `<integer> (1 - N)`**

Node id for this node.

**`--votes` `<integer> (0 - N)`**

Number of votes for this node

<a id="cli_pvecm_apiver"></a>



**pvecm apiver**

Return the version of the cluster join API available on this node.

<a id="cli_pvecm_create"></a>



**pvecm create** `<clustername>` `[OPTIONS]`

Generate new cluster configuration. If no links given, default to local IP address as link0.

**`<clustername>`: `<string>`**

The name of the cluster.

**`--link[n]` `[address=]<IP> [,priority=<integer>]`**

Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)

**`--nodeid` `<integer> (1 - N)`**

Node id for this node.

**`--token-coefficient` `<integer> (0 - N)` (*default =* `125`)**

Coefficient used to determine Corosync’s token timeout. See the corosync.conf(5) manual for more details.

**`--votes` `<integer> (1 - N)`**

Number of votes for this node.

<a id="cli_pvecm_delnode"></a>



**pvecm delnode** `<node>`

Removes a node from the cluster configuration.

**`<node>`: `<string>`**

集群节点名称。

<a id="cli_pvecm_expected"></a>



**pvecm expected** `<expected>`

Tells corosync a new value of expected votes.

**`<expected>`: `<integer> (1 - N)`**

Expected votes

<a id="cli_pvecm_help"></a>



**pvecm help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pvecm_keygen"></a>



**pvecm keygen** `<filename>`

Generate new cryptographic key for corosync.

**`<filename>`: `<string>`**

Output file name

<a id="cli_pvecm_mtunnel"></a>



**pvecm mtunnel** `[<extra-args>]` `[OPTIONS]`

Used by VM/CT migration - do not use manually.

**`<extra-args>`: `<array>`**

以数组形式提供的额外参数

**`--get_migration_ip` `<boolean>` (*default =* `0`)**

return the migration IP, if configured

**`--migration_network` `<string>`**

the migration network used to detect the local migration IP

**`--run-command` `<boolean>`**

Run a command with a tcp socket as standard input. The IP address and port are printed via this command’s stdandard output first, each on a separate line.

<a id="cli_pvecm_nodes"></a>



**pvecm nodes**

Displays the local view of the cluster nodes.

<a id="cli_pvecm_qdevice_remove"></a>



**pvecm qdevice remove**

Remove a configured QDevice

<a id="cli_pvecm_qdevice_setup"></a>



**pvecm qdevice setup** `<address>` `[OPTIONS]`

Setup the use of a QDevice

**`<address>`: `<string>`**

Specifies the network address of an external corosync QDevice

**`--force` `<boolean>`**

Do not throw error on possible dangerous operations.

**`--network` `<string>`**

The network which should be used to connect to the external qdevice

<a id="cli_pvecm_status"></a>



**pvecm status**

Displays the local view of the cluster status.

<a id="cli_pvecm_updatecerts"></a>



**pvecm updatecerts** `[OPTIONS]`

Update node certificates (and generate all needed files/directories).

**`--force` `<boolean>`**

Force generation of new SSL certificate.

**`--silent` `<boolean>`**

Ignore errors (i.e. when cluster has no quorum).

**`--unmerge-known-hosts` `<boolean>` (*default =* `0`)**

Unmerge legacy SSH known hosts.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
