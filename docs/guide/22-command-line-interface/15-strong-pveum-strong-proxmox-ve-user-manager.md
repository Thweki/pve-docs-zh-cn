# 22.15. **pveum** \- Proxmox VE 用户管理器 <a href="#strong_pveum_strong_proxmox_ve_user_manager" id="strong_pveum_strong_proxmox_ve_user_manager"></a>

## **pveum** `<COMMAND> [ARGS] [OPTIONS]` <a href="#cli_pveum" id="cli_pveum"></a>

## **pveum acl delete** `<path> --roles <string>` `[OPTIONS]` <a href="#cli_pveum_acl_delete" id="cli_pveum_acl_delete"></a>

更新访问控制列表（添加或移除权限）。

**`<path>`: `<string>`**

访问控制路径

**`--groups` `<string>`**

组列表。

**`--propagate` `<boolean>` （*默认值 \=* `1`）**

允许传播（继承）权限。

**`--roles` `<string>`**

角色列表。

**`--tokens` `<string>`**

API 令牌列表。

**`--users` `<string>`**

用户列表。

## **pveum acl list** `[FORMAT_OPTIONS]` <a href="#cli_pveum_acl_list" id="cli_pveum_acl_list"></a>

获取访问控制列表（ACL）。

## **pveum acl modify** `<path> --roles <string>` `[OPTIONS]` <a href="#cli_pveum_acl_modify" id="cli_pveum_acl_modify"></a>

更新访问控制列表（添加或移除权限）。

**`<path>`: `<string>`**

访问控制路径

**`--groups` `<string>`**

组列表。

**`--propagate` `<boolean>` （*默认值 \=* `1`）**

允许传播（继承）权限。

**`--roles` `<string>`**

角色列表。

**`--tokens` `<string>`**

API 令牌列表。

**`--users` `<string>`**

用户列表。

## **pveum acldel** <a href="#cli_pveum_acldel" id="cli_pveum_acldel"></a>

*pveum acl delete* 的别名。

## **pveum aclmod** <a href="#cli_pveum_aclmod" id="cli_pveum_aclmod"></a>

*pveum acl modify* 的别名。

## **pveum group add** `<groupid>` `[OPTIONS]` <a href="#cli_pveum_group_add" id="cli_pveum_group_add"></a>

创建新组。

**`<groupid>`: `<string>`**

没有可用的说明

**`--comment` `<string>`**

没有可用的说明

## **pveum group delete** `<groupid>` <a href="#cli_pveum_group_delete" id="cli_pveum_group_delete"></a>

删除组。

**`<groupid>`: `<string>`**

没有可用的说明

## **pveum group list** `[FORMAT_OPTIONS]` <a href="#cli_pveum_group_list" id="cli_pveum_group_list"></a>

组索引。

## **pveum group modify** `<groupid>` `[OPTIONS]` <a href="#cli_pveum_group_modify" id="cli_pveum_group_modify"></a>

更新组数据。

**`<groupid>`: `<string>`**

没有可用的说明

**`--comment` `<string>`**

没有可用的说明

## **pveum groupadd** <a href="#cli_pveum_groupadd" id="cli_pveum_groupadd"></a>

*pveum group add* 的别名。

## **pveum groupdel** <a href="#cli_pveum_groupdel" id="cli_pveum_groupdel"></a>

*pveum group delete* 的别名。

## **pveum groupmod** <a href="#cli_pveum_groupmod" id="cli_pveum_groupmod"></a>

*pveum group modify* 的别名。

## **pveum help** `[OPTIONS]` <a href="#cli_pveum_help" id="cli_pveum_help"></a>

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

## **pveum passwd** `<userid>` `[OPTIONS]` <a href="#cli_pveum_passwd" id="cli_pveum_passwd"></a>

更改用户密码。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--confirmation-password` `<string>`**

执行更改的用户的当前密码。

## **pveum pool add** `<poolid>` `[OPTIONS]` <a href="#cli_pveum_pool_add" id="cli_pveum_pool_add"></a>

创建新资源池。

**`<poolid>`: `<string>`**

没有可用的说明

**`--comment` `<string>`**

没有可用的说明

## **pveum pool delete** `<poolid>` <a href="#cli_pveum_pool_delete" id="cli_pveum_pool_delete"></a>

删除资源池。

**`<poolid>`: `<string>`**

没有可用的说明

## **pveum pool list** `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_pool_list" id="cli_pveum_pool_list"></a>

