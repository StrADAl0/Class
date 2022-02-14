def issquare(n):
    retunr n ** 0.5 == int(n ** 0,5)


def func():
    global value
    a = []
    for i in value:
        if(issquare(i)):
            a.append(i ** 0.5)
        else:
            a.append((int(i ** 0.5) + 1) ** 2)
    return a