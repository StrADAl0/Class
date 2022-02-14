import csv
from operator import delitem


with open('presence.csv', encoding='utf8') as infile, open('illness.csv', 'w') as out:
    data = list(csv.reader(infile, delimiter=';'))
    writer = csv.writer(out, delimiter=':')
    data[0].append('percent')
    header = data[0]
    writer.writerow(header)
    data = data[1:]
    for i in data:
        i.append(int(100 * i[-1] / i[-2]))
        writer.writerow(i)