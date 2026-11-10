"""Render translated, structurally preserved HTML into GitBook-native Markdown."""
from __future__ import annotations
import argparse, collections, copy, hashlib, html, json, os, re, unicodedata
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter
from translate import validate

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
BASE='https://pve.proxmox.com/pve-docs/'
UNITS=json.loads((ROOT/('work/units.json' if (ROOT/'work/units.json').exists() else 'translations/units.json')).read_text())
TRANSLATIONS=json.loads((ROOT/'translations/zh-CN.json').read_text()) if (ROOT/'translations/zh-CN.json').exists() else {}
if (ROOT/'work/translations.jsonl').exists():
    for line in (ROOT/'work/translations.jsonl').read_text().splitlines():
        if line.strip():TRANSLATIONS.update(json.loads(line))
TRANSLATIONS={k:v for k,v in TRANSLATIONS.items() if k in UNITS and not validate(UNITS[k]['text'],v)}
PAGES=[];ANCHORS={};FILE_DEFAULTS={};CHAPTER_DEFAULTS={};API_LINKS={};PAGE_TOP_ANCHORS=set()

def restore(key):
    u=UNITS[key];text=TRANSLATIONS.get(key,u['text'])
    escaped=html.escape(text,quote=False)
    return re.sub(r'⟦(\d+)⟧',lambda m:u['fragments'][int(m[1])],escaped)

def translated_soup(path):
    soup=BeautifulSoup(path.read_text(),'html.parser')
    for el in soup.select('[data-i18n]'):
        key=el['data-i18n']
        el.clear()
        for child in list(BeautifulSoup(restore(key),'html.parser').contents):el.append(child)
    for el in soup.select('[data-i18n-alt]'):
        key=el['data-i18n-alt'];el['alt']=TRANSLATIONS.get(key,UNITS[key]['text'])
    for el in soup.find_all(True):
        for attr in list(el.attrs):
            if attr.startswith('data-i18n'):del el[attr]
    return soup

def plain_heading(el):
    return re.sub(r'\s+',' ',el.get_text(' ',strip=True))

def anchor_id(value):
    # GitBook strips leading underscores and normalizes custom heading anchors.
    return re.sub(r'[^a-z0-9_-]+','-',value.lower()).strip('_-')

def add_page(path,node,source,title=None,shift=0):
    # AsciiDoc's browser JS normally collects inline notes at the end. GitBook
    # drops standalone HTML anchors, so use native heading anchors for endnotes.
    notes=list(node.select('span.footnote'))
    if notes:
        factory=BeautifulSoup('','html.parser');section=factory.new_tag('div')
        heading=factory.new_tag('h'+str(2-shift));heading.string='注释';section.append(heading)
        for i,span in enumerate(notes,1):
            anchor=span.get('id') or 'note-'+hashlib.sha256(str(path).encode()).hexdigest()[:8]+'-'+str(i)
            label=re.sub(r'^_footnote_?','',span.get('id','')) or str(i)
            reference=factory.new_tag('a',href='#'+anchor);reference.string='['+label+']'
            inner=span.decode_contents()
            inner=re.sub(r'^\s*<br\s*/?>\s*\[','',inner)
            inner=re.sub(r'\]\s*<br\s*/?>\s*$','',inner)
            span.replace_with(reference)
            note_heading=factory.new_tag('h'+str(3-shift),id=anchor)
            note_heading.string='注释 '+label;section.append(note_heading)
            content=BeautifulSoup('<div>'+inner+'</div>','html.parser').div
            section.append(content)
        node.append(section)
    # Turn existing anchored captions and command signatures into native
    # headings, since GitBook does not retain standalone HTML bookmarks.
    for block in list(node.select('div[id]')):
        ident=block['id'];caption=block.find(class_='title',recursive=False)
        if caption is None and ident.startswith('cli_'):caption=block.find('p',recursive=False)
        if caption is None:continue
        parent_heading=None
        for parent in block.parents:
            if any(re.fullmatch(r'sect[1-6]',c) for c in parent.get('class',[])):
                parent_heading=parent.find(re.compile('^h[1-6]$'),recursive=False);break
        level=min(6,int(parent_heading.name[1])+1) if parent_heading else 3-shift
        caption.name='h'+str(level);caption['id']=ident;del block['id']
    for bibliography in node.select('.bibliography'):
        for li in list(bibliography.select('li')):li.unwrap()
        for ul in list(bibliography.select('ul')):ul.unwrap()
        for bookmark in list(bibliography.select('a[id]')):
            ident=bookmark['id'];paragraph=bookmark.find_parent('p')
            if paragraph is None:continue
            heading=BeautifulSoup('','html.parser').new_tag('h'+str(2-shift),id=ident)
            heading.string='['+ident+']';paragraph.insert_before(heading)
            sibling=bookmark.next_sibling
            if isinstance(sibling,NavigableString):
                sibling.replace_with(re.sub(r'^\s*\['+re.escape(ident)+r'\]+\s*','',str(sibling),count=1))
            bookmark.extract()
    heading=node.find(re.compile('^h[1-6]$'))
    title=title or (plain_heading(heading) if heading else path.stem)
    page={'path':path,'node':node,'source':source,'title':title,'shift':shift}
    PAGES.append(page)
    current=anchor_id(heading['id']) if heading and heading.get('id') else ''
    if current:PAGE_TOP_ANCHORS.add((path,current))
    for el in node.find_all(True):
        if re.fullmatch(r'h[1-6]',el.name) and el.get('id'):current=anchor_id(el['id'])
        if el.get('id'):
            # Remaining non-heading bookmarks resolve to their section heading.
            ANCHORS[(source,el['id'])]=(path,current)
    return page

