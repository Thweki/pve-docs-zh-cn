# pveperf(1)

## 名称 <a href="#_name" id="_name"></a>

pveperf \- the Proxmox benchmark

## 概要 <a href="#_synopsis" id="_synopsis"></a>

**pveperf** `[PATH]`

## 描述 <a href="#_description" id="_description"></a>

Tries to gather some CPU/hard disk performance data on the hard disk mounted at `PATH` (`/` is used as default):

**CPU BOGOMIPS**

bogomips sum of all CPUs

**REGEX/SECOND**

regular expressions per second (perl performance test), should be above 300000

**HD SIZE**

hard disk size

**BUFFERED READS**

simple HD read test. Modern HDs should reach at least 40 MB/sec

**AVERAGE SEEK TIME**

tests average seek time. Fast SCSI HDs reach values \< 8 milliseconds. Common IDE/SATA disks get values from 15 to 20 ms.

**FSYNCS/SECOND**

value should be greater than 200 (you should enable `write
back` cache mode on you RAID controller \- needs a battery backed cache (BBWC)).

**DNS EXT**

average time to resolve an external DNS name

**DNS INT**

average time to resolve a local DNS name

<a id="footnotes"></a>



---

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pveperf.1.html) · 版本 9.2.13 · 非官方中文翻译。
