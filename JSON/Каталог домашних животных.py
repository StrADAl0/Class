import csv
import json


with open('catalog.csv', encoding='utf-8') as infile:
    data = list(csv.DictReader(infile, delimiter=';'))


ans = {"type": {}}
for i in data:
    ans["type"].setdefault(i["type"], {})
    ans['type'][i['type']].setdefault("breed", {})
    ans['type'][i['type']]['breed'].setdefault(i['breed'], [])
    pet = {"name": i['name'], 'age': i['age'], 'gender': i['gender'], 'owner': i['owner'], 'phone': i['phone']}
    ans['type'][i['type']]['breed'][i['breed']].append(pet)


with open('pets.json', 'w', encoding='utf8') as out:
    json.dump(ans, out)