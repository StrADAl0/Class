def big_data(*data, key=None):
    ans = []
    for i in data:
        ans.append((i[0], i[1], i[2], i[2].split('@')[0].capitalize()))
    return sorted(ans, key=key)
