# 3.6. 外部指标服务器 <a href="#external_metric_server" id="external_metric_server"></a>

[![screenshot/gui-datacenter-metric-server-list.png](../../assets/screenshot-gui-datacenter-metric-server-list-png-29de6badd9c9.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-metric-server-list.png)

在 Proxmox VE 中，您可以定义外部指标服务器，这些服务器将定期接收有关宿主机、虚拟客户机和存储的各种统计信息。

目前支持：

- Graphite（参见 [https://graphiteapp.org](https://graphiteapp.org)）
- InfluxDB（参见 [https://www.influxdata.com/time-series-platform/influxdb/](https://www.influxdata.com/time-series-platform/influxdb/)）
- OpenTelemetry（参见 [https://opentelemetry.io/](https://opentelemetry.io/)）

外部指标服务器定义保存在 */etc/pve/status.cfg* 中，并可通过 Web 界面编辑。

## 3.6.1. Graphite 服务器配置 <a href="#metric_server_graphite" id="metric_server_graphite"></a>

[![screenshot/gui-datacenter-metric-server-graphite.png](../../assets/screenshot-gui-datacenter-metric-server-graphite-png-e9da46d8b1be.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-metric-server-graphite.png)

默认端口设置为 **2003**，默认 Graphite 路径为 **proxmox**。

默认情况下，Proxmox VE 通过 UDP 发送数据，因此必须将 Graphite 服务器配置为接受此方式的数据传输。对于不使用标准 **1500** MTU 的环境，可以在此处配置最大传输单元（MTU）。

您还可以将插件配置为使用 TCP。为避免阻塞重要的 `pvestatd` 统计信息收集守护进程，需要设置超时时间，以应对网络问题。

## 3.6.2. InfluxDB 插件配置 <a href="#metric_server_influxdb" id="metric_server_influxdb"></a>

[![screenshot/gui-datacenter-metric-server-influxdb.png](../../assets/screenshot-gui-datacenter-metric-server-influxdb-png-a15fa331c7ff.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-metric-server-influxdb.png)

Proxmox VE 通过 UDP 发送数据，因此必须对 InfluxDB 服务器进行相应配置。如有必要，也可以在此处配置 MTU。

以下是 InfluxDB 的示例配置（在您的 InfluxDB 服务器上）：

```text
[[udp]]
   enabled = true
   bind-address = "0.0.0.0:8089"
   database = "proxmox"
   batch-size = 1000
   batch-timeout = "1s"
```

使用此配置，您的服务器会监听所有 IP 地址的 8089 端口，并将数据写入 **proxmox** 数据库

或者，可以将插件配置为使用 InfluxDB 2.x 的 http(s) API。InfluxDB 1.8.x 中包含了用于此 v2 API 的向前兼容 API 端点。

要使用该 API，请将 *influxdbproto* 设置为 *http* 或 *https*（取决于您的配置）。默认情况下，Proxmox VE 使用组织 *proxmox* 和存储桶/数据库 *proxmox*（可分别通过配置 *organization* 和 *bucket* 进行设置）。

由于 InfluxDB 的 v2 API 只有在身份验证下才可用，因此您必须生成一个可写入正确存储桶的令牌并进行设置。

在 1.8.x 的 v2 兼容 API 中，您可以使用 *user:password* 作为令牌（如果需要），并且可以省略 *organization*，因为该设置在 InfluxDB 1.x 中没有意义。

您还可以通过 *timeout* 设置 HTTP 超时时间（默认为 1s），并通过 *max-body-size* 设置最大批处理大小（默认为 25000000 bytes）（此设置对应 InfluxDB 中的同名设置）。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
