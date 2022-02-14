from sys import stdin


a = []
for i in stdin:
    x, y = [float(j) for j in i.rstrip().split()]
    a.append((x, y))
a = sorted(a, key=lambda h: h[0])

ans = 0
for i in range(1, len(a)):
    ans += (a[i][0] - a[i - 1][0]) * (a[i][1] + a[i - 1][1]) / 2
with open('res.txt', 'w') as out:
    print(ans, file=out)
