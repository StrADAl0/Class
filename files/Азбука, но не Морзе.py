from sys import stdin
d = dict()


name = input()
with open(name) as infile:
    s = [i.rstrip() for i in infile]
    for i in s:
        d[i.split()[1]] = i.split()[0]


a = [i.rstrip() for i in stdin]
with open('result.txt', 'w') as out:
    for i in a:
        print(''.join(list(map(lambda x: d[x], i.split()))), file=out)

