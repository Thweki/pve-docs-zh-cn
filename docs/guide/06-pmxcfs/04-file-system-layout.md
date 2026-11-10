# 6.4. 文件系统布局 <a href="#file_system_layout" id="file_system_layout"></a>

该文件系统挂载于：

```text
/etc/pve
```

## 6.4.1. 文件 <a href="#files" id="files"></a>

<table>


<tbody>
<tr>
<td><p><code>authkey.pub</code></p></td>
<td><p>票据系统使用的公钥</p></td>
</tr>
<tr>
<td><p><code>ceph.conf</code></p></td>
<td><p>Ceph 配置文件（注意：/etc/ceph/ceph.conf 是指向此文件的符号链接）</p></td>
</tr>
<tr>
<td><p><code>corosync.conf</code></p></td>
<td><p>Corosync 集群配置文件（在 Proxmox VE 4.x 之前，此文件称为 cluster.conf）</p></td>
</tr>
<tr>
<td><p><code>datacenter.cfg</code></p></td>
<td><p>Proxmox VE 全数据中心范围的配置（键盘布局、代理等）</p></td>
</tr>
<tr>
<td><p><code>domains.cfg</code></p></td>
<td><p>Proxmox VE 身份验证域</p></td>
</tr>
<tr>
<td><p><code>firewall/cluster.fw</code></p></td>
<td><p>应用于所有节点的防火墙配置</p></td>
</tr>
<tr>
<td><p><code>firewall/&lt;NAME&gt;.fw</code></p></td>
<td><p>各个节点的防火墙配置</p></td>
</tr>
<tr>
<td><p><code>firewall/&lt;VMID&gt;.fw</code></p></td>
<td><p>VM 和容器的防火墙配置</p></td>
</tr>
<tr>
<td><p><code>ha/crm_commands</code></p></td>
<td><p>显示 CRM 当前正在执行的 HA 操作</p></td>
</tr>
<tr>
<td><p><code>ha/manager_status</code></p></td>
<td><p>有关集群中 HA 服务的 JSON 格式信息</p></td>
</tr>
<tr>
<td><p><code>ha/resources.cfg</code></p></td>
<td><p>高可用性管理的资源及其当前状态</p></td>
</tr>
<tr>
<td><p><code>ha/rules.cfg</code></p></td>
<td><p>用于约束 HA 管理器调度 HA 资源的规则</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/config</code></p></td>
<td><p>节点特定配置</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/lxc/&lt;VMID&gt;.conf</code></p></td>
<td><p>LXC 容器的 VM 配置数据</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/openvz/</code></p></td>
<td><p>在 Proxmox VE 4.0 之前，用于容器配置数据（已弃用，即将移除）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pve-ssl.key</code></p></td>
<td><p><code>pve-ssl.pem</code> 的 SSL 私钥</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pve-ssl.pem</code></p></td>
<td><p>Web 服务器的 SSL 公共证书（由集群 CA 签名）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pveproxy-ssl.key</code></p></td>
<td><p><code>pveproxy-ssl.pem</code> 的 SSL 私钥（可选）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/pveproxy-ssl.pem</code></p></td>
<td><p>Web 服务器的 SSL 公共证书（链）（可选，用于覆盖 <code>pve-ssl.pem</code>）</p></td>
</tr>
<tr>
<td><p><code>nodes/&lt;NAME&gt;/qemu-server/&lt;VMID&gt;.conf</code></p></td>
<td><p>KVM VM 的 VM 配置数据</p></td>
</tr>
<tr>
<td><p><code>priv/authkey.key</code></p></td>
<td><p>票据系统使用的私钥</p></td>
</tr>
<tr>
<td><p><code>priv/authorized_keys</code></p></td>
<td><p>用于身份验证的集群成员 SSH 密钥</p></td>
</tr>
<tr>
<td><p><code>priv/ceph*</code></p></td>
<td><p>Ceph 身份验证密钥及相关权限</p></td>
</tr>
<tr>
<td><p><code>priv/known_hosts</code></p></td>
<td><p>用于验证的集群成员 SSH 密钥</p></td>
</tr>
<tr>
<td><p><code>priv/lock/*</code></p></td>
<td><p>各种服务使用的锁文件，以确保集群范围操作的安全</p></td>
</tr>
<tr>
<td><p><code>priv/pve-root-ca.key</code></p></td>
<td><p>集群 CA 的私钥</p></td>
</tr>
<tr>
<td><p><code>priv/shadow.cfg</code></p></td>
<td><p>PVE Realm 用户的 shadow 密码文件</p></td>
</tr>
<tr>
<td><p><code>priv/storage/&lt;STORAGE-ID&gt;.pw</code></p></td>
<td><p>以明文形式包含某个存储的密码</p></td>
</tr>
<tr>
<td><p><code>priv/tfa.cfg</code></p></td>
<td><p>Base64 编码的双因素身份验证配置</p></td>
</tr>
<tr>
<td><p><code>priv/token.cfg</code></p></td>
<td><p>所有 API 令牌的密钥</p></td>
</tr>
<tr>
<td><p><code>pve-root-ca.pem</code></p></td>
<td><p>集群 CA 的公共证书</p></td>
</tr>
<tr>
<td><p><code>pve-www.key</code></p></td>
<td><p>用于生成 CSRF 令牌的私钥</p></td>
</tr>
<tr>
<td><p><code>sdn/*</code></p></td>
<td><p>软件定义网络（SDN）的共享配置文件</p></td>
</tr>
<tr>
<td><p><code>status.cfg</code></p></td>
<td><p>Proxmox VE 外部指标服务器配置</p></td>
</tr>
<tr>
<td><p><code>storage.cfg</code></p></td>
<td><p>Proxmox VE 存储配置</p></td>
</tr>
<tr>
<td><p><code>user.cfg</code></p></td>
<td><p>Proxmox VE 访问控制配置（用户/组/……）</p></td>
</tr>
<tr>
<td><p><code>virtual-guest/cpu-models.conf</code></p></td>
<td><p>用于存储自定义 CPU 模型</p></td>
</tr>
<tr>
<td><p><code>vzdump.cron</code></p></td>
<td><p>集群范围的 vzdump 备份任务计划</p></td>
</tr>
</tbody>
</table>

## 6.4.2. 符号链接 <a href="#symbolic_links" id="symbolic_links"></a>

集群文件系统中的某些目录使用符号链接，以指向节点自身的配置文件。因此，下表中所指向的文件在集群的每个节点上分别对应不同的文件。

<table>


<tbody>
<tr>
<td><p><code>local</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;</code></p></td>
</tr>
<tr>
<td><p><code>lxc</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;/lxc/</code></p></td>
</tr>
<tr>
<td><p><code>openvz</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;/openvz/</code> (deprecated, removed soon)</p></td>
</tr>
<tr>
<td><p><code>qemu-server</code></p></td>
<td><p><code>nodes/&lt;LOCAL_HOST_NAME&gt;/qemu-server/</code></p></td>
</tr>
</tbody>
</table>

## 6.4.3. 用于调试的特殊状态文件（JSON） <a href="#special_status_files_for_debugging_json" id="special_status_files_for_debugging_json"></a>

<table>


<tbody>
<tr>
<td><p><code>.version</code></p></td>
<td><p>文件版本（用于检测文件修改）</p></td>
</tr>
<tr>
<td><p><code>.members</code></p></td>
<td><p>集群成员信息</p></td>
</tr>
<tr>
<td><p><code>.vmlist</code></p></td>
<td><p>所有 VM 的列表</p></td>
</tr>
<tr>
<td><p><code>.clusterlog</code></p></td>
<td><p>集群日志（最后 50 条）</p></td>
</tr>
<tr>
<td><p><code>.rrd</code></p></td>
<td><p>RRD 数据（最新条目）</p></td>
</tr>
</tbody>
</table>

## 6.4.4. 启用/禁用调试 <a href="#enable_disable_debugging" id="enable_disable_debugging"></a>

可以使用以下命令启用详细的 syslog 消息：

```text
echo "1" >/etc/pve/.debug
```

并使用以下命令禁用详细的 syslog 消息：

```text
echo "0" >/etc/pve/.debug
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
