import json
from sys import stdin


with open('input.txt') as infile:
    data = [i.rstrip()[0] for i in infile.readlines()]


ans = {}
for i in data:
    value = data.count(i)
    ans[i] = 100 * value / len(data)


with open('output.json', 'w') as out:
    json.dump(ans, out)