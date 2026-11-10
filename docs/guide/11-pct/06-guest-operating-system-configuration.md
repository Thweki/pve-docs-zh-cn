# 11.6. Guest Operating System Configuration <a href="#_guest_operating_system_configuration" id="_guest_operating_system_configuration"></a>

Proxmox VE tries to detect the Linux distribution in the container, and modifies some files. Here is a short list of things done at container startup:

**set /etc/hostname**

to set the container name

**modify /etc/hosts**

to allow lookup of the local hostname

**network setup**

pass the complete network setup to the container

**configure DNS**

pass information about DNS servers

**adapt the init system**

for example, fix the number of spawned getty processes

**set the root password**

when creating a new container

**rewrite ssh_host_keys**

so that each container has unique keys

**randomize crontab**

so that cron does not start at the same time on all containers

Changes made by Proxmox VE are enclosed by comment markers:

```text
# --- BEGIN PVE ---
<data>
# --- END PVE ---
```

Those markers will be inserted at a reasonable location in the file. If such a section already exists, it will be updated in place and will not be moved.

Modification of a file can be prevented by adding a `.pve-ignore.` file for it. For instance, if the file `/etc/.pve-ignore.hosts` exists then the `/etc/hosts` file will not be touched. This can be a simple empty file created via:

```text
# touch /etc/.pve-ignore.hosts
```

Most modifications are OS dependent, so they differ between different distributions and versions. You can completely disable modifications by manually setting the `ostype` to `unmanaged`.

OS type detection is done by testing for certain files inside the container. Proxmox VE first checks the `/etc/os-release` file   
[/etc/os-release replaces the multitude of per-distribution release files [https://manpages.debian.org/stable/systemd/os-release.5.en.html](https://manpages.debian.org/stable/systemd/os-release.5.en.html)]  
. If that file is not present, or it does not contain a clearly recognizable distribution identifier the following distribution specific release files are checked.

**Ubuntu**

inspect /etc/lsb-release (`DISTRIB_ID=Ubuntu`)

**Debian**

test /etc/debian_version

**Fedora**

test /etc/fedora-release

**RedHat or CentOS**

test /etc/redhat-release

**ArchLinux**

test /etc/arch-release

**Alpine**

test /etc/alpine-release

**Gentoo**

test /etc/gentoo-release

{% hint style="info" %}
Container start fails if the configured `ostype` differs from the auto detected type.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