列出资源池或获取资源池配置。

**`--poolid` `<string>`**

没有可用的说明

**`--type` `<lxc | qemu | storage>`**

没有可用的说明

{% hint style="info" %}
需要选项：`poolid`
{% endhint %}

## **pveum pool modify** `<poolid>` `[OPTIONS]` <a href="#cli_pveum_pool_modify" id="cli_pveum_pool_modify"></a>

更新资源池。

**`<poolid>`: `<string>`**

没有可用的说明

**`--allow-move` `<boolean>` （*默认值 \=* `0`）**

即使客户机已在其他资源池中，也允许添加。客户机将从当前资源池移除，并添加到此资源池。

**`--comment` `<string>`**

没有可用的说明

**`--delete` `<boolean>` (*默认 \=* `0`)**

移除传入的 VMID 和/或存储 ID，而非添加。

**`--storage` `<string>`**

要添加到此资源池或从中移除的存储 ID 列表。

**`--vms` `<string>`**

要添加到此资源池或从中移除的客户机 VMID 列表。

## **pveum realm add** `<realm> --type <string>` `[OPTIONS]` <a href="#cli_pveum_realm_add" id="cli_pveum_realm_add"></a>

添加认证服务器。

**`<realm>`: `<string>`**

认证域 ID

**`--acr-values` `^[^\x00-\x1F\x7F <>#"]*$`**

指定请求授权服务器在认证请求中使用的认证上下文类引用值。

**`--audiences` `^[^\x00-\x1F\x7F <>#"]*$`**

除了 *client-id* 之外，还接受 OpenID 签发者可能包含的受众列表。

**`--autocreate` `<boolean>` （*默认值 \=* `0`）**

如果用户不存在，则自动创建。

**`--base_dn` `<string>`**

LDAP 基础域名

**`--bind_dn` `<string>`**

LDAP 绑定域名

**`--capath` `<string>` （*默认值 \=* `/etc/ssl/certs`）**

CA 证书存储路径

**`--case-sensitive` `<boolean>` （*默认值 \=* `1`）**

用户名区分大小写

**`--cert` `<string>`**

客户端证书路径

**`--certkey` `<string>`**

客户端证书密钥路径

**`--check-connection` `<boolean>` （*默认值 \=* `0`）**

检查与服务器的绑定连接。

**`--client-id` `<string>`**

OpenID 客户端 ID

**`--client-key` `<string>`**

OpenID 客户端密钥

**`--comment` `<string>`**

描述。

**`--default` `<boolean>`**

将此认证域用作默认认证域

**`--domain` `\S+`**

AD 域名

**`--filter` `<string>`**

用户同步的 LDAP 过滤器。

**`--group_classes` `<string>` （*默认值 \=* `groupOfNames, group, univentionGroup, ipausergroup`）**

组的对象类。

**`--group_dn` `<string>`**

组同步的 LDAP 基础域名。如果未设置，则使用 base\_dn。

**`--group_filter` `<string>`**

组同步的 LDAP 过滤器。

**`--group_name_attr` `<string>`**

表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。

**`--groups-autocreate` `<boolean>` （*默认值 \=* `0`）**

如果组不存在，则自动创建。

**`--groups-claim` `(?^:[A-Za-z0-9\.\-_]+)`**

用于获取组的 OpenID 声明。

**`--groups-overwrite` `<boolean>` （*默认值 \=* `0`）**

登录时覆盖该用户的所有组。

**`--issuer-url` `<string>`**

OpenID 签发者 URL

**`--mode` `<ldap | ldap+starttls | ldaps>` （*默认值 \=* `ldap`）**

LDAP 协议模式。

**`--password` `<string>`**

LDAP 绑定密码。将保存在 */etc/pve/priv/realm/\<REALM\>.pw* 中。

**`--port` `<integer> (1 - 65535)`**

服务器端口。

**`--prompt` `(?:none|login|consent|select_account|\S+)`**

指定授权服务器是否提示最终用户重新认证并同意。

**`--query-userinfo` `<boolean>` （*默认值 \=* `1`）**