def relpath(target,current):
    return os.path.relpath(DOCS/target,(DOCS/current).parent).replace(os.sep,'/')

def link(href,current,source):
    if not href:return href
    parsed=urlsplit(href)
    if parsed.scheme or parsed.netloc:
        if not href.startswith(BASE):return href
        href=href[len(BASE):];parsed=urlsplit(href)
    target=unquote(parsed.path) or source;fragment=unquote(parsed.fragment)
    if target.startswith('assets/'):
        return relpath(Path(target),current)+(('#'+fragment) if fragment else '')
    target=target.removeprefix('./')
    if target in {'api-viewer/','api-viewer/index.html'}:
        if not fragment:return relpath(Path('api/README.md'),current)
        if fragment in API_LINKS:
            page,anchor=API_LINKS[fragment]
            return relpath(page,current)+'#'+anchor
        return urljoin(BASE,href)
    if fragment:
        match=ANCHORS.get((target,fragment))
        if not match and target.startswith('chapter-'):
            match=ANCHORS.get(('pve-admin-guide.html',fragment))
        if match:
            page,anchor=match
            # GitBook promotes the first H1 to the page title, without its HTML id.
            if not anchor or (page,anchor) in PAGE_TOP_ANCHORS:return relpath(page,current)
            return ('' if page==current else relpath(page,current))+'#'+anchor
    if target in FILE_DEFAULTS:
        return relpath(FILE_DEFAULTS[target],current)+(('#'+fragment) if fragment else '')
    if target in CHAPTER_DEFAULTS:
        return relpath(CHAPTER_DEFAULTS[target],current)+(('#'+fragment) if fragment else '')
    if target=='index.html':return relpath(Path('README.md'),current)
    return urljoin(BASE,href)

