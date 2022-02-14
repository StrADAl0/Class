import csv

with open('alpha_oriona.csv') as infile:
    data = list(csv.DictReader(infile, delimiter=';'))


for i in data:
    i['luminosity'] = int(i['luminosity'])


ans = 0
start, end = 0, 0
for i in range(len(data)):
    if start > len(data) - 1:
        break
    if end == 0:
        end += 1
        continue
    if data[end - 1]['luminosity'] > data[end]['luminosity']:
        if end - start > ans:
            ans = end - start
        start = end
        continue
    end += 1




with open('result.txt', 'w') as out:
    print(ans, file=out)
    print(data[start]['date'], data[start]['time'], file=out)