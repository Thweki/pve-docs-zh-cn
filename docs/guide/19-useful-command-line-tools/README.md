# 19\. 实用命令行工具 <a href="#useful_command_line_tools" id="useful_command_line_tools"></a>

## 19.1. pvesubscription \- 订阅管理 <a href="#pvesubscription_subscription_management" id="pvesubscription_subscription_management"></a>

此工具用于处理 Proxmox VE 订阅。

## 19.2. pveperf \- Proxmox VE 基准测试脚本 <a href="#pveperf_proxmox_ve_benchmark_script" id="pveperf_proxmox_ve_benchmark_script"></a>

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

## 19.3. Proxmox VE API 的 Shell 接口 <a href="#shell_interface_for_the_proxmox_ve_api" id="shell_interface_for_the_proxmox_ve_api"></a>

Proxmox VE 管理工具（`pvesh`）允许直接调用 API 函数，无需使用 REST/HTTPS 服务器。

{% hint style="info" %}
只有 <em>root</em> 可以这样做。
{% endhint %}

### 19.3.1. 示例 <a href="#examples_13" id="examples_13"></a>

获取我的集群中的节点列表

```text
# pvesh get /nodes
```

获取数据中心的可用选项列表

```text
# pvesh usage cluster/options -v
```

将 HTMl5 NoVNC 控制台设置为数据中心的默认控制台

```text
# pvesh set cluster/options -console html5
```

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
