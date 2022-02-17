def recursive_len(a):
    if(not a):
        return 0
    return recursive_len(a[1:]) + 1
