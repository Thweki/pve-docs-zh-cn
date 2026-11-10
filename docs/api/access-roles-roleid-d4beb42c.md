# `/access/roles/{roleid}`

原始接口路径：`/access/roles/{roleid}`。

方法、参数名、类型、默认值和枚举值与官方规范一致。

## DELETE `/access/roles/{roleid}`

Delete role.

**方法标识：** `delete_role`

**权限**

```json
{
  "check": [
    "perm",
    "/access",
    [
      "Sys.Modify"
    ]
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `roleid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "roleid": {
      "format": "pve-roleid",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

## GET `/access/roles/{roleid}`

Get role configuration.

**方法标识：** `read_role`

**权限**

```json
{
  "user": "all"
}
```

**允许 API 令牌**

```json
1
```

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `roleid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "roleid": {
      "format": "pve-roleid",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "additionalProperties": 0,
  "properties": {
    "Datastore.Allocate": {
      "optional": 1,
      "type": "boolean"
    },
    "Datastore.AllocateSpace": {
      "optional": 1,
      "type": "boolean"
    },
    "Datastore.AllocateTemplate": {
      "optional": 1,
      "type": "boolean"
    },
    "Datastore.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "Group.Allocate": {
      "optional": 1,
      "type": "boolean"
    },
    "Mapping.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "Mapping.Modify": {
      "optional": 1,
      "type": "boolean"
    },
    "Mapping.Use": {
      "optional": 1,
      "type": "boolean"
    },
    "Permissions.Modify": {
      "optional": 1,
      "type": "boolean"
    },
    "Pool.Allocate": {
      "optional": 1,
      "type": "boolean"
    },
    "Pool.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "Realm.Allocate": {
      "optional": 1,
      "type": "boolean"
    },
    "Realm.AllocateUser": {
      "optional": 1,
      "type": "boolean"
    },
    "SDN.Allocate": {
      "optional": 1,
      "type": "boolean"
    },
    "SDN.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "SDN.Use": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.AccessNetwork": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.Console": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.Incoming": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.Modify": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.PowerMgmt": {
      "optional": 1,
      "type": "boolean"
    },
    "Sys.Syslog": {
      "optional": 1,
      "type": "boolean"
    },
    "User.Modify": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Allocate": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Backup": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Clone": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.CDROM": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.CPU": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.Cloudinit": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.Disk": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.HWType": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.Memory": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.Network": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Config.Options": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Console": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.GuestAgent.Audit": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.GuestAgent.FileRead": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.GuestAgent.FileSystemMgmt": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.GuestAgent.FileWrite": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.GuestAgent.Unrestricted": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Migrate": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.PowerMgmt": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Replicate": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Snapshot": {
      "optional": 1,
      "type": "boolean"
    },
    "VM.Snapshot.Rollback": {
      "optional": 1,
      "type": "boolean"
    }
  },
  "type": "object"
}
```

## PUT `/access/roles/{roleid}`

Update an existing role.

**方法标识：** `update_role`

**权限**

```json
{
  "check": [
    "perm",
    "/access",
    [
      "Sys.Modify"
    ]
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

### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
| --- | --- | --- | --- | --- |
| `append` | boolean | 否 | — |  |
| `privs` | string | 否 | — |  |
| `roleid` | string | 是 | — |  |

<details>
<summary>完整请求参数结构</summary>

```json
{
  "additionalProperties": 0,
  "properties": {
    "append": {
      "optional": 1,
      "requires": "privs",
      "type": "boolean",
      "typetext": "<boolean>"
    },
    "privs": {
      "format": "pve-priv-list",
      "optional": 1,
      "type": "string",
      "typetext": "<string>"
    },
    "roleid": {
      "format": "pve-roleid",
      "type": "string",
      "typetext": "<string>"
    }
  }
}
```

</details>

### 返回值

```json
{
  "type": "null"
}
```

来源：[官方 API 浏览器](https://pve.proxmox.com/pve-docs/api-viewer/index.html#/access/roles/{roleid})。
