import json


with open('in.json', encoding='utf8') as infile, open('out.json', 'w', encoding='utf8') as out:
    data = json.load(infile)['complex']
    ans = {"complex": []}
    ans['complex'].append({"Re": data[0]['Re'] + data[1]['Re'], 'Im': data[0]['Im'] + data[1]['Im']})
    ans['complex'].append({"Re": data[0]['Re'] - data[1]['Re'], 'Im': data[0]['Im'] - data[1]['Im']})
    t1 = data[0]['Re'] * data[1]['Re'] - data[0]['Im'] * data[1]['Im']
    t = {"Re": t1, 'Im': data[0]['Re'] * data[1]['Im'] + data[0]['Im'] * data[1]['Re']}
    ans['complex'].append(t)
    json.dump(ans, out)