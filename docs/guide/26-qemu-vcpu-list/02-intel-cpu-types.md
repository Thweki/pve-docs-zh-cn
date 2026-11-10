# 26.2. Intel CPU 类型 <a href="#intel_cpu_types" id="intel_cpu_types"></a>

[Intel 处理器](https://en.wikipedia.org/wiki/List_of_Intel_Xeon_processors)

- *Nahelem*：[第 1 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Nehalem_(microarchitecture))
- *Nahelem-IBRS (v2)*：添加 Spectre v1 防护（*\+spec-ctrl*）
- *Westmere*：[第 1 代 Intel Core 处理器（Xeon E7-）](https://en.wikipedia.org/wiki/Westmere_(microarchitecture))
- *Westmere-IBRS (v2)*：添加 Spectre v1 防护（*\+spec-ctrl*）
- *SandyBridge*：[第 2 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Sandy_Bridge)
- *SandyBridge-IBRS (v2)*：添加 Spectre v1 防护（*\+spec-ctrl*）
- *IvyBridge*：[第 3 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Ivy_Bridge_(microarchitecture))
- *IvyBridge-IBRS (v2)*：添加 Spectre v1 防护（*\+spec-ctrl*）
- *Haswell*：[第 4 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Haswell_(microarchitecture))
- *Haswell-noTSX (v2)*：禁用 TSX（*-hle*、*-rtm*）
- *Haswell-IBRS (v3)*：重新添加 TSX，并添加 Spectre v1 防护（*\+hle*、*\+rtm*、*\+spec-ctrl*）
- *Haswell-noTSX-IBRS (v4)*：禁用 TSX（*-hle*、*-rtm*）
- *Broadwell*：[第 5 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture))
- *Skylake*：[第 1 代 Xeon 可扩展服务器处理器](https://en.wikipedia.org/wiki/Skylake_(microarchitecture))
- *Skylake-IBRS (v2)*：添加 Spectre v1 防护，禁用 CLFLUSHOPT（*\+spec-ctrl*、*-clflushopt*）
- *Skylake-noTSX-IBRS (v3)*：禁用 TSX（*-hle*、*-rtm*）
- *Skylake-v4*：添加 EPT 切换（*\+vmx-eptp-switching*）
- *Cascadelake*：[第 2 代 Xeon 可扩展处理器](https://en.wikipedia.org/wiki/Cascade_Lake_(microprocessor))
- *Cascadelake-v2*：添加 arch\_capabilities msr（*\+arch-capabilities*、*\+rdctl-no*、*\+ibrs-all*、*\+skip-l1dfl-vmentry*、*\+mds-no*）
- *Cascadelake-v3*：禁用 TSX（*-hle*、*-rtm*）
- *Cascadelake-v4*：添加 EPT 切换（*\+vmx-eptp-switching*）
- *Cascadelake-v5*：添加 XSAVES（*\+xsaves*、*\+vmx-xsaves*）
- *Cooperlake*：[适用于 4 和 8 插槽服务器的第 3 代 Xeon 可扩展处理器](https://en.wikipedia.org/wiki/Cooper_Lake_(microprocessor))
- *Cooperlake-v2*：添加 XSAVES（*\+xsaves*、*\+vmx-xsaves*）
- *Icelake*：[第 3 代 Xeon 可扩展服务器处理器](https://en.wikipedia.org/wiki/Ice_Lake_(microprocessor))
- *Icelake-v2*：禁用 TSX（*-hle*、*-rtm*）
- *Icelake-v3*：添加 arch\_capabilities msr（*\+arch-capabilities*、*\+rdctl-no*、*\+ibrs-all*、*\+skip-l1dfl-vmentry*、*\+mds-no*、*\+pschange-mc-no*、*\+taa-no*）
- *Icelake-v4*：添加缺少的标志（*\+sha-ni*、*\+avx512ifma*、*\+rdpid*、*\+fsrm*、*\+vmx-rdseed-exit*、*\+vmx-pml*、*\+vmx-eptp-switching*）
- *Icelake-v5*：添加 XSAVES（*\+xsaves*、*\+vmx-xsaves*）
- *Icelake-v6*：添加“5 级 EPT”（*\+vmx-page-walk-5*）
- *SapphireRapids*：[第 4 代 Xeon 可扩展服务器处理器](https://en.wikipedia.org/wiki/Sapphire_Rapids)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
