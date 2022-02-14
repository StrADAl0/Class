import csv

with open('alpha_oriona.csv', encoding='utf-8') as infile:
    data = list(csv.reader(infile, delimiter=';'))[1:]

ans1 = 0
ans2 = ''
ans3 = ''
for i in range(len(data)):
    t = 0
    for j in range(i + 1, len(data)):
        if int(data[j][2]) <= int(data[j][2]) - 1:
            if(t > ans1):
                ans1, ans2, ans3 = t, data[i][0], data[i][1]
                break
        t += 1
    

with open('result.txt', 'w') as out:
    print(ans1, file=out)
    print(ans2, ans3, file=out)
