# 14.3. API Tokens <a href="#pveum_tokens" id="pveum_tokens"></a>

API tokens allow stateless access to most parts of the REST API from another system, software, or API client. Exceptions are endpoints that provide access to the virtual machine or system console. These endpoints require user privileges and cannot be accessed via an API token.

Tokens can be generated for individual users and can be given separate permissions and expiration dates to limit the scope and duration of the access. Should the API token get compromised, it can be revoked without disabling the user itself.

API tokens come in two basic types:

- Separated privileges: The token needs to be given explicit access with ACLs. Its effective permissions are calculated by intersecting user and token permissions. **This is the default** for newly created tokens.
- Full privileges: The token’s permissions are identical to that of the associated user. Disable Privilege Separation only when the integration genuinely needs the user’s full permissions.

Set an `expire` timestamp (Unix epoch seconds) when creating a token so that abandoned automation does not silently keep working. The authentication code refuses requests once the deadline has passed.

{% hint style="danger" %}
The token value is only displayed/returned once when the token is generated. It cannot be retrieved again over the API at a later time!
{% endhint %}

To use an API token, set the HTTP header *Authorization* to the displayed value of the form `PVEAPIToken=USER@REALM!TOKENID=UUID` when making API requests, or refer to your API client’s documentation.

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
