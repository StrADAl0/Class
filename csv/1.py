import csv
from email import header


with open('vps.csv', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=';')
    data = list(reader)
    headers = data[0]
    data = data[1:]

p = float(input())
for i in data:
    if(float(i[4]) >= p):
        print(i[0])