# 22.15. **pveum** \- Proxmox VE User Manager <a href="#_strong_pveum_strong_proxmox_ve_user_manager" id="_strong_pveum_strong_proxmox_ve_user_manager"></a>

<a id="cli_pveum"></a>



**pveum** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pveum_acl_delete"></a>



**pveum acl delete** `<path> --roles <string>` `[OPTIONS]`

Update Access Control List (add or remove permissions).

**`<path>`: `<string>`**

Access control path

**`--groups` `<string>`**

List of groups.

**`--propagate` `<boolean>` (*default \=* `1`)**

Allow to propagate (inherit) permissions.

**`--roles` `<string>`**

List of roles.

**`--tokens` `<string>`**

List of API tokens.

**`--users` `<string>`**

List of users.

<a id="cli_pveum_acl_list"></a>



**pveum acl list** `[FORMAT_OPTIONS]`

Get Access Control List (ACLs).

<a id="cli_pveum_acl_modify"></a>



**pveum acl modify** `<path> --roles <string>` `[OPTIONS]`

Update Access Control List (add or remove permissions).

**`<path>`: `<string>`**

Access control path

**`--groups` `<string>`**

List of groups.

**`--propagate` `<boolean>` (*default \=* `1`)**

Allow to propagate (inherit) permissions.

**`--roles` `<string>`**

List of roles.

**`--tokens` `<string>`**

List of API tokens.

**`--users` `<string>`**

List of users.

<a id="cli_pveum_acldel"></a>



**pveum acldel**

An alias for *pveum acl delete*.

<a id="cli_pveum_aclmod"></a>



**pveum aclmod**

An alias for *pveum acl modify*.

<a id="cli_pveum_group_add"></a>



**pveum group add** `<groupid>` `[OPTIONS]`

Create new group.

**`<groupid>`: `<string>`**

no description available

**`--comment` `<string>`**

no description available

<a id="cli_pveum_group_delete"></a>



**pveum group delete** `<groupid>`

Delete group.

**`<groupid>`: `<string>`**

no description available

<a id="cli_pveum_group_list"></a>



**pveum group list** `[FORMAT_OPTIONS]`

Group index.

<a id="cli_pveum_group_modify"></a>



**pveum group modify** `<groupid>` `[OPTIONS]`

Update group data.

**`<groupid>`: `<string>`**

no description available

**`--comment` `<string>`**

no description available

<a id="cli_pveum_groupadd"></a>



**pveum groupadd**

An alias for *pveum group add*.

<a id="cli_pveum_groupdel"></a>



**pveum groupdel**

An alias for *pveum group delete*.

<a id="cli_pveum_groupmod"></a>



**pveum groupmod**

An alias for *pveum group modify*.

<a id="cli_pveum_help"></a>



**pveum help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pveum_passwd"></a>



**pveum passwd** `<userid>` `[OPTIONS]`

Change user password.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`--confirmation-password` `<string>`**

The current password of the user performing the change.

<a id="cli_pveum_pool_add"></a>



**pveum pool add** `<poolid>` `[OPTIONS]`

Create new pool.

**`<poolid>`: `<string>`**

no description available

**`--comment` `<string>`**

no description available

<a id="cli_pveum_pool_delete"></a>



**pveum pool delete** `<poolid>`

Delete pool.

**`<poolid>`: `<string>`**

no description available

<a id="cli_pveum_pool_list"></a>



**pveum pool list** `[OPTIONS]` `[FORMAT_OPTIONS]`

List pools or get pool configuration.

**`--poolid` `<string>`**

no description available

**`--type` `<lxc | qemu | storage>`**

no description available

{% hint style="info" %}
Requires option(s): `poolid`
{% endhint %}

<a id="cli_pveum_pool_modify"></a>



**pveum pool modify** `<poolid>` `[OPTIONS]`

Update pool.

**`<poolid>`: `<string>`**

