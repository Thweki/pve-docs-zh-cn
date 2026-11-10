# datacenter.cfg(5)

## 名称 <a href="#datacenter_configuration_file" id="datacenter_configuration_file"></a>

datacenter.cfg \- Proxmox VE 数据中心配置

## 概要 <a href="#synopsis" id="synopsis"></a>

`/etc/pve/datacenter.cfg`

## 描述 <a href="#description" id="description"></a>

文件 `/etc/pve/datacenter.cfg` 是 Proxmox VE 的配置文件。它包含所有节点使用的集群范围默认值。

## 文件格式 <a href="#file_format" id="file_format"></a>

该文件采用简单的冒号分隔键/值格式。每行的格式如下：

```text
OPTION: value
```

文件中的空白行会被忽略，以 `#` 字符开头的行会被视为注释，同样会被忽略。

## 选项 <a href="#options" id="options"></a>

**`bwlimit`: `[clone=<LIMIT>] [,default=<LIMIT>] [,migration=<LIMIT>] [,move=<LIMIT>] [,restore=<LIMIT>]`**

设置各种操作的 I/O 带宽限制（单位为 KiB/s）。

**`clone`\=`<LIMIT>`**

克隆磁盘的带宽限制，单位为 KiB/s

**`default`\=`<LIMIT>`**

默认带宽限制，单位为 KiB/s

**`migration`\=`<LIMIT>`**

迁移客户机（包括移动本地磁盘）的带宽限制，单位为 KiB/s

**`move`\=`<LIMIT>`**

移动磁盘的带宽限制，单位为 KiB/s

**`restore`\=`<LIMIT>`**

从备份恢复客户机的带宽限制，单位为 KiB/s

**`consent-text`: `<string>`**

登录前显示的同意声明文本。

**`console`: `<applet | html5 | vv | xtermjs>`**

选择默认的控制台查看器。您可以使用内置的 Java 小程序（VNC；已弃用，并映射到 html5）、外部兼容 virt-viewer 的应用程序（SPICE）、基于 HTML5 的 VNC 查看器（noVNC），或基于 HTML5 的控制台客户端（xtermjs）。如果所选查看器不可用（例如，未为 VM 启用 SPICE），则回退到 noVNC。

**`crs`: `[ha=<basic|static|dynamic>] [,ha-auto-rebalance=<1|0>] [,ha-auto-rebalance-hold-duration=<number>] [,ha-auto-rebalance-margin=<number>] [,ha-auto-rebalance-method=<bruteforce|topsis>] [,ha-auto-rebalance-threshold=<number>] [,ha-rebalance-on-start=<1|0>]`**

集群资源调度设置。

**`ha`\=`<basic | dynamic | static>` (*默认值 \=* `basic`)**

配置 HA Manager 应如何选择用于启动或恢复服务的节点：

- 使用 *basic* 时，仅考虑服务数量，
- 使用 *static* 时，会考虑服务的静态 CPU 和内存配置，
- 使用 *dynamic* 时，会考虑服务的静态和动态 CPU 及内存使用情况。

**`ha-auto-rebalance`\=`<boolean>` (*默认值 \=* `0`)**

是否根据当前节点的不均衡程度，使用 CRS 自动均衡 HA 资源。

**`ha-auto-rebalance-hold-duration`\=`<number> (0 - N)` (*默认值 \=* `3`)**

在触发自动资源均衡迁移之前，集群节点不均衡程度必须连续超过阈值的 HA 轮数。

{% hint style="info" %}
需要选项：`ha-auto-rebalance`
{% endhint %}

**`ha-auto-rebalance-margin`\=`<number> (0 - 100)` (*默认值 \=* `10`)**

为执行资源均衡迁移，集群节点不均衡程度必须达到的最小相对改善百分比。

{% hint style="info" %}
需要选项：`ha-auto-rebalance`
{% endhint %}

**`ha-auto-rebalance-method`\=`<bruteforce | topsis>` (*默认值 \=* `bruteforce`)**

用于为均衡迁移评分的方法。

{% hint style="info" %}
需要选项：`ha-auto-rebalance`
{% endhint %}

**`ha-auto-rebalance-threshold`\=`<number> (0 - 100)` (*默认值 \=* `30`)**

集群节点不均衡百分比，超过该值将触发自动资源均衡系统。

{% hint style="info" %}
需要选项：`ha-auto-rebalance`
{% endhint %}

**`ha-rebalance-on-start`\=`<boolean>` (*默认值 \=* `0`)**

设置为在 HA 服务的请求状态从 stop 变为 start 时，使用 CRS 选择合适的节点。

**`description`: `<string>`**

数据中心描述。显示在 Web 界面的数据中心备注面板中。这会作为注释保存在配置文件中。

**`email_from`: `<string>`**

指定用于发送通知的电子邮件地址（默认为 root@$hostname）

