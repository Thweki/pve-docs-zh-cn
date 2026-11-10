# 28.1. Markdown Basics <a href="#markdown_basics" id="markdown_basics"></a>

Note that we only describe the basics here, please search the web for more extensive resources, for example on [https://www.markdownguide.org/](https://www.markdownguide.org/)

## 28.1.1. Headings <a href="#_headings" id="_headings"></a>

```text
# This is a Heading h1
## This is a Heading h2
##### This is a Heading h5
```

## 28.1.2. Emphasis <a href="#_emphasis" id="_emphasis"></a>

Use `*text*` or `_text_` for emphasis.

Use `**text**` or `__text__` for bold, heavy-weight text.

Combinations are also possible, for example:

```text
_You **can** combine them_
```

## 28.1.3. Links <a href="#_links" id="_links"></a>

You can use automatic detection of links, for example, `https://forum.proxmox.com/` would transform it into a clickable link.

You can also control the link text, for example:

```text
Now, [the part in brackets will be the link text](https://forum.proxmox.com/).
```

## 28.1.4. Lists <a href="#_lists" id="_lists"></a>

### Unordered Lists <a href="#_unordered_lists" id="_unordered_lists"></a>

Use `*` or `-` for unordered lists, for example:

```text
* Item 1
* Item 2
* Item 2a
* Item 2b
```

Adding an indentation can be used to created nested lists.

### Ordered Lists <a href="#_ordered_lists" id="_ordered_lists"></a>

```text
1. Item 1
1. Item 2
1. Item 3
  1. Item 3a
  1. Item 3b
```

{% hint style="info" %}
The integer of ordered lists does not need to be correct, they will be numbered automatically.
{% endhint %}

### Task Lists <a href="#_task_lists" id="_task_lists"></a>

Task list use a empty box `[ ]` for unfinished tasks and a box with an `X` for finished tasks.

例如：

```text
- [X] First task already done!
- [X] Second one too
- [ ] This one is still to-do
- [ ] So is this one
```

## 28.1.5. Tables <a href="#_tables" id="_tables"></a>

Tables use the pipe symbol `|` to separate columns, and `-` to separate the table header from the table body, in that separation one can also set the text alignment, making one column left-, center-, or right-aligned.

```text
| Left columns  | Right columns |  Some  | More | Cols.| Centering Works Too
| ------------- |--------------:|--------|------|------|:------------------:|
| left foo      | right foo     | First  | Row  | Here | >center<           |
| left bar      | right bar     | Second | Row  | Here | 12345              |
| left baz      | right baz     | Third  | Row  | Here | Test               |
| left zab      | right zab     | Fourth | Row  | Here | ☁️☁️☁️              |
| left rab      | right rab     | And    | Last | Here | The End            |
```

Note that you do not need to align the columns nicely with white space, but that makes editing tables easier.

## 28.1.6. Block Quotes <a href="#_block_quotes" id="_block_quotes"></a>

You can enter block quotes by prefixing a line with `>`, similar as in plain-text emails.

```text
> Markdown is a lightweight markup language with plain-text-formatting syntax,
> created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums,
>> and to create rich text using a plain text editor.
```

## 28.1.7. Code and Snippets <a href="#_code_and_snippets" id="_code_and_snippets"></a>

You can use backticks to avoid processing for a few word or paragraphs. That is useful for avoiding that a code or configuration hunk gets mistakenly interpreted as markdown.

### Inline code <a href="#_inline_code" id="_inline_code"></a>

Surrounding part of a line with single backticks allows to write code inline, for examples:

```text
This hosts IP address is `10.0.0.1`.
```

### Whole blocks of code <a href="#_whole_blocks_of_code" id="_whole_blocks_of_code"></a>

For code blocks spanning several lines you can use triple-backticks to start and end such a block, for example:

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
