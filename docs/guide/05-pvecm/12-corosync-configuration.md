# 5.12. Corosync Configuration <a href="#_corosync_configuration" id="_corosync_configuration"></a>

`/etc/pve/corosync.conf` 文件在 Proxmox VE 集群中起着核心作用。它控制集群成员关系及其网络。有关更多信息，请查看 corosync.conf 手册页：

```text
man corosync.conf
```

对于节点成员关系，您应始终使用 Proxmox VE 提供的 `pvecm` 工具。对于其他更改，您可能需要手动编辑配置文件。以下是一些执行此操作的最佳实践建议。

## 5.12.1. Edit corosync.conf <a href="#pvecm_edit_corosync_conf" id="pvecm_edit_corosync_conf"></a>

编辑 corosync.conf 文件并不总是很简单直接。每个集群节点上都有两个该文件，一个位于 `/etc/pve/corosync.conf`，另一个位于 `/etc/corosync/corosync.conf`。编辑集群文件系统中的文件会将更改传播到本地文件，但反之则不会。

文件一旦发生更改，配置就会自动更新。这意味着，可在正在运行的 corosync 中集成的更改会立即生效。因此，您应始终先创建一个副本并编辑该副本，以避免在编辑过程中保存文件时触发意外更改。

```text
cp /etc/pve/corosync.conf /etc/pve/corosync.conf.new
```

然后，使用您喜欢的编辑器打开配置文件，例如每个 Proxmox VE 节点上都预装的 `nano` 或 `vim.tiny`。

{% hint style="info" %}
配置更改后，务必递增 *config\_version* 编号；省略此操作可能会导致问题。
{% endhint %}

完成必要的更改后，再创建一份当前工作配置文件的副本。如果新配置无法应用或引发其他问题，此副本可用作备份。

```text
cp /etc/pve/corosync.conf /etc/pve/corosync.conf.bak
```

然后，用新配置文件替换旧配置文件：

```text
mv /etc/pve/corosync.conf.new /etc/pve/corosync.conf
```

您可以使用以下命令检查更改是否可以自动应用：

```text
systemctl status corosync
journalctl -b -u corosync
```

如果更改无法自动应用，您可能需要通过以下命令重启 corosync 服务：

```text
systemctl restart corosync
```

出现错误时，请查看下面的故障排除部分。

## 5.12.2. Changing the Token Coefficient <a href="#pvecm_changing_token_coefficient" id="pvecm_changing_token_coefficient"></a>

The token coefficient can be configured in the `totem` section in `/etc/pve/corosync.conf`. If the token coefficient is not explicitly set, it defaults to 650 milliseconds. Since Proxmox VE 9.2, new clusters are created with a lower token coefficient of 125 milliseconds explicitly set in `/etc/pve/corosync.conf`. This reduces the time needed for reestablishing a new cluster membership after a node failure.

