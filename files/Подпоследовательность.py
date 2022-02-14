with open('sequence.txt', encoding='utf-8') as infile:
    s = infile.readline()
    print(max(list(map(len, s.replace('DF', 'D F').split()))))