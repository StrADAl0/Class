def count_own(n, unit):
    info = {'B': 1,
            'KB': 2 ** 10,
            'MB': 2 ** 20,
            'GB': 2 ** 30,
            'TB': 2 ** 40}
    return n * info[unit]


with open('input.txt', encoding='utf-8') as infile:
    data = [(i.rstrip()).split() for i in infile.readlines()]


files = dict()
for i in data:
    files.setdefault(i[0].split('.')[1], [])
    files[i[0].split('.')[1]].append(i)
d = {'B': 0, 'KB': 1, 'MB' : 2, 'GB': 3, 'TB' : 4}
t = {'B': 'KB', 'KB': 'MB', 'MB': 'GB', 'GB': 'TB'}


output = open('output.txt', 'w')
for i in sorted(files.keys()):
    curr = 'B'
    cnt = 0
    for j in files[i]:
        cnt += count_own(float(j[1]), j[2])
    while(cnt >= 1024):
        cnt /= 1024
        curr = t[curr]
    if(cnt - int(cnt) >= 0.5):
        cnt = int(cnt) + 1
    else:
        cnt = int(cnt)
    print('\n'.join(sorted([j[0] for j in files[i]])), file=output)
    print('----------', file=output)
    print('Summary: {} {}'.format(cnt, curr), file=output)
    print(file=output)