corosync 使用令牌系数，根据集群规模计算多个超时时间[\[1\]](#note-92024276-1)，其中最重要的是令牌超时和共识超时。corosync 实现了令牌传递协议。令牌超时指定节点等待令牌多长时间后会声明令牌丢失[\[2\]](#note-92024276-2)。共识超时[\[3\]](#note-92024276-3)指定节点就新的集群成员关系达成共识的等待时间。令牌超时与共识超时之和，定义了节点离线后重新建立新集群成员关系所需的最短时间。

将令牌超时与共识超时之和保持在 30 秒以下，可缩短节点故障后重新建立新集群成员关系所需的时间。启用 HA 时，尤其重要的是将此时间保持在 45 秒以下，以确保在 60 秒的[看门狗超时](../15-ha-manager/04-how-it-works-2.md#ha_manager_crm)到期之前形成新的集群成员关系，否则会触发节点隔离。建议在此 45 秒限制以下留出安全余量，以免短暂的时间波动使集群超过看门狗阈值。如下面所述，降低令牌和共识超时的推荐机制是降低令牌系数。

您可以使用以下命令检查当前的令牌超时和共识超时（以毫秒为单位）：

```text
corosync-cmapctl | grep -Ew 'runtime.config.totem.token|runtime.config.totem.consensus'
```

例如：

```text
runtime.config.totem.consensus (u32) = 5940
runtime.config.totem.token (u32) = 4950
```

这两个值之和（示例中为 10.89 秒）定义了节点离线后重新建立新集群成员关系所需的最短时间。降低令牌系数是

- 如果该值超过 30 秒，建议进行的一项优化，
- 如果超过 40 秒，则建议这样做，
- 如果超过 45 秒，则强烈建议这样做。

要降低令牌系数，首先请确保您的设置符合[网络要求](08-pvecm-cluster-network.md#pvecm_cluster_network_requirements)，尤其是在延迟方面。然后：

- If the `token_coefficient` is not yet set explicitly to 125 milliseconds in corosync.conf, [edit corosync.conf](#pvecm_edit_corosync_conf) and add `token_coefficient: 125` to the `totem` section. Do not forget to [increase the `config_version`](#pvecm_edit_corosync_conf).
- 否则，如果 125 毫秒仍不足以将超时时间保持在上述限制内，请选择一个 `token_coefficient`，使令牌超时与共识超时之和最多为 45 秒。默认情况下，corosync 按以下公式计算令牌超时和共识超时（以毫秒为单位）：

  ```text
  token = 3000 + (number_of_nodes - 2) * token_coefficient
  consensus = 1.2 * token
  ```

  [Edit corosync.conf](#pvecm_edit_corosync_conf) and set an appropriate `token_coefficient` option in the `totem` section. Do not forget to [increase the `config_version`](#pvecm_edit_corosync_conf). Test your setup thoroughly for stability!

After adjusting the `token_coefficient` in `corosync.conf`, recent corosync versions will automatically adopt the new value for the cluster. For corosync versions below `3.1.10-pve1`, corosync needs to be restarted on all nodes for the change to take effect.

## 5.12.3. Troubleshooting <a href="#_troubleshooting" id="_troubleshooting"></a>

### Issue: *quorum.expected\_votes must be configured* <a href="#_issue_em_quorum_expected_votes_must_be_configured_em" id="_issue_em_quorum_expected_votes_must_be_configured_em"></a>

当 corosync 启动失败并且您在系统日志中收到以下消息时：

```text
[...]
corosync[1647]:  [QUORUM] Quorum provider: corosync_votequorum failed to initialize.
corosync[1647]:  [SERV  ] Service engine 'corosync_quorum' failed to load for reason
    'configuration error: nodelist or quorum.expected_votes must be configured!'
[...]
```

这意味着配置中为 corosync *ringX\_addr* 设置的主机名无法解析。

### Write Configuration When Not Quorate <a href="#_write_configuration_when_not_quorate" id="_write_configuration_when_not_quorate"></a>

如果您需要在无仲裁的节点上更改 */etc/pve/corosync.conf*，并且了解自己在做什么，请使用：

```text
pvecm expected 1
```

这会将预期票数设置为 1，并使集群达到仲裁。然后，您可以修复配置，或将其恢复为最后一个可用的备份。

如果 corosync 已无法启动，仅这样做还不够。在这种情况下，最好编辑 */etc/corosync/corosync.conf* 中 corosync 配置的本地副本，以便 corosync 能够再次启动。确保所有节点上的此配置内容相同，以避免脑裂。

## 5.12.4. Corosync Configuration Glossary <a href="#pvecm_corosync_conf_glossary" id="pvecm_corosync_conf_glossary"></a>

**ringX\_addr**

此项为节点之间 Kronosnet 连接的不同链路地址命名。

## 注释

### 注释 1 <a href="#note-92024276-1" id="note-92024276-1"></a>

`token_coefficient`（见 corosync 手册页）[https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token\_coefficient](https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token_coefficient)

### 注释 2 <a href="#note-92024276-2" id="note-92024276-2"></a>

`token`（见 corosync 手册页）[https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token](https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#token)

### 注释 3 <a href="#note-92024276-3" id="note-92024276-3"></a>

`consensus`（见 corosync 手册页）[https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#consensus](https://manpages.debian.org/stable/corosync/corosync.conf.5.en.html#consensus)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
