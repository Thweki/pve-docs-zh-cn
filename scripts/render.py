"""Render translated, structurally preserved HTML into GitBook-native Markdown."""
from __future__ import annotations
import argparse, collections, copy, hashlib, html, json, os, re
from pathlib import Path
from urllib.parse import urljoin, urlsplit, unquote
from bs4 import BeautifulSoup, NavigableString
from markdownify import MarkdownConverter
from translate import validate

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
BASE='https://pve.proxmox.com/pve-docs/'
UNITS=json.loads((ROOT/'work/units.json').read_text())
TRANSLATIONS={}
if (ROOT/'work/translations.jsonl').exists():
    for line in (ROOT/'work/translations.jsonl').read_text().splitlines():
        if line.strip():TRANSLATIONS.update(json.loads(line))
TRANSLATIONS={k:v for k,v in TRANSLATIONS.items() if k in UNITS and not validate(UNITS[k]['text'],v)}
PAGES=[];ANCHORS={};FILE_DEFAULTS={};CHAPTER_DEFAULTS={};API_LINKS={}

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

def add_page(path,node,source,title=None,shift=0):
    heading=node.find(re.compile('^h[1-6]$'))
    title=title or (plain_heading(heading) if heading else path.stem)
    page={'path':path,'node':node,'source':source,'title':title,'shift':shift}
    PAGES.append(page)
    for el in node.select('[id]'):
        ANCHORS[(source,el['id'])]=(path,el['id'])
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
        if fragment in API_LINKS:return relpath(API_LINKS[fragment],current)
        return urljoin(BASE,href)
    if fragment:
        match=ANCHORS.get((target,fragment))
        if not match and target.startswith('chapter-'):
            match=ANCHORS.get(('pve-admin-guide.html',fragment))
        if match:
            page,anchor=match
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
    def convert_hN(self,n,el,text,parent_tags):
        n=max(1,min(6,n+self.page['shift']))
        title=re.sub(r'\s+',' ',text.strip())
        anchor=el.get('id')
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
        children=[]
        for j,child in enumerate(section.select(':scope > .sectionbody > .sect2'),1):
            h=child.find('h3',recursive=False)
            slug=(h.get('id') if h else f'section-{j}').strip('_').replace('_','-')
            path=folder/f'{j:02d}-{slug[:90]}.md'
            child.extract();children.append(add_page(path,child,'pve-admin-guide.html',shift=-2))
        page=add_page(folder/'README.md',section,'pve-admin-guide.html',shift=-1)
        page['children']=children;chapters.append(page)
    FILE_DEFAULTS['pve-admin-guide.html']=chapters[0]['path']
    names=['pve-intro','pve-installation','sysadmin','pve-gui','pvecm','pmxcfs','pvesm','pveceph','pvesr','qm','pct','pvesdn','pve-firewall','pveum','ha-manager','vzdump','notifications']
    for name,page in zip(names,chapters):CHAPTER_DEFAULTS[f'chapter-{name}.html']=page['path']
    for name,anchor in [('pve-faq','_frequently_asked_questions_2'),('pve-bibliography','_bibliography'),('pvesh','_useful_command_line_tools')]:
        match=next((p for p in chapters if p['node'].find(id=anchor)),None)
        if match:CHAPTER_DEFAULTS[f'chapter-{name}.html']=match['path']
    footnotes=body.select_one('#footnotes')
    if footnotes:add_page(Path('guide/footnotes.md'),footnotes,'pve-admin-guide.html','脚注')
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
    out={k:schema_translated(v) for k,v in x.items() if not k.startswith('_description_i18n')}
    if x.get('_description_i18n'):
        out['description']=BeautifulSoup(restore(x['_description_i18n']),'html.parser').get_text()
    return out

def write(path,text):
    full=DOCS/path;full.parent.mkdir(parents=True,exist_ok=True);full.write_text(text.rstrip()+'\n')

def cell(value):
    return html.escape(str(value),quote=False).replace('|',r'\|').replace('\r','').replace('\n','<br>')

