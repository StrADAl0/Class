import sys
import csv


data = [(i.rstrip()).split('\t') for i in sys.stdin]
headers = 'nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia'.split(';')


with open('plantis.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')
    writer.writerow(headers)
    for i in data:
        writer.writerow(i)