no description available

**`--allow-move` `<boolean>` (*default \=* `0`)**

Allow adding a guest even if already in another pool. The guest will be removed from its current pool and added to this one.

**`--comment` `<string>`**

no description available

**`--delete` `<boolean>` (*默认 \=* `0`)**

Remove the passed VMIDs and/or storage IDs instead of adding them.

**`--storage` `<string>`**

List of storage IDs to add or remove from this pool.

**`--vms` `<string>`**

List of guest VMIDs to add or remove from this pool.

<a id="cli_pveum_realm_add"></a>



**pveum realm add** `<realm> --type <string>` `[OPTIONS]`

Add an authentication server.

**`<realm>`: `<string>`**

Authentication domain ID

**`--acr-values` `^[^\x00-\x1F\x7F <>#"]*$`**

Specifies the Authentication Context Class Reference values that theAuthorization Server is being requested to use for the Auth Request.

**`--audiences` `^[^\x00-\x1F\x7F <>#"]*$`**

A list of audiences that the OpenID Issuer may include that are accepted in addition to *client-id*.

**`--autocreate` `<boolean>` (*default \=* `0`)**

Automatically create users if they do not exist.

**`--base_dn` `<string>`**

LDAP base domain name

**`--bind_dn` `<string>`**

LDAP bind domain name

**`--capath` `<string>` (*default \=* `/etc/ssl/certs`)**

Path to the CA certificate store

**`--case-sensitive` `<boolean>` (*default \=* `1`)**

username is case-sensitive

**`--cert` `<string>`**

Path to the client certificate

**`--certkey` `<string>`**

Path to the client certificate key

**`--check-connection` `<boolean>` (*default \=* `0`)**

Check bind connection to the server.

**`--client-id` `<string>`**

OpenID Client ID

**`--client-key` `<string>`**

OpenID Client Key

**`--comment` `<string>`**

描述。

**`--default` `<boolean>`**

Use this as default realm

**`--domain` `\S+`**

AD domain name

**`--filter` `<string>`**

LDAP filter for user sync.

**`--group_classes` `<string>` (*default \=* `groupOfNames, group, univentionGroup, ipausergroup`)**

The objectclasses for groups.

**`--group_dn` `<string>`**

LDAP base domain name for group sync. If not set, the base\_dn will be used.

**`--group_filter` `<string>`**

LDAP filter for group sync.

**`--group_name_attr` `<string>`**

LDAP attribute representing a groups name. If not set or found, the first value of the DN will be used as name.

**`--groups-autocreate` `<boolean>` (*default \=* `0`)**

Automatically create groups if they do not exist.

**`--groups-claim` `(?^:[A-Za-z0-9\.\-_]+)`**

OpenID claim used to retrieve groups with.

**`--groups-overwrite` `<boolean>` (*default \=* `0`)**

All groups will be overwritten for the user on login.

**`--issuer-url` `<string>`**

OpenID Issuer Url

**`--mode` `<ldap | ldap+starttls | ldaps>` (*default \=* `ldap`)**

LDAP protocol mode.

**`--password` `<string>`**

LDAP bind password. Will be stored in */etc/pve/priv/realm/\<REALM\>.pw*.

**`--port` `<integer> (1 - 65535)`**

Server port.

**`--prompt` `(?:none|login|consent|select_account|\S+)`**

Specifies whether the Authorization Server prompts the End-User for reauthentication and consent.

**`--query-userinfo` `<boolean>` (*default \=* `1`)**

Enables querying the userinfo endpoint for claims values.

**`--scopes` `<string>` (*default \=* `email profile`)**

Specifies the scopes (user details) that should be authorized and returned, for example *email* or *profile*.

**`--secure` `<boolean>`**

Use secure LDAPS protocol. DEPRECATED: use *mode* instead.

**`--server1` `<string>`**

Server IP address (or DNS name)

**`--server2` `<string>`**