**`fencing`: `<both | hardware | watchdog>` (*默认值 \=* `watchdog`)**

设置 HA 集群的隔离模式。硬件模式需要在 /etc/pve/ha/fence.cfg. 中对隔离设备进行有效配置。使用 both 时，会同时采用两种模式。

{% hint style="warning" %}
*hardware* 和 *both* 均为实验性功能，仍在开发中
{% endhint %}

**`ha`: `shutdown_policy=<enum>`**

集群范围的高可用性设置。

**`shutdown_policy`\=`<conditional | failover | freeze | migrate>` (*默认值 \=* `conditional`)**

描述节点关机或重启时处理 HA 服务的策略。Freeze 将始终在节点关闭时冻结仍位于该节点上的服务，HA Manager 不会恢复这些服务。Failover 不会将服务标记为冻结，因此，如果关机的节点未快速（\< 1 分钟）恢复运行，服务将被恢复到其他节点。*conditional* 会根据关机类型自动选择，即重启时服务将被冻结，而关机时服务将保持原状，因此会在约 2 分钟后被恢复。Migrate 会尝试在触发重启或关机时，将所有正在运行的服务迁移到另一个节点。只有当节点上不再有任何正在运行的服务时，关机过程才会继续。如果节点再次启动，服务将被迁回之前关机的节点，至少在没有发生其他迁移、重定位或恢复的情况下会如此。

**`http_proxy`: `http://.*`**

指定用于下载的外部 http 代理（示例：*http://username:password@host:port/*）

**`keyboard`: `<da | de | de-ch | en-gb | en-us | es | fi | fr | fr-be | fr-ca | fr-ch | hu | is | it | ja | lt | mk | nl | no | pl | pt | pt-br | sl | sv | tr>`**

VNC 服务器的默认键盘布局。

**`language`: `<ar | ca | da | de | en | es | eu | fa | fr | he | hr | it | ja | ka | kr | nb | nl | nn | pl | pt_BR | ru | sl | sv | tr | ukr | zh_CN | zh_TW>`**

默认 GUI 语言。

**`location`: `latitude=<number> ,longitude=<number> [,name=<name>]`**

集群的位置。

**`latitude`\=`<number> (-90 - 90)`**

节点位置的纬度，单位为度。

**`longitude`\=`<number> (-180 - 180)`**

节点位置的经度，单位为度。

**`name`\=`<name>`**

此节点所在位置的名称

**`mac_prefix`: `<string>` (*默认值 \=* `BC:24:11`)**

虚拟客户机自动生成的 MAC 地址的前缀。默认的 `BC:24:11` 是 IEEE 分配给 Proxmox Server Solutions GmbH 的组织唯一标识符（OUI），用于大型 MAC 地址块（MA-L）。您可以在本地网络中使用它，即公众无法直接访问的网络（例如 LAN 或 NAT/伪装网络中）。

请注意，当您运行多个集群，且这些集群的虚拟客户机（部分）共享网络时，强烈建议您扩展默认 MAC 前缀，或生成自定义（有效的）前缀，以降低 MAC 地址冲突的可能性。例如，为每个集群在 Proxmox OUI 后添加一个单独的额外十六进制位，第一个集群使用 `BC:24:11:0`，第二个集群使用 `BC:24:11:1`，依此类推。或者，您也可以从逻辑上隔离客户机网络，例如使用 VLAN。

