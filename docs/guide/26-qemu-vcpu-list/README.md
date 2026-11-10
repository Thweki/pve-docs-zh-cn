# 26\. 附录 E：QEMU vCPU 列表 <a href="#qemu_vcpu_list" id="qemu_vcpu_list"></a>

## 26.1. 引言 <a href="#chapter_qm_vcpu_list" id="chapter_qm_vcpu_list"></a>

这是 QEMU 中定义的 AMD 和 Intel x86-64/amd64 CPU 类型列表，可追溯到 2007 年。

## 26.2. Intel CPU 类型 <a href="#intel_cpu_types" id="intel_cpu_types"></a>

[Intel 处理器](https://en.wikipedia.org/wiki/List_of_Intel_Xeon_processors)

- <em>Nahelem</em>：[第 1 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Nehalem_(microarchitecture))
- <em>Nahelem-IBRS (v2)</em>：添加 Spectre v1 防护（<em>\+spec-ctrl</em>）
- <em>Westmere</em>：[第 1 代 Intel Core 处理器（Xeon E7-）](https://en.wikipedia.org/wiki/Westmere_(microarchitecture))
- <em>Westmere-IBRS (v2)</em>：添加 Spectre v1 防护（<em>\+spec-ctrl</em>）
- <em>SandyBridge</em>：[第 2 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Sandy_Bridge)
- <em>SandyBridge-IBRS (v2)</em>：添加 Spectre v1 防护（<em>\+spec-ctrl</em>）
- <em>IvyBridge</em>：[第 3 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Ivy_Bridge_(microarchitecture))
- <em>IvyBridge-IBRS (v2)</em>：添加 Spectre v1 防护（<em>\+spec-ctrl</em>）
- <em>Haswell</em>：[第 4 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Haswell_(microarchitecture))
- <em>Haswell-noTSX (v2)</em>：禁用 TSX（<em>-hle</em>、<em>-rtm</em>）
- <em>Haswell-IBRS (v3)</em>：重新添加 TSX，并添加 Spectre v1 防护（<em>\+hle</em>、<em>\+rtm</em>、<em>\+spec-ctrl</em>）
- <em>Haswell-noTSX-IBRS (v4)</em>：禁用 TSX（<em>-hle</em>、<em>-rtm</em>）
- <em>Broadwell</em>：[第 5 代 Intel Core 处理器](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture))
- <em>Skylake</em>：[第 1 代 Xeon 可扩展服务器处理器](https://en.wikipedia.org/wiki/Skylake_(microarchitecture))
- <em>Skylake-IBRS (v2)</em>：添加 Spectre v1 防护，禁用 CLFLUSHOPT（<em>\+spec-ctrl</em>、<em>-clflushopt</em>）
- <em>Skylake-noTSX-IBRS (v3)</em>：禁用 TSX（<em>-hle</em>、<em>-rtm</em>）
- <em>Skylake-v4</em>：添加 EPT 切换（<em>\+vmx-eptp-switching</em>）
- <em>Cascadelake</em>：[第 2 代 Xeon 可扩展处理器](https://en.wikipedia.org/wiki/Cascade_Lake_(microprocessor))
- <em>Cascadelake-v2</em>：添加 arch\_capabilities msr（<em>\+arch-capabilities</em>、<em>\+rdctl-no</em>、<em>\+ibrs-all</em>、<em>\+skip-l1dfl-vmentry</em>、<em>\+mds-no</em>）
- <em>Cascadelake-v3</em>：禁用 TSX（<em>-hle</em>、<em>-rtm</em>）
- <em>Cascadelake-v4</em>：添加 EPT 切换（<em>\+vmx-eptp-switching</em>）
- <em>Cascadelake-v5</em>：添加 XSAVES（<em>\+xsaves</em>、<em>\+vmx-xsaves</em>）
- <em>Cooperlake</em>：[适用于 4 和 8 插槽服务器的第 3 代 Xeon 可扩展处理器](https://en.wikipedia.org/wiki/Cooper_Lake_(microprocessor))
- <em>Cooperlake-v2</em>：添加 XSAVES（<em>\+xsaves</em>、<em>\+vmx-xsaves</em>）
- <em>Icelake</em>：[第 3 代 Xeon 可扩展服务器处理器](https://en.wikipedia.org/wiki/Ice_Lake_(microprocessor))
- <em>Icelake-v2</em>：禁用 TSX（<em>-hle</em>、<em>-rtm</em>）
- <em>Icelake-v3</em>：添加 arch\_capabilities msr（<em>\+arch-capabilities</em>、<em>\+rdctl-no</em>、<em>\+ibrs-all</em>、<em>\+skip-l1dfl-vmentry</em>、<em>\+mds-no</em>、<em>\+pschange-mc-no</em>、<em>\+taa-no</em>）
- <em>Icelake-v4</em>：添加缺少的标志（<em>\+sha-ni</em>、<em>\+avx512ifma</em>、<em>\+rdpid</em>、<em>\+fsrm</em>、<em>\+vmx-rdseed-exit</em>、<em>\+vmx-pml</em>、<em>\+vmx-eptp-switching</em>）
- <em>Icelake-v5</em>：添加 XSAVES（<em>\+xsaves</em>、<em>\+vmx-xsaves</em>）
- <em>Icelake-v6</em>：添加“5 级 EPT”（<em>\+vmx-page-walk-5</em>）
- <em>SapphireRapids</em>：[第 4 代 Xeon 可扩展服务器处理器](https://en.wikipedia.org/wiki/Sapphire_Rapids)

## 26.3. AMD CPU 类型 <a href="#amd_cpu_types" id="amd_cpu_types"></a>

[AMD 处理器](https://en.wikipedia.org/wiki/List_of_AMD_processors)

- <em>Opteron\_G3</em> : [K10](https://en.wikipedia.org/wiki/AMD_10h)
- <em>Opteron\_G4</em>：[Bulldozer](https://en.wikipedia.org/wiki/Bulldozer_(microarchitecture))
- <em>Opteron\_G5</em>：[Piledriver](https://en.wikipedia.org/wiki/Piledriver_(microarchitecture))
- <em>EPYC</em>：[第 1 代 Zen 处理器](https://en.wikipedia.org/wiki/Zen_(first_generation))
- <em>EPYC-IBPB (v2)</em>：添加 Spectre v1 防护（<em>\+ibpb</em>）
- <em>EPYC-v3</em>：添加缺少的标志（<em>\+perfctr-core</em>、<em>\+clzero</em>、<em>\+xsaveerptr</em>、<em>\+xsaves</em>）
- <em>EPYC-Rome</em>：[第 2 代 Zen 处理器](https://en.wikipedia.org/wiki/Zen_2)
- <em>EPYC-Rome-v2</em>：添加 Spectre v2、v4 防护（<em>\+ibrs</em>、<em>\+amd-ssbd</em>）
- <em>EPYC-Milan</em>：[第 3 代 Zen 处理器](https://en.wikipedia.org/wiki/Zen_3)
- <em>EPYC-Milan-v2</em>：添加缺少的标志（<em>\+vaes</em>、<em>\+vpclmulqdq</em>、<em>\+stibp-always-on</em>、<em>\+amd-psfd</em>、<em>\+no-nested-data-bp</em>、<em>\+lfence-always-serializing</em>、<em>\+null-sel-clr-base</em>）

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
