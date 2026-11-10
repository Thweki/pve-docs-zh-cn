# 8.14. Ceph 维护 <a href="#_ceph_maintenance" id="_ceph_maintenance"></a>

## 8.14.1. 替换 OSD <a href="#pve_ceph_osd_replace" id="pve_ceph_osd_replace"></a>

通过以下步骤，您可以替换 OSD 的磁盘，这是 Ceph 中最常见的维护任务之一。如果 OSD 出现问题，但其磁盘看起来仍然正常，请先阅读 [故障排除](15-pve-ceph-mon-and-ts.md) 部分。

1. 如果磁盘发生故障，请准备一块 [推荐](03-recommendations-for-a-healthy-ceph-cluster.md#pve_ceph_recommendation_disk) 的、类型和大小相同的替换磁盘。
2. [销毁](07-pve-ceph-osds.md#pve_ceph_osd_destroy) 相关 OSD。
3. 从服务器上卸下旧磁盘并安装新磁盘。
4. [重新创建](07-pve-ceph-osds.md#pve_ceph_osd_create) 该 OSD。
5. 自动重新平衡后，集群状态应恢复为 `HEALTH_OK`。对于仍列出的任何崩溃记录，可以运行以下命令予以确认：

```text
ceph crash archive-all
```

## 8.14.2. Trim/Discard <a href="#_trim_discard" id="_trim_discard"></a>

定期在虚拟机和容器中运行 *fstrim*（discard）是一种良好做法。这会释放文件系统不再使用的数据块，从而减少数据占用和资源负载。大多数现代操作系统都会定期向其磁盘发出此类 discard 命令。您只需确保虚拟机启用 [磁盘丢弃选项](../10-virtual-machines/02-qm-virtual-machines-settings.md#qm_hard_disk_discard)。

## 8.14.3. 擦洗与深度擦洗 <a href="#pveceph_scrub" id="pveceph_scrub"></a>

Ceph 通过对归置组进行 *擦洗* 来确保数据完整性。Ceph 会检查 PG 中每个对象的健康状况。擦洗分为两种形式：每天进行的低成本元数据检查和每周进行的深度数据检查。每周深度擦洗会读取对象并使用校验和来确保数据完整性。如果正在运行的擦洗干扰业务（性能）需求，您可以调整执行擦洗 [\[1\]](#note-4de62a9e-1) 的时间。

## 8.14.4. 将健康检查静音 <a href="#pveceph_mute_health_check" id="pveceph_mute_health_check"></a>

将健康检查静音后，它仍然可见，但会被排除在总体健康状态之外，从而更容易发现新问题。Ceph 会继续评估该检查。请设置一个持续时间，以便被暂缓的警告自动恢复，例如两周后：

```text
ceph health mute <CHECK> 2w
```

在 Web 界面中，展开 **数据中心 → Ceph** 下的检查，点击 *静音*，并设置持续时间。该检查会保留在列表中，并标记为已静音；如需提前恢复，请在同一位置使用 *取消静音*。

默认情况下，当更多项目受到影响时，静音会被清除。仅当希望在这种情况下仍保持静音时，才启用 *保持静音*，或在命令中添加 `--sticky`。这不会改变持续时间：设置了持续时间的粘性静音仍会到期。

{% hint style="info" %}
静音并不能解决该状况。在静音持续期间，即表示您接受其风险。
{% endhint %}

## 8.14.5. 将 Cephx 密钥从 `aes` 迁移到 `aes256k` <a href="#pveceph_cephx_migration" id="pveceph_cephx_migration"></a>

本节介绍如何将集群拥有的密钥和兼容 Ceph 用户的密钥从 `aes` 迁移到 `aes256k`。有关 Ceph 用户、票据和密钥存储的说明，请参阅 [Cephx 身份验证](11-pveceph-cephx-how-it-works.md)。

### 为什么会出现这些健康检查 <a href="#_why_the_health_checks_appear" id="_why_the_health_checks_appear"></a>

Ceph Squid 19.2.6 和 Ceph Tentacle 20.2.4 针对使用较旧 `aes` 加密方法的密钥和临时访问凭据新增了健康检查。因此，即使集群在升级前运行时没有警告，这些检查也可能在升级后立即出现。较旧的方法受 [*CVE-2025-30156*](https://docs.ceph.com/en/latest/security/CVE-2025-30156) 影响。有关背景信息，请参阅上游发布公告 [\[2\]](#note-4de62a9e-2)。

两项检查会将集群状态设置为 *HEALTH\_ERR*。这并不意味着存储访问或某个 Ceph 服务发生故障。请按照以下步骤迁移到 `aes256k`，并在所有客户端都支持后，禁用这种易受攻击的方法。

### 迁移步骤 <a href="#pveceph_cephx_migration_helper" id="pveceph_cephx_migration_helper"></a>

迁移辅助工具会检查集群、轮换密钥，并继续中断的工作。在应用计划之前，请检查每次试运行的结果；添加 `--verbose` 可获取完整的节点、密钥环和设备清单以及检查诊断信息。

重复运行不会再次轮换已完成的密钥。每次运行后，请不带选项调用辅助工具，以检查当前状态并按照其输出的后续步骤操作。

**开始之前**

- 将 `pve-manager` 升级到 9.2.19 或更新版本，并在每个节点上安装最新的 Ceph 软件包。分阶段客户端密钥轮换要求每个监视器上都安装 Ceph 19.2.6-pve3、20.2.4-pve3 或更新版本。
- 然后完成所有 Ceph 服务的滚动重启。
- 解决 [健康检查参考](#pveceph_cephx_health_check_reference) 中未列出的健康警告和错误。确保每个节点均可通过 SSH 访问。
- 仅以 `root` 身份在一个节点上运行辅助工具。在其运行期间，不要启动另一次迁移或滚动重启，也不要使用其他工具更改 Ceph 密钥。辅助工具的锁不会阻止直接执行 Ceph 身份验证命令。
- 如果此集群禁用了 Cephx，请改为按照 [禁用 Cephx 的集群](#pveceph_cephx_disabled) 中的说明操作。

#### 1\. 迁移集群拥有的密钥 <a href="#_1_migrate_the_cluster_owned_keys" id="_1_migrate_the_cluster_owned_keys"></a>

在默认试运行模式下检查集群拥有的密钥迁移计划：

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys --rotate-cluster-keys
```

如果计划未报告任何阻塞项，请应用相同的选择：

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys --rotate-cluster-keys --apply
```

辅助工具会轮换管理器、元数据服务器、OSD、监视器、bootstrap、crash 和 [加密 OSD 锁箱密钥](11-pveceph-cephx-how-it-works.md#pveceph_cephx_lockbox)。它会在需要时逐个重启服务，包括监视器。存储用户密钥和 `client.admin` 保持不变，现有票据仍然有效，旧加密算法保持启用。

Ceph 更新其健康状态后，两项错误级别的检查会清除。在旧的轮换密钥过期期间，有关轮换服务密钥的警告可能会持续几个小时。继续迁移之前，无需等待此警告清除。

#### 2\. 迁移兼容 Ceph 用户的密钥 <a href="#pveceph_cephx_migration_clients" id="pveceph_cephx_migration_clients"></a>

<a id="pveceph_cipher_support"></a>



**检查兼容性**

多个工作负载可以共享一个 Ceph 用户。仅当所有客户端（包括已断开连接的客户端和外部客户端）都支持 `aes256k` 时，才迁移其密钥。更新后的 Proxmox VE 软件包中的 Ceph 程序支持该功能；内核客户端要求 **正在运行** 的内核版本为 7.0 或更新。

<table>


<tbody>
<tr>
<td><p>使用 RBD 磁盘的虚拟机</p></td>
<td><p>用户空间，除非启用了 <code>krbd</code>。</p></td>
</tr>
<tr>
<td><p>RBD 上的容器</p></td>
<td><p>始终使用内核客户端。</p></td>
</tr>
<tr>
<td><p>CephFS 挂载</p></td>
<td><p>内核，除非启用了 <code>fuse</code>。</p></td>
</tr>
</tbody>
</table>

还要检查外部系统。如果任何受影响的客户端不兼容或情况未知，请保持其用户的密钥不变，并推迟此步骤。

**暂存密钥**

将 `--rotate-all-storage-keys` 用于托管的本地 RBD 和 CephFS 存储的专用用户，并将 `--rotate-admin-key` 用于 `client.admin`，后者由命令行和没有自己用户的存储共用。这些用户的每个客户端都会受到影响；外部集群的存储除外。

辅助程序会暂存每个新密钥，并将其写入托管的密钥环和机密密钥文件。在确认之前，两个密钥都保持有效，以便客户端在旧密钥停用前完成刷新。如果某个监视器无法让两个密钥同时保持有效，辅助程序会拒绝暂存，并指出需要更新或重启的监视器。

检查合并后的计划：

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys \
    --rotate-all-storage-keys --rotate-admin-key
```

如果计划未报告任何阻塞项，请应用该计划：

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys \
    --rotate-all-storage-keys --rotate-admin-key --apply
```

在某个密钥处于暂存状态期间，不要添加或降级监视器，也不要使用其他工具更改该用户的密钥。其 `AUTH_INSECURE_CLIENT_KEY_TYPE` 警告会一直保留，直到确认操作将新密钥设为当前密钥并使旧密钥失效。

<a id="pveceph_cephx_refresh_clients"></a>



**刷新客户端**

- 在 Web 界面中在线迁移受影响的虚拟机，或者将其停止后再启动。仅重启客户机是不够的。
- 停止并重新启动受影响的容器和其他 RBD 客户端。
- 在确认之前，让 Ceph 存储上的备份、恢复、磁盘导入和克隆操作完成；这些操作可能会一直保留其开始时使用的密钥。
- 辅助程序会刷新空闲的 CephFS 挂载，而不会处理繁忙或无响应的挂载。待这些挂载不再被使用后，使用 `--apply` 重新运行辅助程序，以重试尚未完成的挂载。如果您的虚拟机挂载了来自 CephFS 挂载的 ISO，您可能需要卸载这些 ISO，或者将受影响的虚拟机迁移到其他节点，才能刷新该节点上的 CephFS 挂载。
- 对于 Proxmox VE 之外的客户端，请从[托管的密钥文件](#pveceph_cephx_external_copies)中分发暂存凭据，然后重启或重新挂载这些客户端。

辅助程序会报告可能仍持有旧密钥的会话。客户端提示涵盖整个宿主机，并非会话归属信息或完整的工作负载清单。没有所属进程的套接字会单独列出。请自行检查已断开连接的客户端和外部密钥副本。

#### 3\. 完成或暂停迁移 <a href="#pveceph_cephx_finish" id="pveceph_cephx_finish"></a>

执行最后一次试运行，检查是否仍有使用旧密钥的会话。当其观察到的检查全部通过时，它会提供确认命令，但无法为您验证已断开连接的客户端或外部密钥副本。

```text
/usr/share/pve-manager/migrations/pve-cephx-rotate-service-keys
```

{% hint style="warning" %}
在此步骤之后，仍需要旧密钥或旧加密算法的客户端将无法通过身份验证。现有 I/O 可能看起来仍能正常工作，直到重新连接时才失败。不要使用 `--force` 绕过阻塞项。
{% endhint %}

检查已断开连接的客户端和外部副本后，运行试运行所打印的确切命令。当所有轮换都已就绪且没有密钥需要旧加密算法时，它将打印选项 `--apply --confirm-all-clients-refreshed
--restrict-ciphers`。

如果任何客户端仍不兼容，请保持其密钥不变并继续启用旧加密算法，而不是限制旧加密算法。您可以在等待这些客户端升级期间[将剩余警告静音](#pveceph_mute_health_check)。

使用 `pveceph auth status` 查看当前和待处理的密钥加密算法，因为 `ceph auth ls` 不会列出待处理的密钥。

{% hint style="info" %}
`/etc/pve/priv/cephx-key-migration.json` 会记录进度，并包含保密的旧密钥。请妥善保护它，并一直保留到迁移完成且每个客户端都已刷新。过早删除它会丢失恢复迁移所需的记录。
{% endhint %}

### 其他迁移详情 <a href="#_additional_migration_details" id="_additional_migration_details"></a>

#### 健康检查参考 <a href="#pveceph_cephx_health_check_reference" id="pveceph_cephx_health_check_reference"></a>

<table>



<thead>
<tr>
<th>健康检查</th>
<th>含义</th>
<th>操作</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>AUTH_INSECURE_SERVICE_KEY_TYPE</code></p></td>
<td><p>某个 Ceph 服务密钥使用了旧加密算法。</p></td>
<td><p>运行由集群负责的迁移。此检查的严重级别为错误。</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_SERVICE_TICKETS</code></p></td>
<td><p>监视器使用旧加密算法签发服务票据。</p></td>
<td><p>运行由集群负责的迁移。此检查的严重级别为错误。</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_CLIENT_KEY_TYPE</code></p></td>
<td><p>某个 Ceph 用户的活动密钥使用了旧加密算法。已暂存密钥的用户会一直列在其中，直到其轮换得到确认。</p></td>
<td><p>轮换兼容用户的密钥并确认轮换，或者将警告静音。</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_ROTATING_SERVICE_KEY_TYPE</code></p></td>
<td><p>正在轮换的服务密钥使用了旧加密算法。</p></td>
<td><p>继续迁移；正在轮换的旧密钥会自动过期，不会妨碍最终限制加密算法。</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_KEYS_ALLOWED</code></p></td>
<td><p>监视器接受旧加密算法。</p></td>
<td><p>完成迁移，或者在仍有旧客户端期间将警告静音。</p></td>
</tr>
<tr>
<td><p><code>AUTH_INSECURE_KEYS_CREATABLE</code></p></td>
<td><p>监视器可以创建使用旧加密算法的密钥。</p></td>
<td><p>完成迁移，或者在仍有旧客户端期间将警告静音。</p></td>
</tr>
</tbody>
</table>

#### 禁用 Cephx 的集群 <a href="#pveceph_cephx_disabled" id="pveceph_cephx_disabled"></a>

Ceph 会根据存储的密钥和加密算法设置评估这些健康检查，即使禁用了 Cephx 也是如此，也就是当 `auth_cluster_required`、`auth_service_required` 和 `auth_client_required` 设置为 `none` 时。因此，禁用 Cephx 并不会清除这些检查，而更改身份验证方法会中断现有客户端，之后需要重启或重新挂载这些客户端。

在禁用 Cephx 的集群上：

1. 运行不带选项的辅助程序并应用其计划。它会迁移管理器、元数据服务器和 OSD 密钥，在需要时逐个重启服务，并将服务票据切换到新加密算法。这会清除两个严重级别为错误的检查。如果身份验证数据库中存储了旧的 `mon.` 密钥，辅助程序会改为拒绝执行，并要求您先迁移该密钥。
2. 可以选择使用 `--rotate-client-keys` 迁移 bootstrap 和 crash 密钥。
3. 在不设置时长的情况下将剩余警告静音。禁用 Cephx 期间，辅助程序不会迁移其他 Ceph 用户的密钥，因为其客户端不使用 Cephx 进行身份验证：

   ```text
   ceph health mute AUTH_INSECURE_CLIENT_KEY_TYPE --sticky
   ceph health mute AUTH_INSECURE_KEYS_ALLOWED --sticky
   ceph health mute AUTH_INSECURE_KEYS_CREATABLE --sticky
   ```

当首选加密算法仍为 `aes` 时，不要手动限制允许的加密算法或禁止创建使用旧加密算法的密钥，否则创建密钥会失败。

在重新启用 Cephx 之前，请取消这些检查的静音，并确保每个监视器、Ceph 服务和客户端仍具有与身份验证数据库匹配的密钥文件。先重启监视器，然后重启所有其他 Ceph 服务，并重启或重新挂载客户端。随后按照[迁移步骤](#pveceph_cephx_migration_helper)中的说明运行迁移。

#### 暂存密钥与确认 <a href="#pveceph_cephx_staged_keys" id="pveceph_cephx_staged_keys"></a>

辅助程序会禁用待处理客户端密钥的自动提升，以便监视器让两个凭据都保持有效。较旧的监视器会在暂存密钥首次使用时将其提升，并终止整个集群的宽限期。因此，只有在每个监视器都支持该功能时，辅助程序才会进行暂存，并且每次运行时都会再次检查这一点。

使用 `--apply` 时，`--confirm-all-clients-refreshed` 会将每个暂存密钥设为当前密钥，并使其先前的密钥失效。如果任何尚未完成的轮换未就绪，初始检查会拒绝整个批次。随后，辅助程序会在停用每个旧凭据之前重新检查相应密钥。如果某个客户端在此批次处理期间重新出现，已完成的轮换会保持提交状态，而受阻的密钥会保持暂存状态。要单独确认已就绪的用户，请将 `--confirm-clients-refreshed <USER>` 与 `--apply` 一起使用。

Ceph 19.2.6-pve4 和 20.2.4-pve4 或更新版本的监视器可以识别每个会话的密钥，从而让已刷新的客户端在正向确认或回滚确认期间保持连接。请升级并重启较旧的监视器以使用此功能。如果没有密钥识别功能，该用户的每个可见客户端都必须在确认前断开连接；对于 `client.admin` 这类共享用户，最好进行升级。

#### 外部客户端的密钥副本 <a href="#pveceph_cephx_external_copies" id="pveceph_cephx_external_copies"></a>

对于本地集群的外部客户端，请从其 Ceph 用户的托管文件中复制暂存凭据：

- RBD 密钥环：`/etc/pve/priv/ceph/<STORAGE_ID>.keyring`
- CephFS 原始密钥：`/etc/pve/priv/ceph/<STORAGE_ID>.secret`
- 管理密钥环：`/etc/pve/priv/ceph.client.admin.keyring`

请使用该用户的凭据，不要用 `client.admin` 代替。请安全地传输凭据，并在刷新客户端之前更新每个已保存的副本。由外部集群提供后端的存储则有所不同：辅助程序绝不会轮换该集群的密钥。请遵循其管理员的密钥轮换流程。

设置了 `monhost` 的存储会被视为外部存储，即使其监视器属于本地集群也是如此，因此辅助程序不会更新其密钥副本。如果该副本保存了您要迁移的 Ceph 用户的密钥，请在确认前使用同一用户的暂存密钥更新它，或者在确认回滚前使用恢复的密钥更新它。如果辅助程序在存储密钥副本中发现某个密钥，它会拒绝停用该密钥；请自行验证辅助程序无法检查的副本。

辅助程序会单独列出不受 Proxmox VE 管理的本地用户。请遵循其客户端支持的轮换流程，或者保持其密钥不变并继续启用旧加密算法。

#### 回滚暂存的客户端密钥 <a href="#pveceph_cephx_rollback" id="pveceph_cephx_rollback"></a>

要将已暂存密钥的用户恢复为其当前密钥：

1. 使用 `--abort-staged-key <USER> --apply` 运行辅助程序。在两个凭据均保持有效期间，它会将当前密钥恢复到每个托管副本。
2. 将所有客户端刷新回该密钥，包括已断开连接的客户端和外部密钥副本。辅助程序会像正向迁移期间一样重试托管的 CephFS 挂载。
3. 使用 `--confirm-abort-clients-refreshed <USER> --apply` 运行辅助程序以停用暂存密钥。如果监视器会话收集不完整、某个可见会话使用了暂存密钥、其密钥未知，或者某个存储密钥副本仍保存着暂存密钥，辅助程序会拒绝执行。

#### 紧急加密算法覆盖 <a href="#_emergency_cipher_override" id="_emergency_cipher_override"></a>

监视器通常使用 MonMap 中存储的 `auth_allowed_ciphers` 列表来决定允许哪些密钥加密算法通过身份验证。本地启动选项 `mon_auth_emergency_allowed_ciphers` 会为某个监视器替换该列表。在错误的限制导致管理员无法访问后，它可以临时允许现有管理密钥所使用的加密算法 [\[3\]](#note-4de62a9e-3)。

配置此覆盖后，Ceph 会触发 `AUTH_EMERGENCY_CIPHERS_SET`。辅助程序会拒绝最终限制，因为更改 MonMap 不会生效。请仅使用此覆盖来恢复访问，然后修复正常配置，将其从 `/etc/pve/ceph.conf` 中移除，并在最后一次试运行之前重启每个监视器。

#### 中断的运行与手动回退 <a href="#_interrupted_runs_and_manual_fallback" id="_interrupted_runs_and_manual_fallback"></a>

发生中断后，待受影响的节点可以访问时，运行不带选项的辅助程序。未完成的密钥更新可以在其守护进程停止期间恢复。请保持日志不变，并遵循打印出的后续步骤，而不要开始手动轮换。请检查受影响的节点和服务日志，而不要假定已停止守护进程的密钥需要修复。

如果辅助程序仍无法继续，请安装最新的 `pve-manager` 并重试。在编辑日志或密钥环之前，或者在使用上游 Cephx 密钥迁移流程 [\[4\]](#note-4de62a9e-4) 之前，请联系 Proxmox 支持。该流程会更改 Ceph 身份验证数据库，但不会考虑以下 Proxmox VE 细节：

- 确保 `/etc/pve/priv` 和 `/var/lib/ceph` 下的每个托管密钥副本都包含 Ceph 接受的密钥。将更改合并到 `/etc/pve/priv/ceph.mon.keyring`；切勿覆盖它。
- 在身份验证数据库和加密 OSD 的块设备 LVM 标签中更新其 lockbox 密钥。其临时密钥环不是持久副本。
- 在使客户端先前的 Ceph 用户密钥失效之前，刷新每个客户端。
- 最后轮换 `client.admin`，并在更改它之前准备一个经过独立测试的恢复用户。

只有在具备涵盖上述每一项的完整且经过测试的恢复计划时，才能使用手动密钥轮换或加密算法限制命令。

## 8.14.6. 关闭 Proxmox VE \+ Ceph HCI 集群 <a href="#pveceph_shutdown" id="pveceph_shutdown"></a>

要关闭整个 Proxmox VE \+ Ceph 集群，请先停止所有 Ceph 客户端。这些客户端主要是虚拟机和容器。如果您有其他可能访问 Ceph FS 或已安装的 RADOS GW 的客户端，也请停止它们。通过 Proxmox VE 工具关机时，高可用性客户机会将其状态切换为 *stopped*。

一旦所有客户端、虚拟机和容器都已关闭或不再访问 Ceph 集群，请验证 Ceph 集群处于健康状态。可以通过 Web UI 或 CLI 进行验证：

```text
ceph -s
```

为避免在关机和后续开机阶段引发任何恢复，请启用 *noout* OSD 标志。可以通过 **Ceph → OSD** 面板中的 **管理全局标志**按钮，或者通过 CLI 启用：

```text
ceph osd set noout
```

先关闭没有监视器（MON）的节点。这些节点关闭后，再继续关闭带有监视器的节点。

为集群开机时，先启动带有监视器（MON）的节点。所有节点都启动并运行后，确认所有 Ceph 服务都已启动并运行。最后，您应该看到的唯一 Ceph 警告是 *noout* 标志仍处于设置状态。您可以通过 Web UI 或 CLI 禁用它：

```text
ceph osd unset noout
```

现在可以启动客户机了。高可用性客户机开机时，会将其状态更改为 *started*。

## 8.14.7. 网络更改 <a href="#pveceph_network_change" id="pveceph_network_change"></a>

如果**可以同时配置旧网络和新网络**，则可以在 HCI 部署中更改 Ceph 使用的网络，而不会造成任何停机。

具体流程会因您要更改的网络而异。

{% hint style="info" %}
注意！谨慎更改 Ceph 所使用的网络至关重要。否则可能导致 Ceph 集群损坏，并需要停机才能使其恢复工作状态！我们建议先在（虚拟）测试集群中试运行该过程，然后再更改生产基础设施。
{% endhint %}

在所有宿主机上配置好新网络后，请务必先对其进行测试，然后再继续更改。一种方法是在新网络上 ping 所有宿主机。如果使用较大的 MTU，请确保也测试其是否正常工作。例如，可以发送 ping 数据包，使最终数据包的大小达到最大 MTU。

要测试 9000 的 MTU，需要使用以下数据包大小：

{% hint style="info" %}
我们假设采用简单的网络配置。在更复杂的部署中，您可能需要配置较低的 MTU，以计入数据包离开宿主机后可能添加的任何标头。
{% endhint %}

<table>
<tr>
<td>IPv4 <br/></td>
<td>
<p>IP 和 ICMP 的开销为 <em>28</em> 字节；因此 ping 最终的数据包大小为 <em>8972</em> 字节。</p>
</td>
</tr>
<tr>
<td>IPv6 <br/></td>
<td>
<p>开销为 <em>48</em> 字节，最终数据包大小为 <em>8952</em> 字节。</p>
</td>
</tr>
</table>

对于 IPv4，最终使用的 ping 命令如下所示：

```text
ping -M do -s 8972 {target IP}
```

在 IPv4 和 IPv6 网络之间切换时，需要确保 `ceph.conf` 文件中的以下选项正确设置为 `true` 或 `false`。这些配置选项决定 Ceph 服务应绑定到 IPv4 还是 IPv6 地址。

```text
ms_bind_ipv4 = true
ms_bind_ipv6 = false
```

### 更改 Ceph 公共网络 <a href="#pveceph_network_change_public" id="pveceph_network_change_public"></a>

Ceph 公共网络是 Ceph 集群中不同服务与客户端（例如 VM）之间的主要通信通道。将其更改为其他网络并不像更改 Ceph 集群网络那样简单。主要原因是，除了在 `ceph.conf` 文件中的配置外，Ceph MON（监视器）还有一项内部配置，用于跟踪属于集群的所有其他 MON，即 *monmap*。

因此，更改 Ceph 公共网络的过程要稍微复杂一些：

1. 更改 `public_network`（在 `/etc/pve/ceph.conf` 文件中，不要更改任何其他值）
2. 重启一台宿主机上的非 MON 服务：OSD、MGR 和 MDS
3. 等待 Ceph 恢复 *HEALTH\_OK* 状态
4. 验证服务是否正在使用新网络
5. 继续在下一台宿主机上重启服务
6. 销毁一个 MON
7. 重新创建 MON
8. 等待 Ceph 恢复 *HEALTH\_OK* 状态
9. 继续销毁并重新创建 MON

首先需要编辑 `/etc/pve/ceph.conf` 文件。更改 `public_network` 行，使其与新子网匹配。

```text
public_network = 10.9.9.30/24
```

{% hint style="warning" %}
不要更改 `mon_host` 行或任何 `[mon.HOSTNAME]` 节。销毁并重新创建 MON 时，这些内容会自动更新。
{% endhint %}

{% hint style="info" %}
如果默认设置了主机位（例如最后一个八位组），不必担心；CIDR 表示法中的网络掩码定义了网络部分。
{% endhint %}

更改网络后，需要重启集群中的非 MON 服务，才能使更改生效。请每次只操作一个节点！要重启一个节点上的所有非 MON 服务，可以在该节点上使用以下命令。Ceph 为每种服务类型都设有 `systemd` 目标。

```text
systemctl restart ceph-osd.target
systemctl restart ceph-mgr.target
systemctl restart ceph-mds.target
```

{% hint style="info" %}
只有使用 CephFS 时，才会有 MDS 守护进程（元数据服务器）。
{% endhint %}

{% hint style="info" %}
第一个 OSD 服务重启后，GUI 会提示该 OSD 不再可达。这不是问题；VM 仍然可以访问这些 OSD。出现该消息的原因是 MGR 服务无法再访问该 OSD。MGR 服务重启后，该错误会消失。
{% endhint %}

{% hint style="warning" %}
不要同时在多台宿主机上重启 OSD。对于某些 PG（归置组），（默认）3 个副本中很可能有 2 个会不可用。这将导致 I/O 暂停，直到可用副本数量重新达到最低要求（`min_size`）。
{% endhint %}

要验证服务是否正在新网络上监听，可以在每个节点上运行以下命令：

```text
ss -tulpn | grep ceph
```

{% hint style="info" %}
由于 OSD 也会在 Ceph 集群网络上监听，因此在 `ss -tulpn` 的输出中也会看到该网络。
{% endhint %}

一旦 Ceph 集群恢复完全健康状态（*HEALTH\_OK*），且服务正在新网络上监听，就继续重启该宿主机上的服务。

最后需要迁移到新网络的服务是 Ceph MON 本身。最简单的方法是逐一销毁并重新创建每个监视器。这样，`ceph.conf` 和监视器内部 `monmap` 中任何与之相关的条目都会自动处理。

销毁第一个 MON，然后重新创建它。继续处理集群中的下一个 MON 之前，请稍等片刻，并确保集群报告 *HEALTH\_OK* 后再继续。

重新创建所有 MON 后，可以验证 `ceph.conf` 文件中所有涉及 MON 的内容是否都引用新网络。这主要包括 `mon_host` 行和 `[mon.HOSTNAME]` 节。

最后再运行一次 `ss -tulpn | grep ceph`，应显示任何 Ceph 服务都不再使用旧网络。

### 更改 Ceph 集群网络 <a href="#pveceph_network_change_cluster" id="pveceph_network_change_cluster"></a>

Ceph 集群网络用于 OSD 之间的复制流量。因此，将其放置在独立的高速物理网络上可能会有所帮助。

总体过程如下：

1. 更改 `cluster_network`（位于 `/etc/pve/ceph.conf` 文件中）
2. 重启一台宿主机上的 OSD
3. 等待 Ceph 恢复 *HEALTH\_OK* 状态
4. 验证 OSD 是否正在使用新网络
5. 继续在下一台宿主机上重启 OSD

首先需要编辑 `/etc/pve/ceph.conf` 文件。更改 `cluster_network` 行，使其与新子网匹配。

```text
cluster_network = 10.9.9.30/24
```

{% hint style="info" %}
如果默认设置了主机位（例如最后一个八位组），不必担心；CIDR 表示法中的网络掩码定义了网络部分。
{% endhint %}

更改网络后，需要重启集群中的 OSD，才能使更改生效。请每次只操作一个节点！要重启一个节点上的所有 OSD，可以在该节点的 CLI 中运行以下命令：

```text
systemctl restart ceph-osd.target
```

{% hint style="warning" %}
不要同时在多台宿主机上重启 OSD。对于某些 PG（归置组），（默认）3 个副本中很可能有 2 个会不可用。这将导致 I/O 暂停，直到可用副本数量重新达到最低要求（`min_size`）。
{% endhint %}

要验证 OSD 服务是否正在新网络上监听，可以检查 **OSD 详细信息 → 网络** 选项卡（位于 **Ceph → OSD** 面板中），也可以在宿主机上运行以下命令：

```text
ss -tulpn | grep ceph-osd
```

{% hint style="info" %}
由于 OSD 也会在 Ceph 公共网络上监听，因此在 `ss -tulpn` 的输出中也会看到该网络。
{% endhint %}

一旦 Ceph 集群恢复完全健康状态（*HEALTH\_OK*），且 OSD 正在新网络上监听，就继续在下一台宿主机上重启 OSD。

## 注释

### 注释 1 <a href="#note-4de62a9e-1" id="note-4de62a9e-1"></a>

Ceph 擦洗 [https://docs.ceph.com/en/tentacle/rados/configuration/osd-config-ref/#scrubbing](https://docs.ceph.com/en/tentacle/rados/configuration/osd-config-ref/#scrubbing)

### 注释 2 <a href="#note-4de62a9e-2" id="note-4de62a9e-2"></a>

Ceph：Squid v19.2.6 和 Tentacle v20.2.4 发布 [https://ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/](https://ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/)

### 注释 3 <a href="#note-4de62a9e-3" id="note-4de62a9e-3"></a>

Ceph：紧急允许的加密算法 [https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#emergency-allowed-ciphers](https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#emergency-allowed-ciphers)

### 注释 4 <a href="#note-4de62a9e-4" id="note-4de62a9e-4"></a>

Ceph 文档：[https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#cephx-upgrade](https://docs.ceph.com/en/tentacle/rados/configuration/auth-config-ref/#cephx-upgrade)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
