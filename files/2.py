with open('in_file.txt', mode='r') as f, open('out_file.txt', 'w') as b:
    c = [i.rstrip() for i in f.readlines()]
    for elem in c:
        qwerty = str(elem) + ' = ' + str(eval(elem))
        print(qwerty, file=b)
