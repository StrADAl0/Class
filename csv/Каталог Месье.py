import csv


with open('messier.txt', encoding='utf-8') as infile, open('messier.csv', 'w') as out:
    data = [(i.rstrip()).split('\t') for i in infile.readlines()]
    writer = csv.writer(out, delimiter=';')
    for i in data:
        writer.writerow(i)