启用对 userinfo 端点的查询，以获取声明值。

**`--scopes` `<string>` （*默认值 \=* `email profile`）**

指定应授权并返回的作用域（用户详细信息），例如 *email* 或 *profile*。

**`--secure` `<boolean>`**

使用安全的 LDAPS 协议。已弃用：请改用 *mode*。

**`--server1` `<string>`**

服务器 IP 地址（或 DNS 名称）

**`--server2` `<string>`**

备用服务器 IP 地址（或 DNS 名称）

**`--sslversion` `<tlsv1 | tlsv1_1 | tlsv1_2 | tlsv1_3>`**

LDAPS TLS/SSL 版本。不建议使用低于 1.2 的版本！

**`--sync-defaults-options` `[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]`**

同步行为的默认选项。

**`--sync_attributes` `\w+=[^,]+(,\s*\w+=[^,]+)*`**

以逗号分隔的 key\=value 对列表，用于指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 *mail* 映射到 PVE 的 *email*，请写入 *email\=mail*。默认情况下，每个 PVE 用户字段都由同名 LDAP 属性表示。

**`--tfa` `type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]`**

使用双因素认证。

**`--type` `<ad | ldap | openid | pam | pve>`**

认证域类型。

**`--user_attr` `\S{2,}`**

LDAP 用户属性名称

**`--user_classes` `<string>` （*默认值 \=* `inetorgperson, posixaccount, person, user`）**

用户的对象类。

**`--username-claim` `<string>`**

用于生成唯一用户名的 OpenID 声明。

**`--verify` `<boolean>` （*默认值 \=* `0`）**

验证服务器的 SSL 证书

## **pveum realm delete** `<realm>` <a href="#cli_pveum_realm_delete" id="cli_pveum_realm_delete"></a>

删除认证服务器。

**`<realm>`: `<string>`**

认证域 ID

## **pveum realm list** `[FORMAT_OPTIONS]` <a href="#cli_pveum_realm_list" id="cli_pveum_realm_list"></a>

认证域索引。

## **pveum realm modify** `<realm>` `[OPTIONS]` <a href="#cli_pveum_realm_modify" id="cli_pveum_realm_modify"></a>

更新认证服务器设置。

**`<realm>`: `<string>`**

认证域 ID

**`--acr-values` `^[^\x00-\x1F\x7F <>#"]*$`**

指定请求授权服务器在认证请求中使用的认证上下文类引用值。

**`--audiences` `^[^\x00-\x1F\x7F <>#"]*$`**

除了 *client-id* 之外，还接受 OpenID 签发者可能包含的受众列表。

**`--autocreate` `<boolean>` （*默认值 \=* `0`）**

如果用户不存在，则自动创建。

**`--base_dn` `<string>`**

LDAP 基础域名

**`--bind_dn` `<string>`**

LDAP 绑定域名

**`--capath` `<string>` （*默认值 \=* `/etc/ssl/certs`）**

CA 证书存储路径

**`--case-sensitive` `<boolean>` （*默认值 \=* `1`）**

用户名区分大小写

**`--cert` `<string>`**

客户端证书路径

**`--certkey` `<string>`**

客户端证书密钥路径

**`--check-connection` `<boolean>` （*默认值 \=* `0`）**

检查与服务器的绑定连接。

**`--client-id` `<string>`**

OpenID 客户端 ID

**`--client-key` `<string>`**

OpenID 客户端密钥

**`--comment` `<string>`**

描述。

**`--default` `<boolean>`**

