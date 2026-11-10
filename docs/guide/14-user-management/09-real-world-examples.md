# 14.9. 实际示例 <a href="#real_world_examples" id="real_world_examples"></a>

## 14.9.1. 管理员组 <a href="#administrator_group" id="administrator_group"></a>

管理员可能希望创建一组具有完整管理员权限的用户（不使用 root 账户）。

为此，首先定义组：

```text
 pveum group add admin -comment "System Administrators"
```

然后分配角色：

```text
 pveum acl modify / -group admin -role Administrator
```

最后，可以将用户添加到新的 *admin* 组：

```text
 pveum user modify testuser@pve -group admin
```

## 14.9.2. 审计员 <a href="#auditors" id="auditors"></a>

可以通过向用户或组分配 `PVEAuditor` 角色，授予用户只读访问权限。

示例 1：允许用户 `joe@pve` 查看所有内容

```text
 pveum acl modify / -user joe@pve -role PVEAuditor
```

示例 2：允许用户 `joe@pve` 查看所有虚拟机

```text
 pveum acl modify /vms -user joe@pve -role PVEAuditor
```

## 14.9.3. 委派用户管理 <a href="#delegate_user_management" id="delegate_user_management"></a>

如果希望将用户管理委派给用户 `joe@pve`，可以使用：

```text
 pveum acl modify /access -user joe@pve -role PVEUserAdmin
```

用户 `joe@pve` 现在可以添加和移除用户，以及更改其他用户属性，例如密码。这是一个非常强大的角色，您很可能希望将其限制在选定的认证域和组中。以下示例允许 `joe@pve` 修改认证域 `pve` 内的用户，条件是这些用户属于组 `customers`：

```text
 pveum acl modify /access/realm/pve -user joe@pve -role PVEUserAdmin
 pveum acl modify /access/groups/customers -user joe@pve -role PVEUserAdmin
```

{% hint style="info" %}
该用户可以添加其他用户，但前提是这些用户属于组 `customers` 且位于认证域 `pve` 内。
{% endhint %}

## 14.9.4. 用于监控的受限 API 令牌 <a href="#limited_api_token_for_monitoring" id="limited_api_token_for_monitoring"></a>

API 令牌的权限始终是对应用户权限的子集，这意味着 API 令牌不能用于执行其所属用户无权执行的任务。本节将演示如何使用具有单独权限的 API 令牌，进一步限制令牌所有者的权限。

为用户 `joe@pve` 在所有虚拟机上授予 PVEVMAdmin 角色：

```text
 pveum acl modify /vms -user joe@pve -role PVEVMAdmin
```

添加具有单独权限的新 API 令牌，仅允许查看虚拟机信息（例如用于监控）：

```text
 pveum user token add joe@pve monitoring -privsep 1
 pveum acl modify /vms -token 'joe@pve!monitoring' -role PVEAuditor
```

验证用户和令牌的权限：

```text
 pveum user permissions joe@pve
 pveum user token permissions joe@pve monitoring
```

## 14.9.5. 资源池 <a href="#resource_pools" id="resource_pools"></a>

企业通常分为多个较小部门，通常希望为各部门分配资源并委派管理任务。假设要为软件开发部门设置一个池。首先创建组：

```text
 pveum group add developers -comment "Our software developers"
```

现在创建属于该组的新用户：

```text
 pveum user add developer1@pve -group developers -password
```

{% hint style="info" %}
“-password”参数将提示输入密码
{% endhint %}

然后为开发部门创建资源池：

```text
 pveum pool add dev-pool --comment "IT development pool"
```

最后，可以为该池分配权限：

```text
 pveum acl modify /pool/dev-pool/ -group developers -role PVEAdmin
```

软件开发人员现在可以管理分配给该池的资源。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
