def rec_linear_sum(some_list):
    if(len(some_list) == 0):
        return 0
    return a[-1] + rec_linear_sum(a[:-1])
