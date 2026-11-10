# 5.12. Corosync Configuration <a href="#_corosync_configuration" id="_corosync_configuration"></a>

The `/etc/pve/corosync.conf` file plays a central role in a Proxmox VE cluster. It controls the cluster membership and its network. For further information about it, check the corosync.conf man page:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
man corosync.conf
```

For node membership, you should always use the `pvecm` tool provided by Proxmox VE. You may have to edit the configuration file manually for other changes. Here are a few best practice tips for doing this.

## 5.12.1. Edit corosync.conf <a href="#pvecm_edit_corosync_conf" id="pvecm_edit_corosync_conf"></a>

Editing the corosync.conf file is not always very straightforward. There are two on each cluster node, one in `/etc/pve/corosync.conf` and the other in `/etc/corosync/corosync.conf`. Editing the one in our cluster file system will propagate the changes to the local one, but not vice versa.

The configuration will get updated automatically, as soon as the file changes. This means that changes which can be integrated in a running corosync will take effect immediately. Thus, you should always make a copy and edit that instead, to avoid triggering unintended changes when saving the file while editing.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
cp /etc/pve/corosync.conf /etc/pve/corosync.conf.new
```

Then, open the config file with your favorite editor, such as `nano` or `vim.tiny`, which come pre-installed on every Proxmox VE node.

{% hint style="info" %}
Always increment the *config_version* number after configuration changes; omitting this can lead to problems.
{% endhint %}

After making the necessary changes, create another copy of the current working configuration file. This serves as a backup if the new configuration fails to apply or causes other issues.

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
cp /etc/pve/corosync.conf /etc/pve/corosync.conf.bak
```

Then replace the old configuration file with the new one:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
mv /etc/pve/corosync.conf.new /etc/pve/corosync.conf
```

You can check if the changes could be applied automatically, using the following commands:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
systemctl status corosync
journalctl -b -u corosync
```

If the changes could not be applied automatically, you may have to restart the corosync service via:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
systemctl restart corosync
```

On errors, check the troubleshooting section below.

## 5.12.2. Changing the Token Coefficient <a href="#pvecm_changing_token_coefficient" id="pvecm_changing_token_coefficient"></a>

The token coefficient can be configured in the `totem` section in `/etc/pve/corosync.conf`. If the token coefficient is not explicitly set, it defaults to 650 milliseconds. Since Proxmox VE 9.2, new clusters are created with a lower token coefficient of 125 milliseconds explicitly set in `/etc/pve/corosync.conf`. This reduces the time needed for reestablishing a new cluster membership after a node failure.

corosync uses the token coefficient to calculate several timeouts in relation to the cluster size   
[`token_coefficient` in the corosync manual page [https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token_coefficient](https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token_coefficient)]  
, most importantly the token timeout and consensus timeout. corosync implements a token-passing protocol. The token timeout specifies how long a node waits for the token until it declares the token to be lost   
[`token` in the corosync manual page [https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token](https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token)]  
. The consensus timeout   
[`consensus` in the corosync manual page [https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#consensus](https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#consensus)]  
 specifies the time nodes wait for a consensus on a new cluster membership. The sum of token and consensus timeouts defines the minimum time needed to reestablish a new cluster membership after a node goes offline.

Keeping the sum of token and consensus timeouts below 30 seconds reduces the time needed for reestablishing a new cluster membership after a node failure. When HA is enabled, it is especially important that this time stays below 45 seconds to ensure that a new cluster membership is formed before the [watchdog timeout](../15-ha-manager/04-how-it-works-2.md#ha_manager_crm) of 60 seconds expires, which would trigger a node fence. A safety margin below this 45 second limit is advisable so that transient timing variations do not push the cluster past the watchdog threshold. The recommended mechanism for lowering the token and consensus timeouts is lowering the token coefficient as explained below.

You can check the current token and consensus timeouts (in milliseconds) with the following command:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
corosync-cmapctl | grep -Ew 'runtime.config.totem.token|runtime.config.totem.consensus'
```

For example:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
runtime.config.totem.consensus (u32) = 5940
runtime.config.totem.token (u32) = 4950
```

The sum of these two values (10.89 seconds in the example) defines the minimum time needed to reestablish a new cluster membership after a node goes offline. Lowering the token coefficient is

- a suggested optimization if this value exceeds 30 seconds,
- recommended if it exceeds 40 seconds,
- strongly recommended if it exceeds 45 seconds.

To lower the token coefficient, first make sure your setup adheres [to the network requirements](08-pvecm-cluster-network.md#pvecm_cluster_network_requirements), especially with regards to latency. Then:

- If the `token_coefficient` is not yet set explicitly to 125 milliseconds in corosync.conf, [edit corosync.conf](#pvecm_edit_corosync_conf) and add `token_coefficient: 125` to the `totem` section. Do not forget to [increase the `config_version`](#pvecm_edit_corosync_conf).
- Otherwise, if 125 milliseconds is not low enough to keep the timeouts within the limits above, select a `token_coefficient` with which the token and consensus timeouts sum up to at most 45 seconds. By default, corosync computes the token and consensus timeouts (in milliseconds) according to the following formula:

  ```text
  token = 3000 + (number_of_nodes - 2) * token_coefficient
  consensus = 1.2 * token
  ```

  [Edit corosync.conf](#pvecm_edit_corosync_conf) and set an appropriate `token_coefficient` option in the `totem` section. Do not forget to [increase the `config_version`](#pvecm_edit_corosync_conf). Test your setup thoroughly for stability!

After adjusting the `token_coefficient` in `corosync.conf`, recent corosync versions will automatically adopt the new value for the cluster. For corosync versions below `3.1.10-pve1`, corosync needs to be restarted on all nodes for the change to take effect.

## 5.12.3. Troubleshooting <a href="#_troubleshooting" id="_troubleshooting"></a>

### Issue: *quorum.expected_votes must be configured* <a href="#_issue_em_quorum_expected_votes_must_be_configured_em" id="_issue_em_quorum_expected_votes_must_be_configured_em"></a>

When corosync starts to fail and you get the following message in the system log:

```text
[...]
corosync[1647]:  [QUORUM] Quorum provider: corosync_votequorum failed to initialize.
corosync[1647]:  [SERV  ] Service engine 'corosync_quorum' failed to load for reason
    'configuration error: nodelist or quorum.expected_votes must be configured!'
[...]
```

It means that the hostname you set for a corosync *ringX_addr* in the configuration could not be resolved.

### Write Configuration When Not Quorate <a href="#_write_configuration_when_not_quorate" id="_write_configuration_when_not_quorate"></a>

If you need to change */etc/pve/corosync.conf* on a node with no quorum, and you understand what you are doing, use:

Generator: GNU source-highlight by Lorenzo Bettini http://www.lorenzobettini.it http://www.gnu.org/software/src-highlite

```text
pvecm expected 1
```

This sets the expected vote count to 1 and makes the cluster quorate. You can then fix your configuration, or revert it back to the last working backup.

This is not enough if corosync cannot start anymore. In that case, it is best to edit the local copy of the corosync configuration in */etc/corosync/corosync.conf*, so that corosync can start again. Ensure that on all nodes, this configuration has the same content to avoid split-brain situations.

## 5.12.4. Corosync Configuration Glossary <a href="#pvecm_corosync_conf_glossary" id="pvecm_corosync_conf_glossary"></a>

**ringX_addr**

This names the different link addresses for the Kronosnet connections between nodes.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
