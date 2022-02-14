with open('in_file.txt', encoding='utf-8') as infile:
    data = [i.rstrip() for i in infile.readlines()]


n = int(data[0])
data = data[1:]
total_len = 0
for i in data:
    total_len += len(i)
mid_value = int(total_len / len(data))


with open('out_file.txt', 'w') as out:
    print(mid_value, file=out)
    for i in data:
        if(abs(len(i) - mid_value) <= n):
            print(i, file=out)