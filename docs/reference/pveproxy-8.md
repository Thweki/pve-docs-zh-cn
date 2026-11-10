# pveproxy(8)

## NAME <a href="#_name" id="_name"></a>

pveproxy \- PVE API Proxy Daemon

## SYNOPSIS <a href="#_synopsis" id="_synopsis"></a>

<a id="cli_pveproxy"></a>



**pveproxy** `<COMMAND> [ARGS] [OPTIONS]`

<a id="cli_pveproxy_help"></a>



**pveproxy help** `[OPTIONS]`

获取指定命令的帮助。

**`--extra-args` `<array>`**

显示特定命令的帮助

**`--verbose` `<boolean>`**

详细输出格式。

<a id="cli_pveproxy_restart"></a>



**pveproxy restart**

Restart the daemon (or start if not running).

<a id="cli_pveproxy_start"></a>



**pveproxy start** `[OPTIONS]`

Start the daemon.

**`--debug` `<boolean>` (*default \=* `0`)**

Debug mode \- stay in foreground

<a id="cli_pveproxy_status"></a>



**pveproxy status**

Get daemon status.

<a id="cli_pveproxy_stop"></a>



**pveproxy stop**

Stop the daemon.

## DESCRIPTION <a href="#_description" id="_description"></a>

This daemon exposes the whole Proxmox VE API on TCP port 8006 using HTTPS. It runs as user `www-data` and has very limited permissions. Operation requiring more permissions are forwarded to the local `pvedaemon`.

Requests targeted for other nodes are automatically forwarded to those nodes. This means that you can manage your whole cluster by connecting to a single Proxmox VE node.

## Host based Access Control <a href="#pveproxy_host_acls" id="pveproxy_host_acls"></a>

It is possible to configure “apache2”-like access control lists. Values are read from file `/etc/default/pveproxy`. For example:

```text
ALLOW_FROM="10.0.0.1-10.0.0.5,192.168.0.0/22"
DENY_FROM="all"
POLICY="allow"
```

IP addresses can be specified using any syntax understood by `Net::IP`. The name `all` is an alias for `0/0` and `::/0` (meaning all IPv4 and IPv6 addresses).

The default policy is `allow`.

<table>



<thead>
<tr>
<th>Match</th>
<th>POLICY=deny</th>
<th>POLICY=allow</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>Match Allow only</p></td>
<td><p>allow</p></td>
<td><p>allow</p></td>
</tr>
<tr>
<td><p>Match Deny only</p></td>
<td><p>deny</p></td>
<td><p>deny</p></td>
</tr>
<tr>
<td><p>No match</p></td>
<td><p>deny</p></td>
<td><p>allow</p></td>
</tr>
<tr>
<td><p>Match Both Allow &amp; Deny</p></td>
<td><p>deny</p></td>
<td><p>allow</p></td>
</tr>
</tbody>
</table>

## Listening IP Address <a href="#pveproxy_listening_address" id="pveproxy_listening_address"></a>

By default the `pveproxy` and `spiceproxy` daemons listen on the wildcard address and accept connections from both IPv4 and IPv6 clients.

By setting `LISTEN_IP` in `/etc/default/pveproxy` you can control to which IP address the `pveproxy` and `spiceproxy` daemons bind. The IP-address needs to be configured on the system.

Setting the `sysctl` `net.ipv6.bindv6only` to the non-default `1` will cause the daemons to only accept connection from IPv6 clients, while usually also causing lots of other issues. If you set this configuration we recommend to either remove the `sysctl` setting, or set the `LISTEN_IP` to `0.0.0.0` (which will only allow IPv4 clients).

`LISTEN_IP` can be used to only to restricting the socket to an internal interface and thus have less exposure to the public internet, for example:

```text
LISTEN_IP="192.0.2.1"
```

Similarly, you can also set an IPv6 address:

```text
LISTEN_IP="2001:db8:85a3::1"
```

Note that if you want to specify a link-local IPv6 address, you need to provide the interface name itself. For example:

```text
LISTEN_IP="fe80::c463:8cff:feb9:6a4e%vmbr0"
```

{% hint style="warning" %}
The nodes in a cluster need access to `pveproxy` for communication, possibly on different sub-nets. It is **not recommended** to set `LISTEN_IP` on clustered systems.
{% endhint %}

To apply the change you need to either reboot your node or fully restart the `pveproxy` and `spiceproxy` service:

```text
systemctl restart pveproxy.service spiceproxy.service
```

{% hint style="info" %}
Unlike `reload`, a `restart` of the pveproxy service can interrupt some long-running worker processes, for example a running console or shell from a virtual guest. So, please use a maintenance window to bring this change in effect.
{% endhint %}

## SSL Cipher Suite <a href="#_ssl_cipher_suite" id="_ssl_cipher_suite"></a>

You can define the cipher list in `/etc/default/pveproxy` via the `CIPHERS` (TLS ⇐ 1.2) and `CIPHERSUITES` (TLS \>\= 1.3) keys. For example

```text
CIPHERS="ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256"
CIPHERSUITES="TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256"
```

Above is the default. See the ciphers(1) man page from the openssl package for a list of all available options.

Additionally, you can set the client to choose the cipher used in `/etc/default/pveproxy` (default is the first cipher in the list available to both client and `pveproxy`):

```text
HONOR_CIPHER_ORDER=0
```

