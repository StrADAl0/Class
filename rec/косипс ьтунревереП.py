def recursive_reverse(a):
    if(not a):
        return []
    return [a[-1]] + recursive_reverse(a[:-1])