将此认证域用作默认认证域

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--domain` `\S+`**

AD 域名

**`--filter` `<string>`**

用户同步的 LDAP 过滤器。

**`--group_classes` `<string>` （*默认值 \=* `groupOfNames, group, univentionGroup, ipausergroup`）**

组的对象类。

**`--group_dn` `<string>`**

组同步的 LDAP 基础域名。如果未设置，则使用 base\_dn。

**`--group_filter` `<string>`**

组同步的 LDAP 过滤器。

**`--group_name_attr` `<string>`**

表示组名称的 LDAP 属性。如果未设置或未找到，则使用 DN 的第一个值作为名称。

**`--groups-autocreate` `<boolean>` （*默认值 \=* `0`）**

如果组不存在，则自动创建。

**`--groups-claim` `(?^:[A-Za-z0-9\.\-_]+)`**

用于获取组的 OpenID 声明。

**`--groups-overwrite` `<boolean>` （*默认值 \=* `0`）**

登录时覆盖该用户的所有组。

**`--issuer-url` `<string>`**

OpenID 签发者 URL

**`--mode` `<ldap | ldap+starttls | ldaps>` （*默认值 \=* `ldap`）**

LDAP 协议模式。

**`--password` `<string>`**

LDAP 绑定密码。将保存在 */etc/pve/priv/realm/\<REALM\>.pw* 中。

**`--port` `<integer> (1 - 65535)`**

服务器端口。

**`--prompt` `(?:none|login|consent|select_account|\S+)`**

指定授权服务器是否提示最终用户重新认证并同意。

**`--query-userinfo` `<boolean>` （*默认值 \=* `1`）**

启用对 userinfo 端点的查询，以获取声明值。

**`--scopes` `<string>` （*默认值 \=* `email profile`）**

指定应授权并返回的作用域（用户详细信息），例如 *email* 或 *profile*。

**`--secure` `<boolean>`**

使用安全的 LDAPS 协议。已弃用：请改用 *mode*。

**`--server1` `<string>`**

服务器 IP 地址（或 DNS 名称）

**`--server2` `<string>`**

备用服务器 IP 地址（或 DNS 名称）

**`--sslversion` `<tlsv1 | tlsv1_1 | tlsv1_2 | tlsv1_3>`**

LDAPS TLS/SSL 版本。不建议使用低于 1.2 的版本！

**`--sync-defaults-options` `[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]`**

同步行为的默认选项。

**`--sync_attributes` `\w+=[^,]+(,\s*\w+=[^,]+)*`**

以逗号分隔的 key\=value 对列表，用于指定哪些 LDAP 属性映射到哪些 PVE 用户字段。例如，要将 LDAP 属性 *mail* 映射到 PVE 的 *email*，请写入 *email\=mail*。默认情况下，每个 PVE 用户字段都由同名 LDAP 属性表示。

**`--tfa` `type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]`**

使用双因素认证。

**`--user_attr` `\S{2,}`**

LDAP 用户属性名称

**`--user_classes` `<string>` （*默认值 \=* `inetorgperson, posixaccount, person, user`）**

用户的对象类。

**`--verify` `<boolean>` （*默认值 \=* `0`）**

验证服务器的 SSL 证书

## **pveum realm sync** `<realm>` `[OPTIONS]` <a href="#cli_pveum_realm_sync" id="cli_pveum_realm_sync"></a>

将用户和/或组从配置的 LDAP 同步到 user.cfg。注意：同步后的组将命名为 *name-$realm*，因此请确保这些组不存在，以免覆盖。

**`<realm>`: `<string>`**

认证域 ID

**`--dry-run` `<boolean>` （*默认值 \=* `0`）**

如果设置，则不写入任何内容。

**`--enable-new` `<boolean>` （*默认值 \=* `1`）**

立即启用新同步的用户。

**`--full` `<boolean>`**

已弃用：请改用 *remove-vanished*。如果设置，则以 LDAP 目录为准，删除同步未返回的用户或组，并移除同步用户所有在本地修改的属性。如果未设置，则仅同步已同步数据中存在的信息，不删除或修改其他任何内容。

**`--purge` `<boolean>`**

已弃用：请改用 *remove-vanished*。移除在同步期间从配置中移除的用户或组的 ACL。

**`--remove-vanished` `([acl];[properties];[entry])|none` （*默认值 \=* `none`）**

以分号分隔的列表，指定当相应项目或用户在同步中消失时要移除的内容。可用值如下：*entry* 在同步未返回用户/组时将其移除。*properties* 移除现有用户/组上已设置但源中不存在的属性（包括自定义属性）。*acl* 在同步未返回用户/组时移除 ACL。也可以不使用列表，而使用 *none*（默认值）。

**`--scope` `<both | groups | users>`**

选择要同步的内容。

## **pveum role add** `<roleid>` `[OPTIONS]` <a href="#cli_pveum_role_add" id="cli_pveum_role_add"></a>

创建新角色。

**`<roleid>`: `<string>`**

没有可用的说明

**`--privs` `<string>`**

没有可用的说明

## **pveum role delete** `<roleid>` <a href="#cli_pveum_role_delete" id="cli_pveum_role_delete"></a>

删除角色。

**`<roleid>`: `<string>`**

没有可用的说明

## **pveum role list** `[FORMAT_OPTIONS]` <a href="#cli_pveum_role_list" id="cli_pveum_role_list"></a>

角色索引。

## **pveum role modify** `<roleid>` `[OPTIONS]` <a href="#cli_pveum_role_modify" id="cli_pveum_role_modify"></a>

更新现有角色。

**`<roleid>`: `<string>`**

没有可用的说明

**`--append` `<boolean>`**

没有可用的说明

{% hint style="info" %}
需要选项：`privs`
{% endhint %}

**`--privs` `<string>`**

没有可用的说明

## **pveum roleadd** <a href="#cli_pveum_roleadd" id="cli_pveum_roleadd"></a>

*pveum role add* 的别名。

## **pveum roledel** <a href="#cli_pveum_roledel" id="cli_pveum_roledel"></a>

*pveum role delete* 的别名。

## **pveum rolemod** <a href="#cli_pveum_rolemod" id="cli_pveum_rolemod"></a>

*pveum role modify* 的别名。

## **pveum ticket** `<username>` `[OPTIONS]` <a href="#cli_pveum_ticket" id="cli_pveum_ticket"></a>

创建或验证认证票据。

**`<username>`: `<string>`**

用户名

**`--new-format` `<boolean>` （*默认值 \=* `1`）**

此参数现在会被忽略，并视为 1。

**`--otp` `<string>`**

双因素认证的一次性密码。

**`--path` `<string>`**

验证票据，并检查用户是否具有 *privs* 访问权限，路径为 *path*

{% hint style="info" %}
需要选项：`privs`
{% endhint %}

**`--privs` `<string>`**

验证票据，并检查用户是否具有 *privs* 访问权限，路径为 *path*

{% hint style="info" %}
需要选项：`path`
{% endhint %}

**`--realm` `<string>`**

可以选择通过此参数传入认证域。通常将认证域直接添加到用户名中：\<username\>@\<realm\>。

**`--tfa-challenge` `<string>`**

用户要响应的已签名 TFA 质询字符串。

## **pveum user add** `<userid>` `[OPTIONS]` <a href="#cli_pveum_user_add" id="cli_pveum_user_add"></a>

创建新用户。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--comment` `<string>`**