class GitBookMarkdown(MarkdownConverter):
    def __init__(self,page):
        self.page=page
        super().__init__(heading_style='ATX',bullets='-',escape_misc=True,escape_underscores=True,escape_asterisks=True,autolinks=False,table_infer_header=True)
    def convert_strong(self,el,text,parent_tags):
        # CJK punctuation can prevent CommonMark ** delimiters from closing.
        return '<strong>'+text+'</strong>' if text else ''
    convert_b=convert_strong
    def convert_em(self,el,text,parent_tags):
        return '<em>'+text+'</em>' if text else ''
    convert_i=convert_em
    def convert_hN(self,n,el,text,parent_tags):
        n=max(1,min(6,n+self.page['shift']))
        title=re.sub(r'\s+',' ',text.strip())
        anchor=anchor_id(el['id']) if el.get('id') else None
        explicit=f' <a href="#{anchor}" id="{anchor}"></a>' if anchor else ''
        return '\n\n'+'#'*n+' '+title+explicit+'\n\n'
    def convert_pre(self,el,text,parent_tags):
        raw=el.get_text();fence='`'*max(3,max((len(m[0])+1 for m in re.finditer(r'`{3,}',raw)),default=3))
        return f'\n\n{fence}text\n{raw.rstrip(chr(10))}\n{fence}\n\n'
    def convert_span(self,el,text,parent_tags):
        if 'monospaced' in el.get('class',[]):
            raw=el.get_text();fence='``' if '`' in raw else '`'
            return fence+raw+fence
        return (f'<a id="{el["id"]}"></a>' if el.get('id') else '')+text
    def convert_a(self,el,text,parent_tags):
        href=el.get('href');anchor=el.get('id')
        if anchor and not text.strip():return f'<a id="{anchor}"></a>'
        if href:
            el=copy.copy(el)
            el['href']=link(href,self.page['path'],self.page['source'])
        return super().convert_a(el,text,parent_tags)
    def convert_img(self,el,text,parent_tags):
        src=el.get('src','');src=link(src,self.page['path'],self.page['source'])
        alt=el.get('alt','').replace('[',r'\[').replace(']',r'\]')
        return f'![{alt}]({src})'
    def convert_dt(self,el,text,parent_tags):return '\n\n**'+text.strip()+'**\n\n'
    def convert_dd(self,el,text,parent_tags):return '\n\n'+text.strip()+'\n\n'
    def convert_div(self,el,text,parent_tags):
        classes=el.get('class',[])
        if 'admonitionblock' in classes:
            icon=el.select_one('td.icon img')
            name=icon.get('alt','Note') if icon else 'Note'
            kind={'Note':'info','提示':'info','注':'info','注意':'info','Tip':'success','技巧':'success','建议':'success','Warning':'warning','警告':'warning','Important':'warning','重要':'warning','Caution':'danger','小心':'danger'}.get(name,'warning' if 'warning' in name.lower() else 'info')
            content=el.select_one('td.content')
            rendered=self.convert(content.decode_contents()).strip() if content else text.strip()
            return '\n\n{% hint style="'+kind+'" %}\n'+rendered+'\n{% endhint %}\n\n'
        if 'title' in classes:return '\n\n**'+text.strip()+'**\n\n'
        anchor=el.get('id')
        prefix=f'\n\n<a id="{anchor}"></a>\n\n' if anchor and anchor!='content' else ''
        return prefix+super().convert_div(el,text,parent_tags)
    def convert_table(self,el,text,parent_tags):
        if 'tableblock' not in el.get('class',[]) and 'hdlist' not in el.parent.get('class',[]):
            return super().convert_table(el,text,parent_tags)
        table=copy.deepcopy(el)
        for c in table.select('col,colgroup'):c.decompose()
        for tag in [table]+list(table.find_all(True)):
            if tag.name=='span' and 'monospaced' in tag.get('class',[]):tag.name='code'
            for attr in list(tag.attrs):
                if attr not in {'rowspan','colspan','href','src','alt','id'}:del tag[attr]
            if tag.get('href'):tag['href']=link(tag['href'],self.page['path'],self.page['source'])
            if tag.name=='img':tag['src']=link(tag['src'],self.page['path'],self.page['source'])
        return '\n\n'+str(table)+'\n\n'

def guide_pages():
    soup=translated_soup(ROOT/'source/prepared/pve-admin-guide.html')
    body=soup.select_one('#content');chapters=[]
    for i,section in enumerate(body.select(':scope > .sect1'),1):
        heading=section.find(re.compile('^h[1-6]$'),recursive=False)
        anchor=heading.get('id',f'chapter-{i}')
        folder=Path(f'guide/{i:02d}-{anchor.strip("_").replace("chapter_","").replace("_","-")}')
        page=add_page(folder/'README.md',section,'pve-admin-guide.html',shift=-1)
        page['children']=[];chapters.append(page)
    FILE_DEFAULTS['pve-admin-guide.html']=chapters[0]['path']
    names=['pve-intro','pve-installation','sysadmin','pve-gui','pvecm','pmxcfs','pvesm','pveceph','pvesr','qm','pct','pvesdn','pve-firewall','pveum','ha-manager','vzdump','notifications']
    for name,page in zip(names,chapters):CHAPTER_DEFAULTS[f'chapter-{name}.html']=page['path']
    for name,anchor in [('pve-faq','_frequently_asked_questions_2'),('pve-bibliography','_bibliography'),('pvesh','_useful_command_line_tools')]:
        match=next((p for p in chapters if p['node'].find(id=anchor)),None)
        if match:CHAPTER_DEFAULTS[f'chapter-{name}.html']=match['path']
    footnotes=body.select_one('#footnotes')
    if footnotes and footnotes.get_text(strip=True):
        add_page(Path('guide/footnotes.md'),footnotes,'pve-admin-guide.html','脚注')
    elif (DOCS/'guide/footnotes.md').exists():
        (DOCS/'guide/footnotes.md').unlink()
    return chapters

