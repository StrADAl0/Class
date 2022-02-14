from asyncore import write
from cmath import inf
import json
import csv

with open('results.json', encoding='utf8') as infile:
    data = json.load(infile)


ans = []
ans.append('Фамилия;Имя;общий балл по всем предметам'.split(';'))

for i in data.keys():
    cnt = 0
    for j in data[i]:
        cnt += j[1]
    ans.append([i.split()[0], i.split()[1], cnt / len(data[i])])


with open('results.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')
    for i in ans:
        writer.writerow(i)