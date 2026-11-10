"""Freeze the published PVE documentation and extract deduplicated translation units.

Translations modify inline prose only. HTML structure, code, URLs, anchors, and
original images are never passed to the translator as editable material.
"""
from __future__ import annotations
import base64, concurrent.futures, hashlib, html, json, mimetypes, re, subprocess, time
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://pve.proxmox.com/pve-docs/'
UNITS = {}
ASSETS = {}
BLOCKS = {'p','h1','h2','h3','h4','h5','h6','dt','dd','li','td','th','caption'}
SKIP = {'script','style','pre','code','svg','math'}
TOKEN = re.compile(r'⟦\d+⟧')
LITERALS = re.compile(r'https?://[^\s<>]+|(?<![\w])/(?:[\w.{}+@%:-]+/)*[\w.{}+@%:-]+|--[A-Za-z][\w-]*|\b[\w+-]+\.(?:conf|cfg|json|yaml|yml|service|socket|timer|iso|img|qcow2|vmdk|raw|sh|pem|key|crt|po)\b|\b[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]+\b|`[^`]+`')

def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()[:20]

def fetch(name):
    path = ROOT/'source/html'/name
    if not path.exists():
        for attempt in range(4):
            try:
                r = requests.get(urljoin(BASE,name), timeout=90)
                r.raise_for_status()
                path.parent.mkdir(parents=True,exist_ok=True)
                path.write_bytes(r.content)
                break
            except requests.RequestException:
                if attempt == 3: raise
                time.sleep(2*(attempt+1))
    return name

def asset(src, alt):
    if src in ASSETS: return ASSETS[src]['path']
    if src.startswith('data:'):
        head, data = src.split(',',1)
        mime = head.split(';')[0][5:]
        if ';base64' in head: content = base64.b64decode(data)
        else:
            from urllib.parse import unquote_to_bytes
            content = unquote_to_bytes(data)
    else:
        path=ROOT/'source/raw-assets'/digest(src)
        if not path.exists():download_asset(src)
        content=path.read_bytes();mime=path.with_suffix('.mime').read_text()
    ext={'image/png':'png','image/jpeg':'jpg','image/svg+xml':'svg','image/gif':'gif'}.get(mime,'bin')
    sha=hashlib.sha256(content).hexdigest()
    name=re.sub(r'[^a-z0-9]+','-',alt.lower()).strip('-')[:60] or 'image'
    path=f'assets/{name}-{sha[:12]}.{ext}'
    (ROOT/'docs'/path).write_bytes(content)
    ASSETS[src]={'path':path,'sha256':sha,'bytes':len(content),'alt':alt,'mime':mime}
    return path

def download_asset(src):
    path=ROOT/'source/raw-assets'/digest(src)
    if not path.exists():
        path.parent.mkdir(parents=True,exist_ok=True)
        subprocess.run(['curl','--fail','--silent','--show-error','--retry','3','--max-time','60',
                        urljoin(BASE,src),'-o',str(path)],check=True)
        path.with_suffix('.mime').write_text(mimetypes.guess_type(src)[0] or 'application/octet-stream')
    return src

def protect_element(el):
    """Serialize inline content, with markup and literal/code values protected."""
    fragments=[]
    def token(value):
        marker=f'⟦{len(fragments)}⟧';fragments.append(value);return marker
    def visit(n):
        if isinstance(n,NavigableString):
            text=re.sub(r'\s+',' ',str(n))
            # Bare links are executable destinations too; keep them byte-for-byte.
            return LITERALS.sub(lambda m:token(html.escape(m[0],quote=False)),text)
        if not isinstance(n,Tag):return ''
        if n.name in {'code','tt','kbd','samp','img','br','sup'} or 'monospaced' in n.get('class',[]):
            return token(str(n))
        raw=str(n);opening=raw[:raw.index('>')+1]
        return token(opening)+''.join(visit(c) for c in n.children)+token(f'</{n.name}>')
    text=''.join(visit(c) for c in el.children).strip()
    return text,fragments

def add_unit(el, attribute=None):
    if attribute:
        value=el.get(attribute,'');text=value;fragments=[];canonical=f'attr:{attribute}:{value}'
    else:
        text,fragments=protect_element(el);canonical=str(el.decode_contents())
    prose=TOKEN.sub('',text)
    if not re.search(r'[a-zA-Z]{2}',prose):return
    # The English legal license is intentionally retained verbatim as well.
    key='u'+digest(canonical+'\n'+text)
    UNITS.setdefault(key,{'id':key,'text':text,'fragments':fragments})
    el['data-i18n-'+attribute if attribute else 'data-i18n']=key

