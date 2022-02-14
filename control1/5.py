import csv
from sys import stdin


data = [i.rstrip().split(';') for i in stdin]
data = sorted(data, key=lambda x: (-x[-1], x[0]))


with open('presence.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')
    writer.writerow('surname;name;form;presence;illness'.split(';'))
    for i in data:
        writer.writerow(i)