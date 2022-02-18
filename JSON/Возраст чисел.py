from sys import stdin
import json


def func(n, cnt=0):
    if(len(n) == 1):    
        return cnt
    ans = 1
    for i in n:
        ans *= int(i)
    return func(str(ans), cnt + 1)


a = [i.rstrip() for i in stdin]
ans = dict()
ans.setdefault('1', [])
for i in a:
    if len(i) == 1:
        ans['1'].append(i)
        continue
    t = func(i)
    ans.setdefault(str(t), [])
    ans[str(t)].append(i)


with open('numbers_age.json', 'w') as out:
    json.dump(ans, out)