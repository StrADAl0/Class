def recursive_len(a):
    if(not a):
        return []
    return [a[-1]] + recursive_len(a[:-1])


print(*recursive_len([1, 2, 3, 4]))