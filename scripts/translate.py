"""Translate inline prose through the user's existing Kimi Code installation.

Uses documented --prompt/--output-format stream-json; no credentials are read.
Each validated unit is cached immediately, and interrupted runs are resumable.
"""
from __future__ import annotations
import argparse, collections, concurrent.futures, json, os, re, subprocess, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TOKENS=re.compile(r'⟦\d+⟧')
NUMBER_WORDS=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
CN_DIGITS={'零':0,'一':1,'二':2,'两':2,'双':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9}

def numeric_error(source,target):
    """Preserve quantities while accepting 'three/3/三' translation choices."""
    a=collections.Counter(re.findall(r'\d+(?:[.,]\d+)*',source))
    b=collections.Counter(re.findall(r'\d+(?:[.,]\d+)*',target))
    chinese=collections.Counter()
    for word in re.findall('[零一二两双三四五六七八九十]+',target):
        if word=='十':value=10
        elif word.count('十')==1:
            left,right=word.split('十')
            if len(left)>1 or len(right)>1:continue
            value=CN_DIGITS.get(left,1)*10+CN_DIGITS.get(right,0)
        elif len(word)==1:value=CN_DIGITS[word]
        else:continue
        chinese[str(value)]+=1
    for number,count in (a-b).items():
        if chinese[number]<count:return True
    for number,count in (b-a).items():
        if number.isdigit() and int(number)<len(NUMBER_WORDS):
            if len(re.findall(r'\b'+NUMBER_WORDS[int(number)]+r'\b',source,re.I))>=count:continue
        return True
    return False
SYSTEM='''你是精通 Proxmox VE、Linux、KVM、LXC、Ceph、ZFS、网络、虚拟化的中文技术文档译者。
任务：将给出的 JSON 对象中每一个英文值完整翻译成简体中文，返回相同键的 JSON 对象。
硬性要求：
1. 完整、准确逐句翻译，不删节、不总结、不添加说明。每个输入键必须且只能出现一次。
2. ⟦数字⟧ 是不可修改的占位符，代表 HTML 标记、命令、参数、路径或链接。每个值中的占位符必须原样、同样次数、按原顺序保留。不得增加占位符。
3. 不要翻译品牌、产品名、命令、参数名、配置键、变量、枚举值、协议缩写、文件名、路径、URL、数值及单位。不要改变技术含义、否定词、条件、警告或版本号。
4. 术语统一：node=节点；cluster=集群；guest=客户机；host=宿主机；container=容器；storage=存储；pool=池；quorum=仲裁；fencing=隔离；bridge=网桥；replication=复制；snapshot=快照；live migration=在线迁移；thin provisioning=精简置备；high availability=高可用性。
5. 使用自然、清楚的中文技术文体。输入值可能是标题、段落、表格单元格或 API 描述，按原用途翻译。占位符保留在合理的句子位置且不得改变顺序。
6. 只输出有效 JSON，不要 Markdown 围栏、思考、前言、后记。不要使用工具，不要读取文件，不要执行任何命令。
输入 JSON：
'''

def validate(source, translated):
    if not isinstance(translated,str) or not translated.strip():return 'empty/non-string'
    if TOKENS.findall(source)!=TOKENS.findall(translated):return 'placeholder sequence changed'
    # A suspiciously short output is retried, never silently accepted as a summary.
    prose=TOKENS.sub('',source);target=TOKENS.sub('',translated)
    if numeric_error(prose,target):return 'numeric values changed'
    if collections.Counter(re.findall(r'<[A-Za-z][^<>]*>',prose))!=collections.Counter(re.findall(r'<[A-Za-z][^<>]*>',target)):
        return 'literal angle-bracket values changed'
    if len(prose)>160 and len(target)<len(prose)*0.12:return 'too short'
    if re.search(r'[A-Za-z]{4}',prose) and len(prose)>90 and translated==source:return 'untranslated paragraph'
    return None