Fallback Server IP address (or DNS name)

**`--sslversion` `<tlsv1 | tlsv1_1 | tlsv1_2 | tlsv1_3>`**

LDAPS TLS/SSL version. It’s not recommended to use version older than 1.2!

**`--sync-defaults-options` `[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]`**

The default options for behavior of synchronizations.

**`--sync_attributes` `\w+=[^,]+(,\s*\w+=[^,]+)*`**

Comma separated list of key\=value pairs for specifying which LDAP attributes map to which PVE user field. For example, to map the LDAP attribute *mail* to PVEs *email*, write *email\=mail*. By default, each PVE user field is represented by an LDAP attribute of the same name.

**`--tfa` `type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]`**

Use Two-factor authentication.

**`--type` `<ad | ldap | openid | pam | pve>`**

Realm type.

**`--user_attr` `\S{2,}`**

LDAP user attribute name

**`--user_classes` `<string>` (*default \=* `inetorgperson, posixaccount, person, user`)**

The objectclasses for users.

**`--username-claim` `<string>`**

OpenID claim used to generate the unique username.

**`--verify` `<boolean>` (*default \=* `0`)**

Verify the server’s SSL certificate

<a id="cli_pveum_realm_delete"></a>



**pveum realm delete** `<realm>`

Delete an authentication server.

**`<realm>`: `<string>`**

Authentication domain ID

<a id="cli_pveum_realm_list"></a>



**pveum realm list** `[FORMAT_OPTIONS]`

Authentication domain index.

<a id="cli_pveum_realm_modify"></a>



**pveum realm modify** `<realm>` `[OPTIONS]`

Update authentication server settings.

**`<realm>`: `<string>`**

Authentication domain ID

**`--acr-values` `^[^\x00-\x1F\x7F <>#"]*$`**

Specifies the Authentication Context Class Reference values that theAuthorization Server is being requested to use for the Auth Request.

**`--audiences` `^[^\x00-\x1F\x7F <>#"]*$`**

A list of audiences that the OpenID Issuer may include that are accepted in addition to *client-id*.

**`--autocreate` `<boolean>` (*default \=* `0`)**

Automatically create users if they do not exist.

**`--base_dn` `<string>`**

LDAP base domain name

**`--bind_dn` `<string>`**

LDAP bind domain name

**`--capath` `<string>` (*default \=* `/etc/ssl/certs`)**

Path to the CA certificate store

**`--case-sensitive` `<boolean>` (*default \=* `1`)**

username is case-sensitive

**`--cert` `<string>`**

Path to the client certificate

**`--certkey` `<string>`**

Path to the client certificate key

**`--check-connection` `<boolean>` (*default \=* `0`)**

Check bind connection to the server.

**`--client-id` `<string>`**

OpenID Client ID

**`--client-key` `<string>`**

OpenID Client Key

**`--comment` `<string>`**

描述。

**`--default` `<boolean>`**

Use this as default realm

**`--delete` `<string>`**

要删除的设置列表。

**`--digest` `<string>`**

如果当前配置文件的摘要不同，则阻止更改。这可用于防止并发修改。

**`--domain` `\S+`**

AD domain name

**`--filter` `<string>`**

LDAP filter for user sync.

**`--group_classes` `<string>` (*default \=* `groupOfNames, group, univentionGroup, ipausergroup`)**

The objectclasses for groups.

**`--group_dn` `<string>`**

LDAP base domain name for group sync. If not set, the base\_dn will be used.

**`--group_filter` `<string>`**

LDAP filter for group sync.

**`--group_name_attr` `<string>`**

LDAP attribute representing a groups name. If not set or found, the first value of the DN will be used as name.

**`--groups-autocreate` `<boolean>` (*default \=* `0`)**

Automatically create groups if they do not exist.

**`--groups-claim` `(?^:[A-Za-z0-9\.\-_]+)`**