def manual_pages():
    pages=[]
    for path in sorted((ROOT/'source/prepared').glob('*.html')):
        if path.name=='pve-admin-guide.html':continue
        node=translated_soup(path).select_one('#content')
        title=path.name.replace('.html','').replace('.1','(1)').replace('.5','(5)').replace('.8','(8)')
        target=Path('reference')/(path.stem.replace('.','-')+'.md')
        node.insert(0,BeautifulSoup(f'<h1>{html.escape(title)}</h1>','html.parser'))
        page=add_page(target,node,path.name,title)
        FILE_DEFAULTS[path.name]=target;pages.append(page)
    return pages

def schema_translated(x):
    if isinstance(x,list):return [schema_translated(v) for v in x]
    if not isinstance(x,dict):return x
    out={k:schema_translated(v) for k,v in x.items() if not (k.startswith('_') and k.endswith('_i18n'))}
    for field in ('description','verbose_description','title'):
        if x.get('_'+field+'_i18n'):
            out[field]=BeautifulSoup(restore(x['_'+field+'_i18n']),'html.parser').get_text()
    return out

def write(path,text):
    full=DOCS/path;full.parent.mkdir(parents=True,exist_ok=True);full.write_text(text.rstrip()+'\n')

def cell(value):
    return html.escape(str(value),quote=False).replace('|',r'\|').replace('\r','').replace('\n','<br>')

def api_json(value,max_width=160):
    """Format generated API JSON compactly without changing any JSON token.

    Keep larger containers indented, but fit small containers and adjacent simple
    fields on one line. Count CJK characters as two columns. A single long key or
    string stays intact even when it exceeds the preferred width.
    """
    def width(text):
        return sum(0 if unicodedata.combining(char) or unicodedata.category(char)=='Cf'
                   else 2 if unicodedata.east_asian_width(char) in 'WF' else 1
                   for char in text)
    def emit(node,depth,prefix,trailing=False):
        comma=',' if trailing else ''
        flat=json.dumps(node,ensure_ascii=False,separators=(', ',': '))
        if width(prefix+flat+comma)<=max_width or not isinstance(node,(dict,list)) or not node:
            return [prefix+flat+comma]
        is_object=isinstance(node,dict)
        lines=[prefix+('{' if is_object else '[')]
        entries=list(node.items()) if is_object else list(enumerate(node))
        indent='  '*(depth+1);pending=''
        for index,(key,child) in enumerate(entries):
            child_prefix=indent+(json.dumps(key,ensure_ascii=False)+': ' if is_object else '')
            child_lines=emit(child,depth+1,child_prefix,index<len(entries)-1)
            if len(child_lines)==1:
                addition=child_lines[0].lstrip()
                if pending and width(pending+' '+addition)<=max_width:
                    pending+=' '+addition
                else:
                    if pending:lines.append(pending)
                    pending=child_lines[0]
            else:
                if pending:lines.append(pending);pending=''
                lines.extend(child_lines)
        if pending:lines.append(pending)
        lines.append('  '*depth+('}' if is_object else ']')+comma)
        return lines
    return '\n'.join(emit(value,0,''))

def api_inline_json(value):
    """Keep scalar JSON literal text intact inside a Markdown code span."""
    literal=json.dumps(value,ensure_ascii=False)
    fence='`'*max(1,max((len(match[0])+1 for match in re.finditer(r'`+',literal)),default=1))
    return fence+literal+fence

def api_parameter_row(key,value):
    """Retain every former five-column field in a two-column API row."""
    typ=cell(value.get('type',''))
    required='是' if not value.get('optional',False) else '否'
    default=cell(json.dumps(value['default'],ensure_ascii=False)) if 'default' in value else '—'
    description=value.get('verbose_description') or value.get('description','')
    if value.get('enum') is not None:
        description+='；可选值：'+', '.join('`'+str(item)+'`' for item in value['enum'])
    definition=f'类型：{typ}；必填：{required}；默认值：{default}<br>'+cell(description)
    return f'| `{key}` | {definition} |'

