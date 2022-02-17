def func():
    global value
    a = []
    for i in value:
        a.append(i)
    value[0] = a[0] + a[1]
    value[-1] = a[-1] + a[-2]
    for i in range(1, len(value) - 1):
        value[i] += max(a[i - 1], a[i + 1])
    

value = [1, 2, 3, 4, 5]
#[3, 5, 7, 9, 9]
func()
print(*value)