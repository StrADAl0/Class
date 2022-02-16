import csv

with open('in_file.csv', encoding='utf-8') as infile:
    data = list(csv.reader(infile, delimiter=';'))


tree = dict()
for i in data:
    tree.setdefault(i[0],[])
    tree.setdefault(i[1], [])
    tree[i[0]].append(i[1])


root = None
for i in tree.keys():
    cnd = 1
    for j in tree.keys():
        if(i == j):
            continue
        if(i in tree[j]):
            cnd = 0
            break
    if(cnd):
        root = i
        break


with open('out_file.csv', 'w', newline='') as out:
    writer = csv.writer(out, delimiter=';')
    writer.writerow([root])
    level = tree[root]
    while level:
        new_level = []
        writer.writerow(sorted(level))
        for i in level:
            new_level += tree[i]
        level = new_level

