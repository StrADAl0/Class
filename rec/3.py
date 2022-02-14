a = [0, 0, 1]
def tribonacci(n):
    if(len(a) <= n):
        a.append(tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3))
    return a[n - 1]
    



print(tribonacci(100))