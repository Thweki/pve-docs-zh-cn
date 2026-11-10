# `/nodes/{node}/lxc/{vmid}/resize`

原始接口路径：`/nodes/{node}/lxc/{vmid}/resize`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## PUT `/nodes/{node}/lxc/{vmid}/resize`

调整容器挂载点的大小。

**权限**

```json
{
  "check": [
    "perm",
    "/vms/{vmid}",
    [
      "VM.Config.Disk"
    ],
    "any",
    1
  ]
}
```

**允许 API 令牌**

```json
1
```

**受保护接口**

```json
1
```

**代理目标**

```json
"node"
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `digest` | string | 否 | — | Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications. |
| `disk` | string | 是 | — | The disk you want to resize.；可选值：`rootfs`, `mp0`, `mp1`, `mp2`, `mp3`, `mp4`, `mp5`, `mp6`, `mp7`, `mp8`, `mp9`, `mp10`, `mp11`, `mp12`, `mp13`, `mp14`, `mp15`, `mp16`, `mp17`, `mp18`, `mp19`, `mp20`, `mp21`, `mp22`, `mp23`, `mp24`, `mp25`, `mp26`, `mp27`, `mp28`, `mp29`, `mp30`, `mp31`, `mp32`, `mp33`, `mp34`, `mp35`, `mp36`, `mp37`, `mp38`, `mp39`, `mp40`, `mp41`, `mp42`, `mp43`, `mp44`, `mp45`, `mp46`, `mp47`, `mp48`, `mp49`, `mp50`, `mp51`, `mp52`, `mp53`, `mp54`, `mp55`, `mp56`, `mp57`, `mp58`, `mp59`, `mp60`, `mp61`, `mp62`, `mp63`, `mp64`, `mp65`, `mp66`, `mp67`, `mp68`, `mp69`, `mp70`, `mp71`, `mp72`, `mp73`, `mp74`, `mp75`, `mp76`, `mp77`, `mp78`, `mp79`, `mp80`, `mp81`, `mp82`, `mp83`, `mp84`, `mp85`, `mp86`, `mp87`, `mp88`, `mp89`, `mp90`, `mp91`, `mp92`, `mp93`, `mp94`, `mp95`, `mp96`, `mp97`, `mp98`, `mp99`, `mp100`, `mp101`, `mp102`, `mp103`, `mp104`, `mp105`, `mp106`, `mp107`, `mp108`, `mp109`, `mp110`, `mp111`, `mp112`, `mp113`, `mp114`, `mp115`, `mp116`, `mp117`, `mp118`, `mp119`, `mp120`, `mp121`, `mp122`, `mp123`, `mp124`, `mp125`, `mp126`, `mp127`, `mp128`, `mp129`, `mp130`, `mp131`, `mp132`, `mp133`, `mp134`, `mp135`, `mp136`, `mp137`, `mp138`, `mp139`, `mp140`, `mp141`, `mp142`, `mp143`, `mp144`, `mp145`, `mp146`, `mp147`, `mp148`, `mp149`, `mp150`, `mp151`, `mp152`, `mp153`, `mp154`, `mp155`, `mp156`, `mp157`, `mp158`, `mp159`, `mp160`, `mp161`, `mp162`, `mp163`, `mp164`, `mp165`, `mp166`, `mp167`, `mp168`, `mp169`, `mp170`, `mp171`, `mp172`, `mp173`, `mp174`, `mp175`, `mp176`, `mp177`, `mp178`, `mp179`, `mp180`, `mp181`, `mp182`, `mp183`, `mp184`, `mp185`, `mp186`, `mp187`, `mp188`, `mp189`, `mp190`, `mp191`, `mp192`, `mp193`, `mp194`, `mp195`, `mp196`, `mp197`, `mp198`, `mp199`, `mp200`, `mp201`, `mp202`, `mp203`, `mp204`, `mp205`, `mp206`, `mp207`, `mp208`, `mp209`, `mp210`, `mp211`, `mp212`, `mp213`, `mp214`, `mp215`, `mp216`, `mp217`, `mp218`, `mp219`, `mp220`, `mp221`, `mp222`, `mp223`, `mp224`, `mp225`, `mp226`, `mp227`, `mp228`, `mp229`, `mp230`, `mp231`, `mp232`, `mp233`, `mp234`, `mp235`, `mp236`, `mp237`, `mp238`, `mp239`, `mp240`, `mp241`, `mp242`, `mp243`, `mp244`, `mp245`, `mp246`, `mp247`, `mp248`, `mp249`, `mp250`, `mp251`, `mp252`, `mp253`, `mp254`, `mp255` |
| `node` | string | 是 | — | The cluster node name. |
| `size` | string | 是 | — | The new size. With the '+' sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported. |
| `vmid` | integer | 是 | — | The (unique) ID of the VM. |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "digest": {
      "description": "Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications.",
      "maxLength": 40,
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "disk": {
      "description": "The disk you want to resize.",
      "enum": [
        "rootfs",
        "mp0",
        "mp1",
        "mp2",
        "mp3",
        "mp4",
        "mp5",
        "mp6",
        "mp7",
        "mp8",
        "mp9",
        "mp10",
        "mp11",
        "mp12",
        "mp13",
        "mp14",
        "mp15",
        "mp16",
        "mp17",
        "mp18",
        "mp19",
        "mp20",
        "mp21",
        "mp22",
        "mp23",
        "mp24",
        "mp25",
        "mp26",
        "mp27",
        "mp28",
        "mp29",
        "mp30",
        "mp31",
        "mp32",
        "mp33",
        "mp34",
        "mp35",
        "mp36",
        "mp37",
        "mp38",
        "mp39",
        "mp40",
        "mp41",
        "mp42",
        "mp43",
        "mp44",
        "mp45",
        "mp46",
        "mp47",
        "mp48",
        "mp49",
        "mp50",
        "mp51",
        "mp52",
        "mp53",
        "mp54",
        "mp55",
        "mp56",
        "mp57",
        "mp58",
        "mp59",
        "mp60",
        "mp61",
        "mp62",
        "mp63",
        "mp64",
        "mp65",
        "mp66",
        "mp67",
        "mp68",
        "mp69",
        "mp70",
        "mp71",
        "mp72",
        "mp73",
        "mp74",
        "mp75",
        "mp76",
        "mp77",
        "mp78",
        "mp79",
        "mp80",
        "mp81",
        "mp82",
        "mp83",
        "mp84",
        "mp85",
        "mp86",
        "mp87",
        "mp88",
        "mp89",
        "mp90",
        "mp91",
        "mp92",
        "mp93",
        "mp94",
        "mp95",
        "mp96",
        "mp97",
        "mp98",
        "mp99",
        "mp100",
        "mp101",
        "mp102",
        "mp103",
        "mp104",
        "mp105",
        "mp106",
        "mp107",
        "mp108",
        "mp109",
        "mp110",
        "mp111",
        "mp112",
        "mp113",
        "mp114",
        "mp115",
        "mp116",
        "mp117",
        "mp118",
        "mp119",
        "mp120",
        "mp121",
        "mp122",
        "mp123",
        "mp124",
        "mp125",
        "mp126",
        "mp127",
        "mp128",
        "mp129",
        "mp130",
        "mp131",
        "mp132",
        "mp133",
        "mp134",
        "mp135",
        "mp136",
        "mp137",
        "mp138",
        "mp139",
        "mp140",
        "mp141",
        "mp142",
        "mp143",
        "mp144",
        "mp145",
        "mp146",
        "mp147",
        "mp148",
        "mp149",
        "mp150",
        "mp151",
        "mp152",
        "mp153",
        "mp154",
        "mp155",
        "mp156",
        "mp157",
        "mp158",
        "mp159",
        "mp160",
        "mp161",
        "mp162",
        "mp163",
        "mp164",
        "mp165",
        "mp166",
        "mp167",
        "mp168",
        "mp169",
        "mp170",
        "mp171",
        "mp172",
        "mp173",
        "mp174",
        "mp175",
        "mp176",
        "mp177",
        "mp178",
        "mp179",
        "mp180",
        "mp181",
        "mp182",
        "mp183",
        "mp184",
        "mp185",
        "mp186",
        "mp187",
        "mp188",
        "mp189",
        "mp190",
        "mp191",
        "mp192",
        "mp193",
        "mp194",
        "mp195",
        "mp196",
        "mp197",
        "mp198",
        "mp199",
        "mp200",
        "mp201",
        "mp202",
        "mp203",
        "mp204",
        "mp205",
        "mp206",
        "mp207",
        "mp208",
        "mp209",
        "mp210",
        "mp211",
        "mp212",
        "mp213",
        "mp214",
        "mp215",
        "mp216",
        "mp217",
        "mp218",
        "mp219",
        "mp220",
        "mp221",
        "mp222",
        "mp223",
        "mp224",
        "mp225",
        "mp226",
        "mp227",
        "mp228",
        "mp229",
        "mp230",
        "mp231",
        "mp232",
        "mp233",
        "mp234",
        "mp235",
        "mp236",
        "mp237",
        "mp238",
        "mp239",
        "mp240",
        "mp241",
        "mp242",
        "mp243",
        "mp244",
        "mp245",
        "mp246",
        "mp247",
        "mp248",
        "mp249",
        "mp250",
        "mp251",
        "mp252",
        "mp253",
        "mp254",
        "mp255"
      ],
      "type": "string"
    },
    "node": {
      "description": "The cluster node name.",
      "format": "pve-node",
      "type": "string",
      "typetext": "<string>"
    },
    "size": {
      "description": "The new size. With the '+' sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported.",
      "pattern": "\\+?\\d+(\\.\\d+)?[KMGT]?",
      "type": "string"
    },
    "vmid": {
      "description": "The (unique) ID of the VM.",
      "format": "pve-vmid",
      "maximum": 999999999,
      "minimum": 100,
      "type": "integer",
      "typetext": "<integer> (100 - 999999999)"
    }
  }
}
```

</details>

### 返回值

```json
{
  "description": "the task ID.",
  "type": "string"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/nodes/{node}/lxc/{vmid}/resize)。
