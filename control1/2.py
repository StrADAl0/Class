with open('input.txt') as infile, open('output.txt', 'w') as out:
    data = [i.rstrip() for i in infile.readlines()]
    for i in data:
        if 0 in [j.isalnum() for j in i]:
            continue
        print(i, file=out)