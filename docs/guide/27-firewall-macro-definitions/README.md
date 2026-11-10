# 27. Appendix F: Firewall Macro Definitions <a href="#_firewall_macro_definitions" id="_firewall_macro_definitions"></a>

<table>
<tr>
<td><em>Amanda</em> <br/></td>
<td>
<p>Amanda Backup</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Auth (identd) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Border Gateway Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>BitTorrent traffic for BitTorrent 3.1 and earlier</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>BitTorrent traffic for BitTorrent 3.2 and later</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Concurrent Versions System pserver traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Ceph Storage Cluster traffic (Ceph Monitors, OSD &amp; MDS Daemons)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Citrix/ICA traffic (ICA, ICA Browser, CGP)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Digital Audio Access Protocol traffic (iTunes, Rythmbox daemons)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Distributed Checksum Clearinghouse spam filtering mechanism</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Forwarded DHCP traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>DHCPv6 traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Domain Name System traffic (upd and tcp)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Distributed Compiler service</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>File Transfer Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Finger protocol (RFC 742)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>GNUnet secure peer-to-peer networking traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Generic Routing Encapsulation tunneling protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Git distributed revision control traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>OpenPGP HTTP key server protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Hypertext Transfer Protocol (WWW)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Hypertext Transfer Protocol (WWW) over SSL</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Internet Cache Protocol V2 (Squid) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>AOL Instant Messenger traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Internet Message Access Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Internet Message Access Protocol over SSL</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>IPIP capsulation traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>IPsec traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>IPsec authentication (AH) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>IPsec traffic and Nat-Traversal</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Internet Relay Chat traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>HP Jetdirect printing</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Layer 2 Tunneling Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Lightweight Directory Access Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Secure Lightweight Directory Access Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Multicast DNS</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Microsoft Notification Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<th>Action</th>
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
<p>Mail traffic (SMTP, SMTPS, Submission)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Munin networked resource monitoring traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>MySQL server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>NNTP traffic (Usenet).</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Encrypted NNTP traffic (Usenet)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Network Time Protocol (ntpd)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>IPv6 neighbor solicitation, neighbor and router advertisement</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>OSPF multicast traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>OpenVPN traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<th>Action</th>
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
<p>Proxmox Mail Gateway web interface</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>POP3 traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Encrypted POP3 traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Point-to-Point Tunneling Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>ICMP echo request</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>PostgreSQL server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Line Printer protocol printing</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Microsoft Remote Desktop Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Routing Information Protocol (bidirectional)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>BIND remote management protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Razor Antispam System</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Remote time retrieval (rdate)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Rsync server</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>SANE network scanning</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Microsoft SMB traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Samba Web Administration Tool</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Simple Mail Transfer Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Encrypted Simple Mail Transfer Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Simple Network Management Protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Spam Assassin SPAMD traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Proxmox VE SPICE display proxy traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Secure shell traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Subversion server (svnserve)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>SixXS IPv6 Deployment and Tunnel Broker</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Squid web proxy traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Mail message submission traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Syslog protocol (RFC 5424) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Trivial File Transfer Protocol traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Telnet traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Telnet over SSL</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>RFC 868 Time protocol</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Traceroute (for up to 30 hops) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>VNC traffic for VNC display’s 0 - 99</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>VNC traffic from Vncservers to Vncviewers in listen mode</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>WWW traffic (HTTP and HTTPS)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Web Cache/Proxy traffic (port 8080)</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Webmin traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
<p>Whois (nicname, RFC 3912) traffic</p>
</td>
</tr>
</table>

<table>




<thead>
<tr>
<th>Action</th>
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