def run_batch(batch, number, attempt=0):
    payload={u['id']:u['text'] for u in batch}
    started=time.monotonic()
    prompt=SYSTEM+json.dumps(payload,ensure_ascii=False)
    result=subprocess.run(['kimi','--output-format','stream-json','-p',prompt],
                          capture_output=True,text=True,cwd=ROOT,timeout=1200)
    logs=ROOT/'work/kimi-logs';logs.mkdir(exist_ok=True)
    (logs/f'{number:04d}-{attempt}.jsonl').write_text(result.stdout)
    if result.returncode:
        raise RuntimeError(f'Kimi exited {result.returncode}: {result.stderr[-700:]}')
    content=[]
    for line in result.stdout.splitlines():
        try:msg=json.loads(line)
        except json.JSONDecodeError:continue
        if msg.get('role')=='assistant' and isinstance(msg.get('content'),str):content.append(msg['content'])
    text=''.join(content).strip()
    if text.startswith('```'):text=re.sub(r'^```(?:json)?\s*|\s*```$','',text)
    try:translated=json.loads(text)
    except json.JSONDecodeError as e:raise RuntimeError(f'Invalid JSON ({len(text)} chars): {text[:220]}') from e
    if not isinstance(translated,dict):raise RuntimeError('Expected JSON object')
    good={};bad=[]
    for u in batch:
        error=validate(u['text'],translated.get(u['id']))
        if error:bad.append((u,error))
        else:good[u['id']]=translated[u['id']]
    return good,bad,round(time.monotonic()-started,1)

def main():
    p=argparse.ArgumentParser();p.add_argument('--workers',type=int,default=3)
    p.add_argument('--words',type=int,default=1800);p.add_argument('--limit',type=int)
    args=p.parse_args()
    units=json.loads((ROOT/'work/units.json').read_text())
    cache=ROOT/'work/translations.jsonl';translated={}
    if cache.exists():
        for l in cache.read_text().splitlines():
            if not l.strip():continue
            item=json.loads(l)
            translated.update({k:v for k,v in item.items() if k in units and not validate(units[k]['text'],v)})
    pending=[u for k,u in units.items() if k not in translated]
    if args.limit:pending=pending[:args.limit]
    batches=[];batch=[];size=0
    for u in pending:
        n=len(re.findall(r'\w+',u['text']))
        if batch and (size+n>args.words or len(batch)>=100):
            batches.append(batch);batch=[];size=0
        batch.append(u);size+=n
    if batch:batches.append(batch)
    print(f'{len(translated)}/{len(units)} cached; {len(pending)} units in {len(batches)} batches; {args.workers} workers',flush=True)
    errors=[]
    with cache.open('a') as output, concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures={pool.submit(run_batch,b,i): (i,b,0) for i,b in enumerate(batches)}
        while futures:
            done,_=concurrent.futures.wait(futures,return_when=concurrent.futures.FIRST_COMPLETED)
            for f in done:
                i,b,a=futures.pop(f)
                try:
                    good,bad,elapsed=f.result()
                    output.write(json.dumps(good,ensure_ascii=False)+'\n');output.flush()
                    translated.update(good)
                    print(f'batch {i} attempt {a}: +{len(good)}, retry {len(bad)}; {elapsed}s; total {len(translated)}/{len(units)}',flush=True)
                    retry=[u for u,e in bad]
                    if retry:
                        if a<3:futures[pool.submit(run_batch,retry,i,a+1)]=(i,retry,a+1)
                        else:errors.extend({'id':u['id'],'error':e} for u,e in bad)
                except Exception as e:
                    print(f'batch {i} attempt {a} ERROR: {e}',flush=True)
                    if a<2:futures[pool.submit(run_batch,b,i,a+1)]=(i,b,a+1)
                    else:errors.extend({'id':u['id'],'error':str(e)} for u in b)
    report={'total':len(units),'translated':len(translated),'missing':[k for k in units if k not in translated],'errors':errors}
    (ROOT/'reports/translation-progress.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps({k:v for k,v in report.items() if k not in ('missing','errors')}),flush=True)
    if errors:raise SystemExit(1)

if __name__=='__main__':main()
