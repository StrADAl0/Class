with open('test.txt', 'r', encoding='utf8') as out:
    data = out.readlines()
    out.seek(0)
    data1 = out.read().split('\n')
    print(len(data))
    print(len(data1))