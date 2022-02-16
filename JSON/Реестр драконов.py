import csv
import json


with open('dragons.csv', encoding='utf8') as infile, open('dragons.json', 'w', encoding='utf8') as out:
    data = list(csv.DictReader(infile))
    ans = {'dragons': data}
    json.dump(ans, out)

#json.load(infile) -> объект в виде словаря или списка
#json.dump(data, file) 