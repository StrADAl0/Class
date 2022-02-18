from sys import stdin

def check(word, check_word):
    if not set(word).issubset(check_word):
        return 0
    for i in set(word):
        if word.count(i) > check_word.count(i):
            return 0
    return 1

data = [i.rstrip().split() for i in stdin]


for i in data:
    ans = []
    for j in i[1:]:
        if check(j, i[0]):
            ans.append(j)
    print(*sorted(ans, key=len, reverse=True))
    