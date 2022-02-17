from sys import stdin


a = [i.rstrip() for i in stdin]


for i in a:
    print(', '.join(sorted(i.split())))