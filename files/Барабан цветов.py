def color_search(*args, filename="output.txt"):
    with open("flower_drum.txt", encoding="utf8") as file:
        data = [x.rstrip().split("\t") for x in file.readlines()]
        names = {x[0]: x[1:] for x in data}
        hex_code = {x[1]: [x[0], x[2], x[3], x[4]] for x in data}
        rgb = {(int(x[2]), int(x[3]), int(x[4])): x[:2] for x in data}
    if type(args[0]) == tuple:
        result = [list(map(str, arg)) + rgb[arg] for arg in args]
    elif args[0].startswith("#"):
        result = [[arg] + hex_code[arg] for arg in args]
    else:

        result = [[arg] + names[arg] for arg in args]
    with open(filename, 'w', encoding="utf8") as file:
        for item in result:
            file.write('\t'.join(item) + '\n')