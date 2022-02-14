def func(s):
    ans = {"количество слов" : 0,
           "уникальных букв" : 0,
           "длина с пробелами" : 0,
           "длина без пробелов" : 0}
    ans["количество слов"] = len(s.split())
    t = set()
    for i in s.split():
        for j in i:
            t.add(j)
    ans["уникальных букв"] = len(t)
    ans["длина с пробелами"] = len(s)
    cnt = 0
    for i in s.split():
        cnt += len(i)
    ans["длина без пробелов"] = cnt
    return ans


a = func("ff fff adada adadaf")
for i in a.keys():
    print(i, a[i])