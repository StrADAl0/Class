import csv
from sys import stdin


n, m = [int(i) for i in input().split()]
data = [i.rstrip().split() for i in stdin]

ans = []
for i in data:
    if(sum(list(map(int, i[2:5]))) < n):
        continue
    if(1 in list(map(lambda x: x < n, i[2:5]))):
        continue
    ans.append(i)


with open('exam.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')
    writer.writerow('Фамилия; имя; результат 1; результат 2; результат 3; сумма'.split('; '))
    for i in ans:
        writer.writerow(i)