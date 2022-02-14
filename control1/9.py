import json


with open('marks.json', encoding='utf8') as infile:
    data = json.load(infile)


ans = {}
for k, v in ans.items():
    for k1, v1 in v.items():
        for i in v1:
            ans.setdefault(' '.join(i), [k, k1])


with open('results.json', 'w') as out:
    json.dump(ans)