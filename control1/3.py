with open('input.dat') as infile, open('output.dat', 'w') as out:
    data = [i.rstrip() for i in infile.readlines()]
    print('\n'.join(data[:10]), file=out)
    number = [(int(x), int(y)) for j in data[10:] for i in j.split() for x, y in i]
    print('\n'.join([str(number[i][0] + number[i][1]) + str(i + 11) for i in range(len(number))]), file=out)