def api_pages():
    # Plain code blocks keep full JSON readable without expensive token highlighting in GitBook.
    schema=json.loads((ROOT/'source/api/schema.json').read_text());groups=[];operations=0
    def walk(nodes,parent=''):
        nonlocal operations
        for n in nodes:
            path=n.get('path') or (parent+'/'+n.get('text',''))
            if n.get('info'):
                methods=n['info'];slug=re.sub('[^a-zA-Z0-9-]+','-',path).strip('-').lower() or 'root'
                target=groups[-1]['path']
                anchor='api-'+slug+'-'+hashlib.sha256(path.encode()).hexdigest()[:8]
                API_LINKS[path]=(target,anchor)
                body=[f'## `{path}` <a href="#{anchor}" id="{anchor}"></a>\n',f'原始接口路径：`{path}`。\n']
                for method,original in methods.items():
                    operations+=1;info=schema_translated(original)
                    method_anchor=anchor+'-'+method.lower()
                    body += [f'### {method} `{path}` <a href="#{method_anchor}" id="{method_anchor}"></a>\n',html.escape(info.get('verbose_description') or info.get('description',''),quote=False)+'\n']
                    if info.get('name'):body.append('**方法标识：** `'+info['name']+'`\n')
                    for field,label in [('permissions','权限'),('allowtoken','允许 API 令牌'),('protected','受保护接口'),('proxyto','代理目标')]:
                        if field in info:
                            if isinstance(info[field],(dict,list)):
                                body += [f'**{label}**\n', '```text\n'+api_json(info[field])+'\n```\n']
                            else:
                                body.append(f'**{label}：** '+api_inline_json(info[field])+'\n')
                    params=info.get('parameters',{});props=params.get('properties',{})
                    body.append(f'#### 请求参数 <a href="#{method_anchor}-parameters" id="{method_anchor}-parameters"></a>\n')
                    if props:
                        body+=['| 参数 | 定义与说明 |','| --- | --- |']
                        for key,v in props.items():
                            body.append(api_parameter_row(key,v))
                        body += ['\n<details>\n<summary>完整请求参数结构</summary>\n','```text\n'+api_json(params)+'\n```\n','</details>\n']
                    else:body+=['此操作没有请求参数。\n']
                    body += [f'#### 返回值 <a href="#{method_anchor}-returns" id="{method_anchor}-returns"></a>\n','```text\n'+api_json(info.get('returns',{}))+'\n```\n']
                    extras={k:v for k,v in info.items() if k not in {'method','name','description','parameters','returns','permissions','allowtoken','protected','proxyto'}}
                    if extras:body+=['<details>\n<summary>其他接口元数据</summary>\n','```text\n'+api_json(extras)+'\n```\n','</details>\n']
                body.append(f'来源：[官方 API 浏览器]({BASE}api-viewer/index.html#{path})。')
                groups[-1]['body'].append('\n'.join(body));groups[-1]['pages'].append((path,target,anchor))
            walk(n.get('children',[]),path)
    for i,n in enumerate(schema,1):
        groups.append({'name':n.get('text') or n.get('path','API'),'pages':[],'body':[],'path':Path('api')/f'group-{i}.md'});walk([n])
    text='# API 参考\n\n本节根据官方 API 浏览器的同一快照生成，包含 **'+str(operations)+' 个接口操作**。描述翻译为中文，接口路径、方法、参数、类型、约束和默认值保持原值。\n\n'
    for group in groups:
        text+='## '+group['name']+'\n\n'
        for name,path,anchor in group['pages']:text+=f'- [`{name}`]({relpath(path,Path("api/README.md"))}#{anchor})\n'
        text+='\n'
        content='# '+group['name']+' API\n\n本章包含此资源组的全部接口，按路径和 HTTP 方法在同一页展开。接口路径、方法、参数、类型、约束和默认值保持原值。\n\n'
        content+='\n\n'.join(group['body'])
        write(group['path'],content)
    write(Path('api/README.md'),text)
    return groups,operations

