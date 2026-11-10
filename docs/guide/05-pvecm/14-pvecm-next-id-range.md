# 5.14. 客户机 VMID 自动选择 <a href="#pvecm_next_id_range" id="pvecm_next_id_range"></a>

创建新客户机时，Web 界面会自动向后端请求一个空闲的 VMID。默认搜索范围为 `100` 到 `1000000`（低于由模式定义强制规定的最大允许 VMID）。

有时，管理员希望在一个单独的范围内分配新的 VMID，例如，以便轻松地将临时 VM 与手动选择 VMID 的 VM 区分开来。有时，只是希望提供长度固定的 VMID；例如，将下限设置为 `100000` 就能为此提供更大的空间。

为适应这种用例，可以通过 `datacenter.cfg` 配置文件设置下限、上限或同时设置两者；该文件可在 Web 界面的 *数据中心* → *选项* 下编辑。

{% hint style="info" %}
该范围仅用于 next-id API 调用，因此它不是硬性限制。
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
