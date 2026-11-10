"""Check book completeness, source-code fidelity, images, links, and navigation."""
from __future__ import annotations
import argparse, collections, hashlib, json, re, struct, zlib
from pathlib import Path
from urllib.parse import unquote, urlsplit
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from render import ROOT,DOCS,UNITS,TRANSLATIONS,translated_soup,schema_translated

def check_image(path,mime):
    data=path.read_bytes()
    if mime=='image/png':
        if data[:8]!=b'\x89PNG\r\n\x1a\n':raise ValueError('invalid PNG signature')
        pos=8;compressed=[];ended=False
        while pos<len(data):
            size=struct.unpack('>I',data[pos:pos+4])[0];kind=data[pos+4:pos+8]
            chunk=data[pos+8:pos+8+size];crc=struct.unpack('>I',data[pos+8+size:pos+12+size])[0]
            if zlib.crc32(kind+chunk)&0xffffffff!=crc:raise ValueError('invalid PNG chunk CRC')
            if kind==b'IDAT':compressed.append(chunk)
            if kind==b'IEND':ended=True;break
            pos+=12+size
        if not ended:raise ValueError('missing PNG IEND')
        zlib.decompress(b''.join(compressed))
        return dict(zip(('width','height'),struct.unpack('>II',data[16:24])))
    if mime=='image/svg+xml':
        from xml.etree import ElementTree
        root=ElementTree.fromstring(data)
        if not root.tag.endswith('svg'):raise ValueError('invalid SVG root')
        return {'width':root.get('width'),'height':root.get('height')}
    raise ValueError('unexpected image type '+mime)

def technical_schema(x):
    if isinstance(x,list):return [technical_schema(v) for v in x]
    if not isinstance(x,dict):return x
    return {k:technical_schema(v) for k,v in x.items()
            if not (k.startswith('_') and k.endswith('_i18n'))
            and not (k in {'description','verbose_description','title'} and isinstance(v,str))}

