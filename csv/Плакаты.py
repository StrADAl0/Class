import csv


with open('posters.csv', encoding='utf-8') as infile1, open('in_file.txt', encoding='utf-8') as infile2:
    data = list(csv.DictReader(infile1, delimiter=';'))
    sorting = [i.rstrip() for i in infile2.readlines()]

for i in data:
    for j in i.keys():
        if i[j].isdigit():
            i[j] = int(i[j])


data = sorted(data, key=lambda x: [x[i] for i in sorting])

with open('sorted.csv', 'w') as out:
    writer = csv.DictWriter(out, fieldnames=data[0].keys(), delimiter=';')
    for i in data:
        writer.writerow(i)
