# 27\. 附录 F：防火墙宏定义 <a href="#firewall_macro_definitions" id="firewall_macro_definitions"></a>

<table>
<tr>
<td><em>Amanda</em> <br/></td>
<td>
<p>Amanda 备份</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>10080</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>10080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Auth</em> <br/></td>
<td>
<p>Auth（identd）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>113</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BGP</em> <br/></td>
<td>
<p>边界网关协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>179</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BitTorrent</em> <br/></td>
<td>
<p>BitTorrent 3.1 及更早版本的 BitTorrent 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6881:6889</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>6881</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>BitTorrent32</em> <br/></td>
<td>
<p>BitTorrent 3.2 及更高版本的 BitTorrent 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6881:6999</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>6881</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>CVS</em> <br/></td>
<td>
<p>并发版本系统 pserver 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2401</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Ceph</em> <br/></td>
<td>
<p>Ceph 存储集群流量（Ceph 监视器、OSD 和 MDS 守护进程）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6789</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3300</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6800:7300</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Citrix</em> <br/></td>
<td>
<p>Citrix/ICA 流量（ICA、ICA Browser、CGP）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1494</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1604</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2598</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DAAP</em> <br/></td>
<td>
<p>数字音频访问协议流量（iTunes、Rythmbox 守护进程）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3689</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3689</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DCC</em> <br/></td>
<td>
<p>分布式校验和交换中心垃圾邮件过滤机制</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6277</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DHCPfwd</em> <br/></td>
<td>
<p>转发的 DHCP 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>67:68</p></td>
<td><p>67:68</p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DHCPv6</em> <br/></td>
<td>
<p>DHCPv6 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>546:547</p></td>
<td><p>546:547</p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>DNS</em> <br/></td>
<td>
<p>域名系统流量（upd 和 tcp）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>53</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>53</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Distcc</em> <br/></td>
<td>
<p>分布式编译器服务</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3632</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>FTP</em> <br/></td>
<td>
<p>文件传输协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>21</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Finger</em> <br/></td>
<td>
<p>Finger 协议（RFC 742）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>79</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>GNUnet</em> <br/></td>
<td>
<p>GNUnet 安全点对点网络流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2086</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>2086</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1080</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>GRE</em> <br/></td>
<td>
<p>通用路由封装隧道协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>47</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Git</em> <br/></td>
<td>
<p>Git 分布式版本控制流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>9418</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HKP</em> <br/></td>
<td>
<p>OpenPGP HTTP 密钥服务器协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>11371</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HTTP</em> <br/></td>
<td>
<p>超文本传输协议（WWW）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>80</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>HTTPS</em> <br/></td>
<td>
<p>通过 SSL 传输的超文本传输协议（WWW）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>443</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>ICPV2</em> <br/></td>
<td>
<p>互联网缓存协议 V2（Squid）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3130</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>ICQ</em> <br/></td>
<td>
<p>AOL Instant Messenger 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5190</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IMAP</em> <br/></td>
<td>
<p>互联网消息访问协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>143</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IMAPS</em> <br/></td>
<td>
<p>通过 SSL 传输的互联网消息访问协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>993</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPIP</em> <br/></td>
<td>
<p>IPIP 封装流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>94</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsec</em> <br/></td>
<td>
<p>IPsec 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p>500</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>50</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsecah</em> <br/></td>
<td>
<p>IPsec 认证（AH）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p>500</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>51</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IPsecnat</em> <br/></td>
<td>
<p>IPsec 流量和 Nat-Traversal</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>500</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>4500</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>50</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>IRC</em> <br/></td>
<td>
<p>互联网中继聊天流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6667</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Jetdirect</em> <br/></td>
<td>
<p>HP Jetdirect 打印</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>9100</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>L2TP</em> <br/></td>
<td>
<p>第 2 层隧道协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1701</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>LDAP</em> <br/></td>
<td>
<p>轻量级目录访问协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>389</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>LDAPS</em> <br/></td>
<td>
<p>安全轻量级目录访问协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>636</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MDNS</em> <br/></td>
<td>
<p>多播 DNS</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5353</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MSNP</em> <br/></td>
<td>
<p>Microsoft 通知协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1863</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MSSQL</em> <br/></td>
<td>
<p>Microsoft SQL Server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1433</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Mail</em> <br/></td>
<td>
<p>邮件流量（SMTP、SMTPS、Submission）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>25</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>465</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>587</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Munin</em> <br/></td>
<td>
<p>Munin 网络资源监控流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>4949</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>MySQL</em> <br/></td>
<td>
<p>MySQL 服务器</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3306</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NNTP</em> <br/></td>
<td>
<p>NNTP 流量（Usenet）。</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>119</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NNTPS</em> <br/></td>
<td>
<p>加密的 NNTP 流量（Usenet）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>563</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NTP</em> <br/></td>
<td>
<p>网络时间协议（ntpd）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>123</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>NeighborDiscovery</em> <br/></td>
<td>
<p>IPv6 邻居请求、邻居通告和路由器通告</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>router-solicitation</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>router-advertisement</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>neighbor-solicitation</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmpv6</p></td>
<td><p>neighbor-advertisement</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>OSPF</em> <br/></td>
<td>
<p>OSPF 多播流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>89</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>OpenVPN</em> <br/></td>
<td>
<p>OpenVPN 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1194</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PCA</em> <br/></td>
<td>
<p>Symantec PCAnywere (tm)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5632</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5631</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PMG</em> <br/></td>
<td>
<p>Proxmox Mail Gateway Web 界面</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>8006</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>POP3</em> <br/></td>
<td>
<p>POP3 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>110</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>POP3S</em> <br/></td>
<td>
<p>加密的 POP3 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>995</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PPtP</em> <br/></td>
<td>
<p>点对点隧道协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>47</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>1723</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Ping</em> <br/></td>
<td>
<p>ICMP 回显请求</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>icmp</p></td>
<td><p>echo-request</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>PostgreSQL</em> <br/></td>
<td>
<p>PostgreSQL 服务器</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5432</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Printer</em> <br/></td>
<td>
<p>行式打印机协议打印</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>515</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RDP</em> <br/></td>
<td>
<p>Microsoft 远程桌面协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3389</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RIP</em> <br/></td>
<td>
<p>路由信息协议（双向）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>520</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>RNDC</em> <br/></td>
<td>
<p>BIND 远程管理协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>953</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Razor</em> <br/></td>
<td>
<p>Razor 反垃圾邮件系统</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>2703</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Rdate</em> <br/></td>
<td>
<p>远程时间获取（rdate）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>37</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Rsync</em> <br/></td>
<td>
<p>Rsync 服务器</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>873</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SANE</em> <br/></td>
<td>
<p>SANE 网络扫描</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>6566</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMB</em> <br/></td>
<td>
<p>Microsoft SMB 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>135,445</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>137:139</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>1024:65535</p></td>
<td><p>137</p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>135,139,445</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMBswat</em> <br/></td>
<td>
<p>Samba Web 管理工具</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>901</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMTP</em> <br/></td>
<td>
<p>简单邮件传输协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>25</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SMTPS</em> <br/></td>
<td>
<p>加密的简单邮件传输协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>465</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SNMP</em> <br/></td>
<td>
<p>简单网络管理协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>161:162</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>161</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SPAMD</em> <br/></td>
<td>
<p>Spam Assassin SPAMD 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>783</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SPICEproxy</em> <br/></td>
<td>
<p>Proxmox VE SPICE 显示代理流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3128</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SSH</em> <br/></td>
<td>
<p>安全 Shell 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>22</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SVN</em> <br/></td>
<td>
<p>Subversion 服务器（svnserve）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3690</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>SixXS</em> <br/></td>
<td>
<p>SixXS IPv6 部署和隧道代理</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3874</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>3740</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>41</p></td>
<td><p></p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>5072,8374</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Squid</em> <br/></td>
<td>
<p>Squid Web 代理流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>3128</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Submission</em> <br/></td>
<td>
<p>邮件消息提交流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>587</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Syslog</em> <br/></td>
<td>
<p>Syslog 协议（RFC 5424）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>514</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>514</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>TFTP</em> <br/></td>
<td>
<p>简单文件传输协议流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>69</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Telnet</em> <br/></td>
<td>
<p>Telnet 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>23</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Telnets</em> <br/></td>
<td>
<p>通过 SSL 传输的 Telnet</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>992</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Time</em> <br/></td>
<td>
<p>RFC 868 时间协议</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>37</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Trcrt</em> <br/></td>
<td>
<p>Traceroute（最多 30 跳）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>udp</p></td>
<td><p>33434:33524</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>icmp</p></td>
<td><p>echo-request</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>VNC</em> <br/></td>
<td>
<p>VNC 显示器 0 - 99 的 VNC 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5900:5999</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>VNCL</em> <br/></td>
<td>
<p>从 Vncservers 到处于监听模式的 Vncviewers 的 VNC 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>5500</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Web</em> <br/></td>
<td>
<p>WWW 流量（HTTP 和 HTTPS）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>80</p></td>
<td><p></p></td>
</tr>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>443</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Webcache</em> <br/></td>
<td>
<p>Web 缓存/代理流量（端口 8080）</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>8080</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Webmin</em> <br/></td>
<td>
<p>Webmin 流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>10000</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

<table>
<tr>
<td><em>Whois</em> <br/></td>
<td>
<p>Whois（nicname，RFC 3912）流量</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>操作</th>
<th>proto</th>
<th>dport</th>
<th>sport</th>
</tr>
</thead>
<tbody>
<tr>
<td><p>PARAM</p></td>
<td><p>tcp</p></td>
<td><p>43</p></td>
<td><p></p></td>
</tr>
</tbody>
</table>

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
