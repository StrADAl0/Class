def big_data(*data, key=lambda x: x):
    x = data
    yz = []
    for elem in x:
        a = elem[2]
        b = []
        for letter in a:
            if letter == '@':
                break
            else:
                b.append(letter)
        c = ''.join(b)
        d = c.capitalize()
        e = elem[1]
        f = e.split("-")
        g = str(f[0][0]) + str(f[1][-1]) + str(f[2][-1])
        qwerty = d + g
        elem1 = list(elem)
        elem1.append(qwerty)
        elem = tuple(elem1)
        yz.append(elem)
    return sorted(yz, key=key)
