# 16.3. 备份文件压缩 <a href="#backup_file_compression" id="backup_file_compression"></a>

备份文件可以使用以下算法之一压缩：`lzo` [\[1\]](#note-18fb615f-1)、`gzip` [\[2\]](#note-18fb615f-2) 或 `zstd` [\[3\]](#note-18fb615f-3)。

目前，Zstandard（zstd）是这三种算法中最快的。多线程是 zstd 相对于 lzo 和 gzip 的另一个优势。Lzo 和 gzip 使用更广泛，并且通常默认安装。

可以安装 pigz [\[4\]](#note-18fb615f-4)，作为 gzip 的直接替代，通过多线程提供更好的性能。对于 pigz 和 zstd，可以调整线程/核心数量。参见下文 [配置选项](10-vzdump-configuration.md)。

通常可以通过备份文件名的扩展名确定创建备份时使用了哪种压缩算法。

<table>


<tbody>
<tr>
<td><p>.zst</p></td>
<td><p>Zstandard（zstd）压缩</p></td>
</tr>
<tr>
<td><p>.gz 或 .tgz</p></td>
<td><p>gzip 压缩</p></td>
</tr>
<tr>
<td><p>.lzo</p></td>
<td><p>lzo 压缩</p></td>
</tr>
</tbody>
</table>

如果备份文件名不是以上任何文件扩展名结尾，则未由 vzdump 压缩。

## 注释

### 注释 1 <a href="#note-18fb615f-1" id="note-18fb615f-1"></a>

Lempel–Ziv–Oberhumer，无损数据压缩算法 [https://en.wikipedia.org/wiki/Lempel-Ziv-Oberhumer](https://en.wikipedia.org/wiki/Lempel-Ziv-Oberhumer)

### 注释 2 <a href="#note-18fb615f-2" id="note-18fb615f-2"></a>

gzip \- 基于 DEFLATE 算法 [https://en.wikipedia.org/wiki/Gzip](https://en.wikipedia.org/wiki/Gzip)

### 注释 3 <a href="#note-18fb615f-3" id="note-18fb615f-3"></a>

Zstandard，无损数据压缩算法 [https://en.wikipedia.org/wiki/Zstandard](https://en.wikipedia.org/wiki/Zstandard)

### 注释 4 <a href="#note-18fb615f-4" id="note-18fb615f-4"></a>

pigz \- gzip 的并行实现 [https://zlib.net/pigz/](https://zlib.net/pigz/)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
