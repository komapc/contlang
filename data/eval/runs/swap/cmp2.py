# Сравнение наборов без CONSUME (v2/*.json) с исходными кодами (remove.json хранит исходный код и место каждого слова)
import json, glob, os
o = json.load(open('remove.json'))
print('базовый top1', sum(v['rank'] == 1 for v in o.values()))
for f in sorted(glob.glob('v2/*.json')):
    d = json.load(open(f)); n = os.path.basename(f)[:-5]
    print(f"{n:20} top1 {sum(v['rank'] == 1 for v in d.values())}  кодов изменилось {sum(d[w]['code'] != o[w]['code'] for w in d if w in o)}  слов {len(d)}")