def main():
    p=argparse.ArgumentParser();p.add_argument('--allow-partial',action='store_true');args=p.parse_args()
    missing=set(UNITS)-set(TRANSLATIONS)
    if missing and not args.allow_partial:raise SystemExit(f'{len(missing)} untranslated units; refusing release render')
    # All these files were generated by the previous split-page renderer.
    for stale in (DOCS/'guide').glob('*/*.md'):
        if stale.name!='README.md':stale.unlink()
    for stale in (DOCS/'api').glob('*.md'):stale.unlink()
    chapters=guide_pages();manuals=manual_pages()
    groups,operations=api_pages()
    for page in PAGES:
        text=GitBookMarkdown(page).convert(str(page['node'])).strip()
        if not text.startswith('# '):text='# '+page['title']+'\n\n'+text
        if page.get('children'):
            text+='\n\n## 本章内容\n\n'+'\n'.join(f'- [{c["title"]}]({relpath(c["path"],page["path"])})' for c in page['children'])
        text+='\n\n---\n\n来源：[Proxmox VE 官方文档]('+BASE+page['source']+') · 版本 9.2.13 · 非官方中文翻译。'
        write(page['path'],text)
    state='翻译校验预览：仍含未完成翻译的原文。' if missing else '中文译文已完成自动完整性与格式校验。'
    intro=f'''# Proxmox VE 中文文档

本书是 [Proxmox VE 官方文档]({BASE})的非官方简体中文译本，基于 **9.2.13** 版本，原文日期 **2026 年 9 月 24 日**，获取日期 **2026 年 11 月 10 日**。

{state}译文由 AI 辅助生成；尚未经 Proxmox 官方审核。原始命令、配置、参数、链接及截图保持原值。截图中的英文界面文字按原图保留。

## 阅读导航

- [管理手册](guide/README.md)：安装、系统管理、集群、存储、虚拟机、容器、网络、防火墙、权限、高可用、备份与通知。
- [命令与配置参考](reference/README.md)：入口列出的全部 29 份参考手册。
- [API 参考](api/README.md)：全部 {operations} 个接口操作及请求参数、返回结构与权限信息。
- [术语表](glossary.md)
- [版权、翻译说明与许可证](copyright.md)
- [GNU 自由文档许可证英文原文](license-original.md)

## 开源与离线阅读

- [完整源码、译文映射与构建脚本](https://github.com/Thweki/pve-docs-zh-cn)
- [EPUB、PDF、离线 HTML 与源码版本下载](https://github.com/Thweki/pve-docs-zh-cn-releases/releases)

## 版本与来源

文档正文、章节层级、表格、代码示例、提示框和图片均取自上述官方快照。管理手册按原始章节组织，每章及其全部子节在同一页显示；命令参考每篇一页，API 按资源组整组同页。原站交叉引用改写为本书内部链接。标题和书签按 GitBook 规则转换为可跳转的章节锚点，脚注整理为各章末尾的注释。

本书不代表 Proxmox Server Solutions GmbH 对译文的认可。中文译文与英文原文有歧义时，请对照每页底部的官方来源。
'''
    write(Path('README.md'),intro)
    write(Path('guide/README.md'),'# 管理手册\n\n'+'\n'.join(f'- [{c["title"]}]({relpath(c["path"],Path("guide/README.md"))})' for c in chapters))
    write(Path('reference/README.md'),'# 命令与配置参考\n\n'+'\n'.join(f'- [{c["title"]}]({relpath(c["path"],Path("reference/README.md"))})' for c in manuals))
    summary=['# 目录\n','- [Proxmox VE 中文文档](README.md "首页")','- [管理手册](guide/README.md)']
    for c in chapters:
        summary.append(f'  - [{c["title"]}]({c["path"]})')
        for child in c.get('children',[]):summary.append(f'    - [{child["title"]}]({child["path"]})')
    if (DOCS/'guide/footnotes.md').exists():summary.append('  - [脚注](guide/footnotes.md)')
    summary+=['- [命令与配置参考](reference/README.md)']+[f'  - [{m["title"]}]({m["path"]})' for m in manuals]
    summary+=['- [API 参考](api/README.md)']
    # Resource groups keep a large API reference navigable in GitBook.
    for g in groups:
        summary.append(f'  - [{g["name"]} API]({g["path"]})')
    summary+=['- [术语表](glossary.md)','- [版权与翻译说明](copyright.md)','- [GNU 自由文档许可证英文原文](license-original.md)']
    write(Path('SUMMARY.md'),'\n'.join(summary))
    report={'translation_units':len(UNITS),'translated_units':len(TRANSLATIONS),'missing_units':len(missing),'guide_pages':len([p for p in PAGES if p['source']=='pve-admin-guide.html']),'manuals':len(manuals),'api_operations':operations,'pages':len(list(DOCS.rglob('*.md')))}
    (ROOT/'reports/render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    (ROOT/'work/anchor-map.json').write_text(json.dumps({f'{src}#{anchor}':str(path)+(('#'+dest) if dest else '') for (src,anchor),(path,dest) in ANCHORS.items()},ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