## Supported TLS versions <a href="#_supported_tls_versions" id="_supported_tls_versions"></a>

The insecure SSL versions 2 and 3 are unconditionally disabled for pveproxy. TLS versions below 1.1 are disabled by default on recent OpenSSL versions, which is honored by `pveproxy` (see `/etc/ssl/openssl.cnf`).

To disable TLS version 1.2 or 1.3, set the following in `/etc/default/pveproxy`:

```text
DISABLE_TLS_1_2=1
```

or, respectively:

```text
DISABLE_TLS_1_3=1
```

{% hint style="info" %}
Unless there is a specific reason to do so, it is not recommended to manually adjust the supported TLS versions.
{% endhint %}

## Diffie-Hellman Parameters <a href="#_diffie_hellman_parameters" id="_diffie_hellman_parameters"></a>

You can define the used Diffie-Hellman parameters in `/etc/default/pveproxy` by setting `DHPARAMS` to the path of a file containing DH parameters in PEM format, for example

```text
DHPARAMS="/path/to/dhparams.pem"
```

If this option is not set, the built-in `skip2048` parameters will be used.

{% hint style="info" %}
DH parameters are only used if a cipher suite utilizing the DH key exchange algorithm is negotiated.
{% endhint %}

## Alternative HTTPS certificate <a href="#pveproxy_custom_tls_cert" id="pveproxy_custom_tls_cert"></a>

You can change the certificate used to an external one or to one obtained via ACME.

pveproxy uses `/etc/pve/local/pveproxy-ssl.pem` and `/etc/pve/local/pveproxy-ssl.key`, if present, and falls back to `/etc/pve/local/pve-ssl.pem` and `/etc/pve/local/pve-ssl.key`. The private key may not use a passphrase.

It is possible to override the location of the certificate private key `/etc/pve/local/pveproxy-ssl.key` by setting `TLS_KEY_FILE` in `/etc/default/pveproxy`, for example:

```text
TLS_KEY_FILE="/secrets/pveproxy.key"
```

{% hint style="info" %}
The included ACME integration does not honor this setting.
{% endhint %}

See the Host System Administration chapter of the documentation for details.

## Response Compression <a href="#pveproxy_response_compression" id="pveproxy_response_compression"></a>

By default `pveproxy` uses gzip HTTP-level compression for compressible content, if the client supports it. This can be disabled in `/etc/default/pveproxy`:

```text
COMPRESSION=0
```

{% hint style="info" %}
Disabling compression mitigates BREACH-class side-channel attacks against authenticated session cookies, at the cost of slightly more bandwidth used by the web interface. Most deployments do not need to change the default; consider it on hosts where the web interface is exposed across networks you do not fully control.
{% endhint %}

## Real Client IP Logging <a href="#pveproxy_real_ip" id="pveproxy_real_ip"></a>

By default, `pveproxy` logs the IP address of the client that sent the request. In cases where a proxy server is in front of `pveproxy`, it may be desirable to log the IP of the client making the request instead of the proxy IP.

To enable processing of a HTTP header set by the proxy for logging purposes, set `PROXY_REAL_IP_HEADER` to the name of the header to retrieve the client IP from. For example:

```text
PROXY_REAL_IP_HEADER="X-Forwarded-For"
```

Any invalid values passed in this header will be ignored.

The default behavior is log the value in this header on all incoming requests. To define a list of proxy servers that should be trusted to set the above HTTP header, set `PROXY_REAL_IP_ALLOW_FROM`, for example:

```text
PROXY_REAL_IP_ALLOW_FROM="192.168.0.2"
```

The `PROXY_REAL_IP_ALLOW_FROM` setting also supports values similar to the `ALLOW_FROM` and `DENY_FROM` settings.

IP addresses can be specified using any syntax understood by `Net::IP`. The name `all` is an alias for `0/0` and `::/0` (meaning all IPv4 and IPv6 addresses).

## Number of Workers <a href="#pveproxy_max_workers" id="pveproxy_max_workers"></a>

`pveproxy` delegates handling of incoming requests to worker processes. By default, `pveproxy` spawns 3 worker processes, which is sufficient for most workloads. For automation-heavy workloads that issue a huge volume of API requests and that experience slow request handling or timeouts, the number of worker processes can be increased by setting `MAX_WORKERS` in `/etc/default/pveproxy`, for example:

```text
MAX_WORKERS=5
```

Note that a higher number of worker processes may result in higher CPU usage. The number of worker processes must be greater than 0 and smaller than 128\.

The same setting exists for [pvedaemon](pvedaemon-8.md#pvedaemon_max_workers).

## Copyright and Disclaimer <a href="#_copyright_and_disclaimer" id="_copyright_and_disclaimer"></a>

版权所有 © 2007-2022 Proxmox Server Solutions GmbH

本程序是自由软件：您可以根据自由软件基金会发布的 GNU Affero General Public License 的条款重新分发和/或修改本程序，许可证版本可以是第 3 版，或（由您选择）任何更高版本。

本程序的分发是希望它能有用，但不提供任何担保；甚至没有适销性或特定用途适用性的默示担保。有关更多详情，请参阅 GNU Affero General Public License。

您应该已随本程序收到一份 GNU Affero General Public License 的副本。如果没有，请参阅 [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/)

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pveproxy.8.html) · 版本 9.2.13 · 非官方中文翻译。