def main():
    p=argparse.ArgumentParser();p.add_argument('--allow-partial',action='store_true');args=p.parse_args()
    md=MarkdownIt('commonmark',{'html':True}).enable('table')
    errors=[];warnings=[];files=sorted(DOCS.rglob('*.md'));anchors={};heading_anchors={};links=[]
    code=collections.Counter();html_tables=0;hints=0;image_links=[]
    for file in files:
        text=file.read_text();tokens=md.parse(text)
        ids=set();heading_ids=[];in_heading=False
        for token in tokens:
            if token.type=='heading_open':in_heading=True
            if token.type=='heading_close':in_heading=False
            if token.type=='fence' and ('guide' in file.parts or 'reference' in file.parts):
                code[token.content.rstrip('\n')]+=1
            if token.type in {'html_block','html_inline'}:
                soup=BeautifulSoup(token.content,'html.parser')
                for el in soup.select('[id]'):ids.add(el['id'])
                for el in soup.select('[href]'):links.append((file,el['href']))
                for el in soup.select('img[src]'):links.append((file,el['src']));image_links.append((file,el['src']))
                if 'guide' in file.parts or 'reference' in file.parts:
                    for el in soup.select('pre'):code[el.get_text().rstrip('\n')]+=1
                    html_tables+=len(soup.select('table'))
            for child in token.children or []:
                if child.type=='link_open':links.append((file,child.attrGet('href')))
                if child.type=='image':
                    links.append((file,child.attrGet('src')));image_links.append((file,child.attrGet('src')))
                if child.type=='html_inline':
                    s=BeautifulSoup(child.content,'html.parser')
                    for el in s.select('[id]'):
                        ids.add(el['id'])
                        if in_heading:heading_ids.append(el['id'])
                    for el in s.select('[href]'):links.append((file,el['href']))
        anchors[file.resolve()]=ids
        heading_anchors[file.resolve()]=set(heading_ids)
        if len(set(heading_ids))!=len(heading_ids):errors.append(f'duplicate heading id: {file.relative_to(DOCS)}')
        if re.search(r'⟦\d+⟧',text):errors.append(f'unrestored placeholder: {file.relative_to(DOCS)}')
        if text.count('{% hint ')!=text.count('{% endhint %}'):errors.append(f'unbalanced hints: {file.relative_to(DOCS)}')
        if 'guide' in file.parts or 'reference' in file.parts:hints+=text.count('{% hint ')
    for file,href in links:
        if not href:continue
        parsed=urlsplit(href)
        if parsed.scheme or parsed.netloc:continue
        path=unquote(parsed.path);fragment=unquote(parsed.fragment)
        target=(file.parent/path).resolve() if path else file.resolve()
        if not target.exists():errors.append(f'broken file link: {file.relative_to(DOCS)} -> {href}')
        elif fragment and target.suffix=='.md' and fragment not in anchors.get(target,set()):
            errors.append(f'broken anchor: {file.relative_to(DOCS)} -> {href}')
        elif fragment and target.suffix=='.md' and fragment not in heading_anchors.get(target,set()):
            errors.append(f'anchor is not a GitBook heading: {file.relative_to(DOCS)} -> {href}')
    expected_code=collections.Counter();expected_tables=0;expected_hints=0;expected_images=0
    for path in sorted((ROOT/'source/prepared').glob('*.html')):
        original=BeautifulSoup(path.read_text(),'html.parser');translated=translated_soup(path)
        code_before=[el.get_text() for el in original.select('pre')]
        code_after=[el.get_text() for el in translated.select('pre')]
        if code_before!=code_after:errors.append('translated code differs: '+path.name)
        for selector,attr in [('a[href]','href'),('[id]','id'),('img[src]','src')]:
            before=[el.get(attr) for el in original.select(selector)]
            after=[el.get(attr) for el in translated.select(selector)]
            if before!=after:errors.append(f'translation changed {attr}: {path.name}')
        for pre in original.select('pre'):expected_code[pre.get_text().rstrip('\n')]+=1
        expected_tables+=len(original.select('table.tableblock, .hdlist > table'))
        expected_hints+=len(original.select('.admonitionblock'))
        expected_images+=len([img for img in original.select('img') if not img.find_parent(class_='admonitionblock')])
    missing_code=expected_code-code;extra_code=code-expected_code
    if missing_code:errors.append(f'{sum(missing_code.values())} missing or changed original code blocks')
    if extra_code:errors.append(f'{sum(extra_code.values())} unexpected code blocks in guide/reference')
    if html_tables!=expected_tables:errors.append(f'tables: expected {expected_tables}, found {html_tables}')
    if hints!=expected_hints:errors.append(f'hints: expected {expected_hints}, found {hints}')
    actual_images=len([x for x in image_links if 'guide' in x[0].parts or 'reference' in x[0].parts])
    if actual_images!=expected_images:errors.append(f'images: expected {expected_images}, found {actual_images}')
    asset_manifest=json.loads((ROOT/'source/assets-manifest.json').read_text())
    decoded=[]
    for asset in asset_manifest:
        path=DOCS/asset['path']
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=asset['sha256']:
            errors.append('asset missing or changed: '+asset['path'])
        else:
            try:decoded.append({'path':asset['path'],**check_image(path,asset['mime'])})
            except Exception as e:errors.append('invalid image: '+asset['path']+': '+str(e))
    (ROOT/'reports/images.json').write_text(json.dumps(decoded,ensure_ascii=False,indent=2))
    api_schema=json.loads((ROOT/'source/api/schema.json').read_text())
    if technical_schema(api_schema)!=technical_schema(schema_translated(api_schema)):
        errors.append('API technical schema changed during translation')
    # Every book page must be reachable through the canonical GitBook summary.
    summary=(DOCS/'SUMMARY.md').read_text()
    for file in files:
        if file.name=='SUMMARY.md':continue
        if file.relative_to(DOCS).as_posix() not in summary:errors.append('not in SUMMARY: '+file.relative_to(DOCS).as_posix())
    review=[]
    for key,value in TRANSLATIONS.items():
        plain=re.sub(r'⟦\d+⟧','',value)
        source=re.sub(r'⟦\d+⟧','',UNITS[key]['text'])
        if len(re.findall('[A-Za-z]+',source))>14 and not re.search('[\u3400-\u9fff]',plain):
            review.append({'id':key,'source':UNITS[key]['text'],'translation':value})
    missing=set(UNITS)-set(TRANSLATIONS)
    if missing and not args.allow_partial:errors.append(f'{len(missing)} missing or invalid translation units')
    report={'passed':not errors,'mode':'layout-preview' if args.allow_partial else 'release','pages':len(files),'translation_units':len(UNITS),'valid_translations':len(TRANSLATIONS),'missing_translations':len(missing),'original_code_blocks':sum(expected_code.values()),'rendered_original_code_blocks':sum(code.values()),'tables':html_tables,'hints':hints,'image_occurrences':actual_images,'unique_original_assets':len(asset_manifest),'local_links_checked':len([1 for _,h in links if h and not urlsplit(h).scheme]),'errors':errors,'warnings':warnings,'english_prose_for_review':review}
    (ROOT/'reports/verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    (ROOT/'work/code-diff.json').write_text(json.dumps({'missing':dict(missing_code),'extra':dict(extra_code)},ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k not in ('errors','warnings','english_prose_for_review')},ensure_ascii=False))
    for error in errors[:45]:print('ERROR',error)
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
