import csv

with open('presence.csv', encoding='utf8') as infile, open('illness.csv', 'w') as out:
    data = list(csv.reader(infile, delimiter=';'))
    writer = csv.writer(out, delimiter=',')
    for i in data:
        writer.writerow([i[-1], i[0], i[1]])