# 16.3. Backup File Compression <a href="#_backup_file_compression" id="_backup_file_compression"></a>

The backup file can be compressed with one of the following algorithms: `lzo`   
\[Lempel–Ziv–Oberhumer a lossless data compression algorithm [https://en.wikipedia.org/wiki/Lempel-Ziv-Oberhumer](https://en.wikipedia.org/wiki/Lempel-Ziv-Oberhumer)\]  
, `gzip`   
\[gzip \- based on the DEFLATE algorithm [https://en.wikipedia.org/wiki/Gzip](https://en.wikipedia.org/wiki/Gzip)\]  
 or `zstd`   
\[Zstandard a lossless data compression algorithm [https://en.wikipedia.org/wiki/Zstandard](https://en.wikipedia.org/wiki/Zstandard)\]  
.

Currently, Zstandard (zstd) is the fastest of these three algorithms. Multi-threading is another advantage of zstd over lzo and gzip. Lzo and gzip are more widely used and often installed by default.

You can install pigz   
\[pigz \- parallel implementation of gzip [https://zlib.net/pigz/](https://zlib.net/pigz/)\]  
 as a drop-in replacement for gzip to provide better performance due to multi-threading. For pigz \& zstd, the amount of threads/cores can be adjusted. See the [configuration options](10-vzdump-configuration.md#vzdump_configuration) below.

The extension of the backup file name can usually be used to determine which compression algorithm has been used to create the backup.

<table>


<tbody>
<tr>
<td><p>.zst</p></td>
<td><p>Zstandard (zstd) compression</p></td>
</tr>
<tr>
<td><p>.gz or .tgz</p></td>
<td><p>gzip compression</p></td>
</tr>
<tr>
<td><p>.lzo</p></td>
<td><p>lzo compression</p></td>
</tr>
</tbody>
</table>

If the backup file name doesn’t end with one of the above file extensions, then it was not compressed by vzdump.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
