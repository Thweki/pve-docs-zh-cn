# 1.13. Translating Proxmox VE <a href="#translation" id="translation"></a>

The Proxmox VE user interface is in English by default. However, thanks to the contributions of the community, translations to other languages are also available. We welcome any support in adding new languages, translating the latest features, and improving incomplete or inconsistent translations.

We use [gettext](https://www.gnu.org/software/gettext/) for the management of the translation files. Tools like [Poedit](https://poedit.net/) offer a nice user interface to edit the translation files, but you can use whatever editor you’re comfortable with. No programming knowledge is required for translating.

## 1.13.1. Translating with git <a href="#i18n_with_git" id="i18n_with_git"></a>

The language files are available as a [git repository](https://git.proxmox.com/?p=proxmox-i18n.git). If you are familiar with git, please contribute according to our [Developer Documentation](https://pve.proxmox.com/wiki/Developer_Documentation).

You can create a new translation by doing the following (replace <LANG> with the language ID):

```text
# git clone git://git.proxmox.com/git/proxmox-i18n.git
# cd proxmox-i18n
# make init-<LANG>.po
```

Or you can edit an existing translation, using the editor of your choice:

```text
# poedit <LANG>.po
```

## 1.13.2. Translating without git <a href="#i18n_without_git" id="i18n_without_git"></a>

Even if you are not familiar with git, you can help translate Proxmox VE. To start, you can download the language files [here](https://git.proxmox.com/?p=proxmox-i18n.git;a=tree). Find the language you want to improve, then right click on the "raw" link of this language file and select *Save Link As…*. Make your changes to the file, and then send your final translation directly to office(at)proxmox.com, together with a signed [contributor license agreement](https://pve.proxmox.com/wiki/Developer_Documentation#Software_License_and_Copyright).

## 1.13.3. Testing the Translation <a href="#_testing_the_translation" id="_testing_the_translation"></a>

In order for the translation to be used in Proxmox VE, you must first translate the `.po` file into a `.js` file. You can do this by invoking the following script, which is located in the same repository:

```text
# ./po2js.pl -t pve xx.po >pve-lang-xx.js
```

The resulting file `pve-lang-xx.js` can then be copied to the directory `/usr/share/pve-i18n`, on your proxmox server, in order to test it out.

Alternatively, you can build a deb package by running the following command from the root of the repository:

```text
# make deb
```

{% hint style="warning" %}
For either of these methods to work, you need to have the following perl packages installed on your system. For Debian/Ubuntu:
{% endhint %}

```text
# apt-get install perl liblocale-po-perl libjson-perl
```

## 1.13.4. Sending the Translation <a href="#_sending_the_translation" id="_sending_the_translation"></a>

You can send the finished translation (`.po` file) to the Proxmox team at the address office(at)proxmox.com, along with a signed contributor license agreement. Alternatively, if you have some developer experience, you can send it as a patch to the Proxmox VE development mailing list. See [Developer Documentation](https://pve.proxmox.com/wiki/Developer_Documentation).

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
