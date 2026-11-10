# 12.17. 说明 <a href="#pvesdn_notes" id="pvesdn_notes"></a>

## 12.17.1. 多个 EVPN 出口节点 <a href="#multiple_evpn_exit_nodes" id="multiple_evpn_exit_nodes"></a>

如果有多个网关节点，应禁用 `rp_filter`（严格反向路径过滤器）选项，因为数据包可能从一个节点进入，却从另一个节点发出。

创建 sysctl 配置片段文件 `/etc/sysctl.d/99-rp-filter.conf`：

```text
net.ipv4.conf.default.rp_filter=0
net.ipv4.conf.all.rp_filter=0
```

## 12.17.2. VXLAN IPSEC 加密 <a href="#vxlan_ipsec_encryption" id="vxlan_ipsec_encryption"></a>

要在 VXLAN 之上添加 IPSEC 加密，本示例演示如何使用 `strongswan`。

需要将 *MTU* 额外减小 60 字节（IPv4）或 80 字节（IPv6），以处理加密。

因此，当实际默认 MTU 为 1500 时，需要使用 MTU 1370（1370 \+ 80（IPSEC）\+ 50（VXLAN）\=\= 1500）。

在宿主机上安装 strongswan。

```text
apt install strongswan
```

向 `/etc/ipsec.conf` 添加配置。只需加密来自 VXLAN UDP 端口 *4789* 的流量。

```text
conn %default
    ike=aes256-sha1-modp1024!  # the fastest, but reasonably secure cipher on modern HW
    esp=aes256-sha1!
    leftfirewall=yes           # this is necessary when using Proxmox VE firewall rules

conn output
    rightsubnet=%dynamic[udp/4789]
    right=%any
    type=transport
    authby=psk
    auto=route

conn input
    leftsubnet=%dynamic[udp/4789]
    type=transport
    authby=psk
    auto=route
```

使用以下命令生成预共享密钥：

```text
openssl rand -base64 128
```

并将密钥添加到 `/etc/ipsec.secrets`，使文件内容如下所示：

```text
: PSK <generatedbase64key>
```

将 PSK 和配置复制到参与 VXLAN 网络的所有节点。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