\+ 对于可公开访问的客户机，建议您向 IEEE 注册自己的 [OUI](https://standards.ieee.org/products-programs/regauth/)，或与您的或您的托管服务提供商的网络管理员协调。

**`max_workers`: `<integer> (1 - N)`**

定义在执行 *stopall VMs* 等操作或 ha-manager 的任务时，每个节点最多可启动的工作进程数。

**`migration`: `[type=]<secure|insecure> [,network=<CIDR>]`**

用于集群范围的迁移设置。

**`network`\=`<CIDR>`**

用于迁移的（子）网络的 CIDR。如果未设置复制网络设置，则将其用作复制作业的回退设置

**`type`\=`<insecure | secure>` (*默认值 \=* `secure`)**

默认情况下，迁移流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`migration_unsecure`: `<boolean>`**

默认情况下，迁移通过 SSH 隧道确保安全。对于安全的私有网络，您可以禁用它以加快迁移速度。已弃用，请改用 *migration* 属性！

**`next-id`: `[lower=<integer>] [,upper=<integer>]`**

控制空闲 VMID 自动选择池的范围。

**`lower`\=`<integer>` (*默认值 \=* `100`)**

空闲 next-id API 范围的下限（包含下限）。

**`upper`\=`<integer>` (*默认值 \=* `1000000`)**

空闲 next-id API 范围的上限（不包含上限）。

**`notify`: `[fencing=<always|never>] [,package-updates=<auto|always|never>] [,replication=<always|never>] [,target-fencing=<TARGET>] [,target-package-updates=<TARGET>] [,target-replication=<TARGET>]`**

集群范围的通知设置。

**`fencing`\=`<always | never>`**

未使用——请改用数据中心通知设置。

**`package-updates`\=`<always | auto | never>` (*默认值 \=* `auto`)**

已弃用：请改用数据中心通知设置。控制每日更新作业发送通知的频率：

- *auto*：对具有有效订阅的系统每日发送通知，因为这些系统被视为已可用于生产环境，因此应了解待处理的更新。
- *always*：每次更新时，只要存在新的待处理更新就发送通知。
- *never*：从不为新的待处理更新发送通知。

**`replication`\=`<always | never>`**

未使用——请改用数据中心通知设置。

**`target-fencing`\=`<TARGET>`**

未使用——请改用数据中心通知设置。

**`target-package-updates`\=`<TARGET>`**

未使用——请改用数据中心通知设置。

**`target-replication`\=`<TARGET>`**

未使用——请改用数据中心通知设置。

**`registered-tags`: `<tag>[;<tag>...]`**

设置和删除时需要具有 `Sys.Modify`（位于 */* 上）的标签列表。此处设置且也位于 *user-tag-access* 中的标签还需要 `Sys.Modify`。

**`replication`: `[type=]<secure|insecure> [,network=<CIDR>]`**

用于集群范围的复制设置。

**`network`\=`<CIDR>`**

用于复制作业的（子）网络的 CIDR。

**`type`\=`<insecure | secure>` (*默认值 \=* `secure`)**

默认情况下，复制流量使用 SSH 隧道加密。在安全的完全私有网络中，可以禁用此加密以提高性能。

**`tag-style`: `[case-sensitive=<1|0>] [,color-map=<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]] [,ordering=<config|alphabetical>] [,shape=<enum>]`**

标签样式选项。

**`case-sensitive`\=`<boolean>` (*默认 \=* `0`)**

控制更新时过滤唯一标签是否应区分大小写。

**`color-map`\=`<tag>:<hex-color>[:<hex-color-for-text>][;<tag>=...]`**

标签的手动颜色映射（以分号分隔）。

**`ordering`\=`<alphabetical | config>` (*默认 \=* `alphabetical`)**

控制 Web 界面和 API 更新中的标签排序。

**`shape`\=`<circle | dense | full | none>` (*默认 \=* `circle`)**

Web UI 树中的标签形状。*full* 绘制完整标签。*circle* 仅绘制一个使用背景色的圆形。*dense* 仅绘制一个小矩形（当为每个客户机分配许多标签时很有用）。*none* 禁用标签显示。

**`u2f`: `[appid=<APPID>] [,origin=<URL>]`**

u2f

**`appid`\=`<APPID>`**

U2F AppId URL 覆盖。默认为源。

**`origin`\=`<URL>`**

U2F Origin 覆盖。主要用于只有一个 URL 的单节点。

**`user-tag-access`: `[user-allow=<enum>] [,user-allow-list=<tag>[;<tag>...]]`**

用户可设置标签的权限选项

**`user-allow`\=`<existing | free | list | none>` (*默认 \=* `free`)**

控制用户可对其控制的资源（如客户机）设置或删除哪些标签。拥有 `Sys.Modify` 权限且权限范围为 `/` 的用户始终不受限制。

- *none* 不允许使用任何标签。
- *list* 可使用 *user-allow-list* 中的标签。
- *existing* 与 list 类似，但资源上已经存在的标签也可使用。
- *free* 不限制标签。

**`user-allow-list`\=`<tag>[;<tag>...]`**

当 *user-allow* 值为 *list* 和 *existing* 时，允许用户设置和删除的标签列表（以分号分隔）。

**`webauthn`: `[allow-subdomains=<1|0>] [,id=<DOMAINNAME>] [,origin=<URL>] [,rp=<RELYING_PARTY>]`**

webauthn 配置

**`allow-subdomains`\=`<boolean>` (*默认 \=* `1`)**

是否允许源为子域名，而不是必须与 URL 完全匹配。

**`id`\=`<DOMAINNAME>`**

依赖方 ID。必须是不含协议、端口或路径的域名。更改此项**将**破坏现有凭据。

**`origin`\=`<URL>`**

站点源。必须是 `https://` URL（或 `http://localhost`）。应包含用户在浏览器中输入的用于访问 Web 界面的地址。更改此项**可能**会破坏现有凭据。

**`rp`\=`<RELYING_PARTY>`**

依赖方名称。任意文本标识符。更改此项**可能**会破坏现有凭据。

## 版权与免责声明 <a href="#copyright_and_disclaimer" id="copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/datacenter.cfg.5.html) · 版本 9.2.13 · 非官方中文翻译。
