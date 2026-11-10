# 18.2. pveproxy \- Proxmox VE API 代理守护进程 <a href="#pveproxy_proxmox_ve_api_proxy_daemon" id="pveproxy_proxmox_ve_api_proxy_daemon"></a>

此守护进程通过 HTTPS 在 TCP 端口 8006 上提供完整的 Proxmox VE API。它以用户 `www-data` 身份运行，权限非常有限。需要更多权限的操作会转发到本地 `pvedaemon`。

发往其他节点的请求会自动转发到相应节点。这意味着只需连接到一个 Proxmox VE 节点，就可以管理整个集群。

## 18.2.1. 基于宿主机的访问控制 <a href="#pveproxy_host_acls" id="pveproxy_host_acls"></a>

可以配置类似“apache2”的访问控制列表。各项值从文件 `/etc/default/pveproxy` 读取。例如：

```text
ALLOW_FROM="10.0.0.1-10.0.0.5,192.168.0.0/22"
DENY_FROM="all"
POLICY="allow"
```

可以使用 `Net::IP` 能理解的任意语法指定 IP 地址。名称 `all` 是 `0/0` 和 `::/0` 的别名（表示所有 IPv4 和 IPv6 地址）。

默认策略为 `allow`。

<table>



<thead>
<tr>
<th>匹配</th>
<th>POLICY=deny</th>
<th>POLICY=allow</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>仅匹配 Allow</p></td>
<td><p>allow</p></td>
<td><p>allow</p></td>
</tr>
<tr>
<td><p>仅匹配 Deny</p></td>
<td><p>deny</p></td>
<td><p>deny</p></td>
</tr>
<tr>
<td><p>无匹配</p></td>
<td><p>deny</p></td>
<td><p>allow</p></td>
</tr>
<tr>
<td><p>同时匹配 Allow 和 Deny</p></td>
<td><p>deny</p></td>
<td><p>allow</p></td>
</tr>
</tbody>
</table>

## 18.2.2. 监听 IP 地址 <a href="#pveproxy_listening_address" id="pveproxy_listening_address"></a>

默认情况下，`pveproxy` 和 `spiceproxy` 守护进程监听通配地址，并接受来自 IPv4 和 IPv6 客户端的连接。

通过设置 `LISTEN_IP`（位于 `/etc/default/pveproxy` 中），可以控制 `pveproxy` 和 `spiceproxy` 守护进程绑定到哪个 IP 地址。该 IP 地址需要在系统上配置。

将 `sysctl` 的 `net.ipv6.bindv6only` 设置为非默认的 `1`，会导致守护进程仅接受 IPv6 客户端的连接，通常还会引发许多其他问题。如果设置此配置，建议移除 `sysctl` 设置，或将 `LISTEN_IP` 设置为 `0.0.0.0`（这将仅允许 IPv4 客户端）。

`LISTEN_IP` 可用于将套接字限制在内部接口，从而减少对公共互联网的暴露，例如：

```text
LISTEN_IP="192.0.2.1"
```

同样，也可以设置 IPv6 地址：

```text
LISTEN_IP="2001:db8:85a3::1"
```

请注意，如果要指定链路本地 IPv6 地址，需要提供接口名称本身。例如：

```text
LISTEN_IP="fe80::c463:8cff:feb9:6a4e%vmbr0"
```

{% hint style="warning" %}
集群中的节点需要访问 `pveproxy` 进行通信，可能跨越不同子网。**不建议**在集群系统上设置 `LISTEN_IP`。
{% endhint %}

要应用更改，需要重启节点，或完全重启 `pveproxy` 和 `spiceproxy` 服务：

```text
systemctl restart pveproxy.service spiceproxy.service
```

{% hint style="info" %}
与 `reload` 不同，对 pveproxy 服务执行 `restart` 可能会中断一些长时间运行的工作进程，例如虚拟客户机中正在运行的控制台或 Shell。因此，请在维护窗口内使此更改生效。
{% endhint %}

## 18.2.3. SSL 密码套件 <a href="#ssl_cipher_suite" id="ssl_cipher_suite"></a>

可以在 `/etc/default/pveproxy` 中，通过 `CIPHERS`（TLS ⇐ 1.2）和 `CIPHERSUITES`（TLS \>\= 1.3）键定义密码套件列表。例如

```text
CIPHERS="ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256"
CIPHERSUITES="TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256"
```

以上为默认值。所有可用选项的列表请参阅 openssl 软件包中的 ciphers(1) 手册页。

此外，可以在 `/etc/default/pveproxy` 中设置由客户端选择使用的密码套件（默认是客户端与 `pveproxy` 均支持的列表中首个密码套件）：

```text
HONOR_CIPHER_ORDER=0
```

## 18.2.4. 支持的 TLS 版本 <a href="#supported_tls_versions" id="supported_tls_versions"></a>