def api_pages():
    schema=json.loads((ROOT/'source/api/schema.json').read_text());groups=[];operations=0
    def walk(nodes,parent=''):
        nonlocal operations
        for n in nodes:
            path=n.get('path') or (parent+'/'+n.get('text',''))
            if n.get('info'):
                methods=n['info'];slug=re.sub('[^a-zA-Z0-9-]+','-',path).strip('-').lower() or 'root'
                target=Path('api')/f'{slug}-{hashlib.sha256(path.encode()).hexdigest()[:8]}.md'
                API_LINKS[path]=target
                body=[f'# `{path}`\n',f'原始接口路径：`{path}`。\n','方法、参数名、类型、默认值和枚举值与官方规范一致。\n']
                for method,original in methods.items():
                    operations+=1;info=schema_translated(original)
                    body += [f'## {method} `{path}`\n',html.escape(info.get('description',''),quote=False)+'\n']
                    if info.get('name'):body.append('**方法标识：** `'+info['name']+'`\n')
                    for field,label in [('permissions','权限'),('allowtoken','允许 API 令牌'),('protected','受保护接口'),('proxyto','代理目标')]:
                        if field in info:
                            body += [f'**{label}**\n', '```json\n'+json.dumps(info[field],ensure_ascii=False,indent=2)+'\n```\n']
                    params=info.get('parameters',{});props=params.get('properties',{})
                    body.append('### 请求参数\n')
                    if props:
                        body+=['| 参数 | 类型 | 必填 | 默认值 | 说明 |','| --- | --- | --- | --- | --- |']
                        for key,v in props.items():
                            typ=v.get('type','')
                            required=not v.get('optional',False)
                            desc=v.get('description','')
                            if v.get('enum') is not None:desc+='；可选值：'+', '.join('`'+str(z)+'`' for z in v['enum'])
                            body.append('| '+' | '.join([f'`{key}`',cell(typ),'是' if required else '否',cell(json.dumps(v['default'],ensure_ascii=False)) if 'default' in v else '—',cell(desc)])+' |')
                        body += ['\n<details>\n<summary>完整请求参数结构</summary>\n','```json\n'+json.dumps(params,ensure_ascii=False,indent=2)+'\n```\n','</details>\n']
                    else:body+=['此操作没有请求参数。\n']
                    body += ['### 返回值\n','```json\n'+json.dumps(info.get('returns',{}),ensure_ascii=False,indent=2)+'\n```\n']
                    extras={k:v for k,v in info.items() if k not in {'method','name','description','parameters','returns','permissions','allowtoken','protected','proxyto'}}
                    if extras:body+=['<details>\n<summary>其他接口元数据</summary>\n','```json\n'+json.dumps(extras,ensure_ascii=False,indent=2)+'\n```\n','</details>\n']
                body.append(f'来源：[官方 API 浏览器]({BASE}api-viewer/index.html#{path})。')
                write(target,'\n'.join(body));groups[-1]['pages'].append((path,target))
            walk(n.get('children',[]),path)
    for n in schema:
        groups.append({'name':n.get('text') or n.get('path','API'),'pages':[]});walk([n])
    text='# API 参考\n\n本节根据官方 API 浏览器的同一快照生成，包含 **'+str(operations)+' 个接口操作**。描述翻译为中文，接口路径、方法、参数、类型、约束和默认值保持原值。\n\n'
    for group in groups:
        text+='## '+group['name']+'\n\n'
        for name,path in group['pages']:text+=f'- [`{name}`]({relpath(path,Path("api/README.md"))})\n'
        text+='\n'
    write(Path('api/README.md'),text)
    return groups,operations

def main():
    p=argparse.ArgumentParser();p.add_argument('--allow-partial',action='store_true');args=p.parse_args()
    missing=set(UNITS)-set(TRANSLATIONS)
    if missing and not args.allow_partial:raise SystemExit(f'{len(missing)} untranslated units; refusing release render')
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

## 版本与来源

文档正文、章节层级、表格、代码示例、提示框和图片均取自上述官方快照。为了在 GitBook 中阅读，将长章节拆分为子页面，并将原站交叉引用改写为本书内部链接。原始标题锚点予以保留。

本书不代表 Proxmox Server Solutions GmbH 对译文的认可。中文译文与英文原文有歧义时，请对照每页底部的官方来源。
'''
    write(Path('README.md'),intro)
    write(Path('guide/README.md'),'# 管理手册\n\n'+'\n'.join(f'- [{c["title"]}]({relpath(c["path"],Path("guide/README.md"))})' for c in chapters))
    write(Path('reference/README.md'),'# 命令与配置参考\n\n'+'\n'.join(f'- [{c["title"]}]({relpath(c["path"],Path("reference/README.md"))})' for c in manuals))
    summary=['# 目录\n','- [首页](README.md)','- [管理手册](guide/README.md)']
    for c in chapters:
        summary.append(f'  - [{c["title"]}]({c["path"]})')
        for child in c.get('children',[]):summary.append(f'    - [{child["title"]}]({child["path"]})')
    if (DOCS/'guide/footnotes.md').exists():summary.append('  - [脚注](guide/footnotes.md)')
    summary+=['- [命令与配置参考](reference/README.md)']+[f'  - [{m["title"]}]({m["path"]})' for m in manuals]
    summary+=['- [API 参考](api/README.md)']
    # Resource groups keep a large API reference navigable in GitBook.
    for i,g in enumerate(groups):
        groupfile=Path('api')/f'group-{i+1}.md'
        write(groupfile,'# '+g['name']+'\n\n'+'\n'.join(f'- [`{name}`]({relpath(path,groupfile)})' for name,path in g['pages']))
        summary.append(f'  - [{g["name"]}]({groupfile})')
        summary += [f'    - [{name}]({path})' for name,path in g['pages']]
    summary+=['- [术语表](glossary.md)','- [版权与翻译说明](copyright.md)','- [GNU 自由文档许可证英文原文](license-original.md)']
    write(Path('SUMMARY.md'),'\n'.join(summary))
    report={'translation_units':len(UNITS),'translated_units':len(TRANSLATIONS),'missing_units':len(missing),'guide_pages':len([p for p in PAGES if p['source']=='pve-admin-guide.html']),'manuals':len(manuals),'api_operations':operations,'pages':len(list(DOCS.rglob('*.md')))}
    (ROOT/'reports/render.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    (ROOT/'work/anchor-map.json').write_text(json.dumps({f'{src}#{anchor}':str(path)+'#'+dest for (src,anchor),(path,dest) in ANCHORS.items()},ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