OpenID claim used to retrieve groups with.

**`--groups-overwrite` `<boolean>` (*default \=* `0`)**

All groups will be overwritten for the user on login.

**`--issuer-url` `<string>`**

OpenID Issuer Url

**`--mode` `<ldap | ldap+starttls | ldaps>` (*default \=* `ldap`)**

LDAP protocol mode.

**`--password` `<string>`**

LDAP bind password. Will be stored in */etc/pve/priv/realm/\<REALM\>.pw*.

**`--port` `<integer> (1 - 65535)`**

Server port.

**`--prompt` `(?:none|login|consent|select_account|\S+)`**

Specifies whether the Authorization Server prompts the End-User for reauthentication and consent.

**`--query-userinfo` `<boolean>` (*default \=* `1`)**

Enables querying the userinfo endpoint for claims values.

**`--scopes` `<string>` (*default \=* `email profile`)**

Specifies the scopes (user details) that should be authorized and returned, for example *email* or *profile*.

**`--secure` `<boolean>`**

Use secure LDAPS protocol. DEPRECATED: use *mode* instead.

**`--server1` `<string>`**

Server IP address (or DNS name)

**`--server2` `<string>`**

Fallback Server IP address (or DNS name)

**`--sslversion` `<tlsv1 | tlsv1_1 | tlsv1_2 | tlsv1_3>`**

LDAPS TLS/SSL version. It’s not recommended to use version older than 1.2!

**`--sync-defaults-options` `[enable-new=<1|0>] [,full=<1|0>] [,purge=<1|0>] [,remove-vanished=([acl];[properties];[entry])|none] [,scope=<users|groups|both>]`**

The default options for behavior of synchronizations.

**`--sync_attributes` `\w+=[^,]+(,\s*\w+=[^,]+)*`**

Comma separated list of key\=value pairs for specifying which LDAP attributes map to which PVE user field. For example, to map the LDAP attribute *mail* to PVEs *email*, write *email\=mail*. By default, each PVE user field is represented by an LDAP attribute of the same name.

**`--tfa` `type=<TFATYPE> [,digits=<COUNT>] [,id=<ID>] [,key=<KEY>] [,step=<SECONDS>] [,url=<URL>]`**

Use Two-factor authentication.

**`--user_attr` `\S{2,}`**

LDAP user attribute name

**`--user_classes` `<string>` (*default \=* `inetorgperson, posixaccount, person, user`)**

The objectclasses for users.

**`--verify` `<boolean>` (*default \=* `0`)**

Verify the server’s SSL certificate

<a id="cli_pveum_realm_sync"></a>



**pveum realm sync** `<realm>` `[OPTIONS]`

Syncs users and/or groups from the configured LDAP to user.cfg. NOTE: Synced groups will have the name *name-$realm*, so make sure those groups do not exist to prevent overwriting.

**`<realm>`: `<string>`**

Authentication domain ID

**`--dry-run` `<boolean>` (*default \=* `0`)**

If set, does not write anything.

**`--enable-new` `<boolean>` (*default \=* `1`)**

Enable newly synced users immediately.

**`--full` `<boolean>`**

DEPRECATED: use *remove-vanished* instead. If set, uses the LDAP Directory as source of truth, deleting users or groups not returned from the sync and removing all locally modified properties of synced users. If not set, only syncs information which is present in the synced data, and does not delete or modify anything else.

**`--purge` `<boolean>`**

DEPRECATED: use *remove-vanished* instead. Remove ACLs for users or groups which were removed from the config during a sync.

**`--remove-vanished` `([acl];[properties];[entry])|none` (*default \=* `none`)**

A semicolon-separated list of things to remove when they or the user vanishes during a sync. The following values are possible: *entry* removes the user/group when not returned from the sync. *properties* removes the set properties on existing user/group that do not appear in the source (even custom ones). *acl* removes acls when the user/group is not returned from the sync. Instead of a list it also can be *none* (the default).

