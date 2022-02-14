import json


with open('input.json', encoding='utf8') as infile:
    data = json.load(infile)
    data = sorted(data, key=lambda x: (-len(x['colors']), -x['radius'], -(x['x'] ** 2 + x['y'] ** 2) ** 0.5, x['id']))
    for i in data:
        print(i['id'], end=' ')
