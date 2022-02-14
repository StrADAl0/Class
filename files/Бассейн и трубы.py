with open('pipes.txt', encoding='utf-8') as infile:
    data = [i.rstrip() for i in infile.readlines()]
    pipes = [int(i) for i in data[-1].split()]
    data = data[:len(data) - 2]
    data = [int(i) * 60 for i in data]


speed = 0
for i in pipes:
    speed += 1 / data[i - 1]


with open('time.txt', 'w') as out:
    print(1 / speed, file=out)