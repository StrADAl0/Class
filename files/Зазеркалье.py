infile = input()
with open(infile, 'rb') as inputfile, open('output.dat', 'wb') as out:
    data = [i.rstrip() for i in inputfile.readlines()]
    data = [i.decode('utf8') for i in data]
    data = [i[::-1] + '\n' for i in data]
    data = [i.encode('utf8') for i in data]
    for i in data:
        out.write(i)

#['b\x0a\x', '']
#['blabla\n', 'kkk\n']