# 26.2. Intel CPU Types <a href="#_intel_cpu_types" id="_intel_cpu_types"></a>

[Intel processors](https://en.wikipedia.org/wiki/List_of_Intel_Xeon_processors)

- *Nahelem* : [1st generation of the Intel Core processor](https://en.wikipedia.org/wiki/Nehalem_(microarchitecture))
- *Nahelem-IBRS (v2)* : add Spectre v1 protection (*+spec-ctrl*)
- *Westmere* : [1st generation of the Intel Core processor (Xeon E7-)](https://en.wikipedia.org/wiki/Westmere_(microarchitecture))
- *Westmere-IBRS (v2)* : add Spectre v1 protection (*+spec-ctrl*)
- *SandyBridge* : [2nd generation of the Intel Core processor](https://en.wikipedia.org/wiki/Sandy_Bridge)
- *SandyBridge-IBRS (v2)* : add Spectre v1 protection (*+spec-ctrl*)
- *IvyBridge* : [3rd generation of the Intel Core processor](https://en.wikipedia.org/wiki/Ivy_Bridge_(microarchitecture))
- *IvyBridge-IBRS (v2)*: add Spectre v1 protection (*+spec-ctrl*)
- *Haswell* : [4th generation of the Intel Core processor](https://en.wikipedia.org/wiki/Haswell_(microarchitecture))
- *Haswell-noTSX (v2)* : disable TSX (*-hle*, *-rtm*)
- *Haswell-IBRS (v3)* : re-add TSX, add Spectre v1 protection (*+hle*, *+rtm*, *+spec-ctrl*)
- *Haswell-noTSX-IBRS (v4)* : disable TSX (*-hle*, *-rtm*)
- *Broadwell*: [5th generation of the Intel Core processor](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture))
- *Skylake*: [1st generation Xeon Scalable server processors](https://en.wikipedia.org/wiki/Skylake_(microarchitecture))
- *Skylake-IBRS (v2)* : add Spectre v1 protection, disable CLFLUSHOPT (*+spec-ctrl*, *-clflushopt*)
- *Skylake-noTSX-IBRS (v3)* : disable TSX (*-hle*, *-rtm*)
- *Skylake-v4*: add EPT switching (*+vmx-eptp-switching*)
- *Cascadelake*: [2nd generation Xeon Scalable processor](https://en.wikipedia.org/wiki/Cascade_Lake_(microprocessor))
- *Cascadelake-v2* : add arch_capabilities msr (*+arch-capabilities*, *+rdctl-no*, *+ibrs-all*, *+skip-l1dfl-vmentry*, *+mds-no*)
- *Cascadelake-v3* : disable TSX (*-hle*, *-rtm*)
- *Cascadelake-v4* : add EPT switching (*+vmx-eptp-switching*)
- *Cascadelake-v5* : add XSAVES (*+xsaves*, *+vmx-xsaves*)
- *Cooperlake* : [3rd generation Xeon Scalable processors for 4 & 8 sockets servers](https://en.wikipedia.org/wiki/Cooper_Lake_(microprocessor))
- *Cooperlake-v2* : add XSAVES (*+xsaves*, *+vmx-xsaves*)
- *Icelake*: [3rd generation Xeon Scalable server processors](https://en.wikipedia.org/wiki/Ice_Lake_(microprocessor))
- *Icelake-v2* : disable TSX (*-hle*, *-rtm*)
- *Icelake-v3* : add arch_capabilities msr (*+arch-capabilities*, *+rdctl-no*, *+ibrs-all*, *+skip-l1dfl-vmentry*, *+mds-no*, *+pschange-mc-no*, *+taa-no*)
- *Icelake-v4* : add missing flags (*+sha-ni*, *+avx512ifma*, *+rdpid*, *+fsrm*, *+vmx-rdseed-exit*, *+vmx-pml*, *+vmx-eptp-switching*)
- *Icelake-v5* : add XSAVES (*+xsaves*, *+vmx-xsaves*)
- *Icelake-v6* : add "5-level EPT" (*+vmx-page-walk-5*)
- *SapphireRapids* : [4th generation Xeon Scalable server processors](https://en.wikipedia.org/wiki/Sapphire_Rapids)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
