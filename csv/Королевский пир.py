import sys
import csv


data = [i.rstrip().split('\t') for i in sys.stdin]

ans = []
names = list(set([j[0] for j in data]))
ingridients = list(set([j[1] for j in data]))


for i in names:
    t = dict()
    t['recipe'] = i
    for j in ingridients:
        t.setdefault(j, 0)
    for j in filter(lambda x: x[0] == i, data):
        t[j[1]] += int(j[2])
    ans.append(t)

headers = ['recipe']
headers += sorted(ingridients)

with open('recipes.csv', 'w') as out:
    writer = csv.DictWriter(out, delimiter=';', fieldnames=headers)
    writer.writeheader()
    for i in ans:
        writer.writerow(i)