没有可用的说明

**`--email` `<string>`**

没有可用的说明

**`--enable` `<boolean>` （*默认值 \=* `1`）**

启用账户（默认）。可以将其设置为 *0* 以禁用账户

**`--expire` `<integer> (0 - N)`**

账户到期日期（自纪元以来的秒数）。*0* 表示没有到期日期。

**`--firstname` `<string>`**

没有可用的说明

**`--groups` `<string>`**

没有可用的说明

**`--keys` `[0-9a-zA-Z!=]{0,4096}`**

双因素认证的密钥（yubico）。

**`--lastname` `<string>`**

没有可用的说明

**`--password` `<string>`**

初始密码。

## **pveum user delete** `<userid>` <a href="#cli_pveum_user_delete" id="cli_pveum_user_delete"></a>

删除用户。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

## **pveum user list** `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_list" id="cli_pveum_user_list"></a>

用户索引。

**`--enabled` `<boolean>`**

enable 属性的可选过滤器。

**`--full` `<boolean>` （*默认值 \=* `0`）**

包含组和令牌信息。

## **pveum user modify** `<userid>` `[OPTIONS]` <a href="#cli_pveum_user_modify" id="cli_pveum_user_modify"></a>

更新用户配置。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--append` `<boolean>`**

没有可用的说明

{% hint style="info" %}
需要选项：`groups`
{% endhint %}

**`--comment` `<string>`**

没有可用的说明

**`--email` `<string>`**

没有可用的说明

**`--enable` `<boolean>` （*默认值 \=* `1`）**

启用账户（默认）。可以将其设置为 *0* 以禁用账户

**`--expire` `<integer> (0 - N)`**

账户到期日期（自纪元以来的秒数）。*0* 表示没有到期日期。

**`--firstname` `<string>`**

没有可用的说明

**`--groups` `<string>`**

没有可用的说明

**`--keys` `[0-9a-zA-Z!=]{0,4096}`**

双因素认证的密钥（yubico）。

**`--lastname` `<string>`**

没有可用的说明

## **pveum user permissions** `[<userid>]` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_permissions" id="cli_pveum_user_permissions"></a>

获取给定用户/令牌的有效权限。

**`<userid>`: `(?^:^(?^:[^\s:/]+)\@(?^:[A-Za-z][A-Za-z0-9\.\-_]+)(?:!(?^:[A-Za-z][A-Za-z0-9\.\-_]+))?$)`**

用户 ID 或完整的 API 令牌 ID

**`--path` `<string>`**

仅转储此特定路径，而不是整棵树。

## **pveum user tfa delete** `<userid>` `[OPTIONS]` <a href="#cli_pveum_user_tfa_delete" id="cli_pveum_user_tfa_delete"></a>

删除用户的 TFA 条目。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`--id` `<string>`**

TFA ID，如果未提供，则删除所有 TFA 条目。

## **pveum user tfa list** `[<userid>]` <a href="#cli_pveum_user_tfa_list" id="cli_pveum_user_tfa_list"></a>

列出 TFA 条目。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

## **pveum user tfa unlock** `<userid>` <a href="#cli_pveum_user_tfa_unlock" id="cli_pveum_user_tfa_unlock"></a>

解锁用户的 TFA 认证。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

## **pveum user token add** `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_add" id="cli_pveum_user_token_add"></a>