**`--scope` `<both | groups | users>`**

Select what to sync.

<a id="cli_pveum_role_add"></a>



**pveum role add** `<roleid>` `[OPTIONS]`

Create new role.

**`<roleid>`: `<string>`**

no description available

**`--privs` `<string>`**

no description available

<a id="cli_pveum_role_delete"></a>



**pveum role delete** `<roleid>`

Delete role.

**`<roleid>`: `<string>`**

no description available

<a id="cli_pveum_role_list"></a>



**pveum role list** `[FORMAT_OPTIONS]`

Role index.

<a id="cli_pveum_role_modify"></a>



**pveum role modify** `<roleid>` `[OPTIONS]`

Update an existing role.

**`<roleid>`: `<string>`**

no description available

**`--append` `<boolean>`**

no description available

{% hint style="info" %}
Requires option(s): `privs`
{% endhint %}

**`--privs` `<string>`**

no description available

<a id="cli_pveum_roleadd"></a>



**pveum roleadd**

An alias for *pveum role add*.

<a id="cli_pveum_roledel"></a>



**pveum roledel**

An alias for *pveum role delete*.

<a id="cli_pveum_rolemod"></a>



**pveum rolemod**

An alias for *pveum role modify*.

<a id="cli_pveum_ticket"></a>



**pveum ticket** `<username>` `[OPTIONS]`

Create or verify authentication ticket.

**`<username>`: `<string>`**

User name

**`--new-format` `<boolean>` (*default \=* `1`)**

This parameter is now ignored and assumed to be 1\.

**`--otp` `<string>`**

One-time password for Two-factor authentication.

**`--path` `<string>`**

Verify ticket, and check if user have access *privs* on *path*

{% hint style="info" %}
Requires option(s): `privs`
{% endhint %}

**`--privs` `<string>`**

Verify ticket, and check if user have access *privs* on *path*

{% hint style="info" %}
Requires option(s): `path`
{% endhint %}

**`--realm` `<string>`**

You can optionally pass the realm using this parameter. Normally the realm is simply added to the username \<username\>@\<realm\>.

**`--tfa-challenge` `<string>`**

The signed TFA challenge string the user wants to respond to.

<a id="cli_pveum_user_add"></a>



**pveum user add** `<userid>` `[OPTIONS]`

Create new user.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`--comment` `<string>`**

no description available

**`--email` `<string>`**

no description available

**`--enable` `<boolean>` (*default \=* `1`)**

Enable the account (default). You can set this to *0* to disable the account

**`--expire` `<integer> (0 - N)`**

Account expiration date (seconds since epoch). *0* means no expiration date.

**`--firstname` `<string>`**

no description available

**`--groups` `<string>`**

no description available

**`--keys` `[0-9a-zA-Z!=]{0,4096}`**

Keys for two factor auth (yubico).

**`--lastname` `<string>`**

no description available

**`--password` `<string>`**

Initial password.

<a id="cli_pveum_user_delete"></a>



**pveum user delete** `<userid>`

Delete user.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

<a id="cli_pveum_user_list"></a>



**pveum user list** `[OPTIONS]` `[FORMAT_OPTIONS]`

User index.

**`--enabled` `<boolean>`**

Optional filter for enable property.

**`--full` `<boolean>` (*default \=* `0`)**

Include group and token information.

<a id="cli_pveum_user_modify"></a>



**pveum user modify** `<userid>` `[OPTIONS]`

Update user configuration.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`--append` `<boolean>`**

no description available

{% hint style="info" %}
Requires option(s): `groups`
{% endhint %}

**`--comment` `<string>`**

no description available

**`--email` `<string>`**

no description available

**`--enable` `<boolean>` (*default \=* `1`)**

Enable the account (default). You can set this to *0* to disable the account

**`--expire` `<integer> (0 - N)`**

