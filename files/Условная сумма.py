with open('data.txt', encoding='utf8') as infile:
    data = [i.rstrip() for i in infile.readlines()]
    n = int(data[0])
    data = [int(i) for i in data[1].split()]
    ans = 0
    for i in range(1, n):
        for j in data:
            if(i % j == 0):
                ans += i
                break
    print(ans)
