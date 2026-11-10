# 14.9. Real World Examples <a href="#_real_world_examples" id="_real_world_examples"></a>

## 14.9.1. Administrator Group <a href="#_administrator_group" id="_administrator_group"></a>

It is possible that an administrator would want to create a group of users with full administrator rights (without using the root account).

To do this, first define the group:

```text
 pveum group add admin -comment "System Administrators"
```

Then assign the role:

```text
 pveum acl modify / -group admin -role Administrator
```

Finally, you can add users to the new *admin* group:

```text
 pveum user modify testuser@pve -group admin
```

## 14.9.2. Auditors <a href="#_auditors" id="_auditors"></a>

You can give read only access to users by assigning the `PVEAuditor` role to users or groups.

Example 1: Allow user `joe@pve` to see everything

```text
 pveum acl modify / -user joe@pve -role PVEAuditor
```

Example 2: Allow user `joe@pve` to see all virtual machines

```text
 pveum acl modify /vms -user joe@pve -role PVEAuditor
```

## 14.9.3. Delegate User Management <a href="#_delegate_user_management" id="_delegate_user_management"></a>

If you want to delegate user management to user `joe@pve`, you can do that with:

```text
 pveum acl modify /access -user joe@pve -role PVEUserAdmin
```

User `joe@pve` can now add and remove users, and change other user attributes, such as passwords. This is a very powerful role, and you most likely want to limit it to selected realms and groups. The following example allows `joe@pve` to modify users within the realm `pve`, if they are members of group `customers`:

```text
 pveum acl modify /access/realm/pve -user joe@pve -role PVEUserAdmin
 pveum acl modify /access/groups/customers -user joe@pve -role PVEUserAdmin
```

{% hint style="info" %}
The user is able to add other users, but only if they are members of the group `customers` and within the realm `pve`.
{% endhint %}

## 14.9.4. Limited API Token for Monitoring <a href="#_limited_api_token_for_monitoring" id="_limited_api_token_for_monitoring"></a>

Permissions on API tokens are always a subset of those of their corresponding user, meaning that an API token can’t be used to carry out a task that the backing user has no permission to do. This section will demonstrate how you can use an API token with separate privileges, to limit the token owner’s permissions further.

Give the user `joe@pve` the role PVEVMAdmin on all VMs:

```text
 pveum acl modify /vms -user joe@pve -role PVEVMAdmin
```

Add a new API token with separate privileges, which is only allowed to view VM information (for example, for monitoring purposes):

```text
 pveum user token add joe@pve monitoring -privsep 1
 pveum acl modify /vms -token 'joe@pve!monitoring' -role PVEAuditor
```

Verify the permissions of the user and token:

```text
 pveum user permissions joe@pve
 pveum user token permissions joe@pve monitoring
```

## 14.9.5. Resource Pools <a href="#_resource_pools" id="_resource_pools"></a>

An enterprise is usually structured into several smaller departments, and it is common that you want to assign resources and delegate management tasks to each of these. Let’s assume that you want to set up a pool for a software development department. First, create a group:

```text
 pveum group add developers -comment "Our software developers"
```

Now we create a new user which is a member of that group:

```text
 pveum user add developer1@pve -group developers -password
```

{% hint style="info" %}
The "-password" parameter will prompt you for a password
{% endhint %}

Then we create a resource pool for our development department to use:

```text
 pveum pool add dev-pool --comment "IT development pool"
```

Finally, we can assign permissions to that pool:

```text
 pveum acl modify /pool/dev-pool/ -group developers -role PVEAdmin
```

Our software developers can now administer the resources assigned to that pool.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