Account expiration date (seconds since epoch). *0* means no expiration date.

**`--firstname` `<string>`**

no description available

**`--groups` `<string>`**

no description available

**`--keys` `[0-9a-zA-Z!=]{0,4096}`**

Keys for two factor auth (yubico).

**`--lastname` `<string>`**

no description available

<a id="cli_pveum_user_permissions"></a>



**pveum user permissions** `[<userid>]` `[OPTIONS]` `[FORMAT_OPTIONS]`

Retrieve effective permissions of given user/token.

**`<userid>`: `(?^:^(?^:[^\s:/]+)\@(?^:[A-Za-z][A-Za-z0-9\.\-_]+)(?:!(?^:[A-Za-z][A-Za-z0-9\.\-_]+))?$)`**

User ID or full API token ID

**`--path` `<string>`**

Only dump this specific path, not the whole tree.

<a id="cli_pveum_user_tfa_delete"></a>



**pveum user tfa delete** `<userid>` `[OPTIONS]`

Delete TFA entries from a user.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`--id` `<string>`**

The TFA ID, if none provided, all TFA entries will be deleted.

<a id="cli_pveum_user_tfa_list"></a>



**pveum user tfa list** `[<userid>]`

List TFA entries.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

<a id="cli_pveum_user_tfa_unlock"></a>



**pveum user tfa unlock** `<userid>`

Unlock a user’s TFA authentication.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

<a id="cli_pveum_user_token_add"></a>



**pveum user token add** `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Generate a new API token for a specific user. NOTE: returns API token value, which needs to be stored as it cannot be retrieved afterwards!

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

User-specific token identifier.

**`--comment` `<string>`**

no description available

**`--expire` `<integer> (0 - N)` (*default \=* `same as user`)**

API token expiration date (seconds since epoch). *0* means no expiration date.

**`--privsep` `<boolean>` (*default \=* `1`)**

Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.

<a id="cli_pveum_user_token_delete"></a>



**pveum user token delete** `<userid> <tokenid>` `[FORMAT_OPTIONS]`

Remove API token for a specific user.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

User-specific token identifier.

<a id="cli_pveum_user_token_list"></a>



**pveum user token list** `<userid>` `[FORMAT_OPTIONS]`

Get user API tokens.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

<a id="cli_pveum_user_token_modify"></a>



**pveum user token modify** `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Update API token for a specific user. NOTE: when *regenerate* is set, the returned token value needs to be stored as it cannot be retrieved afterwards!

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

User-specific token identifier.

**`--comment` `<string>`**

no description available

**`--delete` `<string>`**

要删除的设置列表。

**`--expire` `<integer> (0 - N)` (*default \=* `same as user`)**

API token expiration date (seconds since epoch). *0* means no expiration date.

**`--privsep` `<boolean>` (*default \=* `1`)**

Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user.

**`--regenerate` `<boolean>` (*default \=* `0`)**

Regenerate the token’s secret value. All users of the previous secret will lose access after this operation.

<a id="cli_pveum_user_token_permissions"></a>



**pveum user token permissions** `<userid> <tokenid>` `[OPTIONS]` `[FORMAT_OPTIONS]`

Retrieve effective permissions of given token.

**`<userid>`: `<string>`**

Full User ID, in the `name@realm` format.

**`<tokenid>`: `(?^:[A-Za-z][A-Za-z0-9\.\-_]+)`**

User-specific token identifier.

**`--path` `<string>`**

Only dump this specific path, not the whole tree.

<a id="cli_pveum_user_token_remove"></a>



**pveum user token remove**

An alias for *pveum user token delete*.

<a id="cli_pveum_useradd"></a>



**pveum useradd**

An alias for *pveum user add*.

<a id="cli_pveum_userdel"></a>



**pveum userdel**

An alias for *pveum user delete*.

<a id="cli_pveum_usermod"></a>



**pveum usermod**

An alias for *pveum user modify*.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
