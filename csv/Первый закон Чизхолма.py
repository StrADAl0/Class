import csv

with open('salary.csv', encoding='utf-8') as infile:
    data = list(csv.DictReader(infile, delimiter=';'))
name = input()
start, end = input().split()
headers = [['Субъект', start, end]]
with open('out_file.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')
    for i in data:
        if i['Федеральный округ'] == name:
            if ((float(i[end]) - float(i[start])) / float(i[start])) < 0.04:
                headers.append([i['Субъект'], i[start], i[end]])
    if len(headers) > 1:
        for i in headers:
            writer.writerow(i)