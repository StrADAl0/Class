data = [[int(j) for j in i.rstrip().split()] for i in open('in.txt').readlines()]


def gradient(corner):
    if corner == 1:
        data = [i[::-1] for i in data]
    if corner == 3:
        data = data[::-1]
    if corner == 2:
        data = [i[::-1] for i in data][::-1]
    ans = [[data[0][0]]]
    for i in range(1, len(data[0])):
        ans[0].append(data[0][i] - data[0][i - 1])
    for i in range(1, len(data)):
        ans.append([data[i][0] - data[i - 1][0]])
        for j in range(1, len(data[i])):
            ans[-1].append(data[i][j] - data[i - 1][j - 1])
    if corner == 1:
        ans = [i[::-1] for i in ans]
    if corner == 3:
        ans = ans[::-1]
    if corner == 2:
        ans = [i[::-1] for i in ans][::-1]
    with open('gradient.txt', 'w') as out:
        for i in ans:
            print(*i, sep='\t', file=out)