为特定用户生成新的 API 令牌。注意：返回的 API 令牌值需要保存，因为之后无法再次获取！

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

**`--comment` `<string>`**

没有可用的说明

**`--expire` `<integer> (0 - N)` （*默认值 \=* `same as user`）**

API 令牌到期日期（自纪元以来的秒数）。*0* 表示没有到期日期。

**`--privsep` `<boolean>` （*默认值 \=* `1`）**

使用单独的 ACL 限制 API 令牌权限（默认），或赋予对应用户的全部权限。

## **pveum user token delete** `<userid> <tokenid>` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_delete" id="cli_pveum_user_token_delete"></a>

移除特定用户的 API 令牌。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

## **pveum user token list** `<userid>` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_list" id="cli_pveum_user_token_list"></a>

获取用户 API 令牌。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

## **pveum user token modify** `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_modify" id="cli_pveum_user_token_modify"></a>

更新特定用户的 API 令牌。注意：设置 *regenerate* 后，返回的令牌值需要保存，因为之后无法再次获取！

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

**`--comment` `<string>`**

没有可用的说明

**`--delete` `<string>`**

要删除的设置列表。

**`--expire` `<integer> (0 - N)` （*默认值 \=* `same as user`）**

API 令牌到期日期（自纪元以来的秒数）。*0* 表示没有到期日期。

**`--privsep` `<boolean>` （*默认值 \=* `1`）**

使用单独的 ACL 限制 API 令牌权限（默认），或赋予对应用户的全部权限。

**`--regenerate` `<boolean>` （*默认值 \=* `0`）**

重新生成令牌的秘密值。此操作之后，所有使用旧秘密值的用户都将失去访问权限。

## **pveum user token permissions** `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]` <a href="#cli_pveum_user_token_permissions" id="cli_pveum_user_token_permissions"></a>

获取给定令牌的有效权限。

**`<userid>`: `<string>`**

完整的用户 ID，格式为 `name@realm`。

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

用户特定的令牌标识符。

**`--path` `<string>`**

仅转储此特定路径，而不是整棵树。

## **pveum user token remove** <a href="#cli_pveum_user_token_remove" id="cli_pveum_user_token_remove"></a>

*pveum user token delete* 的别名。

## **pveum useradd** <a href="#cli_pveum_useradd" id="cli_pveum_useradd"></a>

*pveum user add* 的别名。

## **pveum userdel** <a href="#cli_pveum_userdel" id="cli_pveum_userdel"></a>

*pveum user delete* 的别名。

## **pveum usermod** <a href="#cli_pveum_usermod" id="cli_pveum_usermod"></a>

*pveum user modify* 的别名。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
