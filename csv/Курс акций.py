import csv

with open('yndx_share_price.csv', encoding='utf-8') as infile:
    data = csv.reader(infile, delimiter=',')
    data = list(data)[1:]

ans = []
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if(int(data[j][-1]) > int(data[i][-1])):
            ans.append(j - i)
            break
    if(len(ans) < i + 1):
        ans.append(0)

with open('predict.txt', 'w') as out:
    print(' '.join([str(i) for i in ans]), file=out)
