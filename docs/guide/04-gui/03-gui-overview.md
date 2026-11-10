# 4.3. GUI Overview <a href="#_gui_overview" id="_gui_overview"></a>

[![screenshot/gui-datacenter-summary.png](../../assets/screenshot-gui-datacenter-summary-png-ade3f5660241.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-summary.png)

The Proxmox VE user interface consists of four regions.

<table>
<tr>
<td>Header <br/></td>
<td>
<p>On top. Shows status information and contains buttons for most important actions.</p>
</td>
</tr>
<tr>
<td>Resource Tree <br/></td>
<td>
<p>At the left side. A navigation tree where you can select specific objects.</p>
</td>
</tr>
<tr>
<td>Content Panel <br/></td>
<td>
<p>Center region. Selected objects display configuration options and status here.</p>
</td>
</tr>
<tr>
<td>Log Panel <br/></td>
<td>
<p>At the bottom. Displays log entries for recent tasks. You can double-click on those log entries to get more details, or to abort a running task.</p>
</td>
</tr>
</table>

{% hint style="info" %}
You can shrink and expand the size of the resource tree and log panel, or completely hide the log panel. This can be helpful when you work on small displays and want more space to view other content.
{% endhint %}

## 4.3.1. Header <a href="#_header" id="_header"></a>

On the top left side, the first thing you see is the Proxmox logo. Next to it is the current running version of Proxmox VE. In the search bar nearside you can search for specific objects (VMs, containers, nodes, …). This is sometimes faster than selecting an object in the resource tree.

The right part of the header contains four buttons:

<table>
<tr>
<td>Documentation <br/></td>
<td>
<p>Opens a new browser window showing the reference documentation.</p>
</td>
</tr>
<tr>
<td>Create VM <br/></td>
<td>
<p>Opens the virtual machine creation wizard.</p>
</td>
</tr>
<tr>
<td>Create CT <br/></td>
<td>
<p>Open the container creation wizard.</p>
</td>
</tr>
<tr>
<td>User Menu <br/></td>
<td>
<p>Displays the identity of the user you’re currently logged in with, and clicking it opens a menu with user-specific options.</p>
<div>
<p>In the user menu, you’ll find the <em>My Settings</em> dialog, which provides local UI settings. Below that, there are shortcuts for <em>TFA</em> (Two-Factor Authentication) and <em>Password</em> self-service. You’ll also find options to change the <em>Language</em> and the <em>Color Theme.</em> Finally, at the bottom of the menu is the <em>Logout</em> option.</p>
</div>
</td>
</tr>
</table>

## 4.3.2. My Settings <a href="#gui_my_settings" id="gui_my_settings"></a>

[![screenshot/gui-my-settings.png](../../assets/screenshot-gui-my-settings-png-318ec9e5f40a.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-my-settings.png)

The *My Settings* window allows you to set locally stored settings. These include the *Dashboard Storages* which allow you to enable or disable specific storages to be counted towards the total amount visible in the datacenter summary. If no storage is checked the total is the sum of all storages, same as enabling every single one.

Below the dashboard settings you find the stored user name and a button to clear it as well as a button to reset every layout in the GUI to its default.

On the right side there are *xterm.js Settings*. These contain the following options:

<table>
<tr>
<td>Font-Family <br/></td>
<td>
<p>The font to be used in xterm.js (e.g. Arial).</p>
</td>
</tr>
<tr>
<td>Font-Size <br/></td>
<td>
<p>The preferred font size to be used.</p>
</td>
</tr>
<tr>
<td>Letter Spacing <br/></td>
<td>
<p>Increases or decreases spacing between letters in text.</p>
</td>
</tr>
<tr>
<td>Line Height <br/></td>
<td>
<p>Specify the absolute height of a line.</p>
</td>
</tr>
</table>

## 4.3.3. Resource Tree <a href="#_resource_tree" id="_resource_tree"></a>

This is the main navigation tree. On top of the tree you can select some predefined views, which change the structure of the tree below. The default view is the **Server View**, and it shows the following object types:

<table>
<tr>
<td>Datacenter <br/></td>
<td>
<p>Contains cluster-wide settings (relevant for all nodes).</p>
</td>
</tr>
<tr>
<td>Node <br/></td>
<td>
<p>Represents the hosts inside a cluster, where the guests run.</p>
</td>
</tr>
<tr>
<td>Guest <br/></td>
<td>
<p>VMs, containers and templates.</p>
</td>
</tr>
<tr>
<td>Storage <br/></td>
<td>
<p>Data Storage.</p>
</td>
</tr>
<tr>
<td>Pool <br/></td>
<td>
<p>It is possible to group guests using a pool to simplify management.</p>
</td>
</tr>
</table>

The following view types are available:

<table>
<tr>
<td>Server View <br/></td>
<td>
<p>Shows all kinds of objects, grouped by nodes.</p>
</td>
</tr>
<tr>
<td>Folder View <br/></td>
<td>
<p>Shows all kinds of objects, grouped by object type.</p>
</td>
</tr>
<tr>
<td>Pool View <br/></td>
<td>
<p>Show VMs and containers, grouped by pool.</p>
</td>
</tr>
<tr>
<td>Tag View <br/></td>
<td>
<p>Show VMs and containers, grouped by tags.</p>
</td>
</tr>
</table>

## 4.3.4. Log Panel <a href="#_log_panel" id="_log_panel"></a>

The main purpose of the log panel is to show you what is currently going on in your cluster. Actions like creating an new VM are executed in the background, and we call such a background job a *task*.

Any output from such a task is saved into a separate log file. You can view that log by simply double-click a task log entry. It is also possible to abort a running task there.

Please note that we display the most recent tasks from all cluster nodes here. So you can see when somebody else is working on another cluster node in real-time.

{% hint style="info" %}
We remove older and finished task from the log panel to keep that list short. But you can still find those tasks within the node panel in the *Task History*.
{% endhint %}

Some short-running actions simply send logs to all cluster members. You can see those messages in the *Cluster log* panel.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
