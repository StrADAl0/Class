def func(*args, to_upper=True):
    ans = sorted(args)
    if(to_upper):
        for i in range(len(ans)):
            ans[i].upper()
    else:
        for i in range(len(ans)):
            ans[i].lower()
    return ans


print(*func('ttttt', 'fjfkfjkf', 'fjfjfjaae'))