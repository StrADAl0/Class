def flies(*args, func=None):
    args = [(i.items[0], i.items[1]) for i in args]
    data = []
    if func:
        for i in args:
            if func(i[0], i[1]):
                data.append(i)
    else:
        data = args
    ans = []
    ans.append({'x': min(data, key=lambda x: x[0])[0], 'y': max(data, key=lambda y: y[1])[1]})
    ans.append({'x': max(data, key=lambda x: x[0])[0], 'y': min(data, key=lambda y: y[1])[1]})
    return ans

