from sys import stdin

n = int(input())
data = [i.rstrip() for i in stdin]
for i in data:
    print(i[n % len(i):] + i[:n % len(i)])