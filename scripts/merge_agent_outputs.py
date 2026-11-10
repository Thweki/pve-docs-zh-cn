"""Validate and merge disjoint translation batches without editing book structure."""
import json
from pathlib import Path
from translate import ROOT,validate

def main():
    units=json.loads((ROOT/'work/units.json').read_text());cached={};output={};errors=[];groups={}
    cache=ROOT/'work/translations.jsonl'
    for line in cache.read_text().splitlines():
        if line.strip():cached.update(json.loads(line))
    for name in 'abc':
        assigned={x['id'] for x in json.loads((ROOT/f'work/agents/{name}-input.json').read_text())}
        accepted={}
        for path in sorted((ROOT/'work/agents').glob(name+'-[0-9][0-9][0-9].json')):
            try:data=json.loads(path.read_text())
            except json.JSONDecodeError as e:
                errors.append({'file':path.name,'error':str(e)});continue
            if not isinstance(data,dict):
                errors.append({'file':path.name,'error':'Expected JSON object'});continue
            for key,value in data.items():
                if key not in assigned:
                    errors.append({'file':path.name,'id':key,'error':'Not assigned to this batch owner'});continue
                reason=validate(units[key]['text'],value)
                if reason:
                    errors.append({'file':path.name,'id':key,'error':reason});continue
                if key in accepted and accepted[key]!=value:
                    errors.append({'file':path.name,'id':key,'error':'Conflicting duplicate translation'});continue
                accepted[key]=value
        output.update(accepted)
        groups[name]={'assigned':len(assigned),'valid_outputs':len(accepted),'remaining':len(assigned-set(accepted))}
    added={k:v for k,v in output.items() if cached.get(k)!=v}
    if added:
        with cache.open('a') as out:out.write(json.dumps(added,ensure_ascii=False)+'\n')
        cached.update(added)
    valid={k:v for k,v in cached.items() if k in units and not validate(units[k]['text'],v)}
    missing=sorted(set(units)-set(valid))
    progress={'total':len(units),'translated':len(valid),'missing':missing,'errors':errors}
    (ROOT/'reports/translation-progress.json').write_text(json.dumps(progress,ensure_ascii=False,indent=2))
    report={'groups':groups,'newly_merged':len(added),'total_units':len(units),'valid_translations':len(valid),'missing_translations':len(missing),'errors':errors}
    (ROOT/'reports/agent-progress.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