def annotate(node):
    if not isinstance(node,Tag):return
    if node.name in SKIP or 'monospaced' in node.get('class',[]):return
    if node.name=='img':
        add_unit(node,'alt');return
    if (node.name in BLOCKS or 'title' in node.get('class',[])) and not node.find(list(BLOCKS)) and not node.find('pre'):
        add_unit(node)
        # Alt text is separately discoverable even inside a prose unit.
        return
    for child in list(node.children):
        if isinstance(child,Tag):annotate(child)
        elif isinstance(child,NavigableString) and re.search(r'[A-Za-z]{2}',str(child)):
            wrapper=BeautifulSoup('<span></span>','html.parser').span
            child.replace_with(wrapper);wrapper.append(child);add_unit(wrapper)

def prepare_html(name):
    soup=BeautifulSoup((ROOT/'source/html'/name).read_text(),'html.parser')
    body=soup.select_one('#content')
    if body is None:raise ValueError(f'No content: {name}')
    for el in body.select('a.headerlink,a.to-top,script,style'):el.decompose()
    for img in body.select('img'):
        img['src']=asset(img['src'],img.get('alt','image'))
    for section in body.select(':scope > .sect1'):
        annotate(section)
    if not body.select(':scope > .sect1'):annotate(body)
    footnotes=soup.select_one('#footnotes')
    if footnotes:
        annotate(footnotes);body.append(footnotes.extract())
    path=ROOT/'source/prepared'/name;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(str(body))
    return {'file':name,'bytes':(ROOT/'source/html'/name).stat().st_size,
            'sha256':hashlib.sha256((ROOT/'source/html'/name).read_bytes()).hexdigest(),
            'words':len(re.findall(r'\b\w+\b',body.get_text(' '))),
            'images':len(body.select('img')),'code_blocks':len(body.select('pre')),
            'tables':len(body.select('table.tableblock')),'hints':len(body.select('.admonitionblock'))}

def prepare_api():
    s=(ROOT/'source/api/apidoc.js').read_text()
    schema,_=json.JSONDecoder().raw_decode(s[s.index('['):])
    count=0
    def walk(x):
        nonlocal count
        if isinstance(x,dict):
            for k,v in list(x.items()):
                if k=='description' and isinstance(v,str) and re.search('[A-Za-z]{2}',v):
                    # Treat documentation descriptions as prose, not schema syntax.
                    el=BeautifulSoup('<p></p>','html.parser').p;el.string=v
                    add_unit(el)
                    if el.get('data-i18n'):x['_description_i18n']=el['data-i18n'];count+=1
                else:walk(v)
        elif isinstance(x,list):
            for v in x:walk(v)
    walk(schema)
    (ROOT/'source/api/schema.json').write_text(json.dumps(schema,ensure_ascii=False,indent=2))
    return count

def main():
    index=BeautifulSoup((ROOT/'source/html/index.html').read_text(),'html.parser')
    links=sorted({a['href'] for a in index.select('a[href]') if re.fullmatch(r'[\w.-]+\.html',a['href']) and not a['href'].startswith('chapter-')})
    if 'pve-admin-guide.html' not in links:raise ValueError('Missing administration guide')
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for name in pool.map(fetch,links):print('fetched',name,flush=True)
    remote_images=set()
    for name in links:
        raw=BeautifulSoup((ROOT/'source/html'/name).read_text(),'html.parser')
        remote_images.update(img['src'] for img in raw.select('img[src]') if not img['src'].startswith('data:'))
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for i,src in enumerate(pool.map(download_asset,sorted(remote_images))):
            if i%10==0:print('assets',i+1,'/',len(remote_images),flush=True)
    reports=[]
    for name in links:
        reports.append(prepare_html(name));print('prepared',name,'units',len(UNITS),flush=True)
    api_descriptions=prepare_api()
    (ROOT/'work/units.json').write_text(json.dumps(UNITS,ensure_ascii=False,indent=2))
    (ROOT/'source/assets-manifest.json').write_text(json.dumps(list(ASSETS.values()),ensure_ascii=False,indent=2))
    (ROOT/'source/manifest.json').write_text(json.dumps({'base_url':BASE,'version':'9.2.13','snapshot_date':'2026-11-10','documents':reports,'api_descriptions':api_descriptions},ensure_ascii=False,indent=2))
    print('TOTAL',len(UNITS),'unique units,',sum(len(re.findall(r'\w+',u['text'])) for u in UNITS.values()),'words,',len(ASSETS),'assets',flush=True)

if __name__=='__main__':main()
