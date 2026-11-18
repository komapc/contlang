"""gap1: все 60 предложений bench1 dev по убыванию разрыва tpx − mc (оценки — судьи tpx1), с кодами и прочтениями → pairs.md."""
import json,re,collections
from pathlib import Path
R=Path(__file__).resolve().parent.parent
S=json.load(open(R/'../items/bench1/sents_dev.json'))
mc=json.load(open(R/'v2b2/codes.json'))['mc']['sents']
tp=json.load(open(R/'base1/codes.json'))['tp']['sents']
tpx=json.load(open(R/'tpx1/codes.json'))
tpx=tpx['tpx']['sents']
lists=json.load(open(R/'tpx1/lists.json'))
def pn(p): return {int(m[1]):m[2].strip() for x in open(p) if (m:=re.match(r"\s*(\d+)\.\s*(.+)",x))}
rs={}
for l in lists:
    f = R/f"tpx1/answers/{l['r']}_sents_out.md" if l['lang']=='tpx' else R/f"v2b2/answers/{l['r']}_sents_out.md"
    a=pn(f)
    for k,i in enumerate(l['order']): rs[(l['r'],i)]=a.get(k+1,'—')
sc=collections.defaultdict(list)
for p in json.load(open(R/'tpx1/pairs.json')):
    if p['kind'] in('sent','overlap') and p.get('s') is not None: sc[(p['r'],p['i'])].append(p['s'])
def m(r,i): return sum(sc[(r,i)])/len(sc[(r,i)])
rows=[]
for i in range(len(S)):
    a={L:(m(L+'1',i)+m(L+'2',i))/2 for L in('mc','tp','tpx')}
    rows.append((a['tpx']-a['mc'],i,a))
rows.sort(reverse=True)
out=[]
for g,i,a in rows:
    out.append(f"### #{i}  gap tpx−mc {g:+.2f}  (mc {a['mc']:.2f} tp {a['tp']:.2f} tpx {a['tpx']:.2f})\nEN: {S[i]['s']}\nMC: {mc[i]}\nTP: {tp[i]}")
    for r in('mc1','mc2','tp1','tpx1'):
        out.append(f"  {r} {sc[(r,i)]}: {rs[(r,i)]}")
    out.append('')
open(R/'gap1/pairs.md','w').write('\n'.join(out))
print(sum(1 for g,_,_ in rows if g>=1), sum(1 for g,_,_ in rows if g<=-0.5))
