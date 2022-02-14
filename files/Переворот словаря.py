def dict_flip(*args):
    ans = dict()
    for i in range(0, len(args), 2):
        ans[args[i + 1].decode('utf-8')] = args[i].decode('utf-8')
    return ans