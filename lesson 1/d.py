def func(x):
    ans = (x[0] ** 2 + x[1] ** 2) ** 0.5
    return round(ans, 5)


print(func((1, 1)))