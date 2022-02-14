import csv

with open('in_file.csv', encoding='utf-8') as infile:
    data = list(csv.reader(infile, delimiter=';'))


tree = dict()
for i in data:
    tree.setdefault(i[0],[])
    tree.setdefault(i[1], [])
    tree[i[0]].append(i[1])


root = []
for i in tree.keys():
    cnd = 1
    for j in tree.keys():
        if(i == j):
            continue
        if(i in tree[j]):
            cnd = 0
            break
    if(cnd):
        root.append(i)


with open('outfile.csv', 'w') as out:
    writer = csv.writer(out, delimiter=';')
    i = 0
    while i < len(root):
        if(not tree[root[i]]):
            i += 1
            if i == len(root):
                writer.writerow(root)
            continue
        writer.writerow(root)
        root = tree[root[i]]
        i = 0