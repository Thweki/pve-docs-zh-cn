# 10.12. 资源映射 <a href="#resource_mapping" id="resource_mapping"></a>

[![screenshot/gui-datacenter-resource-mappings.png](../../assets/screenshot-gui-datacenter-resource-mappings-png-da2a9a26150d.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-resource-mappings.png)

使用或引用本地资源（例如 PCI 设备的地址）时，有时直接使用原始地址或 ID 会有问题，例如：

- 使用 HA 时，目标节点上可能存在具有相同 id 或路径的不同设备，如果在将此类客户机分配给 HA 组时不小心，可能会使用错误的设备，从而导致配置出错。
- 更改硬件可能会更改 id 和路径，因此必须检查所有已分配的设备，确认路径或 id 是否仍然正确。

为更好地处理此问题，可以定义集群范围的资源映射，使资源具有集群内唯一、由用户选择的标识符，该标识符可对应不同宿主机上的不同设备。这样，HA 就不会使用错误的设备启动客户机，并且可以检测到硬件更改。

在 Proxmox VE Web GUI 中，可在 `Datacenter` 下 `Resource Mappings` 类别的相关选项卡中创建此类映射，也可以在命令行中使用以下命令创建：

```text
# pvesh create /cluster/mapping/<type> <options>
```

[![screenshot/gui-datacenter-mapping-pci-edit.png](../../assets/screenshot-gui-datacenter-mapping-pci-edit-png-96b3f049d8df.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-mapping-pci-edit.png)

其中，`<type>` 是硬件类型（目前可以是 `pci`、`usb` 或 [dir](02-qm-virtual-machines-settings.md#qm_virtiofs)），`<options>` 是设备映射和其他配置参数。

请注意，选项必须包含一个 map 属性，其中包含该硬件的所有标识属性，以便能够验证硬件未发生更改，并直通正确的设备。

例如，要添加一个 PCI 设备，将其命名为 `device1`，路径为 `0000:01:00.0`，设备 id 为 `0001`，供应商 id 为 `0002`，节点为 `node1`，并将 `0000:02:00.0` 添加到 `node2` 上，可以使用以下命令：

```text
# pvesh create /cluster/mapping/pci --id device1 \
 --map node=node1,path=0000:01:00.0,id=0002:0001 \
 --map node=node2,path=0000:02:00.0,id=0002:0001
```

必须为每个需要该设备映射的节点重复指定 `map` 参数（请注意，目前每个节点上的每个映射只能映射一个 USB 设备）。

使用 GUI 会让此操作容易得多，因为正确的属性会被自动获取并发送到 API。

[![screenshot/gui-datacenter-mapping-usb-edit.png](../../assets/screenshot-gui-datacenter-mapping-usb-edit-png-e01c9f9453d3.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-mapping-usb-edit.png)

对于 PCI 设备，还可以通过为节点指定多个 map 属性，在每个节点上提供多个设备。如果将此类设备分配给客户机，则在客户机启动时会使用第一个空闲设备。给定路径的顺序也是尝试这些设备的顺序，因此可以实现任意的分配策略。

这对于支持 SR-IOV 的设备很有用，因为有时具体直通哪个虚拟功能并不重要。

可以通过 GUI 或使用以下命令将此类设备分配给客户机：

```text
# qm set ID -hostpci0 <name>
```

对于 PCI 设备，使用：

```text
# qm set <vmid> -usb0 <name>
```

对于 USB 设备，使用：

其中，`<vmid>` 是客户机 id，`<name>` 是为所创建映射选择的名称。所有通常用于设备直通的选项均允许使用，例如 `mdev`。

要创建映射，必须具备 `Mapping.Modify` 权限，其作用对象为 `/mapping/<type>/<name>`（其中 `<type>` 是设备类型，`<name>` 是映射名称）。

要使用这些映射，必须具备 `Mapping.Use` 权限，其作用对象为 `/mapping/<type>/<name>`（此外还需具备编辑配置的常规客户机权限）。

**其他选项**

定义集群范围的资源映射时，还有一些其他选项。目前提供以下选项：

- `mdev`（PCI）：将此 PCI 设备标记为能够提供 `mediated devices`。启用后，在客户机上配置该设备时可以选择类型。如果为映射选择了多个 PCI 设备，则会在第一个具有所选类型的可用实例的设备上创建中介设备。
- `live-migration-capable`（PCI）：将此 PCI 设备标记为能够在节点之间进行在线迁移。这需要驱动程序和硬件支持。目前仅已知配备较新内核的 NVIDIA GPU 支持此功能。请注意，在线迁移直通设备是一项实验性功能，可能无法正常工作或引发问题。

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
