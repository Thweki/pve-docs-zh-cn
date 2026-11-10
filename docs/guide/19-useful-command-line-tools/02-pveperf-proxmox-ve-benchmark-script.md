# 19.2. pveperf \- Proxmox VE 基准测试脚本 <a href="#pveperf_proxmox_ve_benchmark_script" id="pveperf_proxmox_ve_benchmark_script"></a>

尝试在挂载到 `PATH` 的硬盘上收集一些 CPU/硬盘性能数据（默认使用 `/`）：

**CPU BOGOMIPS**

所有 CPU 的 bogomips 总和

**REGEX/SECOND**

每秒正则表达式数（perl 性能测试），应高于 300000

**HD SIZE**

硬盘大小

**BUFFERED READS**

简单的硬盘读取测试。现代硬盘应至少达到 40 MB/sec

**AVERAGE SEEK TIME**

测试平均寻道时间。高速 SCSI 硬盘可达到 \< 8 毫秒。普通 IDE/SATA 磁盘的值为 15 到 20 ms。

**FSYNCS/SECOND**

此值应大于 200（应在 RAID 控制器上启用 `write
back` 缓存模式，需要具有电池保护的缓存（BBWC））。

**DNS EXT**

解析外部 DNS 名称的平均时间

**DNS INT**

解析本地 DNS 名称的平均时间

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
