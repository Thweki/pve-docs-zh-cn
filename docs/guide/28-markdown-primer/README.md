# 28\. 附录 G：Markdown 入门 <a href="#markdown_primer" id="markdown_primer"></a>

Markdown 是供 Web 写作者使用的文本转 HTML 工具。Markdown 允许您使用易读、易写的纯文本格式编写内容，然后将其转换为结构有效的 XHTML（或 HTML）。

<em>https://daringfireball.net/projects/markdown/</em>  
— John Gruber

Proxmox VE Web 界面支持使用 Markdown，在节点和虚拟客户机的备注中渲染富文本格式。

Proxmox VE 支持 CommonMark 以及 GFM（GitHub 风格 Markdown）的大多数扩展，例如表格或任务列表。

## 28.1. Markdown 基础 <a href="#markdown_basics" id="markdown_basics"></a>

请注意，这里仅介绍基础知识，更全面的资料请在网上搜索，例如 [https://www.markdownguide.org/](https://www.markdownguide.org/)

### 28.1.1. 标题 <a href="#headings" id="headings"></a>

```text
# This is a Heading h1
## This is a Heading h2
##### This is a Heading h5
```

### 28.1.2. 强调 <a href="#emphasis" id="emphasis"></a>

使用 `*text*` 或 `_text_` 表示强调。

使用 `**text**` 或 `__text__` 表示加粗、粗体文本。

也可以组合使用，例如：

```text
_You **can** combine them_
```

### 28.1.3. 链接 <a href="#links" id="links"></a>

可以使用自动链接检测，例如，`https://forum.proxmox.com/` 会被转换为可点击的链接。

也可以控制链接文本，例如：

```text
Now, [the part in brackets will be the link text](https://forum.proxmox.com/).
```

### 28.1.4. 列表 <a href="#lists" id="lists"></a>

#### 无序列表 <a href="#unordered_lists" id="unordered_lists"></a>

使用 `*` 或 `-` 表示无序列表，例如：

```text
* Item 1
* Item 2
* Item 2a
* Item 2b
```

添加缩进可用于创建嵌套列表。

#### 有序列表 <a href="#ordered_lists" id="ordered_lists"></a>

```text
1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b
```

{% hint style="info" %}
有序列表的整数无需正确，它们会自动编号。
{% endhint %}

#### 任务列表 <a href="#task_lists" id="task_lists"></a>

任务列表使用空框 `[ ]` 表示未完成任务，使用带有 `X` 的框表示已完成任务。

例如：

```text
- [X] First task already done!
- [X] Second one too
- [ ] This one is still to-do
- [ ] So is this one
```

### 28.1.5. 表格 <a href="#tables" id="tables"></a>

表格使用竖线符号 `|` 分隔列，使用 `-` 分隔表头与表格正文；还可以在该分隔行中设置文本对齐方式，使某列左对齐、居中或右对齐。

```text
| Left columns  | Right columns |  Some  | More | Cols.| Centering Works Too
| ------------- |--------------:|--------|------|------|:------------------:|
| left foo      | right foo     | First  | Row  | Here | >center<           |
| left bar      | right bar     | Second | Row  | Here | 12345              |
| left baz      | right baz     | Third  | Row  | Here | Test               |
| left zab      | right zab     | Fourth | Row  | Here | ☁️☁️☁️              |
| left rab      | right rab     | And    | Last | Here | The End            |
```

请注意，不需要使用空白字符将列整齐对齐，但这样做会让表格编辑更方便。

### 28.1.6. 块引用 <a href="#block_quotes" id="block_quotes"></a>

可以通过在行首添加 `>` 输入块引用，类似于纯文本电子邮件中的用法。

```text
> Markdown is a lightweight markup language with plain-text-formatting syntax,
> created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums,
>> and to create rich text using a plain text editor.
```

### 28.1.7. 代码和代码片段 <a href="#code_and_snippets" id="code_and_snippets"></a>

可以使用反引号使几个词或几个段落不被处理。这有助于避免代码或配置片段被错误地解释为 Markdown。

#### 行内代码 <a href="#inline_code" id="inline_code"></a>

使用单个反引号包围一行中的某个部分，可以编写行内代码，例如：

```text
This hosts IP address is `10.0.0.1`.
```

#### 完整代码块 <a href="#whole_blocks_of_code" id="whole_blocks_of_code"></a>

对于跨越多行的代码块，可以使用三个反引号作为代码块的起始和结束，例如：

````text
```
# This is the network config I want to remember here
auto vmbr2
iface vmbr2 inet static
        address 10.0.0.1/24
        bridge-ports ens20
        bridge-stp off
        bridge-fd 0
        bridge-vlan-aware yes
        bridge-vids 2-4094

```
````

---

来源：[Proxmox VE 官方文档](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) · 版本 9.2.13 · 非官方中文翻译。
