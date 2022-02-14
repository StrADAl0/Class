import json


with open('russian_words.txt', encoding='utf-8') as infile:
    data = [i.rstrip() for i in infile.readlines()]


ans = dict()
for i in data:
    ans.setdefault(i[0], [])
    ans[i[0]].append(i)


with open('russian_words.json', encoding='utf-8') as out:
    json.dump(ans, out)