def func(n):
    ans = {}
    n = str(n)
    for i in n:
        if(i not in ans.keys()):
            ans[i] = 0
        ans[i] += 1
    return ans


n = int(input())
a = func(n)
for i in a.keys():
    print(i, a[i])
