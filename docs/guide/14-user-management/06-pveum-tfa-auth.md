# 14.6. 双因素身份验证 <a href="#pveum_tfa_auth" id="pveum_tfa_auth"></a>

有两种方式使用双因素身份验证：

认证域可以要求使用 *TOTP*（基于时间的一次性密码）或 *YubiKey OTP*。此时，新创建的用户需要立即添加密钥，因为没有第二因素就无法登录。对于 *TOTP*，用户还可以稍后更改 *TOTP*，前提是他们能够先登录。

或者，即使认证域不强制要求，用户也可以在之后选择启用双因素身份验证。

## 14.6.1. 可用的第二因素 <a href="#available_second_factors" id="available_second_factors"></a>

可以设置多个第二因素，以避免丢失智能手机或安全密钥后永久无法访问账户。

除认证域强制使用的 TOTP 和 YubiKey OTP 外，还可以使用以下双因素身份验证方法：

- 用户配置的 TOTP（[基于时间的一次性密码](https://en.wikipedia.org/wiki/Time-based_One-Time_Password)）。由共享密钥和当前时间推导出的短代码，每 30 秒更改一次。
- WebAuthn（[Web 身份验证](https://en.wikipedia.org/wiki/WebAuthn)）。一种通用身份验证标准，由各种安全设备实现，例如硬件密钥，或计算机和智能手机中的可信平台模块（TPM）。
- 一次性恢复密钥。应将此密钥列表打印后锁在安全的地方，或以数字形式保存在电子保险库中。每个密钥只能使用一次。即使所有其他第二因素均丢失或损坏，它们也能很好地确保您不会被锁定在账户之外。

在支持 WebAuthn 之前，用户可以设置 U2F。现有 U2F 因素仍可使用，但建议在服务器上配置 WebAuthn 后切换到 WebAuthn。

## 14.6.2. 认证域强制的双因素身份验证 <a href="#realm_enforced_two_factor_authentication" id="realm_enforced_two_factor_authentication"></a>

添加或编辑认证域时，可通过 *TFA* 下拉框选择一种可用方法。认证域启用 TFA 后，TFA 将成为强制要求，只有配置了 TFA 的用户才能登录。

目前有两种可用方法：

**基于时间的 OATH（TOTP）**

这使用标准 HMAC-SHA1 算法，将当前时间与用户配置的密钥一起进行哈希。时间步长和密码长度参数可配置。

用户可以配置多个密钥（以空格分隔），密钥可以使用 Base32（RFC3548）或十六进制表示。

Proxmox VE 提供密钥生成工具（`oathkeygen`），可输出 Base32 表示的随机密钥，直接用于各种 OTP 工具，例如 `oathtool` 命令行工具，或 Android 上的 Google Authenticator、FreeOTP、andOTP 等类似应用。

**YubiKey OTP**

通过 YubiKey 进行身份验证时，必须配置 Yubico API ID、API KEY 和验证服务器 URL，并且用户必须拥有可用的 YubiKey。要从 YubiKey 获取密钥 ID，可以通过 USB 连接后触发 YubiKey 一次，并将输入密码的前 12 个字符复制到用户的 *密钥 ID* 字段。

请参阅 [YubiKey OTP](https://developers.yubico.com/OTP/) 文档，了解如何使用 [YubiCloud](https://www.yubico.com/products/services-software/yubicloud/) 或 [托管自己的验证服务器](https://developers.yubico.com/Software_Projects/Yubico_OTP/YubiCloud_Validation_Servers/)。

## 14.6.3. 双因素身份验证的限制与锁定 <a href="#pveum_tfa_lockout" id="pveum_tfa_lockout"></a>

第二因素旨在用户密码以某种方式泄露或被猜出时提供保护。然而，某些因素仍可能被暴力破解。因此，第二因素登录尝试失败过多后，用户会被锁定。

对于 TOTP，8 次失败尝试会禁用用户的 TOTP 因素。使用恢复密钥登录时会解锁。如果 TOTP 是唯一可用因素，则需要管理员介入，并强烈建议要求用户立即更改密码。

由于 FIDO2/Webauthn 和恢复密钥较不易遭受暴力攻击，其限制较高（100 次尝试），但超出限制后，所有第二因素将被阻止一小时。

管理员可随时通过 UI 中的用户列表或命令行解锁用户的双因素身份验证：

```text
 pveum user tfa unlock joe@pve
```

## 14.6.4. 用户配置的 TOTP 身份验证 <a href="#pveum_user_configured_totp" id="pveum_user_configured_totp"></a>

用户可以选择启用 *TOTP* 或 *WebAuthn* 作为登录时的第二因素，通过用户列表中的 *TFA* 按钮进行设置（除非认证域强制使用 *YubiKey OTP*）。

用户始终可以添加和使用一次性 *恢复密钥*。

[![screenshot/gui-datacenter-two-factor.png](../../assets/screenshot-gui-datacenter-two-factor-png-00fd252ee4e8.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-two-factor.png)

打开 *TFA* 窗口后，用户会看到用于设置 *TOTP* 身份验证的对话框。*密钥* 字段包含密钥，可通过 *随机生成* 按钮随机生成。可以添加可选的 *签发者名称*，向 *TOTP* 应用提供此密钥用途的信息。大多数 *TOTP* 应用会将签发者名称与对应的 *OTP* 值一起显示。用户名也包含在供 *TOTP* 应用使用的二维码中。

生成密钥后，会显示二维码，可用于 FreeOTP 等大多数 OTP 应用。随后用户需要验证当前用户密码（除非以 *root* 登录），并验证能够正确使用 *TOTP* 密钥：将当前 *OTP* 值输入 *验证码* 字段，然后按 *应用* 按钮。

## 14.6.5. TOTP <a href="#user_tfa_setup_totp" id="user_tfa_setup_totp"></a>

[![screenshot/pve-gui-tfa-add-totp.png](../../assets/screenshot-pve-gui-tfa-add-totp-png-9157bafa11cd.png)](https://pve.proxmox.com/pve-docs/images/screenshot/pve-gui-tfa-add-totp.png)

不需要服务器设置。只需在智能手机上安装 TOTP 应用（例如 [FreeOTP](https://freeotp.github.io/)），并使用 Proxmox VE Web 界面添加 TOTP 因素。

## 14.6.6. WebAuthn <a href="#user_tfa_setup_webauthn" id="user_tfa_setup_webauthn"></a>

要使 WebAuthn 正常工作，需要具备两项条件：

- 受信任的 HTTPS 证书（例如使用 [Let’s Encrypt](https://pve.proxmox.com/wiki/Certificate_Management)）。虽然它可能可以使用不受信任的证书工作，但如果证书不受信任，某些浏览器可能发出警告或拒绝 WebAuthn 操作。
- 设置 WebAuthn 配置（参见 Proxmox VE Web 界面的 **数据中心 → 选项 → WebAuthn 设置**）。大多数设置中可以自动填充。

满足这两项要求后，即可在 **双因素** 面板（位于 **数据中心 → 权限 → 双因素** 下）添加 WebAuthn 配置。

## 14.6.7. 恢复密钥 <a href="#user_tfa_setup_recovery_keys" id="user_tfa_setup_recovery_keys"></a>

[![screenshot/pve-gui-tfa-add-recovery-keys.png](../../assets/screenshot-pve-gui-tfa-add-recovery-keys-png-fe14f3271438.png)](https://pve.proxmox.com/pve-docs/images/screenshot/pve-gui-tfa-add-recovery-keys.png)

恢复密钥代码无需任何准备；只需在 **双因素** 面板（位于 **数据中心 → 权限 → 双因素** 下）创建一组恢复密钥。

{% hint style="info" %}
任何时候，每个用户只能有一组一次性恢复密钥。
{% endhint %}

## 14.6.8. 服务器端 Webauthn 配置 <a href="#pveum_configure_webauthn" id="pveum_configure_webauthn"></a>

[![screenshot/gui-datacenter-webauthn-edit.png](../../assets/screenshot-gui-datacenter-webauthn-edit-png-6abfdb023d63.png)](https://pve.proxmox.com/pve-docs/images/screenshot/gui-datacenter-webauthn-edit.png)

要允许用户使用 *WebAuthn* 身份验证，必须使用具有有效 SSL 证书的有效域名，否则某些浏览器可能发出警告或完全拒绝身份验证。

{% hint style="info" %}
更改 *WebAuthn* 配置可能使所有现有的 *WebAuthn* 注册失效！
{% endhint %}

这通过 `/etc/pve/datacenter.cfg` 完成。例如：

```text
webauthn: rp=mypve.example.com,origin=https://mypve.example.com:8006,id=mypve.example.com
```

## 14.6.9. 服务器端 U2F 配置 <a href="#pveum_configure_u2f" id="pveum_configure_u2f"></a>

{% hint style="info" %}
建议改用 WebAuthn。
{% endhint %}

要允许用户使用 *U2F* 身份验证，可能需要使用具有有效 SSL 证书的有效域名，否则某些浏览器可能发出警告或完全拒绝使用 U2F。最初需要配置 *AppId* [\[1\]](#note-f8fe8903-1)。

{% hint style="info" %}
更改 *AppId* 会使所有现有的 *U2F* 注册失效！
{% endhint %}

这通过 `/etc/pve/datacenter.cfg` 完成。例如：

```text
u2f: appid=https://mypve.example.com:8006
```

对于单个节点，*AppId* 可以直接设为 Web 界面的地址，与浏览器中使用的完全相同，包括 *https://* 和端口，如上所示。请注意，某些浏览器在匹配 *AppId* 时可能比其他浏览器更严格。

使用多个节点时，最好使用单独的 `https` 服务器提供 `appid.json` [\[2\]](#note-f8fe8903-2) 文件，因为这似乎与大多数浏览器兼容。如果所有节点使用同一顶级域名的子域名，使用该顶级域名作为 *AppId* 可能就足够了。不过应注意，某些浏览器可能不接受这种方式。

{% hint style="info" %}
错误的 *AppId* 通常会产生错误，但我们遇到过不产生错误的情况，特别是在 Chromium 中，通过子域名访问节点，却使用顶级域名的 *AppId* 时。因此，建议使用多个浏览器测试配置，因为之后更改 *AppId* 会使现有的 *U2F* 注册失效。
{% endhint %}

## 14.6.10. 用户激活 U2F <a href="#pveum_user_configured_u2f" id="pveum_user_configured_u2f"></a>

要启用 *U2F* 身份验证，打开 *TFA* 窗口的 *U2F* 选项卡，输入当前密码（除非以 root 登录），然后按 *注册* 按钮。如果服务器设置正确，且浏览器接受服务器提供的 *AppId*，将出现消息，提示用户按下 *U2F* 设备上的按钮（如果是 *YubiKey*，按钮指示灯应稳定闪烁，约每秒两次）。

Firefox 用户可能需要启用 *security.webauth.u2f*（通过 *about:config*），才能使用 *U2F* 令牌。

## 注释

### 注释 1 <a href="#note-f8fe8903-1" id="note-f8fe8903-1"></a>

AppId [https://developers.yubico.com/U2F/App\_ID.html](https://developers.yubico.com/U2F/App_ID.html)

### 注释 2 <a href="#note-f8fe8903-2" id="note-f8fe8903-2"></a>

多 facet 应用：[https://developers.yubico.com/U2F/App\_ID.html](https://developers.yubico.com/U2F/App_ID.html)

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
