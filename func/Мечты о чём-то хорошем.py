def good_dreams(string, first_div, second_div, *args, **kwargs):
    data = string.split(first_div)
    data = [i.split(second_div) for i in data]
    for i in args:
        if i[0] not in kwargs.keys():
            continue
        data[int(i[1])] = list(map(kwargs[i[0]], data[int(i[1])]))
    return data