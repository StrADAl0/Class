import json
from sys import stdin


data = [i.rstrip() for i in stdin]
ans = {'science': {}}

for i in data:
    ans['science'].setdefault(i[-1], [])
    ans['science'][i[-1]].append(i[0:2])


with open('marks.json', 'w') as out:
    json.dump(ans)