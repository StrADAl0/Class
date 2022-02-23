from sys import stdin

def dif(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt


def order(data, ans):
    while len(data) > len(ans):
        for i in data:
            if dif(i, ans[-1]) == 1:
                if len(ans) == 1:
                    ans.append(i)
                    break
                if ans[-2] != i:
                    ans.append(i)
                    break
    return ans


data = [i.rstrip() for i in stdin]
print(*order(data, [data[0]]), sep='\n')
