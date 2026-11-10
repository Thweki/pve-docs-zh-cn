# 3.1. Package Repositories <a href="#sysadmin_package_repositories" id="sysadmin_package_repositories"></a>

Proxmox VE uses [APT](http://en.wikipedia.org/wiki/Advanced_Packaging_Tool) as its package management tool like any other Debian-based system.

Proxmox VE automatically checks for package updates on a daily basis. The `root@pam` user is notified via email about available updates. From the GUI, the *Changelog* button can be used to see more details about a selected update.

## 3.1.1. Repositories in Proxmox VE <a href="#_repositories_in_proxmox_ve" id="_repositories_in_proxmox_ve"></a>

Repositories are a collection of software packages, they can be used to install new software, but are also important to get new updates.

{% hint style="info" %}
You need valid Debian and Proxmox repositories to get the latest security updates, bug fixes and new features.
{% endhint %}

APT Repositories are defined in the file `/etc/apt/sources.list` in the legacy single-line format and in `.sources` files placed in `/etc/apt/sources.list.d/` for the modern deb822 multi-line format, see [Repository Formats](#sysadmin_apt_repo_formats) for details.

### Repository Management <a href="#_repository_management" id="_repository_management"></a>

[![screenshot/gui-node-repositories.png](../../assets/screenshot-gui-node-repositories-png-994a4b8cedfd.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-node-repositories.png)

Since Proxmox VE 7, you can check the repository state in the web interface. The node summary panel shows a high level status overview, while the separate *Repository* panel shows in-depth status and list of all configured repositories.

Basic repository management, for example, activating or deactivating a repository, is also supported.

The available packages from a repository are acquired by running `apt update`. Updates can be installed directly using `apt`, or via the GUI (Node → Updates).

### Repository Formats <a href="#sysadmin_apt_repo_formats" id="sysadmin_apt_repo_formats"></a>

Package repositories can be configured in the source list */etc/apt/sources.list* and the files contained in */etc/apt/sources.list.d/*.

There are two formats supported:

**single line**

In a single-line `sources.list` file, each line defines a package repository. Empty lines are ignored. A `#` character anywhere on a line marks the remainder of that line as a comment. This is the legacy format. Since Debian 13 Trixie apt will complain about using this format. You can automatically migrate most repositories using the `apt
modernize-sources` command.

**deb822**

In the multi-line format `repo.sources` file each entry consists of multiple lines of key-value pairs. A file can include multiple entries by separating each group with a blank line. This is the modern format.

### Available Repositories <a href="#_available_repositories" id="_available_repositories"></a>

Proxmox VE provides three different package repositories in addition to requiring the base Debian repositories.

## 3.1.2. Debian Base Repositories <a href="#_debian_base_repositories" id="_debian_base_repositories"></a>

**File `/etc/apt/sources.list.d/debian.sources`**

```text
Types: deb deb-src
URIs: http://deb.debian.org/debian/
Suites: trixie trixie-updates
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

Types: deb deb-src
URIs: http://security.debian.org/debian-security/
Suites: trixie-security
Components: main non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
```

## 3.1.3. Proxmox VE Enterprise Repository <a href="#sysadmin_enterprise_repo" id="sysadmin_enterprise_repo"></a>

This is the recommended repository and available for all Proxmox VE subscription users. It contains the most stable packages and is suitable for production use. The `pve-enterprise` repository is enabled by default:

**File `/etc/apt/sources.list.d/pve-enterprise.sources`**

```text
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

Please note that you need a valid subscription key to access the `pve-enterprise` repository. We offer different support levels, which you can find further details about at [https://proxmox.com/en/proxmox-virtual-environment/pricing](https://proxmox.com/en/proxmox-virtual-environment/pricing).

{% hint style="info" %}
Subscription keys are bound to the host architecture. An arm64 host needs a dedicated arm64 subscription key; an x86 key is not valid on it, and vice versa.
{% endhint %}

{% hint style="info" %}
You can disable this repository by adding an `Enabled: no` line to the relevant entry in the file. This will prevent error messages if your host does not have a subscription key. In that case, please configure the `pve-no-subscription` repository.
{% endhint %}

## 3.1.4. Proxmox VE No-Subscription Repository <a href="#sysadmin_no_subscription_repo" id="sysadmin_no_subscription_repo"></a>

As the name suggests, you do not need a subscription key to access this repository. It can be used for testing and non-production use. It’s not recommended to use this on production servers, as these packages are not always as heavily tested and validated.

We recommend to configure this repository in `/etc/apt/sources.list.d/proxmox.sources`.

**File `/etc/apt/sources.list.d/proxmox.sources`**

```text
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

{% hint style="info" %}
Remember that you will always need the base Debian repositories in addition to a Proxmox VE Proxmox repository.
{% endhint %}

## 3.1.5. Proxmox VE Test Repository <a href="#sysadmin_test_repo" id="sysadmin_test_repo"></a>

This repository contains the latest packages and is primarily used by developers to test new features. To configure it, add the following stanza to the file `/etc/apt/sources.list.d/proxmox.sources`:

**File `/etc/apt/sources.list.d/proxmox.sources`**

```text
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-test
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

{% hint style="warning" %}
The `pve-test` repository should (as the name implies) only be used for testing new features or bug fixes.
{% endhint %}

## 3.1.6. Proxmox VE Debug Symbol Repository <a href="#sysadmin_dbgsym_repo" id="sysadmin_dbgsym_repo"></a>

Debug symbol packages, named `<package>-dbgsym`, contain the detached debug information for the matching binary package. They are not needed for normal operation, but let tools such as `gdb`, `systemd-coredump` or `crash` produce useful backtraces when analyzing a crash or hang. They are provided in a dedicated repository, separate from the regular ones, for the Debian Bookworm and Trixie based Proxmox VE releases (and newer).

**File `/etc/apt/sources.list.d/pve-dbgsym.sources`**

```text
Types: deb
URIs: https://dbgsym.proxmox.com/debian/pve
Suites: trixie
Components: pve-dbgsym
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

After enabling the repository, install the `-dbgsym` package that matches the binary you want to debug.

## 3.1.7. Ceph Repositories <a href="#sysadmin_package_repositories_ceph" id="sysadmin_package_repositories_ceph"></a>

Ceph-related packages are kept up to date with a preconfigured Ceph enterprise repository. Preinstalled packages enable connecting to an external Ceph cluster and adding its [RBD](../07-storage/14-ceph-rados-block-devices.md#ceph_rados_block_devices) or [CephFS](../07-storage/15-storage-cephfs.md#storage_cephfs) pools as storage. You can also build a [hyper-converged infrastructure (HCI)](../01-introduction/07-chapter-hyper-converged-infrastructure.md#chapter_hyper_converged_infrastructure) by running [Ceph](../08-pveceph/README.md#chapter_pveceph) on top of the Proxmox VE cluster.

Information from this chapter is helpful in the following cases:

**Installing Ceph to build an HCI**

Decide on a below described repository and recent Ceph release, which you can then select in the [web-based wizard or the CLI tool](../08-pveceph/04-pve-ceph-install-wizard.md#pve_ceph_install_wizard).

**Already running the HCI and want to upgrade to the succeeding *Ceph* major release**

Please follow the related [Ceph upgrade guide](https://pve.proxmox.com/wiki/Category:Ceph_Upgrade).

**Already running the HCI and want to upgrade to the succeeding *Proxmox VE* major release**

In an HCI each Proxmox VE major release requires a corresponding minimum Ceph major release, please follow the related [Proxmox VE upgrade guide](https://pve.proxmox.com/wiki/Category:Upgrade).

**Not running an HCI but using an external Ceph cluster**

To install newer packages used to connect to Ceph, apply available system updates, decide on a repository and Ceph release listed below, add it to your node via the *[Repository](#_repository_management)* panel, apply newly available system updates, verify the result by running `ceph --version` and disable the old Ceph repository.

<a id="ceph_release_table"></a>



**Ceph releases available in Proxmox VE 9**

To read the latest version of the admin guide for your Proxmox VE release, make sure that all system updates are installed and that this page has been reloaded.

<table>





<tbody>
<tr>
<td><p></p></td>
<td><p><a href="https://docs.ceph.com/en/tentacle/releases/">Estimated End-of-Life</a></p></td>
<td><p><strong><code>enterprise</code></strong></p></td>
<td><p><strong><code>no-subscription</code></strong></p></td>
<td><p><strong><code>test</code></strong></p></td>
</tr>
<tr>
<td><p><strong><code>ceph-tentacle</code></strong></p></td>
<td><p>2027-11 (v20.2)</p></td>
<td><p>recommended</p></td>
<td><p>available</p></td>
<td><p>available</p></td>
</tr>
<tr>
<td><p><strong><code>ceph-squid</code></strong></p></td>
<td><p>2026-09 (v19.2)</p></td>
<td><p>available</p></td>
<td><p>available</p></td>
<td><p>available</p></td>
</tr>
</tbody>
</table>

**Ceph repositories for Proxmox VE 9**

The content of the `ceph.sources` file below serves as a reference (prior to Proxmox VE 9 the file `ceph.list` was used). To make changes, please follow the case that applies to your situation as described at the beginning of this subchapter. If you have disabled a repository in the web UI and also want to delist it, you can manually remove the corresponding entry from the file.

**`enterprise`**

This repository is recommended for production use and contains the most stable package versions. It is accessible if the Proxmox VE node has a valid subscription of any level. For details and included customer support levels visit:

[https://proxmox.com/en/proxmox-virtual-environment/pricing](https://proxmox.com/en/proxmox-virtual-environment/pricing)

**File `/etc/apt/sources.list.d/ceph.sources`**

```text
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-tentacle
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

**`no-subscription`**

This repository is suitable for testing and for non-production use. It is freely accessible and does not require a valid subscription. After some time, its package versions are also made available in the enterprise repository.

**File `/etc/apt/sources.list.d/ceph.sources`**

```text
Types: deb
URIs: http://download.proxmox.com/debian/ceph-tentacle
Suites: trixie
Components: no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

**`test`**

This repository contains the latest package versions and is primarily used by developers to test new features and bug fixes.

**File `/etc/apt/sources.list.d/ceph.sources`**

```text
Types: deb
URIs: http://download.proxmox.com/debian/ceph-tentacle
Suites: trixie
Components: test
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
```

{% hint style="warning" %}
The Ceph **`test`** repository should (as the name implies) only be used for testing new features or bug fixes.
{% endhint %}

## 3.1.8. Debian Firmware Repository <a href="#sysadmin_debian_firmware_repo" id="sysadmin_debian_firmware_repo"></a>

Starting with Debian Bookworm (Proxmox VE 8) non-free firmware (as defined by [DFSG](https://www.debian.org/social_contract#guidelines)) has been moved to the newly created Debian repository component `non-free-firmware`.

Since Proxmox VE 9 this repository is enabled by default for new installations to ensure they can get [Early OS Microcode Updates](03-chapter-firmware-updates.md#sysadmin_firmware_cpu).

You can also acquire need additional [Runtime Firmware Files](03-chapter-firmware-updates.md#sysadmin_firmware_runtime_files) not already included in the pre-installed package `pve-firmware`.

To be able to install packages from this component, run `editor /etc/apt/sources.list`, append `non-free-firmware` to the end of each `.debian.org` repository line and run `apt update`.

If you upgraded your Proxmox VE 9 install from a previous version of Proxmox VE and have modernized your package repositories to the new deb822-style, you will need to adapt `/etc/apt/sources.list.d/debian.sources` instead. Run `editor
/etc/apt/sources.list.d/debian.sources` and add `non-free-firmware` to the lines starting with `Components:` of each stanza.

{% hint style="info" %}
Modernizing your package repositories is recommended. Otherwise, `apt` on Debian Trixie will complain. You can run `apt modernize-sources` to do so.
{% endhint %}

## 3.1.9. SecureApt <a href="#repos_secure_apt" id="repos_secure_apt"></a>

The *Release* files in the repositories are signed with GnuPG. APT is using these signatures to verify that all packages are from a trusted source.

If you install Proxmox VE from an official ISO image, the key for verification is already installed.

If you install Proxmox VE on top of Debian, download and install the key with the following commands:

```text
 # wget https://enterprise.proxmox.com/debian/proxmox-archive-keyring-trixie.gpg -O /usr/share/keyrings/proxmox-archive-keyring.gpg
```

{% hint style="info" %}
The `wget` command above adds the keyring for Proxmox releases based on Debian Trixie. Once the `proxmox-archive-keyring` package is installed, it will manage this file. At that point, the hashes below may no longer match the hashes of this file, as keys for new Proxmox releases get added or removed. This is intended, `apt` will ensure that only trusted keys are being used. **Modifying this file is discouraged once `proxmox-archive-keyring` is installed.**
{% endhint %}

Verify the checksum afterwards with the `sha512sum` CLI tool:

```text
# sha256sum /usr/share/keyrings/proxmox-archive-keyring.gpg
 136673be77aba35dcce385b28737689ad64fd785a797e57897589aed08db6e45 /usr/share/keyrings/proxmox-archive-keyring.gpg
```

or the `md5sum` CLI tool:

```text
# md5sum /usr/share/keyrings/proxmox-archive-keyring.gpg
77c8b1166d15ce8350102ab1bca2fcbf /usr/share/keyrings/proxmox-archive-keyring.gpg
```

{% hint style="info" %}
Make sure the path you install the key to matches the `Signed-By:` lines in your repository stanzas.
{% endhint %}

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