pveproxy 无条件禁用不安全的 SSL 版本 2 和 3。近期 OpenSSL 版本默认禁用低于 1.1 的 TLS 版本，`pveproxy` 也遵循此设置（参见 `/etc/ssl/openssl.cnf`）。

要禁用 TLS 版本 1.2 或 1.3，请在 `/etc/default/pveproxy` 中设置以下内容：

```text
DISABLE_TLS_1_2=1
```

或分别设置为：

```text
DISABLE_TLS_1_3=1
```

{% hint style="info" %}
除非有具体原因，否则不建议手动调整支持的 TLS 版本。
{% endhint %}

## 18.2.5. Diffie-Hellman 参数 <a href="#diffie_hellman_parameters" id="diffie_hellman_parameters"></a>

可以在 `/etc/default/pveproxy` 中定义使用的 Diffie-Hellman 参数，方法是将 `DHPARAMS` 设置为包含 PEM 格式 DH 参数的文件路径，例如

```text
DHPARAMS="/path/to/dhparams.pem"
```

如果未设置此选项，则使用内置的 `skip2048` 参数。

{% hint style="info" %}
只有协商选用采用 DH 密钥交换算法的密码套件时，才会使用 DH 参数。
{% endhint %}

## 18.2.6. 替代 HTTPS 证书 <a href="#pveproxy_custom_tls_cert" id="pveproxy_custom_tls_cert"></a>

可以将所用证书改为外部证书或通过 ACME 获取的证书。

如果存在，pveproxy 使用 `/etc/pve/local/pveproxy-ssl.pem` 和 `/etc/pve/local/pveproxy-ssl.key`，否则回退到 `/etc/pve/local/pve-ssl.pem` 和 `/etc/pve/local/pve-ssl.key`。私钥不得使用口令。

可以覆盖证书私钥 `/etc/pve/local/pveproxy-ssl.key` 的位置，方法是设置 `TLS_KEY_FILE`，该设置位于 `/etc/default/pveproxy` 中，例如：

```text
TLS_KEY_FILE="/secrets/pveproxy.key"
```

{% hint style="info" %}
内置的 ACME 集成不遵循此设置。
{% endhint %}

详情请参阅文档的宿主机系统管理章节。

## 18.2.7. 响应压缩 <a href="#pveproxy_response_compression" id="pveproxy_response_compression"></a>

默认情况下，如果客户端支持，`pveproxy` 会对可压缩内容使用 gzip HTTP 层压缩。可以在 `/etc/default/pveproxy` 中禁用：

```text
COMPRESSION=0
```

{% hint style="info" %}
禁用压缩可缓解针对已认证会话 Cookie 的 BREACH 类侧信道攻击，代价是 Web 界面的带宽用量略有增加。大多数部署无需更改默认值；对于 Web 界面需要跨越不完全受您控制的网络进行访问的宿主机，可以考虑此设置。
{% endhint %}

## 18.2.8. 真实客户端 IP 日志记录 <a href="#pveproxy_real_ip" id="pveproxy_real_ip"></a>

默认情况下，`pveproxy` 记录发送请求的客户端 IP 地址。如果在 `pveproxy` 前方部署了代理服务器，可能希望记录发出请求的客户端 IP，而不是代理的 IP。

要启用对代理设置的 HTTP 标头的处理以用于日志记录，请将 `PROXY_REAL_IP_HEADER` 设置为用于获取客户端 IP 的标头名称。例如：

```text
PROXY_REAL_IP_HEADER="X-Forwarded-For"
```

此标头中传入的任何无效值都会被忽略。

默认行为是对所有传入请求记录此标头中的值。要定义可信任的代理服务器列表，允许这些服务器设置上述 HTTP 标头，请设置 `PROXY_REAL_IP_ALLOW_FROM`，例如：

```text
PROXY_REAL_IP_ALLOW_FROM="192.168.0.2"
```

`PROXY_REAL_IP_ALLOW_FROM` 设置也支持与 `ALLOW_FROM` 和 `DENY_FROM` 设置类似的值。

可以使用 `Net::IP` 能理解的任意语法指定 IP 地址。名称 `all` 是 `0/0` 和 `::/0` 的别名（表示所有 IPv4 和 IPv6 地址）。

## 18.2.9. 工作进程数量 <a href="#pveproxy_max_workers" id="pveproxy_max_workers"></a>

`pveproxy` 将传入请求交给工作进程处理。默认情况下，`pveproxy` 启动 3 个工作进程，这对大多数工作负载已经足够。对于发出大量 API 请求并遇到请求处理缓慢或超时的高度自动化工作负载，可以设置 `MAX_WORKERS` 来增加工作进程数量，此设置位于 `/etc/default/pveproxy` 中，例如：

```text
MAX_WORKERS=5
```

请注意，增加工作进程数量可能会提高 CPU 使用率。工作进程数量必须大于 0 且小于 128。

[pvedaemon](01-pvedaemon-proxmox-ve-api-daemon.md#pvedaemon_max_workers) 也有相同的设置。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
